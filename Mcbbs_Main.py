import requests
import re
import datetime
import time


def get_session(Cookies):
    Tempdit = {}
    for line in Cookies.split(';'):
        name, value = line.strip().split('=', 1)
        Tempdit[name] = value
    session.cookies = requests.utils.cookiejar_from_dict(Tempdit)


def get_centerTxt(str,beforestr,afterstr):
    Regex= re.compile(beforestr+'(.*?)'+afterstr,re.S)
    txt= Regex.findall(str)
    return txt[0]

def get_formhash():
    params={
     'id':'dc_signin:sign',
     'infloat':'yes',
     'handlekey':'sign',
     'inajax':'1',
    'ajaxtarget':'fwin_content_sign'
    }
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    response = session.get('http://www.mcbbs.net/plugin.php',params=params,headers=headers)
    try:
        fromhash = get_centerTxt(response.text,'name="formhash" value="','"')
    except Exception as e:
        print(e)
        print('此账号签到过')
        return '12345'
    return fromhash


def post_sign(fromhash):
    params = {
        'id':'dc_signin:sign',
        'inajax':'1'
    }
    data = {
        'formhash':fromhash,
        'signsubmit':'yes',
        'handlekey':'signin',
        'emotid':'1',
        'content':'记上一笔，hold住我的快乐！'
    }
    session.post('http://www.mcbbs.net/plugin.php',params=params,data=data)



if __name__ == '__main__':
    my_set_time='13-10'
    Cookieslist=[
        'UM_distinctid=166072b4d4525c-0cc51b6980b12e-454c092b-1fa400-166072b4d4661a; CNZZDATA4434322=cnzz_eid%3D87272129-1537716948-%26ntime%3D1539515896; Hm_lvt_affdf09dddabcdf2d681acefa474b973=1539958815,1540090755,1540099888,1540360343; ZxYQ_2132_pc_size_c=0; ZxYQ_2132_sid=QnVdc0; ZxYQ_2132_saltkey=ABr5BWBe; ZxYQ_2132_lastvisit=1540379209; ZxYQ_2132_sendmail=1; ZxYQ_2132_noticeTitle=1; ZxYQ_2132_ulastactivity=38ccLE0hgNfmlQNGfp3vJGF6c9RFGC%2FaNIaJC8x6PFfLn5VQf%2Fqu; ZxYQ_2132_auth=2370LdLC6s6%2B1NYxXGDGtqwATxvIxSaph1mVhqs4RBWkKM5tDGyo9fn72NNE0CBkVCzjHVJwUyxqiv8QujhmBas%2FnVN1; ZxYQ_2132_lastcheckfeed=2576782%7C1540382950; ZxYQ_2132_checkfollow=1; ZxYQ_2132_lip=171.43.214.25%2C1535005289; ZxYQ_2132_checkpm=1; Hm_lpvt_affdf09dddabcdf2d681acefa474b973=1540382842; ZxYQ_2132_lastact=1540382955%09misc.php%09patch'
    ]
    while True:
        newtime = datetime.datetime.now().strftime('%H-%M')
        print('当前时间为:%s,我设置的时间为%s'%(newtime,my_set_time))
        if newtime==my_set_time:
            for usercookie in Cookieslist:
                session = requests.session()
                get_session(usercookie)
                post_sign(get_formhash())
                session.close()
            time.sleep(60)
        time.sleep(30)
