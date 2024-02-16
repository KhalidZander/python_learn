def outer(func):
    def inner():
        print("准备睡觉")
        func()
        print("睡着了")
    
    return inner

@outer
def sleep():
    import random
    import time
    print("准备中...")
    time.sleep(random.randint(1,5))

#常规写法
fn1 = outer(sleep)
fn1()


#语法糖写法
# sleep()
