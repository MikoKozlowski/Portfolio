import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statannotations.Annotator import Annotator

df = pd.read_excel('../Behavioral_Analysis/Ephys_12_weeks.xlsx')
df = df.sort_values(['Genotype 2','Tag'], ascending=[False,False])

# data = pd.melt(df,id_vars='Timepoint')
# data

######################################
############### CMAP #################
######################################

fig, axes = plt.subplots(2,3, figsize=(12,10))
fig.suptitle('Motor Nerve Electrophysiology', size=30)
pairs =[[('PMP2-Cre(-); DTA(+)'),('PMP2-Cre(+); DTA(+)')]]
#axes[0,1].set_visible(False)
sns.barplot(ax=axes[0,0], data=df, x='Genotype 2', y='Ankle Latency', edgecolor='black', alpha=1, palette=['grey', 'red'], lw=4, errcolor='black', errwidth=4, capsize=0.2)
s1 = sns.swarmplot(ax=axes[0,0],data=df, x='Genotype 2', y='Ankle Latency', dodge=False, size=12, palette=['darkgrey','darkred'], edgecolor='black', linewidth=2)
annotator = Annotator(ax=s1, pairs=pairs, data=df, x='Genotype 2', y='Ankle Latency')
annotator.configure(test="t-test_ind", text_format="star", fontsize='x-large', text_offset=3, line_width=2, line_height=0.02).apply_and_annotate()
#sns.swarmplot(ax=axes[0,0], data=df, x='Genotype 2', y='SN Latency', hue=df[['Genotype 2','Tag','Sex']].apply(tuple, axis=1),
#              dodge=False, size=13, palette=['blue','orange','magenta','darkred','aquamarine','green',
#                       'black','lawngreen','purple','deepskyblue','gold','slategray'], edgecolor='black', linewidth=2)
axes[0,0].set_title('CMAP Latency\nStimulated in Ankle', size=17)
axes[0,0].set_xlabel('')
axes[0,0].tick_params(axis='x', labelsize=10)
axes[0,0].tick_params(axis='y', labelsize=10)
axes[0,0].set_ylabel('Milliseconds',size=15)
#axes[0,0].get_legend().remove()
sns.barplot(ax=axes[0,1], data=df, x='Genotype 2', y='Ankle Amp', edgecolor='black', alpha=1, palette=['grey', 'red'], lw=4, errcolor='black', errwidth=4, capsize=0.2)
s2 = sns.swarmplot(ax=axes[0,1],data=df, x='Genotype 2', y='Ankle Amp', dodge=False, size=12, palette=['darkgrey','darkred'], edgecolor='black', linewidth=2)
annotator = Annotator(ax=s2, pairs=pairs, data=df, x='Genotype 2', y='Ankle Amp')
annotator.configure(test="t-test_ind", text_format="star", fontsize='x-large', text_offset=3, line_width=2, line_height=0.02).apply_and_annotate()
#sns.swarmplot(ax=axes[0,1], data=df, x='Genotype 2', y='SN Amp', hue=df[['Genotype 2','Tag','Sex']].apply(tuple, axis=1),
#              dodge=False, size=13, palette=['blue','orange','magenta','darkred','aquamarine','green',
#                       'black','lawngreen','purple','deepskyblue','gold','slategray'], edgecolor='black', linewidth=2)
axes[0,1].set_title('CMAP Amplitude\nStimulated in Ankle', size=17)
axes[0,1].set_xlabel('')
axes[0,1].tick_params(axis='x', labelsize=10)
axes[0,1].tick_params(axis='y', labelsize=10)
axes[0,1].set_ylabel('Amplitude [mV]',size=15)
#axes[0,1].get_legend().remove()
sns.barplot(ax=axes[0,2], data=df, x='Genotype 2', y='SN CV', edgecolor='black', alpha=1, palette=['grey', 'red'], lw=4, errcolor='black', errwidth=4, capsize=0.2)
s3 = sns.swarmplot(ax=axes[0,2],data=df, x='Genotype 2', y='SN CV', hue='Genotype 2', dodge=False, size=12, palette=['darkgrey','darkred'], edgecolor='black', linewidth=2)
annotator = Annotator(ax=s3, pairs=pairs, data=df, x='Genotype 2', y='SN CV')
annotator.configure(test="t-test_ind", text_format="star", fontsize='x-large', text_offset=3, line_width=2, line_height=0.02).apply_and_annotate()
#sns.swarmplot(ax=axes[0,2], data=df, x='Genotype 2', y='SN CV', hue=df[['Genotype 2','Tag','Sex']].apply(tuple, axis=1),
#              dodge=False, size=13, palette=['blue','orange','magenta','darkred','aquamarine','green',
#                       'black','lawngreen','purple','deepskyblue','gold','slategray'], edgecolor='black', linewidth=2)
axes[0,2].set_title('Motor Neuron\nConduction Velocity', size=17)
axes[0,2].set_ylabel('Velocity [m/s]',size=15)
axes[0,2].set_xlabel('')
axes[0,2].tick_params(axis='x', labelsize=10)
axes[0,2].tick_params(axis='y', labelsize=10)
#axes[0,2].legend(bbox_to_anchor=(1,1))
axes[0,2].get_legend().remove()
sns.barplot(ax=axes[1,0], data=df, x='Genotype 2', y='SN Latency', edgecolor='black', alpha=1, palette=['grey', 'red'], lw=4, errcolor='black', errwidth=4, capsize=0.2)
s4 = sns.swarmplot(ax=axes[1,0], data=df, x='Genotype 2', y='SN Latency', dodge=False, size=12, palette=['darkgrey','darkred'], edgecolor='black', linewidth=2)
annotator = Annotator(ax=s4, pairs=pairs, data=df, x='Genotype 2', y='SN Latency')
annotator.configure(test="t-test_ind", text_format="star", fontsize='x-large', text_offset=3, line_width=2, line_height=0.02).apply_and_annotate()
#sns.swarmplot(ax=axes[1,0], data=df, x='Genotype 2', y='SNAP Amp', hue=df[['Genotype 2','Tag','Sex']].apply(tuple, axis=1),
#              dodge=False, size=13, palette=['blue','orange','magenta','darkred','aquamarine','green',
#                       'black','lawngreen','purple','deepskyblue','gold','slategray'], edgecolor='black', linewidth=2)
axes[1,0].set_title('CMAP Latency\nStimulated in Sciatic Notch', size=17)
axes[1,0].set_ylabel('Milliseconds',size=15)
axes[1,0].set_xlabel('')
axes[1,0].tick_params(axis='x', labelsize=10)
axes[1,0].tick_params(axis='y', labelsize=10)
#axes[1,0].get_legend().remove()
sns.barplot(ax=axes[1,1], data=df, x='Genotype 2', y='SN Amp', edgecolor='black', alpha=1, palette=['grey', 'red'], lw=4, errcolor='black', errwidth=4, capsize=0.2)
s5 = sns.swarmplot(ax=axes[1,1], data=df, x='Genotype 2', y='SN Amp', dodge=False, size=12, palette=['darkgrey','darkred'], edgecolor='black', linewidth=2)
annotator = Annotator(ax=s5, pairs=pairs, data=df, x='Genotype 2', y='SN Amp')
annotator.configure(test="t-test_ind", text_format="star", fontsize='x-large', text_offset=3, line_width=2, line_height=0.02).apply_and_annotate()
#sns.swarmplot(ax=axes[1,1], data=df, x='Genotype 2', y='SNAP CV', hue=df[['Genotype 2','Tag','Sex']].apply(tuple, axis=1),
#              dodge=False, size=13, palette=['blue','orange','magenta','darkred','aquamarine','green',
#                       'black','lawngreen','purple','deepskyblue','gold','slategray'], edgecolor='black', linewidth=2)
axes[1,1].set_title('CMAP Amplitude\nStimulated in Sciatic Notch', size=17)
axes[1,1].set_ylabel('Amplitude [mV]',size=15)
axes[1,1].set_xlabel('')
axes[1,1].tick_params(axis='x', labelsize=10)
axes[1,1].tick_params(axis='y', labelsize=10)
#axes[1,1].get_legend().remove()
axes[1,2].set_visible(False)
plt.tight_layout()

