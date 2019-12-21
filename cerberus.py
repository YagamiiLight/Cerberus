import time
import argparse
from core.banner import show_banner



show_banner()

time = time.strftime('%H:%M:%S')

parser = argparse.ArgumentParser()

parser.add_argument('-target', nargs='+', dest='target')
parser.add_argument('-thread', nargs='?', default=7, type=int, dest='thread')
parser.add_argument('-proxy', dest='proxy',action="store_true")
parser.add_argument('-waf',dest='waf',action="store_true")
parser.add_argument('-outfile',nargs='?',dest='outfile')
parser.add_argument('-mail', nargs='?', dest='mail')
parser.add_argument('-subdomains',dest='subdomains',action = "store_true")
parser.add_argument('-file', nargs='?', dest='file')
parser.add_argument('-detectMid', dest='detectmid', action='store_true')
parser.add_argument('-middleware', nargs='?', dest='middleware')
parser.add_argument("--account", nargs = '?',dest = 'account')
parser.add_argument("--password", nargs = '?', dest = 'password')



args = parser.parse_args()


mail = args.mail
waf = args.waf
file = args.file
target = args.target
detectmid = args.detectmid
middleware = args.middleware
subdomains = args.subdomains
proxy = args.proxy or None
threads = args.thread or 7
outfile = args.outfile
account = args.account
password = args.password



from core.proxies import Proxy
from strike.attack import Attack
from core.colors import red,green,end
from core.subdomain import subdomain
from core.middleware import detect_info
from strike.detect_waf import check_waf
from core.Quicksilver import quicksliver
from strike.Poc.poc_Attack import middleware_vulne
from core.auxiliary import convert_target,get_proxy,load_queue



file_= None
subdomain_queue = None



if file:
    file_= str(file)


if target:
    target = convert_target(target[0])



logger_type = "StreamLogger"


if outfile:
    logger_type = "FileLogger"


if mail:
    logger_type = "STMPLogger"
    if account and password:
        account = account
        password = password
    else:
        print(f"{green}[!]{time} Need to provide account and password to login STMP email server{end}")
        quit()


if subdomains:
    sub = subdomain(target, file = "DNSPod.txt", logger_type = logger_type)
    subdomain_set = sub.execution()
    subdomain_queue = load_queue(subdomain_set)



if detectmid:
    middleware_info = detect_info(target,logger_type)
    middleware_vulne(url=target,logger_type = logger_type,middleware_info=middleware_info)


if middleware:
    vulne = middleware_vulne(target,logger_type,middleware_type = middleware)
    vulne.analyse()


if proxy:
    proxies = Proxy(target,logger_type)
    proxy_queue = proxies.executor()



if waf:
    if proxy:
        proxy = get_proxy(proxy_queue)
        check_waf(target, logger_type, proxy = proxy)
    else:
        check_waf(target, logger_type)



module_attack = Attack(target,logger_type,subdomain_queue = subdomain_queue,file = file_)
execution = module_attack.execution
quicksliver(execution,threads)
print(f"{red}[!!][{time}] Vulnerability scan has finished !{end}")







