from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score:{self.score}", align="center", font=("Courier", 15, "normal"))
        
    
    def update_score(self):
        self.clear()    # Clear the text first written in __init__()
        self.score += 1
        self.write(f"Score:{self.score}", align="center", font=("Courier", 15, "normal"))


    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game over! Your score: {self.score}", align="center", font=("Courier", 15, "normal"))