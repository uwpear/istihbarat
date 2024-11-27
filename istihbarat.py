import os
import sqlite3
from colorama import Fore, Back, init, Style
from time import sleep
from datetime import datetime

# Veritabanı bağlantısı ve tablo oluşturma
def init_db():
    conn = sqlite3.connect('kullanici_bilgileri.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS bilgiler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ad TEXT,
            soyad TEXT,
            hobi TEXT,
            fobi TEXT,
            meslek TEXT,
            yas INTEGER,
            dgm_tarih TEXT,
            sehir TEXT,
            favori_renk TEXT,
            yemek_tercihi TEXT,
            sosyal_medya TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Banner gösterimi
def show_banner():
    banner = """
 ██▓  ██████ ▄▄▄█████▓ ██▓ ██░ ██  ▄▄▄▄    ▄▄▄       ██▀███   ▄▄▄     ▄▄▄█████▓
▓██▒▒██    ▒ ▓  ██▒ ▓▒▓██▒▓██░ ██▒▓█████▄ ▒████▄    ▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒
▒██▒░ ▓██▄   ▒ ▓██░ ▒░▒██▒▒██▀▀██░▒██▒ ▄██▒██  ▀█▄  ▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░
░██░  ▒   ██▒░ ▓██▓ ░ ░██░░▓█ ░██ ▒██░█▀  ░██▄▄▄▄██ ▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ 
░██░▒██████▒▒  ▒██▒ ░ ░██░░▓█▒░██▓░▓█  ▀█▓ ▓█   ▓██▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ 
░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   ░▓   ▒ ░░▒░▒░▒▓███▀▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   
 ▒ ░░ ░▒  ░ ░    ░     ▒ ░ ▒ ░▒░ ░▒░▒   ░   ▒   ▒▒ ░  ░▒ ░ ▒░  ▒   ▒▒ ░   ░    
 ░        ░            ░   ░  ░  ░ ░    ░   ░   ░   ░░   ░   ░   ▒    ░      
 ░        ░            ░   ░  ░  ░ ░            ░  ░   ░           ░  ░        
                                        ░                                      
                                                                               
"""
    print(Fore.GREEN + Back.BLACK + banner + Style.RESET_ALL)

# Veritabanına yeni kullanıcı ekleme işlemini yapıyoruz burada
def kayit():
    conn = sqlite3.connect('kullanici_bilgileri.db')
    c = conn.cursor()
    
    # Kullanıcı bilgilerini alma
    ad = input("Adı: ")
    soyad = input("Soyadı: ")
    hobi = input("Hobisi: ")
    fobi = input("Fobisi: ")
    meslek = input("Mesleği: ")
    dgm_tarih = input("Doğum Tarihi (YYYY-MM-DD): ")
    sehir = input("Şehir: ")
    favori_renk = input("Favori Renk: ")
    yemek_tercihi = input("Yemek Tercihi: ")
    sosyal_medya = input("Sosyal Medya Hesapları (varsa): ")
    
    # Yaş hesaplaması
    bugün = datetime.today()
    dogum_tarih = datetime.strptime(dgm_tarih, '%Y-%m-%d')
    yas = bugün.year - dogum_tarih.year - ((bugün.month, bugün.day) < (dogum_tarih.month, dogum_tarih.day))
    
    c.execute('''
        INSERT INTO bilgiler (ad, soyad, hobi, fobi, meslek, yas, dgm_tarih, sehir, favori_renk, yemek_tercihi, sosyal_medya)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (ad, soyad, hobi, fobi, meslek, yas, dgm_tarih, sehir, favori_renk, yemek_tercihi, sosyal_medya))
    
    conn.commit()
    conn.close()
    
    print(f"Bilgiler veritabanına kaydedildi. Yaş: {yas}")
    
    # Sosyal medya ve kullanıcı adı ile wordlist oluşturma
    wordlist = olustur_wordlist(ad, soyad, yas, dgm_tarih, sehir, sosyal_medya, meslek, favori_renk)
    dosya_adi = dosya_adini_kontrol_et()
    wordlist_dosyaya_yaz(dosya_adi, wordlist)
    print(f"Wordlist '{dosya_adi}' dosyasına kaydedildi.")

# Kullanıcıya özel Wordlist oluşturma 
def olustur_wordlist(ad, soyad, yas, dgm_tarih, sehir, sosyal_medya, meslek, favori_renk):
    # Güncel yıl bilgisini almak için datetime kullanıyoruz
    yil = datetime.now().year
    
    wordlist = []
    
    wordlist.append(ad.lower() + "1234")   # kullanıcı adı + sayılar
    wordlist.append(ad[::-1] + str(yil))   # ters kullanıcı adı + yıl
    wordlist.append(sosyal_medya.lower() + "@" + ad.lower())  # sosyal medya + kullanıcı adı + @
    wordlist.append(ad.lower() + sosyal_medya.lower())  # kullanıcı adı + sosyal medya
    wordlist.append(soyad.lower() + "2024")  # soyad + yıl
    wordlist.append(favori_renk.lower() + ad.lower())  # favori renk + kullanıcı adı
    wordlist.append(sehir.lower() + str(yil))  # şehir + yıl
    wordlist.append(meslek.lower() + ad.lower())  # meslek + kullanıcı adı
    wordlist.append(str(yas) + ad.lower())  # yaş + kullanıcı adı
    wordlist.append(str(yil) + soyad.lower())  # yıl + soyad
    wordlist.append(ad.lower() + str(yas))  # kullanıcı adı + yaş
    wordlist.append(ad.lower() + sosyal_medya.lower() + str(yil))  # kullanıcı adı + sosyal medya + yıl
    wordlist.append(sosyal_medya.lower() + str(yil))  # sosyal medya + yıl
    wordlist.append(sehir.lower() + sosyal_medya.lower())  # şehir + sosyal medya
    
    return '\n'.join(wordlist)

def dosya_adini_kontrol_et():
    dosya_adi = "wordlist.txt"
    sayac = 1
    
    # eğer wordlist.txt varsa, dosya ismini artırarak kontrol et
    while os.path.exists(dosya_adi):
        dosya_adi = f"wordlist{sayac}.txt"
        sayac += 1
    
    return dosya_adi

def wordlist_dosyaya_yaz(dosya_adi, wordlist):
    with open(dosya_adi, 'w') as f:
        f.write(wordlist)

def wordlist_goruntule():
    print("\nMevcut wordlist dosyaları:")
    dosya_adi = "wordlist.txt"
    sayac = 0
    dosya_listesi = []

    while os.path.exists(dosya_adi):
        dosya_listesi.append(dosya_adi)
        sayac += 1
        dosya_adi = f"wordlist{sayac}.txt"  

    if dosya_listesi:
        for i, dosya in enumerate(dosya_listesi, 1):
            print(f"{i}. {dosya}")
        
        secim = input("\nSeçmek istediğiniz wordlist dosyasının tam adını yazın (örn: wordlist.txt): ").strip()
        
        if secim in dosya_listesi:
            # dosya görüntüleme
            with open(secim, 'r') as file:
                print("\nWordlist içeriği:")
                print(file.read())
        else:
            print("Geçersiz dosya adı!")
    else:
        print("Henüz oluşturulmuş bir wordlist dosyası yok.")



def goruntule():
    conn = sqlite3.connect('kullanici_bilgileri.db')
    c = conn.cursor()
    c.execute("SELECT * FROM bilgiler")
    records = c.fetchall()
    
    if records:
        print(Fore.YELLOW + "\nKayıtlı Bilgiler:\n" + Style.RESET_ALL)
        for record in records:
            print(f"ID: {record[0]}, Ad: {record[1]}, Soyad: {record[2]}, Yaş: {record[6]}, Şehir: {record[7]}")
    else:
        print("Henüz kayıtlı bilgi bulunmuyor.")
    conn.close()

# Arama fonksiyonu (ad ile)
def ara():
    aranan_ad = input("Aramak istediğiniz kişinin adı: ").strip()
    conn = sqlite3.connect('kullanici_bilgileri.db')
    c = conn.cursor()
    c.execute("SELECT * FROM bilgiler WHERE ad LIKE ?", ('%' + aranan_ad + '%',))
    records = c.fetchall()
    
    if records:
        print(Fore.GREEN + "\nAranan Kişi:\n" + Style.RESET_ALL)
        for record in records:
            print(f"ID: {record[0]}, Ad: {record[1]}, Soyad: {record[2]}, Yaş: {record[6]}, Şehir: {record[7]}")
    else:
        print("Kayıt bulunamadı.")
    
    conn.close()

def sil():
    sil_ad = input("Silmek istediğiniz kişinin adı: ").strip()
    conn = sqlite3.connect('kullanici_bilgileri.db')
    c = conn.cursor()
    c.execute("DELETE FROM bilgiler WHERE ad LIKE ?", ('%' + sil_ad + '%',))
    
    if c.rowcount > 0:
        print(f"{sil_ad} adlı kişi silindi.")
    else:
        print("Kayıt bulunamadı.")
    
    conn.commit()
    conn.close()

def kisi_sayisi():
    conn = sqlite3.connect('kullanici_bilgileri.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM bilgiler")
    count = c.fetchone()[0]
    print(f"Kayıtlı kişi sayısı: {count}")
    conn.close()

def main():
    show_banner()
    init_db()
    while True:
        print(Fore.CYAN + "HOŞGELDİN KAPTAN!" + Style.RESET_ALL)
        print("Mevcut komutlar: istihbarat, bilgi, ara, sil, say, wordlist, exit")
        command = input(">> ")

        if command == "istihbarat":
            kayit()
        elif command == "bilgi":
            goruntule()
        elif command == "ara":
            ara()
        elif command == "sil":
            sil()
        elif command == "say":
            kisi_sayisi()
        elif command == "wordlist":
            wordlist_goruntule()
        elif command == "exit":
            print("Çıkış yapılıyor...")
            sleep(2)
            break
        else:
            print("Bilinmeyen komut!")

if __name__ == "__main__":
    main()
