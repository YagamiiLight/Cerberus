# Cerberus

一款功能强大的漏洞扫描器，子域名爆破使用aioDNS，asyncio异步快速扫描，覆盖目标全方位资产进行批量漏洞扫描，中间件信息收集，自动收集ip代理，探测Waf信息时自动使用来保护本机真实Ip，在本机Ip被Waf杀死后，自动切换代理Ip进行扫描，Waf信息收集(国内外100+款waf信息)包括安全狗，云锁，阿里云，云盾，腾讯云等，提供部分已知waf bypass 方案，中间件漏洞检测(Thinkphp,weblogic等 CVE-2018-5955,CVE-2018-12613,CVE-2018-11759等)，支持SQL注入, XSS, 命令执行,文件包含, ssrf 漏洞扫描, 支持自定义漏洞邮箱推送功能

[![asciicast](https://asciinema.org/a/289717.svg)](https://asciinema.org/a/289717)


## 主要功能

- :smiling_imp:单url漏洞扫描

  支持SQL注入, XSS, 命令执行,文件包含, ssrf

  进行单站点漏洞扫描

  `python3 cerberus.py -target www.qq.com`
  
  [![asciicast](https://asciinema.org/a/6fOJu4DkVhMGutLeIGmwE7Ppi.svg)](https://asciinema.org/a/6fOJu4DkVhMGutLeIGmwE7Ppi)
  
- :cherry_blossom: 线程设置

  多线程，默认7线程
  
  `python3 cerberus.py -target www.qq.com -thread 7`


- :imp:子域名异步批量扫描

  使用aioDNS，asyncio异步，子域名爆破后，加入扫描队列，覆盖目标全方位资产进行批量漏洞扫描

  `python3 cerberus.py -target www.qq.com -subdomain`
  
  [![asciicast](https://asciinema.org/a/n8zwz58eOkqH8JNZAi85opa61.svg)](https://asciinema.org/a/n8zwz58eOkqH8JNZAi85opa61)


- :skull: 代理IP收集

  爬取了9个站点的实时免费代理IP，但IP存活率较低，大概在20%左右，检测IP是否存活的过程中可能会阻塞扫描过程。

  - www.data5u.com
  - www.xicidaili.com
  - www.goubanjia.com
  - www.ip3366.net
  - www.iphai.com
  - cn-proxy.com
  - ip.jiangxianli.com
  - www.xiladaili.com
  - ip.ihuan.me

  `python3 cerberus.py -target www.qq.com -proxy`
  
  [![asciicast](https://asciinema.org/a/p4A6ZhN5kCKIzlXZbdApltgNe.svg)](https://asciinema.org/a/p4A6ZhN5kCKIzlXZbdApltgNe)
  
- :japanese_ogre:Waf信息收集

  国内外100+款waf信息,强大的指纹库，包括安全狗，云锁，阿里云，云盾，腾讯云等，提供部分已知waf bypass 方案
  
  请务必提供带有参数的URL进行WAF测试！
  
  `python3 cerberus.py -target https://open.weixin.qq.com/frame?t=home/web_tmpl&lang=zh_CN -waf`

- :see_no_evil:中间件信息收集

  信息收集完毕后，根据获取结果，自动进行中间件漏洞扫描

  - WAF
  
  - CDN
  
  - CMS
  
  - Web Servers
  
  - Web Frameworks
  
  - Operating Systems
  
  `python3 cerberus.py -target -detectMid`
  
  [![asciicast](https://asciinema.org/a/mQ6qLc98J87Srpf7nGq8MakdP.svg)](https://asciinema.org/a/mQ6qLc98J87Srpf7nGq8MakdP)
  
- :panda_face: 指定中间件漏洞扫描

  如果已知目标部分中间件信息，可以指定类型，直接进行扫描
  
  - Thinkphp CVE-2018-5955
  
  - Phpmyadmain CVE-2018-12613
  
  - Dedecms
  
  - Tomcat CVE-2018-11759
  
  - Weblogic
  
  - Wordpress
  
  `python3 cerberus.py -target www.qq.com -midlleware weblogic`
  
  
  
- :trollface: 输入文件批量扫描

  - 文件路径需为绝对路径
  
  - 需为txt文本格式，确保每一行只有一个域名
  
  `python3 cerberus.py -file absolute path`

- :cookie: 设置Cookie
  
  `python3 cerberus.py -cookie cookie`

- :speak_no_evil: 输出漏洞扫描报告

  `python3 cerberus.py -outfile`
  
  

## :rabbit: Praise me!

   - :kissing_cat: 如果您认为本项目对您有一定帮助，为了更好的开源安全工具！请赞赏我！感谢您的赞赏！

   ![praise](https://github.com/YagamiiLight/Cerberus/blob/master/images/praise.jpg)

## 声明

本项目仅供学习交流，使用本工具所造成的任何违法后果，与本人无关！！


  



  
  
  

