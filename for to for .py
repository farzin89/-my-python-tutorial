class_list = [["ali",10,15,20],["reza",17,18,20],["sara",15,10,14]]
cheater_list = ["ali"]
for student in class_list:
    sum_score = 0

    if student[0] in cheater_list:
      print(student[0],"is a cheater")
      continue

    for score in student[1:]:
        sum_score = sum_score+score

    ave = sum_score/(len(student) -1)
    print("ave is :",ave)
print("the end")









