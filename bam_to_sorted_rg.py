#####################################################################
#bam_to_sorted_rg.py										14.06.25
#
#
#
#Description : For project of breast_cancer_han
#
#
#python fasta_to_bam.py [list] [ref file]
#####################################################################

import os
import sys

#input. list of sequences
bam_list_argv = sys.argv[1]
bam_list_file = file(bam_list_argv)
bam_list_readlines = bam_list_file.readlines()

picard_dir = '/data/project/breast_cancer_han/hurben/packages/picard/picard-tools-1.115'

for i in range(len(bam_list_readlines)):
	read = bam_list_readlines[i]
	read = read.replace('\n','')
	token = read.split('.')[0]
	bam_file = token.split('_')[0]

	print '#Process step ', bam_file


	samtools_sort_cmd = 'samtools sort ' + str(read) + ' ' + str(bam_file) + '_sorted'
	os.system(samtools_sort_cmd)

	sorted_bam_file = str(bam_file) + '_sorted.bam'
	
	rg_add_cmd = 'java -jar ' + str(picard_dir)+'/AddOrReplaceReadGroups.jar INPUT=' + str(sorted_bam_file) + ' OUTPUT=' + str(bam_file) +'_rg_sorted.bam RGLB=NULL RGPL=illumina RGPU=NULL RGSM=' + str(bam_file) 
	os.system(rg_add_cmd)

	rm_sorted_bam = 'rm ' +str(bam_file) + '_sorted.bam'
	os.system(rm_sorted_bam)

	bam_index_cmd = 'java -jar ' + str(picard_dir) + '/BuildBamIndex.jar INPUT=' +str(bam_file) + '_rg_sorted.bam'
	os.system(bam_index_cmd)





	
	



