"""
try:
    print 'try...'
    r = 10 / 0
    print 'result:', r
except ZeroDivisionError, e:
    print 'except:', e
finally:
    print 'finally...'
print 'End'
"""


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar(0)
    except StandardError, e:
        print "Error!"
    
    finally:
        print 'finally'

if __name__ == '__main__':
    main()
