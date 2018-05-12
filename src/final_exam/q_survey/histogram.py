def display_histogram():
    infile = open('survey.dat', 'r')
    survey = infile.readlines()
    infile.close()



    index = 0
    while index < len(survey):
        survey[index] = survey[index].rstrip('\n')
        survey_w_sym = ['************************************' + survey for survey in survey]
        survey_w_sym
        index +=1



    
    print(surveya)
