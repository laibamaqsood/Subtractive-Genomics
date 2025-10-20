from Bio import SeqIO
import pandas as pd
seqs_id = []
for seq_records in SeqIO.parse("Non Homologous.fasta",'fasta'):
    data_dict = {}
    data_dict['ID'] = seq_records.id
    seqs_id.append(data_dict)

df = pd.DataFrame(seqs_id)
df.to_excel("Non Homologous IDs.xlsx",index = False)