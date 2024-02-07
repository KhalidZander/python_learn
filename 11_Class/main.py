from student import Student
from Clock import Clock
from iPhone import iPhone
from iPhone15 import iPhone15
from typing import Union

def func(data:Union[int,str]) ->str:
    return f"{data}"

if __name__ == "__main__":

    student1 = Student("zs","n",15)
    student1.name = "zs"
    student1.age = 15
    student1.gender = "nv"

    # student1.introdunce()
    
    student2 = Student("ls","n",20)
    
    student3 = Student("ww","n",20)
    
    if student1>student2:
        student1.introdunce()
    else:
        student2.introdunce()
    
    iphone5 = iPhone(True)
    iphone5.call_by_5g()
    
    iphone15 = iPhone15(True)
    
    iphone15.call_by_5g()
    # Clock(1,1).ring()
    
    #使用Union限制范围
    dic = dict[str,Union[int,str]]
    
    # 此时ide会显示需要输入的范围 （非强制性）
    # 输入 str/int 输出 str
    func()
    
