class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def damage(self, damage):
        self.health -= damage
        print(f"{self.name} получил {damage} урона, осталось {self.health}")
    def heal(self, heal):
        self.health += heal
        print(f"{self.name} получил + {heal} и теперь у него {self.health}")
    def attack(self, other_player, damage):
        print(f"{other_player.name} получил от {self.name}")
        other_player.damage(damage)




player1 = Player("витя")
player2 = Player("коля")


player1.attack(player2, 20)