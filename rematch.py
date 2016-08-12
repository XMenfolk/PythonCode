# coding=utf-8
import re
mail = raw_input("请输入邮箱：")
if re.match(r'[^\._-][\w\.-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+$', mail):
    print 'ok'
else:
    print '邮箱格式不正确，请重新输入！'
