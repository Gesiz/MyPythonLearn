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
    window.blit(bg, (10, 20))
    pygame.display.update()
    while True:
        # 减少CPU的使用
        time.sleep(0.05)  # 让程序进入休眠 单位 秒
        pass


main()
