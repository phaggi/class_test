class MyUser:
    def __init__(self, name, id, money, password):
        self.user_name = name
        self.id_user = id
        self.money = money
        self.password = password

    def add_money(self, summa):
        self.money += summa

    def __repr__(self):
        return f'{self.user_name, self.money, self.password}'


user_alan = MyUser(name='Alan', id=12345, money=0, password='MYPASS')
user_limonchik = MyUser(name='Limonchik', id=23456, money=1000, password='')

user_limonchik.user_name = 'Limonchik'

print(user_alan, user_limonchik)
user_limonchik.add_money(10)

print(user_alan, user_limonchik)

user_limonchik.password = 'wwwww'
print(user_alan, user_limonchik)

print(type(user_alan), type(user_limonchik))

def print_user(user: MyUser):
    print(user.)

print_user(user_limonchik)
