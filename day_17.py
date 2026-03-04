print("Never Give up !!")
Hokages ={
    "Hashirama senju":"God of Shinobi",
    "Tobirama Senju":"The creater of many jutsu",
    "Hiruzen Sarutobi":"Master of all five nature transformations",
    "Minato Namikaze":"The Yellow Flash of the leaf",
    "Tsunade":"The legendary Sannin and great Medical Ninja",
    "Kakashi Hatake":"Kakashi the copy ninja",
    "Naruto Uzumaki":"The Hero of hidden leaf: The child of prophecy",
    "Madara Uchiha":"Savior of this World"
}
Hokages["Shikamaru Nara"]="The 200 IQ Strategist : What a drag"     #add
Hokages["Minato Namikaze"]="Flying Raijin Jutsu : Fourth Hokage"    #update
del Hokages["Madara Uchiha"]                                        #delete
print(Hokages.keys())
print("\n")
print(Hokages.values())
print("\n")
print(Hokages)
-------------------------------------------------------------------------------------------------------------------------------------------------------------
leaf={
    "Uchiha1":{
        "Itachi Uchiha":"The Selfless Martyr ",
        "Sasuke Uchiha":"Shadow Hokage"
    },
    "Uchiha2":{
        "Madara Uchiha":"Ghost of the Uchiha",
        "Obito Uchiha":"The broken Hero",
        "Shisui Uchiha":"Shisui of the Body Flicker"
    }
}
print(leaf["Uchiha1"])
print("\n")
print(leaf["Uchiha2"])
--------------------------------------------------------------------------------------------------------------------------------------------------------------
time=int(input("Enter the time : "))
if time==8:
    print("its time to breakfast")
elif time==1:
    print("its time to lunch")
elif time==9:
    print("its time to dinner")
else:
    print("its not a time to eat")
---------------------------------------------------------------------------------------------------------------------------------------------------------------
seats=8
while seats>0:
    print("book one seat : ")
    seats = seats-1
    print("remaining seats:",seats)
print("All seats are booked !!")
----------------------------------------------------------------------------------------------------------------------------------------------------------------
import time
i=10
while i>0:
    print(i)
    time.sleep(1)
    i=i-1
print("Happy new year.!!!")
---------------------------------------------------------------------------------------------------------------------------------------------------------------
sum=0
for i in range(1,11):
    sum=sum+i
print(sum)
print((10*11)/2)    #  (n*(n+1))/2 
--------------------------------------------------------------------------------------------------------------------------------------------------
vowels = "aeiou"
s= "this is ullas"
count=0
for letter in s:
    if letter in vowels:
        print(letter)
        count +=1

print(count)
print("a" in  vowels)
----------------------------------------------------------------------------------------------------------------------------------------------------------
l=["Abc","Pqr","Xyz"]
u_list=[ item.upper()  for item in l]
print(u_list)
u_list=[ item.lower()  for item in l]
print("\n")
print(u_list)
-------------------------------------------------------------------------------------------------------------------------------------------------------
row=int(input("Enter the row :" ))
columns=int(input("Enter the colums :"))
matrix=[]
for i in range(row):
    x=[int(num) for num in input(f"Enter the  rows {i+1} : ").split()]
    matrix.append(x)
print(matrix)



