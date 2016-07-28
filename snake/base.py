# -*- coding: utf-8 -*-
import random

class Snake():
    route = []
    direction = ''
    def __init__(self, map):
        self.route.append(map.get_central())
        self.direction = 'R'
        
    def head_move(self):
        if self.direction == 'L':
            head = self.route[0]
            head = (head[0] - 1, head[1])
            self.route.insert(0, head)
        if self.direction == 'R':
            head = self.route[0]
            head = (head[0] + 1, head[1])
            self.route.insert(0, head)
        if self.direction == 'U':
            head = self.route[0]
            head = (head[0], head[1] - 1)
            self.route.insert(0, head)
        if self.direction == 'D':
            head = self.route[0]
            head = (head[0], head[1] + 1)
            self.route.insert(0, head)
    def move(self):
        self.head_move()
        self.route.pop()
    def eat(self):
        self.head_move()
        
        
class Map():
    x = 0
    y = 0
    width = 10
    snake = None
    food = (0, 0)
    
    def __init__(self, screen_x, screen_y):
        self.x = screen_x / self.width
        self.y = screen_y / self.width
        self.snake = Snake(self)
        self.food = (random.randint(0, self.x), random.randint(0, self.y))
        
    def get_central(self):
        return self.x / 2, self.y / 2
    
    def get_positions(self):
        positions = []
        for point in self.snake.route:
            positions.append((point[0] * self.width, point[1] * self.width, self.width, self.width))
        return positions
        
    def move(self):
        self.snake.move()
    
    def change_direction(self, input):
        cur_direc = self.snake.direction
        if input == 'R':
            if cur_direc != 'L':
               self.snake.direction = 'R'
        if input == 'L':
            if cur_direc != 'R':
               self.snake.direction = 'L'
        if input == 'U':
            if cur_direc != 'D':
               self.snake.direction = 'U'
        if input == 'D':
            if cur_direc != 'U':
               self.snake.direction = 'D'
    def get_food_position(self):
        food_position = (self.food[0] * self.width + self.width / 2, self.food[1] * self.width + self.width / 2)
        return food_position
        
    def eat(self):
        self.snake.eat()
        
    def isEat(self):
        if self.snake.route[0] == self.food:
            self.eat()
            self.food = (random.randint(0, self.x), random.randint(0, self.y))
        
if __name__ == '__main__':
    map = Map(100, 300)
    print map.get_central()
    snake = Snake(map)
    