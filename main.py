class Biblioteka2(object) :
	def _init_(self):
		self.ksiazki = []
		self.tytuly = []
		self.komunikaty = []
		self.egzemplarze = []
		self.czytelnicy = {}

	def assksiazka(slef, ksiazka)
		self.ksiazki.append(ksiazka)

	def addegzemplarz(self, egzemlarz):
		egzemplarz1 = list(egzeplarz)
		if egzemplarz1[1:3] in self.ksiazki:
			self.egzemplarze.append(egzemplarz1[1:3])
			self.tytuly.append(egzemplarz1[1])
			self.komunikaty.append ('True')
		else:
			liblary.addksiazka(egzemplarz1[1:3])
			self.egzemplarze.append(egzemplarz1[1:3])
			self.tytuly.append(egzemplarz1[1])
			self.komunikaty.append('True')

	def czytelnicy(self, nazwisko, tytul):
		if naziwsko in self.czytelnicy:
			if len(self.czytelnicy[naziwsko]) < 3 and tytul not in self.czytelnicy[nazwisko]:
				self.tytuly.remove(tytul)
				self.czytelnicy[naziwsko].append(tytul)
				slef.komunikaty.append('True')
			else: 
				self.komunikaty.append('False')

	def liczenie(self):
	    listafinal=[]
	    listasort=[]
	    for ksiazka in self.ksiazki:
	        ksiaza1= [ksiazka[0], ksiazka[1],a]
	        a= self.egzemplarze.count(ksiazka)
	        listafinal.append(ksiazka1)
	    listasort = sorted(listafinal, key=lambda x: x[0])
	    for element in listasort:
	    	element1 = (element[0], element[1], element[2])
	    	print(element)

	    def drukuj(self):
	    	for komunikat in self.komunikaty:
	    		print(komunikat)

	    def wypozycz(self, nazwisko, tytul):
	    	if tytul in self.tytuly:
	    		self.czytelnik(nazwisko,tytul)
	    	else:
	    		self.komunikaty.append('False')

	    def oddaj(self, nazwisko, tytul):
	    	if nazwisko in self.czytelnicy:
	    		if tytul in self.czytelnicy[nazwisko]:
	    			self.czytelnicy[naziwsko].remove(tytul)
	    			self.tytuly.append(tytul)
	    			self.komunikaty.append('True')
	    		else:
	    			self.komunikaty.append('False')

	    	else:
	    		self.komunikaty.append('False')

	 library = Biblioteka()

	 k=int(input())
	 for i in range (o, k):
	 	if wjescie[0] == "dodaj":
	 		library.addegzemplarz(wejscie)
	 	elif wejscie[0] == "wpozycz":
	 		library.wypozycz(wejscie[1], wejscie[2])
	 	elif wejscie [0] == "oddaj":
	 		library.oddaj(wejscie[1], wejscie[2])

	 library.drukuj()