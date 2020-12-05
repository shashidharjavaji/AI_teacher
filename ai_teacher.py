#-*- coding: utf-8 -*-
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
# nltk.download('all')
import random
import numpy as np
from array import array
from playsound import playsound
from gtts import gTTS
import os
train_text = state_union.raw("2005-GWBush.txt")

sample_text = '''The mutual electric force between two charges is given by Coulomb’s law. How to calculate the force on a charge where there are not one but several charges around? Consider a system of n stationary charges q1, q2, q3, ..., qn in vacuum. What is the force on q1 due to q2, q3, ..., qn? Coulomb’s law is not enough to answer this question.  Recall that forces of mechanical origin add according to the parallelogram law of addition. Is the same true for forces of electrostatic origin?
'''
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)

import speech_recognition as sr

def process_content():
    try:
        myText="you can practice on the following\n1.Nouns\n2.Verbs\n3.Adverbs\n4.Adjectives\n5.Prepositions\n6.Conjunctions\n7.Determiners\n8.Pronouns\n9.If subjects drill say others  please say your option out load"
        correct="you got it right correct answer"
        wrong="OOPS that's a wrong answer"
        output=gTTS(text=myText, lang='en', slow=False)
        yes=gTTS(text=correct, lang='en', slow=False)
        yes.save("right.mp3")
        no=gTTS(text=wrong, lang='en',slow=False)
        no.save("wrong.mp3")
        output.save("choices.mp3")
        #playsound("choices.mp3")
        score=0
        choice=" "
        print("you can practice on the following\n1.Nouns\n2.Verbs\n3.Adverbs\n4.Adjectives\n5.Prepositions\n6.Conjunctions\n7.Determiners\n8.Pronouns\n9.If subjects drill say others")
        playsound("choices.mp3")
        pq=sr.Recognizer()
        with sr.Microphone() as source:
            print("spell out the type of drills you want to practice")
            audio1=pq.listen(source, timeout=3,phrase_time_limit=3)
        choice=pq.recognize_google(audio1)
        print(choice)
        if choice=="noun" or choice=="nouns":
            ch=['NNP', ' ', 'NN', 'NN', 'NNS', 'NNP', 'NNS']
        elif choice=="adjective" or choice=="adjectives" or choice=="adj":
            ch=['JJ','JJS','JJR']
        elif choice=="prepositions" or choice=="preposition" or choice=="prep":
            ch=['IN']
        elif choice=="verb" or choice=="verbs" or choice=="vb":
            ch=['VB','VBD','VBG','VBN','VBP','VBZ']
        elif choice=="adverb" or choice=="adverbs" or choice=="adv":
            ch=['RB','RBR','RBS','WRB']
        elif choice=="pronoun" or choice=="pronouns" or choice=="prp":
            ch=['PRP','PRP$','WP','WP$']
        elif choice=="determiner" or choice=="determiners":
            ch=['DT','WDT']
        elif choice=="conjunction" or choice=="conjunctions":
            ch=['CC']
        elif choice=="other" or choice=="others":
            ch=['NNP', ' ','NN','NN', 'NNS','NNP','NNS','VBD', 'JJ','VBN']
        for i in tokenized[:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            res = [lis[1] for lis in tagged]
            n = 1
            k = [x[n] for x in tagged]
            n = 0
            l = [x[n] for x in tagged]
            n = 0
            m = [x[n] for x in tagged]
            text = ' '.join(m)
            val1 = array("i")
            final = []
            """print("you can practice on the following\n1.Nouns\n2.Verbs\n3.Adverbs\n4.Adjectives\n5.Prepositions\n6.Conjunctions\n7.Determiners\n8.Pronouns\n9.If subjects drill say others")
            pq=sr.Recognizer()
            with sr.Microphone() as source:
                print("spell out the type of drills you want to practice")
                audio1=pq.listen(source, timeout=3,phrase_time_limit=3)
            choice=pq.recognize_google(audio1)
            print(choice)
            if choice=="noun" or choice=="nouns":
                ch=['NNP', ' ', 'NN', 'NN', 'NNS', 'NNP', 'NNS']
            elif choice=="adjective" or choice=="adjectives" or choice=="adj":
                ch=['JJ','JJS','JJR']
            elif choice=="prepositions" or choice=="preposition" or choice=="prep":
                ch=['IN']
            elif choice=="verb" or choice=="verbs" or choice=="vb":
                ch=['VB','VBD','VBG','VBN','VBP','VBZ']
            elif choice=="adverb" or choice=="adverbs" or choice=="adv":
                ch=['RB','RBR','RBS','WRB']
            elif choice=="pronoun" or choice=="pronouns" or choice=="prp":
                ch=['PRP','PRP$','WP','WP$']
            elif choice=="determiner" or choice=="determiners":
                ch=['DT','WDT']
            elif choice=="conjunction" or choice=="conjunctions":
                ch=['CC']
            elif choice=="other" or choice=="others":
                ch=['NNP', ' ','NN','NN', 'NNS','NNP','NNS','VBD', 'JJ','VBN']"""
            for idx, val in enumerate(k):
                #if random.choice(['NNP', ' ', 'NN', 'NN', 'NNS', 'NNP', 'NNS']) in val:
                if len(val1)<1 and random.choice(ch) in val:
                    val1.append(idx)
            for value in val1:
                final.append(l[value])

            for indx, val in enumerate(l):
                for m, v in enumerate(final):
                    if val == v:
                        l[indx] = "________"
            output = {
                "text": text,
                "fibs": final,
            }
            print(' '.join(l))
            #import speech_recognition as sr
            #print("say something1")
            r = sr.Recognizer()
            #print("say something2")
            with sr.Microphone() as source:
                print("spell your answer here in 3 seconds")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            if r.recognize_google(audio) in final:
                print("correct")
                playsound("right.mp3")
                score=score+1
            else:
                print("incorrect")
                playsound("wrong.mp3")
            #print(score)
        print("your score is = {}".format(score))
        scoretxt="your final score is "+str(score)
        scr=gTTS(text=scoretxt, lang='en', slow=False)
        scr.save("scr.mp3")
        playsound("scr.mp3")
    except:
        print("error")
process_content()
