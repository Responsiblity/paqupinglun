import pygame
import random
import string

# 初始化 Pygame 库
pygame.init()

# 设置屏幕尺寸和帧率
screen_width, screen_height = 800, 600
frame_rate = 60

# 创建屏幕对象
screen = pygame.display.set_mode((screen_width, screen_height))

# 定义颜色
black = (0, 0, 0)

# 获取可用字体列表
font_list = pygame.font.get_fonts()
font_name = random.choice(font_list)

# 创建字体对象和文本列表
font_size = 20
font = pygame.font.SysFont(font_name, font_size)
texts = [font.render(random.choice(string.ascii_letters + string.digits), True, (0, 255, 0)) for _ in range(screen_height // font_size)]

# 定义代码列数、速度和密度
num_columns = len(texts)
speed = 5
density = 5

# 启动主循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # 填充背景
    screen.fill(black)

    # 更新每一列的文本位置
    for i in range(num_columns):
        y = i * font_size
        x = random.randint(-screen_width, 0) - density * font_size
        for j in range(density):
            index = random.randint(0, len(texts) - 1)
            text = texts[index]
            screen.blit(text, (x + j * font_size, y))
            x += font_size

    # 移动每一列的文本位置
    for i in range(num_columns):
        for j in range(density):
            index = random.randint(0, len(texts) - 1)
            text = texts[index]
            x, y = text.get_rect().move(j * font_size, i * font_size).topleft
            text_rect = pygame.Rect(x + speed, y, font_size, font_size)
            screen.blit(text, text_rect)

    # 更新屏幕显示
    pygame.display.flip()

    # 控制帧率
    pygame.time.Clock().tick(frame_rate)