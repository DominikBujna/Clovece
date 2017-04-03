from random import randint

# globalne premenne
num_of_players = 2
num_of_figures = 4
board_size = 180


# udrzujem info o hracoch
class Player:
    name = ""
    player_position = [-6] * num_of_figures

    def __init__(self, username):
        self.name = username


# pole hracov
hraci = [Player("Dominik"), Player("Jozko")]
# hra

while (True):
    for hrac in hraci:
        hod = randint(1, 6)
        print(hrac.name, " hodil ", hod)
        if (hrac.on_board and hod == 6):
            hrac.player_position
            # vyberiem ktoreho hraca chcem
            tah = int(input("Vyberte hraca")) % num_of_figures
            hrac.player_position[tah] += hod
            # TODO: vykonanie tahu - ceknut, ci je volne pole, posunut
            # pozrem, ci je pole volne
            for protihrac in hraci:
                for pozicia in protihrac.player_position:
                    # ak je pole plne, vyhodim ho
                    if (hrac.player_position[tah] == pozicia and protihrac != hrac):
                        pozicia = -6
