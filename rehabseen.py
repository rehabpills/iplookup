import requests
import json
import pyfiglet
from colorama import Fore, Back, Style, init
import os

# Инициализация colorama для поддержки цветов в Windows
init()

def clear_screen():
    """Очищает экран консоли."""
    os.system('cls' if os.name == 'nt' else 'clear')

def colored_text(text, color=Fore.WHITE, background=Back.BLACK, style=Style.NORMAL):
    """Возвращает текст с заданным цветом, фоном и стилем."""
    return f"{style}{color}{background}{text}{Style.RESET_ALL}"

def centered_text(text, width):
    """Центрирует текст в заданной ширине."""
    padding = (width - len(text)) // 2
    return " " * padding + text + " " * padding

def print_menu():
    """Печатает главное меню с красивым оформлением."""
    clear_screen()
    width = 80  # Ширина рамки
    print(Fore.CYAN + "=" * width + Style.RESET_ALL)
    ascii_banner = pyfiglet.figlet_format("IP Lookup", font="slant")
    print(colored_text(ascii_banner, color=Fore.GREEN, style=Style.BRIGHT))
    print(colored_text(centered_text("A Powerful IP Information Tool", width), color=Fore.YELLOW, style=Style.BRIGHT))
    print(Fore.CYAN + "=" * width + Style.RESET_ALL)
    print(colored_text(centered_text("1. Lookup IP Address", width), color=Fore.WHITE))
    print(colored_text(centered_text("2. Exit", width), color=Fore.WHITE))
    print(Fore.CYAN + "=" * width + Style.RESET_ALL)


def get_ip_info(ip_address):
    """Получает информацию об IP-адресе."""
    try:
        # Используем ip-api.com, он менее строгий к локальным IP и не требует API key
        url = f"http://ip-api.com/json/{ip_address}"
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses (4XX, 5XX)
        data = response.json()

        # Проверка статуса ответа ip-api.com
        if data.get('status') == 'success':
            return data
        else:
            print(colored_text(f"Error from ip-api.com: {data.get('message', 'Unknown error')}", color=Fore.RED))
            return None

    except requests.exceptions.RequestException as e:
        print(colored_text(f"Error: Could not connect to IP information service. {e}", color=Fore.RED))
        return None
    except json.JSONDecodeError:
        print(colored_text("Error: Could not decode JSON response.", color=Fore.RED))
        return None

def display_ip_info(ip_data):
    """Отображает информацию об IP-адресе с красивым оформлением."""
    if ip_data:
        width = 60
        print(Fore.CYAN + "-" * width + Style.RESET_ALL)
        print(colored_text(centered_text("IP Information", width), color=Fore.BLUE, style=Style.BRIGHT))
        print(Fore.CYAN + "-" * width + Style.RESET_ALL)

        # Выводим данные с использованием форматирования
        print(colored_text(f"IP Address: {ip_data.get('query', 'N/A')}", color=Fore.GREEN))  # Используем 'query' вместо 'ip'
        print(colored_text(f"Country: {ip_data.get('country', 'N/A')}", color=Fore.GREEN))
        print(colored_text(f"Country Code: {ip_data.get('countryCode', 'N/A')}", color=Fore.GREEN))
        print(colored_text(f"Region: {ip_data.get('regionName', 'N/A')}", color=Fore.GREEN)) # Используем 'regionName'
        print(colored_text(f"City: {ip_data.get('city', 'N/A')}", color=Fore.GREEN))
        print(colored_text(f"Zip Code: {ip_data.get('zip', 'N/A')}", color=Fore.GREEN))
        print(colored_text(f"Latitude: {ip_data.get('lat', 'N/A')}", color=Fore.GREEN))
        print(colored_text(f"Longitude: {ip_data.get('lon', 'N/A')}", color=Fore.GREEN))
        print(colored_text(f"Timezone: {ip_data.get('timezone', 'N/A')}", color=Fore.GREEN))
        print(colored_text(f"ISP: {ip_data.get('isp', 'N/A')}", color=Fore.GREEN)) # Добавлено ISP (провайдер)
        print(colored_text(f"Organization: {ip_data.get('org', 'N/A')}", color=Fore.GREEN)) # Добавлено Organization
        print(colored_text(f"AS: {ip_data.get('as', 'N/A')}", color=Fore.GREEN)) # Добавлено AS (номер автономной системы)

        print(Fore.CYAN + "-" * width + Style.RESET_ALL)
    else:
        print(colored_text("No information found for this IP address.", color=Fore.RED))


def main():
    """Главная функция."""
    while True:
        print_menu()
        choice = input(colored_text("Enter your choice (1 or 2): ", color=Fore.YELLOW))

        if choice == '1':
            ip_address = input(colored_text("Enter IP address: ", color=Fore.YELLOW))
            ip_info = get_ip_info(ip_address)
            display_ip_info(ip_info)
            input(colored_text("Press Enter to continue...", color=Fore.WHITE))  # Пауза
        elif choice == '2':
            print(colored_text("Exiting...", color=Fore.YELLOW))
            break
        else:
            print(colored_text("Invalid choice. Please try again.", color=Fore.RED))


if __name__ == "__main__":
    main()