import re
def select(input_func):
    def output_func():
        print("="*50)
        input_func()
        print("=" *50)

    return output_func


regular_menu={
        'Маргарита':{'цена': 450,
                     'описание': 'томатный соус, моцарелла, базилик',
                     "ингредиенты":['соус','моцарелла','базилик']},
        'Пепперони':{'цена': 550,
                     'описание': 'томатный соус, моцарелла, пепперони',
                     "ингредиенты":['соус','моцарелла','пепперони']},
        'Гавайская':{'цена': 500,
                     'описание': 'томатный соус, моцарелла, ветчина, ананасы',
                     "ингредиенты":['соус','моцарелла','ветчина','ананасы']},
        'Четыре сыра':{'цена': 600,
                       'описание': 'моцарелла, горгонзола, пармезан, чеддер',
                       "ингридиенты":['соус','моцарелла','горгонзола','пармезан','чеддер']}
    }

adult_menu = {
        'Маргарита':{'цена': 650,
                     'описание': 'томатный соус, моцарелла, базилик (большая порция)',
                     "ингредиенты":['соус','моцарелла','базилик']},
        'Пепперони':{'цена': 750,
                     'описание': 'томатный соус, моцарелла, пепперони (двойная порция)',
                     "ингредиенты":['соус','моцарелла','пепперони']},
        'Гавайская':{'цена': 700,
                     'описание': 'томатный соус, моцарелла, ветчина, ананасы (большая порция)',
                     "ингредиенты":['соус','моцарелла','ветчина','ананасы']},
        'Четыре сыра':{'цена': 800,
                       'описание': 'моцарелла, горгонзола, пармезан, чеддер (двойная порция)',
                       "ингридиенты": ['соус', 'моцарелла', 'горгонзола', 'пармезан', 'чеддер']
                       },
        'Острая':{'цена': 750,
                  'описание': 'томатный соус, моцарелла, салями, перец чили',
                  "ингридиенты": ['соус', 'моцарелла', 'салями', 'перец']
                  }
}
drinks={
    "вода": 100,
    "сок яблочный": 250,
    "кола":299,
    "спрайт":299,
    "фанта":299
}

