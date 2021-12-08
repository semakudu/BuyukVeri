def evleri_listele(baglanti,listele):
    eylem = baglanti.cursor()
    komut = listele
    eylem.execute(komut)
    return eylem

def evleri_ekle(baglanti,ekle):
    eylem2 = baglanti.cursor()
    komut2 = ekle
    eylem2.execute(komut2)
    return eylem2

def evleri_sil(baglanti,sil):
    eylem3 = baglanti.cursor()
    komut3 = sil
    eylem3.execute(komut3)
    return eylem3

def evleri_guncelle(baglanti,guncelle):
    eylem4 = baglanti.cursor()
    komut4 = guncelle
    eylem4.execute(komut4)
    return eylem4

def evleri_getir(baglanti, getir):
    eylem5 = baglanti.cursor()
    komut5 = getir
    eylem5.execute(komut5)
    return eylem5
