#sprite = codesters.Arrow(x-start, y-start, x-end, y-end, double_headed)
stage.set_background("summer")

arrowURL = "http://www.pngall.com/wp-content/uploads/2016/07/Arrow-Free-Download-PNG.png"

arrowSprite = codesters.Sprite(arrowURL)
arrowSprite.go_to(0, -210)
arrowSprite.set_size(0.5)
arrowSprite.set_rotation(90)
# sprite = codesters.Rectangle(x, y, width, height, "color")
sprite = codesters.Rectangle(0, 240, 1000, 50, "blue")

Moving = False
shot_count = 0
game_over = False
row = 3
columns = 19
colosr = ["Blue", "green", "Yellow", "Red"]
bubbles = []

def reset_ball():
    circle = codesters.Circle(0, 240, 1000, 50)
    circle.go_to(0, 240)
    random.choice(colors)