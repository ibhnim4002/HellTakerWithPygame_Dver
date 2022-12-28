import pygame
import random
import math

pygame.init()

class Settings:
    def __init__(self):
        self.timer = pygame.time.Clock()
        self.fps = 60
        self.width = 1300
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.image.load('assets/backgrounds/background.png').convert_alpha()
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.loser = pygame.image.load('assets/backgrounds/loser.png').convert_alpha()
        self.loser = pygame.transform.scale(self.loser, (self.width, self.height))
        self.succ = pygame.image.load('assets/backgrounds/success.png').convert_alpha()
        self.succ = pygame.transform.scale(self.succ, (self.width, self.height))
        self.ending = pygame.image.load('assets/backgrounds/ending_8.png').convert_alpha()
        self.ending = pygame.transform.scale(self.ending, (self.width, self.height))
        self.secret = pygame.image.load('assets/backgrounds/secret.jpg').convert_alpha()
        self.secret = pygame.transform.scale(self.secret, (self.width, self.height))
        self.hud = pygame.image.load('assets/backgrounds/hud.png').convert_alpha()
        self.hud = pygame.transform.scale(self.hud, (self.width, self.height))
        self.cutscenes = pygame.image.load('assets/cutscenes/cutscenes_0.png').convert_alpha()
        self.cutscenes = pygame.transform.scale(self.cutscenes, (200, 200))
        self.box = pygame.image.load('assets/backgrounds/dialog_box.png').convert_alpha()
        self.box = pygame.transform.scale(self.box, (self.width, 300))
        self.player = pygame.image.load('assets/objects/player/player.png').convert_alpha()
        self.player = pygame.transform.scale(self.player, (50, 50))
        self.player_kill = pygame.image.load('assets/objects/player/player_kill_1.png').convert_alpha()
        self.player_kill = pygame.transform.scale(self.player_kill, (50, 50))
        self.player_touch = pygame.image.load('assets/objects/player/player_touch_1.png').convert_alpha()
        self.player_touch = pygame.transform.scale(self.player_touch, (50, 50))
        self.player_walk = pygame.image.load('assets/objects/player/player_walk_1.png').convert_alpha()
        self.player_walk = pygame.transform.scale(self.player_walk, (50, 50))
        self.stone = pygame.image.load('assets/objects/stone.png').convert_alpha()
        self.stone = pygame.transform.scale(self.stone, (50, 50))
        self.wall = pygame.image.load('assets/objects/wall.png').convert_alpha()
        self.wall = pygame.transform.scale(self.wall, (50, 50))
        self.hwall = pygame.image.load('assets/objects/highwall.png').convert_alpha()
        self.hwall = pygame.transform.scale(self.hwall, (50, 50))
        self.goal = pygame.image.load('assets/objects/goal.png').convert_alpha()
        self.goal = pygame.transform.scale(self.goal, (50, 50))
        self.ske = pygame.image.load('assets/objects/skeleton/ske_idle_1.png').convert_alpha()
        self.ske = pygame.transform.scale(self.ske, (50, 50))
        self.ske_dead = pygame.image.load('assets/objects/skeleton/ske_dead_1.png').convert_alpha()
        self.ske_dead = pygame.transform.scale(self.ske_dead, (50, 50))
        self.spike = pygame.image.load('assets/objects/spike/spike_4.png').convert_alpha()
        self.spike = pygame.transform.scale(self.spike, (50, 50))
        self.key = pygame.image.load('assets/objects/key.png').convert_alpha()
        self.key = pygame.transform.scale(self.key, (50, 50))
        self.lock = pygame.image.load('assets/objects/lock/lock.png').convert_alpha()
        self.lock = pygame.transform.scale(self.lock, (50, 50))
        self.unlock = pygame.image.load('assets/objects/lock/unlock.png').convert_alpha()
        self.unlock = pygame.transform.scale(self.unlock, (50, 50))
        self.holea = pygame.image.load('assets/objects/spike/spike_4.png').convert_alpha()
        self.holea = pygame.transform.scale(self.holea, (50, 50))
        self.holeb = pygame.image.load('assets/objects/spike/spike_1.png').convert_alpha()
        self.holeb = pygame.transform.scale(self.holeb, (50, 50))
        self.sfx_spike = pygame.image.load('assets/objects/sfx/spike_1.png').convert_alpha()
        self.sfx_spike = pygame.transform.scale(self.sfx_spike, (50, 50))
        self.lvl_frame = pygame.image.load(f'assets/backgrounds/frame.png').convert_alpha()
        self.lvl_frame = pygame.transform.scale(self.lvl_frame, (100, 100))
        self.lvl_frame = pygame.transform.rotozoom(self.lvl_frame, 0, 1)
        self.lvl_lock = pygame.image.load('assets/backgrounds/lock.png').convert_alpha()
        self.lvl_lock = pygame.transform.scale(self.lvl_lock, (50, 50))
        self.quit = pygame.image.load('assets/backgrounds/quit.png').convert_alpha()
        self.quit = pygame.transform.scale(self.quit, (900, 75))
        self.arrow = pygame.image.load('assets/objects/Arrow-Keys.png').convert_alpha()
        self.arrow = pygame.transform.scale(self.arrow, (250, 200))
        self.lvl_frame_list = [[6, 4, 1], [10, 4, 2], [14, 4, 3], [18,4, 4], [6, 8, 5], [10, 8, 6], [14, 8, 7], [18, 8, 8]]
        self.KEY_DIR = {pygame.K_RIGHT: (1, 0), pygame.K_LEFT: (-1, 0), pygame.K_UP: (0, -1), pygame.K_DOWN: (0, 1)}
        self.event_list = {1: "nghèo", 2: "rớt môn", 3: "thấy crush lấy chồng", 4: "điểm thấp", 5: "chia tay", 6: "không được về quê", 7: "mất tiền"}
        self.ingame = pygame.font.Font('assets/font/CrimsonPro-VariableFont_wght.ttf', 150)
        self.title_1 = pygame.font.Font('assets/font/CrimsonPro-VariableFont_wght.ttf', 200)
        self.title_2 = pygame.font.Font('assets/font/CrimsonPro-VariableFont_wght.ttf', 95)
        self.minigame = pygame.font.Font('assets/font/CrimsonPro-VariableFont_wght.ttf', 100)
        self.tutorial = pygame.font.Font('assets/font/CrimsonPro-VariableFont_wght.ttf', 30)
        self.main_menu = pygame.font.Font('assets/font/CrimsonPro-VariableFont_wght.ttf', 50)
        self.main_menu_2 = pygame.font.Font('assets/font/CrimsonPro-VariableFont_wght.ttf', 20)
        pygame.mixer.music.load('assets/soundtracks/menu.mp3')
        pygame.mixer.music.play(loops = -1, fade_ms = 3000)
        self.snd_hurt = pygame.mixer.Sound('assets/soundtracks/hurt.mp3')
        self.snd_touch = pygame.mixer.Sound('assets/soundtracks/touch.mp3')
        self.snd_lvlup = pygame.mixer.Sound('assets/soundtracks/lvlup.mp3')
        self.snd_bad = pygame.mixer.Sound('assets/soundtracks/bad_end.mp3')
        self.snd_nut = pygame.mixer.Sound('assets/soundtracks/cracked_nut_end.mp3')
        self.snd_kill = pygame.mixer.Sound('assets/soundtracks/kill.mp3')
        self.snd_demon = pygame.mixer.Sound('assets/soundtracks/true_pink.mp3')
        self.snd_gun = pygame.mixer.Sound('assets/soundtracks/gun_shot.mp3')

