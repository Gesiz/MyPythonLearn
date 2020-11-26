import pygame

window_width = 512
window_height = 768

def init():
    # 绘制 windows 窗口 宽和高应该和背景图片的大小保持一致
    window = pygame.display.set_mode((window_width, window_height))
    # 加载图片文件 返回图片对象
    bg = pygame.image.load("res/img_bg_level_1.jpg")
    # 贴图 指定坐标将图片指定位置
    window.blit(bg, (0, 0))
    # 贴图 自己的飞机
    hero_img = pygame.image.load('res/hero2.png')




if __name__ == "__main__":
    pygame.init()
    init()