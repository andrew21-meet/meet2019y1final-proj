#Hangman Trivia!!

#make variables for
#[questions]
#right_answer
#wrong_answers
#bad_pictures
#good_pictures
#name
#
#


#register all graphics and pictures


#ask user to input name

#welcome the user to hang man

#do the following 5 times

    #ask user question

    #show answers

    #take answers
        #if right
            #add  1 good_picture to the drawing
        #else
            #add 1  bad_picture to the drawing

#if loses more the wins
    #print you lose
#else wins more then loses
    #print you win

#congratulate if user wins
#dont congratulate if user loses
import pygame

import turtle

pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.init() #turn all of pygame on.


# pictures

turtle.bgcolor("green")
screen = turtle.Screen()
screen.setup(1500, 1000)
turtle.register_shape("car.gif")
turtle.register_shape("cow.gif")
turtle.register_shape("electric car.gif")
turtle.register_shape("factory.gif")
turtle.register_shape("cow-farting.gif")
turtle.register_shape("fire.gif")
turtle.register_shape("flowers.gif")
turtle.register_shape("6 trash images.gif")
turtle.register_shape("recycling factory.gif")
turtle.register_shape("6 sea.gif")

car = turtle.clone ()
car.shape("car.gif")
car.penup()
car.hideturtle()
car.goto(-600, -200)

elec_car = turtle.clone()
elec_car.shape("electric car.gif")
elec_car.penup()
elec_car.hideturtle()
elec_car.goto(-600, -200)
car_s=pygame.mixer.Sound("Car Engine Sound Effect.wav")

cow = turtle.clone()
cow.shape("cow.gif")
cow.penup()
cow.hideturtle()
cow.goto(-300, -200)
cow_s=pygame.mixer.Sound("Moo! Sound Effect [COW].wav")

farting_cow = turtle.clone()
farting_cow.shape("cow-farting.gif")
farting_cow.penup()
farting_cow.hideturtle()
farting_cow.goto(-300, -200)
f_cow_s=pygame.mixer.Sound("Fart sound effect.wav")

factory = turtle.clone()
factory.shape("factory.gif")
factory.penup()
factory.hideturtle()
factory.goto(0, -200)
factory_s=pygame.mixer.Sound("factory.wav")


refactory = turtle.clone()
refactory.shape("recycling factory.gif")
refactory.penup()
refactory.hideturtle()
refactory.goto(0, -200)

fire = turtle.clone()
fire.shape("fire.gif")
fire.penup()
fire.hideturtle()
fire.goto(500, -200)
fire_s=pygame.mixer.Sound("FIRE SOUND EFFECT IN HIGH QUALITY.wav")

flowers = turtle.clone()
flowers.shape("flowers.gif")
flowers.penup()
flowers.hideturtle()
flowers.goto(400, -200)
flowers_s=pygame.mixer.Sound("Bird Sound Effect.wav")

sea = turtle.clone()
sea.shape("6 sea.gif")
sea.penup()
sea.hideturtle()
sea.goto(0, -400)
sea_s=pygame.mixer.Sound("OCEAN SOUND EFFECT [HD].wav")

trash = turtle.clone()
trash.shape("6 trash images.gif")
trash.penup()
trash.hideturtle()
trash.goto(0, -400)


null = turtle.clone()
null.penup()
null.hideturtle()
null.goto(1000,1000)
c_answer_s=pygame.mixer.Sound("Correct-answer.wav")
w_answer_s=pygame.mixer.Sound("Wrong-answer-sound-effect.wav")


# sounds

def car_s_f():
     pygame.mixer.Sound.play(car_s)

def cow_s_f():
     pygame.mixer.Sound.play(cow_s)

def f_cow_s_f():
     pygame.mixer.Sound.play(f_cow_s)

def factory_s_f():
     pygame.mixer.Sound.play(factory_s)

def flowers_s_f():
     pygame.mixer.Sound.play(flowers_s)

def fire_s_f():
     pygame.mixer.Sound.play(fire_s)

def sea_s_f():
     pygame.mixer.Sound.play(sea_s)








# what the question has
class Question:
     def __init__(self, prompt, answer, turtle_shape, bad_turtle, sound, b_sound):
          self.prompt = prompt
          self.answer = answer
          self.turtle_shape = turtle_shape
          self.bad_turtle = bad_turtle
          self.sound=sound
          self.b_sound=b_sound



     def p_g_sound(self):
           pygame.mixer.Sound.play(self.sound)

     def p_b_sound(self):
           pygame.mixer.Sound.play(self.b_sound)
          #questions,options of answers, \n = linebreaker
question_prompts = [
     "\nwhich country has the most pollution?\n(a) China\n(b) Brazil\n(c) United States\n(d) Indonesia\n",
     "\nHow many years of oil is left in the world?\n(a) 101 years\n(b) 53 years\n(c) 20 years\n(d) 69 years\n",
     "\nHow much oil is left in the world?\n(a) 6.003 trillion barrels\n(b) 3.775 trillion barrels\n(c) 0.804 trillion barrels\n(d) 1.688 trillion barrels\n",
     "\nWho is the biggest oil producer in the world?\n(a) Saudi Arabia\n(b) USA\n(c) Russia\n(d) China\n",
     "\nHow many years of gas are left in the world?\n(a)200 years\n(b) 86 years\n(c) 115 years\n(d)98 years\n",
     "\nwhat is the easiest plastic code to recycle?\n(a) 3\n(b) 6\n(c) 7\n(d) 1\n",
     "\nWhat is cutting of trees called?\n(a) hewing\n(b) cutzing\n(c) CTs\n(d) falling\n",
     "\nWhat is the largest oil company in Canada?\n(a)Encana Corporation\(b)Suncor Energy\n(c)Husky Energy\n(d)Enbridge\n",
     "\nWhat is the largest oil company in Canada?\n(a)water\n(b)sand\n(c)dust\n(d)stones\n",
     "\nWhat is the top cause of air pollution?\n(a)Emission from Vehicles\n(b)Poisonous Gas\n(c)Combustion of Fossil Fuels\n(d)Pollution From AC\n",
     


#right answers 
]
questions = [
     Question(question_prompts[0], "a", refactory, factory, factory_s , factory_s),
     Question(question_prompts[1], "b", elec_car, car, car_s, car_s),
     Question(question_prompts[2], "d", cow, farting_cow, cow_s,f_cow_s),
     Question(question_prompts[3], "a", flowers, fire, flowers_s, fire_s),
     Question(question_prompts[4], "c", sea, trash,sea_s, sea_s),
     Question(question_prompts[5], "d", null, null, c_answer_s, w_answer_s),
     Question(question_prompts[6], "a", null, null, c_answer_s, w_answer_s),
     Question(question_prompts[7], "b", null, null, c_answer_s, w_answer_s),
     Question(question_prompts[8], "c", null, null, c_answer_s, w_answer_s),
     Question(question_prompts[9], "b", null, null, c_answer_s, w_answer_s),
     
]
#loop, if the answer is right or wrong and print the line

def run_quiz(questions):
    print("\n")
    for question in questions:
            
          answer = input(question.prompt)
          if answer == question.answer:
            print("the answer is correct!")
            question.turtle_shape.showturtle()
            pygame.mixer.music.stop()
            question.p_g_sound()

          else:
            print("the answer is incorrect..")
            print("the right answer is " + question.answer)
            question.bad_turtle.showturtle()
            pygame.mixer.music.stop()
            question.p_b_sound()

            
            


run_quiz(questions)





    








