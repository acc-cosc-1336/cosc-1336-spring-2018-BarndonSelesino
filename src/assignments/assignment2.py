def faculty_evaluation_result(nev, rar, som, oft, voft, alw):
    '''
    Write code to calculate faculty evaluation rating according to asssignment instructions
	
    :param nev: Never
    :param rar: Rarely
    :param som: Sometimes
    :param oft: Often
    :param voft: Very Often
    :param alw: Always
    :return: rating as a string
    '''
    totalratio = nev+rar+som+oft+voft+alw:
    nev_ratio = nev/totalratio:
    rar_ratio = rar/totalratio:
    som_ratio = som/totalratio:
    oft_ratio = oft/totalratio:
    voft_ratio = voft/totalratio:
    alw_ratio = alw/totalratio:
	
	if (alw_ratio + voft_ratio) >= 0.9:
		return 'excellent'
	
	elif (oft_ratio+voft_ratio+alw_ratio) >= .80:
		return 'very good'
	
	elif (som_ratio+oft_ratio+voft_ratio+alw_ratio) >= .70:
		return 'good'
	
	elif (rar_ratio+som_ratio+oft_ratio+voft_ratio+alw_ratio) >= .60:
		return 'needs improvement'
	
	else :
		return 'unacceptable':
def get_ratings(nev,rar,som, oft,voft, alw):
    '''
    Students aren't expected to know this material yet!
    '''
    ratings = []
    total = nev + rar + som + oft + voft + alw

    ratings.append(round(alw / total, 2))
    ratings.append(round(voft / total, 2))
    ratings.append(round(oft / total, 2))
    ratings.append(round(som / total, 2))
    ratings.append(round(rar / total, 2))
    ratings.append(round(nev / total, 2))

    return ratings
    

    