topping={
    'сыр':50,
    'ветчина':70,
    'грибы':60,
    'оливки':40,
    'перец':50,
    'ананасы':80,
    'пепперони':90
}
stock = {
    'соус': 5, 'моцарелла': 10, 'базилик': 3, 'пепперони': 4, 'ветчина': 4, 'ананасы': 3,
    'горгонзола': 2, 'пармезан': 2, 'чеддер': 2, 'салями': 3, 'перец чили': 2,
    'вода': 10, 'сок яблочный': 8, 'кола': 8, 'спрайт': 8, 'фанта': 8
}
phone_pattern=re.compile(r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$')
email_patter=re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

user_data = {}
order = []
total_amount = 0
current_menu = {}
def chek_ingridients(ingridients):
    for item in ingridients:
        if item not in stock or stock[item] <=0:
            print(f"Простите но вы не сможете сделать заказ так как у нас нет {item}")
            return False
    for item in ingridients:
        stock[item] -=1
        return True
print("=== Добро пожаловать в пиццерию 'pizza hut'! ===")
while True:
    fio=input("введите имя фамилию отчество\n")
    pattern =re.compile(r"^[А-ЯЁ][а-яё]+(?:-[А-ЯЁ][а-яё]+)*\s+[А-ЯЁ][а-яё]+(?:-[А-ЯЁ][а-яё]+)*\s+[А-ЯЁ][а-яё]+(?:-[А-ЯЁ][а-яё]+)*$")
    if pattern.match(fio):
        print("ваше имя фамилия отчество добавлено")
        user_data['фио'] =fio
        break
    else:
        print("ведите нормальное фио")


while True:
    try:
        age = int(input("Введите ваш возраст\n"))
        if age > 0 and age < 100:
            user_data['возраст'] = age
            break
        else:
            print("Пожалуйста, введите корректный возраст!")
    except ValueError:
        print("Пожалуйста, введите число!")
print(f"\n=== Приветствуем,{user_data['фио']}!===")
if user_data['возраст'] >= 18:
    print("Вам доступно взрослое меню с увеличенными порциями!")
    current_menu = adult_menu
else:
    print("Вам доступно стандартное меню.")
    current_menu = regular_menu
while True:
    phone = input("введите номер телефона")
    if phone_pattern.match(phone):
        user_data['телефон'] =phone
        break
    else:
        print("вы вели неправильный номер")
while True:
    email_user = input("введите почту\n")
    if email_patter.match(email_user):
        user_data['email']=email_user
        break
    else:
        print("вы вели неправильную почту")

print("\nНАШЕ МЕНЮ")
print("\nПИЦЦЫ")
for pizza, price in current_menu.items():
    print(f"{pizza} : {price['описание']} : {price['цена']}")

print("\nНАПИТКИ")
for drink, price in drinks.items():
    print(f"{drink}: {price} руб")


print("\n=== ОФОРМЛЕНИЕ ЗАКАЗА ===")

while True:
    print("\n1 - Выбрать готовую пиццу")
    print("2 - Создать кастомную пиццу")
    print("3 - Выбрать напиток")
    print("4 - Завершить заказ")

    choice = input("Выберите что хотите сделать\n")

    if choice == '1':
        print("\n=== ВЫБОР ПИЦЦЫ ===")
        for pizza, price in current_menu.items():
            print(f"{pizza} : {price['описание']} : {price['цена']}")
        user_pizza=input("выберите себе какую нибудь пиццу ")
        if user_pizza in current_menu.keys():
            ingridients=current_menu[user_pizza]['ингредиенты']
            if chek_ingridients(ingridients):
                print("выша пицца добавлена")
                total_amount +=current_menu[user_pizza]['цена']
                order.append({
                    "название": user_pizza,
                    "цена": current_menu[user_pizza]['цена'],
                    "тип": "пицца"
                })
        else:
            print("пицца не добавлена")

    elif choice == '2':
        print("\n=== СОЗДАНИЕ КАСТОМНОЙ ПИЦЦЫ===")
        base_price = 400
        custom_price = base_price
        selected_toppings = []

        print("Доступные начинки:")
        for toppin, price in topping.items():
            print(f"{toppin}: +{price} руб.")

        print(f"\nБазовая цена пиццы: {base_price} руб.")

        while True:
            print(f"\nТекущий состав: {', '.join(selected_toppings) if selected_toppings else 'нет начинок'}")
            print(f"Текущая цена: {custom_price} руб.")
            ingredients = ['соус', 'моцарелла']
            action = input("\nВведите:\n- название начинки чтобы добавить\n- 'готово' для завершения: ").lower()

            if action == 'готово':
                if not selected_toppings:
                    print("Вы не добавили ни одной начинки! Создаем базовую пиццу.")
                break
            elif action in topping:
                if action not in selected_toppings:
                    selected_toppings.append(action)
                    custom_price+=topping[action]
                    print(f"Добавили: {action}")
                else:
                    print(f"Начинка '{action}' уже добавлена")
            else:
                print("Неизвестная команда или начинка")
        pizza_name = "Кастомная пицца"
        if selected_toppings:
            pizza_name += f" ({', '.join(selected_toppings)})"

        order.append({
            'название': pizza_name,
            'цена': custom_price,
            'тип': 'пицца'
        })
        total_amount += custom_price
        print(f"\nКастомная пицца добавлена в заказ!")
    elif choice == '3':
        print("\n--- НАПИТКИ ---")
        for drink,price in drinks.items():
            print(f"{drink} : {price}")
        try:
            print("\n--- НАПИТКИ ---")
            drink_choice = input("\nВыберите напиток: \n")
            if drink_choice in drinks:
                if chek_ingridients(ingridients):
                    total_amount += drinks[drink_choice]
                    print("ваш напиток добавлен")
                    order.append({
                        "название": drink_choice,
                        "цена": drinks[drink_choice],
                        "тип": "напитки"
                    })

        except ValueError:
            print("введите нормальное имя напитка")
    elif choice == '4':
        if not order:
            print("Ваш заказ пуст! Добавьте что-нибудь.")
        else:
            break
    else:
        print("Неверный выбор!")

@select
def chek():
    print("ВАШ ЧЕК")
for i, item in enumerate(order, 1):
    print(f"{i}. {item['название']}: {item['цена']} руб.")
@select
def result_finish():
    print(f"ИТОГО: {total_amount} руб.")
result_finish()


print("\n=== ОПЛАТА ===")

while True:
    print("1- заказ собой")
    print("2- здесь")
    try:
        issuing_an_order = int(input())
        if issuing_an_order == 1:
            print(f"ваш заказ приготовиться и мы вам его принесем а покачто оплатите заказ его сумма {total_amount}")
            payid =input("выберите оплату"
                         "картой"
                         "наличными")
            if payid =="картой":
                print("оплата прошла подождите заказ")
            elif payid =="наличными":
                summa=int(input(f"вот сумма {total_amount}  к оплате"))
                if summa == total_amount:
                    print("оплата прошла успешна")
                else:
                    print("вы дали не достаточно денег")
        else:
            print(f"подождите заказ и пресядьте но сначала оплатите вот суммма к оплате {total_amount}")
            payid = input("выберите оплату"
                          "картой"
                          "наличными")
            if payid == "картой":
                print("оплата прошла подождите заказ")
            elif payid == "наличными":
                summa = int(input(f"вот сумма {total_amount}  к оплате"))
                if summa == total_amount:
                    print("оплата прошла успешна")
                else:
                    print("вы дали не достаточно денег")
    except ValueError:
        print("введите число")
