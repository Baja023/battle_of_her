import random

class Hero:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.attack_types = {
            'Удар рукой': 10,
            'Удар ногой': 15,
            'Мощный удар': 25
        }

    def attack(self, other, attack_type):
        if self.is_alive():
            attack_power = self.attack_types.get(attack_type, 0)
            other.health -= attack_power
            print(f"{self.name} использует {attack_type} и наносит {attack_power} урона.")
            print(f"У {other.name} осталось {other.health} здоровья.")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        print("Игра начинается!")
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player_turn()
            if not self.computer.is_alive():
                print(f"{self.player.name} побеждает!")
                break

            # Ход компьютера
            self.computer_turn()
            if not self.player.is_alive():
                print(f"{self.computer.name} побеждает!")
                break

    def player_turn(self):
        print("\nВаш ход!")
        print("Доступные атаки:")
        for attack in self.player.attack_types:
            print(f"- {attack}")
        attack_type = input("Выберите атаку: ")
        if attack_type not in self.player.attack_types:
            print("Неверный выбор, попробуйте снова.")
            self.player_turn()
        else:
            self.player.attack(self.computer, attack_type)

    def computer_turn(self):
        print("\nХод компьютера!")
        attack_type = random.choice(list(self.computer.attack_types.keys()))
        self.computer.attack(self.player, attack_type)

# Создание героев
player = Hero(name="Игрок")
computer = Hero(name="Компьютер")

# Начало игры
game = Game(player, computer)
game.start()
