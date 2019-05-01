####################################################################
#snp_files_to_matrix.py								 	15.05.20
#
#
#
#
#
#
#
#
#####################################################################

import sys

file_list = sys.argv[1]
open_file_list = file(file_list)
read_file_list = open_file_list.readlines()


matrix_dict = {}
gene_list = []
sample_list = []

for i in range(len(read_file_list)):
	read = read_file_list[i]
	read = read.replace('\n','')
	
	sample_name = read.split('.')[0]

	if sample_name in sample_list:
		print 'something wrong with sample name'
	if sample_name not in sample_list:
		sample_list.append(sample_name)
	
	file_name = read

	open_file_name = file(file_name)
	read_file_name = open_file_name.readlines()

	for i in range(len(read_file_name)):
		read_2nd = read_file_name[i]
		read_2nd = read_2nd.replace('\n','')
		token = read_2nd.split('\t')

		gene = token[0]
		if gene not in gene_list:
			gene_list.append(gene)

		snv_count = token[1]

		matrix_dict[sample_name,gene] = snv_count


			

output_text = file('snv.gene.matrix.txt','w')

output_text.write('gene')
for sample in sample_list:
	output_text.write('\t' + str(sample))
output_text.write('\n')

for gene in gene_list:
	output_text.write(str(gene))
	for sample in sample_list:
		try : snv_count = matrix_dict[sample,gene]
		except KeyError : snv_count = 0
		output_text.write('\t'+str(snv_count))
	output_text.write('\n')






	

	

		

	



