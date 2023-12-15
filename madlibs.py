"""A madlib game that compliments its users."""

from random import sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = sample(AWESOMENESS,3)
    compliment_len = len(compliment)

    return render_template("compliment.html", person=player, compliment=compliment, compliment_len=compliment_len)


@app.route("/game")
def show_madlib_form():
    """Display madbil form"""

    player_answer = request.args.get("play-game")

    if player_answer == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")
    
@app.route("/madlib")
def show_madlib():
    """Display user madlib"""


    verb1 = request.args.get("verb1")
    person1 = request.args.get("person1")
    noun1 = request.args.get("noun1")
    person2 = request.args.get("person2")
    noun2 = request.args.get("noun2")
    noun3 = request.args.get("lang-noun")
    room = request.args.getlist("house-room")
    person3 = request.args.get("person3")
    food = request.args.get("food")
    adjective1 = request.args.get("adjective1")
    adjective2 = request.args.get("adjective2")
    adjective3 = request.args.get("adjective3")
    scent = request.args.get("scent")
    verb2 = request.args.get("verb2")
    noun4 = request.args.get("noun4")
    noun5 = request.args.get("noun5-lang")
    person4 = request.args.get("person4")
    transport = request.args.get("transport")
    animal = request.args.get("animal")
    adjective4 = request.args.get("adjective4")

    templates = ["madlib.html", "madlib1.html"]

    template_choose = choice(templates)
    print(template_choose)


    return render_template(template_choose, verb1=verb1,
                        person1=person1,
                        noun1=noun1,
                        person2=person2,
                        noun2=noun2,
                        noun3=noun3,
                        room=room,
                        person3=person3,
                        food=food,
                        adjective1=adjective1,
                        adjective2=adjective2,
                        adjective3=adjective3,
                        scent=scent,
                        verb2=verb2,
                        noun4=noun4,
                        noun5=noun5,
                        person4=person4,
                        transport=transport,
                        animal=animal,
                        adjective4=adjective4               
                        )


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
