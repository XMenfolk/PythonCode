# coding=utf-8


import poplib
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

# -----------通过POP3下载邮件----------
# 输入邮件地址, 口令和 POP3 服务器地址:
email = raw_input('Email: ')
password = raw_input('Password: ')
pop3_server = raw_input('POP3 server: ')

# 连接到 POP3 服务器:
server = poplib.POP3(pop3_server)

# 可以打开或关闭调试信息:
# server.set_debuglevel(1)

# 可选:打印 POP3 服务器的欢迎文字:
print(server.getwelcome())

# 身份认证:
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间:
print('Messages: %s. Size: %s' % server.stat())

# list()返回所有邮件的编号:
resp, mails, octets = server.list()

# 可以查看返回的列表类似['1 82923', '2 2184', ...]
print(mails)

# 获取最新一封邮件, 注意索引号从 1 开始:
index = len(mails)
resp, lines, octets = server.retr(index)

# lines 存储了邮件的原始文本的每一行,

# 可以获得整个邮件的原始文本:
msg_content = '\r\n'.join(lines)

# 稍后解析出邮件:
msg = Parser().parsestr(msg_content)

# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
# 关闭连接:
server.quit()

# ---------解析邮件-----------
# 将邮件内容解析为Message对象：
msg = Parser().parsestr(msg_content)


# 递归打印出Message对象的层次结构
# indent 用于缩进显示:
def print_info(msg, indent=0):
    if indent == 0:
        # 邮件的 From, To, Subject 存在于根对象上:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
        if value:
            if header == 'Subject':
                # 需要解码 Subject 字符串:
                value = decode_str(value)
            else:
                # 需要解码 Email 地址:
                hdr, addr = parseaddr(value)
                name = decode_str(hdr)
                value = u'%s <%s>' % (name, addr)
        print('%s%s: %s' % (' ' * indent, header, value))
    if (msg.is_multipart()):
        # 如果邮件对象是一个 MIMEMultipart,
        # get_payload()返回 list，包含所有的子对象:
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % (' ' * indent, n))
            print('%s--------------------' % (' ' * indent))
            # 递归打印每一个子对象:
            print_info(part, indent + 1)
    else:
        # 邮件对象不是一个 MIMEMultipart,
        # 就根据 content_type 判断:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            # 纯文本或 HTML 内容:
            content = msg.get_payload(decode=True)
            # 要检测文本编码:
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
                print('%sText: %s' % (' ' * indent, content + '...'))
        else:
            # 不是文本,作为附件处理:
            print('%sAttachment: %s' % (' ' * indent, content_type))


# 邮件的 Subject 或者 Email 中包含的名字都是经过编码后的 str，要正常显示，就必须 decode：
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


# 文本邮件的内容也是 str，还需要检测编码，否则，非 UTF-8 编码的邮件都无法正常显示：
def guess_charset(msg):
    # 先从 msg 对象获取编码:
    charset = msg.get_charset()
    if charset is None:
        # 如果获取不到，再从 Content-Type 字段获取:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset
