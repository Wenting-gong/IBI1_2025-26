def mass(sequence):
    dic={'G':57.02,'A':71.04,'S':87.03,'P':97.05,'V':99.07,'T':101.05,'C':103.01,'I':113.08,'N':114.04,'D':115.03,'Q':128.06,'K':128.09,'E':129.04,'M':131.04,'H':137.06,'F':147.07,'R':156.10,'Y':163.06,'W':186.08}
    total_mass=0
    for i in range(len(sequence)):
        amino_acid=sequence[i-1]
        if amino_acid in dic:
            amino_mass=dic[amino_acid]
            total_mass+=amino_mass
        else:
            raise ValueError(f'Error:',amino_acid,'has no recorded mass!')
    return total_mass
sequence=input('Please input a amino acid sequence using the symbol:')
total_mass=mass(sequence)
print('The mass of total protein in amu is',total_mass)