# coding: utf8
import requests
from datetime import date
from lxml import html
from smtplib import SMTP_SSL
from email.mime.text import MIMEText

# get time


def today():
    d = date.today()
    return str(d)
    pass

# getwebpage through requests


def requestwebpage(url):
    m = requests.get(url)
    mt = m.text.encode('latin-1')
    mt = mt.decode('utf-8')
    return mt
    pass


def main():
    # get all url
    '''
    a = 0
    for x in range(1, 15):
        if x == 1:
            num = '.shtml'
        else:
            a = a + 1
            num = '_' + str(a) + '.shtml'
        pass
    url = 'http://i.whut.edu.cn/xxtg/znbm/jwc/index' + num
    '''

    # only get the firstpage
    url = 'http://i.whut.edu.cn/xxtg/znbm/jwc/index.shtml'

    # use requests get imformation
    # use lxml build tree for get useful imformation
    maintree = html.fromstring(requestwebpage(url))
    newsdate = maintree.xpath('//ul[@class="normal_list2"]/li/strong/text()')
    links = maintree.xpath('//ul[@class="normal_list2"]/li/span/a/@href')
    news = maintree.xpath('//ul[@class="normal_list2"]/li/span/a/@title')

    # check the date and send email by qqmail
    b = 0
    for x in newsdate:
        if x == today():
            newsurl = links[b]
            newsurl = 'http://i.whut.edu.cn/xxtg/znbm/jwc' + newsurl[1:]

            newstree = html.fromstring(requestwebpage(newsurl))
            newstext = newstree.xpath(
                '//div[@class="TRS_Editor"]//span/text()')

            newscontent = ''
            for y in newstext:
                newscontent += y
                pass

            alltext = "<a href=\"http://i.whut.edu.cn/xxtg/znbm/jwc" + \
                str(links[b])[1:] + "\">" + news[b] + \
                "</a>" + newscontent

            # change the param to suit you !sendmail(sender, key, reciver,mailtitle, text)
            sendmail('666666@qq.com', '666666',
                     '666666',
                     x + news[b],
                     alltext)
            print(alltext)
            b += 1
            pass
        pass
    pass


def sendmail(sender, key, reciver, mailtitle, text):

    msg = MIMEText(text, 'html')
    msg["Subject"] = mailtitle
    msg["From"] = sender
    msg["To"] = reciver

    s = SMTP_SSL('smtp.qq.com', 465)
    s.login(sender, key)
    s.sendmail(sender, reciver, msg.as_string())
    s.quit()
    pass

main()
