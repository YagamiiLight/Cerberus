import queue
from data.payloads import Sql_injection,XSS,file_inclusion,command_injection,ssrf


class assault_pre:

    def __init__(self):
        self.SQLi = queue.Queue()
        self.XSS = queue.Queue()
        self.file_inclusion = queue.Queue()
        self.command_injection = queue.Queue()
        self.ssrf = queue.Queue()
        self.payload_category = dict()

    def payload_provide(self):
        for payload_list in Sql_injection.values():
            for payload in payload_list:
                self.SQLi.put(payload)

        for payload in XSS:
            self.XSS.put(payload)

        for payload in file_inclusion:
            self.file_inclusion.put(payload)

        for payload in command_injection:
            self.command_injection.put(payload)

        for payload in ssrf:
            self.ssrf.put(payload)


    def get_SQLipayload(self):
        if not self.SQLi.empty():
            return self.SQLi.get()
        return None

    def get_XSSpayload(self):
        if not self.XSS.empty():
            return self.XSS.get()
        return None

    def get_fileInclusion(self):
        if not self.file_inclusion.empty():
            return self.file_inclusion.get()
        return None

    def get_commandInjection(self):
        if not self.command_injection.empty():
            return self.command_injection.get()
        return None

    def get_ssrf(self):
        if not self.ssrf.empty():
            return self.ssrf.get()
        return None



    def get_payload_category(self):

        self.payload_category = {"SQLi" : (self.get_SQLipayload,self.SQLi),
                                 "XSS" : (self.get_XSSpayload,self.XSS),
                                 "file_inclusion" : (self.get_fileInclusion,self.file_inclusion),
                                 "command_injection" : (self.get_commandInjection,self.command_injection),
                                 "ssrf" : (self.get_ssrf,self.ssrf)
                                }

        return self.payload_category


