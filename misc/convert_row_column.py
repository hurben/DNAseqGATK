import sys

data_file = sys.argv[1]
data_open = file(data_file)
data_readlines = data_open.readlines()

data2_file = sys.argv[2]
data2_open = file(data2_file)
data2_readlines = data2_open.readlines()

available_sample_list = []


temp_header = []
temp_dict = {}

for i in range(len(data2_readlines)):

	read = data2_readlines[i]
	read = read.replace('\n','')
	read = read.replace('\r','')
	
	token = read.split('\t')
	

	if i == 0:
		temp_header= token

	if i != 0:
		sample =token[0]
		if sample not in available_sample_list:
			available_sample_list.append(sample)

		ba = token[4]
		da = token[6]
		stand_logpd = token[7]
		standpd = token[9]
		pd = token[8]

		temp_dict[sample,temp_header[4]] = ba
		temp_dict[sample,temp_header[6]] = da
		temp_dict[sample,temp_header[7]] = stand_logpd
		temp_dict[sample,temp_header[8]] = pd
		temp_dict[sample,temp_header[9]] = standpd
			
	

	



dict = {}
sample_list = []
gene_list = []





for i in range(len(data_readlines)):
	read = data_readlines[i]
	read = read.replace('\n','')
	read = read.replace('\r','')
	

	token = read.split('\t')
	gene = token[0]

	if gene not in gene_list:
		gene_list.append(gene)

	if i == 0:
		sample_list = token

	if i != 0:

		for j in range(1, len(token)):
			value = token[j]
			dict[gene,sample_list[j]] = value


txt = file("converted_r_ready.txt",'w')


txt.write('\t'+str(temp_header[4]) + '\t' +str(temp_header[6]) + '\t' + str(temp_header[8]) + '\t' + str(temp_header[7]) + '\t' + str(temp_header[9]))


gene_list.pop(0)

for gene in gene_list:
	txt.write('\t' + str(gene))
txt.write('\n')


for sample in available_sample_list:
	
	ba = temp_dict[sample,temp_header[4]]
	da = temp_dict[sample,temp_header[6]]
	pd = temp_dict[sample,temp_header[8]]
	stand_logpd = temp_dict[sample,temp_header[7]]
	stand_pd = temp_dict[sample,temp_header[9]]
	
	txt.write(str(sample) + '\t'+  str(ba) +'\t'+  str(da) +'\t'+  str(pd) + '\t'+  str(stand_logpd) + '\t' +str(stand_pd))

	for gene in gene_list:
		value = dict[gene, sample]

		txt.write('\t' + str(value))
	txt.write('\n')
		

	

	
