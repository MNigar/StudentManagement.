import database
def Insert():
      print("Telebenin qeydiyyati")
      j=0
   
      telebekodu=(input("Telebe kodunu daxil edin: "))       
      name=input("Adi daxil edin: ")   
      surname=input("Soyadi daxil edin: ")
      phone=input("Telefon nomresini daxil edin: ")
      email=input("emaili daxil edin: ")  
      if(j<10):
        yeniIstifadeci=database.Istifadeci(telebekodu,name,surname,email,phone)
        
        if(database.check(telebekodu,email,phone)):
         j+=1
        else:
         print("yeniden daxil edin")

def Edit():
  kod=input('Telebe kodunu daxil edin: ')
  edit=input("Adi ve Soyadi deyisdirmek ucun 1-i daxil edin: \n Butun melumatlari deyisdirmek ucun 2-ni daxil edin: \n")

  for i in database.userlist:
   if (kod==i.code):  
     if(edit=="1"):
       newname=input("Yeni adi daxil edin: ")
       i.name=newname
       newsurname=input("Yeni Soyadi daxil edin:")
       i.surname=newsurname
      
     if(edit=="2"):
        newname=input("Yeni Adi daxil edin:")
        newsurname=input("Yeni Soyadi daxil edin:")
        newphone=input("Yeni Telefon nomresini daxil edin:")
        newemail=input("Yeni emaili daxil edin:")
        i.name=newsurname
        i.surname=newsurname
        i.email=newemail
        i.telephone=newphone
     print("Deyisdirildi")
     i.melumatlariGoster()

def GetbyStudentcode():
   print("Telebenin melumatlari")
   kod=input('Telebe kodunu daxil edin: ')
   for i in database.userlist:
    if (kod==i.code):
      i.melumatlariGoster()
      break
   else:
      print("Bele telebe yoxdur")

def GetAll():
  print("Telebe siyahisi")
  if(len(database.userlist)==0):
        print("Siyahi bosdur")
  else:
   for i in database.userlist:
   
    i.melumatlariGoster()

def Delete():
   print("Silinme emeliyyati")
   kod=input('Telebe kodunu daxil edin: ')
   for i in database.userlist:
    if ( kod==i.code):
      database.userlist.remove(i)
      print("Silindi")
      break
    else:
       print("bele istifadeci yoxdur")
