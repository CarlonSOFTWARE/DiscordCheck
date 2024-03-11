import requests
import random
import string
import os
import pyfiglet
from termcolor import colored

try:
    from colorama import init, Fore
    init(autoreset=True)
except ImportError:
    print("Colorama kütüphanesi bulunamadı. Lütfen yükleyin: pip install colorama")
    exit()

def check_token(token):
    headers = {
        "Authorization": token
    }
    response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
    if response.status_code == 200:
        print(colored("Token geçerli: " + token, "green"))
        return True
    else:
        print(colored("Token geçersiz: " + token, "red"))
        return False

def generate_random_token():
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(59)) + '.' + random.choice(string.ascii_letters + string.digits)

def print_banner():
    ascii_banner = pyfiglet.figlet_format("Discord Token +", font="slant")
    
    colored_banner = colored(ascii_banner, color="red")
    print(colored_banner)
    print(colored("\n                                          Geliştirici: Carlon", "green"))

    print(colored("\n                                          https://github.com/CarlonSOFTWARE", "green"))

def check_tokens_from_file():
    file_path = input("\nDosya yolunu girin: ")
    try:
        with open(file_path, "r") as file:
            tokens = file.readlines()
            for token in tokens:
                token = token.strip()  
                check_token(token)
    except FileNotFoundError:
        print("Dosya bulunamadı!")

def main():
    os.system("clear")
    valid_tokens = []  
    print_banner()
    
    while True:
        print("[1] Dosyadan Tokenleri Kontrol Et")
        print("[2] Kaydedilmiş Tokenleri Göster")
        print("[3] Rastgele Token Oluştur")
        print("[4] Çıkış")
        
        choice = input("\nSeçiminizi yapın: ")
        
        if choice == "1":
            check_tokens_from_file()
            input("\nAna menüye dönmek için herhangi bir tuşa basın...")
            os.system("clear")
            print_banner()
        elif choice == "2":
            print("\nKaydedilmiş Tokenler:")
            for token in valid_tokens:
                print(token)
            input("\nAna menüye dönmek için herhangi bir tuşa basın...")
            os.system("clear")
            print_banner()
        elif choice == "3":
            token_sayısı = int(input("\nKaç token oluşturmak istiyorsunuz? "))
            for _ in range(token_sayısı):
                random_token = generate_random_token()
                try:
                    check_token(random_token)
                    valid_tokens.append(random_token)  
                except Exception as e:
                    print(f"Hata oluştu: {e}")
            input("\nDevam etmek için herhangi bir tuşa basın...")
            os.system("clear")
            print_banner()
        elif choice == "4":
            with open("tokenler.txt", "w") as file:
                for token in valid_tokens:
                    file.write(token + "\n")  
            print("\nGeçerli tokenler kaydedildi!.")
            break
        else:
            print("\nGeçersiz seçim. Tekrar deneyin.")
        input("\nAna menüye dönmek için herhangi bir tuşa basın...")
        os.system("clear")
        print_banner()

if __name__ == "__main__":
    main()
