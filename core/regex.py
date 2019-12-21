import re
import requests
from data import config
from core.requester import requester

"""
file:///
dict://
sftp://
ldap://
tftp://
"""

Espace_eliminate = re.compile(r"\s+")

IP_REGEX = re.compile(r"(\d{1,3}\.){3}\d{1,3}?")

# URL_REGEX1 = re.compile(r"((http|https|ftp)|\s)://.+\.sina(\.com|\.cn).*\=.+?\" \b")

SEPARATE_PARAMS = re.compile(r"")

URL_REGEX = re.compile("(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')")

img = re.compile("(.*)<img (.*?) src=\"(.*?)img(.*?)\"(.*?)")


FILE_TYPE1 = re.compile(r".bmp|.css|.csv|.docx|.ico|.jpeg|.jpg|.js|.json|.pdf|.png|.svg|.xls|.xml|.gif"
                       r"|function()|javascript:|display:|float:|width:|position:|default:|type:|"
                       r"padding-right:|element:|border-right:|false:|null:")


FILE_TYPE = re.compile(r".bmp|.css|.csv|.docx|.ico|.jpeg|.jpg|.js|.json|.pdf|.png|.svg|.xls|.xml|.gif"
                       r"|function()|javascript:|<|>")
# URL_REGEX1 = re.compile(r"(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")

# URL_REGEX3 = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")

# URL_REGEX2 = re.compile(r'(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))')
# URL_REGEX = re.compile(r'(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')')

URL_PATH = re.compile(r"=\w+\b")

# type = re.compile(r"<li>http[s]+</li>")

# test2 = re.compile(r"http[s]?://(\w|[$-_@.&+=](sina))+")
#
# test = re.compile(r"http[s]?://(\w+\.sina(\.c(om|n))+)")
#
# test3 = re.compile(r"http[s]?://(\w+\.sina(\.c(om|n))).*=.+")


"""
    这里的正则表达式犯了一个很蠢的错误，没有必要再用正则'sub'规则清洗多余的杂质，
    因为finditer返回的也是match对象，利用分组group就可以正确提取，一开始弄错了，
    后来才意识到，我也懒得改了就这样吧，可能代码复杂度稍微要高一点吧。
"""

data5u = {'ip' : re.compile(r"<li>(\d{1,3}\.){3}\d{1,3}?</li>"),
          'port' : re.compile(r"<li class=\"port.+?\">\d+</li>",re.VERBOSE),
          'type': re.compile(r"<li>http[s]?</li>"),
          'sub' : re.compile(r"<([/]li)?.+?>",re.IGNORECASE)}


xicidaili = {'ip' : re.compile(r"<td>(\d{1,3}\.){3}\d{1,3}?</td>"),
             'port' : re.compile(r"<td>\d{1,5}</td>"),
             'type': re.compile(r"<td>http[s]?</td>",re.IGNORECASE),
             'sub' : re.compile(r"<([/]td)?.+?>",re.IGNORECASE)}


iphai = {'ip' : re.compile(r"(\d{1,3}\.){3}\d{1,3}?"),
         'port' : re.compile(r"<td>\d{1,5}</td>"),
         'type' : re.compile(r"<td>http[s]?</td>",re.IGNORECASE),
         'sub' : re.compile(r"<([/]td)?.+?>",re.IGNORECASE)}


xiladaili = {'ip' : re.compile(r"<td>(\d{1,3}\.){3}\d{1,3}:\d+?</td>"),
             'port' : re.compile(r":\d+?</td>"),
             'type' : re.compile(r"<td>http[s]?</td>",re.IGNORECASE),
             'sub' : re.compile(r"<([/]td)?.+?>",re.IGNORECASE)}


ip3366 = {'ip' : re.compile(r"<td>(\d{1,3}\.){3}\d{1,3}?</td>"),
          'port' : re.compile(r"<td>\d{1,5}</td>"),
          'type' : re.compile(r"<td>http[s]?</td>",re.IGNORECASE),
          'sub' : re.compile(r"<([/]td)?.+?>",re.IGNORECASE)}

jiangxianli = {'ip' : re.compile(r"<td>(\d{1,3}\.){3}\d{1,3}?</td>"),
               'port' : re.compile(r"<td>\d{1,5}</td>"),
               'type' : re.compile(r"<td>https[s]</td>",re.IGNORECASE),
               'sub' : re.compile(r"<([/]td)?.+?>",re.IGNORECASE)}

ip_huan = {'link': re.compile(r"\"\?page=.+?\""),
           'ip' : re.compile(r"(\d{1,3}\.){3}\d{1,3}?"),
           'port' : re.compile(r"<td>\d{1,5}</td>"),
           'sub' : re.compile(r"(<([/]td)?.+?>)|(\")")}