# plt.savefig('../Behavioral_Analysis/Ephys_12_weeks_CMAP.tiff', bbox_inches='tight')


######################################
############### SNAP #################
######################################


fig, axes = plt.subplots(1,2, figsize=(8,5))
fig.suptitle('Sensory Nerve Electrophysiology', size=24)
pairs =[[('PMP2-Cre(-); DTA(+)'),('PMP2-Cre(+); DTA(+)')]]
#axes[0,1].set_visible(False)
sns.barplot(ax=axes[0], data=df, x='Genotype 2', y='SNAP Amp', edgecolor='black', alpha=1, palette=['grey', 'red'], lw=4, errcolor='black', errwidth=4, capsize=0.2)
s1 = sns.swarmplot(ax=axes[0],data=df, x='Genotype 2', y='SNAP Amp', dodge=False, size=12, palette=['darkgrey','darkred'], edgecolor='black', linewidth=2)
annotator = Annotator(ax=s1, pairs=pairs, data=df, x='Genotype 2', y='SNAP Amp')
annotator.configure(test="t-test_ind", text_format="star", fontsize='x-large', text_offset=3, line_width=2, line_height=0.02).apply_and_annotate()
#sns.swarmplot(ax=axes[0,0], data=df, x='Genotype 2', y='SN Latency', hue=df[['Genotype 2','Tag','Sex']].apply(tuple, axis=1),
#              dodge=False, size=13, palette=['blue','orange','magenta','darkred','aquamarine','green',
#                       'black','lawngreen','purple','deepskyblue','gold','slategray'], edgecolor='black', linewidth=2)
axes[0].set_title('Sensory Neuron\nAction Potential Amplitude', size=14)
axes[0].set_xlabel('')
axes[0].set_ylabel('Amplitude [μV]',size=12)
axes[0].tick_params(axis='x', labelsize=10)
axes[0].tick_params(axis='y', labelsize=10)
#axes[0,0].get_legend().remove()
sns.barplot(ax=axes[1], data=df, x='Genotype 2', y='SNAP CV', edgecolor='black', alpha=1, palette=['grey', 'red'], lw=4, errcolor='black', errwidth=4, capsize=0.2)
s2 = sns.swarmplot(ax=axes[1],data=df, x='Genotype 2', y='SNAP CV', dodge=False, size=12, palette=['darkgrey','darkred'], edgecolor='black', linewidth=2)
annotator = Annotator(ax=s2, pairs=pairs, data=df, x='Genotype 2', y='SNAP CV')
annotator.configure(test="t-test_ind", text_format="star", fontsize='x-large', text_offset=3, line_width=2, line_height=0.02).apply_and_annotate()
#sns.swarmplot(ax=axes[0,1], data=df, x='Genotype 2', y='SN Amp', hue=df[['Genotype 2','Tag','Sex']].apply(tuple, axis=1),
#              dodge=False, size=13, palette=['blue','orange','magenta','darkred','aquamarine','green',
#                       'black','lawngreen','purple','deepskyblue','gold','slategray'], edgecolor='black', linewidth=2)
axes[1].set_title('Sensory Neuron\nConduction Velocity', size=14)
axes[1].set_xlabel('')
axes[1].set_ylabel('Velocity [m/s]',size=12)
axes[1].tick_params(axis='x', labelsize=10)
axes[1].tick_params(axis='y', labelsize=10)
plt.tight_layout()

