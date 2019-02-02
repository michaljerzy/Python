try:
	import funkcje as fn
except ImportError:
	print('Błąd importu')

print(""" WITAJ W MINI KALKULATORZE! 
	Wybierz jedną z opcji: 
	a) Suma ciągu
	b) Iloczyn ciągu
	c) Średnia artmetyczna
	d) Średnia ważona


	""")
opcja = input("Wybierz opcję: ")
opcja = isalpha()
