import os
import secrets

try:
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
except ImportError:
    print("Ошибка: Нужно установить библиотеку! / Error: Library required!")
    print("Выполни команду: pip install pycryptodome")
    exit()

# КЛЮЧ ШИФРОВАНИЯ (MASTER KEY) - Не менять!
MASTER_KEY = bytes([102, 213, 122, 113, 226, 89, 169, 26, 130, 132, 188, 167, 10, 45, 6, 6, 121, 122, 150, 83, 91, 70, 132, 153, 161, 61, 144, 105, 181, 62, 72, 144])

# --- НАСТРОЙКИ ПУТЕЙ / PATH SETTINGS ---

# RU_SOURCE: Папка, где лежат твои готовые переведенные JSON
# RU_SOURCE: Folder where your translated JSON files are located
RU_SOURCE = r"C:\path\to\your\translated\json" 

# DOCS_PATH: Путь к папке игры в Документах (замени 'your_id' на цифры своего Steam ID)
# DOCS_PATH: Path to the game folder in Documents (replace 'your_id' with your Steam ID)
DOCS_PATH = r"C:\Users\User\Documents\My Games\FF7EC\Steam\your_id\LocalizeText\En"

# ---------------------------------------

def encrypt_file(data, key):
    # Создаем случайный IV (16 байт) для шифрования CBC
    iv = secrets.token_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Дополняем данные до кратности 16 байт (PKCS7 Padding)
    padded_data = pad(data, AES.block_size)
    encrypted_payload = cipher.encrypt(padded_data)
    # Итоговый файл = IV + Зашифрованные данные
    return iv + encrypted_payload

def run_packer():
    print(r"""
    #################################################
    #                                               #
    #      FF7 EVER CRISIS JSON ENCRYPTOR           #
    #    (Convert your JSON to Game Format)         #
    #             by PIXELPASHA                     #
    #                                               #
    #################################################
    """)
    
    # Проверка наличия папок
    if not os.path.exists(RU_SOURCE):
        print(f"[ОШИБКА/ERROR] Папка с JSON не найдена: {RU_SOURCE}")
        print("Отредактируйте путь RU_SOURCE в коде скрипта!")
        return
    
    if not os.path.exists(DOCS_PATH):
        print(f"[ИНФО/INFO] Создаю папку назначения: {DOCS_PATH}")
        os.makedirs(DOCS_PATH, exist_ok=True)

    # Собираем список всех JSON файлов
    files = [f for f in os.listdir(RU_SOURCE) if f.endswith(".json")]
    if not files:
        print("[ОШИБКА/ERROR] В папке RU_SOURCE нет файлов .json!")
        return

    print(f"[СТАРТ] Найдено файлов: {len(files)}. Начинаю упаковку...\n")

    for filename in files:
        src_path = os.path.join(RU_SOURCE, filename)
        dest_path = os.path.join(DOCS_PATH, filename)
        
        try:
            with open(src_path, "rb") as f:
                raw_content = f.read()
            
            if not raw_content:
                continue

            # Шифруем данные
            encrypted_blob = encrypt_file(raw_content, MASTER_KEY)
            
            with open(dest_path, "wb") as f:
                f.write(encrypted_blob)
            
            print(f"  [+] Успешно упакован: {filename}")
        except Exception as e:
            print(f"  [-] Ошибка в файле {filename}: {e}")
            
    print("\n" + "="*50)
    print("      SUCCESS: ALL FILES ENCRYPTED & PACKED!")
    print("      WORK FINISHED BY PIXELPASHA")
    print("="*50)

if __name__ == "__main__":
    run_packer()