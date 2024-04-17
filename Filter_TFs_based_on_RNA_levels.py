"""
Author: Miko Kozlowski
Date: June 2023

This script filters the transcription factor candidates found in an ATACseq dataset based on the expression level (RNAseq dataset)
"""

# load modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read TF candidate dataset
PMP2_MPZ_ATAC_AME = pd.read_excel('../PMP2_TF_Analysis/2023_11_30/AME_np_Pmp2_pos_1_SIC0805_FDRcutoff_10_INT_mm10.pc60_filtered_0_8_merged_VS_np_Mpz_pos_SIC825_FDRcutoff_10_INT_mm10.pC60_filtered_0_8_merged.xlsx')

# read RNAseq dataset
Mpz_sciatic_Ribotag = pd.read_excel('../ATAC_seq_QC/sciatic-riboTag.xlsx')

# filter the columns in the TF dataset so that you have TF name (gene), p_val, adj_p_val, e_val
PMP2_MPZ_ATAC_AME = PMP2_MPZ_ATAC_AME[['motif_alt_ID', 'p-value', 'adj_p-value', 'E-value']]
# rename TF name (gene) column
PMP2_MPZ_ATAC_AME = PMP2_MPZ_ATAC_AME.rename({'motif_alt_ID':'Gene'}, axis=1)
# change TF name (gene) format so that only the first letter is capitalized
PMP2_MPZ_ATAC_AME['Gene'] = PMP2_MPZ_ATAC_AME['Gene'].str.capitalize()

# modify the gene column in RNAseq dataset so tht it only has the gene name
Mpz_sciatic_Ribotag['Gene'] = Mpz_sciatic_Ribotag['Gene'].str.split('|', expand=True)[1]
# filter the columns in the TF dataset so that you have gene name and three data from three ribotagged samples
Mpz_sciatic_Ribotag = Mpz_sciatic_Ribotag[['Gene', 'SN_ribotag_1_ATGACAG', 'SN_ribotag_2_GCTTAGA', 'SN_ribotag_3_TGAGGTT']]

# merge both datasets on gene name
Merged = pd.merge(left=PMP2_MPZ_ATAC_AME, right=Mpz_sciatic_Ribotag, on="Gene")
# remove any TFs whose expression = 0 in the ribottaged samples
Merged2 = Merged[Merged['SN_ribotag_1_ATGACAG'] != 0]
Merged2 = Merged2[Merged['SN_ribotag_2_GCTTAGA'] != 0]
Merged2 = Merged2[Merged['SN_ribotag_3_TGAGGTT'] != 0]
# remove any duplicates
Merged2 = Merged2.drop_duplicates('Gene')
# create a new column with an averaged expression score
Merged2['Avg_ribotag'] = Merged2[['SN_ribotag_1_ATGACAG','SN_ribotag_2_GCTTAGA','SN_ribotag_3_TGAGGTT']].mean(axis=1)
# save data to excel file
Merged2.to_excel('../PMP2_TF_Analysis/2023_11_30/Merged2.xlsx')

