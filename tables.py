import gspread
from oauth2client.service_account import ServiceAccountCredentials
import logging
import os

logging.basicConfig(level=logging.INFO)

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
script_directory = os.path.dirname(os.path.abspath(__file__))
file_name = 'my-project-447908-1d8990ec2b4f.json'
file_path = os.path.join(script_directory, file_name)

# учетные данные для поключения
creds = ServiceAccountCredentials.from_json_keyfile_name(file_path, scope)

# Авторизуия
client = gspread.authorize(creds)
# Откройтие таблицы по имени
sheet = client.open("Конфиренция 2025").sheet1


def insert_row_teble(row):
    row_arr = [row]
    # Заполнение ячейки
    sheet.append_row(row_arr)
    row_arr = []

