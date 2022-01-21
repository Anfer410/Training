import ascii_art
import main
import position


def test_ascii():
    test_card_1 = main.Card('Spades','3')
    test_card_2 = main.Card('Diamonds','King')
    test_card_3 = main.Card('Hearts','10')
    test_card_4 = main.Card('Clubs','Queen')
    
    test_deck=[test_card_1,test_card_2,test_card_3,test_card_4]
    
    print("One Card:")
    print(ascii_art.ascii_card(test_card_1))
    
    print("Few Cards:")
    print(ascii_art.ascii_card(*test_deck))
    
def test_alert():
    main.alert("Test","Test message")
    


def tests():
    test_alert()
    
    pass
    

    
if __name__ == "__main__":
    tests()