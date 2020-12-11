'''
Author: Bazoge Adrien	
'''

import pandas as pd
from sklearn.metrics import cohen_kappa_score
import sys
import argparse
import statistics
import os
from nltk import agreement

def prep_list_label_binaire(dataframe, label_input):
	return [1 if label_input in elem else 0 for elem in list(dataframe.label)]


def check_args(args):
	if not(args.cohen) and not(args.scott) and not(args.fleiss):
		e.write("Arg -cohen, -scott or -fleiss missing\n")
		exit(1)
	if args.cohen:
		if not(args.f):
			e.write("Arg -f : Input CSV missing\n")
			exit(1)
		if not(args.s):
			e.write("Arg -s : Input CSV missing\n")
			exit(1)
		if not(os.path.exists(args.f)):
			e.write("Arg -f : path doesn't exists\n")
			exit(1)
		if not(os.path.exists(args.s)):
			e.write("Arg -s : path doesn't exists\n")
			exit(1)
	if args.scott:
		if not(args.i):
			e.write("Arg -i : Input path missing\n")
			exit(1)
		if not(os.path.exists(args.i)):
			e.write("Arg -i : path doesn't exists\n")
			exit(1)
	if args.fleiss:
		if not(args.i):
			e.write("Arg -i : Input path missing\n")
			exit(1)
		if not(os.path.exists(args.i)):
			e.write("Arg -i : path doesn't exists\n")
			exit(1)


if __name__ == '__main__':
	o = sys.stdout
	e = sys.stderr

	parser = argparse.ArgumentParser()
	parser.add_argument('-scott', '--scott_pi', dest='scott', required=False, action="store_true",
			help="compute Scott's Pi score")
	parser.add_argument('-cohen', '--cohen_kappa', dest='cohen', required=False, action="store_true",
			help="compute Cohen's Kappa score")
	parser.add_argument('-fleiss', '--fleiss_kappa', dest='fleiss', required=False, action="store_true",
			help="compute Fleiss's Kappa score")
	parser.add_argument('-f', '--first_input', dest='f', type=str, required=False, 
			help="first annotator CSV path (ONLY FOR COHEN'S KAPPA)")
	parser.add_argument('-s', '--second_input', dest='s', type=str, required=False, 
			help="second annotator CSV path (ONLY FOR COHEN'S KAPPA)")
	parser.add_argument('-i', '--input_folder', dest='i', type=str, required=False, 
			help="folder absolute path with all annotators's CSVs (ONLY FOR FLEISS'S KAPPA AND SCOTT'S PI)")
	args = parser.parse_args()

	check_args(args)
	sys.setrecursionlimit(100000)

	if args.cohen:
		if args.f and args.s:
			df_annotation_a1 = pd.read_csv(args.f, encoding='utf-8', keep_default_na=False)
			df_annotation_a2 = pd.read_csv(args.s, encoding='utf-8', keep_default_na=False)

			labels1 = list(set(list(df_annotation_a1.label) + list(df_annotation_a2.label)))
			labels = []
			for elem in labels1:
				if '---' in elem:
					labels += elem.split('---')
				else:
					labels.append(elem)
			labels = list(set(labels))
			labels.remove("O")

			score_categorie = []

			for label in labels:
				print("Entity :", label)
				score = cohen_kappa_score(prep_list_label_binaire(df_annotation_a1, label), prep_list_label_binaire(df_annotation_a2, label))
				score_categorie.append(score)
				print("Cohen\'s Kappa : ", score)
				print()
			print("All entities")
			print("Cohen\'s Kappa : ", statistics.mean(score_categorie))

	elif args.scott:
		if args.i:
			list_files = [i for i in os.listdir(args.i) if i.endswith(".csv")]
			csvs = []
			labels1 = []
			for j in list_files:
				df_annotation = pd.read_csv(os.path.join(args.i, j), encoding='utf-8', keep_default_na=False)
				csvs.append(df_annotation)
				labels1 += list(df_annotation.label)

			labels1 = list(set(labels1))
			labels = []
			for elem in labels1:
				if '---' in elem:
					labels += elem.split('---')
				else:
					labels.append(elem)
			labels = list(set(labels))
			labels.remove("O")

			score_categorie = []

			for label in labels:
				formatted_codes = []
				for index, elem in enumerate(csvs):
					bin_data = prep_list_label_binaire(elem, label)
					formatted_codes += [[(index+1),i,bin_data[i]] for i in range(len(bin_data))]
				ratingtask = agreement.AnnotationTask(data=formatted_codes)
				score = ratingtask.pi()
				score_categorie.append(score)
				print("Entity :", label)
				print('Scott\'s pi:', score)
				print()
			print("All entities")
			print("Scott\'s Pi : ", statistics.mean(score_categorie))

	elif args.fleiss:
		if args.i:
			list_files = [i for i in os.listdir(args.i) if i.endswith(".csv")]
			csvs = []
			labels1 = []
			for j in list_files:
				df_annotation = pd.read_csv(os.path.join(args.i, j), encoding='utf-8', keep_default_na=False)
				csvs.append(df_annotation)
				labels1 += list(df_annotation.label)

			labels1 = list(set(labels1))
			labels = []
			for elem in labels1:
				if '---' in elem:
					labels += elem.split('---')
				else:
					labels.append(elem)
			labels = list(set(labels))
			labels.remove("O")

			score_categorie = []

			for label in labels:
				formatted_codes = []
				for index, elem in enumerate(csvs):
					bin_data = prep_list_label_binaire(elem, label)
					formatted_codes += [[(index+1),i,bin_data[i]] for i in range(len(bin_data))]
				ratingtask = agreement.AnnotationTask(data=formatted_codes)
				score = ratingtask.multi_kappa()
				score_categorie.append(score)
				print("Entity :", label)
				print('Fleiss\'s Kappa:', score)
				print()
			print("All entities")
			print("Fleiss\'s Kappa : ", statistics.mean(score_categorie))


		



