#!/usr/bin/python3

"""
Author: Mikolaj Kozlowski
Date: Feb 2022

Usage: python3 get_gene_coordinates.py <gene_name> <gtf> <scan_distance> <ATAC-seq Peaks BED file> <FASTA_file>

Description:
This script was written to facilitate the search for a transcription factor that controls the expression of the gene of interest (GOI). The script finds the genomic coordinates of GOI,
creates a scanning window upstream and downstream of the gene, finds open chromatin regions in the scanning window, and generates FASTA sequences for these regions. The user has to provide
the script with a 1) gene name (i.e., GAPDH), 2) a GTF file for the appropriate organism (I recommend Ensembl - for hg38:  http://ftp.ensembl.org/pub/release-105/gtf/homo_sapiens/),
3) number of basepairs that will be added upstream and downstream of the beginning of the GOI to create the scanning window, 4) a BED file with already called ATAC-seq peaks,
5) FASTA file for the appropriate organism.

The script returns a file called "FINAL_FASTA.txt" with a summary of GOI (gene name, chromosome number, strandness, gene beginning coordinate, and scan coordinates)
and the open chromatin coordinates and their corresponding FASTA sequences.
"""

###############################################################################################################################################################
#STEP 0 - Import required modules and assign script arguments to variables
###############################################################################################################################################################

import sys
import pybedtools as bd

# Check the correct number of command line arguments
if(len(sys.argv)!= 6): #quits if errors
    sys.exit(__doc__)

# assign script arguments to variables
gene_name = sys.argv[1]
gtf = sys. argv[2]
scan_distance = int(sys.argv[3])
peak_file = sys.argv[4]
FASTA_file = sys.argv[5]

peak_file_name = peak_file.split('/')
peak_file_name = peak_file_name[-2]

###############################################################################################################################################################
#STEP 1 - From the gtf/gff file, isolate the following data for your gene of interest: gene chromosome, gene coordinates, and strand polarity (+ / -)
###############################################################################################################################################################

# create an empty list
gtf_list = []

gtf = open(gtf)
# go line by line in the gtf file
for i in gtf:
    # search the gene name in quatation marks, for example, "GAPDH"
    if "".join(["\"",gene_name,"\""]) in i:
        i = i.strip().split('\t')
        # if the line has the searched gene, add the line to "gtf_list"
        if i[2] == 'gene':
            gene_data = i
gtf.close()

# save gene chromosome, gene beginning coordinate, and strand polarity as appropriate variables
chromosome = 'chr' + gene_data[0]
strandness = gene_data[6]
if strandness == '+':
    gene_beginning = int(gene_data[3])
else:
    gene_beginning = int(gene_data[4])

# establish the borders of the scanning window for the open chromatin regions using gene coodrinates nad "scan_distance"
scan_coordinate_1 = gene_beginning - scan_distance
scan_coordinate_2 = gene_beginning + scan_distance

###############################################################################################################################################################
#STEP 2 - Scan the ATAC-seq peak_file using the data from STEP 1 to find open chromatin regions in the "proximity" of your gene of interest
###############################################################################################################################################################

# create an empty string
peak_coordinates = ""

peak_file = open(peak_file)
# go line by line in the ATAC-seq file with already-called peaks
for i in peak_file:
    # consider only the lines that are on the correct chromosome (gene chromosome)
    i = i.strip().split('\t')
    if i[0] == chromosome:
        # narrow down the peak search to the scanning window coordinates
        if int(i[1]) > scan_coordinate_1 and int(i[2]) < scan_coordinate_2:
            # eliminate redundant records
            if i[0] and i[1] and i[2] not in peak_coordinates:
                # add the chromosome and peak coordinates to "peak_coordinates" string
                peak_coordinates = peak_coordinates + i[0] + "\t" + i[1] + "\t" + i[2] + "\n"
peak_file.close()

###############################################################################################################################################################
#STEP 3 - Using BEDtools, get fasta sequences for the regions found in STEP 2
###############################################################################################################################################################

peak_coordinates_bed = bd.BedTool(peak_coordinates, from_string=True)
peak_sequence = peak_coordinates_bed.sequence(fi=FASTA_file)
fasta_sequence = open(peak_sequence.seqfn).read()

###############################################################################################################################################################
#STEP 4 - Save the fasta sequences to "FINAL_FASTA" file
###############################################################################################################################################################

file = open('Peak_FASTA_of_' + peak_file_name + '_for_' + gene_name + '_scanning_distance_=' + str(scan_distance) + '.txt', "w+")
#file.write("Gene Name" + "\t" + "Chromosome" + "\t" + "Strandness" + "\t" + "Gene Beginninng Coordinate" + "\t" + "Scan Coordinate I" + "\t" + "Scan Coordinate II" + "\n")
#file.write(gene_name + "\t" + chromosome + "\t" + strandness + "\t" + str(gene_beginning) + "\t" + str(scan_coordinate_1) + "\t" + str(scan_coordinate_2) + "\n")
file.write("\n" + fasta_sequence + "\n")
file.close()

