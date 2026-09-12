class Creature:
    def __init__(self, name, effect, score):
        self.name = name
        self.effect = effect
        self.score = score

    def display_info(self):
        print("Name:", self.name)
        print("Effect:", self.effect)
        print("Score:", self.score)