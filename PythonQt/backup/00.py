# def __init__(self, widget_main):
#     pg.setConfigOptions(antialias=True, background='w', foreground='k')  # pg全局变量设置函数，antialias=True开启曲线抗锯齿
#     # pg.setConfigOption('foreground', 'k')
#     win = pg.GraphicsLayoutWidget()  # 创建pg layout，可实现数据界面布局自动管理
#
#     # pg绘图窗口可以作为一个widget添加到GUI中的graph_layout，当然也可以添加到Qt其他所有的容器中
#     widget_main.verticalLayout.addWidget(win)
#
#     p1 = win.addPlot()  # 添加第一个绘图窗口 title="sin 函数"
#
#     # p1.setLabel('left', color='#000000')  # y轴设置函数
#     p1.showGrid(x=True, y=True)  # 栅格设置函数
#     p1.setLogMode(x=False, y=False)  # False代表线性坐标轴，True代表对数坐标轴
#     # p1.setLabel('bottom', text='time', units='s')  # x轴设置函数
#     t = np.linspace(0, 20, 200)
#     y_sin = np.sin(t)
#     p1.plot(t, y_sin, pen='g', name='sin(x)', clear=True)