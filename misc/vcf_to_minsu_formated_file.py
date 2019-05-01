#from VCF file resulted by GATK-RNA-seq


import sys


vcf_file = sys.argv[1]
vcf_open = file(vcf_file)
vcf_readlines = vcf_open.readlines()


snv_dict = {}
indel_dict = {}

file_token = vcf_file.split('_')
sample_name = file_token[2]


for i in range(len(vcf_readlines)):
	read = vcf_readlines[i]
	read = read.replace('\n','')
	
	if '#' not in read[0]:
		token = read.split('\t')
		chromosome = token[0]
		pos = token[1]
		ref = token[3]
		alt = token[4]	
		key = str(chromosome) + '.' + str(pos)
	
		if len(ref) >= 2 or len(alt) >= 2 :
			
			indel_dict[key] = [ref,alt]
		else :
			snv_dict[key] = [ref,alt]

result_snv_text = file(str(sample_name) + '.SNV.txt','w')
result_indel_text = file(str(sample_name) + '.INDEL.txt','w')


#function write results

print len(snv_dict)
print len(indel_dict)


def write_results(text, dict):

	for key in dict.keys():
	
		ref = dict[key][0]
		alt = dict[key][1]
	
		text.write(str(key) +'||' + str(ref) + ':' + str(alt) +'\n')




write_results(result_snv_text,snv_dict)
write_results(result_indel_text,indel_dict)
