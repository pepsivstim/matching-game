#===MODULES===#
from tkinter import *
from random import randint
import time

#===VARIABLES AND LISTS===#
#the number of times the procedure random has run
random_run = 0
#the amount of cards in the game
card_amount = 16
open_card = []
already_used = []
matches = 0
clicks = 0
start = time.time()

#===WINDOW===#
#create a new window, and set the sizes of the window and title
main_window = Tk()
main_window.geometry("428x530")
main_window.title('Memory Card 4x4')
main_window.iconbitmap('.\playing_cards\icon.ico')

#===INSTRUCTIONS===#
#print instructions
print("Tkinter Matching Card Game | 1/17/2017 | Period 7 Computer Science |")
print('')
print("By: Timothy Chu and Robert Bao")
print('')
print("This is a simple card flipping game that involves memory.  Click a card to flip it over.  Flip over another card to find a match.  If the cards don’t match, they flip back.  If the cards do match, they are flipped over and grayed out.  Once you make all of the cards match, and win and receive your results in a separate window.")
print('')
print("REMEMBER: Cards are matched by both suit and number!")
print('')
print("Highscore: 383.8 (Timothy - 26 clicks | 20 seconds)")



#===IMPORT ALL IMAGES===#
card_back = PhotoImage(file=".\playing_cards\card_back.pgm")
spade_ace = PhotoImage(file=".\playing_cards\spade_ace.pgm")
spade_2 = PhotoImage(file=".\playing_cards\spade_2.pgm")
spade_3 = PhotoImage(file=".\playing_cards\spade_3.pgm")
spade_4 = PhotoImage(file=".\playing_cards\spade_4.pgm")
spade_5 = PhotoImage(file=".\playing_cards\spade_5.pgm")
spade_6 = PhotoImage(file=".\playing_cards\spade_6.pgm")
spade_7 = PhotoImage(file=".\playing_cards\spade_7.pgm")
spade_8 = PhotoImage(file=".\playing_cards\spade_8.pgm")
spade_9 = PhotoImage(file=".\playing_cards\spade_9.pgm")
spade_10 = PhotoImage(file=".\playing_cards\spade_10.pgm")
spade_jack = PhotoImage(file=".\playing_cards\spade_jack.pgm")
spade_queen = PhotoImage(file=".\playing_cards\spade_queen.pgm")
spade_king = PhotoImage(file=".\playing_cards\spade_king.pgm")
club_ace = PhotoImage(file=".\playing_cards\club_ace.pgm")
club_2 = PhotoImage(file=".\playing_cards\club_2.pgm")
club_3 = PhotoImage(file=".\playing_cards\club_3.pgm")
club_4 = PhotoImage(file=".\playing_cards\club_4.pgm")
club_5 = PhotoImage(file=".\playing_cards\club_5.pgm")
club_6 = PhotoImage(file=".\playing_cards\club_6.pgm")
club_7 = PhotoImage(file=".\playing_cards\club_7.pgm")
club_8 = PhotoImage(file=".\playing_cards\club_8.pgm")
club_9 = PhotoImage(file=".\playing_cards\club_9.pgm")
club_10 = PhotoImage(file=".\playing_cards\club_10.pgm")
club_jack = PhotoImage(file=".\playing_cards\club_jack.pgm")
club_queen = PhotoImage(file=".\playing_cards\club_queen.pgm")
club_king = PhotoImage(file=".\playing_cards\club_king.pgm")
heart_ace = PhotoImage(file=".\playing_cards\heart_ace.pgm")
heart_2 = PhotoImage(file=".\playing_cards\heart_2.pgm")
heart_3 = PhotoImage(file=".\playing_cards\heart_3.pgm")
heart_4 = PhotoImage(file=".\playing_cards\heart_4.pgm")
heart_5 = PhotoImage(file=".\playing_cards\heart_5.pgm")
heart_6 = PhotoImage(file=".\playing_cards\heart_6.pgm")
heart_7 = PhotoImage(file=".\playing_cards\heart_7.pgm")
heart_8 = PhotoImage(file=".\playing_cards\heart_8.pgm")
heart_9 = PhotoImage(file=".\playing_cards\heart_9.pgm")
heart_10 = PhotoImage(file=".\playing_cards\heart_10.pgm")
heart_jack = PhotoImage(file=".\playing_cards\heart_jack.pgm")
heart_queen = PhotoImage(file=".\playing_cards\heart_queen.pgm")
heart_king = PhotoImage(file=".\playing_cards\heart_king.pgm")
diamond_ace = PhotoImage(file=".\playing_cards\diamond_ace.pgm")
diamond_2 = PhotoImage(file=".\playing_cards\diamond_2.pgm")
diamond_3 = PhotoImage(file=".\playing_cards\diamond_3.pgm")
diamond_4 = PhotoImage(file=".\playing_cards\diamond_4.pgm")
diamond_5 = PhotoImage(file=".\playing_cards\diamond_5.pgm")
diamond_6 = PhotoImage(file=".\playing_cards\diamond_6.pgm")
diamond_7 = PhotoImage(file=".\playing_cards\diamond_7.pgm")
diamond_8 = PhotoImage(file=".\playing_cards\diamond_8.pgm")
diamond_9 = PhotoImage(file=".\playing_cards\diamond_9.pgm")
diamond_10 = PhotoImage(file=".\playing_cards\diamond_10.pgm")
diamond_jack = PhotoImage(file=".\playing_cards\diamond_jack.pgm")
diamond_queen = PhotoImage(file=".\playing_cards\diamond_queen.pgm")
diamond_king = PhotoImage(file=".\playing_cards\diamond_king.pgm")

#various images
image_list = [spade_ace, spade_2, spade_3, spade_4, spade_5, spade_6, spade_7, spade_8, spade_9, spade_10, spade_jack, spade_queen, spade_king,
              club_ace, club_2, club_3, club_4, club_5, club_6, club_7, club_8, club_9, club_10, club_jack, club_queen, club_king,
              heart_ace, heart_2, heart_3, heart_4, heart_5, heart_6, heart_7, heart_8, heart_9, heart_10, heart_jack, heart_queen, heart_king,
              diamond_ace, diamond_2, diamond_3, diamond_4, diamond_5, diamond_6, diamond_7, diamond_8, diamond_9, diamond_10, diamond_jack, diamond_queen, diamond_king]



#===PROCEDURES===#
def flip(button):

  """ Precondition: flips button and checks to see if there is a match.
If there is not match, everything flips back over.
If there is a match, the cards are disabled

The input "button" is the button that is being clicked
There is no output. """
  
  global open_card
  global clicks
  #WHEN A BUTTON IS CLICKED, TURN TO THE IMAGE TO REPRESENT A FLIP
  if button['flip'] == False:
    button['button'].config(image=button['image'])
    button['flip'] = True
    clicks = clicks + 1
    open_card.append(button['image'])
    #IF THE TWO CARDS IN OPEN_CARD MATCH
    if len(open_card) >= 2:
      if open_card[0] == open_card[1]:
        global matches
        #looks for the card using find_image(), and flips them back to card_back
        find_image(open_card[0], None)['button'].config(image=card_back, state=DISABLED)
        find_image(open_card[0], None)['flip'] = False
        find_image(open_card[1], find_image(open_card[0], None))['button'].config(image=card_back, state=DISABLED)
        find_image(open_card[1], find_image(open_card[0], None))['flip'] = False
        open_card = []
        matches = matches + 1
        #IF THERE ARE 2 MATCHES, THE GAME IS COMPLETED
        if matches == 8:
          win_screen()
          
      else:
        #IF THE TWO CARDS IN OPEN_CARD DON'T MATCH, FLIP ALL THE CARDS BACK AFTER A 500 MS DELAY
        button_1_1['button'].after(500, lambda: button_1_1['button'].config(image=card_back))
        button_1_2['button'].after(500, lambda: button_1_2['button'].config(image=card_back))
        button_1_3['button'].after(500, lambda: button_1_3['button'].config(image=card_back))
        button_1_4['button'].after(500, lambda: button_1_4['button'].config(image=card_back))
        
        button_2_1['button'].after(500, lambda: button_2_1['button'].config(image=card_back))
        button_2_2['button'].after(500, lambda: button_2_2['button'].config(image=card_back))
        button_2_3['button'].after(500, lambda: button_2_3['button'].config(image=card_back))
        button_2_4['button'].after(500, lambda: button_2_4['button'].config(image=card_back))

        button_3_1['button'].after(500, lambda: button_3_1['button'].config(image=card_back))
        button_3_2['button'].after(500, lambda: button_3_2['button'].config(image=card_back))
        button_3_3['button'].after(500, lambda: button_3_3['button'].config(image=card_back))
        button_3_4['button'].after(500, lambda: button_3_4['button'].config(image=card_back))
        
        button_4_1['button'].after(500, lambda: button_4_1['button'].config(image=card_back))
        button_4_2['button'].after(500, lambda: button_4_2['button'].config(image=card_back))
        button_4_3['button'].after(500, lambda: button_4_3['button'].config(image=card_back))
        button_4_4['button'].after(500, lambda: button_4_4['button'].config(image=card_back))
        
        button_1_1['flip'] = False
        button_1_2['flip'] = False
        button_1_3['flip'] = False
        button_1_4['flip'] = False

        button_2_1['flip'] = False
        button_2_2['flip'] = False
        button_2_3['flip'] = False
        button_2_4['flip'] = False

        button_3_1['flip'] = False
        button_3_2['flip'] = False
        button_3_3['flip'] = False
        button_3_4['flip'] = False

        button_4_1['flip'] = False
        button_4_2['flip'] = False
        button_4_3['flip'] = False
        button_4_4['flip'] = False
        
        open_card = []

#THIS CREATES THE WIN SCREEN
def win_screen():
  """
Precondition: win_screen creates a screen when you match everything and tells you how many clicks it took and the amount of time

There is no input.
There is no output.
                    """

  global start
  
  #CALCULATES THE SCORE BY USING BOTH THE TIME AND CLICKS AS FACTORS
  stop = time.time()
  total_time = round((stop - start), 2)
  score = round((10000 - total_time)/clicks, 1)
  
  win_win = Tk()
  win_win.title('Win!')
  win_win.geometry('250x200')
  win_win.iconbitmap('.\playing_cards\icon.ico')
  
  title = Label(win_win,text="You Win!",font=("ComicSans",20,"bold"),fg="#1908d6",bg="#a1dbcd")
  title.place(x=65,y=20)
  #this is the label for number of clicks
  clicks_label = Label(win_win,text='Clicks:', font=("ComicSans",10,"bold"))
  clicks_label.place(x=65, y=100)
  click_label = Label(win_win,text=clicks, font=("ComicSans",10,"bold"))
  click_label.place(x=125, y=100)
  #this is the label for time used
  times_label = Label(win_win,text='Time:', font=("ComicSans",10,"bold"))
  times_label.place(x=65, y=130)
  time_label = Label(win_win,text=total_time, font=("ComicSans",10,"bold"))
  time_label.place(x=125, y=130)
  #this is the label for score
  scores_label = Label(win_win,text='Score:', font=("ComicSans",10,"bold"))
  scores_label.place(x=65, y=160)
  scores_label = Label(win_win,text=score, font=("ComicSans",10,"bold"))
  scores_label.place(x=125, y=160)

  main_window.destroy()


  
#THIS PROCEDURE CHECKS FOR THE BUTTON THE IMAGES ARE LINKED TO
def find_image(open_card, no_use):
  """
Precondition: find_image uses a cards image to find the dictionary it is stored in.
It makes sure it is not looking for the same thing last time using no_use.

There is both open_card and no_use as input (no_use is sometimes not used).
The output is the dictionary that the images was in.
  """

  if no_use != button_1_1:
    if button_1_1['image'] == open_card:
      return button_1_1
  if no_use != button_1_2:
    if button_1_2['image'] == open_card:
      return button_1_2
  if no_use != button_1_3:
    if button_1_3['image'] == open_card:
      return button_1_3
  if no_use != button_1_4:
    if button_1_4['image'] == open_card:
      return button_1_4

  if no_use != button_2_1:
    if button_2_1['image'] == open_card:
      return button_2_1
  if no_use != button_2_2:
    if button_2_2['image'] == open_card:
      return button_2_2
  if no_use != button_2_3:
    if button_2_3['image'] == open_card:
      return button_2_3    
  if no_use != button_2_4:
    if button_2_4['image'] == open_card:
      return button_2_4

  if no_use != button_3_1:
    if button_3_1['image'] == open_card:
      return button_3_1
  if no_use != button_3_2:
    if button_3_2['image'] == open_card:
      return button_3_2
  if no_use != button_3_3:
    if button_3_3['image'] == open_card:
      return button_3_3
  if no_use != button_3_4:
    if button_3_4['image'] == open_card:
      return button_3_4

  if no_use != button_4_1:
    if button_4_1['image'] == open_card:
      return button_4_1
  if no_use != button_4_2:
    if button_4_2['image'] == open_card:
      return button_4_2
  if no_use != button_4_3:
    if button_4_3['image'] == open_card:
      return button_4_3
  if no_use != button_4_4:
    if button_4_4['image'] == open_card:
      return button_4_4
    
#THESE PROCEDURES ARE REQUIRED FOR TKINTER TO RUN THE FLIP(TKINTER DOESN'T TAKE ARGUMENTS)
def flip_1_1():
  flip(button_1_1)

def flip_1_2():
  flip(button_1_2)

def flip_1_3():
  flip(button_1_3)

def flip_1_4():
  flip(button_1_4)


def flip_2_1():
  flip(button_2_1)
    
def flip_2_2():
  flip(button_2_2)
    
def flip_2_3():
  flip(button_2_3)
    
def flip_2_4():
  flip(button_2_4)

    
