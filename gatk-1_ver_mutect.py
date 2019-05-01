#####################################################################
#gatk-1.py													14.06.25
#
#
#
#Description : For project of breast_cancer_han
#			   PIPELINE FOR INDEL Realignment, Base Recalibration
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

gatk_file = '/home/hurben/GATK/gatk/GenomeAnalysisTK.jar'
ref_file = '/home/hurben/GATK/gatk/ref_genome_canonical/hg19_karyotypic.fa'
dbsnp_file = '/home/hurben/GATK/gatk/dbsnp/sorted_dbsnp_138.hg19.vcf'


#Reading each file
for i in range(len(bam_list_readlines)):
	read = bam_list_readlines[i]
	read = read.replace('\n','')
	
	temp_token = read.split('/')
	bam_file = temp_token[len(temp_token) - 1]

	token = bam_file.split('.')
	file_name = token[0]
	

	print '#Process step ', bam_file, file_name

	#Realigner Target creator
	realign_target_creator_output = str(file_name) + '_intervals.list' #result file
	realign_target_creator_cmd = 'java -jar ' + str(gatk_file) + ' -T RealignerTargetCreator -R ' + str(ref_file) + ' -I ' + str(read) + ' -o ' + str(realign_target_creator_output)
	print 'MESSAGE : ', realign_target_creator_cmd
	os.system(realign_target_creator_cmd)
	



	#Indel Realigner. : Note that RealignerTargetCreator needs to be done.
	realigned_bam = 'realigned_'+str(file_name) + '.bam' # result file
	indel_realigner_cmd = 'java -jar ' + str(gatk_file) + ' -I ' + str(read) + ' -R ' + str(ref_file) + ' -T IndelRealigner -targetIntervals ' + str(realign_target_creator_output) + ' -o ' + str(realigned_bam)
	print 'MESSAGE : ', indel_realigner_cmd
	os.system(indel_realigner_cmd)


	#base recalibration phase 1
	recal_bam_table = 'recal_'+str(realigned_bam) + '.table' # result file
	recal_cmd = 'java -jar ' + str(gatk_file) + ' -T BaseRecalibrator -R ' + str(ref_file) + ' -I ' + str(realigned_bam) + ' -knownSites ' + str(dbsnp_file) + ' -o ' + str(recal_bam_table)
	os.system(recal_cmd)

	#base recalibration phase 1
	apply_recal_bam = 'recal_' + str(realigned_bam)
	apply_recal_cmd = 'java -jar ' + str(gatk_file) + ' -T PrintReads -R ' + str(ref_file) + ' -I ' + str(realigned_bam) + ' -BQSR ' + str(recal_bam_table) + ' -o ' + str(apply_recal_bam)
	os.system(apply_recal_cmd)
	

	
	



