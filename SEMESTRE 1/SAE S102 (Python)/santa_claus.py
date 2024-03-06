from time import time
from math import *
from numpy import *
from random import *

##############
# SAE S01.01 #
##############

def nb_villes(villes):
    """Retourne le nombre de villes"""
    return len(villes)//3


def noms_villes(villes):
    """Retourne un tableau contenant le nom des villes"""
    noms_v = []
    i = 0
    while 3*i < len(villes):
        noms_v.append(villes[3*i])
        i += 1
    return noms_v


def d2r(nb):
    return nb*pi/180


def distance(long1, lat1, long2, lat2):
    """retourne la distance entre les points (long1, lat1) et (long2, lat2)"""
    lat1 = d2r(lat1)
    long1 = d2r(long1)
    lat2 = d2r(lat2)
    long2 = d2r(long2)
    R = 6370.7
    d = R*arccos(sin(lat1)*sin(lat2)+cos(lat1)*cos(lat2)*cos(long2-long1))
    return d


def indexCity(ville, villes):
    """Retourne l'indice dans le tableau villes de la ville de nom ville,
       et -1 si elle n'existe pas
    """
    res = -1
    i = 0
    while 3*i < len(villes) and villes[3*i] != ville:
        i += 1
    if 3*i < len(villes):
        res = 3*i
    return res


def distance_noms(nom1, nom2, villes):
    """Retourne la distance entre les villes nom1 et nom2 
       en fonction de la structure de données villes
    """
    index1 = indexCity(nom1, villes)
    index2 = indexCity(nom2, villes)

    if index1 == -1 or index2 == -1:
        d = -1
    else:
        d = distance(villes[index1+1], villes[index1+2],
                     villes[index2+1], villes[index2+2])
    return d


def lecture_villes(path):
    """Retourne la structure de données villes en fonction des données du fichier path"""
    f_in = open(path, encoding='utf-8', mode='r')
    villes = []
    li = f_in.readline()
    li = li.strip()
    while li != '':
        tab_li = li.split(';')
        villes.append(tab_li[0])
        villes.append(float(tab_li[1]))
        villes.append(float(tab_li[2]))
        li = f_in.readline()
        li = li.strip()
    f_in.close()
    return villes


def long_tour(villes, tournee):
    """Retourne la longueur d'une tournée en fonction de la structure de données villes"""
    long = 0
    i = 0
    while i+1 < len(tournee):
        long += distance_noms(tournee[i], tournee[i+1], villes)
        i += 1
    long += distance_noms(tournee[i], tournee[0], villes)
    return long

##############
# SAE S01.02 #
##############


def dictionary_cities(villes):
    """
    Paramètre(s) :
    - villes : un tableau contenant des noms de villes, puis leur longitude et leur latitude 
    La fonction retourne un dictionnaire, dont les clés sont les noms des villes, et les valeurs sont des dictionnaires contenant pour
    chaque ville, différente de la clé, la distance entre cette ville et la clé du dictionnaire (dictionnaire de distances),
    contenant les distances entre les villes du tableau passé en paramètres
    dict = {}
    """
    
    for i in range(0,len(villes),3):
        ville1 = villes[i]
        long1 = villes[i+1]
        lat1 = villes[i+2]

        if ville1 not in dict:
            dict[ville1] = {}
        
        for j in range(0,len(villes),3):
            if i != j:
                ville2 = villes[j]
                long2 = villes[j+1]
                lat2 = villes[j+2]

                dict[ville1][ville2] = distance(long1,lat1,long2,lat2)

    return dict


d = dictionary_cities(["Paris",2.33, 48.86, "Lyon", 4.85, 45.75, "Marseille", 5.40, 43.30, "Lille", 3.06, 50.63])

#print(d)


def distance_cities(name1, name2, d_cities):
    """
    Paramètre(s) :
    - name1 : un premier nom de ville
    - name2 : un second nom de ville
    - d_cities : un dictionnaire de distances
    La fonction renvoie la distance entre les deux villes passées en paramètres si elles sont dans le dictionnaire,
    -1 sinon.
    """
    if name1 not in d_cities or name2 not in d_cities[name1]: #on vérifie que les villes sont dans le dictionnaire
        return -1
    dist = d_cities[name1][name2]
    return dist

#print(distance_cities("Paris","Marseille",d))


def tour_length(tour, d_cities):
    """
    Paramètre(s) :
    - tour : un tableau contenant l'ordre des villes à parcourir
    - d_cities : un dictionnaire de distances
    La fonction renvoie la longueur du tour passé en paramètres.
    """
    dist = 0
    v_depart = tour[0]
    for i in range(len(tour)-1):
        ville1 = tour[i]
        ville2 = tour[i+1]
        dist += distance_cities(ville1,ville2,d_cities)
    dist += distance_cities(ville2,v_depart,d_cities)
    return dist

#print(tour_length(["Lyon", "Marseille", "Paris", "Lille"],d))



