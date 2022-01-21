from itertools import product
import random
from ascii_art import ascii_card, ascii_hidden_card, ascii_logo

class Card(object):

    card_values = {
        'Ace': 11,  # value of the ace is high until it needs to be low
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10
    }

    def __init__(self, suit, rank):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param rank: The value of the card, e.g 3 or King
        """
        self.suit = suit.capitalize()
        self.rank = rank
        self.points = self.card_values[rank]

class Player(object):
    
    def add_card(self, card):
        self.cards_on_hand.append(card)
        
        self.points = sum([card.points for card in self.cards_on_hand])
        
        if self.points > 21:  # if you are about to loose re-evaluate aces 
            aces_count = [card.rank for card in self.cards_on_hand].count('Ace')
            self.points -= 10 * aces_count
    
    def dealer_points(self):
        if len(self.cards_on_hand) > 1:
            return sum([card.points for card in self.cards_on_hand[1:]])
        else: 
            return 0
    
    def __init__(self,points,cards_on_hand):
        self.points = 0
        self.cards_on_hand = []



def deck_shuffled(shuffle=True):
    
    ranks = [str(card_num) for card_num in range(2,10)] + ['Jack','Queen','King','Ace']
    cards = list(product(['Spades','Hearts','Diamonds','Clubs'], ranks)) 
    deck = []
    
    for card in cards:
        deck.append(Card(card[0],card[1]))
        
    if shuffle:
        random.shuffle(deck)
    
    return deck

def game_loop(deck):
    # print(list(test_deck[i].rank for i in range(4)))
    # print(ascii_card(*[test_deck[i] for i in range(4)]))
    # print(ascii_hidden_card(*[test_deck[i] for i in range(4)]))

    player = Player(0,[])
    dealer = Player(0,[])
    player_turn = True
    dealer_turn = True
    next_card_index = 4
    bust = False
    
    for i in [0,2]:
        dealer.add_card(deck[i])
        player.add_card(deck[i+1])
    
    while player_turn:
        print('Dealer: ', dealer.dealer_points())
        print(ascii_hidden_card(*dealer.cards_on_hand))
        
        print('Player: ',player.points)
        print(ascii_card(*player.cards_on_hand))
        
        if player.points > 21: 
            bust = True
            break
        
        print('Take next card?(y/n)')
        r = input()
        if r != 'y': 
            break
        
        player.add_card(deck[next_card_index])
        next_card_index += 1

    while dealer_turn:
        print('Dealer: ', dealer.points)
        print(ascii_card(*dealer.cards_on_hand))
        
        print('Player: ',player.points)
        print(ascii_card(*player.cards_on_hand))
        
        if bust: break
        if player.points > 21: break
        if dealer.points >= player.points: break
        
        dealer.add_card(deck[next_card_index])
        next_card_index += 1
    
    if player.points == dealer.points : print("Tie! Try again!")
    elif player.points > dealer.points and bust == False: print("Nice job! You won") 
    elif dealer.points > 21 and bust == False: print("Nice job! You won") 
    else: print("You Lose!")
    
    
    
    
    
    
 
 # TEST CASES
test_card_1 = Card('Diamonds', '4')
test_card_2 = Card('Clubs', 'Ace')
test_card_3 = Card('Spades', 'Jack')
test_card_4 = Card('Hearts', '10')

test_deck = [test_card_1,test_card_2,test_card_3,test_card_4]       

def main():
    while True:
        print(ascii_logo())
        game_loop(deck_shuffled())
        print('Next round?(y/n)')
        r = input()
        if r != 'y': 
            break
    
    

if __name__ == '__main__':
    main()