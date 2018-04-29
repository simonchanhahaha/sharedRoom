# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import scrapy
from scrapy.pipelines.images import ImagesPipeline
class AspiderPipeline(object):
    def __init__(self):
        self.filename = open('anjuke.json', 'w')

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + ",\n"

        self.filename.write(text)

        return item

    def close_spider(self, spider):
        self.filename.close()

class PicPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]  # ok判断是否下载成功
        # if not image_paths:
        #     raise DropItem("Item contains no images")
        # # item['image_paths'] = image_paths
        return item
