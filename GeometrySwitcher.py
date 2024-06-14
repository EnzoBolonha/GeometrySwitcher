import os
import shutil
dir_path = os.path.dirname(os.path.realpath(__file__))
pastafeito = f"{dir_path}\\Feito"
os.chdir(dir_path)
tipo = input("Tipo: ")
talvez = "s"
while talvez == "s":
    numi = input("Numero Inicial: ")
    numf = input("Numero Final: ")
    for file in os.listdir(dir_path):
        if file.count(tipo) >= 1:
            if file.count(numi) == 1:
                new = file.replace(numi, numf)
                os.rename(file, new)
                lugar = f"{dir_path}\\{new}"
                shutil.move(lugar, pastafeito)
    jorge = input("dnv? (s/t/n) ")
    print("----------")
    if jorge == "t":
        tipo = input("Tipo: ")
    elif jorge == "n":
        talvez = "n"
