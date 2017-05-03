# coding:utf-8
import requests
import re
import urllib2
import urllib
import selenium
import cookielib


def get_cookies():
    open_page_for_cookie = urllib2.urlopen('http://172.16.47.84/')
    cookie = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    # response = opener.open('http://172.16.47.84/')
    # print response

    return opener


def get_state(html_text):
    viewstate = re.findall('__VIEWSTATE" value="(.*?)"', html_text, re.S)
    return viewstate[0]


def get_eventval(html_text):
    eventval = re.findall('EVENTVALIDATION" value="(.*?)"', html_text, re.S)
    return eventval[0]


def make_post_data(username, password, state, eventval):
    post_data = {
        'ScriptManager1': 'UpdatePanel1|Button1',
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': state,
        '__EVENTVALIDATION': eventval,
        'TextBox1': username,
        'TextBox2': password,
        '__ASYNCPOST': 'true',
        'Button1': '登      录'
    }
    return post_data


def step_1():
    start_url = 'http://172.16.47.84/'
    login_url = 'http://172.16.47.84/Login.aspx'
    opener = get_cookies()
    # open_page_for_cookie = urllib2.urlopen(start_url)
    open_page_for_cookie = urllib2.urlopen('http://172.16.47.84/')

    headers = {'Host': '172.16.47.84',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/57.0.2987.133 Safari/537.36',
               'Referer': 'http://172.16.47.84/Login.aspx',
               'Origin': 'http://172.16.47.84',
               'Connection': 'keep-alive'
               }

    response = requests.get(start_url)
    html_text = response.text

    viewstate = get_state(html_text)
    eventval = get_eventval(html_text)

    # print viewstate
    # print eventval
    post_data = make_post_data('2014021072', '509271', viewstate, eventval)
    postdata = urllib.urlencode(post_data)
    # test = opener.open(login_url, postdata)
    # test = opener.open('http://172.16.47.84/index.aspx')
    # print test.read()

    # session = requests.session()
    # ttt = session.post(login_url, data=post_data, headers=headers)
    # print ttt.content
    # f = ttt.get('http://172.16.47.84/index.aspx', headers=headers)
    # print f.content
    # print postdata

    # ---------------------------------------------------------------------
    s = requests.Session()
    r2 = s.post(login_url, headers=headers, data=postdata)
    #print r2.text
    # ---------------------------------------------------------------------
    """request = urllib2.Request(login_url, postdata, headers)
    login_response = urllib2.urlopen(request)
    login_html_text = login_response.read()
    """
    temp = s.get('http://172.16.47.84/DayNavigation.aspx')
    print temp.text
    # print login_html_text

    # # response2 = requests.get('http://172.16.47.84/DayNavigation.aspx')
    # # html_text2 = response2.text
    # # # print html_text2
    # #
    # # response3 = requests.get('http://172.16.47.84/index.aspx')
    # # html_text3 = response3.text
    # print login_html_text
step_1()