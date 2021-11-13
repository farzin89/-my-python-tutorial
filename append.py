
day_list = ["sat","sun","mon","tue","mon","thu","fri"]

step_list=[]

for day in day_list:
    day_step = int(input(day + " step:"))
    step_list.append(day_step)

print("step_list is:")
print(step_list)

for i in range(len(step_list)):
    print(i)
    n = (step_list[i] * 50) // 20000
    print(day_list[i],":","*"*n)


