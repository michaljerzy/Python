#funkcja def
def show_info(name, **args):
	print(name)
	print(args)

show_info('kurs php', price = 59)


#użycie listy w pętli
list = [1,10]

for i in range(*list):
	print(i)

#funkcja lambda
 
x = lambda a, b: a + b

print(x(2,5))

y = lambda a, b: a * b

print(y(4,4))