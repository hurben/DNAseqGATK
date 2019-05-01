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

#Dictionary complete



gene_average_snp_dict = {}


#average
for gene in gene_list:
	gene_total_snp = 0

	for sample in sample_list:
		gene_total_snp += int(matrix_dict[gene,sample])
	

	gene_average_snp = float(gene_total_snp / len(sample_list))
	gene_average_snp_dict[gene] = gene_average_snp

write_result(gene_average_snp_dict, 'gene_average_snp.txt')

risk_snp_info = sys.argv[2]
open_info = file(risk_snp_info)
info_readlines = open_info.readlines()


snp_list = sys.argv[3]
open_snp_list = file(snp_list)
snp_list_readlines = open_snp_list.readlines()


risk_snp_info_list = []
risk_snp_rs_dict = {}

for i in range(len(info_readlines)):
	read = info_readlines[i]
	read = read.replace('\n','')
	read = read.replace('\r','')

	token = read.split('\t')

	chr = token[1]
	position = token[3]
	info = 'chr' + str(chr) + '.' + str(position)

	rs_id = token[0]

	risk_snp_rs_dict[info] = rs_id
	risk_snp_info_list.append(info)



risk_result_dict ={}
risk_snp_count_dict = {}

print risk_snp_info_list

for i in range(len(snp_list_readlines)):
	read = snp_list_readlines[i]
	read = read.replace('\n','')

	token = read.split('/')
	sample_name = token[len(token) -1].split('.')[0]
	
	open_snp_file = file(read)
	read_snp_file = open_snp_file.readlines()
	
	
	for i in range(len(read_snp_file)):
		read = read_snp_file[i]
		read = read.replace('\n','')
		info = read.split('||')[0]

		#print info

		if info in risk_snp_info_list:
			print "found one!"
			rs_id = risk_snp_rs_dict[info]
			risk_result_dict[sample_name] = rs_id

			try : risk_snp_count_dict[rs_id].append(sample_name)
			except KeyError: risk_snp_count_dict[rs_id] = [sample_name]
		
write_result(risk_snp_count_dict,'40samples.2ndsnps.txt')
#write_result(risk_snp_count_dict,'40samples.77snps.txt')
	
	
	









	
		

