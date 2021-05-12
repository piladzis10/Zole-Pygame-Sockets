class Card:
    def __init__(self, name, x = 0, y = 0, width = 0, height = 0):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.position = (self.x, self.y, self.x + width, self.y + self.height)
        self.points = self.get_points()
        self.suit = self.get_suit()


    def get_suit(self):
        # check suit
        if "D" in self.name or "Q" in self.name or "J" in self.name:
            suit = "T"  # trump
        elif "C" in self.name:
            suit = "C"  # club
        elif "H" in self.name:
            suit = "H"  # heart
        else:
            suit = "S"  # spade
        return suit

    def get_points(self):
        # check points
        if "A" in self.name:
            points = 11
        elif "10" in self.name:
            points = 10
        elif "K" in self.name:
            points = 4
        elif "Q" in self.name:
            points = 3
        elif "J" in self.name:
            points = 2
        else:
            points = 0
        return points

    def validation_of_suit(self, suit_2):
            if self.suit == suit_2:
                return True
            else:
                return False

    def draw_card(self, card_images):
        pass