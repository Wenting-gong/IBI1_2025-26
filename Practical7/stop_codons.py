import re
#file name
input_fa = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_fa = "stop_genes.fa"

# Read file
f = open(input_fa, "r")
lines = f.readlines()
f.close()

#store genes in dictionary
genes = {}
current_name = ""
current_seq = ""
for line in lines:
    line = line.strip()
    if not line:
        continue
    if line.startswith(">"):
        if current_name:
            genes[current_name] = current_seq
        current_name = line.split()[0][1:]
        current_seq = ""
    else:
        current_seq += line
if current_name:
    genes[current_name] = current_seq

#find stop codons
out = open(output_fa, "w")
start = "ATG"
stops = {"TAA", "TAG", "TGA"}
for name, seq in genes.items():
    # find start codon
    start_pos = seq.find(start)
    if start_pos == -1:
        continue
    
    # check for stop codons
    found = set()
    for i in range(start_pos + 3, len(seq) - 2, 3):
        codon = seq[i:i+3]
        if codon in stops:
            found.add(codon)
    
    # write new file
    if found:
        stop_str = ",".join(sorted(found))
        out.write(f">{name} {stop_str}\n")
        out.write(seq + "\n")

out.close()
print("Done!")