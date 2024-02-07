class Data:
    date:str = ""
    order_id:str = ""
    money:int = 0
    province:str = ""
    
    def __str__(self) -> str:
        return f"时间：{self.date} 序号:{self.order_id} 消费：{self.money} 省份:{self.province}"
    
    def __init__(self,date:str,order_id:str,money:int,province:str):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province