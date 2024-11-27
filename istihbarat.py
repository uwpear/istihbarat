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
 ▒ ░░  ░  ░    ░       ▒ ░ ░  ░░ ░ ░    ░   ░   ░   ░░   ░   ░   ▒    ░      
 ░        ░            ░   ░  ░  ░ ░            ░  ░   ░           ░  ░        
                                        ░                                      
                                                                               
"""
    print(Fore.GREEN + Back.BLACK + banner + Style.RESET_ALL)

# Veritabanına yeni kullanıcı ekleme
def kayit():
    conn = sqlite3.connect('kullanici_bilgileri.db')
    c = conn.cursor()
    
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
    today = datetime.today()
    birth_date = datetime.strptime(dgm_tarih, '%Y-%m-%d')
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    
    c.execute('''
        INSERT INTO bilgiler (ad, soyad, hobi, fobi, meslek, yas, dgm_tarih, sehir, favori_renk, yemek_tercihi, sosyal_medya)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (ad, soyad, hobi, fobi, meslek, age, dgm_tarih, sehir, favori_renk, yemek_tercihi, sosyal_medya))
    
    conn.commit()
    conn.close()
    
    print(f"Bilgiler veritabanına kaydedildi. Yaş: {age}")
        
# Kayıtlı bilgileri görüntüleme
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

# Kişiyi silme
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

# Kişi sayısını gösterme
def kisi_sayisi():
    conn = sqlite3.connect('kullanici_bilgileri.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM bilgiler")
    count = c.fetchone()[0]
    print(f"Kayıtlı kişi sayısı: {count}")
    conn.close()

# Ana döngü
def main():
    show_banner()
    init_db()
    while True:
        print(Fore.CYAN + "HOŞGELDİN KAPTAN!" + Style.RESET_ALL)
        print("Mevcut komutlar: istihbarat, bilgi, ara, sil, say, exit")
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
        elif command == "exit":
            print("Çıkış yapılıyor...")
            sleep(2)
            break
        else:
            print("Bilinmeyen komut!")

if __name__ == "__main__":
    main()
