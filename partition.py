"""
l'idée consiste en transformer la matrice du fichier en matrice interpretable par la machine.
Cette matrice obtenu sera alors plus fichier facile à manipuler, le partitionnement ici est assimilé avec un split de la matrice """

# importation de la librairie numpy permettant de manipuler les matrices
import numpy as np
import time 
start_time = time.time() 
 


baseDonnee = input("Donner le nom de la base données: ")
if baseDonnee == "SUSY":

	data = np.loadtxt(baseDonnee+".txt", dtype='a', delimiter=' ')
	#data = np.genfromtxt(baseDonnee+".txt", dtype='i', delimiter=' ')
else:
	data = np.loadtxt(baseDonnee+".txt", dtype='i', delimiter=' ')
print(data)

import shutil, os

import random

def pick(k):
	return random.randint(1,k)

def move_bd(k,p):
	if int(p) == 1 or int(p) ==2:
		for x in range(1,k+1):
			# Déplacer un fichier du répertoire rep1 vers rep2
			if int(p)==1:
				shutil.move("HL"+baseDonnee+str(x)+".txt", "DDsampling/dataSplited/HL/"+baseDonnee+"/HL"+baseDonnee+str(x)+".txt")
			else:
				shutil.move("HV"+baseDonnee+str(x)+".txt", "DDsampling/dataSplited/HV/"+baseDonnee+"/HV"+baseDonnee+str(x)+".txt")
		
	else:
		for x in range(0,4):
			shutil.move("HD"+baseDonnee+str(x)+".txt", "DDsampling/dataSplited/HD/"+baseDonnee+"/HD"+baseDonnee+str(x)+".txt")
		
			


nombreLigne = np.shape(data)[0]
nombreColonne = np.shape(data)[1]

# partitionnement verticale
def horizontale(matrix, k):
	for x in range(0,nombreLigne):
		line = data[x]
		picked = pick(k)
		#print(picked)
		f = open("HL"+baseDonnee+str(picked)+".txt", "a")
		f.write(str(x)+" ; ")
		for i in range(0, np.size(line)):
			f.write(str(line[i])+" ")
		f.write(str("\n"))
		f.close()



def verticale(matrix, k):
	for x in range(0,nombreColonne):
		column = data[:,x]
		picked = pick(k)
		#print(picked)
		f = open("HV"+baseDonnee+str(picked)+".txt", "a")
		f.write(str(x)+" ; ")
		for i in range(0, np.size(column)):
			f.write(str(column[i])+" ")
		f.write(str("\n"))
		f.close()

def hybride(matrix, k):
	for x in range(0,(nombreLigne//2)+1):
		line = data[x]
		picked = pick(k)
		#print(picked)
		f = open("HD"+baseDonnee+str(picked)+".txt", "a")
		f.write(str(x)+" ; ")
		for i in range(0, (np.size(line)//2)+1):
			f.write(str(line[i])+" ")
		f.write(str("\n"))
		f.close()
		picked = pick(k)
		#print(picked)
		f = open("HD"+baseDonnee+str(picked)+".txt", "a")
		f.write(str(x)+" ; ")
		for i in range((np.size(line)//2), np.size(line)):
			f.write(str(line[i])+" ")
		f.write(str("\n"))
		f.close()
	for x in range((nombreLigne//2), nombreLigne):
		line = data[x]
		picked = pick(k)
		#print(picked)
		f = open("HD"+baseDonnee+str(picked)+".txt", "a")
		f.write(str(x)+" ; ")
		for i in range(0, (np.size(line)//2)+1):
			f.write(str(line[i])+" ")
		f.write(str("\n"))
		f.close()
		picked = pick(k)
		#print(picked)
		f = open("HD"+baseDonnee+str(picked)+".txt", "a")
		f.write(str(x)+" ; ")
		for i in range((np.size(line)//2)+1, np.size(line)):
			f.write(str(line[i])+" ")
		f.write(str("\n"))
		f.close()
	
def introduce():
	k = input("Donner le nombre de fragment ! : ")
	choice = input (" 1. horizontale / 2. verticale / autre.hybride ")
	# copie de la matrice pour ne pas perder de données
	copie = np.copy(data)
	if int(choice) == 1:
		for x in range(1, int(k)+1):
			f = open("HL"+baseDonnee+str(x)+".txt", "x")
			f.close()

		horizontale(copie, int(k))
	
	elif int(choice) == 2:
		for x in range(1,int(k)+1):
			f = open("HV"+baseDonnee+str(x)+".txt", "x")
			f.close()

		verticale(copie, int(k))
	else:
		for x in range(1,5):
			f = open("HD"+baseDonnee+str(x)+".txt", "x")
			f.close()

		hybride(copie, int(k))

	move_bd(int(k), int(choice))
print("--- %s seconds ---" % (time.time() - start_time))





k = introduce()
print("--- %s seconds ---" % (time.time() - start_time))

