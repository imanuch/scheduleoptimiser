def find_combinations(courses):
    """
    Fonction pour trouver toutes les combinaisons de 6 cours sans chevauchement dans une semaine.

    Args:
        courses: Une liste de listes de dictionnaires représentant les séances des cours.

    Returns:
        Une liste de listes contenant toutes les combinaisons possibles de 6 cours.
    """

  # Filtrer les cours qui se chevauchent
    non_chevauchants = []
    for i in range(len(courses)):
        for j in range(i + 1, len(courses)):
            if not chevauchement_entre_cours(courses[i], courses[j]):
            
                non_chevauchants.append((courses[i], courses[j]))

    
  # Récursivité pour trouver toutes les combinaisons de 6 cours
    def _find_combinations_recur(non_chevauchants, selection, profondeur):
        if profondeur == 6:
            return [selection]

        combinaisons = []
        for i in range(len(non_chevauchants)):
            if not chevauchement_avec_selection(non_chevauchants[i][0], selection):
                combinaisons += _find_combinations_recur(non_chevauchants[i+1:], selection + [non_chevauchants[i][0]], profondeur + 1)

        return combinaisons

    return _find_combinations_recur(non_chevauchants, [], 0)

def chevauchement_entre_cours(cours1, cours2):
  """
  Fonction pour vérifier si deux cours se chevauchent.

  Args:
    cours1: Une liste de dictionnaires représentant les séances d'un cours.
    cours2: Une liste de dictionnaires représentant les séances d'un cours.

  Returns:
    True si les cours se chevauchent, False sinon.
  """
  for seance1 in cours1:
    for seance2 in cours2:
        if seance1== seance2:
            return True
        if horaires_chevauchent_meme_jour(seance1, seance2):
            return True
  return False

def horaires_chevauchent_meme_jour(seance1, seance2):
  return seance1["jour"] == seance2["jour"] and horaires_chevauchent(seance1["horaire_debut"], seance1["horaire_fin"], seance2["horaire_debut"], seance2["horaire_fin"]) 

def horaires_chevauchent(debut1, fin1, debut2, fin2):
  """
  Fonction pour vérifier si deux horaires se chevauchent.

  Args:
    debut1: Heure de début du premier cours.
    fin1: Heure de fin du premier cours.
    debut2: Heure de début du deuxième cours.
    fin2: Heure de fin du deuxième cours.

  Returns:
    True si les horaires se chevauchent, False sinon.
  """
  return debut1 < fin2 and debut2 < fin1

def chevauchement_avec_selection(cours, selection):
  """
  Fonction pour vérifier si un cours se chevauche avec une sélection de cours.

  Args:
    cours: Une liste de dictionnaires représentant les séances d'un cours.
    selection: Une liste de listes de dictionnaires représentant les séances des cours sélectionnés.

  Returns:
    True si le cours se chevauche avec la sélection, False sinon.
  """
  for c in selection:
    if chevauchement_entre_cours(cours, c):
      return True
  return False

