while True:

    sen = int(input("sen:"))
    if not (18<= sen <50):

        print("sen shoma mojaz nist")
        continue
    tedad_nemone_kar = int(input("Tedad Nemone Kar?"))
    sabeghe_kar = int(input("chand sal sabeghe kar darid?"))

    sen = int(input("sen:"))
    etiad = input("Aya ediad darid? y/n")

    if etiad =="n":
        etiad= False
    elif etiad == "y":
        etiad = True
    if  not(etiad) and (tedad_nemone_kar >= 5 or sabeghe_kar>=4):
        print("ok")
    else:
        print("nok")
    edame_dadan = input("edame midi? y/n" )
    if edame_dadan == "n":
        break




