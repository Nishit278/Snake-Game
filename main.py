from turtle import Screen
import time
from scoreboard import Scoreboard 
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0) #screen is not going to refresh until we use update
screen.title("Snake")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

def hit_wall(x,y):
    return (x > 280 or x < -280 or y > 280 or y < -280)

while(game_is_on):
    screen.update() #updates the screen after all segments have moved
    time.sleep(0.1) #slows down the animation of moving 
    snake.move_snake()
#Detect collision with food 
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extent()
        scoreboard.inc_score()
#Detect collision with wall 
    if hit_wall(snake.head.xcor(), snake.head.ycor()):
        game_is_on = False        
        scoreboard.game_over()
#Detect collision with tail 
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on=False
            scoreboard.game_over()




screen.exitonclick()
