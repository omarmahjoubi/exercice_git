def nb_voyelles(ch) :
compt=0
for car in ch :
    if car in "aeiouyAEIOUY" :
        compt=compt+1
return compt 

ch=input("donner une phrase : ")
i=nb_voyelles(ch)
print("la phrase",ch,"contient",i,"voyelles.")
