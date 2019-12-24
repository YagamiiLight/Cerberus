import re
import json
import time
from core.colors import red,green,purple,end
from core.auxiliary import chambering
from core.requester import requester
from data.payloads import waf_checker
from core.log import factory_logger,time




def check_waf(target, logger_type, proxy = None):

    if "=" not in target:
        print(f"{red}[!][{time}] Please provide a url with parameters! {end}")
        quit()


    # folder = Path.cwd().parent
    # waf_file = str(folder / "data/waf_signature")
    waf_file = "data/waf_signature"
    logger = factory_logger(logger_type,target,"Waf")


    with open(waf_file,'r') as loader:
        waf_data = json.load(loader)
        waf_match = {0: None}
        waf_info = {'company': None,
                    'waf_type': None,
                    'bypass_known': None}


        for intruder in waf_checker:
            try:
                target, payload = chambering(target, strike=True, payload=intruder)
                response = requester(target, payload, GET=True, timeout=5, proxy=proxy)
                print(f"{purple}[~][{time}] using {intruder} to detect WAF !{end}")


                if code >= 400 and not response is None:

                    match = 0
                    page, code, headers = response.text, response.status_code, response.headers

                    for waf_name, waf_signature in waf_data.items():

                        if re.search(waf_signature['regex'],page,re.I):
                            match = match + 1

                        if "code" in waf_signature:
                            if re.search(waf_signature['code'],code,re.I):
                                match = match + 1

                        if "header" in waf_signature:
                            if re.search(waf_signature["header"],headers,re.I):
                                match = match +1

                        if match > max(waf_match,key=waf_match.get):
                            waf_info['company'] = waf_name
                            waf_info['waf_type'] = waf_signature['name']
                            if 'bypass_known' not in waf_signature:
                                waf_info['bypass_known'] = None
                            else:
                                waf_info['bypass_known'] = waf_signature['bypass_known']
                            waf_match.clear()
                            waf_match[match] : waf_info
            except Exception:
                pass

        if max(waf_match,key=waf_match.get) > 0:
            logger.info(match)

        else:
            print(f"{green}[!][{time}] Waf Information : No firewall detected !{end}")


if __name__ == '__main__':

    check_waf("http://www.qq.com","StreamLogger")
