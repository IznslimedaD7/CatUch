import os
import secrets
from flask import current_app
from PIL import Image
from werkzeug.security import generate_password_hash

data_list = {'01': 'января', "02": 'февраля', '03': 'марта', "04": 'апреля', '05': 'мая', "06": 'июня', '07': 'июля', "08": 'августа',
              '09': 'сентября', "10": 'октября', '11': 'ноября', "12": 'декабря',}

def save_file(file, folder, option=False, size=(500, 500)):
    random_hex = secrets.token_hex(16)
    _, f_ext = os.path.splitext(file.filename)
    file_fn = random_hex + f_ext
    full_path = os.path.join(current_app.root_path, 'static', folder)
    file_path = os.path.join(full_path, file_fn)

    if option == True:
        output_size = size
        i = Image.open(file)
        i.thumbnail(output_size)
        i.save(file_path)
    else:
        file.save(file_path)

    return file_fn

def format_data(question):
    new_questions_data = []
    for i in range(0, len(question)):
        data = str(question[i].created_at)
        data = data.split(' ')[0].split('-')
        new_data = f"{int(data[2])} {data_list.get(data[1])} {data[0]}"
        new_questions_data.append(new_data)
    return new_questions_data

