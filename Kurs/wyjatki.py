x = 3

try:
	x / 0
	pritn(x)
except ZeroDivisionError:
	print(ZeroDivisionError)
finally:
	print(x)