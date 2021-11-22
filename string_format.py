

name_list = ["ali","reza","sara"]
age_list = [25,20,15,]

for i in range(len(name_list)):
    name = name_list[i]
    age = age_list[i]
    text1="my name is "+ name + " my age is " + str(age)
    print(text1)

# or

name_list1 = ["hasan","hosein","taghi"]
age_list1 = [30,40,50]

for i in range(len(name_list)):
    name1 = name_list1[i]
    age1 = age_list1[i]
    text2="my name is {}  my age is {} ".format( name1, age1)
    print(text2)

 ############################

mahsol = "Moz"
tedad = 200
price = 1000
text3 = f"{tedad} adad mahsool {mahsol} ba gheymat {price}" # F string method
print(text3)

######################################

for namee in ["farzin","salin","pari"]:
    message = "the name is {}".format(namee)
    print(message)
#########################################
for nameee in ["naser","sahand","soheyb"]:
    message1= f"the nameee is {nameee}"    # F string method
    print(message1)



