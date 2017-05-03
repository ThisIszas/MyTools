import urllib2
import urllib
import cookielib


def get_cookies():
    cj = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)


def step_1():
    get_cookies()
    start_url = 'http://172.20.124.12:8081/ibillingportal'
    open_page_for_cookie = urllib2.urlopen(start_url)
    post_url = 'http://172.20.124.12:8081/ibillingportal/LoginAction_login.do'

    headers = {'Host': '172.20.124.12:8081',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/55.0.2883.87 Safari/537.36',
               'Referer': 'http://172.20.124.12:8081/ibillingportal/wx/renew_pre.jsp?op=modifypwd'
               }
    post_data = {
        'loginName': 'jt20140210610',  # you should write your username here.
        'loginPwd': 'hiavril.520',  # you should write your password here.
        'vmode': "1",
        'verfiyCode': "",
        'queryString': ""
    }

    postdata = urllib.urlencode(post_data)

    request = urllib2.Request(post_url, postdata, headers)
    response = urllib2.urlopen(request)
    print response.read()

if __name__ == '__main__':
    step_1()