def closest_city(city, cities, d_cities):
    """
    Paramètre(s) :
    - city : un nom de ville
    - cities : un tableau de noms de villes
    - d_cities : un dictionnaire de distances
    La fonction renvoie l'indice de la ville contenue dans cities, la plus proche de city.
    """
    v_min = distance_cities(city,cities[0],d_cities)
    indice = 0
    for i in range(1,len(cities)):
        if city != cities[i]:
            dist = distance_cities(city,cities[i],d_cities)
            if dist < v_min:
                v_min = dist
                indice = i
    return indice

#print(closest_city("Paris", ["Marseille","Lyon","Lille"] ,d))



def tour_from_closest_city(city, d_cities):
    """
    Paramètre(s) :
    - city : un nom de ville
    - d_cities : un dictionnaire de distances
    La fonction renvoie un petit tour en prenant city comme ville de départ.
    """
    tour = [city]

    while len(tour) < len(d_cities):
        act_city = tour[-1]
        cities = list(d_cities[act_city].keys())
        cities2 = []

        for i in range(len(cities)):
            if cities[i] not in tour:
                cities2.append(cities[i])

        ind = closest_city(act_city,cities2,d_cities)

        # si l'indice que nous obtenons vaut quelque chose on l'ajoute dans la table sinon, c'est qu'il n'y a rien et du coup on arrête la boucle
        if ind is not None:
            tour.append(cities2[ind])
        else:
            break
            
    return tour

#print(tour_from_closest_city("Marseille",d))

def best_tour_from_closest_city(d_cities):
    """
    Paramètre(s) :
    - d_cities : un dictionnaire de distances
    La fonction renvoie la distance entre les deux villes passées en paramètres si elles sont dans le dictionnaire,
    -1 sinon.
    La fonction renvoie le meilleur tour parmi ceux obtenus avec la fonction tour_from_closest_city en prenant chaque ville comme ville de départ
    """
    cities = list(d_cities)
    tour = tour_from_closest_city(cities[0], d_cities)
    dist_min_tour = tour_length(tour, d_cities)

    for i in range(1,len(cities)):
        tourTemp = tour_from_closest_city(cities[i], d_cities)
        if dist_min_tour > tour_length(tourTemp, d_cities):
            tour = tour_from_closest_city(cities[i], d_cities)
            dist_min_tour = tour_length(tour, d_cities)
    
    return tour,dist_min_tour
        
#print(best_tour_from_closest_city(d))

def reverse_part_tour(tour, ind_b, ind_e):
    """
    Paramètre(s) :
    - tour : un tableau de noms de villes
    - ind_b et ind_e : deux indices
    La fonction inverse la partie du tableau tour contenue entre les deux indices inclus.
    """
    if ind_b < 0 or ind_e >= len(tour) or ind_b >= ind_e:
        return tour
    
    tour_copy = tour.copy()
    tour_copy[ind_b:ind_e + 1] = reversed(tour_copy[ind_b:ind_e+1])
    return tour_copy

#print(reverse_part_tour(["Agen", "Belfort", "Cahors", "Dijon", "Épinay", "Fréjus", "Grenoble", "Hyères"],2,5))


def inversion_length_diff(tour, d_cities, ind_b, ind_e):
    """
    Paramètre(s) :
    - tour : un tableau noms de villes
    - d_cities : un dictionnaire de distances
    - ind_b et ind_e : deux indices
    La fonction renvoie la différence entre la distance du tour passé en paramètres et celle obtenu en
    inversant la partie du tour contenue entre ind_b et ind_e inclus.
    """
    tour1 = tour.copy()
    tour2 = reverse_part_tour(tour, ind_b, ind_e)

    dist_tour2 = tour_length(tour2,d_cities)
    dist_tour1 = tour_length(tour1,d_cities)

    return dist_tour1 - dist_tour2

#print(inversion_length_diff(["Marseille", "Lyon", "Paris", "Lille"],d,1,2))


def better_inversion(tour, d_cities):
    """
    Paramètre(s) :
    - tour : un tableau noms de villes
    - d_cities : un dictionnaire de distances 
    La fonction renvoie True si une inversion du tour a été faite et False sinon.
    """
    min_dist = tour_length(tour,d_cities)
    tour1 = tour.copy()
    
    for i in range(len(tour)):
        for j in range(i+1,len(tour)):
            tourTemp = reverse_part_tour(tour1, i, j)
            dist_tour_temp = tour_length(tourTemp,d_cities)

            if dist_tour_temp < min_dist:
                min_dist = dist_tour_temp
                tour[:] = tourTemp
                return True   
            
    return False 


def best_obtained_with_inversions(tour, d_cities):
    """
    Paramètre(s) :
    - tour : un tableau noms de villes
    - d_cities : un dictionnaire de distances 
    La fonction renvoie le nombre d'inversions du tableau tour effectuées.
    """
    inversions_count = 0
    while better_inversion(tour, d_cities):
        inversions_count += 1
    return inversions_count


tour = ["Marseille", "Paris", "Lyon", "Lille"]
inversions_count = best_obtained_with_inversions(tour, d)
print(inversions_count, tour)


print(tour_length(['Lille', 'Paris', 'Marseille', 'Lyon'],d))




