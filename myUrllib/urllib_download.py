import urllib.request

class urllib_download:
    def __init__(self):
        pass

    def download(self,url,filename):
        from urllib.request import urlretrieve  # Add this line
        urlretrieve(url,filename,None,'$0')  # Use the urlretrieve function directly
        print("download success")