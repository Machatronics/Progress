import random
def mp3_calar():
    sarki_listesi = ["nane nane","ucan kuslaraa","ey gidi karadeniz","huu"]
    ses = 10
    secilen_sarki = 0

    def sarki_sec (indeks):
        global secilen_sarki
        secilen_sarki = indeks
        return secilen_sarki

    def ses_arttir (sess):
        sess += 10
        return sess
    
    def ses_azalt (sess):
        sess -= 10
        return sess
    
    def rastgele_sarki_sec (son_sarki):
        global secilen_sarki
        secilen_sarki = random.randint(0,son_sarki)
        return secilen_sarki
    
    def sarki_ekle():
        global sarki_listesi
        
    
    while True:
        print("""
              Sarki listesi:{}
              Suan calan sarki : {}
              Ses : %{}
              
              1-Sarki Sec
              2-Ses arttir
              3-Ses azalt
              4-Rastgele sarki sec
              5-Sarki ekle
              6-Sarki sil
              7-Kapat
              """.format(sarki_listesi,sarki_listesi[secilen_sarki],ses))
        giris = int(input())
        if(giris == 1):
            for i in range(0,len(sarki_listesi)):
                print( str(i+1) +")"+ sarki_listesi[i])
            secilen_sarki = sarki_sec(int(input("Seçmek istediginiz sarki numarasini girin :"))-1)
        
        if(giris == 2):
            if(ses != 100):
                ses =  ses_arttir(ses)
            
        if(giris == 3):
            if(ses != 0):
                ses = ses_azalt(ses)
        
        if(giris == 4):
           secilen_sarki = rastgele_sarki_sec(len(sarki_listesi)-1)
        
        if(giris == 5):
            sarki_listesi.append(input("Eklemek istediginiz sarki adini yaziniz :"))
        
        if(giris == 6):
            for i in range(0,len(sarki_listesi)):
                print( str(i+1) +")"+ sarki_listesi[i])
            sarki_listesi.pop(int(input("Silmek istediginiz sarkinin numarasini giriniz : "))-1)
            
        if(giris == 7):
            break
            
            

mp3_calar()
        
        