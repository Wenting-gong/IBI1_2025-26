import re
import matplotlib.pyplot as plt

#input and check the validity of the stop codon
while True:
    stop_codon=input('Please input a stop codon (TAA, TAG, TGA): ').upper()
    if stop_codon in ['TAA', 'TAG', 'TGA']:
        break
    print("Invalid stop codon! Please enter TAA, TAG, or TGA.")

# read file
input_fa="Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
try:
    with open(input_fa, 'r') as f:
        lines=f.readlines()
except FileNotFoundError:
    print(f"Error: File {input_fa} not found!")
    exit(1)

#store genes
genes={}
current_name=""
current_seq=""

for line in lines:
    line=line.strip()
    if not line:
        continue
    if line.startswith(">"):
        # save the last gene
        if current_name:
            genes[current_name]=current_seq
        #save gene name
        current_name=line.split()[0][1:]
        current_seq=""
    else:
        current_seq+=line
# save the last gene
if current_name:
    genes[current_name]=current_seq

codon_count={}

for name, seq in genes.items():
    max_orf_length=0
    best_codons=[]
    for frame in range(3):
        codons=re.findall(r'.{3}', seq[frame:])
        # find the first stop codon
        for i in range(len(codons)):
            codon=codons[i]
            if codon==stop_codon:
                # all upstream in-frame codons
                orf_codons=codons[:i]
                orf_length=len(orf_codons)
                # fetch the longest orf
                if orf_length>max_orf_length:
                    max_orf_length=orf_length
                    best_codons=orf_codons
                break

    # count the loghest orf
    for codon in best_codons:
        if codon in codon_count:
            codon_count[codon]+=1
        else:
            codon_count[codon]=1

# print outcomes
print(f"\n{stop_codon}")
sorted_codons = sorted(codon_count.items(), key=lambda x: x[1], reverse=True)
for codon, count in sorted_codons:
    print(f"{codon}: {count}")

# draw pie chart
top_codons = sorted_codons[:top_n]
other_count = sum(c for _, c in sorted_codons[top_n:]) if len(sorted_codons)>top_n else 0
labels = [codon for codon, _ in top_codons]
sizes = [count for _, count in top_codons]
plt.figure(figsize=(12, 8))
wedges, texts, autotexts=plt.pie(sizes,labels=labels,autopct="%1.1f%%",startangle=90,textprops={"fontsize": 10})
plt.title(f"Codon Frequency Distribution Upstream of {stop_codon}", fontsize=16, pad=20)

#beautify lables
for autotext in autotexts:
    autotext.set_color("white")
    autotext.set_fontsize(9)

# save image to file
output_img=f"{stop_codon}_codon_frequency.png"
plt.savefig(output_img, dpi=300, bbox_inches="tight")
plt.close()
print(f"\npie chart saved in: {output_img}")