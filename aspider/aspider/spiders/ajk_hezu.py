# -*- coding: utf-8 -*-

import sys
import os
import django
sys.path.append(os.getcwd())
sys.path.append('/Users/Simonchan/Desktop/workspaces/SharedRoom/sharedRoom')  # 具体路径
os.environ['DJANGO_SETTINGS_MODULE']='sharedRoom.settings'
django.setup()

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from aspider.items import GardenItem,ApartmentImgItem,ApartmentItem,AspiderItem
from customAuth.models import Location
from django.contrib.auth.models import User
from apartment.models import Garden,Apartment
class AnjukeSpider(CrawlSpider):
    name = 'ajk_hezu'
    allowed_domains = ['anjuke.com']
    start_urls = ['https://sz.zu.anjuke.com/fangyuan/p2-x2/']

    rules = (
        Rule(LinkExtractor(allow=r'/fangyuan/p(\d+)-x2/'), follow=True),
        Rule(LinkExtractor(allow=r'/fangyuan/(\d+)'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        try:

            location_name = response.xpath("//li/a[@class='link']/text()").extract()[1]
            location = Location.objects.filter(province__contains=location_name).first()
            if location is None:
                location_name = response.xpath("//li/a[@class='link']/text()").extract()[2]
                location = Location.objects.filter(province__contains=location_name).first()

            garden_name = response.xpath("//li/a[@class='link']/text()").extract()[0]
            garden_obj = Garden.objects.filter(name=garden_name)
            if len(garden_obj)!=0:
                garden=garden_obj.first()
            else:
                garden = GardenItem()

                garden['name'] = garden_name
                garden['location_id'] = location
                garden['company'] = '本小区物业管理公司'
                garden.save()

            new_garden_obj = Garden.objects.filter(name=garden_name).first()

            house_info = response.xpath("//ul[@class='house-info-zufang cf']")

            apartment = ApartmentItem()
            apartment['name'] = response.xpath("//h3[@class='house-title']/text()").extract()[0]
            apartment['rent_type'] = 0
            apartment['size'] = house_info.re('(\d+)平方米')[0]

            structure = house_info.re("(\d+)室(\d+)厅(\d+)卫")
            apartment['room'] = structure[0]
            apartment['hall'] = structure[1]
            apartment['bathroom'] = structure[2]

            apartment['floor'] = house_info.re("共(\d+)层")[0]
            apartment['has_furniture'] = 1
            apartment['requirement'] = house_info.xpath("//li[9]/span[@class='info']/text()").extract()[0]
            decor = response.xpath("//ul[1]/li[6]/span[2]/text()").extract()[0]
            if decor == '毛坯':
                decoration = 1
            elif decor == '简单装修':
                decoration = 2
            elif decor == '中等装修':
                decoration = 3
            elif decor == '精装修':
                decoration = 4
            elif decor == '豪华装修':
                decoration = 5
            else:
                decoration = 6

            apartment['decoration_type'] = decoration

            apartment['price'] = response.xpath("//span[@class='price']/em/text()").extract()[0]

            pay = response.xpath("//li[@class='full-line cf']/span[@class='type']/text()").extract()[0]

            if pay == '付1押1':
                payment = 1
            elif pay == '付1押2':
                payment = 2
            elif pay == '付3押1':
                payment = 3
            elif pay == '半年付':
                payment = 4
            elif pay == '年付':
                payment = 5
            else:
                payment = 6
            apartment['payment_type'] = payment

            forward_tmp = response.xpath("//ul[1]/li[4]/span[2]/text()")
            if len(forward_tmp) != 0:
                f = forward_tmp.re('朝(\S+)')

                if len(f) != 0:
                    f_tmp = f[0]
                else:
                    f_tmp = forward_tmp.extract()[0]

                if f_tmp == '东':
                    forward = 0
                elif f_tmp == '南':
                    forward = 1
                elif f_tmp == '西':
                    forward = 2
                elif f_tmp == '北':
                    forward = 3
                elif f_tmp == '东北':
                    forward = 4
                elif f_tmp == '西北':
                    forward = 5
                elif f_tmp == '东南':
                    forward = 6
                elif f_tmp == '西南':
                    forward = 7
                else:
                    forward = 8

                apartment['forward'] = forward

            else:
                apartment['forward'] = 8

            description = ''
            desc = response.xpath("//div[@class='auto-general']//text()").extract()
            for d in desc:
                description += d + '\n'
            apartment['description'] = description

            apartment['user_id'] = User.objects.filter(id=4).first()
            apartment['is_rent'] = 0



            apartment['garden_id'] = new_garden_obj
            apartment.save()
            new_apartment_obj = Apartment.objects.filter(name=apartment['name']).filter(garden_id=new_garden_obj.id).first()
            apartment_img = ApartmentImgItem()

            # apartment_img.img = response.xpath(
            #     "//div[@id='room_pic_wrap']/div[@class='img_wrap'][1]/img/@src").extract()
            apartment_img['img'] = 'apartment/default.jpeg'
            apartment_img['apartment'] = new_apartment_obj
            apartment_img.save()

            item = AspiderItem()
            item['apartment']=apartment
            item['garden']=new_garden_obj
            # item['img_urls'] = response.xpath("//div[@id='room_pic_wrap']/div[@class='img_wrap'][1]/img/@src").extract()
            yield apartment
        except Exception as e:
            print(e)


