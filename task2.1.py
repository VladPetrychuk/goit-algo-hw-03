def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary_str = line.strip().split(',')
                salary = int(salary_str)
                total += salary
                count += 1
        average = total / count if count > 0 else 0
        return total, average
    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0
    except Exception as e:
        print("Помилка при обробці файлу:", e)
        return 0, 0
    
total, average = total_salary("hw2/sallary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")