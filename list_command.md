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
