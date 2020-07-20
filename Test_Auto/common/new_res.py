import requests,json

class API:
    def api_method(self,method,url,parma=None,header=None):
        print(method)
        if method == 'get' or 'GET':
            print(123123123)
            if header == None:
                res = requests.get(url=url,params=parma)
                return res.json()
            else:
                head = {'Content-type': 'application/x-www-form-urlencoded'}
                res = requests.get(url=url,params=parma,headers=head)
                return res.json()
        else:
            print(99999999999999999999)
            if header == None:
                res = requests.post(url=url,data=json.loads(eval(parma)))
                return res.json()
            else:
                res = requests.post(url=url,data=json.loads(eval(parma)),headers=header)
                return res.json()