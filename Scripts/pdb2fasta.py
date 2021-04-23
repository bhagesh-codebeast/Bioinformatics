from Bio.PDB.Polypeptide import PPBuilder

ppb=PPBuilder()
protseq = ''
for pp in ppb.build_peptides(structure):
    protseq += str(pp.get_sequence())
print(protseq)