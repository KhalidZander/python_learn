from iPhone import iPhone as base_iphone

# 多继承同名优先使用靠左的属性或方法
class iPhone15(base_iphone):
    face_id = 10001
    
    def __init__(self,is_5g_enable:bool):
        self.__is_5g_enable = is_5g_enable
    
    def call_by_5g(self):
        print(f"[新功能] 面部识别 {self.face_id}")
        
class iPhone16(iPhone15,base_iphone):
    # pass用于不写具体类时使用
    pass