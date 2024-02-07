import os
import json

class MyJson:
    def __init__(self, path):
        self.path = path

    def read(self):
        print(os.getcwd())
        if not os.path.exists(self.path):
            open(self.path, 'w').close()
            return {}
        with open(self.path, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}

    def write(self, data):
        with open(self.path, 'w') as f:
            json.dump(data, f, indent=4)
            return True        