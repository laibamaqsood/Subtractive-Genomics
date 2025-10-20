# Script to use after Blastp 
from Bio import SeqIO
from Bio import SeqRecord
import pandas as pd
import pandas as pd
import time
from openpyxl.workbook import Workbook
# ---------------> Reading Blast Output File from text outfmt-6 form into an excel format
df = pd.read_csv('CD_Blast_Output.text',
                 sep="\t",
                 header=None,
                 names=["query_id", "subject_id", "pct_identity", "aln_length", "n_of_mismatches",
                        "gap_openings", "q_start", "q_end", "s_start", "s_end", "e_value", "bit_score"])
time.sleep(1)
df.to_excel('output.xlsx',index=False)


# time.sleep(1)
# ----------> Saving IDs in a text File for later use 
df = pd.read_excel('output.xlsx')
file = open ('IDs.text','w')
for i in df['query_id']:
    file.write(i + '\n')


time.sleep(1)
# -----------> Reading the IDs from Blast Output File 
with open ('IDs.text','r') as file:
    ids = set(file.read().splitlines())


time.sleep(1)
# ---------> Removing the Homologous Sequences from Fasta and Making new files 
handle1 = open("HomoLogous.fasta","w")
handle2 = open("Non HomoLogous.fasta","w")
for records in SeqIO.parse('querey.fasta','fasta'):
    if records.id in ids:
        SeqIO.write(records,handle1,'fasta')
    else:
        SeqIO.write(records,handle2,'fasta')

time.sleep(1)
# ------- >       To check the number of Sequences in both fasta files 
len_homo = len([rec for rec in SeqIO.parse("HomoLogous.fasta", "fasta")])
print("Length for Homologous is : %i"%len_homo)
len_non_homo = len([rec for rec in SeqIO.parse("Non HomoLogous.fasta", "fasta")])
print("Length for Non-Homologous is : %i"%len_non_homo)