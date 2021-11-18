import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def dealing():
    """Randomly gives dealer and player 2 cards each"""
    for i in range(2):
        game_dict["dealer"].append(cards[random.randint(0, len(cards) - 1)])
        game_dict["player"].append(cards[random.randint(0, len(cards) - 1)])


def real_cards(cards):
    suit = ["c", "d", "s", "h"]
    face = ["T", "J", "Q", "K"]
    r_cards = []
    for i in cards:
        if i == 11 or i == 1:
            r_cards.append("A" + suit[random.randint(0, 3)])
        elif i == 10:
            r_cards.append(face[random.randint(0, 3)] + suit[random.randint(0, 3)])
        else:
            r_cards.append(str(i) + suit[random.randint(0, 3)])
    return r_cards


def sum_cards(list_cards):
    """a is sum of cards"""
    c = list_cards
    a = sum(c)
    while 11 in c and a > 21:
        c[c.index(11)] = 1
        a = sum(c)
    return a


def hit(dict_key):
    """When hit is called providing a key - player/dealer - adds a card acordingly"""
    # TODO return a new updated dict
    game_dict[dict_key].append(cards[random.randint(0, len(cards) - 1)])
    print("Card was added")


def dealer(i):
    card_sum = sum_cards(i)
    while sum_cards(i) < 16:
        print("Sum bellow 16 HITTING")
        hit("dealer")
        print(real_cards(i))
        card_sum = sum_cards(i)
    return card_sum


global game_dict
game_dict = {"dealer": [],
             "player": []}


def play_again():
    finished = input("Do you wish to play again? Y/N: ").lower()

    if finished == 'y':
        game_dict["player"] = []
        game_dict["dealer"] = []
        game()


def game():
    dealing()

    p_cards = game_dict["player"]
    d_cards = game_dict["dealer"]

    real_p_cards = real_cards(p_cards)
    real_d_cards = real_cards(d_cards)

    print(f"Your cards: {real_p_cards[0]} {real_p_cards[1]}\nDealer cards: {real_d_cards[0]} X")

    if sum_cards(p_cards) > 21:
        finished = input("You have more then 21,You lose! Do you wish to play again? Y/N: ").lower()

        if finished == 'y':
            game_dict["player"] = []
            game_dict["dealer"] = []
            game()

    hitting = True
    while hitting:
        if sum_cards(p_cards) > 20:
            if sum_cards(p_cards) == 21:
                print("You have 21, wait for dealer to draw!")
                hitting = False
            else:
                print(f"You lost with {sum_cards(p_cards)}")
                play_again()
                hitting = False

        else:
            print(f"Your cards {real_p_cards}")
            hit_stand = input(f"You have {sum_cards(p_cards)}, HIT or STAND?: ").lower()
        if hit_stand == "hit":
            hit("player")
        else:
            hitting = False
    print(f"Dealer reveals {real_d_cards}")
    dealer_score = dealer(d_cards)

    if sum_cards(p_cards) < dealer_score < 22:
        print(f"You have {sum_cards(p_cards)}, Dealer has {dealer(d_cards)}. You lose!")
    elif dealer_score < sum_cards(p_cards) or dealer_score > 21:
        print(f"You have {sum_cards(p_cards)}, Dealer has {dealer(d_cards)}. You Win!")
    else:
        print(f"You have {sum_cards(p_cards)}, Dealer has {dealer(d_cards)}. It\'s a draw!")
    play_again()


game()
