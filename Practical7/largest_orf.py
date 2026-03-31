import re
seq='AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
ORF=re.findall(r'AUG(?:.{3}).+?(?:UAA|UAG|UGA)',seq)
longest_orf=max(ORF,key=len)
print(longest_orf)
n=len(longest_orf)
print(n)