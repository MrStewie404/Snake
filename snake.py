from time import sleep
from os import system
import getch
from random import randint

class Snake:
    body = '◉'
    head = '𖣯'
    size = 1

    def __init__(self):
        self.cell_pos = [[0, 0], [0, 1], [0, 2]]


    def move_snake(self):
        if len(self.cell_pos) < self.size:
            # self.cell_pos.append([0, 0])
            ...

        for i in range(len(self.cell_pos)-1):
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
        print('Wait...')

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
        print(f'Snake: {Snake.cell_pos[0]} | Food: {Map.food_pos} | Size: {Snake.size}\n{Snake.cell_pos}')
        return text
    

class Game:

    def __init__(self):
        self.pos = [0, 0]

    def key_trigger(self, key):
        if len(key) > 1:
            key = (key.split())[0]
        else:
            ...
        if key == 's':
            Snake.cell_pos[0][0] += 1
        elif key == 'w':
            Snake.cell_pos[0][0] -= 1
        elif key == 'd':
            Snake.cell_pos[0][1] += 1
        elif key == 'a':
            Snake.cell_pos[0][1] -= 1

    def pos_memory(self, position):
        # self.pos.append(position[0])
        # print(self.pos)
        return self.pos

    def master_process(self):
        try:
            if Snake.cell_pos[0] == Map.food_pos:
                Snake.size += 1
                Snake.cell_pos.append(Map.food_pos)
                Map.insert_food()
            for i in range(Snake.size-1):
                print(Snake.cell_pos[Snake.size-2])
                Snake.cell_pos[Snake.size-2] = Snake.cell_pos[Snake.size-1]
            
        except:
            ...

Map = Map()
Screen = Screen()
Snake = Snake()
Game = Game()

Map.create_map()
Map.insert_food()


while True:
    key = getch.getch()
    Game.key_trigger(key)
    Game.master_process()
    Game.pos_memory(Snake.cell_pos)
    Snake.move_snake()
    map = Map.insert_snake(Snake)
    # sleep(0)
    print(Screen.show(map))
