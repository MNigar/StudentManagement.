import re
userlist=[]
def check(code,email,telephone):
     x=True
     if not (re.search("@",email)) :
          print("Email daxilində @  işarəsi olmalıdır \n" )
          x=False
     if not( re.findall("^00994", telephone)) :
          print("Telefon nömrəsi +00994lə başlamalıdır")
          x=False
     if not( re.findall("\d{3}", code)): 
          print("kod 3 reqemden ibaret olmalidir") 
          x=False
     if(x==True):
      return True
     else:
      return False
class Istifadeci:
    def __init__(self,_code,_name,_surname,_email,_phone):
        self.name=_email
        self.telephone=_phone
        self.name=_name
        self.surname=_surname
        self.code=_code
        self.email=_email
        if (check(self.code,self.email,self.telephone)): 
         userlist.append(self)  

   
    def melumatlariGoster(self):
     print(self.code+ " " +self.name + "  " + self.surname+ " " +self.email + "  "+self.telephone )  
   


    
    
    
    
    
    
    
    
    