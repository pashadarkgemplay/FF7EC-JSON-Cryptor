# FF7 Ever Crisis JSON Encryptor v0.2
**Developed by PIXELPASHA**

Этот инструмент предназначен для шифрования JSON файлов перевода в формат, который понимает игра Final Fantasy VII: Ever Crisis (Steam версия).

## Особенности / Features:
- **AES-CBC Encryption:** Использует оригинальный алгоритм игры.
- **Auto-folder creation:** Сам создает нужные пути в Документах.
- **Simple use:** Достаточно указать пути в коде.

## Как использовать / How to use:
1. Установите библиотеку: `pip install pycryptodome`
2. Откройте `ff7ec_encryptor.py` через блокнот или VS Code.
3. Укажите ваш путь к JSON в `RU_SOURCE` и путь к папке игры в `DOCS_PATH`.
4. Запустите скрипт: `python ff7ec_encryptor.py`

## Credits:
- **Author:** PIXELPASHA
- **Community:** Ever Crisis Localization Team