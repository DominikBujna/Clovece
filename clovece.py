from random import randint

# globalne premenne
num_of_players = 2
num_of_figures = 4
board_size = 179


# udrzujem info o hracoch
class Player:
    name = ""
    player_position = [-6] * num_of_figures

    def __init__(self, username):
        self.name = username


# pole hracov
hraci = [Player("Dominik"), Player("Jozko")]
# hra
game_on = False
while (game_on):
    for hrac in hraci:
        # hodim kockou
        hod = randint(1, 6)
        nahadzane = hod + 0
        print(hrac.name, " hodil ", hod)
        # ak hodim 6, hadzem dalej
        while (hod == 6):
            hod = randint(1, 6)
            nahadzane += hod
        # ak som na ploche, vyberiem kym idem
        if -6 not in hrac.player_position:
            # vyberiem ktoreho hraca chcem
            tah = int(input("Vyberte hraca od 1 po ", num_of_figures + 1)) % num_of_figures
            # vykonam tah zvolenym hracom, ak nie je v dome
            if (hrac.player_position[tah + 1] + nahadzane > board_size):
                print("Nemozem vykonat tah.")
            else:
                hrac.player_position[tah + 1] += nahadzane
            # pozrem, ci je pole volne
            for protihrac in hraci:
                for pozicia in protihrac.player_position:
                    # ak je pole plne, vyhodim ho
                    if (hrac.player_position[tah] == pozicia and protihrac != hrac):
                        pozicia = -6
                        # ak som tymto tahom skoncil
            if (i for i in hrac.player_position if i > (board_size - num_of_figures)):
                game_on = False
                print(hrac, " vyhral hru.")
