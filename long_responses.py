
import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_EMERGENCY = "I will call 911 immediately!"
R_HOMEWORK = "I'm sorry I can't help you on that but if you do need help I suggest you to surf sites like Brainly, Vedantu etc."

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response