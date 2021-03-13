'''
this file calculate length of posts
'''
def creating_text_file():
    lc = open('Length_count.csv','w')

    lc.write('Filename   AWPPost   AWPPerson')
    lc.write('\n')
    lc.close()

    
def main():
    creating_text_file()
    list_file = ('ENFJ.txt',
                 'ENFP.txt',
                 'ENTJ.txt',
                 'ENTP.txt',
                 'ESFJ.txt',
                 'ESFP.txt',
                 'ESTJ.txt',
                 'ESTP.txt',
                 'INFJ.txt',
                 'INFP.txt',
                 'INTJ.txt',
                 'INTP.txt',
                 'ISFJ.txt',
                 'ISFP.txt',
                 'ISTJ.txt',
                 'ISTP.txt')
    for i in list_file:
        calculateLength(i)

def calculateLength(file_name):
    '''
        This fuction will go in each file and extract the average length of each post
        and also the average length of posts each person has posted

    '''

    fname=file_name
    print('process')
    f = open(fname,'r')
    line_count=0
    total_char=0
    total_words=0
    for line in f:
        for i in range(0,len(line)):
            if line[i]==' ':
                total_words+=1
        total_char+=len(line)
        if(line != '\n'):
            line_count+=1
            
    total_people=int(line_count/50)

    average_words_per_post = total_words/line_count
    average_words_per_person = total_words/total_people
    print(average_words_per_post)
    print(average_words_per_person)
    lengthCountFile = open('Length_count.csv','a')
    lengthCountFile.write(fname+'    ')
    lengthCountFile.write(str("{:.2f}".format(average_words_per_post))+'     ')
    lengthCountFile.write(str("{:.2f}".format(average_words_per_person))+'\n')
    lengthCountFile.close()
    
    f.close()
    
    
    

    print('done')
    



    
