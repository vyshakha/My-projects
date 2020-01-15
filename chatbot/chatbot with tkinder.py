
from textblob import TextBlob
from nltk.corpus import stopwords
stop_words=set(stopwords.words('english'))
import random
import wikipedia
import listing
import datetime
from tkinter import *
from requests.exceptions import ConnectionError


master=Tk()
master.geometry("800x500")  
master.title('chatbot')
Label(master , text="input here").grid(row=0,column=0)
sen1=Entry(master)
sen1.grid(row=0,column=1)



class Chatbot():
        def __init__(self):
                self.text=Text(master)
                self.text.grid(row=0,column=3,rowspan=3)

        def start(self):
                
                sen=sen1.get()
                sen1.delete(0,'end')
                self.greet(sen)
                
                                

        def greet(self,sen):
                sen=sen.lower()
                if sen in listing.greetin:
                        print(random.choice(listing.greetout))
                        self.text.insert(INSERT,(random.choice(listing.greetout)))
                        self.text.insert(INSERT,'\n')
                        
                        
                else :
                        text1=TextBlob(sen)
                        self.parts_of_speech(text1)
                        
                        
                
        def parts_of_speech(self,text1):
                self.which=False
                self.whowhat=False
                self.howwhen=False
                self.noun=False
                self.adverb=False
                self.verb=False
                self.adjective=False
                self.pronoun=False
                texts=text1.tags
                #print(texts)
                for i,j in texts:
                        if j in listing.noun_list:
                                self.noun=i
                        elif j in listing.adverb_list:
                                self.adverb=i
                        elif j in listing.verb_list:
                                self.verb=i
                        elif j in listing.adjective_list:
                                self.adjective=i
                        elif j in listing.pronoun_list:
                                self.pronoun=i
                        elif j in listing.wh_determiner_list:
                                self.which=True
                        elif j in listing.wh_pronoun_list:
                                self.whowhat=True
                        elif j in listing.wh_adverb_list:
                                self.howwhen=True
                                self.howwhenwhere=i
                                

                if self.which==True:
                        self.whichf(self.pronoun)
                elif self.whowhat==True:
                        self.whowhatf(self.noun,self.pronoun,self.adjective)
                elif self.howwhen==True:
                        self.whenwheref(self.howwhenwhere,self.noun,self.pronoun,self.verb,self.adjective)
                else:
                        print(random.choice(listing.casualreplay))
                        self.text.insert(INSERT,(random.choice(listing.casualreplay)))
                        self.text.insert(INSERT,'\n')
                       
                                

                                
        def whichf(self,pronoun):
                if pronoun in listing.bot_call:
                        print(random.choice(listing.bot_unknown_questions_himself))
                        self.text.insert(INSERT,(random.choice(listing.bot_unknown_questions_himself)))
                        self.text.insert(INSERT,'\n')
                        
                elif pronoun in listing.user_call:
                        print(random.choice(listing.user_unknown_questions))
                        self.text.insert(INSERT,(random.choice(listing.user_unknown_questions)))
                        self.text.insert(INSERT,'\n')
                
        def whowhatf(self,noun,pronoun,adjective):
                if noun=='name' and pronoun in listing.bot_call:
                        print("You can call me chatbot")
                        self.text.insert(INSERT,("You can call me chatbot\n"))  
                        
                elif noun=='age' and pronoun in listing.bot_call:
                        print(listing.age)
                        self.text.insert(INSERT,(listing.age))
                        self.text.insert(INSERT,'\n')
                        
                     
                elif noun=='name' and pronoun in listing.user_call:
                        print("You haven't told me your name")
                        self.text.insert(INSERT,("You haven't told me your name\n"))  
                 
                elif pronoun in listing.bot_call:
                        print("I am a chatbot and i am here to help you...")
                        self.text.insert(INSERT,("I am a chatbot and i am here to help you..\n"))  
                        
                elif noun in listing.time_list:
                        x=datetime.datetime.now()
                        if noun=='day' or noun=='week' :
                                print(x.strftime('%A'))
                                self.text.insert(INSERT,(x.strftime('%A')))
                                self.text.insert(INSERT,'\n')
                                
                        elif noun=='date':
                                print(x)
                                self.text.insert(INSERT,(x))
                                self.text.insert(INSERT,'\n')
                                
                        elif noun=='month' :
                                print(x.strftime('%B'))
                                self.text.insert(INSERT,(x.strftime('%B')))
                                self.text.insert(INSERT,'\n')
                                
                        elif noun=='time':
                                print(x.time())
                                self.text.insert(INSERT,(x.time()))
                                self.text.insert(INSERT,'\n')
                                
                        elif noun=='year':
                                print(x.year)
                                self.text.insert(INSERT,(x.year))  
                                self.text.insert(INSERT,'\n')
                        
                        
                        
                else:
                        self.wikiinit(noun,adjective)
                        
                       
                                
                                                        
                                                                
                        

        def whenwheref(self,howw,noun,pronoun,verb,adjective):
                if pronoun in listing.bot_call and howw=='how':
                                if adjective=='old' and pronoun in listing.bot_call:
                                        print(listing.age)
                                        self.text.insert(INSERT,(listing.age))  
                                        self.text.insert(INSERT,'\n')
                                        
                                print("I am fine .How are you")
                                self.text.insert(INSERT,("I am fine .How are you"))
                                self.text.insert(INSERT,'\n')
                                
                elif  verb in listing.user_call or pronoun in listing.bot_call  and howw=='where':
                                print("I think we are in kerala")
                                self.text.insert(INSERT,("I think we are in kerala"))
                                self.text.insert(INSERT,'\n')
                                
                else:
                                self.wikiinit(noun,adjective)

        def wikiinit(self,noun,adjective):
                        print("Wait a second let me search ......")
                        self.text.insert(INSERT,("Wait a second let me search ......\n"))
                        if noun is False:
                                self.wiki(adjective)
                        elif adjective is False:
                                self.wiki(noun)
                                
                        else :
                                print(random.choice(listing.bot_unknown_questions_himself))
                                self.text.insert(INSERT,(random.choice(listing.bot_unknown_questions_himself)))  
                                self.text.insert(INSERT,'\n')
                

        def wiki(self,sen):
                try:
                        wik1=wikipedia.summary(sen)
                except ConnectionError as e:
                        print("error occured")
                        self.text.insert(INSERT,"******I think there is some problem with your connection*****\n")  
                        
                        
                text=TextBlob(wik1)
                wik2=text.sentences
                for i in range(2) :
                        print(wik2[i])
                        self.text.insert(INSERT,(wik2[i]))
                        self.text.insert(INSERT,'\n')
                        
                      
g=Chatbot()

def button():
        Button(master,text='GO',command=g.start,width=25).grid(row=1,column=1)

button()
                                


