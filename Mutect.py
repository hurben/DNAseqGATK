#####################################################################
#Mutect.py													14.06.25
#
#
#
#Description : For project of breast_cancer_han
#			   PIPELINE FOR INDEL Realignment, Base Recalibration
#
#
#python
#####################################################################

import os
import sys

#input. list of sequences
bam_list_argv = sys.argv[1]
bam_list_file = file(bam_list_argv)
bam_list_readlines = bam_list_file.readlines()


java_file = '/home/hurben/GATK/packages/jdk1.6.0_45/bin/java'
ref_file = '/home/hurben/GATK/gatk/ref_genome_canonical/hg19_karyotypic.fa'
dbsnp_file = '/home/hurben/GATK/gatk/dbsnp/sorted_dbsnp_138.hg19.vcf'
mutect_file = '/home/hurben/GATK/packages/Mutect/muTect-1.1.4.jar'


#Reading each file
for i in range(len(bam_list_readlines)):
	read = bam_list_readlines[i]
	read = read.replace('\n','')

	sample_token = read.split('\t')
	normal_bam_file = sample_token[0]
	tumor_bam_file = sample_token[1]

#	temp_token = normal_bam_file.split('/')
#	normal_bam = temp_token[len(temp_token) - 1]
	temp_token = tumor_bam_file.split('/')
	tumor_bam = temp_token[len(temp_token) - 1]

#	token = normal_bam.split('.')
	token = tumor_bam.split('.')
	file_name = token[0]
	file_name = file_name.split('.')[0]

	print '#Process step ', file_name
	
	
	
	mutect_out = str(file_name) + '.out'
	mutect_coverage = str(file_name) + '.coverage.wig.txt'
	print mutect_out
	print mutect_coverage
	mutect_cmd = str(java_file) + ' -jar ' + str(mutect_file) + ' -T MuTect -R ' +str(ref_file) + ' --dbsnp ' + str(dbsnp_file) + ' --input_file:normal ' + str(normal_bam_file) + ' --input_file:tumor ' + str(tumor_bam_file) + ' --out ' +str(mutect_out) + ' --coverage_file ' + str(mutect_coverage)
	os.system(mutect_cmd)


