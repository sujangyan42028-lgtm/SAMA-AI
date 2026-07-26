EMOTIONS = {

    "sad": [
        "i am sad",
        "i feel sad",
        "i'm sad",
        "feeling sad"
    ],

    "happy": [
        "i am happy",
        "i feel happy",
        "i'm happy",
        "feeling happy"
    ],

    "angry": [
        "i am angry",
        "i'm angry",
        "i feel angry"
    ],

    "tired": [
        "i am tired",
        "i'm tired",
        "i feel tired"
    ],

    "excited": [
        "i am excited",
        "i'm excited",
        "i feel excited"
    ]
}


RESPONSES = {

    "sad":
    "I'm sorry you're feeling sad. Don't worry, I'm here with you.",

    "happy":
    "That's wonderful! I'm happy to hear that.",

    "angry":
    "Take your time. Try to stay calm. Everything will be alright.",

    "tired":
    "You should get some rest. Your health is important.",

    "excited":
    "That's amazing! I hope everything goes well."
}


def handle(user):

    user = user.lower()

    for emotion in EMOTIONS:

        for sentence in EMOTIONS[emotion]:

            if sentence in user:

                return RESPONSES[emotion]

    return None