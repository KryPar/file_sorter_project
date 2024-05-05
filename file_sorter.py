import os
import shutil

slozka = r"C:\Users\ucite\Desktop"
soubory = os.listdir(slozka)

def file_sortet(soubory):
    for soubor in soubory:
        nazev, pripona = os.path.splitext(soubor)
        cilova_slozka = None

        if pripona == ".pdf":
            cilova_slozka = os.path.join(slozka, "Pdf")
        elif pripona == ".jpg":
            cilova_slozka = os.path.join(slozka, "Obrázky")
        elif pripona == ".mp3":
            cilova_slozka = os.path.join(slozka, "Hudba")
        elif pripona == ".avi":
            cilova_slozka = os.path.join(slozka, "Filmy")
        elif pripona == ".docx" or ".doc":
            cilova_slozka = os.path.join(slozka, "Word")
        elif pripona == ".xlsx":
            cilova_slozka = os.path.join(slozka, "Excel")

        if cilova_slozka:
            if not os.path.exists(cilova_slozka):
                os.makedirs(cilova_slozka)
            try:
                shutil.move(os.path.join(slozka, soubor), os.path.join(cilova_slozka, soubor))
            except FileNotFoundError:
                print(f"Soubor '{soubor}' nelze najít.")
        else:
            print(f"Soubor '{soubor}' má neznámou příponu.")

file_sortet(soubory)


