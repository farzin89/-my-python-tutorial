
while True:
    name = input ("name:")

    vazn =input("vazn (KG):")
    vazn_float = float (vazn)

    ghad = input ("ghad (M):")
    ghad_float = float(ghad)

    bmi = vazn_float/(ghad_float**2)

    if bmi < 16.5:
        massage = "2char kambood vazn shadid"

    elif 16.5 <= bmi < 18:
        massage ="kambod vazn"

    elif 18.5 <= bmi < 25 :
        massage ="addi"
    elif 25 <= bmi < 30:
        massage ="Ezafe vazn"
    elif 30 <= bmi < 35 :
        massage ="chaghi kelas e 1"
    elif 35 <= bmi <= 40:
        massage ="chaghi kelas e 2"
    elif 40 <= bmi :
        massage ="chaghi kelas e 3"

    print(name,"aziz","bmi shoma:",bmi)
    print("vaziat:")
    print(massage)
