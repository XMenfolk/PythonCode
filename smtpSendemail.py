# coding=utf-8


from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


# 格式化一个邮件地址。注意不能简单地传入 name <addr @ example.com > ，因为如果包含中文，需要通过Header对象进行编码

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr
    ))


# 输入Email 地址和口令：
from_addr = raw_input('发件人邮箱地址：')
passworld = raw_input('请输入邮箱密码：')

# 输入SMTP服务器地址：
smtp_server = raw_input('SMTP服务器地址：')

# 输入收件人邮箱地址：
to_addr = raw_input('收件人邮箱地址：')

# 构造纯文本邮件:
# msg = MIMEText('Hello World! Send by python...', 'plain', 'utf-8')

# 构造HTML邮件：
msg = MIMEText('<html><body><h1>Hello World!</h1>' +
               '<p>Send by <a href="http://www.python.org">Python</a>...</p>' +
               '</body></html>', 'html', 'utf-8')

# 将发件人、收件人、邮件主题 添加到MIMEText中
msg['发件人邮箱地址'] = _format_addr(u'Python 爱好者<%s>' % from_addr)
msg['收件人邮箱地址'] = _format_addr(u'管理员<%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候......', 'utf-8').encode()

# 通过SMTP发送：
server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, passworld)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
