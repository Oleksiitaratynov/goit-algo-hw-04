import os

def get_cats_info(filename):
    cats_info = []
    try:
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                cat_info = {
                    "id": cat_data[0],
                    "name": cat_data[1],
                    "age": cat_data[2]
                }
             
                cats_info.append(cat_info)
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print("Помилка при читанні файлу:", e)
    return cats_info

cats_info = get_cats_info("cats_file.txt")
print(cats_info)
