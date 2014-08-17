def intro():
    ''' This function prints the intro to the program'''
    print 'This program reports information about DNA'
    print 'nucleotide sequences that may encode proteins.'

def codon(line,out):
    ''' This function creates a list of the codons and writes it in the output file. '''
    nucleotides = line.replace("-","").upper().replace("\n","")
    codonlist = [nucleotides[x*3:(x*3+3)] for x in range(0,len(line)/3)]
    out.write('Codons List: ' + str(codonlist)+'\n')
    return codonlist

def files():
    ''' This function receives the input to obtain the input and output files and also calls the functions to write the information in the output file. '''
    count = 0
    input_file=raw_input('Input file name? ')
    output_file=raw_input('Output file name? ')
    f=open(input_file, 'r')
    out = open(output_file, 'w')
    for line in f:
        count += 1
        if count%2==1:
            out.write('Region name: ' + line)
        if count%2==0:
            out.write('Nucleotides: ',)
            line = line.upper().strip().strip("-")
            out.write(line)
            c_and_g=count_mass(line,out)
            codonlist=codon(line, out)
            is_protein(line,out,c_and_g,codonlist)

def count_mass(line,out):
    ''' This function counts the number of each base and determines the total mass of each sequence each nucleotide constitutes.
    This also writes the data in the output file. '''
    adenine=line.count('A')
    guanine=line.count('G')
    cytosine=line.count('C')
    thymine=line.count('T')
    junk=line.count('-')
    code=str([adenine,cytosine,guanine,thymine])
    out.write('\nNuc. Counts: '+code +'\n')
    total = adenine*135.128+cytosine*111.103+guanine*151.128+thymine*125.107+junk*100.000
    perc_a= adenine*135.128/total*100
    perc_c= cytosine*111.103/total*100
    perc_g= guanine*151.128/total*100
    perc_t= thymine*125.107/total*100
    out.write('Total Mass%: [{:.3}, {:.3}, {:.3}, {:.3}] of {:.5}\n'.format(perc_a,perc_c,perc_g,perc_t,round(total,1)))
    x=perc_c+perc_g
    return x

def is_protein(line, out, c_and_g,codonlist):
    ''' This function determines if the sequence creates a protein and displays the answer in the output file. '''
    if line[0:3]=='ATG' and len(line)>=15 and c_and_g>=30:
        if codonlist[len(codonlist)-1]=='TAA' or codonlist[len(codonlist)-1]=='TAG' or codonlist[len(codonlist)-1]=='TGA': 
            out.write('Is Protein?: YES\n\n')
        else:
            out.write('Is Protein?: NO\n\n')
    else:
        out.write('Is Protein?: NO\n\n')


intro()
files()
