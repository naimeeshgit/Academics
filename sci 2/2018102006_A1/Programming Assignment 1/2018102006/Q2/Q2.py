"""
In this question, we are using the M.AaaS1ORF662P gene which is a methyl transferase gene. We are checking for the restriction enzyme called ApoI.
Recognition site for ApoI is RAATTY. R = A or G  and   Y = C or T
"""

"""
From the results of Mapper.png and Restriction_Map.png for the particular RE and gene sequence, we observe that 
our results match exactly. 
"""

import numpy as np
import matplotlib.pyplot as plt
from RE import RE_sites

pairs = {
    'A': 'T',
    'C': 'G',
    'G': 'C',
    'T': 'A'
}

DNA_seq = ""
f = open("M.AaaS1ORF662P.txt","r")
DNA_seq = f.read().replace('\n','').replace('\r','').replace(' ','')

l = len(DNA_seq)
start1 = 0
end1 = 6
L1 = []
count = 1
cuts = [0]

print("Length of M.AaaS1ORF662P gene = ",l,"bp\n")
while (end1 <= l):
    site1 = DNA_seq[start1:end1:] 
    if (site1[1]=='A' and site1[2]=='A' and site1[3]=='T' and site1[4]=='T' and (site1[0]=='A' or site1[0]=='G') and (site1[5]=='C' or site1[5]=='T')):           
        print("Site No.: ",count,"\tat ",start1+1," - ",end1,"\tRE Site: ",site1,"\tRE Name: ApoI \t cuts after ",start1+1)
        cuts.append(start1+1)
        count += 1
    start1 += 1
    end1 += 1

f = open("Q2_map.txt","w")
for i in range(1,count):
    print("Fragment No.: ",i,"\tof length ",cuts[i]-cuts[i-1],"bp")
    s = "Fragment No.: "+str(i)+"\t"+str(cuts[i-1]+1)+"-"+str(cuts[i])+"\tof length "+str(cuts[i]-cuts[i-1])+"bp\n"
    f.write(s)
    cuts[i-1] = cuts[i] - cuts[i-1]
print("Fragment No.: ",count,"\tof length ",l-cuts[-1],"bp")
s = "Fragment No.: "+str(count)+"\t"+str(cuts[-1]+1)+"-"+str(l)+"\tof length "+str(l-cuts[-1])+"bp\n"
f.write(s)
cuts[-1] = l-cuts[-1]

f.close()

plt.figure(figsize=(3,10))
colors = ['#eb3434','orange','#b5561f','#96790f','#0f593f','brown','#750970']
for i in range(len(cuts)):
    x = np.linspace(0,5)
    y = cuts[i] * np.ones(len(x))
    plt.plot(x,y,color=colors[i],linewidth=2,linestyle=':')
    plt.text(3-((~i) & 1),cuts[i]+2,'ApoI ('+str(cuts[i])+')',fontsize=12)
plt.xlabel('')
plt.ylabel('Fragment length (bp)')
plt.title('Restriction Map for ApoI in M.AaaS1ORF662P gene')
plt.show()