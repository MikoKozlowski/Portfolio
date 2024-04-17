"""
Author: Miko Kozlowski
Date: October 2023

Generate a figure ready bar plot with overlayed swarmplot and statistics
"""

# import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statannotations.Annotator import Annotator
import pingouin as pg

# read the data frame
df = pd.read_excel("../IF/PMP2_DTA_Tmx@TueFri_long_term/12wks_tmx_+_12wks_regen/IF_Regen_Quant_PMP2_MBP_cTUJ.xlsx")

# create pairs between which the statistic tests will be calculated
pairs = [
    [('PMP2', 'PMP2-Cre(+); DTA(+); 12 wks Tmx+12 wks Regen'), ('PMP2', 'PMP2-Cre(+); DTA(+); 12 wks Tmx')],
    [('PMP2', 'PMP2-Cre(-); DTA(+); 12 wks Tmx+12 wks Regen'), ('PMP2', 'PMP2-Cre(+); DTA(+); 12 wks Tmx+12 wks Regen')],
    [('MBP', 'PMP2-Cre(+); DTA(+); 12 wks Tmx+12 wks Regen'), ('MBP', 'PMP2-Cre(+); DTA(+); 12 wks Tmx')],
    [('MBP', 'PMP2-Cre(-); DTA(+); 12 wks Tmx+12 wks Regen'), ('MBP', 'PMP2-Cre(+); DTA(+); 12 wks Tmx+12 wks Regen')],
    [('cTUJ', 'PMP2-Cre(+); DTA(+); 12 wks Tmx+12 wks Regen'), ('cTUJ', 'PMP2-Cre(+); DTA(+); 12 wks Tmx')],
    [('cTUJ', 'PMP2-Cre(-); DTA(+); 12 wks Tmx+12 wks Regen'), ('cTUJ', 'PMP2-Cre(+); DTA(+); 12 wks Tmx+12 wks Regen')],
    [('ChAT', 'PMP2-Cre(+); DTA(+); 12 wks Tmx+12 wks Regen'), ('ChAT', 'PMP2-Cre(+); DTA(+); 12 wks Tmx')],
    [('ChAT', 'PMP2-Cre(-); DTA(+); 12 wks Tmx+12 wks Regen'), ('ChAT', 'PMP2-Cre(+); DTA(+); 12 wks Tmx+12 wks Regen')]
]

###################################
############ FEMORAL ##############
###################################

# divide the dataframe into smaller one based on the cell investigated cell marker
df_PMP2 = df[df['Target'] == 'PMP2']
df_MBP = df[df['Target'] == 'MBP']
df_cTUJ = df[df['Target'] == 'cTUJ']
df_ChAT = df[df['Target'] == 'ChAT']

# perform anova between the genotypes (col 'Genotypes 2') using 'Count' column as dependent variable
anova_PMP2 = df_PMP2.anova(dv='Count', between='Genotype 2')
# perform posthoc test
posthoc_PMP2 = pg.pairwise_tests(data=df_PMP2, dv='Count', between='Genotype 2', padjust='fdr_bh')
# extract p_values
p_vals_PMP2 = np.array(posthoc_PMP2['p-corr'])
# remove the second value as it will not be needed for plotting
p_vals_PMP2 = np.delete(p_vals_PMP2, 1)

anova_MBP = df_MBP.anova(dv='Count', between='Genotype 2')
posthoc_MBP = pg.pairwise_tests(data=df_MBP, dv='Count', between='Genotype 2', padjust='fdr_bh')
p_vals_MBP = np.array(posthoc_MBP['p-corr'])
p_vals_MBP = np.delete(p_vals_MBP, 1)

anova_cTUJ = df_cTUJ.anova(dv='Count', between='Genotype 2')
posthoc_cTUJ = pg.pairwise_tests(data=df_cTUJ, dv='Count', between='Genotype 2', padjust='fdr_bh')
p_vals_cTUJ = np.array(posthoc_cTUJ['p-corr'])
p_vals_cTUJ = np.delete(p_vals_cTUJ, 1)

anova_ChAT = df_ChAT.anova(dv='Count', between='Genotype 2')
posthoc_ChAT = pg.pairwise_tests(data=df_ChAT, dv='Count', between='Genotype 2', padjust='fdr_bh')
p_vals_ChAT = np.array(posthoc_ChAT['p-corr'])
p_vals_ChAT = np.delete(p_vals_ChAT, 1)

# create an array of all calculated p_values
p_vals = np.concatenate([p_vals_PMP2, p_vals_MBP, p_vals_cTUJ, p_vals_ChAT])

# create a figure
#plt.figure(figsize=(21,7.5))
plt.figure(figsize=(16,12))
# create a barplot with cell marker on the X-axis and the count numbers on the Y-axis. Separate datapoint based on the 'Genotype 2'
barplot = sns.barplot(data=df, x='Target', y='Count', hue='Genotype 2', edgecolor='black', alpha=1, palette=['grey', 'red', 'dodgerblue'], lw=4, errcolor='black', errwidth=4, capsize=0.2)
# overlay with swarmplot
swarmplot = sns.swarmplot(data=df, x='Target', y='Count', hue='Genotype 2', dodge=True, size=12, palette=['darkgrey','darkred', 'dodgerblue'], edgecolor='black', linewidth=2)
# create an annotation object to show put the significance tests on the plot.
annotator = Annotator(ax=swarmplot, pairs=pairs, data=df, x='Target', y='Count', hue='Genotype 2')
# coonfigure the layout od the annotation
annotator.configure(text_format="star", fontsize='xx-large', text_offset=3, line_width=2, line_height=0.02)
# annote using the pre-calculated p_values
annotator.set_pvalues_and_annotate(p_vals)
# adjust x and y lables
plt.ylabel('Count per mm\N{SUPERSCRIPT TWO}', size=30)
plt.xlabel('')
# adjust x and y ticks
barplot.set_xticks(range(4)) # <--- set the ticks first
barplot.set_xticklabels(['PMP2\n(PMP2+ SCs)','MBP\n(myelinating SCs)','β-TUB\n(all axons)', 'ChAT\n(motor axons)'])
plt.xticks(size=20)
plt.yticks(size=20)
# adjust the plot title
plt.title('Cell Abundance in Femoral Nerve', size=35)
# in the figure legend, how only barplot
h,l = barplot.get_legend_handles_labels()
plt.legend(h[3:7],l[3:7], loc=2, fontsize = 16)
# set tight layout
plt.tight_layout()

# save the plot
#plt.savefig("../IF/PMP2_DTA_Tmx@TueFri_long_term/12wks_tmx_+_12wks_regen/IF_Regen_Quant_PMP2_MBP_cTUJ.tiff",  bbox_inches='tight')
plt.savefig("../IF/PMP2_DTA_Tmx@TueFri_long_term/12wks_tmx_+_12wks_regen/IF_Regen_Quant_PMP2_MBP_cTUJ_pp.tiff",  bbox_inches='tight')

