import requests


class Action :

    files = None

    def __init__(self, url, data=None,headers=None) -> None:
        self.url = url
        self.data = data
        self.headers = headers

    

    def post (self) :
        self.req = requests.post(self.url,data=self.data,headers=self.headers,files=self.files)
        
    def get (self) :
        self.req = requests.get(self.url,data=self.data,headers=self.headers,files=self.files)
        
    def patch (self) :
        self.req = requests.patch(self.url,data=self.data,headers=self.headers,files=self.files)
        

    def is_valid (self) : 
        return (200 == self.req.status_code)
    
    def json_data (self) : 
        return self.req.json()