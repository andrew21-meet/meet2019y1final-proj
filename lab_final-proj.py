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
import turtle
import Tkinter
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
turtle.register_shape("plastic trash.gif")
turtle.register_shape("recycling factory.gif")
turtle.register_shape("sea.gif")

car = turtle.clone ()
car.shape("car.gif")
car.penup()
car.hideturtle()
car.goto(-600, -100)

elec_car = turtle.clone()
elec_car.shape("electric car.gif")
elec_car.penup()
elec_car.hideturtle()
elec_car.goto(-600, -100)


cow = turtle.clone()
cow.shape("cow.gif")
cow.penup()
cow.hideturtle()
cow.goto(-300, -100)

farting_cow = turtle.clone()
farting_cow.shape("cow-farting.gif")
farting_cow.penup()
farting_cow.hideturtle()
farting_cow.goto(-300, -100)

factory = turtle.clone()
factory.shape("factory.gif")
factory.penup()
factory.hideturtle()
factory.goto(0, -100)

refactory = turtle.clone()
refactory.shape("recycling factory.gif")
refactory.penup()
refactory.hideturtle()
refactory.goto(0, -100)

fire = turtle.clone()
fire.shape("fire.gif")
fire.penup()
fire.hideturtle()
fire.goto(300, -100)

flowers = turtle.clone()
flowers.shape("flowers.gif")
flowers.penup()
flowers.hideturtle()
flowers.goto(300, -100)

sea = turtle.clone()
sea.shape("sea.gif")
sea.penup()
sea.hideturtle()
sea.goto(600, -100)

trash = turtle.clone()
trash.shape("plastic trash.gif")
trash.penup()
trash.hideturtle()
trash.goto(600, -100)


null = turtle.clone()
null.penup()
null.hideturtle()
null.goto(1000,1000)

                    















class Question:
     def __init__(self, prompt, answer, turtle_shape, bad_turtle):
          self.prompt = prompt
          self.answer = answer
          self.turtle_shape = turtle_shape
          self.bad_turtle = bad_turtle
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
     

     


]
questions = [
     Question(question_prompts[0], "a", elec_car, car),
     Question(question_prompts[1], "b", cow, farting_cow),
     Question(question_prompts[2], "d", refactory, factory),
     Question(question_prompts[3], "a", flowers, fire),
     Question(question_prompts[4], "c", sea, trash),
     Question(question_prompts[5], "d", null, null),
     Question(question_prompts[6], "a", null, null),
     Question(question_prompts[7], "b", null, null),
     Question(question_prompts[8], "c", null, null),
     Question(question_prompts[9], "b", null, null),
     
]

def run_quiz(questions):
    print("\n")
    for question in questions:
            
          answer = input(question.prompt)
          if answer == question.answer:
            print("the answer is correct!")
            question.turtle_shape.showturtle()
          else:
            print("the answer is incorrect..")
            print("the right answer is " + question.answer)
            question.bad_turtle.showturtle()
            
            


run_quiz(questions)





    





