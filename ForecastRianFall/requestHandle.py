import requests ,json


class GetData:
   def check_url(self,url):
      try:
         session = requests.Session()
         req = session.get(url,timeout=1)
         return True
      except requests.exceptions.ConnectionError:
         return False
   def getURL(self,url):
     if self.check_url(url) == False:
        return None
     # Send Request to url 
     session = requests.Session()
     req =session.get(url)
     # GET JSON
     try:
      jsonData=json.loads(req.text)
      return jsonData
     except json.decoder.JSONDecodeError:
        return False
     except TypeError:
        return False
   def SortJsonData(self,jsonData):
       yerasBar=[]
       years=[]
       try:
          jsonData[0]["year"]
       except KeyError:
          return False
       for i in jsonData:
           yerasBar.append(i["Levelrainfall"])
           years.append(i["year"])
       years.sort()
       return (yerasBar,years)

