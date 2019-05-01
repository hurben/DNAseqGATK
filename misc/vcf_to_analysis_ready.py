import sys

vcf_name = sys.argv[1]
vcf_file = file(vcf_name)
vcf_readlines = vcf_file.readlines()

dict = {}

for i in range(len(vcf_readlines)):

	if '#' not in vcf_readlines[i][0]:
		read = vcf_readlines[i]
		read = read.replace('\n','')
		
		token = read.split('\t')
	
		chr = token[0]
		pos = token[1]
		id = token[2]
		ref = token[3]
		alt = token[4]

		info = str(ref) + '/' + str(alt)		

		dict[id] = [chr,info,pos]

txt = file("2nd_required_snp.txt",'w')

for id in dict.keys():

	chr = dict[id][0]
	info = dict[id][1]
	pos = dict[id][2]

	txt.write(str(id) + '\t' +str(chr) + '\t' + str(info) + '\t' + str(pos) + '\n')


		
