import os

def total_salary(filename):
    total_salary = 0
    count = 0

    try:
        filepath = os.path.join(os.path.dirname(__file__), filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    total_salary += int(salary)
                    count += 1
                except ValueError:
                    print(f"Помилка: некоректні дані у файлі на рядку '{line.strip()}'")

        if count == 0:
            return 0, 0  
        average_salary = int(total_salary / count)
        return total_salary, average_salary
    except FileNotFoundError:
        print("Помилка: файл не знайдено")
        return None, None
    except Exception as e:
        print(f"Помилка: {e}")
        return None, None


total, average = total_salary("salary_file.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
