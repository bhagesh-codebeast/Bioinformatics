import warnings
import argparse
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Polypeptide import PPBuilder

#To ignore warnings due to PDB file
warnings.filterwarnings('ignore')

#Argparse arguments
parser = argparse.ArgumentParser(description='\n PDB to Fasta converter.')
parser.add_argument("-i","--input", help = "input filepath/filename of PDB file example: Data/inputfile.pdb")
parser.add_argument("-o","--output", help = "output filepath/filename of fasta file example: Data/outputfile.fasta")

args = parser.parse_args()

#conditions for input & output files
if not args.input:
    print("\n Please enter input file name using -i or --input")
elif not args.output:
    print("\n Please enter Output file name using -o or --ouput")
else:
    inputpath = args.input
    outputpath = args.output

    #PDB parser 
    parser = PDBParser()
    structure = parser.get_structure("",inputpath)

    #for loop to join multiple chains into a single chain
    ppb=PPBuilder()
    protseq = ''
    for pp in ppb.build_peptides(structure):
        protseq += str(pp.get_sequence())

    #writing to a file
    with open(outputpath,'w') as f:
        f.write(">"+outputpath.replace("/","").replace(".","")+"\n"+protseq)
        print("\n Fasta file has been created in the folder: "+outputpath)