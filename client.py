import pygame
import os
from network import Network
from card import Card
from game import Game, Player
pygame.font.init()

# Initializing window
WIDTH, HEIGHT = 700, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zole")

CARD_WIDTH = 60

############################## Uploading cards
def get_card_size(card_width, image):
        card_height = image.get_height() / (image.get_width()/card_width)
        return round(card_height)

CARD_IMAGE_BACK_GRAY = pygame.image.load(
    os.path.join("images", "gray_back.png"))

CARD_HEIGHT = get_card_size(CARD_WIDTH, CARD_IMAGE_BACK_GRAY)

# Uploading backside of cards
CARD_IMAGE_BACK_GRAY = pygame.transform.scale(
    CARD_IMAGE_BACK_GRAY, (CARD_WIDTH, CARD_HEIGHT))

# Uploading all the cards
def upload_card_images(card_name):
    card_n = pygame.image.load(os.path.join("images", card_name + ".png"))
    card_n = pygame.transform.scale(
        card_n, (CARD_WIDTH, CARD_HEIGHT))
    return card_n


CARD_NAMES = ["AC", "AH", "AS", "AD", "KS", "KH", "KD", "KC", "QS", "QH", "QD", "QC", "JS", "JH", "JD", "JC", "10S", "10H", "10D",
              "10C", "9S", "9H", "9D", "9C", "8D", "7D"]

CARD_IMAGES = {}

# Uploading all card images in dictionary
for name in CARD_NAMES:
    CARD_IMAGES[name] = upload_card_images(name)

############################## Uploading cards End


# Card strengths

STRENGTH_SCALE_TRUMPS = ["QC", "QS", "QH", "QD", "JC", "JS", "JH", "JD", "AD", "10D", "KD", "9D", "8D", "7D", "AC", "10C", "KC", "9C",
                         "AH", "10H", "KH", "9H", "AS", "10S", "KS", "9S", "None"]

STRENGTH_SCALE_NON_TRUMPS = ["A", "10", "K", "9", "None"]


def draw_player(win,x, y,width,height, cards, card_images):
    i = 0
    for card in cards:
        win.blit(card_images[card.name], (x + i * width, y))
        card.position = (x + i * width, y, x +
                            i * width + width, y + height)
        i += 1

def draw_opponents(win,x, y,width,height,back_image,count, hor = True):
    if hor:
        for i in range(count):
            win.blit(back_image, (x + i * width, y))

    else:
        for i in range(count):
            win.blit(pygame.transform.rotate(back_image, 90), (x , y + i * height))

def draw_played_cards(win, cards, card_images, turn_order):
    position = [(300,300),(315, 260),(330,300)]
    counter = turn_order
    for _ in range(len(cards)):
        win.blit(card_images[cards[0].name], (position[counter]))
        turn_order = (counter + 1) % 3





def main():
    run = True
    clock = pygame.time.Clock()
    main_font = pygame.font.SysFont("comicsans", 30)
    n = Network()

    player = n.connect()


    def redraw_window(win):
        win.fill((53, 101, 77))


        draw_player(win, 60, 650, CARD_WIDTH, CARD_HEIGHT, player.cards,CARD_IMAGES)
        draw_opponents(win, 60, 150, CARD_WIDTH, CARD_WIDTH, CARD_IMAGE_BACK_GRAY, 8)
        draw_opponents(win, 550, 150, CARD_WIDTH, CARD_WIDTH, CARD_IMAGE_BACK_GRAY, 8, hor = False)
        draw_played_cards(win,game.played_cards_round, CARD_IMAGES, game.turn_order)

        if player.turn == True:
            for card in player.Cards:
                if card.position[0] >= pos[0] and card.position[1] >= pos[1] and card.position[2] <= pos[0] and card.position[3] <= pos[1]:
                    player.cards.remove(card)
                    player.played_card = True
                    player.last_played_card = card
                    player.turn = False


        pygame.display.update()

    while run:
        pos = (-5, -5)
        clock.tick(60)
        game = n.send(player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and player.turn == True:
                pos = pygame.mouse.get_pos()

        redraw_window(WIN)


main()


