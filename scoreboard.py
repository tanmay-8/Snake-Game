from turtle import Turtle
file = r"D:\CODING\Python Projects\Games\snakegame\highscore.txt"
ALIGNMENT = "center"
FONT = ("Courier",24,"normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        
        with open(file ) as data:
            line = int(data.read())

        self.highscore = line
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.write(f"SCORE:{self.score} HIGH SCORE:{self.highscore}",move=False,align=ALIGNMENT,font=FONT)
        self.write("------------------------------------------------------------------------------------------",align=ALIGNMENT)
    
    def update(self):
        self.clear()
        self.write(f"SCORE:{self.score} HIGH SCORE:{self.highscore}",move=False,align=ALIGNMENT,font=FONT)
        self.write("------------------------------------------------------------------------------------------",align=ALIGNMENT)

    def increase(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over.",move=False,align=ALIGNMENT,font=("Courier",20,"normal"))

    def resetc(self):
        self.goto(0,260)
        if self.score > self.highscore:
            self.highscore = self.score
            with open(file,mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update()
        