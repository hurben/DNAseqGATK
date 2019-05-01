#analysis_snp_matrix.py      		15.02.20

#analysis of snps
#input = matrix

import sys


matrix_file = sys.argv[1]
open_matrix_file = file(matrix_file)
matrix_readlines = open_matrix_file.readlines()

sample_list = []
matrix_dict = {}
gene_list = []


def write_result(dict,string):
	txt = file(str(string),'w')

	for key in dict.keys():
		txt.write(str(key))
	
		try:
			for i in len(dict[key]):
				txt.write('\t' + str(dict[key][i]))
		except TypeError:
			txt.write('\t' + str(dict[key]))



		txt.write('\n')



for i in range(len(matrix_readlines)):
		
	read = matrix_readlines[i]
	read = read.replace('\n','')
	token = read.split('\t')
	gene = token[0]
	if gene not in gene_list:
		gene_list.append(gene)
	
	if i == 0:
		sample_list = token
		sample_list.pop(0)

	if i != 0:
		for j in range(1,len(token)):
			matrix_dict[gene,sample_list[j-1]] = token[j]

gene_list.pop(0)			

#matrix _dict Dictionary complete


risk_gene_info = sys.argv[2]
open_info = file(risk_gene_info)
info_readlines = open_info.readlines()

risk_gene_info_list = []

for i in range(len(info_readlines)):
	read = info_readlines[i]
	read = read.replace('\n','')
	read = read.replace('\r','')

	risk_gene_info_list.append(read)




text_ready_dict = {}
txt = file('critical_gene.result','w')

txt.write('gene')

for sample in sample_list:
	txt.write('\t'+str(sample))

txt.write('\n')



print risk_gene_info_list

for gene in risk_gene_info_list:
	txt.write(str(gene))
	for sample in sample_list:

		try : 
			snps = matrix_dict[gene,sample]
			txt.write('\t' + str(snps))
		except KeyError :
			print gene, "not in data" 
			break

	txt.write('\n')







		

