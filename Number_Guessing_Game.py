import random

number = random.randrange(1, 101)
replies = ["А может быть все-таки введем целое число от 1 до 100?", "Вы ввели что-то не то, попробуйте еще раз", "Еще разок число от 1 до 100"]

print("Добро пожаловать в числовую угадайку!")
counter = 0
flag = True

def is_valid(num):

    if num.isdigit():
        num = int(num)
        if 100 >= num >= 1:
            return True
        return False
    return False
    
while flag:
    n = input("Введите число от 1 до 100 ")
    if not is_valid(n):
        print(random.choice(replies))
        continue
    n = int(n)

    if n < number:
        print("Ваше число меньше загаданного, попробуйте еще разок")
        counter +=1
    elif n > number:
        print("Ваше число больше загаданного, попробуйте еще разок")
        counter +=1
    else:
        n == number
        counter +=1
        print("Вы угадали, поздравляем! Вам потребовалось", counter, "попыток")
        flag = False

        
    
