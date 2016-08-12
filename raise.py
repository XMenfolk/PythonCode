def foo(s):
    n = int(s)
    return 10 / n

def bar(s):
    try:

        return foo(s) * 2
    except StandardError, e:
        print 'Error'

    #raise
    raise ValueError('Input Error!')

def main():
    bar('0')

main()