# plt.savefig('../Behavioral_Analysis/Ephys_12_weeks_SNAP.tiff', bbox_inches='tight')





#################################################################################################################

plt.figure(figsize=(7,6))
pairs =[[('PMP2-Cre(-); DTA(+)'),('PMP2-Cre(+); DTA(+)')]]
#axes[0,1].set_visible(False)
barplot = sns.barplot(data=df, x='Genotype 2', y='Ankle Latency', edgecolor='black', alpha=1, palette=['grey', 'red'], lw=4, errcolor='black', errwidth=4, capsize=0.2)
swarmplot = sns.swarmplot(data=df, x='Genotype 2', y='Ankle Latency', dodge=False, size=12, palette=['darkgrey','darkred'], edgecolor='black', linewidth=2)
annotator = Annotator(ax=swarmplot, pairs=pairs, data=df, x='Genotype 2', y='Ankle Latency')
annotator.configure(test="t-test_ind", text_format="star", fontsize='xx-large', text_offset=3, line_width=2, line_height=0.02).apply_and_annotate()

#sns.swarmplot(ax=axes[0,0], data=df, x='Genotype 2', y='SN Latency', hue=df[['Genotype 2','Tag','Sex']].apply(tuple, axis=1),
#              dodge=False, size=13, palette=['blue','orange','magenta','darkred','aquamarine','green',
#                       'black','lawngreen','purple','deepskyblue','gold','slategray'], edgecolor='black', linewidth=2)
plt.title('CMAP Latency\nStimulated in Ankle', size=22)
barplot.set_xlabel('')
barplot.tick_params(axis='x', labelsize=14)
barplot.tick_params(axis='y', labelsize=15)
barplot.set_ylabel('Milliseconds',size=20)

