class item:
    id: int
    name: str
    damage: int

    def __init__(self, id: int, name: str, damage: int) -> None:
        self.id     = id
        self.name   = name
        self.damage = damage

class items:
    
    items: list = list()

    def __init__(self, items: list = list()) -> None:
        self.items = items
    
    def contains(self, item: item) -> bool:
        for i in self.items:
            if item.id == i.id:
                return True

        return False

    def add(self, item: item) -> bool:
        if (self.contains(item) == False):
            self.items.append(item)
            return True
        else:
            return False

    def update(self, item: item) -> bool:
        if self.contains(item) == False:
            return False
        
        x = 0
        for i in self.items:
            if i.id == item.id:
                break
            else:
                x = x + 1

        self.items[x] = item
        return True
