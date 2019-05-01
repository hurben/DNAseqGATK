#FOR
#exonic, nonsynonymous.


import sys

file_list = sys.argv[1]
list_open = file(file_list)
list_readlines = list_open.readlines()


output = sys.argv[2]
#output_txt = file(output, 'w')










for i in range(len(list_readlines)):
	read = list_readlines[i]
	read = read.replace('\n','')
	
	file_name = read

	print file_name

	open_file = file(file_name)
	file_readlines = open_file.readlines()


	output_name = file_name.split('.')[0] 
	output_name += '.'
	output_name += file_name.split('.')[1]
	output_name += '.'
	output_name += output
	output_txt = file(output_name,'w')

	dict = {}
	for j in range(len(file_readlines)):
	
		read_file = file_readlines[j]
		read_file = read_file.replace('\n','')
		
		token = read_file.split('\t')

		status = token[1]
		status = status.split(' ')[0]


		gene = token[2]
		gene = gene.split(":")[0]


		if status == 'nonsynonymous' or status == 'frameshift':
	
			try : dict[gene] += 1
			except KeyError : dict[gene] = 1

	print "Number of Genes: ", len(dict.keys())

	for gene in dict.keys():
		count = dict[gene]

		output_txt.write(str(gene) +'\t' + str(count) + '\n')
		


	

					

		

	
