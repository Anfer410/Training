def ascii_card(*cards, return_string=True):
    
    # prints the appropriate icons for each card
    suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    suits_symbols = ['♠', '♦', '♥', '♣']

    # create an empty list of list, each sublist is a line
    lines = [[] for i in range(9)]

    for index, card in enumerate(cards):
        # "King" should be "K" and "10" should still be "10"
        if card.rank == '10':  # "10" is the only one who's rank is 2 char long
            rank = card.rank
            space = ''  # if we write "10" on the card that line will be 1 char to long
        else:
            rank = card.rank[0]  # some have a rank of 'King' this changes that to a simple 'K' ("King" doesn't fit)
            space = ' '  # no "10", we use a blank space to will the void
        # get the cards suit in two steps
        suit = suits_name.index(card.suit)
        suit = suits_symbols[suit]

        # add the individual card on a line by line basis
        lines[0].append('┌─────────┐')
        lines[1].append('│{}{}       │'.format(rank, space))  # use two {} one for char, one for space or char
        lines[2].append('│         │')
        lines[3].append('│         │')
        lines[4].append('│    {}    │'.format(suit))
        lines[5].append('│         │')
        lines[6].append('│         │')
        lines[7].append('│       {}{}│'.format(space, rank))
        lines[8].append('└─────────┘')

    result = []
    for index, line in enumerate(lines):
        result.append(''.join(lines[index]))

    # hidden cards do not use string
    if return_string:
        return '\n'.join(result)
    else:
        return result

def ascii_hidden_card(*cards):
    
    # a flipper over card. # This is a list of lists instead of a list of string becuase appending to a list is better then adding a string
    lines = [['┌─────────┐'], 
             ['│░░░░░░░░░│'], 
             ['│░░░░░░░░░│'], 
             ['│░░░░░░░░░│'], 
             ['│░░░░░░░░░│'], 
             ['│░░░░░░░░░│'], 
             ['│░░░░░░░░░│'], 
             ['│░░░░░░░░░│'], 
             ['└─────────┘']]

    # store the non-flipped over card after the one that is flipped over
    cards_except_first = ascii_card(*cards[1:], return_string=False)
    for index, line in enumerate(cards_except_first):
        lines[index].append(line)

    # make each line into a single list
    for index, line in enumerate(lines):
        lines[index] = ''.join(line)

    # convert the list into a single string
    return '\n'.join(lines)


def ascii_logo():
    return """
┌─────────┐
│A        │
│      ┌─────────┐   _     _            _    _            _          
│      │K        │  | |   | |          | |  (_)          | |         
│    ♠ │         │  | |__ | | __ _  ___| | ___  __ _  ___| | __    
│      │         │  | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /   
│      │    ♥    │  | |_) | | (_| | (__|   <| | (_| | (__|   <     
│      │         │  |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\   
└──────│         │                         _/ |                 
       │        K│                        |__/           
       └─────────┘ 
"""                   

def logo():
    return """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""