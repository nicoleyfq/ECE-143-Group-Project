def clean_data(data):
    '''
        This function will help clean data before writing them to 16 files
        This code will take in data, eliminate '|||' and replace them with'\n'
        :para data: store the information of each line in the data set file.
        :type data: string
    '''
    cleaned_data = data.replace('|||','\n')
    return cleaned_data


def creating_text_file():
    '''
        Creating 16 different types that represent for each personality
    '''
    INFJ = open('INFJ.txt','w')
    INFP = open('INFP.txt','w')
    INTJ = open('INTJ.txt','w')
    INTP = open('INTP.txt','w')
    ISFJ = open('ISFJ.txt','w')
    ISFP = open('ISFP.txt','w')
    ISTJ = open('ISTJ.txt','w')
    ISTP = open('ISTP.txt','w')
    ENFJ = open('ENFJ.txt','w')
    ENFP = open('ENFP.txt','w')
    ENTJ = open('ENTJ.txt','w')
    ENTP = open('ENTP.txt','w')
    ESFJ = open('ESFJ.txt','w')
    ESFP = open('ESFP.txt','w')
    ESTJ = open('ESTJ.txt','w')
    ESTP = open('ESTP.txt','w')


    INFJ.close()
    INFP.close()
    INTJ.close()
    INTP.close()
    ISFJ.close()
    ISFP.close()
    ISTJ.close()
    ISTP.close()
    ENFJ.close()
    ENFP.close()
    ENTJ.close()
    ENTP.close()
    ESFJ.close()
    ESFP.close()
    ESTJ.close()
    ESTP.close()

def data_processing():

    '''
        Author: Blue Luu

        READ ME:
        This code will help extract the first 6000 data lines from the main file
        The data will be send to 16 differents files depends on the code in front of it
        The data will also be processed and clean for future use

        :para data: store the information of each line in the data set file.
        :type data: string

        Note that each of the 16 files will have the following template:

        #line_number_in main_file: post1
        post2
        post3
        ...
        post50
        (2 empty lines)
        #line_number_in_main_file:post1
        post2
        post3
        ...
        post50
        (2 empty lines)
    '''

    f = open('mbti_1.csv','r')                  #open main file to read
    address = 0                                 #an address that track the line number from main file
    creating_text_file()                        #calling function to create 16 files
    print(f.readline())                         #read the first line in main file ( should read name of column :'type' and 'post' in main file)
    print('processing')
    for i in range(0,5998):                     #taking data from line 2 to line 6000 in main file
        address=i+2                             #updating address
        data=f.readline()                       #read and store information in data
        data=clean_data(data)                   #clean all the information (eliminating '|||' and add newline)
        mini_file = open(data[0:4]+'.txt','a')  #open the file that represent that personallity based on the type in main file
        mini_file.write(str(address)+': ')      #write the address of
        mini_file.write(data[6:-1])             #write all the information stored in data variable to the corresponding file
        mini_file.write('\n\n\n')               #create 2 newlines to seperate each data

        mini_file.close()                       
        

    print('done')
    f.close()
