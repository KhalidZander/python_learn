
class Student:
    # 在此定义成员变量
    name = None
    gender = None
    age = None
    
    # 构造函数
    def __init__(self):
        return
    
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age    
    
    # 魔术方法 ToString
    def __str__(self):
        return f"Name:{self.name} Gender:{self.gender} Age:{self.age}"

    # 魔术方法 比大小(不能相等)
    def __lt__(self,other):
        return self.age <other.age
        
    # 魔术方法 是否大于（小于）等于    
    def __le__(self,other):
        return self.age <=other.age
        
    # 魔术方法 是否相等
    def __eq__(self,other):
        return self.age == other.age
     
    # 在此定义成员方法，非静态方法必须带self,私有方法需要在前面加上self.
    def introdunce(self):
        self.__log(f"Hello! my name is {self.name} i'm is {self.gender} and age is {self.age}")
    
    def __log(self,msg:str):
        print(f"打印消息：{str}")
    