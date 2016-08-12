def main():
    '''
    try:
        f = open('D:\MyTestFile\\testlog.txt', 'w')
    except IOError:
        print 'fail open file'
        return
    '''
    filepath = 'D:\MyTestFile\\testlog.txt'
    str = raw_input('input str:')+'\n'
    with open(filepath, 'w') as f:
        for i in range(10):
            f.write(str)
    f = open(filepath, 'r')
    print f.read()
    f.close()

if __name__ == '__main__':
    main()