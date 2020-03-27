from module import witcher_trial as wt


class Player_Template_Class:
    def __init__(self, name):
        self.name = name

    def tuplefy_self(self):
        return (str(self.name))

def character_creator():
    name = input("What is your name?\n")
    return name

player_character = Player_Template_Class(character_creator())
player_info = player_character.tuplefy_self()

def hand_off_function(player_info_hand_off):
     wt.w_t_game(player_info_hand_off)


if __name__ == "__main__":
    hand_off_function(player_info)
