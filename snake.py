from time import sleep
from os import system
from os.path import exists
import getch
from random import randint
import json

class Snake:
    body = '◉'
    head = 'h'
    size = 1

    def __init__(self):
        self.cell_pos = [[1, 0], [0, 0]]
        self.score = 0

    def move_snake(self):
        if len(self.cell_pos)-1 < self.size:
            self.cell_pos.append(Map.food_pos)

        else:
            self.cell_pos = [self.cell_pos[0]] + self.cell_pos
            cell_pos_local = self.cell_pos
            for i in range(len(self.cell_pos)-1, -1, -1):
                cell_pos_local[i] = cell_pos_local[i-1]
            cell_pos_local = cell_pos_local[len(cell_pos_local)-1:]

            self.cell_pos = cell_pos_local
            # print(self.cell_pos[i], self.cell_pos[i-1])

class Map:
    width = 10
    height = 5
    cell = ' '
    food = '@'
    food_pos = [1, 1]
    
    def __init__(self):
        ...
      
    def create_map(self) -> list:
        # Создание карты (массив)
        self.map = [[]]
        
        for i in range(self.height):
            for j in range(self.width):
                self.map[i].append(self.cell)
            self.map.append([])
        return self.map

    def insert_snake(self):
        for i in range(len(Snake.cell_pos)):
            if i == 0:
                self.map[Snake.cell_pos[i][0]][Snake.cell_pos[i][1]] = Snake.head
            else:
                self.map[Snake.cell_pos[i][0]][Snake.cell_pos[i][1]] = Snake.body

        for i in range(self.height):
            for j in range(self.width):
                if [i, j] not in [*Snake.cell_pos, self.food_pos]:
                    self.map[i][j] = self.cell

        return self.map
    
    def insert_food(self):
        self.food_pos = [randint(0, self.height-1), randint(0, self.width-1)]
        if self.map[self.food_pos[0]][self.food_pos[1]] in [Snake.head, Snake.body]:
            self.insert_food()
        else:
            self.map[self.food_pos[0]][self.food_pos[1]] = self.food
        
        return self.map


class Screen:
    width = Map.width
    height = Map.height

    def __init__(self):
        system('clear')
        print('\n' * int(self.height/2) + 
            ' ' * int(self.width/2) + 
            'Press WASD or arrow...')

    def show(self, map) -> str:
        # Отрисовка карты
        # system('clear')
        text = ' ' + '-'*self.width
        for i in range(self.height):
            text += '\n|'
            for j in range(self.width):
                text += '| '.join(map[i][j])
            text += '|'

        text += '\n ' + '-'*self.width
        print(f'Snake: {Snake.cell_pos[0]} | Food: {Map.food_pos} | Score: {Snake.score} | Size: {Snake.size}\n' \
                f'Cells: {Snake.cell_pos}')
        return text
    

class Game:

    def __init__(self):
        self.pos = [0, 0]
        self.file_name = 'save.json'

    def key_trigger(self, key):
        if len(key) > 1:
            key = (key.split())[0]
        else:
            ...
        if key in ['s', 'B']:
            if Snake.cell_pos[0][0] != Map.height-1:
                Snake.cell_pos[0][0] += 1
        elif key in ['w', 'A']:
            if Snake.cell_pos[0][0] != 0:
                Snake.cell_pos[0][0] -= 1
        elif key in ['d', 'C']:
            if Snake.cell_pos[0][1] != Map.width-1:
                Snake.cell_pos[0][1] += 1
        elif key in ['a', 'D']:
            if Snake.cell_pos[0][1] != 0:
                Snake.cell_pos[0][1] -= 1
        else:
            # print(f'Press unknown {key}')
            ...

    def save(self, score=0):
        data = json.dumps({"score": score})
        open(self.file_name, "w").write(data)

    def load(self):
        if exists(self.file_name):
            file = open(self.file_name, "r").read()
            data = json.loads(file)
            Snake.score = data["score"]
        else:
            self.save()

    def master_process(self):
        try:
            if Snake.cell_pos[0] == Map.food_pos:
                Map.insert_food()
                Snake.score += 1
                Snake.size += 1
                self.save(score = Snake.score)
            Snake.move_snake()
        except:
            ...

Map = Map()
Screen = Screen()
Snake = Snake()
Game = Game()
Game.load()

Map.create_map()
Map.insert_food()

while True:
    key = getch.getch()
    Game.key_trigger(key)
    Game.master_process()
    map = Map.insert_snake()
    print(Screen.show(map))
    if Snake.score == 2500:
        print('YOU WIN :)')
        break

