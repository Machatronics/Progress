import json
import random
    
def giris_yap(kullanici_adi,sifre):
    deneme = 3
    while deneme > 0 :
        with open("json_kullanici_bilgileri.json","r") as dosya:
            kullanici_bilgileri = json.load(dosya)
            for bilgiler in kullanici_bilgileri["giris_bilgileri"]:
                if(bilgiler["kadi"] == kullanici_adi and bilgiler["sifre"] == sifre):
                    print("giris basarili")
                    return True
        return False
        deneme -= 1
        if(deneme == 0):
            print("Giris hakkiniz kalmamistir. Ana sayfaya yonlendirliyorsnuuz.")
            break
        print("Giris basarisiz.Tekrar deneyiniz.Kalan deneme hakki : {}".format(deneme))
        sifre = input()
           
def kayit_ol(kullanici_adi,sifre,mail):
    kullanici_bilgileri = {}
    kullanici_bilgileri["giris_bilgileri"] = [{"kadi" : "Admin" , "sifre" : "Admin", "mail": "Admin@gmail.com"}]
    if(sifre != input("Lutfen sifrenizi tekrar yaziniz.")):
        print("Hatali sifre tekrari. Ana sayfaya yonlendirliyorsunuz.")
        return
    try :
        with open("json_kullanici_bilgileri.json","r") as dosya:
            json_kullanici_bilgileri = json.load(dosya)
    except : 
        with open("json_kullanici_bilgileri.json","a") as dosya:
             json.dump(kullanici_bilgileri,dosya)
        with open("json_kullanici_bilgileri.json","r") as dosya:       
             json_kullanici_bilgileri = json.load(dosya)
    for bilgiler in json_kullanici_bilgileri["giris_bilgileri"]:
        if(bilgiler["kadi"] == kullanici_adi or bilgiler["mail"] == mail):
            print("Bu kullanici adi veya eposta zaten kullanılmaktadır. Lutfen baska seciniz")
            break
    if(bilgiler["kadi"] != kullanici_adi and bilgiler["mail"] != mail):
        json_kullanici_bilgileri["giris_bilgileri"].append({"kadi" : kullanici_adi ,"sifre" : sifre,"mail" : mail })
        print("Kayit isleminiz basariyla gerceklesmistir.")
        with open("json_kullanici_bilgileri.json","w") as dosya:
            json.dump(json_kullanici_bilgileri,dosya)   
            return True
    return False
def kullanici_sil(kullanici_adi,sifre,mail):
    pass
          
def sifremi_unuttum(mail):
    print("Aktivasyon kodu gonderilmistir.")
    try :
        dosya = open("aktivasyon.txt","x")
        dosya.close()
        dosya = open("aktivasyon.txt","w")
    except:
        dosya = open("aktivasyon.txt","w")
    dosya.write(str(random.randint(100000,999999)))
    dosya.close()
    aktivasyon_kodu = input("Lutfen aktivasyon kodunuzu giriniz:")
    dosya = open("aktivasyon.txt","r")
    if(dosya.readline(6) == aktivasyon_kodu):
        dosya.close()
        with open("json_kullanici_bilgileri.json","r") as dosya_json:
            tutucu = json.load(dosya_json)
            for bilgiler in tutucu["giris_bilgileri"]:
                if(bilgiler["mail"] == mail):
                    yeni_sifre = input("Girmek istediginizi yeni sifreyi yaziniz : ")
                    yeni_sifre_tekrar = input("Sifrenizi tekrar yaziniz :")
                    if(yeni_sifre == yeni_sifre_tekrar):
                        bilgiler["sifre"] = yeni_sifre
        with open("json_kullanici_bilgileri.json","w") as dosya_json:
            json.dump(tutucu,dosya_json)
    dosya.close()
    print("YES BE")
    return True
        
while True:
    print("""
          1-Giris yap
          2-Kayit ol
          3-Sifremi unuttum
          4-Çıkış
          """)
    hangisi = int(input("Islem yapmak istediginiz sayi : "))

    if(hangisi == 1):       
        kullanici_adi = input("Lutfen kullanici adinizi giriniz : ")
        sifre = input("Lutfen sifrenizi giriniz : ")
        check = giris_yap(kullanici_adi,sifre)
        if(check == True):
            break
    if(hangisi == 2):
        kullanici_adi = input("Lutfen kullanici adinizi giriniz : ")
        sifre = input("Lutfen sifrenizi giriniz : ")
        mail = input("Lutfen mailinizi giriniz : ")
        check = kayit_ol(kullanici_adi,sifre,mail)
        if(check == True):
            break
    if(hangisi == 3 ):
        mail = input("Lutfen mailinizi giriniz : ")
        check = sifremi_unuttum(mail)
        if(check == True):
            break
        

    
