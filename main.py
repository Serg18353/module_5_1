class House:
    def __init__(self, name, numbers_of_floor):
        self.name = name
        self.numbers_of_floor = numbers_of_floor

    def go_to(self, a):
        c = 1
        for i in range(self.numbers_of_floor):
            if self.numbers_of_floor < a:
                print('Такого этажа не существует')
                break
            elif i != a:
                print(c)
                c += 1
            else:
                break

h1 = House(name='ЖК Горский', numbers_of_floor=18)
h2 = House(name='Домик в деревне', numbers_of_floor=2)
h1.go_to(5)
h2.go_to(10)