plt.savefig('../Behavioral_Analysis/Ephys_12_weeks_Ankle_Latency.tiff', bbox_inches='tight')

#################################################################################################################

plt.figure(figsize=(7,6))
barplot = sns.barplot(data=df, x='Genotype 2', y='Ankle Amp', edgecolor='black', alpha=1, palette=['grey', 'red'], lw=4, errcolor='black', errwidth=4, capsize=0.2)
swarmplot = sns.swarmplot(data=df, x='Genotype 2', y='Ankle Amp', dodge=False, size=12, palette=['darkgrey','darkred'], edgecolor='black', linewidth=2)
annotator = Annotator(ax=swarmplot, pairs=pairs, data=df, x='Genotype 2', y='Ankle Amp')
annotator.configure(test="t-test_ind", text_format="star", fontsize='xx-large', text_offset=3, line_width=2, line_height=0.02).apply_and_annotate()
#sns.swarmplot(ax=axes[0,1], data=df, x='Genotype 2', y='SN Amp', hue=df[['Genotype 2','Tag','Sex']].apply(tuple, axis=1),
#              dodge=False, size=13, palette=['blue','orange','magenta','darkred','aquamarine','green',
#                       'black','lawngreen','purple','deepskyblue','gold','slategray'], edgecolor='black', linewidth=2)
plt.title('CMAP Amplitude\nStimulated in Ankle', size=22)
barplot.set_xlabel('')
barplot.tick_params(axis='x', labelsize=14)
barplot.tick_params(axis='y', labelsize=15)
barplot.set_ylabel('Amplitude [mV]',size=20)

plt.savefig('../Behavioral_Analysis/Ephys_12_weeks_Ankle_Amp.tiff', bbox_inches='tight')

#################################################################################################################

