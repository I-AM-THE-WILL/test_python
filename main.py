class Dragon:
    def __init__(self, name, health):
        self.name = name
        self.health = health


    def is_alive(self):
        return self.health > 0


    def get_damage(self, damage):
        health = max(0, self.health - damage)


    def talk_about_health(self):
        print(f"My name is {self.name}. My health is {self.health}. Hit me!")


    def finally_cry(self):
        print(f"Oh no! I'm, great {self.name}, is dead! :'(")

def main():
    dragon_list = [Dragon('Vasya', 100500), Dragon('Petya', 200)]
    finish = False
    while not finish:
        dragon = dragon_list[0]
        dragon.talk_about_health()
        damage = int(input())
        dragon.health -= damage
        if not dragon.is_alive():
            dragon.finally_cry()
            dragon_list = dragon_list[1::] #delete dead enemy
        if not dragon_list: #this list is empty or not
            finish = True

    print("You're win!")

main()