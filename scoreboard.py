from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 16, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.score()

    def score(self):
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.write_it()

    def write_it(self):
        self.clear()
        self.write(f"Score: {self.current_score}  High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.current_score = 0
        self.write_it()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.current_score += 1
        self.write_it()
