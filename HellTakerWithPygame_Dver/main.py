import pygame
import random
import math

pygame.init()

class Settings:
    def __init__(self):
        self.width = 1300
        self.height = 700
        """self.obj_size = int(self.height / 14)
        self.row_size = int(self.width / self.obj_size)
        self.font_ingame = int(self.height / 4.5)"""
        self.background = pygame.image.load('assets/backgrounds/background.jpg')
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.player = pygame.image.load('assets/objects/player.png')
        self.player = pygame.transform.scale(self.player, (50, 50))
        self.stone = pygame.image.load('assets/objects/stone.png')
        self.stone = pygame.transform.scale(self.stone, (50, 50))
        self.wall = pygame.image.load('assets/objects/wall.png')
        self.wall = pygame.transform.scale(self.wall, (50, 50))
        self.goal = pygame.image.load('assets/objects/goal.png')
        self.goal = pygame.transform.scale(self.goal, (50, 50))
        self.ske = pygame.image.load('assets/objects/ske.png')
        self.ske = pygame.transform.scale(self.ske, (50, 50))
        self.spike = pygame.image.load('assets/objects/spike.png')
        self.spike = pygame.transform.scale(self.spike, (50, 50))
        self.key = pygame.image.load('assets/objects/key.png')
        self.key = pygame.transform.scale(self.key, (50, 50))
        self.lock = pygame.image.load('assets/objects/lock.png')
        self.lock = pygame.transform.scale(self.lock, (50, 50))
        self.unspike = pygame.image.load('assets/objects/unspike.png')
        self.unspike = pygame.transform.scale(self.unspike, (50, 50))
        self.KEY_DIR = {pygame.K_RIGHT: (1, 0), pygame.K_LEFT: (-1, 0), pygame.K_UP: (0, -1), pygame.K_DOWN: (0, 1)}
        #self.reso_list = [[640, 480], [800, 600], [1024, 720], [1280, 720], [1280, 768], [1360, 768], [1366, 768]]
        self.ingame = pygame.font.Font('assets/font/CrimsonPro-VariableFont_wght.ttf', 150)
        self.tutorial = pygame.font.Font('assets/font/CrimsonPro-VariableFont_wght.ttf', 30)
        self.main_menu = pygame.font.Font('assets/font/CrimsonPro-VariableFont_wght.ttf', 50)
        self.main_menu_2 = pygame.font.Font('assets/font/CrimsonPro-VariableFont_wght.ttf', 20)
        pygame.mixer.music.load('assets/music/minigame.mp3')
        

class Object:
    wall_list = ['#']
    player_list = ['p', 'P']
    stone_list = ['o', 'O', 'q', 'Q']
    ske_list = ['s', 'S']
    goal_list = ['g', 'G']
    holea_list = ['h', 'q']
    holeb_list = ['H', 'Q']
    key_list = ['k', 'K']
    lock_list = ['l', 'L']
    spike_list = ['e', 'P', 'O', 'S', 'G', 'K', 'L']
    level = 0
    def __init__(self):
        self.all_pos = []
        self.wall_pos = []
        self.ske_pos = []
        self.stone_pos = []
        self.spike_pos = []
        self.holea_pos = []
        self.holeb_pos = []
        self.key_pos = []
        self.lock_pos = []
        self.player_pos = []
        self.goal_pos = []
        self.getkey = False
        self.popup = True
        self.choose = 1
        self.menu = 2
        self.event_pos = []
        self.event_lose = False
        self.event_spawn = 400
        self.event_speed = 0.1
        self.event_player_pos = (650, 350)
        self.event_time = 0
        self.event_time_now = 0
        #self.reso = 3
        if(self.level == 9):
            self.level = 0
        if(self.level > 10):
            self.level = 1
        with open(f'levels\level{self.level}.txt', 'r') as f:
            self.moves = int(f.readline())
            for row in f.read().splitlines():
                self.all_pos.append(list(row))
            self.row_count = len(self.all_pos)
            self.col_count = 0
        for i in range (0, len(self.all_pos)):
            self.in_col_count = 0
            for j in range (0, len(self.all_pos[i])):
                self.in_col_count += 1
                if (self.all_pos[i][j] in self.player_list):
                    self.player_pos = [i, j]
                if (self.all_pos[i][j] in self.wall_list):
                    self.wall_pos.append([i, j])
                if (self.all_pos[i][j] in self.ske_list):
                    self.ske_pos.append([i, j])
                if (self.all_pos[i][j] in self.stone_list):
                    self.stone_pos.append([i, j])
                if (self.all_pos[i][j] in self.goal_list):
                    self.goal_pos.append([i, j])
                if (self.all_pos[i][j] in self.key_list):
                    self.key_pos.append([i, j])
                if (self.all_pos[i][j] in self.lock_list):
                    self.lock_pos.append([i, j])
                if (self.all_pos[i][j] in self.holea_list):
                    self.holea_pos.append([i, j])
                if (self.all_pos[i][j] in self.holeb_list):
                    self.holeb_pos.append([i, j])
                if (self.all_pos[i][j] in self.spike_list):
                    self.spike_pos.append([i, j])
            self.col_count = max(self.in_col_count, self.col_count)
        self.row_count = int((14 - self.row_count)/2)
        self.col_count = int((26 - self.col_count)/2)
                
        
