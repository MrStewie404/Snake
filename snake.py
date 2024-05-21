from time import sleep
from os import system
from os.path import exists
import getch
from random import randint
import json

class Snake:
    body = '◉'
    head = '𖣯'
    size = 1

    def __init__(self):
        self.cell_pos = [[0, 0]]
        self.score = 0

    def move_snake(self):
        if len(self.cell_pos) < self.size:
            # self.cell_pos.append([0, 0])
            ...

        for i in range(len(self.cell_pos)):
            print(f'a: {self.cell_pos[-i]}')
            # self.cell_pos[self.size-2] = self.cell_pos[self.size-1]


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

    def insert_snake(self, snake):
        for i in range(self.height):
            for j in range(self.width):
                if [i, j] in snake.cell_pos:
                    if [i, j] == snake.cell_pos[0]:
                        self.map[snake.cell_pos[0][0]][snake.cell_pos[0][1]] = snake.body
                else:
                    if self.map[i][j] not in [self.cell, self.food]:
                        self.map[i][j] = self.cell
        return self.map
    
    def insert_food(self):
        for i in range(self.height-1):
            for j in range(self.width-1):
                if [i, j] == self.food:
                    return

        self.food_pos = [randint(0, self.height-1), randint(0, self.width-1)]
        self.map[self.food_pos[0]][self.food_pos[1]] = self.food
        return self.map


class Screen:
    width = Map.width
    height = Map.height

    def __init__(self):
        system('clear')
        print('Wait WASD...')

    def show(self, map) -> str:
        # Отрисовка карты
        system('clear')
        text = ' ' + '-'*self.width
        for i in range(self.height):
            text += '\n|'
            for j in range(self.width):
                text += '| '.join(map[i][j])
            text += '|'

        text += '\n ' + '-'*self.width
        print(f'Snake: {Snake.cell_pos[0]} | Food: {Map.food_pos} | Score: {Snake.score}')
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
        if key == 's':
            if Snake.cell_pos[0][0] != Map.height-1:
                Snake.cell_pos[0][0] += 1
        elif key == 'w':
            if Snake.cell_pos[0][0] != 0:
                Snake.cell_pos[0][0] -= 1
        elif key == 'd':
            if Snake.cell_pos[0][1] != Map.width-1:
                Snake.cell_pos[0][1] += 1
        elif key == 'a':
            if Snake.cell_pos[0][1] != 0:
                Snake.cell_pos[0][1] -= 1

    def pos_memory(self, position):
        # self.pos.append(position[0])
        # print(self.pos)
        return self.pos

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
                # Snake.size += 1
                # Snake.cell_pos.append(Map.food_pos)
                Map.insert_food()
                Snake.score += 1
                self.save(score = Snake.score)
            for i in range(Snake.size-1):
                # print(Snake.cell_pos[Snake.size-2])
                # Snake.cell_pos[Snake.size-2] = Snake.cell_pos[Snake.size-1]
                ...
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
    #Game.pos_memory(Snake.cell_pos)
    # Snake.move_snake()
    map = Map.insert_snake(Snake)
    # sleep(0)
    print(Screen.show(map))
    if Snake.score == 1000:
        print('YOU WIN :)')
        break

