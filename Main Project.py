#-------------------------------Number Plate Generator-------------------------------------------------------------------------------------#
# Author: Ashutosh Jagdish Patil
# Date of Start: 10 April 2022
# Date of Finish : 11 April 2022
#------------------------------------------------------------------------------------------------------------------------------------------#

import random
print('''Hello An Welcome To Autonomous Number plate Generating System''')
avail = ["maharashtra","gujrat","madhyapradesh"]
print("Available states are: ",avail)
input1 = input("Enter your state: ")
avail2 ={"maharashtra":("dhule","jalgaon","pune"),"gujrat":('anand','ahmedabad','surat','rajkot'),"madhyapradesh":('indore','dhar','bhopal')}
distcode = {"dhule":"MH 18","jalgaon":"MH 19","pune":"MH 12","anand":"GJ 23","ahmedabad":"GJ 01","surat":"GJ 28","rajkot":"GJ 03","indore":"MP 09"
,"bhopal":"MP 04","dhar":"MP 11"}
plate = []
for i in avail:
    plate =[]
    if input1 in avail:
        if "maharashtra" in input1:
            print("Available districts are: ",avail2["maharashtra"])
            input2 = input("Enter Your District: ")
            for i in avail2:
                if "dhule"in input2:
                    plate.append(distcode["dhule"])
                    break
                if "jalgaon" in input2:
                    plate.append(distcode["jalgaon"])
                    break
                if "pune" in input2:
                    plate.append(distcode["pune"])
                    break
            break
        elif "gujrat" in input1:
            print("Available districts are: ",avail2["gujrat"])
            input2 = input("Enter Your District: ") 
            for x in avail2:
                if "anand" in input2:
                    plate.append(distcode["anand"])
                    break
                if "ahmedabad" in input2:
                    plate.append(distcode["ahmedabad"])
                    break
                if "surat" in input2:
                    plate.append(distcode["surat"])
                    break
                if "rajkot"in input2:
                    plate.append(distcode["rajkot"])
                    break
            break
        elif "madhyapradesh" in input1:
            plate =[]
            print("Available districts are: ",avail2["madhyapradesh"])
            input2 = input("Enter Your District: ")  
            for y in avail2:
                if "indore" in input2:
                    plate.append(distcode["indore"])
                    break
                if "dhar" in input2:
                    plate.append(distcode["dhar"])
                    break
                if "bhopal" in input2:
                    plate.append(distcode["bhopal"])
                    break
            break
cv = []
a = random.randint(1000,9000)
for i in range(2):
    z = random.randint(65,90)
    xc = random.randint(65,90)
    jk = chr(z)+chr(xc)
    cv.append(jk)
    cv.append(a)
    plate+=cv
    break
print("Your number plate is : ")
for i in plate:
    print(i,end = " ")
    

