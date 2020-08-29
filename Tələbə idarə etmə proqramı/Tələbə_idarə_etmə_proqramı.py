import database
import Functions
x=True

while (x):
 emr=input("\n Tələbəni daxil etmək üçün 1-i daxil edin : \n Tələbənin axtarışı üçün 2-ini daxil edin: \n Bütün tələbələrin məlumatlarını əldə etmək üçün 3-ü daxil edin: \n Tələbənin siyahıdan silinməsi üçün 4-ü daxil edin: \n Tələbənin məlumatlarının dəyişdrilməsi üçün 5-i daxil edin \n")
 print("*******************************************")
 #Telebenin daxil edilmesi
 if (emr=="1"):
     Functions.Insert()
  #Telebe melumatlarinin telebekodu ile elde edilmesi (axtaris)       
 elif(emr=="2"):
  Functions.GetbyStudentcode()
  #Butun telebelerin melumatlari    
 elif(emr=="3"):
  Functions.GetAll()

 #Telebenin telebe kodu vasitesi ile siyahidan silinmesi 

 elif(emr=="4"):
   Functions.Delete()
 #Telebenin melumatlarinin deyisdirilmesi 

 elif(emr=="5"):

  Functions.Edit()
 elif(emr=="6"):
  x=False


        

