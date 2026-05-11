import re

input_fa = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_fa = "stop_genes.fa"

# Read fasta file
with open(input_fa, "r") as f:
    lines = f.readlines()

# Store gene names and sequences
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

# Search for ORFs and stop codons
with open(output_fa, "w") as out:
    start_codon = "ATG"
    stop_codons = {"TAA", "TAG", "TGA"}

    for name, seq in genes.items():
        found_stops = set()
        # Find all positions of ATG in the sequence
        all_atg_positions = [match.start() for match in re.finditer("ATG", seq)]

        # Check every ORF starting from each ATG
        for start_pos in all_atg_positions:
            # Search in-frame codons after current ATG
            for i in range(start_pos + 3, len(seq) - 2, 3):
                codon = seq[i:i+3]
                if codon in stop_codons:
                    found_stops.add(codon)
                    # Stop at the first stop codon of this ORF
                    break

        if found_stops:
            stop_str = ",".join(sorted(found_stops))
            out.write(f">{name} {stop_str}\n")
            out.write(seq + "\n")

print("Done!")