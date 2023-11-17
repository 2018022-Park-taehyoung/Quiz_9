class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate(self, number):
        total = self.price * int(number)
        print(self.name + "는 " + str(self.price) + "원으로, \n" + number + "개는 총 " + str(total) + "원 입니다.")

Coffee = Beverage("커피", 3000)
GreenTea = Beverage("녹차", 2500)
IceTea = Beverage("아이스티", 3000)

selected_beverage = input("커피, 녹차, 아이스티 중 구입하려는 음료를 입력하세요: ")

if selected_beverage == "커피":
    number = input("구입하려는 음료의 수량을 입력하세요: ")
    Coffee.calculate(number)
elif selected_beverage == "녹차":
    number = input("구입하려는 음료의 수량을 입력하세요: ")
    GreenTea.calculate(number)
elif selected_beverage == "아이스티":
    number = input("구입하려는 음료의 수량을 입력하세요: ")
    IceTea.calculate(number)
else:
    print(selected_beverage + "는 없는 메뉴입니다. 커피, 녹차, 아이스티 중 하나를 골라주세요.")
