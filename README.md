

Subtractive genomics is a computational approach used to identify pathogen-specific, essential, and non-homologous protein that can serve as novel drug or vaccine target.  
In this project, I implemented a step-by-step pipeline to filter the bacterial proteome and exclude proteins homologous to the human host, focusing on unique and essential bacterial targets.


Methodology Workflow

1. Protein Data Retrieval 
   - Complete proteome of the pathogen was downloaded from **NCBI** in FASTA format.

2. Redundancy Removal
   - Non-redundant protein sequences were obtained using **CD-HIT** (90% similarity threshold).

3. Essential Gene Identification 
   - BLASTp search was performed against the **Database of Essential Genes (DEG)** to identify essential proteins.

4. Host Non-Homology Analysis  
   - BLASTp was executed against the **human reference proteome (Homo sapiens)** to remove host-homologous sequences.

5. Subcellular Localization Prediction  
   - Localization was predicted using **CELLO v.2.5** and **PSORTb** to prioritize cytoplasmic and membrane-associated targets.

6. Druggability Assessment 
   - Identified essential, non-homologous proteins were compared with **DrugBank** entries to evaluate druggability.

