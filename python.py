from Bio import SeqIO
from Bio import SeqRecord
import pandas as pd
import time

# ---------------> Reading Blast Output File from text outfmt-6 form into an excel format
df = pd.read_csv('output_with_-10.txt',
                 sep="\t",
                 header=None,
                 names=["query_id", "subject_id", "pct_identity", "aln_length", "n_of_mismatches",
                        "gap_openings", "q_start", "q_end", "s_start", "s_end", "e_value", "bit_score"])
time.sleep(1)
df.to_excel('output_with_1e-10.xlsx',index=False)