# Что делает
Скрипт принимает на вход ссылку пользователя и, если она длинная - создает битлинк (укороченную ссылку), если
пользователь ввел битлинк, то выдает сумму кликов по ссылке за все дни.

# Как запустить
Для запуска требуется установленный Python версии 3.6 и выше и macOS или Linux

- Скачайте код
- Установите зависимости из requirements.txt
```
pip install -r requirements.txt
```
- Зарегистрируйтесь на https://bitly.com, получите Access token в 
- в <a href="https://app.bitly.com/settings/api/" target="_blank">личном кабинете</a>
- Создайте файл .env и поместите туда свой API-токен TOKEN=token
- Запустите программу:
```
python clicks_count.py
```
- Вставьте ссылку;
# Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org. 