from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)
print(random_number)


@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route("/<int:number>")
def guess(number):
    if number > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbHZya2syY2pubmw0NnBldzB4NnRpOHk0azRibWk3Yjl5dHRjb25uMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1HKaikaFqDt7i/giphy.gif'/>"
    elif number < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWxxY2NsdmgwdmxrcWJwMjVwcXpvcjdkZmUxNmVsbDFrM3g5eTBzbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/nR4L10XlJcSeQ/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDdnenliaTE4MDJwbWNnZmw1MHQwMmxrY2J0cmpnbDJwMGRtY2pkNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vFKqnCdLPNOKc/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