class Board:
    def __init__(self):
        self.sett = Settings()
        self.obj = Object()
        self.screen = pygame.display.set_mode((self.sett.width, self.sett.height))
        pygame.display.set_caption("SUSUSUSUSUSUS")
        pygame.mouse.set_visible(False)
        
    def _draw_main_menu(self):
        self.screen.blit(self.sett.background, (0, 0))
        if(self.obj.menu == 2):
            self.screen.blit(self.sett.main_menu.render("Bắt đầu", False, (255, 255, 255)), (11 * 50, 6 * 50))
            self.screen.blit(self.sett.main_menu.render("Hardcore", False, (255, 255, 255)), (11 * 50, 7 * 50))
            self.screen.blit(self.sett.main_menu.render("Hướng dẫn", False, (255, 255, 255)), (11 * 50, 8 * 50))
            self.screen.blit(self.sett.main_menu.render("Credit", False, (255, 255, 255)), (11 * 50, 9 * 50))
            self.screen.blit(self.sett.main_menu.render("Minigame Tết", False, (255, 255, 255)), (11 * 50, 10 * 50))
            self.screen.blit(self.sett.main_menu_2.render("SPACE để chọn", False, (255, 255, 255)), (12 * 50, 12 * 50))
            self.screen.blit(self.sett.player, (self.obj.player_pos[1] * 50, self.obj.player_pos[0] * 50))
            self.screen.blit(self.sett.ingame.render("SUSUSUSUSUSUS", False, (255, 255, 255)), (2.5 * 50, 0.5 * 50))
        elif(self.obj.menu == 1):
            self.screen.blit(self.sett.tutorial.render("Giải cứu công chúa để qua màn", False, (255, 255, 255)), (5 * 50, 2 * 50))
            self.screen.blit(pygame.transform.scale(self.sett.goal, (100, 100)), (7 * 50, 3.5 * 50))
            self.screen.blit(self.sett.tutorial.render("Đẩy Người Xương vào Đá", False, (255, 255, 255)), (15 * 50, 2 * 50))
            self.screen.blit(self.sett.tutorial.render("hoặc Tường để giết", False, (255, 255, 255)), (15 * 50, 3 * 50))
            self.screen.blit(pygame.transform.scale(self.sett.ske, (75, 75)), (15 * 50, 5 * 50))
            self.screen.blit(pygame.transform.scale(self.sett.stone, (75, 75)), (18 * 50, 4 * 50))
            self.screen.blit(pygame.transform.scale(self.sett.wall, (75, 75)), (18 * 50, 6 * 50))
            self.screen.blit(self.sett.tutorial.render("Nhặt chìa khoá để mở vật cản", False, (255, 255, 255)), (5 * 50, 7 * 50))
            self.screen.blit(pygame.transform.scale(self.sett.key, (75, 75)), (6 * 50, 9 * 50))
            self.screen.blit(pygame.transform.scale(self.sett.lock, (75, 75)), (9 * 50, 9 * 50))
            self.screen.blit(self.sett.tutorial.render("Cẩn thận hố gai", False, (255, 255, 255)), (15 * 50, 8 * 50))
            if((pygame.time.get_ticks() % 2000) in range(0, 1001)):
                self.screen.blit(pygame.transform.scale(self.sett.spike, (75, 75)), (16 * 50, 9 * 50))
            else:
                self.screen.blit(pygame.transform.scale(self.sett.unspike, (75, 75)), (16 * 50, 9 * 50))
            self.screen.blit(self.sett.main_menu_2.render("SPACE để tiếp tục", False, (255, 255, 255)), (12 * 50, 12 * 50))
            """elif(self.obj.menu == 3):
            self.screen.blit(self.sett.main_menu.render("", False, (255, 255, 255)), (11 * 50, 5 * 50))
            self.screen.blit(self.sett.main_menu.render("", False, (255, 255, 255)), (11 * 50, 6 * 50))
            self.screen.blit(self.sett.main_menu.render("", False, (255, 255, 255)), (11 * 50, 6 * 50))
            self.screen.blit(self.sett.main_menu.render("", False, (255, 255, 255)), (11 * 50, 6 * 50))
            self.screen.blit(self.sett.main_menu_2.render("SPACE để tiếp tục", False, (255, 255, 255)), (10 * 50, 12 * 50))"""
        elif(self.obj.menu == 4):
            self.screen.blit(self.sett.main_menu_2.render("SPACE để quay lại", False, (255, 255, 255)), (12 * 50, 12 * 50))
            self.screen.blit(self.sett.main_menu_2.render("Time: ", False, (255, 255, 255)), (16 * 50, 12 * 50))
            self.screen.blit(self.sett.main_menu_2.render(str(self.obj.event_time_now), False, (255, 255, 255)), (17 * 50, 12 * 50))
            if(pygame.mouse.get_pos()[0] in range(0, 1250) and pygame.mouse.get_pos()[1] in range (0, 650)):
                self.obj.event_player_pos = pygame.mouse.get_pos()
            self.screen.blit(self.sett.player, self.obj.event_player_pos)
            if(self.obj.event_lose):
                self.screen.blit(self.sett.ingame.render("Tết này bạn đã nghèo", False, (255, 255, 255)), (0.3 * 50, 5.5 * 50))
            else:
                if((pygame.time.get_ticks() % self.obj.event_spawn) == 0):
                    self.spawn = [random.randint(10, 1290), random.randint(10, 690)]
                    if(math.dist((self.spawn[0]+15, self.spawn[1]+10), (self.obj.event_player_pos[0]+25,self.obj.event_player_pos[1]+25)) > 200): 
                        self.obj.event_pos.append(self.spawn)
                for pos in self.obj.event_pos:
                    self.screen.blit(self.sett.main_menu_2.render("nghèo", False, (255, 255, 255)), (pos[0], pos[1]))
                    if(pos[0] > self.obj.event_player_pos[0]):
                        pos[0] -= (self.obj.event_speed*1.1)
                    elif(pos[0] < self.obj.event_player_pos[0]):
                        pos[0] += (self.obj.event_speed*1.1)
                    if(pos[1] > self.obj.event_player_pos[1]):
                        pos[1] -= self.obj.event_speed
                    elif(pos[1] < self.obj.event_player_pos[1]):
                        pos[1] += self.obj.event_speed
                    if(math.dist((pos[0]+15, pos[1]+10), (self.obj.event_player_pos[0]+25,self.obj.event_player_pos[1]+25)) < 25):
                        self.obj.event_lose = True
            if((pygame.time.get_ticks() % 7000) == 0):
                if(self.obj.event_spawn > 20):
                    self.obj.event_spawn -= 20
                self.obj.event_speed += 0.04
            if((pygame.time.get_ticks() - self.obj.event_time) % 1000 == 0):
                self.obj.event_time_now += 1
        
    def _draw_board(self):
        self.screen.blit(self.sett.background, (0, 0))
        self.screen.blit(self.sett.main_menu_2.render("ESC để quay lại", False, (255, 255, 255)), (12 * 50, 12.5 * 50))
        if(self.obj.moves > 9):
            self.screen.blit(self.sett.ingame.render(str(self.obj.moves), False, (255, 255, 255)), (1.3 * 50, 9 * 50))
        else:
            self.screen.blit(self.sett.ingame.render(str(self.obj.moves), False, (255, 255, 255)), (2 * 50, 9 * 50))
        if(self.obj.level < 10):
            self.screen.blit(self.sett.ingame.render(str(self.obj.level), False, (255, 255, 255)), (22.5 * 50, 9 * 50))
        else:
            self.screen.blit(self.sett.ingame.render(str(self.obj.level), False, (255, 255, 255)), (22 * 50, 9 * 50))
        for pos in self.obj.spike_pos:
            self.screen.blit(self.sett.spike, ((pos[1] + self.obj.col_count) * 50, (pos[0] + self.obj.row_count) * 50))
        if(self.obj.popup):
            for pos in self.obj.holeb_pos:
                self.screen.blit(self.sett.spike, ((pos[1] + self.obj.col_count) * 50, (pos[0] + self.obj.row_count) * 50))
            for pos in self.obj.holea_pos:
                self.screen.blit(self.sett.unspike, ((pos[1] + self.obj.col_count) * 50, (pos[0] + self.obj.row_count) * 50))
        else:
            for pos in self.obj.holea_pos:
                self.screen.blit(self.sett.spike, ((pos[1] + self.obj.col_count) * 50, (pos[0] + self.obj.row_count) * 50))
            for pos in self.obj.holeb_pos:
                self.screen.blit(self.sett.unspike, ((pos[1] + self.obj.col_count) * 50, (pos[0] + self.obj.row_count) * 50))
        for pos in self.obj.key_pos:
            self.screen.blit(self.sett.key, ((pos[1] + self.obj.col_count) * 50, (pos[0] + self.obj.row_count) * 50))
        for pos in self.obj.stone_pos:
            self.screen.blit(self.sett.stone, ((pos[1] + self.obj.col_count) * 50, (pos[0] + self.obj.row_count) * 50))
        for pos in self.obj.wall_pos:
            self.screen.blit(self.sett.wall, ((pos[1] + self.obj.col_count) * 50, (pos[0] + self.obj.row_count) * 50))
        for pos in self.obj.goal_pos:
            self.screen.blit(self.sett.goal, ((pos[1] + self.obj.col_count) * 50, (pos[0] + self.obj.row_count) * 50))
        for pos in self.obj.ske_pos:
            self.screen.blit(self.sett.ske, ((pos[1] + self.obj.col_count) * 50, (pos[0] + self.obj.row_count) * 50))
        for pos in self.obj.lock_pos:
            self.screen.blit(self.sett.lock, ((pos[1] + self.obj.col_count) * 50, (pos[0] + self.obj.row_count) * 50))
        self.screen.blit(self.sett.player, ((self.obj.player_pos[1] + self.obj.col_count) * 50, (self.obj.player_pos[0] + self.obj.row_count) * 50))
        
    def move(self, dir):
        next_move = [self.obj.player_pos[0] + dir[1], self.obj.player_pos[1] + dir[0]]
        if((self.obj.player_pos in self.obj.spike_pos) or ((self.obj.player_pos in self.obj.holea_pos) and (self.obj.popup == True)) or ((self.obj.player_pos in self.obj.holeb_pos) and (self.obj.popup == False))):
            stand_spike = True
        else:
            stand_spike = False
        if(next_move in self.obj.wall_pos):
            touch_wall = True
        else:
            touch_wall = False
        if(next_move in self.obj.stone_pos):
            touch_stone = True
        else:
            touch_stone = False
        if(next_move in self.obj.ske_pos):
            touch_ske = True
        else:
            touch_ske = False
        if(next_move in self.obj.key_pos):
            touch_key = True
        else:
            touch_key = False
        if(next_move in self.obj.lock_pos):
            touch_lock = True
        else:
            touch_lock = False
        if((next_move in self.obj.spike_pos) or ((next_move in self.obj.holea_pos) and (self.obj.popup == True)) or ((next_move in self.obj.holeb_pos) and (self.obj.popup == False))):
            touch_spike = True
        else:
            touch_spike = False
        if(next_move in self.obj.goal_pos):
            touch_goal = True
        else:
            touch_goal = False
        ske_counts = -1
        for pos in self.obj.ske_pos:
            ske_counts += 1
            if(((pos in self.obj.holea_pos) and (self.obj.popup == True)) or ((pos in self.obj.holeb_pos) and (self.obj.popup == False))):
                del self.obj.ske_pos[ske_counts]
        if(touch_goal):
            self.obj.player_pos = [self.obj.player_pos[0] + dir[1], self.obj.player_pos[1] + dir[0]]
            self.obj.level += 1
            self.obj.__init__()
        elif(touch_stone):
            stone_count = -1
            for pos in self.obj.stone_pos:
                stone_count += 1
                if(next_move == pos):
                    next_stone = [pos[0] + dir[1], pos[1] + dir[0]]
                    if(next_stone not in (self.obj.wall_pos + self.obj.stone_pos + self.obj.ske_pos + self.obj.lock_pos + self.obj.goal_pos)):
                        self.obj.stone_pos[stone_count] = next_stone
                    if(stand_spike):
                        self.act(0, dir)
                    self.act(2, dir)
        elif(touch_ske):
            ske_count = -1
            for pos in self.obj.ske_pos:
                ske_count += 1
                if(next_move == pos):
                    next_ske = [pos[0] + dir[1], pos[1] + dir[0]]
                    if(next_ske in self.obj.goal_pos):
                        ""
                    else:
                        if(next_ske not in (self.obj.wall_pos + self.obj.stone_pos + self.obj.ske_pos + self.obj.lock_pos + self.obj.spike_pos)):
                            if(((next_ske in self.obj.holea_pos) and (self.obj.popup == True)) or ((next_ske in self.obj.holeb_pos) and (self.obj.popup == False))):
                                del self.obj.ske_pos[ske_count]
                            else:
                                self.obj.ske_pos[ske_count] = next_ske
                        else:
                            del self.obj.ske_pos[ske_count]
                        self.act(2, dir)
                    if(stand_spike):
                        self.act(0, dir)                     
        elif(touch_key):
            key_count = -1
            for pos in self.obj.key_pos:
                key_count += 1
                if(next_move == pos):
                    del self.obj.key_pos[key_count]
                    self.obj.getkey = True
                    if(touch_spike):
                        self.act(0, dir)
                    self.act(1, dir)
        elif(touch_lock):
            lock_count = -1
            for pos in self.obj.lock_pos:
                lock_count += 1
                if(next_move == pos):
                    if(self.obj.getkey):
                        del self.obj.lock_pos[lock_count]
                        self.obj.getkey = False
                        self.act(1, dir)
        elif(touch_spike):
            self.act(0, dir)
            self.act(1, dir)
        elif(not touch_wall):
            if(self.obj.level == 0):
                if((self.obj.menu == 2) and (dir[1] != 0)):
                    if(self.obj.choose + dir[1] in range(1, 6)):
                        self.obj.player_pos = next_move
                        self.obj.choose += dir[1]
                """elif(self.obj.menu == 3):
                    if(dir[1] != 0):
                        if(self.obj.choose + dir[1] in range(1, 3)):
                            self.obj.player_pos = next_move
                            self.obj.choose += dir[1]
                    elif(self.obj.choose == 1):
                        if(self.obj.reso + dir[0] in range(0, 7)):
                            self.sett.width = self.sett.reso_list[self.obj.reso+dir[0]][0]
                            self.sett.height = self.sett.reso_list[self.obj.reso+dir[0]][1]
                            self.obj.reso += dir[0]"""   
            else:
                self.act(1, dir)
                
    """def move(self, dir):
        counts = -1
        for pos in self.obj.ske_pos:
            counts += 1
            if(((pos in self.obj.holea_pos) and (self.obj.popup == True)) or ((pos in self.obj.holeb_pos) and (self.obj.popup == False))):
                del self.obj.ske_pos[counts]
        next_move = [self.obj.player_pos[0] + dir[1], self.obj.player_pos[1] + dir[0]]
        if(next_move in self.obj.goal_pos):
            self.obj.player_pos = [self.obj.player_pos[0] + dir[1], self.obj.player_pos[1] + dir[0]]
            self.obj.level += 1
            self.obj.__init__()
        elif(next_move in self.obj.lock_pos):
            count = -1
            for pos in self.obj.lock_pos:
                count += 1
                if(next_move == pos):
                    if(self.obj.getkey):
                        del self.obj.lock_pos[count]
                        self.obj.getkey = False
                        self.act(1, dir)
        elif(next_move in self.obj.stone_pos):
            count = -1
            for pos in self.obj.stone_pos:
                count += 1
                if(next_move == pos):
                    next_stone = [pos[0] + dir[1], pos[1] + dir[0]]
                    if((next_stone not in self.obj.wall_pos) and (next_stone not in self.obj.goal_pos) and (next_stone not in self.obj.stone_pos) and (next_stone not in self.obj.ske_pos) and (next_stone not in self.obj.lock_pos)):
                        self.obj.stone_pos[count] = [pos[0] + dir[1], pos[1] + dir[0]]
                        #self.obj.player_pos = [self.obj.player_pos[0] + dir[1], self.obj.player_pos[1] + dir[0]]
                    if((self.obj.player_pos in self.obj.spike_pos) or ((self.obj.player_pos in self.obj.holea_pos) and (self.obj.popup == True)) or ((self.obj.player_pos in self.obj.holeb_pos) and (self.obj.popup == False))):
                        self.act(0, dir)   
                    self.act(2, dir)
        elif(next_move in self.obj.ske_pos):
            count = -1
            for pos in self.obj.ske_pos:
                count += 1
                if(next_move == pos):
                    next_ske = [pos[0] + dir[1], pos[1] + dir[0]]
                    if((next_ske not in self.obj.wall_pos) and (next_ske not in self.obj.stone_pos) and (next_ske not in self.obj.ske_pos) and (next_ske not in self.obj.spike_pos) and (next_ske not in self.obj.lock_pos) and (next_ske not in self.obj.goal_pos) and ((next_move not in self.obj.holea_pos) and (self.obj.popup == False)) and ((next_move in self.obj.holeb_pos) and (self.obj.popup == True))):
                        self.obj.ske_pos[count] = [pos[0] + dir[1], pos[1] + dir[0]]
                        #self.obj.player_pos = [self.obj.player_pos[0] + dir[1], self.obj.player_pos[1] + dir[0]]
                        if((self.obj.player_pos in self.obj.spike_pos) or ((self.obj.player_pos in self.obj.holea_pos) and (self.obj.popup == False)) or ((self.obj.player_pos in self.obj.holeb_pos) and (self.obj.popup == True))):
                            self.act(0, dir)
                        self.act(2, dir)
                    elif((next_ske in self.obj.wall_pos) or (next_ske in self.obj.goal_pos) or (next_ske in self.obj.ske_pos) or (next_ske in self.obj.stone_pos) or (next_ske in self.obj.spike_pos) or ((next_move in self.obj.holea_pos) and (self.obj.popup == True)) or ((next_move in self.obj.holeb_pos) and (self.obj.popup == False))):
                        del self.obj.ske_pos[count]
                        #self.obj.player_pos = [self.obj.player_pos[0] + dir[1], self.obj.player_pos[1] + dir[0]]
                        self.act(2, dir)
        elif(next_move in self.obj.spike_pos):
            self.act(1, dir)
            self.act(0, dir)
        elif(((next_move in self.obj.holea_pos) and (self.obj.popup == True)) or ((next_move in self.obj.holeb_pos) and (self.obj.popup == False))):
            self.act(1, dir)
            self.act(0, dir)
        elif(next_move in self.obj.key_pos):
            count = -1
            for pos in self.obj.key_pos:
                count += 1
                if(next_move == pos):
                    del self.obj.key_pos[count]
                    self.obj.getkey = True
                    self.act(1, dir)
        elif(next_move not in self.obj.wall_pos):
            self.act(1, dir)"""

    def act(self, possive, dir):
        if(possive == 1):
            self.obj.player_pos = [self.obj.player_pos[0] + dir[1], self.obj.player_pos[1] + dir[0]]
            self.obj.moves -= 1
            self.obj.popup = not self.obj.popup
        elif(possive == 2):
            self.obj.moves -= 1
            self.obj.popup = not self.obj.popup
        else:
            self.obj.moves -=1
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if(self.obj.level == 0):
                        if event.key in self.sett.KEY_DIR:
                            self.move(self.sett.KEY_DIR[event.key])
                        if event.key == pygame.K_SPACE:
                            if(self.obj.menu == 2):
                                if(self.obj.choose == 1):
                                    self.obj.level += 1
                                    self.obj.__init__()
                                    self.hardcore = False
                                elif(self.obj.choose == 2):
                                    self.obj.level += 1
                                    self.obj.__init__()
                                    self.hardcore = True
                                elif(self.obj.choose == 3):
                                    self.obj.menu -= 1
                                    """elif(self.obj.choose == 4):
                                    self.obj.menu += 1
                                    self.obj.choose = 1
                                    self.obj.player_pos = [self.obj.player_pos[0] - 2, self.obj.player_pos[1]]"""
                                elif(self.obj.choose == 5):
                                    self.obj.menu += 2
                                    self.obj.event_time = pygame.time.get_ticks()
                                    pygame.mixer.music.play(loops=-1)
                            elif(self.obj.menu == 1):
                                self.obj.menu += 1
                                self.obj.choose = 1
                                self.obj.player_pos = [self.obj.player_pos[0] - 2, self.obj.player_pos[1]]
                                """elif(self.obj.menu == 3):
                                if(self.obj.choose == 2):
                                    self.obj.menu -= 1
                                    self.obj.choose = 1
                                    self.obj.player_pos = [self.obj.player_pos[0] - 1, self.obj.player_pos[1]]"""
                            elif(self.obj.menu == 4):
                                self.obj.__init__()
                                pygame.mixer.music.stop()
                                """self.obj.choose = 1
                                self.obj.player_pos = [self.obj.player_pos[0] - 2, self.obj.player_pos[1]]"""
                    else:
                        if event.key in self.sett.KEY_DIR:
                            self.move(self.sett.KEY_DIR[event.key])
                        elif event.key == pygame.K_ESCAPE:
                            self.obj.level = 0
                            self.obj.__init__()
                        elif(not self.hardcore):
                            if event.key == pygame.K_r:
                                self.obj.__init__()
                            elif event.key == pygame.K_l:
                                self.obj.moves +=10
                            elif event.key == pygame.K_z:
                                self.obj.level += 1
                                self.obj.__init__()
                            elif event.key == pygame.K_t:
                                self.obj.level = 10
                                self.obj.__init__()
                        
            if (int(self.obj.moves) <= 0):
                if(self.hardcore):
                    self.obj.level = 1
                self.obj.__init__()
            if(self.obj.level == 0):
                self._draw_main_menu()
            else:
                self._draw_board()
            pygame.display.update()
            #(pygame.time.Clock()).tick(300)


myLevel = Board()
myLevel.run()

