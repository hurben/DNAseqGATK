#make file list for mutect.

import sys

normal_dir = '//data/project/breast_cancer_han/exome_seq/hurben/recal_data/normal/batch3/'
tumor_dir = '//data/project/breast_cancer_han/exome_seq/hurben/recal_data/tumor/batch3/'

list_argv = sys.argv[1]
list_file = file(list_argv)
list_readlines = list_file.readlines()

normal_list_argv = sys.argv[2]
normal_list_file = file(normal_list_argv)
normal_list_readlines = normal_list_file.readlines()

tumor_list_argv = sys.argv[3]
tumor_list_file = file(list_argv)
tumor_list_readlines = list_file.readlines()


result1_text = file('list_for_mutect1.txt','w')
result2_text = file('list_for_mutect2.txt','w')
result3_text = file('list_for_mutect3.txt','w')
result4_text = file('list_for_mutect4.txt','w')
result5_text = file('list_for_mutect5.txt','w')
result6_text = file('list_for_mutect6.txt','w')
result7_text = file('list_for_mutect7.txt','w')
result8_text = file('list_for_mutect8.txt','w')
result9_text = file('list_for_mutect9.txt','w')
result10_text = file('list_for_mutect10.txt','w')


normal_list = []
tumor_list = []


def list_making(sample_list, readlines):

	for i in range(len(readlines)):
		read = readlines[i]
		read = read.replace('\n','')
		read = read.replace('normal_','')
		read = read.replace('tumor_','')
		sample_list.append(read)


list_making(normal_list, normal_list_readlines)
list_making(tumor_list, tumor_list_readlines)
	
count = 1

for name in normal_list:

	if count <= 5 :

		result1_text.write(str(normal_dir) + 'normal_' +str(name) + '\t' + str(tumor_dir) + 'tumor_' +str(name) + '\n')
	
	if 6 <= count <= 10 :

		result2_text.write(str(normal_dir) + 'normal_' +str(name) + '\t' + str(tumor_dir) + 'tumor_' +str(name) + '\n')
				
	if 11 <= count <= 15 :

		result3_text.write(str(normal_dir) + 'normal_' +str(name) + '\t' + str(tumor_dir) + 'tumor_' +str(name) + '\n')
	
	if 16 <= count <= 20 :

		result4_text.write(str(normal_dir) + 'normal_' +str(name) + '\t' + str(tumor_dir) + 'tumor_' +str(name) + '\n')
	
	if 21 <= count <= 25 :

		result5_text.write(str(normal_dir) + 'normal_' +str(name) + '\t' + str(tumor_dir) + 'tumor_' +str(name) + '\n')

	if 26 <= count <= 30 :

		result6_text.write(str(normal_dir) + 'normal_' +str(name) + '\t' + str(tumor_dir) + 'tumor_' +str(name) + '\n')


	if 31 <= count <= 35 :

		result7_text.write(str(normal_dir) + 'normal_' +str(name) + '\t' + str(tumor_dir) + 'tumor_' +str(name) + '\n')
	

	if 36 <= count <= 40 :

		result8_text.write(str(normal_dir) + 'normal_' +str(name) + '\t' + str(tumor_dir) + 'tumor_' +str(name) + '\n')
	
	if 41 <= count <= 45 :

		result9_text.write(str(normal_dir) + 'normal_' +str(name) + '\t' + str(tumor_dir) + 'tumor_' +str(name) + '\n')

	if 46 <= count <= 50 :

		result10_text.write(str(normal_dir) + 'normal_' +str(name) + '\t' + str(tumor_dir) + 'tumor_' +str(name) + '\n')

	count = count + 1
	