class Object:
    wall_list = ['#']
    hwall_list = ['$']
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
        self.hwall_pos = []
        self.ske_pos = []
        self.ske_dead_pos = []
        self.stone_pos = []
        self.spike_pos = []
        self.holea_pos = []
        self.holeb_pos = []
        self.key_pos = []
        self.lock_pos = []
        self.player_pos = []
        self.player_kill_pos = []
        self.player_touch_pos = []
        self.player_walk_pos = []
        self.player_walk_dir = []
        self.cre = []
        self.goal_pos = []
        self.getkey = False
        self.unlock = False
        self.popup = True
        self.choose = 1
        self.menu = 1
        self.lvl_choose = 1
        self.lvl_state = 1
        self.player_flip = False
        self.hurt = False
        self.walk = False
        self.level_list = []
        self.event_pos = []
        self.event_lose = False
        self.event_lose_by = 1
        self.event_spawn = 4
        self.event_spawn_check = True
        self.event_speed = 0.6
        self.event_time = 0
        self.event_time_now = 0
        self.event_time_old = 0
        self.quit = False
        self.levelup = False
        self.secret = False
        self.final = False
        self.cutscenes = 0
        self.final_choose = 1
        self.final_score = 0
        self.fchoose_1 = []
        self.fchoose_2 = []
        self.fscript_0 = []
        self.fscript_1 = []
        self.fscript_2 = []
        self.ending = []
        self.change = False
        self.vision = []
        if(self.level == 9):
            self.level = 0
        if(self.level > 10):
            self.level = 1
        with open('assets/ending.txt', 'r', encoding = 'utf-8-sig') as f:
            self.cutscenes = int(f.readline())
            for i in range (0, self.cutscenes):
                self.fscript_0.append(str(f.readline()))
                self.fscript_0[i] = self.fscript_0[i][0:len(self.fscript_0[i])-1]
            for i in range (0, self.cutscenes):
                self.fscript_1.append(f.readline())
                self.fscript_1[i] = self.fscript_1[i][0:len(self.fscript_1[i])-1]
            for i in range (0, self.cutscenes):
                self.fchoose_1.append(int(f.readline()))
            for i in range (0, self.cutscenes):
                self.fscript_2.append(f.readline())
                self.fscript_2[i] = self.fscript_2[i][0:len(self.fscript_2[i])-1]
            for i in range (0, self.cutscenes):
                self.fchoose_2.append(int(f.readline()))
            for i in range (0, self.cutscenes):
                self.vision.append(int(f.readline()))
            for row in f.read().splitlines():
                self.ending.append(int(row))
        with open('levels/lvl.txt', 'r') as f:
            for row in f.read().splitlines():
                self.level_list.append(int(row))
        self.cre_count = 0
        self.cre_y = 14
        with open(f'credits.txt', mode = 'r', encoding = 'utf-8-sig') as f:
            for row in f.read().splitlines():
                self.cre.append([self.cre_count, self.cre_y, str(row)])
                self.cre_count += 1
                self.cre_y += 1
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
                if(self.all_pos[i][j] in self.player_list):
                    self.player_pos = [i, j]
                if(self.all_pos[i][j] in self.wall_list):
                    self.wall_pos.append([i, j])
                if(self.all_pos[i][j] in self.hwall_list):
                    self.hwall_pos.append([i, j])
                if(self.all_pos[i][j] in self.ske_list):
                    self.ske_pos.append([i, j])
                if(self.all_pos[i][j] in self.stone_list):
                    self.stone_pos.append([i, j])
                if(self.all_pos[i][j] in self.goal_list):
                    self.goal_pos.append([i, j])
                if(self.all_pos[i][j] in self.key_list):
                    self.key_pos.append([i, j])
                if(self.all_pos[i][j] in self.lock_list):
                    self.lock_pos.append([i, j])
                if(self.all_pos[i][j] in self.holea_list):
                    self.holea_pos.append([i, j])
                if(self.all_pos[i][j] in self.holeb_list):
                    self.holeb_pos.append([i, j])
                if(self.all_pos[i][j] in self.spike_list):
                    self.spike_pos.append([i, j])
            self.col_count = max(self.in_col_count, self.col_count)
        self.row_count = int((14 - self.row_count)/2)
        self.col_count = int((26 - self.col_count)/2)
                
        