# Exemple d'utilisation
courses = [
  [
    {
      "nom": "database",
      "jour": "mardi",
      "horaire_debut": "14h00",
      "horaire_fin": "16h00",
    },
    {
      "nom": "database",
      "jour": "vendredi",
      "horaire_debut": "14h00",
      "horaire_fin": "16h00",
    },
  ],
  [
    {
      "nom": "zero-knowledge-proofs",
      "jour": "mardi",
      "horaire_debut": "10h00",
      "horaire_fin": "12h00",
    },
    {
      "nom": "zero-knowledge-proofs",
      "jour": "jeudi",
      "horaire_debut": "12h00",
      "horaire_fin": "14h00",
    },
  ],
#     [
#     {
#       "nom": "programmanalise",
#       "jour": "mardi",
#       "horaire_debut": "10h00",
#       "horaire_fin": "12h00",
#     },
#     {
#       "nom": "programmanalise",
#       "jour": "mercredi",
#       "horaire_debut": "8h00",
#       "horaire_fin": "10h00",
#     },
#   ],
        [
    {
      "nom": "vehiculesautonomes",
      "jour": "mardi",
      "horaire_debut": "14h00",
      "horaire_fin": "16h00",
    },
    {
      "nom": "vehiculesautonomes",
      "jour": "jeudi",
      "horaire_debut": "12h00",
      "horaire_fin": "14h00",
    },
  ],
    [
    {
      "nom": "langage",
      "jour": "mercredi",
      "horaire_debut": "16h00",
      "horaire_fin": "18h00",
    },
    {
      "nom": "langage",
      "jour": "vendredi",
      "horaire_debut": "12h00",
      "horaire_fin": "14h00",
    },
  ],
    [
    {
      "nom": "neuro",
      "jour": "lundi",
      "horaire_debut": "14h00",
      "horaire_fin": "16h00",
    },
    {
      "nom": "neuro",
      "jour": "vendredi",
      "horaire_debut": "10h00",
      "horaire_fin": "12h00",
    },
  ],
        [
    {
      "nom": "data",
      "jour": "jeudi",
      "horaire_debut": "14h00",
      "horaire_fin": "16h00",
    },
    {
      "nom": "data",
      "jour": "vendredi",
      "horaire_debut": "14h00",
      "horaire_fin": "16h00",
    },
  ],
                [
    {
      "nom": "krypto",
      "jour": "jeudi",
      "horaire_debut": "10h00",
      "horaire_fin": "12h00",
    },
    {
      "nom": "krypto",
      "jour": "vendredi",
      "horaire_debut": "12h00",
      "horaire_fin": "14h00",
    },
  ],

#   [
#     {
#       "nom": "systemsecurity",
#       "jour": "lundi",
#       "horaire_debut": "14h00",
#       "horaire_fin": "18h00",
#     },
#   ],
  
#   [
#     {
#       "nom": "computationalneuro",
#       "jour": "jeudi",
#       "horaire_debut": "10h00",
#       "horaire_fin": "14h00",
#     },
#   ],

    [
    {
      "nom": "machinelearning",
      "jour": "jeudi",
      "horaire_debut": "10h00",
      "horaire_fin": "14h00",
    },
  ],
      [
    {
      "nom": "robotics",
      "jour": "jeudi",
      "horaire_debut": "14h00",
      "horaire_fin": "18h00",
    },
  ],
      
    [
    {
      "nom": "physiqueattaque",
      "jour": "mardi",
      "horaire_debut": "8h00",
      "horaire_fin": "12h00",
    },
  ],
        [
    {
      "nom": "introIA",
      "jour": "vendredi",
      "horaire_debut": "10h00",
      "horaire_fin": "14h00",
    },
  ],
                [
    {
      "nom": "distributed",
      "jour": "jeudi",
      "horaire_debut": "10h00",
      "horaire_fin": "14h00",
    },
  ],
  # ...
]

combinaisons = find_combinations(courses)
combinaisons2 = []
print(f"Nombre de combinaisons possibles : {len(combinaisons)}")
def supprimer_doublons(liste):
    
    """
    Fonction pour supprimer les doublons d'une liste.

    Args:
        liste: La liste à partir de laquelle les doublons doivent être supprimés.

    Returns:
        Une nouvelle liste sans doublons.
    """
    cours_contraint = ["physiqueattaque"]
    liste_sans_doublons = []
    for element in liste:
        k = 0
        for cours in element:
            if cours[0]['nom'] in cours_contraint:
                k = 1
        if element not in liste_sans_doublons and k==1:
            liste_sans_doublons.append(element)
            
    return liste_sans_doublons

combinaisons2 = supprimer_doublons(combinaisons)

for combinaison in combinaisons2:
    print("Combinaison :")
    for cours in combinaison:
        print(cours[0]['nom'] +' '+ cours[0]['jour'] +' '+ cours[0]['horaire_debut'] +' '+ cours[0]['horaire_fin'])
        if len(cours)>1:
            print(cours[1]['nom'] +' '+ cours[1]['jour'] +' '+ cours[1]['horaire_debut'] +' '+ cours[1]['horaire_fin'])
    print("\n")
print(len(combinaisons2))