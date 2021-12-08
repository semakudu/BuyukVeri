import function
import sqlite3

baglanti=sqlite3.connect("evler.db")

komut="CREATE TABLE IF NOT EXISTS evler(Yapi text, Mimar text, Renk text, Fiyat int)"
baglanti.commit()

komut2= "INSERT INTO from evler where Mimar"
function.evleri_ekle()
baglanti.commit()

komut3= "DELETE from evler where Yapi"
function.evleri_sil()
baglanti.commit()

komut4= "UPDATE evler WHERE Fiyat=?"
function.evleri_guncelle()
baglanti.commit()

komut5 = "Select * from evler"
function.evleri_getir()
baglanti.commit()

baglanti.close()
