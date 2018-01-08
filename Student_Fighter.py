class StudentFighter(object):

    def __init__(self, strength, health, name):
        self.strength = strength
        self.name = name
        self.health = health

jestina = StudentFighter(strength=6, health=10000, name="jestina")
santos = StudentFighter(strength=10, health=10000, name="santos")

print(jestina.name, jestina.strength, jestina.health)
print(santos.name, santos.strength, santos.health)
