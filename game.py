# угадай число - game

import random
from colorama import init
from colorama import Fore, Back, Style # Fore - текст, Back - фон, Style - тусклый(dim), нормальный(normal) или яркий(bright)

print(Back.CYAN)
print(Fore.BLACK)
attempts = int(input('Какое хотите количество попыток? ')) # Кол-во пыток.

b = random.randint(1,100)                                  # Рандом число игры.

print(Back.GREEN)
print('Я загадал случайное число... ')                     # Задача.

print(Back.YELLOW)
a = int(input("Попробуй отгадать... "))                    # Первое число игрока.

while True:
	if(a > 100):
		print('Это число больше 100! Давай нормальное.')
		a = int(input('Назови число, только давай уже меньше 100, но больше 1...'))
	elif(a < 1):
		print('Ты издеваешься? Числа должны быть от 1 и до 100.')
		a = int(input('Назови нормальное, целое, положительное число от 1 до 100...'))
	else:
		break

while True:                                                # Залупливаю, чтобы можно было выбирать число до окончания попыток. 
	if(a > b):
		print(Back.WHITE)
		print('\nВы не угадали, число меньше...')
		attempts -= 1
		if attempts < 0:
			print('Попытки кончились.')
			break
		a = int(input('\nВведите Ваше новое число... \n'))

	elif(a < b):
		print(Back.RED)
		print('\nВы не угадали, число больше...')
		attempts -= 1
		if attempts < 0:
			print('Попытки кончились.')
			break
		a = int(input('\nВведите Ваше новое число... \n'))

	else: 
		print(Style.BRIGHT)
		print(Back.GREEN)
		print('\nПоздравляю! Ты угадал.')
		print('У тебя осталось {0} попыток, гад'.format(attempts))
		break