plt.figure(figsize=(7,6))
barplot = sns.barplot(data=df, x='Genotype 2', y='SN CV', edgecolor='black', alpha=1, palette=['grey', 'red'], lw=4, errcolor='black', errwidth=4, capsize=0.2)
swarmplot = sns.swarmplot(data=df, x='Genotype 2', y='SN CV', hue='Genotype 2', dodge=False, size=12, palette=['darkgrey','darkred'], edgecolor='black', linewidth=2)
annotator = Annotator(ax=swarmplot, pairs=pairs, data=df, x='Genotype 2', y='SN CV')
annotator.configure(test="t-test_ind", text_format="star", fontsize='xx-large', text_offset=3, line_width=2, line_height=0.02).apply_and_annotate()
#sns.swarmplot(ax=axes[0,2], data=df, x='Genotype 2', y='SN CV', hue=df[['Genotype 2','Tag','Sex']].apply(tuple, axis=1),
#              dodge=False, size=13, palette=['blue','orange','magenta','darkred','aquamarine','green',
#                       'black','lawngreen','purple','deepskyblue','gold','slategray'], edgecolor='black', linewidth=2)
plt.title('Motor Neuron\nConduction Velocity', size=22)
barplot.set_ylabel('Velocity [m/s]',size=20)
barplot.set_xlabel('')
barplot.tick_params(axis='x', labelsize=14)
barplot.tick_params(axis='y', labelsize=15)
plt.legend().remove()

plt.savefig('../Behavioral_Analysis/Ephys_12_weeks_SN_CV.tiff', bbox_inches='tight')

#################################################################################################################

plt.figure(figsize=(7,6))
barplot = sns.barplot(data=df, x='Genotype 2', y='SN Latency', edgecolor='black', alpha=1, palette=['grey', 'red'], lw=4, errcolor='black', errwidth=4, capsize=0.2)
swarmplot = sns.swarmplot(data=df, x='Genotype 2', y='SN Latency', dodge=False, size=12, palette=['darkgrey','darkred'], edgecolor='black', linewidth=2)
annotator = Annotator(ax=swarmplot, pairs=pairs, data=df, x='Genotype 2', y='SN Latency')
annotator.configure(test="t-test_ind", text_format="star", fontsize='xx-large', text_offset=3, line_width=2, line_height=0.02).apply_and_annotate()
#sns.swarmplot(ax=axes[1,0], data=df, x='Genotype 2', y='SNAP Amp', hue=df[['Genotype 2','Tag','Sex']].apply(tuple, axis=1),
#              dodge=False, size=13, palette=['blue','orange','magenta','darkred','aquamarine','green',
#                       'black','lawngreen','purple','deepskyblue','gold','slategray'], edgecolor='black', linewidth=2)
plt.title('CMAP Latency\nStimulated in Sciatic Notch', size=22)
barplot.set_ylabel('Milliseconds',size=20)
barplot.set_xlabel('')
barplot.tick_params(axis='x', labelsize=14)
barplot.tick_params(axis='y', labelsize=15)
#axes[1,0].get_legend().remove()

plt.savefig('../Behavioral_Analysis/Ephys_12_weeks_SN_Latency.tiff', bbox_inches='tight')

#################################################################################################################

plt.figure(figsize=(7,6))
barplot = sns.barplot(data=df, x='Genotype 2', y='SN Amp', edgecolor='black', alpha=1, palette=['grey', 'red'], lw=4, errcolor='black', errwidth=4, capsize=0.2)
swarmplot = sns.swarmplot(data=df, x='Genotype 2', y='SN Amp', dodge=False, size=12, palette=['darkgrey','darkred'], edgecolor='black', linewidth=2)
annotator = Annotator(ax=swarmplot, pairs=pairs, data=df, x='Genotype 2', y='SN Amp')
annotator.configure(test="t-test_ind", text_format="star", fontsize='xx-large', text_offset=3, line_width=2, line_height=0.02).apply_and_annotate()
#sns.swarmplot(ax=axes[1,1], data=df, x='Genotype 2', y='SNAP CV', hue=df[['Genotype 2','Tag','Sex']].apply(tuple, axis=1),
#              dodge=False, size=13, palette=['blue','orange','magenta','darkred','aquamarine','green',
#                       'black','lawngreen','purple','deepskyblue','gold','slategray'], edgecolor='black', linewidth=2)
plt.title('CMAP Amplitude\nStimulated in Sciatic Notch', size=22)
barplot.set_ylabel('Amplitude [mV]',size=20)
barplot.set_xlabel('')
barplot.tick_params(axis='x', labelsize=14)
barplot.tick_params(axis='y', labelsize=15)
#axes[1,1].get_legend().remove()

