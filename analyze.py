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
    
  In this development version, what we have done is we have added the feature
  to extract the words from the chat for each user and then create a .csv file
  containing the result. The CSV file will contain the word:word_count in it.
    
"""

import re

FILE_NAME = "WhatsApp Chat with sample user.txt"
FIRST_USER = "sample_user_1"
SECOND_USER = "sample_user_2"


"""
    Regex to match the lines having the message from user 1 and user 2
"""
REGEX_USER_1 = r".+"+r"\b"+FIRST_USER+r"\b.+"
REGEX_USER_2 = r".+"+r"\b"+SECOND_USER+r"\b.+"

SOURCE_FILE_PATTERN = re.compile(r'[a-z,_,A-Z,0-9,\s]+.txt$')

FIRST_USER_REGEX = re.compile(REGEX_USER_1)
SECOND_USER_REGEX = re.compile(REGEX_USER_2)

REGEX_MATCH_RESULT = SOURCE_FILE_PATTERN.match(FILE_NAME)

FIRST_USER_TOTAL_LINE_COUNT = 0
SECOND_USER_TOTAL_LINE_COUNT = 0
TOTAL_LINE_COUNT = 0

FIRST_USER_WORD = []
SECOND_USER_WORD = []

FIRST_USER_WORD_DICTIONARY = {}
SECOND_USER_WORD_DICTIONARY = {}

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
                FIRST_USER_WORD.append(line.strip().split(' ')[4:])
            else:
                SECOND_USER_MATCH_RESULT = SECOND_USER_REGEX.match(line)
                if SECOND_USER_MATCH_RESULT != None:
                    SECOND_USER_TOTAL_LINE_COUNT = SECOND_USER_TOTAL_LINE_COUNT+1
                    SECOND_USER_WORD.append(line.strip().split(' ')[5:])
                else:
                    print(line)
    FILE.close()

print(FIRST_USER, "line count : ",(FIRST_USER_TOTAL_LINE_COUNT))
print(SECOND_USER, "line count : ",(SECOND_USER_TOTAL_LINE_COUNT))
print("Total line count : ",TOTAL_LINE_COUNT)

"""
    The word analysis for the user. First task is to separate out the sentences into 
    individual words and to find the number of times each word occur in the complete chat
    by the given user.
"""
# FIRST USER.
for listing in FIRST_USER_WORD:
    for words in listing:
        FLAG_PRESENT_IN_DICT = 0
        for key in FIRST_USER_WORD_DICTIONARY.keys():
            if words.lower() == key:
                FIRST_USER_WORD_DICTIONARY[key] = FIRST_USER_WORD_DICTIONARY[key]+1
                FLAG_PRESENT_IN_DICT = 1
                break;
        if FLAG_PRESENT_IN_DICT == 0:
            FIRST_USER_WORD_DICTIONARY[words.lower()] = 1

# SECOND USER.
for listing in SECOND_USER_WORD:
    for words in listing:
        
        FLAG_PRESENT_IN_DICT = 0
        for key in SECOND_USER_WORD_DICTIONARY.keys():
            if words.lower() == key:
                SECOND_USER_WORD_DICTIONARY[key] = SECOND_USER_WORD_DICTIONARY[key]+1
                FLAG_PRESENT_IN_DICT = 1
                break
        if FLAG_PRESENT_IN_DICT == 0:
            SECOND_USER_WORD_DICTIONARY[words.lower()] = 1


max_val = 0
max_val_word = []
index_count = 0

"""
    To find the word with the maximum number of occurences.
"""
# FIRST USER.
for key in FIRST_USER_WORD_DICTIONARY.keys():
    if index_count == 0:
        max_val = FIRST_USER_WORD_DICTIONARY[key]
        max_val_word.append(key)
        index_count = 1
    else:
        if max_val < FIRST_USER_WORD_DICTIONARY[key]:
            max_val = FIRST_USER_WORD_DICTIONARY[key]
            max_val_word = []
            max_val_word.append(key)
        elif max_val == FIRST_USER_WORD_DICTIONARY[key]:
            max_val_word.append(key)

print(FIRST_USER, ": Maximum used word : ", max_val_word, "With number of occurences :", max_val)


max_val = 0
max_val_word = []
index_count = 0

# SECOND USER.
for key in SECOND_USER_WORD_DICTIONARY.keys():
    if index_count == 0:
        max_val = SECOND_USER_WORD_DICTIONARY[key]
        max_val_word.append(key)
        index_count = 1
    else:
        if max_val < SECOND_USER_WORD_DICTIONARY[key]:
            max_val = SECOND_USER_WORD_DICTIONARY[key]
            max_val_word = []
            max_val_word.append(key)
        elif max_val == SECOND_USER_WORD_DICTIONARY[key]:
            max_val_word.append(key)

print(SECOND_USER, ": Maximum used word : ", max_val_word, "With number of occurences :", max_val)



"""
    The key value pairs... i.e. the WORD:<WORD_COUNT>
    This would be inserted into a .csv file if anyone wants to do some 
    analysis using some other tool. This is for the first user.
"""
with open(FIRST_USER+".csv", "w") as CSVFile:
    CSVWriter = csv.writer(CSVFile)
    CSVWriter.writerow(["Word", "Count"])
CSVFile.close()

for key in FIRST_USER_WORD_DICTIONARY.keys():
    dataField = []
    dataField.append(key)
    dataField.append(FIRST_USER_WORD_DICTIONARY[key])
    with open(FIRST_USER+".csv", 'a') as CSVFile:
        CSVWriter = csv.writer(CSVFile)
        CSVWriter.writerow(dataField)
    CSVFile.close()

"""
    This is for the second user.
"""
with open(SECOND_USER+".csv", "w") as CSVFile:
    CSVWriter = csv.writer(CSVFile)
    CSVWriter.writerow(["Word", "Count"])
CSVFile.close()

for key in SECOND_USER_WORD_DICTIONARY.keys():
    dataField = []
    dataField.append(key)
    dataField.append(SECOND_USER_WORD_DICTIONARY[key])
    with open(SECOND_USER+".csv", 'a') as CSVFile:
        CSVWriter = csv.writer(CSVFile)
        CSVWriter.writerow(dataField)
    CSVFile.close()

