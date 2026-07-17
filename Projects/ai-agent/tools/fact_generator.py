import random

facts = [

    "Python was created by Guido van Rossum in 1991.",

    "Artificial Intelligence can automate repetitive tasks.",

    "Machine Learning is a subset of AI.",

    "The first AI program was developed in the 1950s.",

    "Large Language Models are trained on massive text datasets."

]

def random_fact():
    return random.choice(facts)