plt.savefig('../Behavioral_Analysis/Ephys_12_weeks_SN_Amp.tiff', bbox_inches='tight')

#################################################################################################################

plt.figure(figsize=(5,6))
pairs =[[('PMP2-Cre(-); DTA(+)'),('PMP2-Cre(+); DTA(+)')]]
barplot = sns.barplot(data=df, x='Genotype 2', y='SNAP Amp', edgecolor='black', alpha=1, palette=['grey', 'red'], lw=4, errcolor='black', errwidth=4, capsize=0.2)
swarmplot = sns.swarmplot(data=df, x='Genotype 2', y='SNAP Amp', dodge=False, size=12, palette=['darkgrey','darkred'], edgecolor='black', linewidth=2)
annotator = Annotator(ax=swarmplot, pairs=pairs, data=df, x='Genotype 2', y='SNAP Amp')
annotator.configure(test="t-test_ind", text_format="star", fontsize='xx-large', text_offset=3, line_width=2, line_height=0.02).apply_and_annotate()
#sns.swarmplot(ax=axes[0,0], data=df, x='Genotype 2', y='SN Latency', hue=df[['Genotype 2','Tag','Sex']].apply(tuple, axis=1),
#              dodge=False, size=13, palette=['blue','orange','magenta','darkred','aquamarine','green',
#                       'black','lawngreen','purple','deepskyblue','gold','slategray'], edgecolor='black', linewidth=2)
plt.title('Sensory Neuron\nAction Potential Amplitude', size=22)
barplot.set_xlabel('')
barplot.set_ylabel('Amplitude [μV]',size=20)
barplot.tick_params(axis='x', labelsize=12)
barplot.tick_params(axis='y', labelsize=15)
#axes[0,0].get_legend().remove()

plt.savefig('../Behavioral_Analysis/Ephys_12_weeks_SNAP_Amp.tiff', bbox_inches='tight')

#################################################################################################################

plt.figure(figsize=(5,6))
barplot = sns.barplot(data=df, x='Genotype 2', y='SNAP CV', edgecolor='black', alpha=1, palette=['grey', 'red'], lw=4, errcolor='black', errwidth=4, capsize=0.2)
swarmplot = sns.swarmplot(data=df, x='Genotype 2', y='SNAP CV', dodge=False, size=12, palette=['darkgrey','darkred'], edgecolor='black', linewidth=2)
annotator = Annotator(ax=swarmplot, pairs=pairs, data=df, x='Genotype 2', y='SNAP CV')
annotator.configure(test="t-test_ind", text_format="star", fontsize='xx-large', text_offset=3, line_width=2, line_height=0.02).apply_and_annotate()
#sns.swarmplot(ax=axes[0,1], data=df, x='Genotype 2', y='SN Amp', hue=df[['Genotype 2','Tag','Sex']].apply(tuple, axis=1),
#              dodge=False, size=13, palette=['blue','orange','magenta','darkred','aquamarine','green',
#                       'black','lawngreen','purple','deepskyblue','gold','slategray'], edgecolor='black', linewidth=2)
plt.title('Sensory Neuron\nConduction Velocity', size=22)
barplot.set_xlabel('')
barplot.set_ylabel('Velocity [m/s]',size=20)
barplot.tick_params(axis='x', labelsize=12)
barplot.tick_params(axis='y', labelsize=15)

plt.savefig('../Behavioral_Analysis/Ephys_12_weeks_SNAP_CV.tiff', bbox_inches='tight')