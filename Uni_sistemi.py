import sqlite3
import random
import re

def ogrenci_sistemi():

    def ogrenci_kayit():
        
        ad = input("Ogrencinin adini giriniz :")
        soyad = input("Ogrencinin soyadini giriniz :")
        fakulte = input("Ogrencinin fakultesini giriniz :") 
        bolum = input("Bolum giriniz :")
        numara = int(input("Numarasini giriniz  :"))
        ogrenim_turu = input("Ogrenim turunu giriniz : ")
        durum = input("Durum girinizi :")
        
        with sqlite3.connect("ogrencisistemi.db") as ogrenci_veritabani_dosya:
            cursor = ogrenci_veritabani_dosya.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS ogrenci_veritabani(ad TEXT,soyad TEXT,fakulte TEXT,bolum TEXT,numara INT,ogrenim_turu TEXT,durum TEXT,essiz_ID INT)")
            #cursor.execute("INSERT INTO ogrenci_veritabani VALUES(?,?,?,?,?,?,?)",(ad,soyad,fakulte,bolum,numara,ogrenim_turu,durum))
            while True:
                global id_check
                id_check = 0
                essiz_ID = random.randint(10000000,99999999)
                for id_check in cursor.fetchall():
                    if(id_check == essiz_ID ):
                        break
                if(id_check != essiz_ID):    
                    cursor.execute("INSERT INTO ogrenci_veritabani VALUES(:ad,:soyad,:fakulte,:bolum,:numara,:ogrenim_turu,:durum,:essiz_ID)",{'ad':ad,'soyad' :soyad,'fakulte':fakulte,'bolum':bolum,'numara':numara,'ogrenim_turu':ogrenim_turu,'durum':durum,'essiz_ID' :essiz_ID})
                    ogrenci_veritabani_dosya.commit()
                    print("Kayit basariyla tamamlandi.")
                    break
            ogrenci_veritabani_dosya.commit()

    def ogrenci_silme():
        ad = input("Ogrencinin adi :")
        soyad = input("Ogrencinin soyadi :")
        numara = int(input("Ogrencinin numarasi :"))
        with sqlite3.connect("ogrencisistemi.db") as ogrenci_veritabani_dosya:
            cursor = ogrenci_veritabani_dosya.cursor()
            try:
                cursor.execute("SELECT * from ogrenci_veritabani WHERE ad ==:ad AND soyad == :soyad AND numara == :numara",{'ad':ad,'soyad':soyad,'numara':numara})
            except:
                print("Ogrenci bulunamadi")
                return
            print("calisti la")
            silinecek_ogrenci_id = cursor.fetchone()[7]
            print(type(silinecek_ogrenci_id))
            print(silinecek_ogrenci_id)
            last_delete_check = input("Ogrenciyi silmek istediginiziden emin misiniz(e/h) : ")
            if(last_delete_check == 'e'):
                cursor.execute("DELETE FROM ogrenci_veritabani WHERE essiz_ID = ?",(silinecek_ogrenci_id,))
            print("Basariyla silindi.")
    def ogrenci_bilgisi_degisme(): 
        bilgisi_degisecek_ogrenci_essiz_ID = int(input("Bilgisi degisecek ogrencinin essiz ID'sini giriniz."))
        print("""
              Ogrencinin degisecek parametresini yaziniz;
              
              ad
              soyad
              fakulte
              bolum
              numara
              ogrenim_turu
              durum
              """)
        
        degisecek_parametre = input()
        regex = re.compile('[@!#$%^&*()<>?/\|}{~:]') 
        if(regex.search(degisecek_parametre) == None): 
            if(degisecek_parametre == 'numara'):
                girilen_parametre = int(input("Yeni giriniz :"))
            elif(degisecek_parametre == 'ad' or degisecek_parametre == 'soyad' or degisecek_parametre == 'fakulte' or degisecek_parametre == 'bolum' or degisecek_parametre == 'ogrenim_turu' or degisecek_parametre == 'durum'):
                girilen_parametre = input("Yeni giriniz :")
                
        elif():
            print("hatali giris")
            return
        with sqlite3.connect("ogrencisistemi.db") as ogrenci_veritabani_dosya:
            cursor = ogrenci_veritabani_dosya.cursor()
            cursor.execute("SELECT * from ogrenci_veritabani WHERE essiz_ID == ? ",(bilgisi_degisecek_ogrenci_essiz_ID, ))
            cursor.execute("UPDATE ogrenci_veritabani SET {} = ?".format(degisecek_parametre),(girilen_parametre,))


    print("""
          Islem yapmak istediginiz numarayi yaziniz :
              
              1-Ogrenci kayit
              2-Ogrenci silme
              3-Ogrenci bilgisini degistirme
          """)
    secim = int(input())
    if(secim == 1):
        ogrenci_kayit()
    if(secim==2):
        ogrenci_silme()
    if(secim == 3 ):
        ogrenci_bilgisi_degisme()
    
    
        
ogrenci_sistemi()