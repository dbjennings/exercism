codon_ref = {"AUG":"Methionine",
             "UUU":"Phenylalanine",
             "UUC":"Phenylalanine",
             "UUA":"Leucine",
             "UUG":"Leucine",
             "UCU":"Serine",
             "UCC":"Serine",
             "UCA":"Serine",
             "UCG":"Serine",
             "UAU":"Tyrosine",
             "UAC":"Tyrosine",
             "UGU":"Cysteine",
             "UGC":"Cysteine",
             "UGG":"Tryptophan",
             "UAA":"STOP",
             "UAG":"STOP",
             "UGA":"STOP"}

def proteins(strand: str) -> list:
    
    codons = [strand[i:i+3] for i in range(0,len(strand),3)]
    peptides = []
    
    for codon in codons:
        if codon_ref[codon]=="STOP": break
        peptides.append(codon_ref[codon])

    return peptides