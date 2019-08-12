"""
    Some input parameters like the file name and the user names in the 
    exported WhatsApp chat. 
    
    For now, the following functionality is present,
    
    If the WhatsApp chat file is exported, then the file contents would be read.
    
    With the help of the regex, the process will look for the lines containing 
    the names of the given users. If it isn't found then that line is printed 
    along with the lone number. This can be taken as some future task to see
    how to analyse these types of chats.
    
    If the regex matches then we increment the count of the number of lines 
    written by the given user. This is simple.
    
    What would be interesting is to form a dictionary of the words used 
    by each of the user and then generate a report on their usage. Though the 
    initial analysis sounds dry but then one can rope in sentiment analysis 
    and who knows, skys the limit.
    
    Me being an enthusiast, I haven't looked up into much of the theory. So, 
    if anyone has a better idea on how it is to be done or to improve the 
    working of the code. Crticism will help both my understanding as well as
    the efficiency of the code.
"""

import re

FILE_NAME = "WhatsApp Chat with sample user.txt"
FIRST_USER = "sample_user_1"
SECOND_USER = "sample_user_2"


REGEX_USER_1 = r".+"+r"\b"+FIRST_USER+r"\b.+"
REGEX_USER_2 = r".+"+r"\b"+SECOND_USER+r"\b.+"

print(REGEX_USER_1)

SOURCE_FILE_PATTERN = re.compile(r'[a-z,_,A-Z,0-9,\s]+.txt$')

FIRST_USER_REGEX = re.compile(REGEX_USER_1)
SECOND_USER_REGEX = re.compile(REGEX_USER_2)

REGEX_MATCH_RESULT = SOURCE_FILE_PATTERN.match(FILE_NAME)

FIRST_USER_TOTAL_LINE_COUNT = 0
SECOND_USER_TOTAL_LINE_COUNT = 0
TOTAL_LINE_COUNT = 0


if __name__ == "__main__":
    if REGEX_MATCH_RESULT == None:
        print("Invalid File")
    
    else:
        FILE = open(FILE_NAME, 'r')

        for line in FILE:
            TOTAL_LINE_COUNT = TOTAL_LINE_COUNT+1
            FIRST_USER_MATCH_RESULT = FIRST_USER_REGEX.match(line)
            if FIRST_USER_MATCH_RESULT != None:
                FIRST_USER_TOTAL_LINE_COUNT = FIRST_USER_TOTAL_LINE_COUNT+1
            else:
                SECOND_USER_MATCH_RESULT = SECOND_USER_REGEX.match(line)
                if SECOND_USER_MATCH_RESULT != None:
                    SECOND_USER_TOTAL_LINE_COUNT = SECOND_USER_TOTAL_LINE_COUNT+1
                else:
                    print(line)
    FILE.close()

print(FIRST_USER, "line count : ",(FIRST_USER_TOTAL_LINE_COUNT))
print(SECOND_USER, "line count : ",(SECOND_USER_TOTAL_LINE_COUNT))
print("Total line count : ",TOTAL_LINE_COUNT)

    
    