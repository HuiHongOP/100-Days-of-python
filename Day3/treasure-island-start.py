print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
road_decision= input("You have arrived at an intersection road, Which side you want to go? 'Right' or 'Left':  ")


if road_decision == "Left" or road_decision == "left":
  swim_or_wait= input("There is a lake in front of you. You want 'swim' or 'wait' ? ")
  if swim_or_wait =="Wait" or swim_or_wait == "wait":
    door= input("Which door? 'Red', 'Blue', 'Yellow? ")
    if door == "Red" or door =="red":
      print('''
               (  .      )
                )        (         )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      ''')
      print("Burned by fire. Game Over.")
    elif door == "Blue" or door == "blue":
      print('''             
       ---_ ......._-_--.
      (|\ /      / /| \  
      /  /     .'  -=-'   `.
     /  /    .'             )
   _/  /   .'        _.)   /
  / o   o        _.-' /  .'
  \          _.-'    / .'*|
   \______.-'//    .'.' \*|
    \|  \ | //   .'.' _ |*|
     `   \|//  .'.'_ _ _|*|
      .  .// .'.' | _ _ \*|
      \`-|\_/ /    \ _ _ \*
       `/'\__/      \ _ _ \*
      /^|            \ _ _ \*
     '  `             \ _ _ \      
                       \_
      ''')
      print("Eaten by beasts. Game Over.")
    elif door== "Yellow" or door == "yellow":
      print("You Win!!")
    else:
      print("Game Over.")
  else:
    print('''
                     )_ `.
                )_ `. '
               )_ `. `|
              )_ `.` /
             )_ `-.` |
            )_ `-.` ` '
             )_.- ` `  '
              )_.-` `   '
               )_.-`\ /\ '
                )_.-| \O  '
                    |  \   'l
          _        /   /    \        _left
         ) `-._   / /O\  /O\ \   _.-` (
        )      `-/  `-'  `-'  \-`      (
        )     _.-|    __      |-._     (
         )_.-`   \ .-'  `-._  /   `-._(
                  \ `-.__.--`/
                   `-._  _.-"
                       ``
    ''')
    print("Attacked by a fish monster. Game over.")
else:
  print('''
                                       _.-'
                                 _.-'
                 _____________.-'________________
                /         _.-' O                /|
               /  i====_======O      __________/ /
              /  / _.-'      O      /     _   /|/
             /  / | p       o      /     (   / /
            /  /           O      /_________/ /
           /  L===========O                /|/
          /______________O________________/ /
         |________________________________|/
  ''')
  print("Fall into a trap hole. Game Over.")



#The FlowChart for the program : https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
