import queue
from core import regex
from core.filter import Filter
from core.log import factory_logger
from core.requester import requester
from data.config import origin_proxies
from core.auxiliary import chambering
from urllib3.exceptions import ConnectTimeoutError


class Proxy:
    def __init__(self,target,logger_type):

        self.filter_proxy = set()
        self.container = queue.Queue()
        # self.logger = factory_logger("StreamLogger","qq.com","proxy_generator")
        self.logger = factory_logger(logger_type, target, "proxy_generator")
        # self.filter_proxy = Filter()

        self.dic = {
            'data5u' : regex.data5u,
            'xicidaili' : regex.xicidaili,
            'iphai' : regex.iphai,
            'xiladaili' : regex.xiladaili,
            'ip3366' : regex.ip3366,
            'ip_jiangxianli' : regex.jiangxianli,
            'ip_huan' : regex.ip_huan
        }

        self.list_name = ['data5u', 'xicidaili', 'iphai']
        # self.expansion = ['xiladaili']
        # self.count = 0

    def generator_proxies(self):

        for name in self.list_name:
            if name in self.dic:
                url,params = chambering(origin_proxies[name],strike=False)
                result = requester(url,params,GET=True,timeout=None)
                response = regex.Espace_eliminate.sub("",result.text)
                ips, ports, types = self.dic[name]['ip'].finditer(response),\
                                    self.dic[name]['port'].finditer(response),\
                                    self.dic[name]['type'].finditer(response)

                for i, j, k in zip(ips,ports,types):

                    ip = self.dic[name]['sub'].sub(" ", i.group())
                    port = self.dic[name]['sub'].sub(" ", j.group())
                    type = self.dic[name]['sub'].sub(" ", k.group())

                    # self.count = self.count+1

                    # print((ip, port, type))

                    if Filter.filter(ip,self.filter_proxy):
                        proxy = eval(regex.Espace_eliminate.sub("", str((ip, port, type.lower()))))
                        self.logger.info(f"ip : {proxy[0]} port : {proxy[1]} type : {proxy[2]}")
                        self.container.put(proxy)



    def proxy_xiladaili(self):
        url, params = chambering("http://www.xiladaili.com", strike=False)
        result = requester(url,params,GET=True,timeout=None)
        text = regex.Espace_eliminate.sub("",result.text)
        proxy_ips,proxy_types = self.dic['xiladaili']['ip'].finditer(text),\
                   self.dic['xiladaili']['type'].finditer(text)


        for ips, types in zip(proxy_ips,proxy_types):

            ip, type = self.dic['xiladaili']['sub'].sub(" ",ips.group()),\
                       self.dic['xiladaili']['sub'].sub(" ",types.group())
            pro = eval(regex.Espace_eliminate.sub("", str((ip,type.lower()))))
            proxy = (pro[0].split(":")[0],pro[0].split(":")[1],pro[1])
            self.logger.info(f"ip : {proxy[0]} port : {proxy[1]} type : {proxy[2]}")

            self.container.put(proxy)


    def proxy_ip3366(self):

        for page in range(1,11):
            try:
                url, params = chambering(f"http://www.ip3366.net/?stype=1&page={page}", strike=False)
                result = requester(url,params,GET=True,timeout=None)
                text = regex.Espace_eliminate.sub("",result.text)

                proxy_ips, proxy_ports, proxy_types = self.dic['ip3366']['ip'].finditer(text),\
                                                      self.dic['ip3366']['port'].finditer(text),\
                                                      self.dic['ip3366']['type'].finditer(text)

                for ips, ports, types in zip(proxy_ips, proxy_ports, proxy_types):

                    ip, port, type = self.dic['ip3366']['sub'].sub(" ",ips.group()),\
                                     self.dic['ip3366']['sub'].sub(" ",ports.group()),\
                                     self.dic['ip3366']['sub'].sub(" ",types.group())

                    proxy = eval(regex.Espace_eliminate.sub("", str((ip,port,type.lower()))))

                    self.logger.info(f"ip : {proxy[0]} port : {proxy[1]} type : {proxy[2]}")

                    self.container.put(proxy)
            except:
                pass

    def proxy_iphuan(self):
        url, params = chambering("https://ip.ihuan.me/", strike=False)

        url = requester("https://ip.ihuan.me/",params,GET=True,timeout=None)
        links = [link.group() for link in self.dic['ip_huan']['link'].finditer(url.text)]
        print(links)


        for i in range(len(links)):
            # print("".join(["https://ip.ihuan.me/",links[i]]))
            link = self.dic['ip_huan']['sub'].sub("",links[i])
            print(link)

            result = requester("".join(["https://ip.ihuan.me/",link]))
            text = regex.Espace_eliminate.sub("",result)
            proxy_ips, proxy_ports = self.dic['ip_huan']['ip'].finditer(text),\
                                     self.dic['ip_huan']['port'].finditer(text)

            for ips, ports in zip(proxy_ips,proxy_ports):
                ip, port, type = ips.group(),\
                                 self.dic['ip_huan']['sub'].sub(" ",ports),\
                                 "http"
                # print(ip)
                self.container.put((ip,port,type))


    def executor(self):
        self.proxy_ip3366()
        # self.proxy_xiladaili()
        self.generator_proxies()
        # self.proxy_iphuan()

        return self.container


    @staticmethod
    def check_live(proxy):
        check_ip = "http://httpbin.org/ip"
        ip = proxy[0]+":"+proxy[1]
        try:
            response = requester(check_ip, data = None, timeout = 3, GET = True, proxy = ip)
            if not response is None:

                if proxy[0] in response.text:
                    return True
                return False
            return False
        except ConnectTimeoutError:
            return False



if __name__ == '__main__':
    pro = Proxy("qq.com","StreamLogger")
    # pro.proxy_iphuan()
    prox = pro.executor()
