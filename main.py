from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

# Screen setup
def setup_screen():
    sc = Screen()
    sc.setup(width=600, height=600)
    sc.bgcolor("black")
    sc.title("Snake Game")
    sc.tracer(0)
    return sc

def restart_game():
    return sc.textinput(title="Snake Game", prompt="Would you like to play again? (y/n)").lower()

sc = setup_screen()
snake = Snake()
food = Food()
score = Score()

sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.right, "Right")
sc.onkey(snake.left, "Left")

condition = True
n = 0
score.count(n)

# Main game loop
while condition:
    sc.update()
    time.sleep(0.1)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        n += 1
        score.count(n)
        snake.extend()

    # Collision with wall
    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        score.gameover()
        if restart_game() == 'y':
            snake.reset()
            food.refresh()
            score.reset()
            n = 0
        else:
            condition = False

    # Collision with self
    for segment in snake.lis_tur[1:]:
        if snake.head.distance(segment) < 10:
            score.gameover()
            if restart_game() == 'y':
                snake.reset()
                food.refresh()
                score.reset()
                n = 0
            else:
                condition = False

sc.exitonclick()
