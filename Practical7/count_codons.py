import re
import matplotlib.pyplot as plt

# Input and validate the stop codon
while True:
    stop_codon = input('Please input a stop codon (TAA, TAG, TGA): ')
    if stop_codon in ['TAA', 'TAG', 'TGA']:
        break
    print("Invalid stop codon! Please enter TAA, TAG, or TGA.")

# Read FASTA file
input_fa = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
try:
    with open(input_fa, 'r') as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f"Error: File {input_fa} not found!")
    exit(1)

# Store gene name and sequence
genes = {}
current_name = ""
current_seq = ""

for line in lines:
    line = line.strip()
    if not line:
        continue
    if line.startswith(">"):
        # Save previous gene
        if current_name:
            genes[current_name] = current_seq
        # Get new gene name
        current_name = line.split()[0][1:]
        current_seq = ""
    else:
        current_seq += line
# Save the last gene
if current_name:
    genes[current_name] = current_seq

# Dictionary to count codon occurrences
codon_count = {}

# Process each gene
for name, seq in genes.items():
    max_orf_length = 0
    best_codons = []
    
    # Check all three reading frames
    for frame in range(3):
        # Split sequence into 3-base codons
        codons = re.findall(r'.{3}', seq[frame:])
        
        # Collect positions of the target stop codon
        stop_pos = []
        for idx, codon in enumerate(codons):
            if codon == stop_codon:
                stop_pos.append(idx)
        
        # If stop codons exist in this frame
        if stop_pos:
            # Take the last stop codon to get the longest ORF in this frame
            last_stop_idx = stop_pos[-1]
            orf_codons = codons[:last_stop_idx]
            orf_length = len(orf_codons)
            
            # Update the longest ORF across three frames
            if orf_length > max_orf_length:
                max_orf_length = orf_length
                best_codons = orf_codons

    # Count codons from the longest ORF
    for codon in best_codons:
        if codon in codon_count:
            codon_count[codon] += 1
        else:
            codon_count[codon] = 1

# Print codon counting results
print(f"\n{stop_codon}")
sorted_codons = sorted(codon_count.items(), key=lambda x: x[1], reverse=True)
for codon, count in sorted_codons:
    print(f"{codon}: {count}")

# Prepare data for pie chart (show all codons)
labels = [codon for codon, _ in sorted_codons]
sizes = [count for _, count in sorted_codons]

# Create pie chart
plt.figure(figsize=(12, 12))
wedges, texts, autotexts = plt.pie(sizes, labels=labels, autopct="%1.1f%%",
                                   startangle=90, textprops={"fontsize": 10})
plt.title(f"Codon Frequency Distribution Upstream of {stop_codon}", fontsize=16, pad=20)

# Beautify percentage text
for autotext in autotexts:
    autotext.set_color("white")
    autotext.set_fontsize(9)

# Save pie chart to file
output_img = f"{stop_codon}_codon_frequency.png"
plt.savefig(output_img, dpi=300, bbox_inches="tight")
plt.close()
print(f"\npie chart saved in: {output_img}")