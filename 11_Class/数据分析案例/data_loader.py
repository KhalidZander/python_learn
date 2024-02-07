from data_define import Data
import json

class DataLoader:
    
    def read_data(self) ->list:
        pass

class CsvDataLoader(DataLoader):
    
    def __init__(self,path):
        self.path = path
        
    def read_data(self) -> list:
        res = [] 
        with open(self.path,"r",encoding="utf-8") as f:
            message = f.readlines()     
        for line in message:
            arr = line.strip().split(',')
            data = Data(arr[0],arr[1],arr[2],arr[3])
            res.append(data)
            print(data)
        return res

class JsonDataLoader(DataLoader):
    
    def __init__(self,path:str):
        self.path = path
    
    def read_data(self) -> list:
        res = []
        with open(self.path,"r",encoding="utf-8") as f:  
            data_dict:dict = json.loads(f.readlines()[0]);
            for kv in data_dict:
                data =  Data(kv['date'],kv['order_id'],kv['money'],kv['province'])
                res.append(data)
                print(data)
            return res