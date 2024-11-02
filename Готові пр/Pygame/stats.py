
class Stats():

    def __init__(self):
        self.reset_stats()
        self.run_game = True
        with open("hight_score.txt", "r") as f:
            self.hight_score = int(f.readline())

    def reset_stats(self):
        self.gun_left = 2
        self.score = 0

