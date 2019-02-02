def sprawdzenie():
	i = input("Ile liczb znajduje się w ciągu? ")
	#sprawdzenie czy podana wartość nie jest literą
	sprawdzenie = i.isdigit()
	while sprawdzenie is False:
		print("Podana wartość musi być liczbą!")
		i = input("Ile liczb znajduje się w ciągu? ")
		sprawdzenie = i.isdigit()
	i=int(i)
	while (i<=0):
		print("Ilość liczb musi być mniejsza i różna od 0")
		i = int(input("Ile liczb znajduje się w ciągu? "))
	return i

def sprawdzenieliczby():
	a = input("Podaj wartość liczby: ")
	sprawdzenie = a.isdigit()
	while sprawdzenie is False:
		print("Podana wartość musi być liczbą!")
		a = input("Ile liczb znajduje się w ciągu? ")
		sprawdzenie = a.isdigit()
	a=int(a)
	return a

def sumaciagu():
	s = 0
	i = sprawdzenie()
	for x in range(i):
		a = sprawdzenieliczby()
		s += a
	return s

def iloczynciagu():
	s = 1
	i = sprawdzenie()
	for x in range(i):
		a = sprawdzenieliczby()
		s *= a
	return s

def sredniaartmetyczna():
	s = 0
	i = sprawdzenie()
	for x in range(i):
		a = sprawdzenieliczby()
		s += a
		suma = s/i
	return suma

def sredniawazona():
	s = 0
	q = 0
	i = sprawdzenie()
	for x in range(i):
		a = sprawdzenieliczby()
		print("Wprowadź wagę liczby")
		b = sprawdzenieliczby()
		s += a*b
		q += b;
	return s/q