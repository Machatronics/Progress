import random
def xox_oyunu(kullanici_sayisi):
    tablo = ['1','2','3','4','5','6','7','8','9']
    giris = 'a'
    bitti = False
    def x(sayi):
        while True:
            if(tablo[sayi] == "X" or tablo[sayi] == "O" ):
                print("****Sectiginiz bolge doludur. Baska bolge seciniz.****")
            if(tablo[sayi] != "X" and tablo[sayi] != "O" ):
                tablo[sayi] = "X"
                if(tablo[0] == tablo[1] == tablo[2] or tablo[3] == tablo[4] == tablo[5] or tablo[6] == tablo[7] == tablo[8] or tablo[0] == tablo[3] == tablo[6] or tablo[1] == tablo[4] == tablo[7] or tablo[2] == tablo[5] == tablo[8] or tablo[0] == tablo[4] == tablo[8] or tablo[2] == tablo[4] == tablo[6]):
                    print("Kazandınız : ************** {} **************".format(*oyun_sirasi[oyuncu]))
                    bitti= True
                    return bitti
                break
    
    def o(sayi):
        while True:
            if(tablo[sayi] == "X" or tablo[sayi] == "O" ):
                print("****Sectiginiz bolge doludur. Baska bolge seciniz.****")
                sayi = int(input())-1
            if(tablo[sayi] != "X" and tablo[sayi] != "O" ):
                tablo[sayi] = "O"
                if(tablo[0] == tablo[1] == tablo[2] or tablo[3] == tablo[4] == tablo[5] or tablo[6] == tablo[7] == tablo[8] or tablo[0] == tablo[3] == tablo[6] or tablo[1] == tablo[4] == tablo[7] or tablo[2] == tablo[5] == tablo[8] or tablo[0] == tablo[4] == tablo[8] or tablo[2] == tablo[4] == tablo[6]):
                    print("Kazandınız : ************** {} **************".format(*oyun_sirasi[oyuncu]))
                    bitti = True
                    return bitti
                break
    
    def robot_x():
        while True:
            sayi = random.randint(0,8)
            if(tablo[sayi] != "X" and tablo[sayi] != "O" ):
                tablo[sayi] = "X"
                if(tablo[0] == tablo[1] == tablo[2] or tablo[3] == tablo[4] == tablo[5] or tablo[6] == tablo[7] == tablo[8] or tablo[0] == tablo[3] == tablo[6] or tablo[1] == tablo[4] == tablo[7] or tablo[2] == tablo[5] == tablo[8] or tablo[0] == tablo[4] == tablo[8] or tablo[2] == tablo[4] == tablo[6]):
                    print("Kazandınız : ************** {} **************".format(*oyun_sirasi[oyuncu]))
                    bitti = True
                    return bitti
                tablo_yazdir()
                break
            
    def tablo_yazdir():
        print("""
              {} | {} | {}
              ---------
              {} | {} | {}
              ---------
              {} | {} | {}
              """.format(tablo[0],tablo[1],tablo[2],tablo[3],tablo[4],tablo[5],tablo[6],tablo[7],tablo[8]))
        return

    while True:
        tablo_yazdir()
        oyuncu = 0
        oyun_sirasi = ["O","X"]
        giris = int(input(("İlk oyuncu O yazdırmak istediginiz numarayi giriniz.(O == 1 , X == 2)\n")))-1 
        
        while(kullanici_sayisi == 2 and bitti == False ):
            if(oyun_sirasi[oyuncu] == "O"):
                o(giris)
            elif(oyun_sirasi[oyuncu] == "X"):
                x(giris)
            if(oyuncu == 1):
                oyuncu -= 1
            elif(oyuncu == 0):
                oyuncu += 1
            tablo_yazdir()
            print("\n\n\n**************************************************************")
            if(tablo[0] == tablo[1] == tablo[2] or tablo[3] == tablo[4] == tablo[5] or tablo[6] == tablo[7] == tablo[8] or tablo[0] == tablo[3] == tablo[6] or tablo[1] == tablo[4] == tablo[7] or tablo[2] == tablo[5] == tablo[8] or tablo[0] == tablo[4] == tablo[8] or tablo[2] == tablo[4] == tablo[6]):
                print("Kazandınız : ************** {} **************".format(*oyun_sirasi[oyuncu-1]))
                break
            giris = int(input(("Sıradaki oyuncu,yazdırmak istediginiz numarayi giriniz.(O == 1 , X == 2)\n")))-1

            
            
            
        while(kullanici_sayisi == 1 and bitti == False):
            o(giris)
            tablo_yazdir()
            while True:
                robot_x()
                break
            print("*****Bilgisayarin sirasi*****")
            tablo_yazdir()
            print("\n\n\n**************************************************************")
            if(tablo[0] == tablo[1] == tablo[2] or tablo[3] == tablo[4] == tablo[5] or tablo[6] == tablo[7] == tablo[8] or tablo[0] == tablo[3] == tablo[6] or tablo[1] == tablo[4] == tablo[7] or tablo[2] == tablo[5] == tablo[8] or tablo[0] == tablo[4] == tablo[8] or tablo[2] == tablo[4] == tablo[6]):
                print("Kazandınız : ************** {} **************".format(*oyun_sirasi[oyuncu]))
                break
            giris = int(input(("Yazdırmak istediginiz numarayi giriniz : ")))-1

            

        
        
        
        
        
while True:        
    kullanici_sayisi = int(input("Oyun tek kisilik mi cift kisilik mi?(1 ya da 2 giriniz)"))
    xox_oyunu(kullanici_sayisi)
    print("Oyunu sonlandırmak isterseniz 'y' giriniz")
    if('y' == input()):
        break
