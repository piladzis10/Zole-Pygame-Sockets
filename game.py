import random
from card import Card




class Game():
    def __init__(self, id):
        self.ready = False
        self.id = id
        self.state = 1
        self.round_points = 0
        self.suit_of_the_round = None
        self.played_cards_round = []
        self.played_cards_count = 26
        self.card_deck = ["AC", "AH", "AS", "AD", "KS", "KH", "KD", "KC", "QS", "QH", "QD", "QC", "JS", "JH", "JD", "JC", "10S", "10H", "10D",
              "10C", "9S", "9H", "9D", "9C", "8D", "7D"]

        self.turn_order = 0


    def get_suit_of_the_round(self):
        if self.played_cards:
            self.suit_of_the_round = self.played_cards[0].suit

    # Checks if valid card to play
    def validation_of_move(self, card_suit):
        if self.state == 1:
            return True
        else:
            if self.suit_of_the_round == card_suit:
                return True
            else:
                return False

    # finds the winner of the round
    def winner_of_round(self, strength_scale, strength_scale_non_trumps):
        wInd = 50
        t = False
        for card in self.played_cards:
            if card.suit == "T":
                t = True
        if t:
            for card in self.played_cards:
                if strength_scale.index(card.name) < wInd:
                    wInd = strength_scale.index(card.name)
                    wCard = card.name

        else:
            wCard = self.played_cards[0].name
            for card in self.played_cards[1:]:
                if wCard.suit == card.suit and strength_scale_non_trumps.index(card.name) < strength_scale_non_trumps.index(wCard[0]):
                    wCard = card.name

        return wCard  # Winners card

class Player():
    def __init__(self, p):
        self.p = p
        self.cards = []
        self.turn = False  # checks whose turn it is
        self.last_played_card = None
        self.played_card = False
        self.order = None

    def deal_player_cards(self, card_deck):
        for _ in range(8):
            random_card = random.choice(card_deck)
            self.cards.append(Card(random_card))
            card_deck.remove(random_card)
