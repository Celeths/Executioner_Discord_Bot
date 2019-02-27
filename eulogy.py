from random import *

# First sentence setup
opener = ["Today we are here ", "We would like to gather ", "We are gathered here "]
opener_second = ["to ", "in order to "]
opener_third = ["remember ", "commemorate ", "bring remembrance to ", "honor ", "recognize"]
opener_fourth = ["the life of ", "the memory of ", "the legacy of ", "the actions of ", "the spirit of "]
opener_extra = ["great", "terrible", "loving", "gay", "weak", "strong", "boring", "chaotic", "honored", "loyal",
                "cruel", "tyrannical", "compassionate", "bold", "dunce", "shitopster", "intolerable", "disliked"]

# Second sentence setup
sopener_opener_option = ["It is ", "It was ", "It was once ", "People "]
sopener_opener_option_second = ["said that ", "rumored that ", "thought that ", "known that "]
sopener = ["was ", "once was ", "used to be ", "was compelled to be ", "acted as ", "was known as ",
           "was remembered as ", "is remembered as "]
sopener_second = ["great ", "terrible ", "loving ", "gay ", "weak ", "strong ", "boring ", "chaotic ", "honored ",
                  "loyal ", "cruel ", "tyrannical ", "compassionate ", "bold ", "dunce of a ",  "shitposter ",
                  "intolerable ", "disliked "]
sopener_third = ["person", "individual", "user", "member", "friend", "ally", "stranger", "neighbor"]
sopener_extra = ["although ", "even so, ", "but ", "but perhaps ", "though maybe "]
sopener_extra_second = ["no one cares", "we should forget that", "they were much more", "that was not true",
                        "they were better than that", "we never knew them"]

# Third Sentence Setup
thopener_opener = ["While what is said, ", "That may be true, yet ", "Even so, ", "Yet still "]
thopener_opener_second = ["still committed the ", "did commit ", "did act out ", "pulled "]
thopener_opener_third = ["terrible ", "saddening ", "misguided ", "cruel ", "evil ", "villainous ", "heinous ",
                         "wrongful ", "low ", "disturbing "]
thopener_opener_fourth = ["acts ", "actions ", "behavior ", "choices ", "decisions ", "offence "]
thopener_opener_fifth = ["that led to the ", "that resulted in ", "which resulted in ", "which led to the ",
                         "that required the ", "which require the "]

# Fourth Sentence Setup
fopener = ["Today we ", "Now we "]
fopener_second = ["witness the ", "gather round for the ", "watch the ", "are touched by the ", "don't care for the "]
fopener_third_negative = ["so let us not ", "so we shall not ", "so we shant ", "yet not let us ", "but not let us "]
fopener_third_positive = ["so let us ", "so we shall ", "but let us ", "yet let us "]
fopener_fourth = ["remember ", "forget "]
fopener_fifth = ["for their ", "by their ", "as their "]
fopener_fifth_negative_extra = ["but for their", "but by their ", "but as their "]
fopener_sixth = ["best ", "most notable ", "greatest ", "potential ", "memorable ", "usual "]



def rememberence(name, action):
    # Action Setup
    if action == "ban":
        action = "banning"
    elif action == "kick":
        action = "kicking"
    elif action == "execute":
        action = "executioning"
    elif action == "remember":
        action = "death"
    else:
        action = "muting"
    # FIRST SENTENCE    -----
    eulogy = ""
    eulogy += choice(opener) + choice(opener_second) + choice(opener_third)
    # adding option for opener_fourth to recall the action (33% likely to recall)
    choice_picker = randint(1,3)
    if choice_picker < 2:
        eulogy += "the " + action + " of "
    else:
        eulogy += choice(opener_fourth)
    # deciding whether to add a title (66% likely to add)
    choice_picker = randint(1,3)
    if choice_picker < 3:
        # Rewrites the name to include the title
        name += " the " + choice(opener_extra)
    # adding the users name to the sentance
    eulogy += name
    # adding period and space to the end of the sentence
    eulogy += ".\n\n"

    # SECOND SENTENCE
    # deciding whether to add opener before name (chance to is 40%)
    choice_picker = randint(1,5)
    if choice_picker < 3:
        eulogy += choice(sopener_opener_option) + choice(sopener_opener_option_second)
    eulogy += name + " "
    # finishing second sentence
    eulogy += choice(sopener) + "a " + choice(sopener_second) + choice(sopener_third)
    # deciding whether to add onto first sentence (33% chance)
    choice_picker = randint(1,3)
    if choice_picker < 2:
        eulogy += ", " + choice(sopener_extra) + choice(sopener_extra_second) + ".\n\n"
    else:
        eulogy += ".\n\n"

    #THIRD SENTENCE
    # deciding whether to add third sentence option (70% likely to add)
    choice_picker = randint(1,10)
    if choice_picker < 8:
        eulogy += choice(thopener_opener) + name + " " + choice(thopener_opener_second) + \
                  choice(thopener_opener_third) + choice(thopener_opener_fourth) + \
        choice(thopener_opener_fifth) + action + ".\n\n"

    #FOURTH SENTENCE
    eulogy += choice(fopener) + choice(fopener_second) + action + " of " + name + ", "
    # deciding whether to chose denying of character (chance to deny is 50%)
    choice_picker = randint(1,2)
    if choice_picker < 2:
        eulogy += choice(fopener_third_positive) + choice(fopener_fourth) + name + " " + choice(fopener_fifth) + choice(
            fopener_sixth) + choice(thopener_opener_fourth)[:-1] + "."
    else:
        eulogy += choice(fopener_third_negative) + choice(fopener_fourth) + name + " " + choice(fopener_fifth) + choice(
            thopener_opener_fourth) + choice(fopener_fifth_negative_extra) + choice(fopener_sixth) + choice(
            thopener_opener_fourth)[:-1] + "."

    return eulogy