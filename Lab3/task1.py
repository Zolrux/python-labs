import time, random

def scanning_simulation():
    for i in range(1, random.randint(2, 5)):
        time.sleep(3)
        print(f"Сканирую товар №{i}...")


def main(cashier: list, buyer: list):

    info = {
        'total_price': None,
        'cash': None
    }

    for index, el in enumerate(cashier):

        if isinstance(buyer[index], list):
            print(el, end=" ")
            answer = input().lower()
            while not answer in buyer[index]:
                print(el, end=" ")
                answer = input().lower()

        if index == 0:
            scanning_simulation()

        elif index == 2:
            info["total_price"] = random.randrange(100, 1000)
            time.sleep(3)
            print(f"{el}{info['total_price']}грн")

        elif index == 3:
            print(el, end=" ")
            info["cash"] = input()
            while not info["cash"].isdigit() or float(info["cash"]) < info["total_price"]:
                print(el, end=" ")
                info["cash"] = input()
            else:
                info["cash"] = float(info["cash"])

        elif index == 4:
            if info["cash"] - info["total_price"] > 0:
                change = info["cash"] - info["total_price"]
                time.sleep(3)
                print(f"{el}{change}грн")

        elif index == len(cashier) - 1:
            print(el)


cashier = (
    "Добрый день, вам пакет нужен? [Да/Нет]",
    "Наша карточка есть? [Да/нет]",
    "К оплате ",
    "Сколько вы даете? ",
    "Ваша сдача ",
    "Спасибо за покупку, приходите еще!"
)

buyer = (
    ["да", "нет"],
    ["да", "нет"],
    False,
    False,
    False,
    "Спасибо, всего доброго!"
)

main(cashier, buyer)