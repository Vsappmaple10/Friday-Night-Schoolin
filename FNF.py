#make click function --- DONE
#make background --- DONE
#steps --- DONE
#function to repeat --- DONE
###
#recreate friday night funkin controls and s
#implement music into controls
#make graphic music arrows for the beat
##- Library -##

import tsapp
import tkinter

##- Window -##

window = tsapp.GraphicsWindow()

##- Background -##

background = tsapp.Sprite("Frame.jpg", 0, 0)
window.add_object(background)

##- Sprites -##

sprite_list = ["Boulder.png", "BoulderDance2.png", "BoulderJoy.png", "BoulderMad.png", "BoulderRun.png"]
boulder = tsapp.Sprite("Boulder.png", 150, 200)
window.add_object(boulder)
speech_bubble = tsapp.Sprite("SpeechBubble.png", 225, 40)
window.add_object(speech_bubble)

##- Text -##
intro = tsapp.TextLabel("CaveatBrush-Regular.ttf", 40, 275, 120, 200, "Click for more progress!", tsapp.BLACK)
window.add_object(intro)
##- Function -##

def click():
    x = 1
    while window.is_running:
         
        if x < 26:
            if tsapp.was_mouse_pressed():
                print("click if you love pancakes!")
                
                x += 1
        elif x < 52:
            if tsapp.was_mouse_pressed():
                print("wow you really love pancakes")
                x += 1
        else:
            print("you have achieved pancake mastery")
            window.finish_frame()
            break
        if tsapp.was_mouse_pressed():
            if boulder.image == "Boulder.png":
                boulder.image = "BoulderDance2.png"
            elif boulder.image == "BoulderDance2.png":
                boulder.image = "BoulderJoy.png"
            elif boulder.image == "BoulderJoy.png":
                boulder.image = "BoulderMad.png"
            elif boulder.image == "BoulderMad.png":
                boulder.image = "BoulderRun.png"
            elif boulder.image == "BoulderRun.png":
                boulder.image = "BoulderDance2.png"
        else:
            boulder.image == "Boulder.png"
        window.finish_frame()
