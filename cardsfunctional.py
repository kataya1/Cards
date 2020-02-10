import random
def suits():
    return ('♠', '♥', '♦', '♣')

def numbers():
    return ('Ace', 'King', 'Queen', 'Jack', 10, 9, 8, 7, 6, 5, 4, 3, 2)

def make_deck(suits, numbers):
    return [f'{j} {i}' for i in suits for j in numbers]

def shuffle(deck):
    for i in range(len(deck)):
        x = random.randint(0, len(deck) - 1)
        deck[i], deck[x] = deck[x], deck[i]
    return deck
    
def blackjack(players, decks):
    pass
def poker(players,decks):
    pass

def Game(players=1, deck, game='BlackJack'):
    games = {
        'BlackJack':blackjack,
        'Poker':poker

    }
    games[game](players,deck)
    

def Turn():
    pass
    
def draw(deck):
    return deck.pop()

if __name__ == "__main__":
    deck = shuffle(make_deck(suits(), numbers()))
    print(len(deck))
    print(deck)
    print(draw(deck))
    print(len(deck))


