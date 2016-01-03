class Time:
    """it is time class"""

time = Time()
time.hour = 11
time.minute = 5
time.second = 14
def print_time(hour,minute,second):
    print('%.2d:%.2d:%.2d' % (hour,minute,second))
print_time(time.hour,time.minute,time.second)

def is_after(t1,t2):
    """"""

def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
    return sum
