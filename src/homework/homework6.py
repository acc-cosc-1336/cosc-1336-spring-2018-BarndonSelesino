
#var1 = amount/number/count
#get mutations
def get_point_mutations(dna_string_1, dna_string_2):
    val1 = 0
    for i in range(0, len(dna_string_1)):
        if dna_string_1[i] != dna_string_2[i]:
            val1 = val1 + 1
    return val1

#complement
def get_dna_complement(dna_string):
    val1 = 0
    string = ''
    for i in dna_string[::-1]:        
        if i == 'A':
            i = 'T'
        elif i == 'T':
            i = 'A'
        elif i == 'C':
            i = 'G'
        elif i == 'G':
            i = 'C'
        string += i
    return string    

#transcribe
def transcribe_dna_into_rna(dna_string):
    string = ''
    while len(dna_string)<0 and len(dna_string)>1000:
        print('Invalid length of the DNA string')
    else:
        for i in dna_string:
            if i == 'T':
                i = 'U'
            string += i
    return string               
#get content
def get_gc_content(dna_string):
    var1 = 0
    a = 0
    for i in range(0, len(dna_string)):
        if dna_string[i] == 'C' or dna_string[i] == 'G':
            var1 += 1
    a = var1*100/int(len(dna_string))
    return float(format(a, ".6f"))         
'''
DO NOT USE LISTS
THIS IS OPTIONAL
Create a function get_most_likely_ancestor_conensus with two string parameters dna_string1 and dna_string2 that
returns the beginning position of occurences of dna_string2 in dna_string1.
Problem
Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s 
(as a result, t must be no longer than s).
The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., the 
positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position 
i of s is denoted by s[i].
A substring of s can be represented as s[j:k], where j and k represent the starting and ending positions of the 
substring in s; for example, if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".
The location of a substring s[j:k] is its beginning position j; note that t will have multiple locations in s if it 
occurs more than once as a substring of s (see the Sample below).
See link for more information http://rosalind.info/problems/subs/.
Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.
Sample Dataset (Function parameters)
parameter dna_string1: GATATATGCATATACTT
parameter dna_string2: ATAT
Sample Output(function return value)
2 4 10
'''

'''
DO NOT USE LISTS
THIS IS OPTIONAL
Create a function get_consenus_from_dna with 7 dna string parameters that returns 5 values consenus, profilea, profilec,
profilet, profilet
Problem
A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns. Given 
a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.
Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in 
which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents 
the number of times that C occurs in the jth position, and so on (see below).
A consensus string c is a string of length n formed from our collection by taking the most common symbol at each 
position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the 
profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus 
strings.
DNA Strings	
A T C C A G C T
G G G C A A C T
A T G G A T C T
A A G C A A C C
T T G G A A C T
A T G C C A T T
A T G G C A C T
Profile A   5 1 0 0 5 5 0 0
Profile	C   0 0 1 4 2 0 6 1
Profile G   1 1 6 3 0 1 0 0
Profile T   1 5 0 0 0 1 1 6
Consensus
A T G C A A C T
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then 
you may return any one of them.)
Sample Dataset(function parameters)
dna_string1: ATCCAGCT
dna_string2: GGGCAACT
dna_string3: ATGGATCT
dna_string4: AAGCAACC
dna_string5: TTGGAACT
dna_string6: ATGCCATT
dna_string7: ATGGCACT
dna_string8: ATGCAACT
Sample Output:
return value 1 Consensus: A T G C A A C T 
return value 2 A: 5 1 0 0 5 5 0 0
return value 3 C: 0 0 1 4 2 0 6 1
return value 4 G: 1 1 6 3 0 1 0 0
return value 5 T: 1 5 0 0 0 1 1 6
'''