class Board:
    def __init__(self):
        self.sett = Settings()
        self.obj = Object()
        pygame.display.set_caption("SUStalker")
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)
        self.ske_idle_idx = 1
        self.ske_dead_idx = 1
        self.player_kill_idx = 1
        self.player_touch_idx = 1
        self.player_walk_idx = 1
        self.sfx_spike_idx = 1
        self.holea_idx = 1
        self.holeb_idx = 4.8
        self.react = 0
        self.next_ske_pos = 0
        self.next_ske_loc = []
        self.check_ske = False
        self.next_stone_pos = 0
        self.next_stone_loc =[]
        self.check_stone = False
        self.event_player_rect = self.sett.player.get_rect(center = (650, 350))
        self.holea_popup = False
        self.holeb_popup = False
        self.cre_list = []
        for row in self.obj.cre:
            self.cre_list.append(self.sett.main_menu.render(row[2], False, (192, 192, 192)).get_rect(center = (650, 350)))
        self.cre_run = 0
        self.snd_hurt = False
        self.snd_touch = False
        self.true_win = False

    def _sprite(self):
        self.ske_idle_idx += 0.3
        self.ske_idle_idx_int = int(self.ske_idle_idx)
        self.sett.ske = pygame.image.load(f'assets/objects/skeleton/ske_idle_{self.ske_idle_idx_int}.png').convert_alpha()
        self.sett.ske = pygame.transform.scale(self.sett.ske, (50, 50))
        if(self.ske_idle_idx >= 11.69):
            self.react += 1
            if(self.react < 6):
                self.ske_idle_idx = 1
            elif(self.ske_idle_idx >= 15.69):
                self.ske_idle_idx = 1
                self.react = 0
        self.ske_dead_idx += 0.48
        self.ske_dead_idx_int = int(self.ske_dead_idx)
        self.sett.ske_dead = pygame.image.load(f'assets/objects/skeleton/ske_dead_{self.ske_dead_idx_int}.png').convert_alpha()
        self.sett.ske_dead = pygame.transform.scale(self.sett.ske_dead, (50, 50))
        if(self.ske_dead_idx >= 15.51):
            self.ske_dead_idx = 1
            self.obj.ske_dead_pos.clear()
        self.player_kill_idx += 0.8
        self.player_kill_idx_int = int(self.player_kill_idx)
        self.sett.player_kill = pygame.image.load(f'assets/objects/player/player_kill_{self.player_kill_idx_int}.png').convert_alpha()
        self.sett.player_kill = pygame.transform.scale(self.sett.player_kill, (50, 50))
        if(self.player_kill_idx >= 48.19):
            self.player_kill_idx = 1
            self.obj.player_kill_pos.clear()
        self.player_touch_idx += 1
        self.player_touch_idx_int = int(self.player_touch_idx)
        self.sett.player_touch = pygame.image.load(f'assets/objects/player/player_touch_{self.player_touch_idx_int}.png').convert_alpha()
        self.sett.player_touch = pygame.transform.scale(self.sett.player_touch, (50, 50))
        if(self.player_touch_idx >= 39):
            self.player_touch_idx = 1
            self.obj.player_touch_pos.clear()
        if(self.player_touch_idx >= 16):
            if(self.snd_touch):
                self.sett.snd_touch.play(loops = 1)
                self.snd_touch = False
            if(self.check_ske):
                self.obj.ske_pos[self.next_ske_pos] = self.next_ske_loc
                self.check_ske = False
            if(self.check_stone):
                self.obj.stone_pos[self.next_stone_pos] = self.next_stone_loc
                self.check_stone = False
        if(not self.obj.walk):
            self.sfx_spike_idx += 0.8
            self.sfx_spike_idx_int = int(self.sfx_spike_idx)
            self.sett.sfx_spike = pygame.image.load(f'assets/objects/sfx/spike_{self.sfx_spike_idx_int}.png').convert_alpha()
            self.sett.sfx_spike = pygame.transform.scale(self.sett.sfx_spike, (50, 50))
            if(self.snd_hurt):
                self.sett.snd_hurt.play()
                self.snd_hurt = False
            if(self.sfx_spike_idx >= 8.19):
                self.sfx_spike_idx = 1
                self.obj.hurt = False
        if(self.holea_popup):
            self.holea_idx += 0.4
            self.holea_idx_int = int(self.holea_idx)
            self.sett.holea = pygame.image.load(f'assets/objects/spike/spike_{self.holea_idx_int}.png').convert_alpha()
            self.sett.holea = pygame.transform.scale(self.sett.holea, (50, 50))
            if(self.holea_idx >= 4.59):
                self.holea_idx = 1
                self.holea_popup = False
        if(self.holeb_popup):
            self.holeb_idx -= 0.4
            self.holeb_idx_int = int(self.holeb_idx)
            self.sett.holeb = pygame.image.load(f'assets/objects/spike/spike_{self.holeb_idx_int}.png').convert_alpha()
            self.sett.holeb = pygame.transform.scale(self.sett.holeb, (50, 50))
            if(self.holeb_idx <= 1.41):
                self.holeb_idx = 4.6
                self.holeb_popup = False
        if(self.obj.walk):
            self.player_walk_idx += 0.8
            self.obj.player_walk_pos = [self.obj.player_walk_pos[0] + self.obj.player_walk_dir[1]*0.07, self.obj.player_walk_pos[1] + self.obj.player_walk_dir[0]*0.07]
            self.player_walk_idx_int = int(self.player_walk_idx)
            self.sett.player_walk = pygame.image.load(f'assets/objects/player/player_walk_{self.player_walk_idx_int}.png').convert_alpha()
            self.sett.player_walk = pygame.transform.scale(self.sett.player_walk, (50, 50))
            if(self.player_walk_idx >= 12.19):
                self.player_walk_idx = 1
                self.obj.player_walk_pos.clear()
                self.obj.player_walk_dir.clear()
                self.obj.walk = False
        if(self.obj.change):
            self.sett.cutscenes = pygame.image.load(f'assets/cutscenes/cutscenes_{self.obj.final_score}.png').convert_alpha()
            self.sett.cutscenes = pygame.transform.scale(self.sett.cutscenes, (400, 400))
            self.obj.change = False
                
    def _draw_main_menu(self):
        self.sett.screen.blit(self.sett.background, (0, 0))
        if(self.obj.menu == 1):
            if(self.obj.quit):
                self.sett.screen.blit(self.sett.main_menu.render("Ở lại đi mà", False, (192, 192, 192)), (11 * 50, 4 * 50))
                self.sett.screen.blit(self.sett.main_menu.render("Ô kê", False, (192, 192, 192)), (10 * 50, 7 * 50))
                self.sett.screen.blit(self.sett.main_menu.render("Khồng", False, (192, 192, 192)), (15 * 50, 7 * 50))
                self.sett.screen.blit(self.sett.player, (self.obj.player_pos[1] * 50, self.obj.player_pos[0] * 50))
                self.sett.screen.blit(self.sett.quit, (4 * 50, 10 * 50))
            else:
                self.sett.screen.blit(self.sett.main_menu.render("Game mới", False, (192, 192, 192)), (11 * 50, 5 * 50))
                self.sett.screen.blit(self.sett.main_menu.render("Chọn màn", False, (192, 192, 192)), (11 * 50, 6 * 50))
                self.sett.screen.blit(self.sett.main_menu.render("Hướng dẫn", False, (192, 192, 192)), (11 * 50, 7 * 50))
                self.sett.screen.blit(self.sett.main_menu.render("Credit", False, (192, 192, 192)), (11 * 50, 8 * 50))
                self.sett.screen.blit(self.sett.main_menu.render("Minigame Tết", False, (192, 192, 192)), (11 * 50, 9 * 50))
                self.sett.screen.blit(self.sett.main_menu.render("Thoát", False, (192, 192, 192)), (11 * 50, 10 * 50))
                self.sett.screen.blit(self.sett.main_menu_2.render("SPACE để chọn", False, (192, 192, 192)), (11.5 * 50, 12 * 50))
                self.sett.screen.blit(self.sett.player, (self.obj.player_pos[1] * 50, self.obj.player_pos[0] * 50))
                self.sett.screen.blit(self.sett.title_1.render("S", False, (192, 192, 192)), (10 * 50, 0 * 50))
                self.sett.screen.blit(self.sett.title_2.render("Ú", False, (192, 192, 192)), (11.85 * 50, 0.75 * 50))
                self.sett.screen.blit(self.sett.title_2.render("talkẻ", False, (192, 192, 192)), (11.85 * 50, 2 * 50))
        elif(self.obj.menu == 2):
            for pos in self.sett.lvl_frame_list:
                self.sett.screen.blit(self.sett.lvl_frame, (pos[0] * 50, pos[1] * 50))
                self.sett.screen.blit(self.sett.main_menu.render(str(pos[2]), False, (192, 192, 192)), ((pos[0] + 0.82) * 50, (pos[1] + 2) * 50))
                if(not self.obj.level_list[pos[2]-1]):
                    self.sett.screen.blit(self.sett.lvl_lock, ((pos[0] + 0.5) * 50, (pos[1] + 0.5) * 50))
            self.sett.screen.blit(self.sett.player, (self.obj.player_pos[1] * 50, self.obj.player_pos[0] * 50))
            self.sett.screen.blit(self.sett.main_menu_2.render("SPACE để chọn, ESC để quay lại", False, (192, 192, 192)), (10.5 * 50, 12 * 50))
        elif(self.obj.menu == 3):
            self.sett.screen.blit(self.sett.tutorial.render("Phím mũi tên để di chuyển", False, (192, 192, 192)), (2 * 50, 2 * 50))
            self.sett.screen.blit(self.sett.arrow, (2.5 * 50, 2.5 * 50))
            self.sett.screen.blit(self.sett.tutorial.render("Giải cứu sú pónk để qua màn", False, (192, 192, 192)), (9 * 50, 2 * 50))
            self.sett.screen.blit(pygame.transform.scale(self.sett.goal, (100, 100)), (11.5 * 50, 3.5 * 50))
            self.sett.screen.blit(self.sett.tutorial.render("Dồn Người Xương vào Đá", False, (192, 192, 192)), (17 * 50, 2 * 50))
            self.sett.screen.blit(self.sett.tutorial.render("hoặc Tường để tiêu diệt", False, (192, 192, 192)), (17 * 50, 3 * 50))
            self.sett.screen.blit(pygame.transform.scale(self.sett.ske, (75, 75)), (17 * 50, 5 * 50))
            self.sett.screen.blit(pygame.transform.scale(self.sett.stone, (75, 75)), (20 * 50, 4 * 50))
            self.sett.screen.blit(pygame.transform.scale(self.sett.hwall, (75, 75)), (20 * 50, 6 * 50))
            self.sett.screen.blit(self.sett.tutorial.render("Nhặt dao để chém đối thủ", False, (192, 192, 192)), (5.5 * 50, 8 * 50))
            self.sett.screen.blit(pygame.transform.scale(self.sett.key, (75, 75)), (6 * 50, 9 * 50))
            self.sett.screen.blit(pygame.transform.scale(self.sett.lock, (75, 75)), (9 * 50, 9 * 50))
            self.sett.screen.blit(self.sett.tutorial.render("Cẩn thận hố gai", False, (192, 192, 192)), (15 * 50, 8 * 50))
            self.sett.screen.blit(pygame.transform.scale(self.sett.spike, (75, 75)), (16 * 50, 9 * 50))
            self.sett.screen.blit(self.sett.main_menu_2.render("SPACE để tiếp tục", False, (192, 192, 192)), (11.5 * 50, 12 * 50))
        elif(self.obj.menu == 4):
            for row in self.obj.cre:
                self.sett.screen.blit(self.sett.main_menu.render(row[2], False, (192, 192, 192)), (self.cre_list[row[0]].x, (row[1] - self.cre_run) * 50))
            self.sett.screen.blit(self.sett.main_menu_2.render("SPACE để tiếp tục", False, (192, 192, 192)), (11.5 * 50, 12 * 50))
            self.cre_run += 0.02
        elif(self.obj.menu == 5):
            self.sett.screen.blit(self.sett.main_menu_2.render("SPACE để quay lại", False, (192, 192, 192)), (11.5 * 50, 12 * 50))
            self.sett.screen.blit(self.sett.tutorial.render("Time: ", False, (192, 192, 192)), (16 * 50, 11.85 * 50))
            self.sett.screen.blit(self.sett.tutorial.render(str(self.obj.event_time_now), False, (192, 192, 192)), (17.6 * 50, 11.85 * 50))
            if(self.obj.event_lose):
                self.sett.screen.blit(self.sett.minigame.render("Tết này bạn đã", False, (192, 192, 192)), (3 * 50, 4 * 50))
                self.sett.screen.blit(self.sett.minigame.render(f"{self.sett.event_list[self.obj.event_lose_by]}", False, (192, 192, 192)), (3 * 50, 7 * 50))
            else:
                self.event_player_rect.center = pygame.mouse.get_pos()
                for pos in self.obj.event_pos:
                    self.sett.screen.blit(self.sett.main_menu_2.render(f"{self.sett.event_list[pos[1]]}", False, (pos[2], pos[3], pos[4])), pos[0])
                    if(pos[0].x > self.event_player_rect.center[0]):
                        pos[0].x -= (self.obj.event_speed*1.1)
                    elif(pos[0].x < self.event_player_rect.center[0]):
                        pos[0].x += (self.obj.event_speed*2*1.1)
                    if(pos[0].y > self.event_player_rect.center[1]):
                        pos[0].y -= self.obj.event_speed
                    elif(pos[0].y < self.event_player_rect.center[1]):
                        pos[0].y += (self.obj.event_speed*2)
                    if(pos[0].colliderect(self.event_player_rect)):
                        self.obj.event_lose = True
                        self.obj.event_lose_by = pos[1]
                if((self.obj.event_time_now % int(self.obj.event_spawn) == 0) and self.obj.event_spawn_check):
                    self.event()
                self.obj.event_time_now = int((pygame.time.get_ticks() - self.obj.event_time)/1000)
                if(self.obj.event_time_now > self.obj.event_time_old):
                    self.obj.event_time_old = self.obj.event_time_now
                    self.obj.event_spawn_check = True
            self.sett.screen.blit(self.sett.player, self.event_player_rect)
            
    def event(self):
        for i in range (0, random.randint(1, int(self.obj.event_spawn)+3)):
            self.spawn = [random.randint(-120, 1420), random.randint(-120, 820)]
            event = random.randint(1, 7)
            color_1 = random.randint(0, 255)
            color_2 = random.randint(0, 255)
            color_3 = random.randint(0, 255)
            new_spawn = self.sett.main_menu_2.render(f"{self.sett.event_list[event]}", False, (192, 192, 192)).get_rect(topleft = self.spawn)
            if(math.dist(new_spawn.center, self.event_player_rect.center) > 400):
                self.obj.event_pos.append([new_spawn, event, color_1, color_2, color_3])
        if(self.obj.event_spawn > 1.2):
            self.obj.event_spawn -= 0.15
        self.obj.event_speed += 0.03
        self.obj.event_spawn_check = False
                
    def _draw_board(self):
        if(self.obj.moves <= 0):
            if(self.obj.secret):
                self.sett.screen.blit(self.sett.secret, (0, 0))
                self.sett.screen.blit(self.sett.tutorial.render("R để chơi lại", False, (192, 192, 192)), (11.5 * 50, 11 * 50))
            else:
                self.sett.screen.blit(self.sett.loser, (0, 0))
                self.sett.screen.blit(self.sett.tutorial.render("R để chơi lại", False, (192, 192, 192)), (11.5 * 50, 11 * 50))
        elif(self.obj.levelup):
            if(self.obj.level == 8):
                for end in self.obj.ending:
                    if(self.obj.final_score == end):
                        self.sett.screen.blit(pygame.transform.scale(pygame.image.load(f'assets/backgrounds/ending_{end}.png').convert_alpha(), (self.sett.width, self.sett.height)), (0, 0))
            else:
                self.sett.screen.blit(self.sett.succ, (0, 0))
            self.sett.screen.blit(self.sett.tutorial.render("SPACE để tiếp tục", False, (192, 192, 192)), (11.5 * 50, 11 * 50))
        elif(self.obj.final):
            self.sett.screen.blit(self.sett.background, (0, 0))
            self.sett.screen.blit(self.sett.cutscenes, (self.sett.cutscenes.get_rect(center = (650, 350)).x, 50))
            self.sett.screen.blit(self.sett.box, (0, 400))
            self.sett.screen.blit(self.sett.main_menu.render(str(self.obj.fscript_0[self.obj.final_score]), False, (192, 192, 192)), (5 * 50, 8.5 * 50))
            self.sett.screen.blit(self.sett.tutorial.render(str(self.obj.fscript_1[self.obj.final_score]), False, (192, 192, 192)), (7 * 50, 10 * 50 + 15))
            self.sett.screen.blit(self.sett.tutorial.render(str(self.obj.fscript_2[self.obj.final_score]), False, (192, 192, 192)), (7 * 50, 11 * 50 + 15))
            self.sett.screen.blit(self.sett.main_menu_2.render("SPACE để tiếp tục", False, (192, 192, 192)), (11.5 * 50, 13 * 50))
            if(self.obj.vision[self.obj.final_score]):
                self.sett.screen.blit(self.sett.player, (self.obj.player_pos[1] * 50, self.obj.player_pos[0] * 50))       
        else:
            self.sett.screen.blit(self.sett.background, (0, 0))
            self.sett.screen.blit(self.sett.hud, (0, 0))
            if(self.obj.moves > 9):
                self.sett.screen.blit(self.sett.ingame.render(str(self.obj.moves), False, (192, 192, 192)), (1.3 * 50, 9.5 * 50))
            else:
                self.sett.screen.blit(self.sett.ingame.render(str(self.obj.moves), False, (192, 192, 192)), (2 * 50, 9.5 * 50))
            if(self.obj.level < 10):
                self.sett.screen.blit(self.sett.ingame.render(str(self.obj.level), False, (192, 192, 192)), (23 * 50, 9.5 * 50))
            else:
                self.sett.screen.blit(self.sett.ingame.render(str(self.obj.level), False, (192, 192, 192)), (22.5 * 50, 9.5 * 50))
            for pos in self.obj.spike_pos:
                self.sett.screen.blit(self.sett.spike, ((pos[1] + self.obj.col_count) * 50, (pos[0] + self.obj.row_count) * 50))
            if(self.obj.popup):
                for pos in self.obj.holea_pos:
                    self.sett.screen.blit(self.sett.holeb, ((pos[1] + self.obj.col_count) * 50, (pos[0] + self.obj.row_count) * 50))
                for pos in self.obj.holeb_pos:
                    self.sett.screen.blit(self.sett.holea, ((pos[1] + self.obj.col_count) * 50, (pos[0] + self.obj.row_count) * 50))
            else:
                for pos in self.obj.holea_pos:
                    self.sett.screen.blit(self.sett.holea, ((pos[1] + self.obj.col_count) * 50, (pos[0] + self.obj.row_count) * 50))
                for pos in self.obj.holeb_pos:
                    self.sett.screen.blit(self.sett.holeb, ((pos[1] + self.obj.col_count) * 50, (pos[0] + self.obj.row_count) * 50))
            for pos in self.obj.key_pos:
                self.sett.screen.blit(self.sett.key, ((pos[1] + self.obj.col_count) * 50, (pos[0] + self.obj.row_count) * 50))
            for pos in self.obj.stone_pos:
                self.sett.screen.blit(self.sett.stone, ((pos[1] + self.obj.col_count) * 50, (pos[0] + self.obj.row_count) * 50))
            for pos in self.obj.wall_pos:
                self.sett.screen.blit(self.sett.wall, ((pos[1] + self.obj.col_count) * 50, (pos[0] + self.obj.row_count) * 50))
            for pos in self.obj.hwall_pos:
                self.sett.screen.blit(self.sett.hwall, ((pos[1] + self.obj.col_count) * 50, (pos[0] + self.obj.row_count) * 50))
            for pos in self.obj.goal_pos:
                self.sett.screen.blit(self.sett.goal, ((pos[1] + self.obj.col_count) * 50, (pos[0] + self.obj.row_count) * 50))
            for pos in self.obj.ske_pos:
                self.sett.screen.blit(self.sett.ske, ((pos[1] + self.obj.col_count) * 50, (pos[0] + self.obj.row_count) * 50))
            for pos in self.obj.ske_dead_pos:
                self.sett.screen.blit(self.sett.ske_dead, ((pos[1] + self.obj.col_count) * 50, (pos[0] + self.obj.row_count) * 50))
            for pos in self.obj.lock_pos:
                if(self.obj.unlock):
                    self.sett.screen.blit(self.sett.unlock, ((pos[1] + self.obj.col_count) * 50, (pos[0] + self.obj.row_count) * 50))
                else:
                    self.sett.screen.blit(self.sett.lock, ((pos[1] + self.obj.col_count) * 50, (pos[0] + self.obj.row_count) * 50))
            if(self.obj.walk):
                self.sett.screen.blit(pygame.transform.flip(self.sett.player_walk, self.obj.player_flip, 0), ((self.obj.player_walk_pos[1] + self.obj.col_count) * 50, (self.obj.player_walk_pos[0] + self.obj.row_count) * 50))        
            if(self.obj.player_kill_pos and not self.obj.walk):
                self.sett.screen.blit(pygame.transform.flip(self.sett.player_kill, self.obj.player_flip, 0), ((self.obj.player_kill_pos[1] + self.obj.col_count) * 50, (self.obj.player_kill_pos[0] + self.obj.row_count) * 50))        
            elif(self.obj.player_touch_pos and not self.obj.walk):
                self.sett.screen.blit(pygame.transform.flip(self.sett.player_touch, self.obj.player_flip, 0), ((self.obj.player_touch_pos[1] + self.obj.col_count) * 50, (self.obj.player_touch_pos[0] + self.obj.row_count) * 50))        
            elif(not self.obj.walk):
                self.sett.screen.blit(pygame.transform.flip(self.sett.player, self.obj.player_flip, 0), ((self.obj.player_pos[1] + self.obj.col_count) * 50, (self.obj.player_pos[0] + self.obj.row_count) * 50))        
            if(self.obj.hurt and not self.obj.walk):
                self.sett.screen.blit(pygame.transform.flip(self.sett.sfx_spike, self.obj.player_flip, 0), ((self.obj.player_pos[1] + self.obj.col_count) * 50, (self.obj.player_pos[0] + self.obj.row_count) * 50))        
        self._sprite();

    def move(self, dir):
        if self.obj.final:
            if(dir[1] != 0):
                if(self.obj.fchoose_2[self.obj.final_score]):
                    if((self.obj.final_choose + dir[1]) in range(1, 3)):
                        self.obj.player_pos = [self.obj.player_pos[0] + dir[1], self.obj.player_pos[1]]
                        self.obj.final_choose += dir[1]
        else:
            if(dir[0] == -1):
                self.obj.player_flip = True
            elif(dir[0] == 1):
                self.obj.player_flip = False
            next_move = [self.obj.player_pos[0] + dir[1], self.obj.player_pos[1] + dir[0]]
            if((self.obj.player_pos in self.obj.spike_pos) or ((self.obj.player_pos in self.obj.holea_pos) and (self.obj.popup == True)) or ((self.obj.player_pos in self.obj.holeb_pos) and (self.obj.popup == False))):
                stand_spike = True
            else:
                stand_spike = False
            if(next_move in (self.obj.wall_pos + self.obj.hwall_pos)):
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
            if(next_move in self.obj.ske_dead_pos):
                touch_ske_dead = True
            else:
                touch_ske_dead = False
            if(next_move in self.obj.key_pos):
                touch_key = True
            else:
                touch_key = False
            if((next_move in self.obj.lock_pos) and (self.obj.unlock == False)):
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
                    self.ske_dead_idx = 1
                    self.obj.ske_dead_pos.append(self.obj.ske_pos[ske_counts])
                    del self.obj.ske_pos[ske_counts]
                    self.sett.snd_kill.play()
            if(touch_goal):
                self.obj.player_pos = [self.obj.player_pos[0] + dir[1], self.obj.player_pos[1] + dir[0]]
                pygame.mixer.music.pause()
                if(self.obj.level != 8):
                    self.sett.snd_lvlup.play()
                    self.obj.levelup = True
                else:
                    self.sett.cutscenes = pygame.image.load(f'assets/cutscenes/cutscenes_0.png').convert_alpha()
                    self.sett.cutscenes = pygame.transform.scale(self.sett.cutscenes, (400, 400))
                    self.obj.final = True
                    self.obj.player_pos = [10, 6]
            elif(touch_stone):
                stone_count = -1
                for pos in self.obj.stone_pos:
                    stone_count += 1
                    if(next_move == pos):
                        next_stone = [pos[0] + dir[1], pos[1] + dir[0]]
                        if(next_stone not in (self.obj.wall_pos + self.obj.hwall_pos + self.obj.stone_pos + self.obj.ske_pos + self.obj.lock_pos + self.obj.goal_pos)):
                            self.next_stone_pos = stone_count
                            self.next_stone_loc = next_stone
                            self.check_stone = True
                        if(stand_spike):
                            self.act(0, dir)
                            self.obj.hurt = True
                            self.sfx_spike_idx = 1
                            self.snd_hurt = True
                        self.snd_touch = True
                        self.obj.player_touch_pos.append(self.obj.player_pos[0])
                        self.obj.player_touch_pos.append(self.obj.player_pos[1])
                        self.player_touch_idx = 1
                        self.act(2, dir)
            elif(touch_ske):
                ske_count = -1
                for pos in self.obj.ske_pos:
                    ske_count += 1
                    if(next_move == pos):
                        next_ske = [pos[0] + dir[1], pos[1] + dir[0]]
                        if(next_ske in self.obj.goal_pos):
                            self.obj.moves = 0
                            self.obj.secret = True
                            pygame.mixer.music.pause()
                            self.sett.snd_bad.play()
                        else:
                            if(next_ske not in (self.obj.wall_pos + self.obj.hwall_pos + self.obj.stone_pos + self.obj.ske_pos + self.obj.lock_pos)):
                                if((next_ske in  self.obj.spike_pos) or ((next_ske in self.obj.holea_pos) and (self.obj.popup == True)) or ((next_ske in self.obj.holeb_pos) and (self.obj.popup == False))):
                                    self.ske_dead_idx = 1
                                    self.obj.ske_dead_pos.append(next_ske)
                                    self.obj.player_touch_pos.append(self.obj.player_pos[0])
                                    self.obj.player_touch_pos.append(self.obj.player_pos[1])
                                    self.player_touch_idx = 1
                                    del self.obj.ske_pos[ske_count]
                                    self.sett.snd_kill.play()
                                else:
                                    self.obj.player_touch_pos.append(self.obj.player_pos[0])
                                    self.obj.player_touch_pos.append(self.obj.player_pos[1])
                                    self.player_touch_idx = 1
                                    self.next_ske_pos = ske_count
                                    self.next_ske_loc = next_ske
                                    self.check_ske = True
                                    self.snd_touch = True
                            else:
                                self.ske_dead_idx = 1
                                self.obj.ske_dead_pos.append(self.obj.ske_pos[ske_count])
                                self.obj.player_kill_pos.append(self.obj.player_pos[0])
                                self.obj.player_kill_pos.append(self.obj.player_pos[1])
                                self.player_kill_idx = 1
                                del self.obj.ske_pos[ske_count]
                                self.sett.snd_kill.play()
                            self.act(2, dir)
                        if(stand_spike):
                            self.obj.hurt = True
                            self.snd_hurt = True
                            self.sfx_spike_idx = 1
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
                            self.obj.unlock = True
                            self.obj.getkey = False
                            self.act(1, dir)
            elif(touch_spike):
                self.act(0, dir)
                self.act(1, dir)
                self.obj.hurt = True
                self.sfx_spike_idx = 1
                self.snd_hurt = True
            elif(not touch_wall and not touch_ske_dead):
                if(self.obj.level == 0):
                    if(self.obj.quit):
                        if(dir[0] != 0):
                            if(self.obj.choose + dir[0] in range(1, 3)):
                                self.obj.player_pos = [self.obj.player_pos[0], self.obj.player_pos[1] + dir[0]*5]
                                self.obj.choose += dir[0]
                    else:
                        if((self.obj.menu == 1) and (dir[1] != 0)):
                            if((self.obj.choose + dir[1]) in range(1, 7)):
                                self.obj.player_pos = next_move
                                self.obj.choose += dir[1]
                            elif((self.obj.choose + dir[1]) < 1):
                                self.obj.player_pos = [self.obj.player_pos[0] - dir[1]*5, self.obj.player_pos[1]]
                                self.obj.choose = 6
                            elif((self.obj.choose + dir[1]) > 6):
                                self.obj.player_pos = [self.obj.player_pos[0] - dir[1]*5, self.obj.player_pos[1]]
                                self.obj.choose = 1
                        elif(self.obj.menu == 2):
                            if(dir[0] != 0):
                                if(((self.obj.lvl_choose + dir[0]) in range(1, 5) and (self.obj.lvl_state == 1)) or ((self.obj.lvl_choose + dir[0]) in range(5, 9) and (self.obj.lvl_state == 2))):
                                    if(self.obj.level_list[self.obj.lvl_choose + dir[0] - 1]):
                                        self.obj.player_pos = [self.obj.player_pos[0], self.obj.player_pos[1] + dir[0]*4]
                                        self.obj.lvl_choose += dir[0]
                            else:
                                if((self.obj.lvl_choose + dir[1]*4) in range(1, 9)):
                                    if(self.obj.level_list[self.obj.lvl_choose + dir[1]*4 - 1]):
                                        self.obj.player_pos = [self.obj.player_pos[0] + dir[1]*4, self.obj.player_pos[1]]
                                        self.obj.lvl_choose += dir[1]*4
                                        self.obj.lvl_state += dir[1]
                else:
                    self.act(1, dir)
            
    def act(self, possive, dir):
        if(possive == 1):
            self.obj.player_walk_pos.append(self.obj.player_pos[0])
            self.obj.player_walk_pos.append(self.obj.player_pos[1])
            self.obj.player_walk_dir.append(dir[0])
            self.obj.player_walk_dir.append(dir[1])
            self.obj.player_pos = [self.obj.player_pos[0] + dir[1], self.obj.player_pos[1] + dir[0]]
            self.obj.moves -= 1
            self.obj.walk = True
            self.obj.popup = not self.obj.popup
            self.holea_popup = not self.holea_popup
            self.holeb_popup = not self.holeb_popup
            if(self.obj.moves <= 0):
                pygame.mixer.music.pause()
                self.sett.snd_bad.play()
        elif(possive == 2):
            self.obj.moves -= 1
            self.obj.popup = not self.obj.popup
            self.holea_popup = not self.holea_popup
            self.holeb_popup = not self.holeb_popup
            if(self.obj.moves <= 0):
                self.sett.snd_bad.play()
        else:
            self.obj.moves -=1
            if(self.obj.moves <= 0):
                self.sett.snd_bad.play()
        
    
    def run(self):
        while True:
            self.sett.timer.tick(self.sett.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if(self.obj.level == 0):
                        if event.key in self.sett.KEY_DIR:
                            self.move(self.sett.KEY_DIR[event.key])
                        if event.key == pygame.K_SPACE:
                            if(self.obj.menu == 1):
                                if(not self.obj.quit):
                                    if(self.obj.choose == 1):
                                        self.obj.level += 1
                                        with open('levels/lvl.txt', 'w') as f:
                                            f.write("1\n0\n0\n0\n0\n0\n0\n0")
                                        pygame.mixer.music.load('assets/soundtracks/ingame.mp3')
                                        pygame.mixer.music.play(loops = -1, fade_ms = 3000)
                                        self.obj.__init__()
                                    elif(self.obj.choose == 2):
                                        self.obj.menu = 2
                                        self.obj.player_pos = [4.5, 6.5]
                                    elif(self.obj.choose == 3):
                                        self.obj.menu = 3
                                    elif(self.obj.choose == 4):
                                        self.obj.menu = 4
                                        self.cre_run = 0
                                    elif(self.obj.choose == 5):
                                        self.obj.menu = 5
                                        pygame.mouse.set_pos(650, 350)
                                        self.event_player_rect.center = (650, 350)
                                        self.obj.event_time = pygame.time.get_ticks()
                                        pygame.mixer.music.load('assets/soundtracks/minigame.mp3')
                                        pygame.mixer.music.play(loops = -1, fade_ms = 3000)
                                    elif(self.obj.choose == 6):
                                        self.obj.choose = 1
                                        self.obj.player_pos = [7, 9]
                                        self.obj.quit = True
                                else:
                                    if(self.obj.choose == 1):
                                        self.obj.__init__()
                                    elif(self.obj.choose == 2):
                                        pygame.quit()
                            elif(self.obj.menu == 2):
                                if(self.obj.level_list[self.obj.lvl_choose-1]):
                                    self.obj.level = self.obj.lvl_choose
                                    pygame.mixer.music.load('assets/soundtracks/ingame.mp3')
                                    pygame.mixer.music.play(loops = -1, fade_ms = 3000)
                                    self.obj.__init__()
                            elif(self.obj.menu == 3):
                                self.obj.menu = 1
                                self.obj.choose = 1
                                self.obj.player_pos = [self.obj.player_pos[0] - 2, self.obj.player_pos[1]]
                            elif(self.obj.menu == 4):
                                self.obj.menu = 1
                                self.obj.choose = 1
                                self.obj.player_pos = [self.obj.player_pos[0] - 3, self.obj.player_pos[1]]
                                if(self.true_win):
                                    pygame.mixer.music.load('assets/soundtracks/menu.mp3')
                                    pygame.mixer.music.play(loops = -1, fade_ms = 3000)
                                    self.obj.true_win = False
                            elif(self.obj.menu == 5):
                                pygame.mixer.music.load('assets/soundtracks/menu.mp3')
                                pygame.mixer.music.play(loops = -1, fade_ms = 3000)
                                self.obj.__init__()
                        if event.key == pygame.K_ESCAPE:
                            if(self.obj.menu == 2):
                                self.obj.__init__()
                    else:
                        if((event.key in self.sett.KEY_DIR) and (not self.obj.hurt) and (not self.obj.walk) and (self.obj.player_pos != self.obj.player_kill_pos) and (self.obj.player_pos != self.obj.player_touch_pos)):
                            if(self.obj.moves > 0):
                                self.move(self.sett.KEY_DIR[event.key])
                        elif event.key == pygame.K_ESCAPE:
                            self.obj.level = 0
                            pygame.mixer.music.load('assets/soundtracks/menu.mp3')
                            pygame.mixer.music.play(loops = -1, fade_ms = 3000)
                            self.obj.__init__()
                        elif ((event.key == pygame.K_r) and (not self.obj.hurt) and (not self.obj.walk) and (self.obj.player_pos != self.obj.player_kill_pos) and (self.obj.player_pos != self.obj.player_touch_pos)):
                            self.ske_idle_idx = 1
                            pygame.mixer.stop()
                            if(self.obj.moves <= 0 or self.obj.levelup):
                                pygame.mixer.music.unpause()
                            self.obj.__init__()
                        elif event.key == pygame.K_l:
                            self.obj.moves += 10
                        elif event.key == pygame.K_e:
                            self.obj.moves = 1
                        elif event.key == pygame.K_z:
                            self.obj.level += 1
                            self.ske_idle_idx = 1
                            self.obj.__init__()
                        elif event.key == pygame.K_t:
                            self.obj.level = 10
                            self.ske_idle_idx = 1
                            self.obj.__init__()
                        elif((event.key == pygame.K_SPACE) and self.obj.levelup):
                            if(self.obj.level < 8):
                                if(self.obj.level_list[self.obj.level] == 0):
                                    with open('levels/lvl.txt', 'w') as f:
                                        self.obj.level_list[self.obj.level] = 1
                                        for lvl in self.obj.level_list:
                                            f.write(str(lvl) + "\n")
                                pygame.mixer.stop()
                                pygame.mixer.music.unpause()                               
                            else:
                                self.cre_run = 0
                                if(self.obj.final_score != 19):                                
                                    pygame.mixer.stop()
                                    pygame.mixer.music.load('assets/soundtracks/menu.mp3')
                                    pygame.mixer.music.play(loops = -1, fade_ms = 3000)
                                    if(self.obj.final_score != 13):
                                        with open('levels/lvl.txt', 'w') as f:
                                            f.write("1\n0\n0\n0\n0\n0\n0\n0")
                                else:
                                    self.true_win = True
                            self.obj.level += 1
                            self.ske_idle_idx = 1
                            self.obj.__init__()
                            if(self.obj.level == 0):
                                self.obj.menu = 4
                                self.obj.player_pos = [self.obj.player_pos[0] + 3, self.obj.player_pos[1]]
                        elif((event.key == pygame.K_SPACE) and self.obj.final):
                            if(self.obj.final_score in self.obj.ending):
                                self.obj.levelup = True
                                pygame.mixer.stop()
                                if(self.obj.final_score == 8):
                                    pygame.mixer.music.load('assets/soundtracks/dead_end.mp3')
                                    pygame.mixer.music.play(loops = -1, fade_ms = 3000)
                                elif(self.obj.final_score == 9):
                                    pygame.mixer.music.pause()
                                    self.sett.snd_nut.play()
                                elif(self.obj.final_score == 13):
                                    pygame.mixer.music.load('assets/soundtracks/good_end.mp3')
                                    pygame.mixer.music.play(loops = -1, fade_ms = 3000)
                                elif(self.obj.final_score == 19):
                                    pygame.mixer.music.load('assets/soundtracks/true_end.mp3')
                                    pygame.mixer.music.play(loops = -1, fade_ms = 3000)
                            else:
                                self.obj.change = True
                                if(self.obj.final_choose == 1):
                                    self.obj.final_score += self.obj.fchoose_1[self.obj.final_score]
                                elif(self.obj.final_choose == 2):
                                    self.obj.final_score += self.obj.fchoose_2[self.obj.final_score]
                                    self.obj.final_choose = 1
                                    self.obj.player_pos = [self.obj.player_pos[0] - 1, self.obj.player_pos[1]]
                                if(self.obj.final_score == 18):
                                    self.sett.snd_demon.play()
                                elif(self.obj.final_score == 19 or self.obj.final_score == 9):
                                    self.sett.snd_gun.play()
            if(self.obj.level == 0):
                self._draw_main_menu()
            else:
                self._draw_board()
            pygame.display.update()


myLevel = Board()
myLevel.run()

