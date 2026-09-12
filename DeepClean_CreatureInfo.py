class Creature:
    def __init__(self, name, overview, effect, score):
        self.name = name
        self.overview = overview
        self.effect = effect
        self.score = score
        
    def display_info(self):
        print("Creature Name:", self.name)
        print("Overview", self.overview)
        print("Effect:", self.effect)
        print("Worth:", self.score)
        
