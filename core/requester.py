import logging
from data import config
from random import choice

try:
    import requests
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
except ImportError:
    print("Need to install requests")
    quit()

from urllib3.exceptions import (
     ProtocolError,
     ResponseError,
     ConnectTimeoutError,
)

# session = requests.session()
def requester(url,data,GET,timeout = None,cookie = None,proxy = None):


    headers = {
        'Accept' : '*/*',
        'Accept-Encoding' : '*',
        'Connection':'close',
        'Referer' : choice(config.Referer),
        'User-Agent':choice(config.User_agents)
    }
    GET, POST = (True, False) if GET else (False,True)

    try:
        # proxie = {'http' : '127.0.0.1:8080'}

        proxy = \
            {
                "http" : proxy
            }

        if GET:

            # with requests.session() as request:
            response = requests.get\
                    (
                        url,
                        params = data,
                        cookies = cookie,
                        verify = False,
                        timeout = timeout,
                        stream = True,
                        headers = headers,
                        proxies = proxy
                    )
            # response.encoding = 'utf-8'

        else:
            response = requests.post\
                    (
                         url,
                         data = data,
                         headers=headers,
                         timeout=timeout,
                         files = None,
                         verify = False,
                         proxies = None
                    )

        response.encoding = 'utf-8'

        return response

    except (ProtocolError,ResponseError,ConnectTimeoutError):
        logging.warning("WAF")
    except Exception:
        pass



if __name__ == '__main__':
    result = requester("http://httpbin.org/ip",data = None,GET = True)
    print(result.text)




