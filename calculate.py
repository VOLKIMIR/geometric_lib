import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
	'''
	Функция вычисляет значение заданной фигуры по следующим вводимым параметрам:

	fig:    название фигуры "circle" или "square"
	func:	название функции "perimeter" или "area"
	size:	размер фигуры: для радиуса окружности на вход дается одна величина - r(радиус), для квадрата также одна величина - a(сторона)

	Возвращаемое значение:
		результат вычисляния той или иной фигура с тем или иным действием и размером
	'''
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)



