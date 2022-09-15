#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Madlibs generator python code by Aniesh Das


# In[2]:


#import module
from tkinter import *

# initialize window
root = Tk()
root.geometry('300x300')
root.title('DataFlair-Mad Libs Generator')
Label(root, text= 'Mad Libs Generator \n Have Fun!' , font = 'arial 20 bold').pack()
Label(root, text = 'Click Any One :', font = 'arial 15 bold').place(x=40, y=80)


# In[3]:


def madlib1():

    animals= input('enter an animal name : ')
    profession = input('enter a profession: ')
    cloth = input('enter name of a piece of clothing: ')
    things = input('enter a thing name: ')
    name= input('enter a name: ')
    place = input('enter a place name: ')
    verb = input('enter a verb in ing form: ')
    food = input('a food name: ')
    print('say ' + food + ',said the photographer as the camera flashed! ' + name + ' and I had gone to ' + place +' to get our photos taken today. The first photo we really wanted was a picture of us dressed as ' + animals + ' pretending to be a ' + profession + ' .when we saw the second photo, it was exactly what I wanted. We both looked like ' + things + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind')


# In[4]:


def madlib2():
   
    adjactive = input('enter an adjective : ')
    color = input('enter a color name : ')
    thing = input('enter a thing name :')
    place = input('enter a place name : ')
    person= input('enter a person\'s name : ')
    adjactive1 = input('enter an adjective : ')
    insect= input('enter an insect name : ')
    food = input('enter a food name : ')
    verb = input('enter a verb : ')

    print('Last night I dreamt I was a ' +adjactive+ ' butterfly with ' + color+ ' clothes that looked like '+thing+ ' .I flew to ' + place+ ' with my bestfriend and '+person+ ' who was a '+adjactive1+ ' ' +insect +' .We ate some ' +food+ ' when we got there and then decided to '+verb+ ' and the dream ended when I said-- lets ' +verb+ '.')


# In[5]:


def madlib3():
    person = input('enter a person name: ')
    color = input('enter a colour : ')
    foods = input('enter a food name : ')
    adjective = input('enter an adjective : ')
    thing = input('enter a thing name : ')
    place = input('enter place : ')
    verb = input('enter verb : ')
    adverb = input('enter adverb : ')
    food = input('enter food name: ')
    things = input('enter a thing name : ')
    
    print('Today we picked up an apple from '+person+ "'s Orchard. I had no idea there were so many different varieties of apples. I ate " +color+ ' apples straight off the tree that tasted like '+foods+ '. Then there was a '+adjective+ ' apple that looked like a ' + thing + '.When our bags were full, we went on a ride for a daytrip to '+place+ ' and back. It ended at a hay pile where we got to ' +verb+ ' ' +adverb+ '. I can hardly wait to get home and cook with the apples. We are going to make appple '+food+ ' and '+things+' pies!.')  


# In[ ]:


Button(root, text= 'The Photographer', font ='arial 15', command= madlib1, bg = 'ghost white').place(x=60, y=120)
Button(root, text= 'The Apple story', font ='arial 15', command = madlib3 , bg = 'ghost white').place(x=70, y=180)
Button(root, text= 'The Butterfly', font ='arial 15', command = madlib2, bg = 'ghost white').place(x=80, y=240)

root.mainloop()


# In[ ]:




