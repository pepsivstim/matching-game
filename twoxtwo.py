#===2x2 CODE===#
from tkinter import *
from random import randint
import time

#===VARIABLES AND LISTS===#
random_run = 0
card_amount = 4
open_card = []
already_used = []
matches = 0
clicks = 0
start = time.time()

#===WINDOW===#
twoxtwo_win = Tk()
twoxtwo_win.geometry("215x265")
twoxtwo_win.title('Memory Card 2x2')
twoxtwo_win.iconbitmap('.\playing_cards\icon.ico')


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
#STORE ALL OF THE IMAGES IN A LIST
image_list = [spade_ace, spade_2, spade_3, spade_4, spade_5, spade_6, spade_7, spade_8, spade_9, spade_10, spade_jack, spade_queen, spade_king,
              club_ace, club_2, club_3, club_4, club_5, club_6, club_7, club_8, club_9, club_10, club_jack, club_queen, club_king,
              heart_ace, heart_2, heart_3, heart_4, heart_5, heart_6, heart_7, heart_8, heart_9, heart_10, heart_jack, heart_queen, heart_king,
              diamond_ace, diamond_2, diamond_3, diamond_4, diamond_5, diamond_6, diamond_7, diamond_8, diamond_9, diamond_10, diamond_jack, diamond_queen, diamond_king]



#===PROCEDURES===#

def flip(button):
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
        find_image(open_card[0], None)['button'].config(image=card_back, state=DISABLED)
        find_image(open_card[0], None)['flip'] = False
        find_image(open_card[1], find_image(open_card[0], None))['button'].config(image=card_back, state=DISABLED)
        find_image(open_card[1], find_image(open_card[0], None))['flip'] = False
        open_card = []
        matches = matches + 1
        #IF THERE ARE 2 MATCHES, THE GAME IS COMPLETED
        if matches == 2:
          win_screen()
          
      else:
        #IF THE TWO CARDS IN OPEN_CARD DON'T MATCH, FLIP ALL THE CARDS BACK AFTER A 500 MS DELAY
        button_1_1['button'].after(500, lambda: button_1_1['button'].config(image=card_back))
        button_1_2['button'].after(500, lambda: button_1_2['button'].config(image=card_back))
        button_2_1['button'].after(500, lambda: button_2_1['button'].config(image=card_back))
        button_2_2['button'].after(500, lambda: button_2_2['button'].config(image=card_back))
        button_1_1['flip'] = False
        button_1_2['flip'] = False
        button_2_1['flip'] = False
        button_2_2['flip'] = False
        open_card = []

#THIS CREATES THE WIN SCREEN
def win_screen():
  global start
  
  #CALCULATES THE SCORE BY USING BOTH THE TIME AND CLICKS AS FACTORS
  stop = time.time()
  total_time = round((stop - start), 2)
  score = round((100 - total_time)/clicks, 1)
  
  win_win = Tk()
  win_win.title('Win!')
  win_win.geometry('200x200')
  
  title = Label(win_win,text="You Win!",font=("ComicSans",20,"bold"),fg="#1908d6",bg="#a1dbcd")
  title.place(x=40,y=20)

  clicks_label = Label(win_win,text='Clicks:', font=("ComicSans",10,"bold"))
  clicks_label.place(x=40, y=100)
  click_label = Label(win_win,text=clicks, font=("ComicSans",10,"bold"))
  click_label.place(x=100, y=100)

  times_label = Label(win_win,text='Time:', font=("ComicSans",10,"bold"))
  times_label.place(x=40, y=130)
  time_label = Label(win_win,text=total_time, font=("ComicSans",10,"bold"))
  time_label.place(x=100, y=130)

  scores_label = Label(win_win,text='Score:', font=("ComicSans",10,"bold"))
  scores_label.place(x=40, y=160)
  scores_label = Label(win_win,text=score, font=("ComicSans",10,"bold"))
  scores_label.place(x=100, y=160)

  twoxtwo_win.destroy()


  
#THIS PROCEDURE CHECKS FOR THE BUTTON THE IMAGES ARE LINKED TO
def find_image(open_card, no_use):
  if no_use != button_1_1:
    if button_1_1['image'] == open_card:
      return button_1_1
  if no_use != button_1_2:
    if button_1_2['image'] == open_card:
      return button_1_2
  if no_use != button_2_1:
    if button_2_1['image'] == open_card:
      return button_2_1
  if no_use != button_2_2:
    if button_2_2['image'] == open_card:
      return button_2_2

#THESE PROCEDURES ARE REQUIRED FOR TKINTER TO RUN (TKINTER DOESN'T TAKE ARGUMENTS)
def flip_1_1():
  flip(button_1_1)

def flip_1_2():
  flip(button_1_2)

def flip_2_1():
  flip(button_2_1)

def flip_2_2():
  flip(button_2_2)

#THIS PROCEDURE RANDOMLY GENERATES CARDS FOR EACH BUTTON
def random(number):
  global random_run
  if random_run < card_amount/2:
    rand_int = randint(0, number)
    img_index = image_list[rand_int]
    already_used.append(img_index)
    del image_list[rand_int]
    random_run = random_run + 1
    return img_index
  #THIS SECTION GUARANTEES TWO OF THE SAME CARD
  if random_run >= card_amount/2:
    rand_int2 = randint(0, (number-46)) 
    img_index2 = already_used[rand_int2]
    del already_used[rand_int2]
    return img_index2


#===BUTTONS===#
button_1_1 = {'button': Button(twoxtwo_win, command=flip_1_1, image=card_back), 'flip' : False, 'image':random(len(image_list)-1)}
button_1_1['button'].grid(column=1, row=1)

button_2_1 = {'button': Button(twoxtwo_win, command=flip_2_1, image=card_back), 'flip' : False, 'image':random(len(image_list)-2)}
button_2_1['button'].grid(column=2, row=1)

button_1_2 = {'button': Button(twoxtwo_win, command=flip_1_2, image=card_back), 'flip' : False, 'image':random(len(image_list)-3)} 
button_1_2['button'].grid(column=1, row=2)

button_2_2 = {'button': Button(twoxtwo_win, command=flip_2_2, image=card_back), 'flip' : False, 'image':random(len(image_list)-4)} 
button_2_2['button'].grid(column=2, row=2)


#===MAINLOOP===#
twoxtwo_win.mainloop()

