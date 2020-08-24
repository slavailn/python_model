# Validating sequences 

# FUNCTION 1
# Function that validates DNA sequence
# Allowed symbols: A, G, C, T, N """
def validate_base_sequence(base_sequence):
    """ validate base sequence based on counts of allowed symbols
    A, C, T, G, or N. The function return TRUE if
    the sum of symbol counts is equal to the length of base sequence. 
    Otherwise the function returns FALSE"""
    seq = base_sequence.upper()
    return len(seq) == (seq.count('T') + seq.count('C') + 
	seq.count('G') + seq.count('A') + seq.count('N'))
 
# Run example: validate_base_sequence("ACTGGGTCGGG")
validation = validate_base_sequence("ACTGGGTCGGG")
print("DNA sequence validation: ")
print(validation)

# ------------------------------------------------------------------------- #
# FUNCTION 2 
# Calculate GC content of DNA sequence
def gc_content(base_sequence):
	"""Calculate the ratio of GC nucleotides to all nuceleotides in the
    DNA sequence """
	seq = base_sequence.upper()
	return( (seq.count('C') + seq.count('G'))/len(seq) )

# Run example: gc_content("ACCTAAGGTTCC")
content = gc_content("ACCTAAGGTTCC")
print("GC content: ")
print(content)

# ------------------------------------------------------------------------- #
# FUNCTION 3
# Calculate GC content, but validate the base sequence first using assertion
def gc_content_val(base_sequence):
    """ Calculate GC ratio while validating the sequence """
    seq = base_sequence.upper()
    assert validate_base_sequence(seq), 'The sequence does not appear to be DNA'
    return(gc_content(seq))
# Test this function
content_val = gc_content_val('ACGTTCGCGTTTAAAA')
print("Validated content is: ", content_val)
# content_val = gc_content_val('ACGTTCGCGTTTAAAAR')
# print("Validated content is: ", content_val)

# ------------------------------------------------------------------------- #
# FUNCTION 4
# Validate base sequence which can be either DNA or RNA (just allowing U)
print('##################################################################')
def validate_dna_rna(base_sequence, RNAflag=False):
    """ validate DNA or RNA based on counts of allowed symbols
    A, C, T/U, G, N. The function return TRUE if
    the sum of symbol counts is equal to the length of base sequence. 
    Otherwise the function returns FALSE"""
    seq = base_sequence.upper()
    return len(seq) == (seq.count('U' if RNAflag else 'T') + seq.count('C') + 
	seq.count('G') + seq.count('A') + seq.count('N'))
 
# Run example: validate_base_sequence("ACTGGGTCGGG")
validation_dna_rna = validate_dna_rna("ACTGGGTCGGG", RNAflag = True)
print("DNA/RNA sequence validation: ", validation_dna_rna)
validation_dna_rna = validate_dna_rna("ACUGGGUCGGG", RNAflag = True)
print("DNA/RNA sequence validation: ", validation_dna_rna)
validation_dna_rna = validate_dna_rna("ACTGGGUCGGG", RNAflag = True)
print("DNA/RNA sequence validation: ", validation_dna_rna)







