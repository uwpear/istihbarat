import os
from colorama import Fore, Back, init, Style
from time import sleep

os.system("clear") if os.name == "posix" else os.system("cls")
init()

def show_banner():
    banner = """
 ██▓  ██████ ▄▄▄█████▓ ██▓ ██░ ██  ▄▄▄▄    ▄▄▄       ██▀███   ▄▄▄     ▄▄▄█████▓
▓██▒▒██    ▒ ▓  ██▒ ▓▒▓██▒▓██░ ██▒▓█████▄ ▒████▄    ▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒
▒██▒░ ▓██▄   ▒ ▓██░ ▒░▒██▒▒██▀▀██░▒██▒ ▄██▒██  ▀█▄  ▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░
░██░  ▒   ██▒░ ▓██▓ ░ ░██░░▓█ ░██ ▒██░█▀  ░██▄▄▄▄██ ▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ 
░██░▒██████▒▒  ▒██▒ ░ ░██░░▓█▒░██▓░▓█  ▀█▓ ▓█   ▓██▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ 
░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   ░▓   ▒ ░░▒░▒░▒▓███▀▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   
 ▒ ░░ ░▒  ░ ░    ░     ▒ ░ ▒ ░▒░ ░▒░▒   ░   ▒   ▒▒ ░  ░▒ ░ ▒░  ▒   ▒▒ ░   ░    
 ▒ ░░  ░  ░    ░       ▒ ░ ░  ░░ ░ ░    ░   ░   ▒     ░░   ░   ░   ▒    ░      
 ░        ░            ░   ░  ░  ░ ░            ░  ░   ░           ░  ░        
                                        ░                                      
                                                                               
"""
    print(Fore.GREEN + Back.BLACK + banner + Style.RESET_ALL)

show_banner()

def kayit():
    while True:
        ad = input("Adı: ")
        soyad = input("Soyadı: ")
        hobi = input("Hobisi: ")
        fobi = input("Fobisi: ")
        meslek = input("Mesleği: ")
        yas = input("Yaşı: ")
        dgm_tarih = input("Doğum Tarihi: ")
        sehir = input("Şehir: ")
        favori_renk = input("Favori Renk: ")
        yemek_tercihi = input("Yemek Tercihi: ")
        sosyal_medya = input("Sosyal Medya Hesapları (varsa): ")
        
        with open("bilgiler.txt", "a") as file:
            file.write(f"Adı: {ad}\n")
            file.write(f"Soyadı: {soyad}\n")
            file.write(f"Hobisi: {hobi}\n")
            file.write(f"Fobisi: {fobi}\n")
            file.write(f"Mesleği: {meslek}\n")
            file.write(f"Yaşı: {yas}\n")
            file.write(f"Doğum Tarihi: {dgm_tarih}\n")
            file.write(f"Şehir: {sehir}\n")
            file.write(f"Favori Renk: {favori_renk}\n")
            file.write(f"Yemek Tercihi: {yemek_tercihi}\n")
            file.write(f"Sosyal Medya Hesapları: {sosyal_medya}\n")
            file.write("\n--------------------------------------\n") 

        print(f"Bilgiler 'bilgiler.txt' dosyasına kaydedildi.\n")
        
        devam = input("Başka bir kişi hakkında bilgi girmek ister misin? (Evet/Hayır): ").strip().lower()
        if devam != 'evet':
            break

    print("Girdiğin bilgileri kaydetmeyi tamamladın.")

def goruntule():
    try:
        with open("bilgiler.txt", "r") as file:
            data = file.read()
            if data:
                print(Fore.YELLOW + "\nKayıtlı Bilgiler:\n" + Style.RESET_ALL)
                print(data)
            else:
                print("Henüz kayıtlı bilgi bulunmuyor.")
    except FileNotFoundError:
        print("Henüz bilgiler.txt dosyası oluşturulmadı. Önce veri kaydedin.")

def ara():
    aranan_ad = input("Aramak istediğiniz kişinin adı: ").strip()
    aranan_bulundu = False
    try:
        with open("bilgiler.txt", "r") as file:
            kayitlar = file.read().split("--------------------------------------\n")
            for kayit in kayitlar:
                if aranan_ad in kayit:
                    print(Fore.GREEN + "\nAranan Kişi:\n" + Style.RESET_ALL)
                    print(kayit)
                    aranan_bulundu = True
                    break
            if not aranan_bulundu:
                print("Kayıt bulunamadı.")
    except FileNotFoundError:
        print("Henüz bilgiler.txt dosyası oluşturulmadı.")

def sil():
    sil_ad = input("Silmek istediğiniz kişinin adı: ").strip()
    kayit_silindi = False
    try:
        with open("bilgiler.txt", "r") as file:
            kayitlar = file.read().split("--------------------------------------\n")
        with open("bilgiler.txt", "w") as file:
            for kayit in kayitlar:
                if sil_ad not in kayit:
                    file.write(kayit + "\n--------------------------------------\n")
                else:
                    kayit_silindi = True
        if kayit_silindi:
            print(f"{sil_ad} adlı kişinin kaydı silindi.")
        else:
            print("Kayıt bulunamadı.")
    except FileNotFoundError:
        print("Henüz bilgiler.txt dosyası oluşturulmadı.")

def kisi_sayisi():
    try:
        with open("bilgiler.txt", "r") as file:
            kayitlar = file.read().split("--------------------------------------\n")
            kisi_sayisi = len([k for k in kayitlar if k.strip()])  # Boş kayıtları saymıyoruz
            print(f"Kayıtlı kişi sayısı: {kisi_sayisi}")
    except FileNotFoundError:
        print("Henüz bilgiler.txt dosyası oluşturulmadı.")

while True:
    print(Fore.CYAN + "HOŞGELDİN KAPTAN!" + Style.RESET_ALL)
    print("")
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
