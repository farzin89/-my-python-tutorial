while True:


    masir = int(input("toole masir ra vared konid:(m)"))
    fasele = int(input("Fasele tir ba badi:(m)"))
    gheymat_tir = int(input("gheymat har tir(Toman)"))
    gheymat_lamp = int(input("Gheymat lamp:(Toman)"))

    tedad_tir = masir // fasele
    fasele_baghi = masir % fasele

    Gheymat_kol = (gheymat_tir + (gheymat_lamp*2) * tedad_tir)
    print("Tedad_tir:",tedad_tir)
    print("Fasele_baghi",fasele_baghi)
    print("Gheimat e Kol:", Gheymat_kol,"Toman")
    edame = input("Edame? y/n")
    if edame == "n":
        break



