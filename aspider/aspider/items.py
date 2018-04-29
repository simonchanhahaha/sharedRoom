# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from apartment.models import Apartment,ApartmentImg,Garden
from customAuth.models import Location
from scrapy_djangoitem import DjangoItem
class AspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # image_urls = scrapy.Field()
    # images = scrapy.Field()
    apartment = scrapy.Field()
    garden = scrapy.Field()

class ApartmentItem(DjangoItem):
    django_model = Apartment

class ApartmentImgItem(DjangoItem):
    django_model = ApartmentImg

class LocationItem(DjangoItem):
    django_model = Location

class GardenItem(DjangoItem):
    django_model = Garden