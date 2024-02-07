class iPhone:
    __is_5g_enable =None
    
    def __init__(self,is_5g_enable:bool):
        self.__is_5g_enable = is_5g_enable
    
    def __check_5g(self):
       if(self.__check_5g):
           print("[Info] Current State: 5G")
       else:
           print("[Info] Current State: 4G")
    
    def call_by_5g(self):
        self.__check_5g()
        print("[Info] 通过中...")

# 手机接口 方法全部pass
class iMoble:
    
    def call(self): 
        pass

    def listen_music(self):
        pass
    
    def play_game(self):
        pass