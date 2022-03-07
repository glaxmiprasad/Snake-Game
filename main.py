from turtle import Screen
from snake import Snake
from food import Food
from score import Score

import time

# lis_tur=[]

sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.title("Snake Game")
sc.tracer(0)

snake = Snake()
food = Food()
score = Score()

sc.listen()
sc.onkey(key="Up", fun=snake.up)
sc.onkey(key="Down", fun=snake.down)
sc.onkey(key="Right", fun=snake.right)
sc.onkey(key="Left", fun=snake.left)

condition = True

n = 0
c = 'n'
score.count(n)

while condition:

    sc.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        n = n + 1
        score.count(n)
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        print("GAME OVER")
        condition = False
        score.gameover()
        # c= again()

    for i in range(1, len(snake.lis_tur) - 1):

        if snake.head.distance(snake.lis_tur[i]) < 10:
            condition = False
            score.gameover()
            # c = again()

    if c == 'y':
        condition = True
        n = 0
        del snake
        snake = Snake()
        print(len(snake.lis_tur))
        c = 'p'
        # snake = snake.reset()
        # sc.clear()
        # snake=Snake()

    # cond2=True
    # while cond2:
    #     cond2 = not(food.food_collection(snake))

sc.exitonclick()

# from turtle import Screen
# from snake import Snake
# from food import Food
# from score import Score
#
# import time
#
# sc = Screen()
# snake=Snake()
# food = Food()
# score = Score()
#
# # def screen_setup(sc):
#
# sc.setup(width=600,height=600)
# sc.bgcolor("black")
# sc.title("Snake Game")
# sc.tracer(0)
# # sc.listen()
# # sc.onkey(key="Up",fun=snake.up)
# # sc.onkey(key="Down",fun=snake.down)
# # sc.onkey(key="Right",fun=snake.right)
# # sc.onkey(key="Left",fun=snake.left)
#
#
# # screen_setup(sc)
#
#
#
# sc.listen()
# sc.onkey(key="Up",fun=snake.up)
# sc.onkey(key="Down",fun=snake.down)
# sc.onkey(key="Right",fun=snake.right)
# sc.onkey(key="Left",fun=snake.left)
#
#
# condition=True
#
# n = 0
# c = 'n'
# score.count(n)
#
# def again():
#     user_c = sc.textinput(title="Snake Game",prompt="Would like to play again 'y' or 'n'?").lower()
#
#     return user_c
#
#
# while condition:
#
#     sc.update()
#     time.sleep(0.1)
#     snake.move()
#
#     if snake.head.distance(food) < 15:
#         food.refresh()
#         n = n+1
#         score.count(n)
#         snake.extend()
#
#
#
#     if (snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 290):
#         print("GAME OVER")
#         condition = False
#         score.gameover()
#         c= again()
#
#     for i in range(1,len(snake.lis_tur)-1):
#
#         if snake.head.distance(snake.lis_tur[i])<10:
#             condition = False
#             score.gameover()
#             c = again()
#
#     # if c=='y':
#     #     condition = True
#     #     n=0
#     #     del snake
#     #     del food
#     #     del score
#     #     sc.clear()
#     #     snake = Snake()
#     #     food = Food()
#     #     score = Score()
#     #     score.count(n)
#     #     screen_setup(sc)
#     #     print(len(snake.lis_tur))
#     #     c='p'
#
#
#
# sc.exitonclick()
