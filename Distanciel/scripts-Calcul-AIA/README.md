# Extraction et formatage des annotations de TXM et calcul de l'accord inter-annotateurs

## Librairies Python requises

#### pandas
```bash
pip install pandas
```
#### numpy
```bash
pip install numpy
```
#### beautifulsoup4
```bash
pip install beautifulsoup4
```
#### nltk
```bash
pip install nltk
```
#### scikit-learn
```bash
pip install scikit-learn
```

## 1. Formatage des annotations extraites de TXM (extract_annotation.py)

Le script Python _extract_annotation.py_ permet de récupérer les annotations dans le dossier généré par TXM et de générer deux CSV :
- un CSV de visualisation des annotations
- un CSV des annotations formaté (pour ensuite cacluler les accords inter-annotateurs avec le script _accord_interannotateur.py_)

### Utilisation du script

```bash 
python3 extract_annotation.py -i "/output_TXM/" -o "/output_folder" -n "annotateur1" 
```

Paramètres :
- _-i_ : chemin absolu du dossier extrait de TXM, contenant les dossiers "texts" et "annotations"
- _-o_ : chemin absolu du dossier de sortie où seront enregistrés les CSV
- _-n_ : _nom_ pour les CSV (*nom*\_visualisation.csv et *nom*\_output.csv)

#### Exemples 

```bash 
python3 extract_annotation.py -i "/Users/user1/Desktop/Annotation_TXM_annotateur1" -o "/Users/user1/Desktop/Annotation_output" -n "annotateur1"
python3 extract_annotation.py -i "/Users/user1/Desktop/Annotation_TXM_annotateur2" -o "/Users/user1/Desktop/Annotation_output" -n "annotateur2"
```

## 2. Calcul de l'accord inter-annotateurs (accord_interannotateur.py)

Le script Python _accord_interannotateur.py_ permettant de calculer les accords inter-annotateurs :
- Kappa de Cohen
- Kappa de Fleiss
- Pi de Scott

### Utilisation du script

Paramètres :
- _-cohen_, _--cohen_kappa_ : calcule le Kappa de Cohen entre 2 annotateurs (argument -f et -s pour les CSV des 2 annotateurs)
- _-scott_, _--scott_pi_ : calcule le Pi de Scott entre n annotateurs (argument -i pour le dossier contenant les CSV des n annotateurs)
- _-fleiss_, _--fleiss_kappa_ : calcule le Kappa de Fleiss entre n annotateurs (argument -i pour le dossier contenant les CSV des n annotateurs)

Pour le Kappa de Cohen:
- _-f "/CSV Path/"_, _--first_input "/CSV PATH/"_ : chemin absolu vers le CSV des annotations du premier annotateur
- _-s "/CSV Path/"_, _--second_input "/CSV PATH/"_ : chemin absolu vers le CSV des annotations du deuxième annotateur

Pour le Kappa de Fleiss et le Pi de Scott :
- _-i "/Path/"_, _--input_folder "/Path/"_ : chemin absolu vers le dossier contenant les CSV de tous les annotateurs

#### Exemples

```bash 
python3 accord_interannotateur.py -cohen -f "/Users/user1/Desktop/Annotation_output/annotateur1_output.csv" -s "/Users/user1/Desktop/Annotation_output/annotateur2_output.csv"
python3 accord_interannotateur.py -scott -i "/Users/user1/Desktop/Annotation_output/all_annotators_output"
python3 accord_interannotateur.py -fleiss -i "/Users/user1/Desktop/Annotation_output/all_annotators_output"
```

## License
[GPL3](https://choosealicense.com/licenses/gpl-3.0)