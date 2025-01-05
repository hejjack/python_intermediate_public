import pandas as pd
from classes import Knihovna, Uvod, Items
import sys





def main():

    file_csv = r'..\Python_2024\python_intermediate_public\vsykora_library\data.csv'
    new_items_file = r'..\Python_2024\python_intermediate_public\vsykora_library\add_items_import.csv'
    
    knihovna = Knihovna(file_csv, new_items_file)
    df=knihovna.nacti_knihy_z_csv()


    
    Volba = {
        "0": "Import knih do systému (csv)",
        "1": "Seznam položek v knihovně",
        "2": "Výběr položek dle žánrů",
        "3": "Výběr položek dle autora",
        "4": "Vypůjčení knihy",
        "5": "Vracení knihy",  
        "6" : "Konec Programu"
    }
       
    uvod = Uvod(Volba) 
    uvod.uvodni_zprava()

    while True:
        uvod.zobraz_manual()
        volba_uzivatele = input("Zadej hodnotu ze sloupce volba podle toho co potřebuješ zobrazit :")

        if volba_uzivatele == "0" :  
            df_new = knihovna.pridat_nove_polozky()
            print(df_new)

        elif volba_uzivatele == "1" :
            df =knihovna.nacti_knihy_z_csv()
            print(df)
            
        elif volba_uzivatele == "2" :
            print("")
            unikatni_hodnoty = knihovna.ziskej_unikatni_hodnoty(df, 'genre') # vrací seznam
            uvod.zobraz_genre(unikatni_hodnoty)
            volba_genre = input("Zadej hodnotu ze sloupce volba podle toho co potřebuješ zobrazit :")
            print("")
            if int(volba_genre)  in range(len(unikatni_hodnoty)):
                df_filtr_hodnoty =  knihovna.filtr_hodnoty(df,'genre',unikatni_hodnoty[int(volba_genre)])
                print(df_filtr_hodnoty)
            else: 
                print("Neplatná možnost, je třeba zadat znovu.") 
        elif volba_uzivatele == "3" :
            print("")
            unikatni_hodnoty = knihovna.ziskej_unikatni_hodnoty(df, 'author') # vrací seznam
            uvod.zobraz_genre(unikatni_hodnoty)
            volba_author = input("Zadej hodnotu ze sloupce volba podle toho co potřebuješ zobrazit :")
            print("")
            if int(volba_author)  in range(len(unikatni_hodnoty)):
                df_filtr_hodnoty =  knihovna.filtr_hodnoty(df,'author',unikatni_hodnoty[int(volba_author)])
                print(df_filtr_hodnoty)
            else: 
                print("Neplatná možnost, je třeba zadat znovu.") 
        elif volba_uzivatele == "4" :
            print("ještě není hotovo")

        elif volba_uzivatele == "5" :
            print("ještě není hotovo")
            
        elif volba_uzivatele == "6" :
            print("Konec programu")
            break
            
        else:
            print("Neplatná možnost, je třeba zadat znovu :")
        


# Hlavní část programu
if __name__ == "__main__":

   
    #print(os.getcwd())
     
    main()

