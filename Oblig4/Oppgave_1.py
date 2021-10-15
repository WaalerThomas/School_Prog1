# ==================================================
# File: Oppgave_1.py
# Author: Thomas Waaler
# Info: BlackJack
# ==================================================
# NOTE Generert ASCII fra https://patorjk.com/software/
import random

def get_int_input(message: str) -> int:
    while True:
        try:
            user_input = int( input(message) )
            return user_input
        except ValueError:
            print("[ERROR]: Not a valid number")

class Card():
    def __init__(self, name: str, value: int):
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

    def draw_card(self, face_up: bool=True) -> Card:
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
        aces = []       # Store the aces for calulating value after the other cards
        for card in self.hand:
            if card.face_up == False:
                continue

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
    def __init__(self, chips: int=100):
        super().__init__()
        self.chips = chips


class Game():
    def __init__(self) -> None:
        self.is_running = True
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()
        self.pot = 0
    
    def start(self):
        self._game_loop()
    
    def player_win(self, blackjack: bool=False):
        if blackjack:
            reward = self.pot * 2
            print("BLACKJACK!!")
        else:
            reward = self.pot

        print(f"You won a total of {reward} chips\n")
        self.player.chips += reward
    
    def dealer_win(self):
        print(f"You lost a total {self.pot} chips\n")
        self.player.chips -= self.pot
    
    def _new_game(self):
        # Will only continue if answer is y, else end
            end_input = input("Do you wish to play again? (y/n) ")
            if "y" == end_input:
                self.dealer.clear_hand()
                self.player.clear_hand()
                print("\n\n\n==========[ Next Round ]==========")
            else:
                self.is_running = False
                print(f"You ended the game with {self.player.chips} chips left")

    def _playing_round(self) -> int:
        '''Enters the playing round loop
        
        returns: -1 if busted, 0 if successful'''
        playing_round = True
        while playing_round:
            print("Do you wish to hit or stay?\n1 - Hit\n2 - Stay")
            play_choice = get_int_input("Answer: ")
            if play_choice == 1:
                print("\nYou chose to Hit!\n")
                
                self.player.add_to_hand( self.deck.draw_card() )
                print("You got dealt a card. Your hand:")
                self.player.print_hand_list()
                print(f"Total value: {self.player.get_hand_value()}\n")

                if self.player.get_hand_value() > 21:
                    print("You BUSTED!")
                    self.dealer_win()
                    self._new_game()
                    return -1

            elif play_choice == 2:
                print("\nYou chose to Stay!\n")
                playing_round = False
            
            else:
                print("\nInvalid choice. It's either 1 or 2\n")
        
        return 0

    def _game_loop(self):
        while self.is_running:
            # Shuffle Round
            # -------------
            print("Shuffling the deck...\n")
            self.deck.shuffle()
            # -------------

            # Betting Round
            # -------------
            print("==========[ Betting Round ]==========")
            print(f"You have {self.player.chips} chips\n")

            good_bet = False
            while not good_bet:
                player_bet = get_int_input("How much do you bet? ")
                if player_bet <= 0 or player_bet > self.player.chips:
                    print(f"Invalid chip amount. Must be from 1 to {self.player.chips}\n")
                else:
                    good_bet = True
            
            print(f"You bet {player_bet}\n")
            self.pot = player_bet
            # -------------

            # Dealing round
            # -------------
            print("==========[ Dealing ]==========")
            self.player.add_to_hand( self.deck.draw_card() )
            self.dealer.add_to_hand( self.deck.draw_card() )
            self.player.add_to_hand( self.deck.draw_card() )
            self.dealer.add_to_hand( self.deck.draw_card(False) )
        
            print("Dealers hand:")
            self.dealer.print_hand_list()
            print(f"Total value: {self.dealer.get_hand_value()}")

            print("\nYour hand:")
            self.player.print_hand_list()
            print(f"Total value: {self.player.get_hand_value()}\n")

            # Check for blackjack
            if self.player.get_hand_value() == 21:
                self.player_win(True)
                self._new_game()
                continue
            # -------------

            # Run the playing round loop
            # jump over rest of the loop returned -1 (player busted)
            if self._playing_round() == -1:
                continue

            # Dealers play
            # ------------
            print("==========[ Dealers Play ]==========")
            # First flip the dealers second card
            self.dealer.flip_up_hand()
            max_cards_dealer = False
            while not max_cards_dealer:
                if self.dealer.get_hand_value() < 17:
                    self.dealer.add_to_hand( self.deck.draw_card() )
                    continue
                else:
                    max_cards_dealer = True

            print("Dealer drew until they got more than 17. Dealers hand:")
            self.dealer.print_hand_list()
            print(f"Total value: {self.dealer.get_hand_value()}\n")

            if self.dealer.get_hand_value() > 21:
                print("Dealer BUSTED!")
                self.player_win()
                self._new_game()
                continue
            # ------------

            # Check for results
            # -----------------
            player_result = self.player.get_hand_value()
            dealer_result = self.dealer.get_hand_value()
            if player_result == dealer_result:      # Draw
                print("It's a DRAW")
                print("No reward\n")
            
            elif player_result > dealer_result:     # Player won
                print(f"You won with {player_result} against {dealer_result}")
                self.player_win()

            elif player_result < dealer_result:     # Dealer won
                print(f"You lost with {player_result} against {dealer_result}")
                self.dealer_win()
            # -----------------

            self._new_game()

# Main entry point
if __name__ == "__main__":
    # Opening text
    print(''' _______   __                      __           _____                      __       
/       \ /  |                    /  |         /     |                    /  |      
$$$$$$$  |$$ |  ______    _______ $$ |   __    $$$$$ |  ______    _______ $$ |   __ 
$$ |__$$ |$$ | /      \  /       |$$ |  /  |      $$ | /      \  /       |$$ |  /  |
$$    $$< $$ | $$$$$$  |/$$$$$$$/ $$ |_/$$/  __   $$ | $$$$$$  |/$$$$$$$/ $$ |_/$$/ 
$$$$$$$  |$$ | /    $$ |$$ |      $$   $$<  /  |  $$ | /    $$ |$$ |      $$   $$<  
$$ |__$$ |$$ |/$$$$$$$ |$$ \_____ $$$$$$  \ $$ \__$$ |/$$$$$$$ |$$ \_____ $$$$$$  \ 
$$    $$/ $$ |$$    $$ |$$       |$$ | $$  |$$    $$/ $$    $$ |$$       |$$ | $$  |
$$$$$$$/  $$/  $$$$$$$/  $$$$$$$/ $$/   $$/  $$$$$$/   $$$$$$$/  $$$$$$$/ $$/   $$/ ''')
    print("By Thomas Waaler\n")

    game = Game()
    game.start()