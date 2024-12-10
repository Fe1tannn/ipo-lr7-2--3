import json
with open("dota.json", 'r', encoding='utf-8') as file: 
    flower_data = json.load(file) 
    count = 0
    close = True
    def menu():
        print("""
        1: Вывести все записи n
        2: Вывести запись по полю n
        3: Добавить запись n
        4: Удалить запись по полю n
        5: Выйти из программы
        """)    
    def out_all():
        global count
        for flower in flower_data:
            print(f"""
                Код: {flower['id']}, 
                Название: {flower['name']},                       
                Латинское название: {flower['latin_name']}, 
                Красно-книжная: {flower['is_red_book_flower']},    
                Стоимость: {flower['price']} 
                """)
            count += 1
    def out_index():
        global count
        id_num = int(input("Введите номер цветка: "))
        bools = False  
        i = 0  
        for flower in flower_data:
            if id_num == flower['id']:
                print(f"""
                Название: {flower['name']},                       
                Латинское название: {flower['latin_name']}, 
                Красно-книжная: {flower['is_red_book_flower']},    
                Стоимость: {flower['price']} 
                Индекс в списке: {i}
                """)
                bools = True  
                break  
            i += 1
        count += 1
        if not bools:
            print("Запись не найдена.")
    def input_new():
        global count
        ids = int(input("Введите номер цветка: "))     
        exists = False
        for flower in flower_data:
            if flower['id'] == ids:
                exists = True
                break
        if exists:
            print("Ошибка: цветкок с таким номером уже существует.")
        else:
            name = input("Введите имя цветка: ")  
            latin_name = input("Введите латинское имя: ")  
            is_red_book_flower = input("Введите, является ли цветок красно-книжным (да/нет): ")  
            price = float(input("Введите стоимость цветка: "))  
            new_flower = {
                'id': ids,
                'name': name,
                'is_red_book_flower': is_red_book_flower,
                'is_petrol': True if is_red_book_flower.lower() == 'да' else False, 
                'price': price
            }

            flower_data.append(new_flower) 
            with open("dota.json", 'w', encoding='utf-8') as output_file: 
                json.dump(flower_data, output_file, ensure_ascii = False, indent = 2)
            print("Цветок успешно добавлена.")
        count += 1
    def del_id():
            global count
            id_del = int(input("Введите номер цветка: "))
            bools = False  
            for flower in flower_data:
                if id_del == flower['id']:
                    flower_data.remove(flower)  
                    bools = True  
                    break 
            if not bools:
                print("Запись не найдена.")
            else:
                with open("dota.json", 'w', encoding='utf-8') as output_file:
                    json.dump(flower_data, output_file, ensure_ascii = False, indent = 2)
                print("цветок успешно удалена.")
            count += 1
    def leave():
        global count
        global close
        print(f"Программа завершена. Количество выполненных операций с записями равно: {count}")
        close = False 
def main():
    while close:
        menu()
        point = int(input("Введите номер действия, которое хотите выполнить: "))
        if point == 1:
            out_all()
        elif point == 2:
            out_index()
        elif point == 3:
            input_new()
        elif point == 4:
           del_id()
        elif point == 5:
            leave()
        else:
            print("Некорректный ввод. Пожалуйста, выберите номер от 1 до 5.")
main()      
