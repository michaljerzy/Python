
#slownik = {"kot" : "gato", "pies" : "perro", "koń" : "caballo"}
#for klucz in sorted(slownik.keys()):
#    print(klucz, "->", slownik[klucz])

slownik = {"kot" : "gato", "pies" : "perro", "koń" : "caballo"}

#for polski, hiszpanski in slownik.items():
#    print(polski, "->", hiszpanski)


slownik['kot'] = 'gatito'
print(slownik)
del slownik['kot']
print(slownik)