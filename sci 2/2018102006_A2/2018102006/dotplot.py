def show_plot(seq1,seq2):
    L1 = list(seq1)
    L2 = list(seq2)
    dot_plot = "| |"
    for j in L2:
        dot_plot += j+'|'
    dot_plot += "\n|"
    for j in range(len(L2)):
        dot_plot += '-|'
    dot_plot += '-|\n'
    for i in L1:
        dot_plot += '|'+i+'|'
        for j in L2:
            ele = "x" if (i == j) else " "
            dot_plot += ele+'|'
        dot_plot += '\n'
    return dot_plot