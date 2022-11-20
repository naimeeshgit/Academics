from genetic_code_table import genetic_code, pairs
pairs2 = {
    'A': 't',
    'C': 'g',
    'G': 'c',
    'T': 'a'
}

DNA_seq = ""
RNA_synth = ""
protein_synth = ""

# f = open("testq1.txt","r")                                             # Displaying the DNA sequence
# DNA_seq = f.read().replace('\n','').replace('\r','')
# print("DNA SEQUENCE READ:\t", DNA_seq,"\n")
# DNA_seq = "GTTTCATTATACCAGTTTAGATCTATCGACAGGGCGTTGAGTGTGTGCTTACTCACGGCTGGCATGTAGGTAACAGTAGTGGGGAAGCGTAACATCTGAGGCCTGACTCACATATAGAGTGTCGACCAAGGGGTGAAGCATCATACGCCATACAGGCCCCTAGCGAAACGCCTAGTCTAAAGACACACGAGAATGAAACCCGTGGACTTGGTTACAGCGTAATAATCTGGTCAGAGCTGGTCCGGCGCTGGCGATGTACCTTACGCCACTGCAAACCGGCTTTGCAGAGAACATCTGGGTACATTCCCGTGTCATGTCAAAGCAGGTGATTCCCGCGAAAAACAATTAACGACGCATTTGCTATTGACGAAGTCCTAGTTCTCCGAATTGAGCGGGAGACATATGATGTCGAGACTGCAGGAACCGAATTATCCTGTCCGCAGATCCAATAGCTCACAGAGGTAAGGGGAGTGTGATGGTGCCCTAGGGTGTTTGAACG"
DNA_seq = "ATGATGGGGGCCCGACGTACGACGTAA"

for i in DNA_seq:                                                   # Converting from DNA to RNA sequence using the base pairs imported from genetic_code_table
    RNA_synth += pairs[pairs2[i]]
print("RNA SEQUENCE:\t", RNA_synth,"\n")

print("PROTEIN SYNTHESIZED: ")                                      
start_no = 0
end = 0
i = 0
while i < len(RNA_synth):
    if (RNA_synth[i:i+3:] == "aug"):                                # Checking for start codon
        start_no += 1
        protein = ""
        end = i
        for j in range(i,len(RNA_synth),3):                         # Converting codon into amino acids
            codon = RNA_synth[j:j+3:]
            if (len(codon) == 3):                                   # For "end of sequence" case
                if (genetic_code[codon] == "Stop"):                 # If stop codon is encountered then we stop and then store it
                    end = j
                    break
                protein += genetic_code[codon]+' '
            else:
                break
        if (end == j):
            print("Protein No: ",start_no,"\tRNA sequence number: ",i+1,":",end," Protein: ",protein,"RNA SEQUENCE: ",RNA_synth[i:end])   # Displaying the protein synthesis
            protein_synth += protein + "\n"                             # with the corresponding RNA sequence and also mentioning start , end positions
            i = end
    i += 1

open("RNA_synth.txt","w").write(RNA_synth)                              # Storing the RNA sequences in a file
open("protein_synth.txt","w").write(protein_synth)                      # Storing the Protein sequences in a file
