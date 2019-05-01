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

picard_dir = '/data/project/breast_cancer_han/exome_seq/hurben/packages/picard/picard-tools-1.115'

for i in range(len(bam_list_readlines)):
	read = bam_list_readlines[i]
	read = read.replace('\n','')

	temp_token = read.split('/')
	bam_file = temp_token[len(temp_token) - 1]

	token = bam_file.split('.')[0]
	file_name = token.split('_')[0]

	print '#Process step ', bam_file


	#samtools sort
	samtools_sort_cmd = 'samtools sort ' + str(read) + ' ' + str(file_name) + '_sorted'
	print 'MESSAGE : ', samtools_sort_cmd
	os.system(samtools_sort_cmd)


	sorted_bam_file = str(file_name) + '_sorted.bam'
	sorted_rg_bam_file = str(file_name) + '_rg_sorted.bam'

	#add readgroups
	rg_add_cmd = 'java -jar ' + str(picard_dir)+'/AddOrReplaceReadGroups.jar INPUT=' + str(sorted_bam_file) + ' OUTPUT=' + str(sorted_rg_bam_file) + ' RGLB=NULL RGPL=illumina RGPU=NULL RGSM=' + str(file_name) 
	print 'MESSAGE : ', rg_add_cmd
	os.system(rg_add_cmd)


	#mark_dup_cmd

	dedup_sorted_rg_bam_file = str(file_name) + '_dedup_rg_sorted.bam'
	matrix_file = str(file_name) + '_dedup_rg_sorted_matrix.txt'

	mark_dup_cmd = 'java -jar ' +str(picard_dir)+'/MarkDuplicates.jar INPUT=' + str(sorted_rg_bam_file) + ' OUTPUT=' + str(dedup_sorted_rg_bam_file)+ ' M=' + str(matrix_file)
	print 'MESSAGE : ', mark_dup_cmd
	os.system(mark_dup_cmd)


	#removing unneccesory files
	rm_sorted_bam = 'rm ' +str(sorted_bam_file)
	os.system(rm_sorted_bam)

	rm_rg_sorted_bam = 'rm ' +str(sorted_rg_bam_file)
	os.system(rm_rg_sorted_bam)


	#indexing bam
	bam_index_cmd = 'java -jar ' + str(picard_dir) + '/BuildBamIndex.jar INPUT=' +str(dedup_sorted_rg_bam_file)
	print 'MESSAGE : ', bam_index_cmd
	
	os.system(bam_index_cmd)





	
	



