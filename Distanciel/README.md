# INSTALLATION DE TXM
Lien: http://textometrie.ens-lyon.fr/spip.php?article60

# INSTALLATION DE L'EXTENSION

+ Aller dans fichier: 
	- Ajouter une extension 
	- Choisir l'extension URS
	- Installer l'extension

! Concernant les corpus, créer deux répertoire différent pour chaque corpus (un répertoire contenant les textes propres à chaque binôme/groupe, un répertoire contenant les fichier textes commun à tous le monde)[C'est IMPORTANT pour les calculs des accords inter-annotateurs].

! Pour les répertoires contenant les fichier texte en commun, il faut que tous les groupes nomment ces fichiers pareil pour faire les calculs (sinon, ça va faire des mauvais calculs et se retrouver avec des scores de m**d*s).

# IMPORTATION DES CORPUS SUR TXM:

+ Aller dans fichier: 
	- Importer TXT + CSV
	- Suivre les étapes listé sur TXM:
		- Sélectionner le chemin du répertoire contenant les fichier textes (! Il faut que les fichiers aient l'extension .txt)	(étape 1)
		- modifier les paramètres selon l'onglet correspondant: (étape 2)
			- Langue   --> Sélectionner français (fr)
			- Editions --> mots par page (modifier 500 par 10000)
		- importer le corpus (étape 3)	
	- Aller à l'onlglet de gauche (Corpus) && click droit sur le corpus importé
	-  URS --> import --> import Glozz model (sélectionner le fichier .aam)	

# EXPORTATION DES ANNOTATION:
 	- Aller à l'onlglet de gauche (Corpus) && click droit sur le corpus importé
	- URS --> export --> export XML-TEI URS format	
	- Décocher la case ou il demande une archive (sinon il donnera un .urs à la fin)

# COMMENCER L'ANNOTATION: 
	- Click droit sur le corpus -> Edition
	- Sélectionner le mot à annoter
	- Cliquer sur le bouton "crayon"
 
  