from RE import RE_sites

pairs = {
    'a': 't',
    'c': 'g',
    'g': 'c',
    't': 'a'
}

# DNA_seq = ""
# f = open("pbr322.txt","r")
# DNA_seq = f.read().replace('\n','').replace('\r','')
DNA_seq = "GAGAGAGAGAGAGA"
DNA_seq = DNA_seq.lower()

l = len(DNA_seq)                    # Sequences of lengths 4,6,8
start1 = 0
start2 = 0
start3 = 0
end1 = 4
end2 = 6
end3 = 8
L1 = []
L2 = []
L3 = []
count = 0

# Accounting for circular gene sequence for all the 3 different lengths. 
# Checking for various gene sequences. Some like ApoI, BmtI, NheI are very specific in their restriction sites, so 
# we need to have special if conditions for them

print("Length of pBR322 sequence = ",l,"bp\n")
print("UNIQUE SEQUENCES WITH LENGTH 4:\n")
while (end1-l < 4):                             
    if (end1 <= l):
        site1 = DNA_seq[start1:end1:] 
        if (site1[3]==pairs[site1[0]] and site1[2]==pairs[site1[1]]):
            if (site1 not in L1):
                count += 1
                L1.append(site1)
                print("Site No.: ",count,"\tat ",start1+1," - ",end1,"\tRE Site: ",site1)
    else:
        site1 = DNA_seq[start1:l:]+DNA_seq[0:end1-l:]
        if (site1[3]==pairs[site1[0]] and site1[2]==pairs[site1[1]]):
            if (site1 not in L1):
                count += 1
                L1.append(site1)
                print("Site No.: ",count,"\tat ",start1+1," - ",end1-l,"\tRE Site: ",site1)

    start1 += 1
    end1 += 1

count = 0

print("UNIQUE SEQUENCES WITH LENGTH 6:\n")
while (end2-l < 6):
    if (end2 <= l):
        site2 = DNA_seq[start2:end2:] 
        if (site2[5]==pairs[site2[0]] and site2[4]==pairs[site2[1]] and site2[3]==pairs[site2[2]]):
            if (site2 not in L2):
                count += 1
                L2.append(site2)
                if (site2 in RE_sites):
                    if (site2 == "gctagc"):             # BmtI and NheI have the same restriction recognition sites, although they cut at different points
                        print("Site No.: ",count,"\tat ",start2+1," - ",end2,"\tRE Site: ",site2,"\tRE Name: BmtI , NheI")
                    else:     # Trying to label the restriction sites as per our knowledge of REs
                        print("Site No.: ",count,"\tat ",start2+1," - ",end2,"\tRE Site: ",site2,"\tRE Name: ",RE_sites[site2])
                else:                  
                    print("Site No.: ",count,"\tat ",start2+1," - ",end2,"\tRE Site: ",site2)
        if (site2[1]=='a' and site2[2]=='a' and site2[3]=='t' and site2[4]=='t' and (site2[0]=='a' or site2[0]=='g') and (site2[5]=='c' or site2[5]=='t')):           # recognition site for ApoI is RAATTY. R = A or G  and   Y = C or T
            print("Site No.: ",count,"\tat ",start2+1," - ",end2,"\tRE Site: ",site2,"\tRE Name: ApoI")
    else:
        site2 = DNA_seq[start2:l:]+DNA_seq[0:end2-l:]
        if (site2[5]==pairs[site2[0]] and site2[4]==pairs[site2[1]] and site2[3]==pairs[site2[2]]):
            if (site2 not in L2):
                count += 1
                L2.append(site2)
                if (site2 in RE_sites):
                    if (site2 == "gctagc"):             # BmtI and NheI have the same restriction recognition sites, although they cut at different points
                        print("Site No.: ",count,"\tat ",start2+1," - ",end2,"\tRE Site: ",site2,"\tRE Name: BmtI , NheI")
                    else:     # Trying to label the restriction sites as per our knowledge of REs
                        print("Site No.: ",count,"\tat ",start2+1," - ",end2-l,"\tRE Site: ",site2,"\tRE Name: ",RE_sites[site2])
                else:
                    print("Site No.: ",count,"\tat ",start2+1," - ",end2-l,"\tRE Site: ",site2)
        if (site2[1]=='a' and site2[2]=='a' and site2[3]=='t' and site2[4]=='t' and (site2[0]=='a' or site2[0]=='g') and (site2[5]=='c' or site2[5]=='t')):           # recognition site for ApoI is RAATTY. R = A or G  and  Y = C or T
            print("Site No.: ",count,"\tat ",start2+1," - ",end2-l,"\tRE Site: ",site2,"\tRE Name: ApoI")

    start2 += 1
    end2 += 1

count = 0

print("\nUNIQUE SEQUENCES WITH LENGTH 8:\n")
while (end3-l < 6):
    if (end3 <= l):
        site3 = DNA_seq[start3:end3:]
        if (site3[7]==pairs[site3[0]] and site3[6]==pairs[site3[1]] and site3[5]==pairs[site3[2]] and site3[4] == pairs[site3[3]]):
            if (site3 not in L3):
                count += 1
                L3.append(site3)
                print("Site No.: ",count,"\tat ",start3+1," - ",end3,"\tRE Site: ",site3)
        if (site3[0]=='c' and site3[7]=='g' and site3[2]=='c' and site3[5]=='g' and site3[3]=='c' and site3[4]=='g' and (site3[1]=='a' or site3[1]=='g') and (site3[6]=='c' or site3[6]=='t')):       # recognition site for SgrAI is CRCCGGYG
            print("Site No.: ",count,"\tat ",start3+1," - ",end3,"\tRE Site: ",site3,"\tRE Name: SgrAI")                             # R = A or G  and   Y = C or T
    else:
        site3 = DNA_seq[start3:l:]+DNA_seq[0:end3-l:]
        if (site3[7]==pairs[site3[0]] and site3[6]==pairs[site3[1]] and site3[5]==pairs[site3[2]] and site3[4] == pairs[site3[3]]):
            if (site3 not in L3):
                count += 1
                L3.append(site3)
                print("Site No.: ",count,"\tat ",start3+1," - ",end3-l,"\tRE Site: ",site3)
        if (site3[0]=='c' and site3[7]=='g' and site3[2]=='c' and site3[5]=='g' and site3[3]=='c' and site3[4]=='g' and (site3[1]=='a' or site3[1]=='g') and (site3[6]=='c' or site3[6]=='t')):       # recognition site for SgrAI is CRCCGGYG
            print("Site No.: ",count,"\tat ",start3+1," - ",end3-l,"\tRE Site: ",site3,"\tRE Name: SgrAI")                             # R = A or G  and   Y = C or T

    start3 += 1
    end3 += 1
