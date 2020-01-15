
from textblob import TextBlob
from nltk.corpus import stopwords
stop_words=set(stopwords.words('english'))
import random
import wikipedia
import listing
import datetime




class Chatbot():
        def __init__(self):
                sen=input("Type here!!!!")
                self.greet(sen)
                
                                

        def greet(self,sen):
                
                if sen in listing.greetin:
                        print(random.choice(listing.greetout))
                        self.__init__()
                else :
                        text=TextBlob(sen)
                        self.parts_of_speech(text)
                        
                        
                
        def parts_of_speech(self,text):
                self.which=False
                self.whowhat=False
                self.howwhen=False
                self.noun=False
                self.adverb=False
                self.verb=False
                self.adjective=False
                self.pronoun=False
                texts=text.tags
                print(texts)
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
                        self.__init__()
                                

                                
        def whichf(self,pronoun):
                if pronoun in listing.bot_call:
                        print(random.choice(listing.bot_unknown_questions_himself))
                        self.__init__()
                elif pronoun in listing.user_call:
                        print(random.choice(listing.user_unknown_questions))
                        self.__init__()

        def whowhatf(self,noun,pronoun,adjective):
                if noun=='name' and pronoun in listing.bot_call:
                        print("You can call me chatbot")
                        self.__init__()
                elif noun=='age' and pronoun in listing.bot_call:
                        print(listing.age)
                        self.__init__()
                elif noun=='name' and pronoun in listing.user_call:
                        print("You haven't told me your name")
                elif pronoun in listing.bot_call:
                        print("I am a chatbot and i am here to help you..")
                        self.__init__()
                elif noun in listing.time_list:
                        x=datetime.datetime.now()
                        if noun=='day' or noun=='week' :
                                print(x.strftime('%A'))
                        elif noun=='date':
                                print(x)
                        elif noun=='month' :
                                print(x.strftime('%B'))
                        elif noun=='time':
                                print(x.time())
                        elif noun=='year':
                                print(x.year)
                        self.__init__()
                        
                        
                else:
                        self.wikiinit(noun,adjective)
                        
                       
                                
                                                        
                                                                
                        

        def whenwheref(self,howw,noun,pronoun,verb,adjective):
                if pronoun in listing.bot_call and howw=='how':
                                if adjective=='old' and pronoun in listing.bot_call:
                                        print(listing.age)
                                        self.__init__()
                                print("I am fine .How are you")
                                self.__init__()
                elif  verb in listing.user_call or pronoun in listing.bot_call  and howw=='where':
                                print("I think we are in kerala")
                                self.__init__()

                else:
                                self.wikiinit(noun,adjective)

        def wikiinit(self,noun,adjective):
                        print("Wait a second let me search ......")
                        if noun is False:
                                self.wiki(adjective)
                        elif adjective is False:
                                self.wiki(noun)
                                
                        else :
                                print(random.choice(listing.bot_unknown_questions_himself))
                                self.__init__()
                

        def wiki(self,sen):
                wik1=wikipedia.summary(sen)
                text=TextBlob(wik1)
                wik2=text.sentences
                for i in range(2) :
                        print(wik2[i])
                        self.__init__()
                        
                       
                        
                
                                

g=Chatbot()
