import turtle 
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = turtle.Screen()
screen.setup(width=600,height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
sb = ScoreBoard()


def restartgame():
    sb.resetc()
    snake.resetc()
    return True


game_is_on = True

#moving snake by getting segment to pos of segment on front

while game_is_on:
    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")
    screen.update()
    time.sleep(0.2-(0.001*sb.score))
    snake.move()

    if(snake.head.distance(food)<15):
        snake.extend()
        food.refresh()
        sb.increase()
    if(snake.head.xcor() > 290 or snake.head.xcor() < -300 or  snake.head.ycor() > 266 or  snake.head.ycor() < -290 ):
        game_is_on = False
        sb.game_over()
        again = screen.textinput("GAME OVER","Enter 's' to start again ")
        if(again=='s' or again=='S'):
            game_is_on = restartgame()
        elif(again == ''):
                quit()
        else:
            quit()

        
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on = False
            sb.game_over()
            again = screen.textinput("GAME OVER","Enter 's' to start again ")
            if(again=='s' or again=='S'):
                game_is_on = restartgame()
            elif(again == ''):
                quit()
            else:
                quit()
            

screen.exitonclick()