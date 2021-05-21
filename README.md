# Bioinformatics
#### **Python Scripts & Jupyter NoteBooks to Visualise & Analyse Biological Sequence data**

# A. Requirements

#### **Script Pre-requisites**
    
    *Python pip & Biopython*, which can be installed using the following command: 
    ```
    pip install biopython
    ```

#### **Jupyter Notebook Pre-requisites** 
    
    *Python pip, Biopython & Jupyter notebook*, which can be installed using the following command: 
    ```
    pip install biopython && pip install notebook
    ```

    Run the notebooks by opening command-line/shell in the desired folder and typing in 
    ``` 
    jupyter notebook 
    ```

# B. Python Scripts
#### Clone this repo to run the scripts 👇

https://user-images.githubusercontent.com/59648429/118191110-b49dcd00-b461-11eb-921c-ddf4781eb162.mp4

---
1. [**Script to convert PDB files to Fasta format**](https://github.com/bhagesh-codebeast/Bioinformatics/blob/main/Scripts/pdb2fasta.py)

    Use case:
  
    ```
    python pdb2fasta.py -i folder/inputfile.pdb -o folder/outputfile.fasta
    ```
2. [**Script to convert GenBank files to Fasta format**](https://github.com/bhagesh-codebeast/Bioinformatics/blob/main/Scripts/genbank2fasta.py)

    Use case:
  
    ```
    python genbank2fasta.py -i folder/inputfile.gb -o folder/outputfile.fasta
    ```

3. [**Script to convert FastQ files to Fasta format**](https://github.com/bhagesh-codebeast/Bioinformatics/blob/main/Scripts/fastq2fasta.py)

    Use case:
  
    ```
    python fastq2fasta.py -i folder/inputfile.fastq -o folder/outputfile.fasta
    ```
3. **Script to download Fasta, GenBank & PDB files**

    Use case:
  
    ```
    python biodown.py -i inputID.txt -o outputlocation -f seqformat(gb/fa/pdb)
    ```
3. **Script to output basic statistics and visualisation**

    Use case:
  
    ```
    python seqstats.py -i folder/inputfile.gb/fa/pdb -o folder/outputfile.pdf -f seqformat(gb/fa/pdb)
    ```

# C. Jupyter NoteBooks

1. [**Sequence Parsing & Reading**](https://github.com/bhagesh-codebeast/Bioinformatics/blob/main/Notebooks/sequence_parsing%26reading.ipynb)
2. [**Sequence Downloading**](https://github.com/bhagesh-codebeast/Bioinformatics/blob/main/Notebooks/sequence_download.ipynb)
3. **Sequence Statistics & visualisation**

# D. Binder
Copy GitHub repository URL below and paste it in [**Binder**](https://mybinder.org/) to view & run the jupyter notebooks
```
https://github.com/bhagesh-codebeast/bioinformtics/tree/main/Notebooks
````

#### Connect with me:

[![](https://img.shields.io/badge/linkedin-bhageshhunakunti-informational?style=flat&logo=LinkedIn&logoColor=white&color=2bbc8a)](https://www.linkedin.com/in/bhagesh-hunakunti/)
![](https://img.shields.io/badge/mail-hunakuntibhagesh@gmail.com-informational?style=flat&logo=gmail&logoColor=white&color=2bbc8a)
