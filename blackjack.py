#Black Jack boyeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}



class Card():
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + " of " + self.suit
    
class Deck():
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        full_deck = ""
        for card in self.deck: 
            full_deck += ("\n" + card.__str__())
        
        return full_deck
    
    def __len__(self):
        return len(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        dealt_card = self.deck.pop()
        return dealt_card

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        #this card will be passed in from Deck.deal()
        self.cards.append(card)
        self.value += values.get(card.rank)
        if card.rank == "Ace":
            self.aces += 1
        
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0: 
            self.value -= 10
            self.aces -= 1


class Chips:
    
    def __init__(self, total = 100):
        self.total = total  
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    correct_answer = False
    while not correct_answer:
        chips.bet = int(input("How much would you like to bet? "))
        
        if chips.bet > chips.total:
            print("\n"*50)
            print("You don't have enough chips. Current total: {}".format(chips.total))
        else:
            correct_answer = True
            return chips.bet
        

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    
def hit_or_stand(deck,hand):
    global playing
    while playing: 
        player_input = input("Hit or Stand? h/s ")
        if player_input.lower() == "h":
            hit(deck, hand)
            print("\n"*50)
        elif player_input.lower() == "s":
            print("\n"*50)
            print("Player Stands, Dealer's Turn.")
            playing = False
        else:
            print("Please enter the correct instruction")
            continue
        
        break



def show_some(player,dealer):
    print("\n")
    print("Dealer's Hand: ")
    print("Unknown Card")
    print(dealer.cards[1], "\n")
    print("Player's Hand: ")
    for card in player.cards:
        print(card)
    print("\n")
    
def show_all(player,dealer):
    print("\n")    
    print("Dealer's Hand: ")
    for card in dealer.cards:
        print(card)
    print("\n")
    print("Player's Hand: ")
    for card in player.cards:
        print(card)    
    print("\n")
    
def player_busts(player, dealer, chips):
    print("Player Busted!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player Wins!")
    chips.win_bet()
    
def dealer_busts(player, dealer, chips):
    print("Dealer Busted!")
    chips.win_bet()
    
def dealer_wins(player, dealer, chips):
    print("Dealer Wins!")
    chips.lose_bet()
    
def push():
    print("Dealer and Player Tie! PUSH")
    
#below is code for playing the game
print("\n"*50)        
print("Hello, welcome to Blackjack.")
print("This is Ronnie's second attempt at writing a text-based game in python. Enjoy.")

playing = True

player_chips = Chips()
while True:
# Create & shuffle the deck, deal two cards to each player
    playing_deck = Deck()
    playing_deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(playing_deck.deal())
    player_hand.add_card(playing_deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(playing_deck.deal())
    dealer_hand.add_card(playing_deck.deal())

    
    # Set up the Player's chips

    
    # Prompt the Player for their bet
    print("\n")    
    print("You now have {} chips".format(player_chips.total))
    take_bet(player_chips)
    print("\n"*50)
    
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(playing_deck,player_hand) 
        
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
                player_busts(player_hand,dealer_hand,player_chips)
                break
    
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(playing_deck,dealer_hand)
                
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        
        else:
            push()      
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at", player_chips.total)
    print("\n")    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
        
    if new_game[0].lower()=='y':
        print("\n"*50)
        if player_chips.total == 0:
            print("You ran out of chips!")
            print("Go home, you broke boi.")
            print('\n')
            print("Thanks for playing!")
            print("Please go to TeamTrees.org to plant more trees!")           
            break
        else:
            playing=True
            continue
    
    else:
        print("\n")
        print("Thanks for playing!")
        print("Please go to TeamTrees.org to plant more trees!")
        break