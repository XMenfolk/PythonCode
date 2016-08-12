# coding=utf-8
import threading
import time

'''
由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线
程，Python 的 threading 模块有个 current_thread() 函数，它永远返回当前线程的实例。
主线程实例的名字叫 MainThread ，子线程的名字在创建时指定，我们用 LoopThread 命名子
线程。名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字 Python 就自动给线
程命名为 Thread‐1 ， Thread‐2 ……
'''
# 新线程执行的代码


def loop():
    print 'Thread11 %s is running... ' % threading.current_thread().name
    n = 0
    while n < 5:
        n += 1
        print 'Thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'Thread %s ended.' % threading.current_thread().name

print 'Thread %s is running...' % threading.current_thread().name

if __name__ == '__main__':
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print 'Thread %s ended.' % threading.current_thread().name
