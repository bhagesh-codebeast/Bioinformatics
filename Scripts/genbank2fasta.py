import argparse
from Bio import SeqIO

#Argparse arguments
parser = argparse.ArgumentParser(description='\n GenBank to Fasta converter.')
parser.add_argument("-i","--input", help = "input filepath/filename of GenBank file example: Data/inputfile.gb")
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
   
    with open(inputpath, "r") as input_handle:
        with open(outputpath, "w") as output_handle:

            #GenBank parser
            sequences = SeqIO.parse(input_handle, "genbank")

            #writing to a file
            SeqIO.write(sequences, output_handle, "fasta")

            print("\n Fasta file has been created in the folder: "+outputpath)