def flip_3_1():
  flip(button_3_1)
    
def flip_3_2():
  flip(button_3_2)
    
def flip_3_3():
  flip(button_3_3)
    
def flip_3_4():
  flip(button_3_4)


    
def flip_4_1():
  flip(button_4_1)
    
def flip_4_2():
  flip(button_4_2)
    
def flip_4_3():
  flip(button_4_3)
    
def flip_4_4():
  flip(button_4_4)

#THIS PROCEDURE RANDOMLY GENERATES CARDS FOR EACH BUTTON
def random(number):
  """
Precondition: random generates a random index.
Once half of the cards are generated, it uses what has already been used to guarantee a matching pair.

There is number as the input (the amount of indicies that can be used).
There integer img_index or img_index2 depending on the conditions as the output.
  """
  global random_run
  if random_run < card_amount/2:
    rand_int = randint(0, number)
    img_index = image_list[rand_int]
    already_used.append(img_index)
    #deletes what image was used
    del image_list[rand_int]
    #increments random_run to half 

    random_run = random_run + 1
    return img_index
  #this section uses cards in already_used
  if random_run >= card_amount/2:
    rand_int2 = randint(0, (number-28)) 
    img_index2 = already_used[rand_int2]
    del already_used[rand_int2]
    return img_index2


#===BUTTONS===#

#all of the buttons are stored in dictinaries that hold properties like its image and if its flipped or not
button_1_1 = {'button': Button(main_window, command=flip_1_1, image=card_back), 'flip' : False, 'image':random(len(image_list)-1)}
button_1_1['button'].grid(column=1, row=1)

button_1_2 = {'button': Button(main_window, command=flip_1_2, image=card_back), 'flip' : False, 'image':random(len(image_list)-2)}
button_1_2['button'].grid(column=1, row=2)

button_1_3 = {'button': Button(main_window, command=flip_1_3, image=card_back), 'flip' : False, 'image':random(len(image_list)-3)}
button_1_3['button'].grid(column=1, row=3)

button_1_4 = {'button': Button(main_window, command=flip_1_4, image=card_back), 'flip' : False, 'image':random(len(image_list)-4)}
button_1_4['button'].grid(column=1, row=4)


button_2_1 = {'button': Button(main_window, command=flip_2_1, image=card_back), 'flip' : False, 'image':random(len(image_list)-5)}
button_2_1['button'].grid(column=2, row=1)

button_2_2 = {'button': Button(main_window, command=flip_2_2, image=card_back), 'flip' : False, 'image':random(len(image_list)-6)}
button_2_2['button'].grid(column=2, row=2)

button_2_3 = {'button': Button(main_window, command=flip_2_3, image=card_back), 'flip' : False, 'image':random(len(image_list)-7)}
button_2_3['button'].grid(column=2, row=3)

button_2_4 = {'button': Button(main_window, command=flip_2_4, image=card_back), 'flip' : False, 'image':random(len(image_list)-8)}
button_2_4['button'].grid(column=2, row=4)


button_3_1 = {'button': Button(main_window, command=flip_3_1, image=card_back), 'flip' : False, 'image':random(len(image_list)-9)}
button_3_1['button'].grid(column=3, row=1)

button_3_2 = {'button': Button(main_window, command=flip_3_2, image=card_back), 'flip' : False, 'image':random(len(image_list)-10)}
button_3_2['button'].grid(column=3, row=2)

button_3_3 = {'button': Button(main_window, command=flip_3_3, image=card_back), 'flip' : False, 'image':random(len(image_list)-11)}
button_3_3['button'].grid(column=3, row=3)

button_3_4 = {'button': Button(main_window, command=flip_3_4, image=card_back), 'flip' : False, 'image':random(len(image_list)-12)}
button_3_4['button'].grid(column=3, row=4)


button_4_1 = {'button': Button(main_window, command=flip_4_1, image=card_back), 'flip' : False, 'image':random(len(image_list)-13)}
button_4_1['button'].grid(column=4, row=1)

button_4_2 = {'button': Button(main_window, command=flip_4_2, image=card_back), 'flip' : False, 'image':random(len(image_list)-14)}
button_4_2['button'].grid(column=4, row=2)

button_4_3 = {'button': Button(main_window, command=flip_4_3, image=card_back), 'flip' : False, 'image':random(len(image_list)-15)}
button_4_3['button'].grid(column=4, row=3)

button_4_4 = {'button': Button(main_window, command=flip_4_4, image=card_back), 'flip' : False, 'image':random(len(image_list)-16)}
button_4_4['button'].grid(column=4, row=4)


#===MAINLOOP===#
#allows tkinter to run
main_window.mainloop()

