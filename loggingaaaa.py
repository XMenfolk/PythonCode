import loggingaaaa


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar(0)
    except StandardError, e:
        print 'hahhah'
        loggingaaaa.exception(e)


main()
print 'End'
