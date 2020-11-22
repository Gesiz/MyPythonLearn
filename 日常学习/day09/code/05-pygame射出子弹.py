import pygame
import time
from pygame import locals

pygame.init()

window_width = 512
window_height = 768
# 定义子弹的列表
buller_list = []


def display(window):
    # 子弹的贴图
    print(len(buller_list))
    for bullet in buller_list:
        window.blit(bullet[0], (bullet[1], bullet[2]))
        bullet[2] -= 5
        if bullet[2] <= 0:
            buller_list.pop(0)


def main():
    # 绘制 windows 窗口 宽和高应该和背景图片的大小保持一致
    window = pygame.display.set_mode((window_width, window_height))
    # 加载图片文件 返回图片对象
    bg = pygame.image.load("res/img_bg_level_1.jpg")
    # 贴图 指定坐标将图片指定位置
    window.blit(bg, (0, 0))
    # 贴图 自己的飞机
    hero_img = pygame.image.load('res/hero2.png')

    h_x = window_width / 2 - 60
    h_y = 600

    # 加载子弹的图片

    # bullet_img = pygame.image.load('res/bullet_9.png')
    #
    # b_x = h_x + 120 / 2 - 20 / 2
    #
    # b_y = h_y - 31

    while True:
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                print("陈旭推出")
                pygame.quit()
                exit()

            # elif event.type == locals.KEYDOWN:
            #     if event.key == locals.K_LEFT:
            #         h_x -= 5
            #         if h_x < 0:
            #             h_x = 0
            #         print("left")
            #     elif event.key == locals.K_RIGHT:
            #         h_x += 5
            #         if h_x > window_width:
            #             h_x = window_width - 120
            #         print("right")
            #     elif event.key == locals.K_SPACE:
            #         print("space")
        # 获取键盘的长按时间 返回的是元组

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[locals.K_LEFT]:
            h_x -= 5
            if h_x < 0:
                h_x = 0
            print('left')
        if pressed_keys[locals.K_RIGHT]:
            h_x += 5
            if h_x > window_width:
                h_x = window_width - 120
            print('right')
        if pressed_keys[locals.K_UP]:
            h_y -= 5
            print('up')
        if pressed_keys[locals.K_DOWN]:
            h_y += 5
            print('down')

        if pressed_keys[locals.K_SPACE]:  # 按键发射子弹
            bullet_img = pygame.image.load('res/bullet_9.png')

            b_x = h_x + 120 / 2 - 20 / 2
            b_y = h_y - 31
            buller_list.append([bullet_img, b_x, b_y])
            display(window)
            print('space')
        # 贴图 指定坐标将图片指定位置
        window.blit(bg, (0, 0))
        # 贴图 自己的飞机
        window.blit(hero_img, (h_x, h_y))

        # # 贴子弹
        # window.blit(bullet_img, (b_x, b_y))
        display(window)
        pygame.display.update()

        # 减少CPU的使用
        time.sleep(0.05)  # 让程序进入休眠 单位 秒

        # b_y -= 5


main()
enumerate