# -*- coding: utf-8 -*-
from random import randrange
from math import ceil 

partie_en_cours = True 

print("------------------------") 
print("Bienvenue au Py Casino !") 
print("------------------------ \n")

solde = 1000
print("Votre solde actuel est: " + str(solde) + " $")

# Tant que la partie est en cours... 
while partie_en_cours: 
	
	mise_client = -1 
	# Demander au client le nombre qu'il veut miser entre 0 et 49 
	while mise_client < 0 or mise_client > 49: 
		mise_client = raw_input("Veuillez miser un nombre entre 0 et 49 \n")
		# Validation 
		try:
			mise_client = int(mise_client) 
		except ValueError: 
			print("Entrez un nombre...") 
			mise_client = -1
			continue
		if mise_client < 0:
			print("Votre nombre ne doit pas etre négatif") 
		if mise_client > 49:
			print("Le nombre ne doit pas depasser 49")

	# $$$ mise_argent 
	mise_argent = -1 
	while mise_argent < 0 or mise_argent > solde: 
		mise_argent = raw_input("Combien d'argent voulez-vous miser? ('allin' ou $):  ")
		
		if mise_argent == "allin": 
			mise_argent = solde
		else:
		
			try: 
				mise_argent = int(mise_argent) 
			except ValueError: 
				print("Entrez une mise_argent...") 
				mise_argent = -1 
				continue
			if mise_argent< 0: 
				print("Votre mise_argent ne doit pas être négative...")
			if mise_argent> solde: 
				print("Votre mise_argent ne doit pas dépasser votre solde! Cmon!")
	
	
	resultat = randrange(50) 
	print("Et le tirage se trouve sur........... " + str(resultat)) 
	
	# comparer la mise_argent 
	if mise_client == resultat: 
		gain = mise_argent * 3
		solde += gain
		print("Bravo! Vous avez eu la bonne mise, et vous gagnez " + str(gain) + "$")
	elif resultat % 2 == 0 and mise_client % 2 == 0: 
		gain = ceil(mise_argent / 2) 
		solde += gain
		print("Mise paire! Vous avez gagné " + str(gain) + "$")
	elif resultat % 2 != 0 and mise_client % 2 != 0:
		gain = ceil(mise_argent / 2) 
		solde += gain
		print("Mise impaire! Vous avez gagné " + str(gain) + "$")
	else: 
		print("Oups! Vous avez perdu cette manche")
		solde -= mise_argent 
	
	# Vérifier si le client a assez pour jouer 
	if solde <= 0: 
		print("Vous n'avez plus d'argent pour continuer, revenez une prochaine fois!")
		partie_en_cours = False	
	else: 
		print("Votre solde actuel est : " + str(solde) + "$")
		
		quitter = raw_input("Voulez-vous quitter le casino? (o/n)")
		
		if quitter == "o" or quitter == "O": 
			partie_en_cours = False
			print("Au revoir!")
		else: 
			continue
		
		