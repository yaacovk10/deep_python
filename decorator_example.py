import datetime

    

def exec_time(func):
    t1 = datetime.datetime.now()
    result = func(*args)
    t2 = datetime.datetime.now()
    print('Function', func.__name__, 'time:', round((t2 -t1)*1000,1), 'ms')

@exec_time
def c_funct(num):
    return [num*2 for x in range(10)]

c_funct(5)