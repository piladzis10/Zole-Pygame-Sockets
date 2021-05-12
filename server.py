import socket
from _thread import start_new_thread
import pickle
from game import Game, Player

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = ""
host = 55555
addr = (server, host)

s.bind(addr)

s.listen()

print("Server is working ...")

games = {}
pCount = 0
gId = 0
p = 0
players = []

STRENGTH_SCALE_TRUMPS = ["QC", "QS", "QH", "QD", "JC", "JS", "JH", "JD", "AD", "10D", "KD", "9D", "8D", "7D", "AC", "10C", "KC", "9C",
                         "AH", "10H", "KH", "9H", "AS", "10S", "KS", "9S", "None"]

STRENGTH_SCALE_NON_TRUMPS = ["A", "10", "K", "9", "None"]


def client(conn, p, gId):
    global games

    game = games[gId]

    player = Player(p)

    player.ready = True
    

    conn.send(pickle.dumps(player))


    while True:
        
        player = pickle.loads(conn.recv(2048*4))

        if game.ready:

            # starts new game
            if game.played_cards_count == 26:
                player.deal_player_cards(game.card_deck)
                if len(game.card_deck) > 4:
                    game.card_deck = ["AC", "AH", "AS", "AD", "KS", "KH", "KD", "KC", "QS", "QH", "QD", "QC", "JS", "JH", "JD", "JC", "10S", "10H", "10D",
              "10C", "9S", "9H", "9D", "9C", "8D", "7D"]
                    game.played_cards_count = 2
                    

            if player.played_card == True:

                game.played_cards_round.append(player.last_played_card)
                game.state = game.state + 1 % 3

                if len(game.played_cards_round) == 1:
                    game.suit_of_the_round = game.get_suit_of_the_round()


                # starts new round
                count = 0
                if len(game.played_cards_round) == 3:
                    count += 1
                    winnerCard = game.winner_of_round(STRENGTH_SCALE_TRUMPS, STRENGTH_SCALE_NON_TRUMPS)
                    if player.last_played_card == winnerCard:
                        player.points == game.round_points
                        game.round_points = 0
                        game.suit_of_the_round = None
                        game.state = p

                    player.last_played_card = None

                    if count == 3:
                        game.played_cards_round = []

                player.playedd_card == False


        conn.sendall(pickle.dumps(game))

    

while True:
    conn, addr = s.accept()
    print(addr, " connected to server!")

    pCount += 1
    gCount = pCount // 3 + 1
    p = 0

    if pCount % 3 == 1:
        games[gId] = Game(gId)
        players.append(Player(p))
        gId += 1
        p = 0
    elif pCount % 3  == 2:
        p = 1
    else:
        p = 2
        games[gId - 1].ready = True

    start_new_thread(client, (conn, p, gId -1))
    
