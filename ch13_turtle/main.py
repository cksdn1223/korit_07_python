from turtle import Turtle, Screen
from random import Random

t = Turtle()

screen = Screen()
#'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'.
t.shape('turtle')
# t.color('green')
screen.bgcolor('black')
t.pencolor('green')
t.speed(0)

# 랜덤 객체 생성
random = Random()
colors = [
    'dark red',
    "peru",
    "dark khaki",
    "sea green",
    "crimson",
    "cornsilk",
    "pale violet red",
    "dark slate blue",
    "royal blue",
    "papaya whip",
    "khaki",
    "dark sea green",
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
    "tomato",
    "dark olive green",
    "mint cream",
    "sienna",
    'light yellow'
]
#'standard', 'logo' or 'world
# screen.mode('logo')

# fowward , back , right , left
# for _ in range(10):
#     t.forward(15)
#     t.penup()
#     t.forward(15)
#     t.pendown()

# for _ in range(4):
#     t.forward(100)
#     t.left(90)

# for _ in range(3):
#     t.forward(100)
#     t.left(120)

# for _ in range(5):
#     t.forward(100)
#     t.left(72)
# t.circle(100,steps=5)

# for _ in range(6):
#     t.forward(100)
#     t.left(60)
# t.circle(100,steps=6)

# n = int(input('몇각형 만들래 ? >>> '))
# for _ in range(n):
#     t.forward(100)
#     t.left(360/n)



# for i in range(3, 11):
#     for _ in range(i):
#         t.forward(100)
#         t.left(360/i)
#     t.color(random.choice(colors))

# def draw_shape(n):
#     t.color(random.choice(colors))
#     for _ in range(n):
#         t.forward(100)
#         t.left(360/n)
#
# for i in range(10, 2, -1):
#     draw_shape(i)
# def draw_dotted_line():
#     for _ in range(10):
#         t.forward(5)
#         t.penup()
#         t.forward(5)
#         t.pendown()
#
# for i in range(3, 11):
#     for _ in range(i):
#         draw_dotted_line()
#         # t.dot()
#         t.left(360/i)
#     t.color(random.choice(colors))

# t.forward(100)
# print(t.heading())
# t.left(90)
# t.forward(100)
# print(t.heading())
# t.left(30)
# t.forward(100)
# print(t.heading())
# t.right(30)
# t.forward(100)
# print(t.heading())
# t.setheading(30)
# t.forward(100)
# print(t.heading())
# .heading()의 return 값은 float
# .setheading()의 parameter가 float/return None
# t.setheading(t.heading() + 100)

# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)
# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)
# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)
# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)
# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)
# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)
# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)

# t.color(random.choice(colors))
# t.circle(100)
# 거북이 머리를 다른쪽으로 돌려서 다음 원이 겹치지 않게끔 하는 함수
# t.setheading(t.heading() + 10)


# for _ in range(36):
#     t.color(random.choice(colors))
#     t.circle(100)
#     t.setheading(t.heading() + 10)

# def draw_spirograph(size_of_gap):
#     for _ in range(360 // size_of_gap):
#         t.color(random.choice(colors))
#         t.circle(100)
#         t.setheading(t.heading() + (360/size_of_gap))
# draw_spirograph(5)
# draw_spirograph(0.5)











screen.exitonclick()