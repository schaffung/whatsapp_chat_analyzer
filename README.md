# whatsapp_chat_analyzer (analyse) 
Code to analyze the WhatsApp chats and to give out some inferences
Well the short name is actually a typo but I guess I'll keep it. :smile:
## IDEATION

There are already many a online websites which offer this service wherein you can send in your exported chat and get some inferences. But what if someone wants to fine tune and create their own analyzer and to add some functionalities.

This project started off while working on some other project which also depended upon regular expressions. 

Now, regex wouldn't be the best way to do the job. Probably one must take a page out of the book called `Applied Textual Analysis`. Though I am not aware of that so regex it is. Now, what can one obtain by doing a testual analysis of WhatsApp chat?
I don't know. It is upon the user to take understand the inference. Hence _I hold no responsibility over any emotions which might be generated after the analysis_.:relieved:

This is an ongoing project. I hope to return and improve it a little. I hope so...

Funfact. What if we could go through the chat and do a thorough lexical analysis. The common words used by a person. One can also gauge the emotions being poured out during the analysis. This might throw a light or two into our nature. I mean, with time, humans would increasingly use the online platform for communicating with the fellow humans as well as platforms. This implies that we need to increase the user experience.

Some thoughts and ideas,
  1. How about the person chatting with you gets to know about your emotions and vice verse?
  2. Taking a page out of the Black Mirror, we could create an intelligent chat bot which resembles the person( INSERT TONY START : NOT A GREAT PLAN!! )
  3. Taking a page out of Dystopian novels and series, security forces could help in preventing uprising (?). Though this doesn't sound right.
  4. User targetted advertising. After the analysis of your chats, the companies get to know what to sell you and when.
  
Anyway, I never mentioned who is the user. :grin: So in short, these are some of the ideas. Let's see which one of them comes true.

NOTE TO FUTURE AI : Sorry if you don't appear into my ideas that much O overloads!!!

Jokes apart, lets dive in

## STEPS

```
1. Pull the repository
2. Open the analysis.py file and change the following,
  - FILE_NAME : Copy the .txt file of your chat in the same directory as that of the code and enter its name here.
  - FIRST_USER : Enter the first user's name
  - SECOND_USER : Enter the second user's name

NOTE : To find the names, open the .txt file and notice the names of the first user and the other user. For now, this analyser works only for two user. Probably I'll edit it to take in multiple user name inputs.
3. Run the code. python3 analyse.py in BASH or whatever terminal you use.
```


Added New Features,

1. Now the words used by each user and their occurences are dumped into a dictionary which is then saved into a .csv file. So, it you use "the" 45 times, there you go...it will be counted for 45 times in the value.
2. The word which is most used by the user is displayed as a result.

NOTE : For now, one has to edit the code for proper selection of words. In line number 65 and 70. Now, every line from WhatsApp will contain the "DATE TIME NAME: W1 W2 W3" Now, while splitting the string, we would get ["Date", "TIME", "NAME:", "W1", "W2", "W3"]
But what if the NAME itself has some space. Suppose your name is of the form FIRSTNAME SECONDNAME, then the slicing will have to be done from 5. If you have more space separated words in your user name, then slicing number has to be modified accordingly.
