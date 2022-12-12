from abc import ABC, abstractmethod
import json

class Drink(ABC):
    def __init__(self, volume: float, sparkling: bool, alcoholic: bool):
        self.volume = volume
        self.sparkling = sparkling
        self.alcoholic = alcoholic

    def __repr__(self) -> str:
        return f'<\'{self.__class__.__name__}\' name: {self.name}, volume: {self.volume}, sparkling: {self.sparkling}, alcoholic: {self.alcoholic}>'

    @abstractmethod
    def for_children(self):
        if(self.alcoholic):
            return f'  {self.model} for person older than 18 y.o.'
        return f'  {self.model} allowed for porson yonger than 18 y.o.'


class Water(Drink):
    def __init__(self, volume: int, sparkling: bool, alcoholic: bool):
        self.name = "Water"
        super().__init__(volume, sparkling, alcoholic)

    def for_children(self):
        return super().for_children()


class CocaCola(Drink):
    def __init__(self, volume: int, sparkling: bool, alcoholic: bool):
        self.name = "Coca-Cola"
        super().__init__(volume,sparkling,alcoholic)

    def for_children(self):
        return super().for_children()

class Gin(Drink):
    def __init__(self, volume: int, sparkling: bool, alcoholic: bool):
        self.name = "Gin"
        super().__init__(volume, sparkling, alcoholic)

    def for_children(self):
        return super().for_children()

class Juice(Drink):
    def __init__(self, volume: int, sparkling: bool, alcoholic: bool):
        self.name = "Juice"
        super().__init__(volume, sparkling, alcoholic)

    def for_children(self):
        return super().for_children()


class Beer(Drink):
    def __init__(self, volume: int, sparkling: bool, alcoholic: bool):
        self.name = "Beer"
        super().__init__(volume, sparkling, alcoholic)

    def for_children(self):
        return super().for_children()

def write(data):
    jsonstr = json.dumps(ensure_ascii=False, obj=data, indent=4)
    open('output.json', 'w').write(jsonstr)


def read_from_json():
    return json.load(open('output.json', 'r'))

water = Water(volume=0.5,sparkling=True,alcoholic=False)
cocacola = CocaCola(volume=1.5, sparkling=True,alcoholic=False)
juice = Juice(volume=1,sparkling=False,alcoholic=False)
gin = Gin(volume=0.7,sparkling=False,alcoholic=True)
beer = Beer(volume=0.5,sparkling=True,alcoholic=True)

objects = [water, cocacola, juice, gin, beer]
data = {
        'Drinks': [],
}
for obj in objects:
    data['Drinks'].append(obj.__dict__)

write(data)
data.clear()
objects.clear()
data = read_from_json()
for obj in data['Drinks']:
    match obj['name']:
        case "Water":
            obj = Water(obj['volume'], obj['sparkling'], obj['alcoholic'])
        case "Coca-Cola":
            obj = CocaCola(obj['volume'], obj['sparkling'], obj['alcoholic'])
        case "Juice":
            obj = Juice(obj['volume'], obj['sparkling'], obj['alcoholic'])
        case "Gin":
            obj = Gin(obj['volume'], obj['sparkling'], obj['alcoholic'])
        case "Beer":
            obj = Beer(obj['volume'], obj['sparkling'], obj['alcoholic'])
    objects.append(obj)

with open(encoding='utf-8', file='output.txt', mode='w') as file:
    for obj in objects:
        output = obj.__repr__() + "\n"
        file.write(output)