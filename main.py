class hero:
    # class constructor
    def __init__(self, name: str = 'dawg', lvl: int = "1", hp: int = 0):
        # class attributes
        self.name = name
        self.lvl = lvl
        self.hp = hp
    # class methods
    def base_action(self):
        return f'{self.name} base action, {self.hp}'

# class objects \\ class instances
spiderman =hero(lvl = 100, name='Peter')
print(spiderman.base_action())