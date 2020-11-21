import pygame
import time

pygame.init()

window_width = 512
window_height = 768


def main():
    # 绘制 windows 窗口 宽和高应该和背景图片的大小保持一致
    window = pygame.display.set_mode((window_width, window_height))
    # 加载图片文件 返回图片对象
    bg = pygame.image.load("res/img_bg_level_1.jpg")
    # 贴图 指定坐标将图片指定位置
    bg = window.blit(bg, (0, 0))
    # 贴图 自己的飞机
    hero_img = pygame.image.load('res/hero2.png')

    h_x = window_width / 2 - 60
    h_y = 600
    window.blit(hero_img, (h_x, h_y))

    pygame.display.update()
    while True:
        # 减少CPU的使用
        time.sleep(1)  # 让程序进入休眠 单位 秒
        pass


main()

# from pygame import  locals
#
# for event in pygame.event.get():
#     # 1 鼠标点击的窗口的事件
