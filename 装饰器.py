#装饰器就是函数闭包的一种应用
import time
def debug(func):
    def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
        start = time.time()
        func(*args, **kwargs)
        print(time.time()-start)
    return wrapper  # 返回

@debug
def say(something):
    time.sleep(1)
    print ("hello {}!".format(something))

say(123)