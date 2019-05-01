import sys

input_file = sys.argv[1]
input_open = file(input_file)
input_readlines = input_open.readlines()

output = sys.argv[2]
output_txt = file(output,'w')

dict = {}

for i in range(len(input_readlines)):
	read = input_readlines[i]
	read = read.replace('\n','')
	read = read.replace('[1] ','')

	token = read.split('\\t')
	
	relation = token[0]
	cor = token[1]
	pval = token[2]
	dict[relation] = [cor,pval]



output_txt.write("Density:Gene\tCorrelation\tCorrelation_Status\tP-value\n")
for relation in dict.keys():

	cor = float(dict[relation][0])
	pval = dict[relation][1]
	if cor > 0:
		status = '+'
	if cor < 0:
		status = '-'
	if cor == 0:
		status = '0'

	output_txt.write(str(relation) + '\t' + str(cor) + '\t' + str(status) + '\t' + str(pval) + '\n')
