ögrenciListesi = ["Eren Baltekin", "Sadık Turan"]

def kayit(isim, soyisim):
    ögrenciListesi.append(isim +" "+soyisim)
    return ögrenciListesi

def kayitSil(isim, soyisim):
    ögrenciListesi.remove(isim +" "+soyisim)
    return ögrenciListesi

def cokluKayit(kayitAdedi):
    i = 0
    while i < kayitAdedi:
        isimSoyisim = input("Arada bir boşluk ile isim soyisim giriniz:")
        ögrenciListesi.append(isimSoyisim)
        i += 1
    return ögrenciListesi

def yazdir(liste):
    i = 0
    for i in range(len(liste)):
        print(liste[i])

def ögrenciNoSorgu(isim, soyisim):
    i = 0
    for i in range(len(ögrenciListesi)):
        if (isim+" "+soyisim) == ögrenciListesi[i]:
            print(f"{isim} {soyisim} isimli öğrencinin numarası {i}")
        i += 1    
   
def cokluKayitSil(silmeAdedi):
    i = 0
    while i < silmeAdedi:
        
        ögrenciListesi.remove(ögrenciListesi[int(input("Silinecek ögrencinin numarası: "))])
        i += 1
    return ögrenciListesi    

