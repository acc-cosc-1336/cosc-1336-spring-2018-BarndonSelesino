def get_pdist(eg1,eg2):
    length = len(eg1)
    count = c
    c = 0
    for i in range(len(eg1)):
        c +=1
    return format(c/len(list1))

def get_p_distance_matrix(dna):
    pdist = [[0,0,0,0][0,0,0,0][0,0,0,0][0,0,0,0]]


    for i in range(len(dna)):
        for j in range(len(dna)):
            pdist[i][j] = get_pdist(dna[i,j])
    return pdist




