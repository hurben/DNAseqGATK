#####################################################################
#fasta_to_bam.py										14.06.25
#
#
#
#Description : For project of breast_cancer_han
#				[1] RUN BWA
#				[2] SAM -> Bam
#
#
#python fasta_to_bam.py [list] [ref file]
#####################################################################

import os
import sys

#input. list of sequences
seq_list_argv = sys.argv[1]
seq_list_file = file(seq_list_argv)
seq_list_readlines = seq_list_file.readlines()

ref_file = '//data/project/breast_cancer_han/exome_seq/hurben/gatk/ref_genome_canonical/hg19_karyotypic.fa'

log = file(str(seq_list_argv) + '.log','w')



for i in range(len(seq_list_readlines)):
	read = seq_list_readlines[i]
	read = read.replace('\n','')

	token = read.split('\t')
	print '#Process step ', token

	file_1 = token[0] 
	file_2 = token[1] 

	temp_1_token = file_1.split('/')	
	temp_2_token = file_2.split('/')	

	temp_1_length = len(temp_1_token)
	temp_2_length = len(temp_2_token)

	temp_1 = temp_1_token[temp_1_length -1]
	temp_2 = temp_2_token[temp_2_length -1]

	result_name = str(temp_1) + str(temp_2)
	result_name_sam = str(result_name) + '.sam'


	bwa_cmd = 'bwa mem -t 8 ' + str(ref_file) + ' ' + str(file_1) + ' ' + str(file_2) + ' > ' + str(result_name_sam)
	log.write('CMD USING ' + str(bwa_cmd) + '\n')
	os.system(bwa_cmd)

	sam_to_bam_cmd = 'samtools view -Sb ' + str(result_name_sam) + ' > ' + str(result_name) + '.bam'
	log.write('CMD USING ' + str(sam_to_bam_cmd) + '\n')
	os.system(sam_to_bam_cmd)

	rm_cmd = 'rm ' + str(result_name_sam)
	os.system(rm_cmd)




	
	



