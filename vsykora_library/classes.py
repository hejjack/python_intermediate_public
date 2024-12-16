# definované třídyimport pandas as pd
import pandas as pd

class Items:
    def __init__(self, titul, autor, type_polozky, rok_vydani, druh_liter, isbn, mnozstvi):
        self.title = titul
        self.author = autor
        self.type = type_polozky
        self.publication_year = rok_vydani
        self.genre = druh_liter
        self.isbn = isbn
        self.copies_available = mnozstvi

    # tisk informací o knize
    def info_items(self):
        return f"Název: {self.title}, autor: {self.author}, rok vydání: {self.publication_year}, množství:{self.copies_available}"
    

class Knihovna:

    def __init__(self, import_file, new_items_file):
        self.import_file = import_file 
        self.new_items_file = new_items_file


    def nacti_knihy_z_csv(self):
        try:
            # Načtení csv souboru pomocí pandas

            df = pd.read_csv(self.import_file, encoding='utf-8')
            return df
        except Exception as e:
            print(f"Nastala chyba při načítání souboru: {e}")
            return None
        
    
    def nahraj_knihy_do_csv(self,df,):
        try:
            df.to_csv(self.import_file, index = False)
            print(f"Položky byly přidány do {self.import_file}")
        except Exception as chyba:
            print(f"Nastala chyba při přidávání položek do souboru :{chyba}")


    def pridat_nove_polozky(self):
        try:
            df_existing_books = self.nacti_knihy_z_csv()
        
            if df_existing_books is not None:
                df_new_books = pd.read_csv(self.new_items_file)
                df_combined = pd.concat([df_existing_books, df_new_books])
                df_combined = df_combined.drop_duplicates(subset='isbn', keep='last')
                self.nahraj_knihy_do_csv(df_combined)            
                return df_combined
            else:
                return None
        except Exception as e:
            print(f"Nastala chyba při přidávání nových položek: {e}")
        return None


    def ziskej_unikatni_hodnoty(self, df, sloupec):
        return df[sloupec].unique();
    
    def filtr_hodnoty(self, df, sloupec, hodnota):
        return df[df[sloupec] == hodnota]
    
    


class Uvod:
    def __init__(self, options, unikatni_hodnoty = None):
        self.options = options
        self.unikatni_hodnoty = unikatni_hodnoty if unikatni_hodnoty is not None else []
        
    def uvodni_zprava(self):
        print("Vítejte v programu knihovna")
        print("")
        print("Možnosti programu - jeho obsluha ")
        print('-' * 40)

    def zobraz_manual(self,unikatni_hodnoty = None):
        if  unikatni_hodnoty is None: 
            unikatni_hodnoty = self.unikatni_hodnoty

        header_option = "Volba"  
        header_description = "Popis"

        print(f"| {header_option: ^5} |{header_description: ^29} |")
        print('-' * 40)
        for option, description in self.options.items():
            print(f"| {option: ^5} | {description: <28} |")
        print('-'*40 )
     

    def zobraz_genre(self,unikatni_hodnoty):
        # výpis unikátních hodnot 
        print('-' * 40)
        header_option = "Volba"  
        header_description = "Popis"
        print(f"| {header_option: ^5} |{header_description: ^29} |")
        print('-' * 40)

        vystup = [f"| {index: ^5} |  {type: <28}|" for index, type in enumerate(unikatni_hodnoty)]
        for radek in vystup:
            print(radek)
            print('-' * 40)
    


        

    


    


    
