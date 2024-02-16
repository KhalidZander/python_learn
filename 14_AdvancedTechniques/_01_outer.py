

def outer(logo):
    
    def inner(msg):
        print(f"<{logo}><{msg}><{logo}>")

    return inner

fn1 = outer("123")

fn1("zk")


def OutNum2(num1):
    
    def InNum2(num2):
        nonlocal num1
        num1 +=num2
        print(num1)
        
    return InNum2

fn2 = OutNum2(10)

fn2(100)

fn2(50)