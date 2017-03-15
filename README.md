# WHUT_JWC_NOTICE
get WHUT JWC NOTICE 获取武汉理工大教务处公告并发送邮件通知

通过QQ邮箱  //可修改sendmail函数修改

Usage：
修改72行sendmail函数的参数即可
sendmail(sender, key, reciver, mailtitle, text)
sender:发送者的邮箱
key:邮箱授权码
reciver:邮件接受者

Depend:
requests http://docs.python-requests.org/en/master/
smtplib https://docs.python.org/3.6/library/smtplib.html
lxml http://lxml.de/tutorial.html
