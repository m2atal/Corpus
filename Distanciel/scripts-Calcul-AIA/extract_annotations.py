'''
Author: Bazoge Adrien	
'''

import pandas as pd
import re
import numpy as np
import os
from bs4 import BeautifulSoup
import codecs
from collections import OrderedDict
import sys
import argparse


# Documents XML sans balises mot (light)
def extract_annotations_TEI(text, variable):
	'''
		Extraction des annotations dans un document XML (annotations continues et discontinues)
		
		Input : 
			text : texte XML avec annotations
			variable : liste des variables à extraire (nom de tags XML)
			
		Output :
			res : matrice des annotations au format (variable, offset début, offset fin, valeur associée)
	'''
	res = []
	for v in variable:
		for tag in text.find_all(attrs={"subtype" : v}):
			spans = tag.findChildren("span" , recursive=False)
			for child_span in spans:
				id_span = child_span['ana'][1:]
				begin = child_span['from'].split("_")[-1]
				end = child_span['to'].split("_")[-1]
				offsets =str(begin) + ' ' + str(end)
				attributs = {}
				for fs in text.find_all(id=id_span):
					f = fs.findChildren("f" , recursive=False)
					for f_ in f:
						attributs[f_['name']] = f_.string
					
				res.append([v, offsets, attributs])
	return res


def check_args(args):
	if not(args.i):
		e.write("Input path missing\n")
		exit(1)


if __name__ == '__main__':
	o = sys.stdout
	e = sys.stderr

	parser = argparse.ArgumentParser()
	parser.add_argument('-n', '--name', dest='n', type=str, required=False, 
			help="Input path")
	parser.add_argument('-i', '--input', dest='i', type=str, required=True, 
			help="Input path")
	parser.add_argument('-o', '--output', dest='o', type=str, required=False, 
			help="CSVs output folder")
	args = parser.parse_args()


	check_args(args)
	sys.setrecursionlimit(100000)

	if args.i:
		print("Processing...")
		path_annotations = os.path.join(args.i, "annotations")
		path_texts = os.path.join(args.i, "texts")

		words_all = []
		words_label_all = []

		tab = []
		for annotation in os.listdir(path_annotations):
			num_annotation = '-'.join(annotation.split('-')[:-1])+'.xml'
			with codecs.open(os.path.join(path_annotations, annotation), 'r', errors='ignore', encoding='utf8') as fp_annotation:
				text = BeautifulSoup(fp_annotation, 'html.parser')
				variables = [annotationGrp["subtype"] for annotationGrp in text.find_all('annotationgrp')]
				res = extract_annotations_TEI(text.annotations, variables)
				with codecs.open(os.path.join(path_texts, num_annotation), 'r', errors='ignore', encoding='utf8') as fp_text:
					text_brut = BeautifulSoup(fp_text, 'html.parser')
					words = text_brut("w")
					words_label = ['O' for i in range(len(words))]
					for elem in res:
						offsets = elem[1].split()
						words_annotation = words[int(offsets[0])-1:int(offsets[1])]
						for i in range(int(offsets[0])-1,int(offsets[1])):
							if words_label[i]  == 'O':
								words_label[i] = elem[0]
							else:
								words_label[i] +=  '---' + elem[0]
						text_annotation = [w.contents[0].text for w in words_annotation]
						text_annotation = ' '.join(text_annotation)
						tab_row = [num_annotation, text_annotation, elem[1], elem[0]]
						tab.append(tab_row)
			words_all += [w.contents[0].text for w in words]
			words_label_all += words_label

		df_visualisation = pd.DataFrame(data=np.asarray(tab),columns=['num_doc', 'texte', 'offset', 'catégorie'])

		d = {'mot':words_all,'label':words_label_all}
		df_output = pd.DataFrame(d)

		if args.o:
			output_folder = args.o
		else:
			output_folder = './'

		if args.n:
			name_visu = args.n+"_visualisation.csv"
			name_output = args.n+"_output.csv"
		else:
			name_visu = "annotations_visualisation.csv"
			name_output = "annotations_output.csv"
		print("Writing CSVs...")
		if not os.path.exists(output_folder):
    			os.makedirs(output_folder)
		export_csv_vis = df_visualisation.to_csv(os.path.join(output_folder, name_visu), index=False, encoding='utf-8', quotechar='"')
		export_csv_output = df_output.to_csv(os.path.join(output_folder, name_output), index=False, encoding='utf-8', quotechar='"')
		print("Done.")



