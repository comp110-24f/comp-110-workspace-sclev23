"""Blackjack experiments."""

import random


def spadesPile() -> list[int]:
    idx: int = 1
    slist: list[int] = []
    while idx <= 13:
        slist.append(idx)
        idx += 1
    return slist


def clubsPile() -> list[int]:
    idx: int = 1
    clist: list[int] = []
    while idx <= 13:
        clist.append(idx)
        idx += 1
    return clist


def heartsPile() -> list[int]:
    idx: int = 1
    hlist: list[int] = []
    while idx <= 13:
        hlist.append(idx)
        idx += 1
    return hlist


def diamondsPile() -> list[int]:
    idx: int = 1
    dlist: list[int] = []
    while idx <= 13:
        dlist.append(idx)
        idx += 1
    return dlist


spades: list[int] = spadesPile()
clubs: list[int] = clubsPile()
hearts: list[int] = heartsPile()
diamonds: list[int] = diamondsPile()


def drawPile(s: list[int], c: list[int], h: list[int], d: list[int]) -> int:
    draw: int = 0
    rand: int = random.randint(1, 4)
    if rand == 1:
        draw = random.randint(1, len(s))
        if draw == 1:
            print("Ace of Spades")
        elif draw == 11:
            print("Jack of Spades")
        elif draw == 12:
            print("Queen of Spades")
        elif draw == 13:
            print("King of Spades")
        else:
            print(f"{draw} of Spades")
        if draw > 10:
            draw = 10
        return draw
    elif rand == 2:
        draw = random.randint(1, len(c))
        if draw == 1:
            print("Ace of Clubs")
        elif draw == 11:
            print("Jack of Clubs")
        elif draw == 12:
            print("Queen of Clubs")
        elif draw == 13:
            print("King of Clubs")
        else:
            print(f"{draw} of Clubs")
        return draw
    elif rand == 3:
        draw = random.randint(1, len(h))
        if draw == 1:
            print("Ace of Hearts")
        elif draw == 11:
            print("Jack of Hearts")
        elif draw == 12:
            print("Queen of Hearts")
        elif draw == 13:
            print("King of Hearts")
        else:
            print(f"{draw} of Hearts")
        return draw
    else:
        draw = random.randint(1, len(d))
        if draw == 1:
            print("Ace of Diamonds")
        elif draw == 11:
            print("Jack of Diamonds")
        elif draw == 12:
            print("Queen of Diamonds")
        elif draw == 13:
            print("King of Diamonds")
        else:
            print(f"{draw} of Diamonds")
        return draw


def fSum(list: list[int]):
    sum: int = 0
    for i in list:
        sum += i
    return sum


def turn(s, c, h, d) -> int:
    print("=== Your Hand ===")
    bust: bool = False
    hand: list[int] = []
    hand.append(drawPile(s, c, h, d))
    hand.append(drawPile(s, c, h, d))
    while bust is False:
        print(f"Total: {fSum(hand)}")
        if fSum(hand) < 21:
            hors: str = input("Hit or Stand: ")
            if hors == "Hit":
                hand.append(drawPile(s, c, h, d))
            elif hors == "Stand":
                return fSum(hand)
            else:
                print("Try Again!")
        elif fSum(hand) > 21:
            bust = True
            print("Bust!")
            return 100
        else:
            return fSum(hand)


def dealer(s, c, h, d) -> int:
    print("=== Dealer Hand ===")
    hand: list[int] = []
    hand.append(drawPile(s, c, h, d))
    hand.append(drawPile(s, c, h, d))
    print(f"Total: {fSum(hand)}")
    return fSum(hand)


def play(s, c, h, d) -> int:
    bust: bool = False
    hand: list[int] = []
    dresult: int = dealer(s, c, h, d)
    dresult2: int = 0
    presult: int = turn(s, c, h, d)
    print("=== Dealer Hand ===")
    if dresult > 21:
        bust = True
        dresult2 = 100
    while bust is False:
        print(f"Total: {fSum(hand) + dresult}")
        if fSum(hand) + dresult < 17:
            hand.append(drawPile(s, c, h, d))
        elif fSum(hand) + dresult > 21:
            bust = True
            print("Dealer Bust!")
            dresult2 = 100
        else:
            dresult2 = fSum(hand) + dresult
            bust = True
    if presult == 100 or dresult2 == 100:
        if presult == 100 and dresult2 == 100:
            print("Push!")
            return 2
        elif presult == 100 and dresult2 != 100:
            print("Dealer Wins, You, Lose!")
            return 0
        elif presult != 100 and dresult2 == 100:
            print("You Win, Dealer Busts!")
            return 1
    elif presult > dresult2:
        print("You Win!")
        return 1
    elif presult < dresult2:
        print("Dealer Wins, You Lose!")
        return 0
    else:
        print("Push!")
        return 2
    print("Something went wrong...")
    return 0


def menu(s, c, h, d) -> None:
    credits: int = 100
    print("=-=-=-=-= Welcome to Blackjack =-=-=-=-=")
    playing: bool = True
    while playing is True:
        bet: int = 0
        win: int = 3
        print("=-=-=  What would you like to do?  =-=-=")
        print(f"Credits: {credits}")
        response: str = input("Play or Quit? ")
        if response == "Play":
            bet = int(input("Place your bet: "))
            if bet > credits:
                print("Too many credits!")
            elif bet == 0:
                print("You can't bet nothing!")
            else:
                credits -= bet
                win = play(s, c, h, d)
                if win == 0:
                    credits = credits
                elif win == 1:
                    credits += bet * 2
                elif win == 2:
                    credits += bet
        elif response == "Quit":
            exit()
        else:
            print("Try Again!")


menu(spades, clubs, hearts, diamonds)
