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
game_on = True
while (game_on):
    for hrac in hraci:
        # hodim kockou
        hod = randint(1, 6)
        nahadzane = hod + 0
        print(hrac.name, " hodil ", hod)
        print(hrac.player_position)
        # ak hodim 6, hadzem dalej
        while (hod == 6):
            hod = randint(1, 6)
            nahadzane += hod
            print(hrac.name, " hodil este: ", hod)
        # ak som na ploche, vyberiem kym idem
        # vyberiem ktoreho hraca chcem
        tah = int(input("Vyberte hraca")) % num_of_figures
        # vykonam tah zvolenym hracom, ak nie je v dome
        if (hrac.player_position[tah - 1] + nahadzane > board_size):
            print("Nemozem vykonat tah.")
        else:
            if (hrac.player_position[tah - 1] == -6 and nahadzane < 6):
                tah = int(input("Hrac nie je v hre."))
            else:
                hrac.player_position[tah - 1] += nahadzane
        # pozrem, ci je pole volne
        for protihrac in hraci:
            for pozicia in protihrac.player_position:
                    # ak je pole plne, vyhodim ho
                    if (hrac.player_position[tah] == pozicia and protihrac != hrac):
                        pozicia = -6
                        # ak som tymto tahom skoncil
        if (hrac.player_position[tah] >= board_size - num_of_figures):
            game_on = False
            print(hrac.name, " vyhral hru. ")
