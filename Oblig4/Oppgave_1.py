# ==================================================
# File: Oppgave_1.py
# Author: Thomas Waaler
# Info: BlackJack
# ==================================================
import random
'''
Én vanlig kortstokk med 52 kort.
1-10, J, Q, K. Fire av hver. Har ingen betydning for hva slags type(hjerte, kløver, spar, ruter)

Utfall:
    * Spilleren vinner -> Spilleren tjener like mange chips som spesifisert i innsatsen
    * Dealeren vinner -> Spilleren mister like mange chips som spesifisert i innsatsen
    * Ingen vinner -> Spillerens chips forblir det samme som før innsatsen
    * Blackjack -> Spilleren tjener 2x antallet chips spesifisert i innsatsen
'''

# NOTE Only Ace will have two different values (Depending of the hand total)
class Card():
    def __init__(self, name: str, value: int) -> None:
        self.name = name
        self.value = value
        self.face_up = True

    def __str__(self) -> str:
        '''What will be returned when converting to a string'''
        if self.face_up:
            return f"{self.name}"
        else:
            return f"Face down card"

class Deck():
    BASE_CARDS = {
        "Ace of": 1, "Two of": 2, "Three of": 3, "Four of": 4, "Five of": 5, "Six of": 6,
        "Seven of": 7, "Eight of": 8, "Nine of": 9, "Ten of": 10, "Jack of": 10, "Queen of": 10, "King of": 10
    }

    def __init__(self):
        self.cards = list()
        self._populate_deck()

    def new_deck(self):
        self._populate_deck()

    def shuffle(self):
        '''Shuffles the whole deck'''
        random.shuffle(self.cards)

    def draw_card(self, face_up=True) -> Card:
        '''Draws a card out of the deck and returns it'''
        card = self.cards.pop()
        card.face_up = face_up
        return card

    def _populate_deck(self):
        '''Populates the deck with all 52 cards'''
        self.cards.clear()
        for key, value in self.BASE_CARDS.items():
            self.cards.append( Card(f"{key} Clubs", value) )
            self.cards.append( Card(f"{key} Diamonds", value) )
            self.cards.append( Card(f"{key} Hearts", value) )
            self.cards.append( Card(f"{key} Spades", value) )


class Contender():
    def __init__(self):
        self.hand = list()

    def get_hand_value(self) -> int:
        total_value = 0
        aces = []       # Store the aces for calulating if its 1 or 11 after the other cards
        for card in self.hand:
            if card.face_up == False:
                continue    # Skip card if it's face down

            if "Ace" in card.name:
                aces.append(card)
                continue

            total_value += card.value
        
        # Calculate value of aces
        # TODO Do some failcheck testing on this calculation here
        if len(aces) > 0:
            # TODO Problem if you have two aces and the first gets calulated as 11 but it would have been better that both would be 1
            for card in aces:
                if total_value + 11 > 21:
                    total_value += 1
                else:
                    total_value += 11
        
        return total_value
    
    def clear_hand(self):
        self.hand.clear()

    def add_to_hand(self, card: Card):
        self.hand.append(card)
    
    def print_hand_list(self):
        for card in self.hand:
            print(f"- {card}")


class Dealer(Contender):
    def __init__(self):
        super().__init__()
    
    def flip_up_hand(self):
        for card in self.hand:
            card.face_up = True


class Player(Contender):
    def __init__(self, chips=100):
        super().__init__()
        self.chips = chips


def get_int_input(message: str) -> int:
    while True:
        try:
            user_input = int( input(message) )
            return user_input
        except ValueError:
            print("[ERROR]: Not a valid number")

# Main entry point
if __name__ == "__main__":
    # Opening text
    print("BlackJack By Thomas Waaler")

    is_running = True
    dealer = Dealer()
    player = Player()
    deck = Deck()
    pot = 0

    # Game Loop
    while is_running:
        # Shuffle Round
        # -------------
        print("Shuffling the deck...\n")
        deck.shuffle()
        # -------------

        # Betting Round
        # -------------
        print("==========[ Betting Round ]==========")
        print(f"You have {player.chips} chips\n")

        good_bet = False
        while not good_bet:
            player_bet = get_int_input("How much do you bet? ")
            if player_bet <= 0 or player_bet > player.chips:
                print(f"Invalid chip amount. Must be from 1 to {player.chips}\n")
            else:
                good_bet = True
        
        print(f"You bet {player_bet}\n")
        pot = player_bet
        # -------------

        # Dealing round
        # -------------
        print("==========[ Dealing ]==========")
        player.add_to_hand( deck.draw_card() )
        dealer.add_to_hand( deck.draw_card() )
        player.add_to_hand( deck.draw_card() )
        dealer.add_to_hand( deck.draw_card(False) )
    
        print("Dealers hand:")
        dealer.print_hand_list()
        print(f"Total value: {dealer.get_hand_value()}")

        print("\nYour hand:")
        player.print_hand_list()
        print(f"Total value: {player.get_hand_value()}\n")

        # TODO Check for blackjack: Got 21. Player wins double of pot
        # -------------

        # Play Round
        # -------
        playing_round = True
        while playing_round:
            print("Do you wish to hit or stay?\n1 - Hit\n2 - Stay")
            play_choice = get_int_input("Answer: ")
            if play_choice == 1:
                print("\nYou chose to Hit!\n")
                
                player.add_to_hand( deck.draw_card() )
                print("You got dealt a card. Your hand:")
                player.print_hand_list()
                print(f"Total value: {player.get_hand_value()}\n")

                # TODO Check to see if player has busted or not

            elif play_choice == 2:
                print("\nYou chose to Stay!\n")
                # TODO Implement
                playing_round = False
            
            else:
                print("\nInvalid choice. It's either 1 or 2\n")
        # -------

        # Dealers play
        # ------------
        print("==========[ Dealers Play ]==========")
        # First flip the dealers second card
        dealer.flip_up_hand()


        dealer_value = dealer.get_hand_value()
        print("Dealers hand:")
        dealer.print_hand_list()
        print(f"Total value: {dealer_value}")
        # ------------

        # Check for results
        # -----------------

        # -----------------

        # Game end
        # --------
        # Will only continue if answer is y, else end
        end_input = input("Do you wish to play again? (y/n) ")
        if "y" == end_input:
            dealer.clear_hand()
            player.clear_hand()
            continue
        else:
            is_running = False
        # --------
