from turtle import Turtle

FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.up()
        self.goto(x= 0,y=270)
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.write(arg=f"Score: {self.score}", align="center",font=FONT)
        
    
    def update_scoreboard(self):
        self.write(arg=f"score: {self.score}", align="center",font=FONT)

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", align="center",font=FONT)
