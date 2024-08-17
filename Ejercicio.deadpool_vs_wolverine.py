import random
import time

class Personaje:
	def __init__(self,nombre,vida,dano_min,dano_max,regenerar,evadir):
		self.nombre = nombre
		self.vida = vida
		self.dano_min = dano_min
		self.dano_max = dano_max
		self.regenerar = regenerar
		self.evadir = evadir

	def mostrar_estadisticas(self):
		print(self.nombre, ":", sep="")
		print(f"Vida:", self.vida)
		print("Dano:", self.dano_min)
		print("Dano:", self.dano_max)
		print("Se puede regenerar:", self.regenerar)
		print("Evadir", self.evadir)

	def esta_vivo(self):
		return self.vida > 0

	def morir(self):
		self.vida = 0
		print(f"{self.nombre} ha muerto")

# calcular dano a realizar
	def dano(self):
		return random.randint(self.dano_min, self.dano_max)

	def esquivar(self):
		valor = random.random()
		redondeando = round(valor,2)
		return redondeando

	def no_atacar(self):
		pass

	def regenerarse(self):
		print(f"{self.nombre} se esta regenerando")

	def atacar(self, enemigo, dano):
		dano_hecho = dano
		enemigo.vida -= dano_hecho
		print(self.nombre, "ha realizado", dano_hecho, "puntos de dano a", enemigo.nombre)
		if enemigo.esta_vivo():
			print("Vida de", enemigo.nombre, "es", enemigo.vida)
		else:
			enemigo.morir()

vida_deadpool = int(input("Ingrese la vida que va a tener Deadpool: "))
vida_wolverine = int(input("Ingrese la vida que va a tener Wolverine: "))

def combate(w,d):
	turno = 1
	while w.esta_vivo() and d.esta_vivo():

		# ataca wolverine
		gar = deadpool.esquivar()
		print(f"***Turno {turno}***")
		print(f"---Ataca {w.nombre}")
		if gar <= 0.25:
			wolverine.no_atacar()
			print(f"{d.nombre} ha esquivado el ataque")
		elif gar >= 0.26:
			contener_dano = wolverine.dano()
			if contener_dano == wolverine.dano_max:
				wolverine.regenerarse()
			else:
				wolverine.atacar(deadpool,contener_dano)
		# ataca deadpool
		print(f"---Ataca {d.nombre}")
		var = wolverine.esquivar()
		if var <= 0.20:
			deadpool.no_atacar()
			print(f"{w.nombre} ha esquivado el ataque")
		elif var >= 0.21:
			contener_dano = deadpool.dano()
			if contener_dano == deadpool.dano_max:
				deadpool.regenerarse()
			else:
				deadpool.atacar(wolverine,contener_dano)
		time.sleep(1)
		print("---------------------")

		turno += 1
	if w.esta_vivo():
		print("\nHa ganado", w.nombre)
	elif d.esta_vivo():
		print("\nHa ganado", d.nombre)
	else:
		print("\nEmpate")
	
	

deadpool = Personaje("Deadpool",vida_deadpool,10,100,True,25)

wolverine = Personaje("Wolverine",vida_wolverine,10,120,True,20)

combate(wolverine,deadpool)

print("FIN")



