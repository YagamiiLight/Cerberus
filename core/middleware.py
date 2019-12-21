import zlib
import json
import requests
from core.requester import requester
from core.auxiliary import chambering
from core.log import factory_logger,time
from core.colors import red,end



def detect_info(target,logger_type):

    logger_middle = factory_logger(logger_type, target, "middleware")
    print(f"{red}[!][{time}] Collecting middleware information....{end}")

    info = {

            'Waf': None,
            'CDN' : None,
            'CMS' : None,
            'Web Servers': None,
            'Web Frameworks': None,
            'Operating Systems' : None,
            'JavaScript Frameworks': None,
            'Programming Languages': None

            }

    keys = [
            'Waf','CDN','Web Servers',
            'Web Frameworks','Operating Systems',
            'JavaScript Frameworks',
            'Programming Languages'
            ]


    url, data = chambering(target, strike = False)

    try:
        response = requester(url, data, GET = True)
        whatweb_dict = {"url": response.url, "text": response.text, "headers": dict(response.headers)}
        whatweb_dict = json.dumps(whatweb_dict)
        whatweb_dict = whatweb_dict.encode()
        whatweb_dict = zlib.compress(whatweb_dict)
        data = {"info": whatweb_dict}

        result = requests.post("http://whatweb.bugscaner.com/api.go", files = data)
        data_json = result.json()
        data = dict(data_json)


    except Exception:
        pass


    if 'error' not in data:
        for key in keys:
            if key in dict(data):
                info[key] = data[key]
        logger_middle.info(info)
        return info


    else :

        info.clear()
        info['message'] = "Error Message!"
        logger_middle.info(info)

    # return info


if __name__ == '__main__':
    # logger = factory_logger
    logger_type= "StreamLogger"
    # target = "qq"

    url = "http://www.zctt.com"
    u = "http://www.baidu.com"
    detect_info(url,logger_type)



