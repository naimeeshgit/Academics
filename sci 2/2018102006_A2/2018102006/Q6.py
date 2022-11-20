from dotplot import show_plot

pairs = {
    'A':'U',
    'U':'A',
    'C':'G',
    'G':'C'
}

def comp_seq(seq1):
    comp = ''
    for i in range(len(seq1)):
        comp += pairs[seq1[i]]
    seq2 = comp[::-1]
    return seq2

seq1 = "AUGUGGCAUGCCAGG"
seq2 = comp_seq(seq1)
print(show_plot(seq2,seq1))