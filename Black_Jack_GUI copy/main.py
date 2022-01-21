from tkinter import *
from tkinter import ttk
from itertools import product
from tkinter import messagebox

import random

from position import *
import ascii_art


# Globals 
next_card_index = 4 
bust = False
game = True


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

# generate and shuffle deck of cards
def deck_shuffled(shuffle=True):
    
    ranks = [str(card_num) for card_num in range(2,10)] + ['Jack','Queen','King','Ace']
    cards = list(product(['Spades','Hearts','Diamonds','Clubs'], ranks)) 
    deck = []
    
    for card in cards:
        deck.append(Card(card[0],card[1]))
        
    if shuffle:
        random.shuffle(deck)
    
    return deck

#  let user know about the results of the game
def alert(title, message, kind='info', hidemain=True):
    if kind not in ('error', 'warning', 'info'):
        raise ValueError('Unsupported alert kind.')

    show_method = getattr(messagebox, 'show{}'.format(kind))
    show_method(title, message)

# ask if restart the game
def play_again():  
    res = messagebox.askquestion('Play again?', 
                         'Would you like to play again?')  
    
    if res == 'yes' :
        return True
    else :
        return False

# window x button should close game 
def on_closing(root):
    global game 
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        game = False
        root.destroy()

def update_player(
    root,
    player:Player,
    dealer:Player,
    deck,
    player_points_var:StringVar,
    player_hand_var:StringVar,
    dealer_points_var:StringVar,
    dealer_hand_var:StringVar,
    button_n1,
    button_n2):
    
    global next_card_index
    global bust
    
    # add card to players hand
    player.add_card(deck[next_card_index])
    
    # update next available card index
    next_card_index += 1
    
    # update Gui
    player_points_var.set('Player: ' + str(player.points))
    player_hand_var.set(ascii_art.ascii_card(*player.cards_on_hand))
    
    # check if player went above 21 points
    if player.points > 21: 
        bust = True
        update_dealer(
            root,
            player,
            dealer,
            deck,
            dealer_points_var,
            dealer_hand_var,
            button_n1,
            button_n2
            )
        
def update_dealer(
    root:Tk,
    player:Player,
    dealer:Player,
    deck,
    dealer_points_var:StringVar,
    dealer_hand_var:StringVar,
    button_n1,
    button_n2):
    
    global next_card_index
    global game 
    
    # Play dealer turn
    while True:
        if bust: break
        if player.points > 21: break
        if dealer.points >= player.points: break
        
        dealer.add_card(deck[next_card_index])
        next_card_index += 1
    
    # Update dealer widgets
    dealer_points_var.set('Dealer: ' + str(dealer.points))
    dealer_hand_var.set(ascii_art.ascii_card(*dealer.cards_on_hand))
    button_n1.config(state=DISABLED)
    button_n2.config(state=DISABLED)
    
    # Check who won the game
    if player.points == dealer.points : alert("Tie","Tie! Try again!",kind='warning')
    elif player.points > dealer.points and bust == False: alert("Won","Nice job! You won") 
    elif dealer.points > 21 and bust == False: alert("Won","Nice job! You won") 
    else: alert("Lost","You Lose!",kind='error')
    
    # Restart game
    game = play_again()
    root.destroy()
    
# main game loop
def game_loop(deck):
    global bust
    bust = False
    
    # init player and dealer objects
    player = Player(0,[])
    dealer = Player(0,[])
    
    # give first two cards to players
    for i in [0,2]:
        dealer.add_card(deck[i])
        player.add_card(deck[i+1])
        
    # declare main window
    root = Tk()
    root.title("Black Jack v0.1")
    
    style = ttk.Style()
    style.configure('Style.TButton', font='TkFixedFont')
    
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    
    # Logo Widget
    logo = ttk.Label(frm, justify=LEFT, style='Style.TButton', text=ascii_art.ascii_logo())
    
    # Dealer label text vars
    dealer_points_var  = StringVar()
    dealer_points_var.set( "Dealer: " + str(dealer.dealer_points()) )
    
    # Dealer Widgets
    dealer_hand_var = StringVar()
    dealer_hand_var.set(ascii_art.ascii_hidden_card(*dealer.cards_on_hand))
    
    dealer_points = ttk.Label(frm, justify=LEFT, style='Style.TButton', textvariable=dealer_points_var)
    dealer_hand = ttk.Label(frm, justify=LEFT, style='Style.TButton', textvariable=dealer_hand_var)
    
    # Player label text vars
    player_points_var = StringVar()
    player_points_var.set( "Player: " + str(player.points) )
    
    # Player Widgets
    player_hand_var = StringVar()
    player_hand_var.set(ascii_art.ascii_card(*player.cards_on_hand))
    
    player_points = ttk.Label(frm, justify=LEFT, style='Style.TButton', textvariable=player_points_var)
    player_hand   = ttk.Label(frm, justify=LEFT, style='Style.TButton', textvariable=player_hand_var)
    
    
    # Navigation
    # Hit button
    button_n1  = ttk.Button(frm, text="Hit", command= lambda: 
        update_player(
            root,
            player,
            dealer,
            deck,
            player_points_var,
            player_hand_var,
            dealer_points_var,
            dealer_hand_var,
            button_n1,
            button_n2
            )
        )
    # Stop button
    button_n2 = ttk.Button(frm, text="Stop", command= lambda: 
        update_dealer(
            root,
            player,
            dealer,
            deck,
            dealer_points_var,
            dealer_hand_var,
            button_n1,
            button_n2
            )
        )
    
    
    # Init widgets in window
    logo.grid(column=logo_col,row=logo_row,columnspan=2)
    
    dealer_points.grid(column=dealer_points_col,row=dealer_points_row)
    dealer_hand.grid(column=dealer_hand_col,row=dealer_hand_row)
    
    player_points.grid(column=player_points_col,row=player_points_row)
    player_hand.grid(column=player_hand_col,row=player_hand_row)
    
    button_n1.grid(column=hit_col, row=hit_row)
    button_n2.grid(column=stop_col, row=stop_row)
    
    # Add action on window close
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))
    root.mainloop()


#  main function
def main():    
    global game
    while game:
        game_loop(deck_shuffled())


if __name__ == "__main__":
    main()