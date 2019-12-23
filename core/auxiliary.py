import re
import queue
from difflib import SequenceMatcher
from core.requester import requester
from core.colors import red,green,end
from core.log import factory_logger,time
from urllib3.exceptions import ConnectTimeoutError





def chambering(url,strike,payload = None,type = None):

    if "=" in url:
        data = url.split("?")[1].split("&")
        params_extractor = tuple((i.split('=')[0],i.split('=')[1]) for i in data)
        params = {i:j for i, j in params_extractor}
        url = url.split('?')[0]

        if strike and payload != None:
            if type == "SQLi":
                incursive = {key: "".join([params[key], payload]) for key in params.keys()}

            if type in ["XSS","file_inclusion","command_injection","ssrf"]:
                incursive = {key: payload for key in params.keys()}
            return (url,incursive)

        else:
            return (url,params)
    else:
        return (url,None)


def receive_check(original,payloaded,type,payload = None):
    lower_limit = 0.95

    if type == "SQLi" or type == "file_inclusion" or type == "command_injection":
        sequenceMatcher = SequenceMatcher(None)
        sequenceMatcher.set_seq1(original)
        sequenceMatcher.set_seq2(payloaded)
        ratio = sequenceMatcher.quick_ratio()
        if ratio < lower_limit:
            return True
        else:
            return False

    elif type == "XSS":

        if re.search(payload,payloaded,re.I):
            return True
        else:
            return False


def check_live(proxy):
    check_ip = "http://httpbin.org/ip"
    ip = proxy[0] + ":" + proxy[1]
    try:
        response = requester(check_ip, data=None, timeout=3, GET=True, proxy=ip)
        if not response is None:
            if proxy[0] in response.text:
                return True
            return False
        return False
    except ConnectTimeoutError:
        return False


def get_proxy(proxy_queue):
    proxy = proxy_queue.get()
    while not proxy_queue.empty():

        if check_live(proxy):
            print(f"{red}[!][{time}]{proxy[0]} is alive and testing with it !{end}")
            return proxy[0]
        else:
            print(f"{green}[!][{time}]{proxy[0]} is dead !{end}")
            proxy = proxy_queue.get()
    print(f"{red}[!][{time}] No more No available proxy{end}")
    return None



def vul_message(vul,url,payload):

    message = {
        "SQLi" : "SQL injection vulnerability has already been detected",
        "file_inclusion" : "File Inclusion vulnerability has already been detected",
        "command_injection" : "Command Injection vulnerability has already been detected",
        "ssrf" : "SSRF vulnerability has already been detected"
    }

    message_box = f"-------------------------------------------\n" \
                  f"url : {url}\n"\
                  f"payload : {payload}\n" \
                  f"{message[vul]}\n" \
                  f"--------------------------------------------\n"

    return message_box



def convert_target(url):
    if url.lower().startswith("http"):
        return url
    elif url.lower().startswith("/"):
        return "http:/" + url
    else:
        return "http://"+url



def extract_domain(target):
    if not target is None:
        domain = target.split(".")[1]
        return domain
    return None



def file_handler(file):
    domains = queue.Queue()
    with open(file,'r',buffering=1024) as handler:
        for i in handler:
            url = convert_target(i)
            domains.put(url)
    return domains


def error_check(page):
    if re.search("404",page):
        return False
    return True


def load_queue(subdomain):
    subdomain_queue = queue.Queue()
    for i in subdomain:
        url = "http://"+i
        subdomain_queue.put(url)
    return subdomain_queue




