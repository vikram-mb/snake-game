from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Controls
screen.listen()
screen.onkeypress(snake.up, "w")
screen.onkeypress(snake.left, "a")
screen.onkeypress(snake.down, "s")
screen.onkeypress(snake.right, "d")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.08)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.update_score()
        snake.extend()
        food.refresh()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()