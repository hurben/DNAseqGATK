#########################################################################
#SNV_finding.py													14.08.19 -> 15.03.17 -> 15.05.19
#THIS PROGRAM IS FOR PROF. JEENA's recommend
#IN PURPOSE OF HG19 
#
#
#description : from snp file (VCF) :	handling VCF, or SNP information
#			[1] IF VCF:
#				1. make ANNOVAR ready form
#				2. Run ANNOVAR
#
#			[2] IF SNP information (ANNOVAR form)
#				1. Run ANNOVAR
#
#			#note : [1], [2] control , case each.
#
#			[3] ANNOVAR results to triple_filter snp information form.
#				
#
#command line : python SNV_finding.py -n normal.vcf -t tumor.vcf
#########################################################################


#Function 02 : RUN ANNOTATION
#-----------------------------------------------------
#Check file format
#	[1] if the file format is unknown -> ERROR, terminate program
#	[2] if the file format is VCF -> start parsing, make dictionary
#	[3] if the file format is ANNOVAR ready -> proceed next step
#		for annovar ready format. copy normal file and tumor file to 'annovar_ready.normal/tumor'



def annotation(normal_file_format,input_normal_file, program_dir):


	#open files 
	input_normal_open = file(input_normal_file)


	#buffer
	annovar_dir = str(program_dir) + '/annovar'



	########
	#normal#
	########
	print '[NOTICE] Proceeding normal file : ' + str(input_normal_file) 

	file_format = normal_file_format

	if file_format == 'unknown':
		print '[ERROR] Input file format unknown. Please check input file format.'
		print '[ERROR] This program supports VCF and ANNOVAR ready form'
		print '[Advice] Information of ANNOVAR ready form could by found : http://www.openbioinformatics.org/annovar/annovar_input.html'
		print '[NOTICE] Terminating program.'
		quit()

	if file_format == 'VCF':
		print '[NOTICE] Input file : VCF'
		print '[NOTICE] Making VCF file to ANNOVAR ready form'
		make_annovar_ready_form(file_format, input_normal_open, 'temp.annovar_ready')

		print '\n>> EXECUTING ANNOVAR.'
		annovar_cmd = annovar_dir +'/'+ 'annotate_variation.pl -out temp.annotation -buildver hg19 temp.annovar_ready ' + str(annovar_dir) +'/humandb/'
		os.system(annovar_cmd)

		print '[NOTICE] ANNOVAR DONE'



#Function 02-1 : Making ANNOVAR ready form from VCF file
#-----------------------------------------------------

def make_annovar_ready_form(file_format,input_file, output_file):

	#open and readlines
	input_readlines = input_file.readlines()
	output_txt = file(str(output_file),'w')

	#buffers
	annovar_dict = {}

	for i in range(len(input_readlines)):
		read = input_readlines[i]
		read = read.replace('\n','')

		first_token = read.split('||')[0]
		second_token = first_token.split('.')

		contig = second_token[0]
		position = second_token[1]

		third_token = read.split('||')[1]
		fourth_token = third_token.split(':')

		ref_nucleotide = fourth_token[0]
		alt_nucleotide = fourth_token[1]
		

		annovar_dict[contig,position] = [ref_nucleotide, alt_nucleotide]

				
	for key in annovar_dict.keys():
		contig = key[0]

		if 'chr' not in contig:
			contig = 'chr' + str(contig)

		position = key[1]
		ref_nuc = annovar_dict[key][0]
		alt_nuc = annovar_dict[key][1]

		output_txt.write(str(contig) + '\t' + str(position) + '\t' + str(position) +'\t' + str(ref_nuc) +'\t' + str(alt_nuc) + '\tNULL\n')

	output_txt.close()






#Function 03 : MAKE TRIPLE FILTER ready form, from annotation results
#-----------------------------------------------------
#Modified

def annotation_file_to_dict():
	
	#open and readlines
	annotation_file = file('temp.annotation.variant_function')
	annotation_readlines = annotation_file.readlines()

	annotation_dict = {}

	for i in range(len(annotation_readlines)):
		read = annotation_readlines[i]
		read = read.replace('\n','')
		token = read.split('\t')

		if 'dist' not in token[1]:
			
			gene = token[1].split('(')[0]
			gene = gene.split(',')[0]

			try : annotation_dict[gene] += 1
			except KeyError : annotation_dict[gene] = 1

	return annotation_dict
	

#Function 04 : Write final results
#-------------------------------------------------------

def dict_to_text(result_dict,output):
	
	text = file(str(output),'w')

	for key in result_dict.keys():
		text.write(str(key) + '\t' + str(result_dict[key]) + '\n')



#Starting Program : SNP_finding
if __name__ == '__main__':


	import sys
	import argparse
	import subprocess
	import os


	program_dir = os.path.split(os.path.realpath(__file__))[0]
	lib_path = os.path.abspath(str(program_dir[0])+'/')


	#Using Argparse for Option retrival
	parser = argparse.ArgumentParser()	#initialize argparse

	#Note : n = row, m = column
	parser.add_argument('-i','--input_list', dest = 'input_list', help="")	

	args= parser.parse_args()


	#Defining argument variables
	file_list = args.input_list
	file_list_open = file(file_list)
	file_list_readlines = file_list_open.readlines()


	file_format = 'VCF'

	for i in range(len(file_list_readlines)):
		
		read = file_list_readlines[i]
		read = read.replace('\n','')

		input_file = read
		token = read.split('/')
		file_name = token[len(token)-1]
		print file_name

		annotation(file_format, input_file, program_dir)
	
		annotation_dict = annotation_file_to_dict()

		output = str(file_name) + '.gene.txt'
		dict_to_text(annotation_dict, output)


