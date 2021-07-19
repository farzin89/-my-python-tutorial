# -my-python-tutorial
Basic command for python

    \n   in order to go next step
    for example print("Hello \n world") 
    answer = Hello 
         Worid
    if we want to use Tab we can use : print("Hello\t World")

    answer = Hello    World

     in order to replace two variable we can you replace command
     for example : a = "Hello World"
              b = a.replace("H","h")
              print(b)
              
    len = show us how many characetrs we used
    for example = print(len(a)) 
      answer = 11
      
    index = show us the first occurrence of the specified value
    print(a.index("w"))
    answer = 6
      print(a.index[8])
    answer = 7   (because the first one is zero)
........................................................................................
 
    max = show us the maximum number between two variable
    for example   num1= 10
              num2 = 3
              print(max(num1,num2)
     answer = 10
              print(min(num1,num2)
    answwr = 3
.......................................................................................

    how to use input command:
    for example:
    name = input("please insert your name:")
    team = input ("what is your favorite soccer team?")
    print("Hello" + name + "! \nyour favourit team is" + team)

.....................................................................................
 
    if command with input (calculator)
 
    num1 = input("please insert the first number:")
    num2 = input("please insert the second number:")
    operation = input("please insert your desired operation among: +,-,*,/")

    if operation == "+":
     result = int(num1) +int(num2)
    elif operation =="-":
    result = int(num1)-int(num2)  ### if we want to use integer we use int
    elif operation == "*":
    result = int(num1) *int(num2) ### if we want to use decimal number instead of integer we use float commond
    elif operation == "/":
    result = int(num1) * int(num2)
    else :
    result= "The operation inserted by the user is wrong!"

    print(result)

...............................................................................
 list
    
    colors=["Green","Blue","Black","White","Red"]
    print(colors[1:4])
    
    answer = ['Blue', 'Black',White']
    
    print(colors[:3])
    
    answer = ['Green', 'Blue', 'Black']
     
     print(colors[1:-2])
     answer = ['Blue', 'Black']
     
     colors=["Green","Blue","Black","White","Red"]
    colors[1:4] = ["Yellow","Gray","Orange"]
    print(colors)
    answer = ['Green', 'Yellow', 'Gray', 'Orange', 'Red']
    
    colors=["Green","Blue","Black","White","Red"]
    colors.extend(["orange","gray"])
    print(len(colors))
    answer = 7
    
    colors=["Green","Blue","Black","White","Red"]
    colors.insert(2,"orange")
    print(colors)
    answer= ['Green', 'Blue', 'orange', 'Black', 'White', 'Red']
    
    colors=["Green","Blue","Black","White","Red","Blue"]
    colors.remove("Blue")
    print(colors)
    answer = ['Green', 'Black', 'White', 'Red', 'Blue']
    
    colors=["Green","Blue","Black","White","Red","Blue"]
    colors.clear()
    print(colors)
    answer = []
    
    colors=["Green","Blue","Black","White","Red","Blue"]
    print(colors.index("Black"))
    answer = 2
    
    colors=["Green","Blue","Black","White","Red","Blue"]
    print(colors.count("Blue"))
    answer = 2
    
    colors=["Green","Blue","Black","White","Red","Blue"]
    colors.sort()
    print(colors)
    answer = ['Black', 'Blue', 'Blue', 'Green', 'Red', 'White']
    
    colors=["Green","Blue","Black","White","Red","Blue"]
    colors_sorted = sorted(colors)
    print(colors)
    print(colors_sorted)
    answer =
             ['Green', 'Blue', 'Black', 'White', 'Red', 'Blue']
             ['Black', 'Blue', 'Blue', 'Green', 'Red', 'White']
             
    colors=["Green","Blue","Black","White","Red","Blue"]
    colors_sorted = sorted(colors)
    del colors           
   
    colors=["Green","Blue","Black","White","Red","Blue"]
    colors.reverse()
    print(colors)
    answer = ['Blue', 'Red', 'White', 'Black', 'Blue', 'Green']

   

      
      
              
