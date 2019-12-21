import queue
import hashlib
from collections import Iterable
from core.log import time,factory_logger
from core.colors import green,end,purple
from core.auxiliary import convert_target
from core.regex import FILE_TYPE,URL_PATH


class Filter:

    def __init__(self,data,type,container):
        self.data = data
        self.type = type
        # self.md5 = hashlib.md5()
        self.contain_md5 = set()
        self.contain_target = queue.Queue()
        self.container = container



    @classmethod
    def filter(self,item,container):
        if FILE_TYPE.search(item) is None:
            md5 = hashlib.md5()
            md5.update(item.encode('utf-8'))
            if md5.hexdigest() not in container:
                container.add(md5.hexdigest())
                # print(item)
                return True
        return False


    # @staticmethod
    def extractor(self,logger_type,target):
        try:
            if isinstance(self.data,Iterable):
                for items in self.data:
                    item = items.group()

                    if self.type == "proxy":
                        if self.filter(item,self.container):
                            self.contain_target.put(item)

                    elif self.type == "url":
                        filted_url = URL_PATH.sub("=",item)
                        if self.filter(filted_url,self.container):
                            url = convert_target(item)
                            # # url = "http:/"+item
                            # logger = factory_logger(logger_type,target,"url")
                            # logger.info(url)
                            print(f"{purple}[~][{time}] Collecting a target for testing : {url}{end}")
                            self.contain_target.put(url)
                return self.contain_target
        except Exception as e:
            return e

