#from datetime import date
 
#def calculateAge(birthDate):
#    today = date.today()
#    age = today.year-birthDate.year-((today.month, today.day)<(birthDate.month, birthDate.day))
#    return age
     
#print(calculateAge(date(1997, 2, 3)), "years")



#a=int(input("Age:- "))
#if(a>=0 and a<=10):
#    print("Minor")
#elif(a>=11 and a<=18):
#    print("Major")
#elif(a>=18 and a<=75):
#    print("Matured")
#elif(a>=75 and a<=100):
#    print("Old")
#else:
#   print("Invalid input")




from datetime import date
def age(birthdate):
today = date. today()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
return age.