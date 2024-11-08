class Football:

    def __init__(self,footballgame):
        self.footballgame = footballgame

    def show(self):
        print(f"{self.footballgame}")


class Cricket:

    def __init__(self,cricketgame):
        self.cricketgame = cricketgame

    def show(self):
        print(f"{self.cricketgame}")


class Games(Cricket,Football):

    def __init__(self,footballgame,cricketgame):
        self.footballgame = footballgame
        self.cricketgame = cricketgame

gam = Games("mohit","rajan")
gam.show()
print(Games.mro())