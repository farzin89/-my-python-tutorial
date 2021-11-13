mylist = ["ali","khandan",24,True,[18,19,20]]

scores_list = mylist[-1]
ac = 0
print("scores_list:",scores_list)
for score in scores_list:
    ac = ac+score
print("majmoo:",ac)

avg = ac/len(scores_list)
print("miangin:",avg)


