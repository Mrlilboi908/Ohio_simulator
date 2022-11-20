print('''
   (
                )
               (
         /\  .-"""-.  /\
        //\\/  ,,,  \//\\
        |/\| ,;;;;;, |/\|
        //\\\;-"""-;///\\
       //  \/   .   \/  \\
      (| ,-_| \ | / |_-, |)
        //`__\.-.-./__`\\
       // /.-(() ())-.\ \\
      (\ |)   '---'   (| /)
       ` (|           |) `
    \)           (/
''')
print("Welcome to Ohio simulator")
print("Your mission is to not die") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

spider_input = input("You are walking down the streets of Ohio, and you see a spider. \n Do you touch it? Y or N?: \n")
if (spider_input == "Y"):
    print("You have siezed and died. You would not make it in Ohio GAME OVER")
    quit()
elif(spider_input == "N"):
    print("Congrats you have survived five minutes in Ohio")
else:
    print("You did not enter a valid input. Please try again")
    quit()

#Next Level
print('''

          .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
                                      (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-'
''')
Crocodile_input = input("You continue to walk through Ohio. You hear a funny noise coming from the sewer. Its a Crocodile!! The crocodile snaps at you. \n Are you brave enough to touch it? REMEMBER: YOU ARE IN OHIO! Y or N?: \n ")

if (Crocodile_input == "Y"):
    print("The Croc admires your Bravery, and he swears to protect you at all costs. He says to you 'You gon need a crocodile to survive ohio pimp, my name Jaquavion'")
elif (Crocodile_input == "N"):
    print("You survived 10 minutes in Ohio. Any Logical person in Ohio woulda touched the croc! You are in OHIO you fool! GAME OVER")
    quit()
else:
    print("Bitch we in Ohio, stop pressin the wrong buttons!")
    quit()


#Third level



god_input = input(" You and Jaquavion are walking down the streets, when GOD himself appears(daily coccurence in Ohio).\n Jaquavion snaps at him to protect you from his wrath, but he gets pulverized, his last words to you are \n 'That mufucka crazy pimp, you best get to steppin'. \n Do you run? Y or N?:  ")
if (god_input == "Y"):
    print("God sees that you are a weak man and turns yo ass into a chameleon, which makes up roughly 90 percent of the Ohio population. GAME OVER")
    quit()
elif (god_input == "N"):
    print('''
                                                        ,jf
   _am,    ,_am,  ,_g_oam,    _am,   _g_ag,   _am,   koewkovg   _mm_
 ,gF  @._-gF   @-"  jf   @  ,gF  @  ^ NX  #_,gF  @     jf      qK  "
 8Y      8Y    d   j#   jF .8Y  ,d   dY     8Y   d    jf       *b,
jK   ,  jK   ,N   jN   jF  :K  ,Z  ,jF     jK  ,Z"  ,jfk,       dN.
 NbpP    NbpP    dP   dFk_o8NbpP"V^dF       NbpY"V^"dF "dYo-"*h,W"
                         ,gF',@'
                        :8K  j8
                         "*w*"
    ''')
    print("God admires your courage and makes him your disciple. You will now oversee Ohio for eternity")
else:
    print("MUFUCKA YOU ON THE LAST LEVEL OF THE GAME AND YOU PRESSING THE WRONG BUTTONS!!!!")
    quit()
    

