class WidgetGraph:

    def __init__(self, widget_main):
        self.figure = Figure(dpi=100)
        # self.figure = plt.gcf()
        img = plt.imread("src.png")  # 读取图片
        print(img.shape)  # 高宽 像素值 opencv显示
        # plt.grid(True)  # 生成网格
        self.dynamic_canvas = FigureCanvas(self.figure)

        widget_main.verticalLayout.addWidget(NavigationToolbar(self.dynamic_canvas, widget_main))  # 添加
        widget_main.verticalLayout.addWidget(self.dynamic_canvas)

        self.dynamic_canvas.mpl_connect("button_release_event", self._on_left_click)  # 连接信号
        self.dynamic_canvas.mpl_connect('scroll_event', self._on_wheel)

        self._dynamic_ax = self.dynamic_canvas.figure.subplots()

        self._dynamic_ax.imshow(img, extent=[0, img.shape[1], 0, img.shape[0]])  # 设置图片大小

        # t = np.linspace(0, 100, 100)
        self.x = np.linspace(0, img.shape[1], 10)
        self.y = np.linspace(0, img.shape[0], 10)

        # Set up a Line2D.
        # self._line, = self._dynamic_ax.plot(t, np.sin(t + time.time()))
        self._line, = self._dynamic_ax.plot(self.x, self.y)
        self._timer = self.dynamic_canvas.new_timer(50)
        self._timer.add_callback(self._update_canvas)
        self._timer.start()

    def _update_canvas(self):
        # t = np.linspace(0, 100, 100)
        # Shift the sinusoid as a function of time.
        self._line.set_data(self.x, self.y)
        self._line.figure.canvas.draw()

    def _on_left_click(self, event):
        print(event)
        pass

    def _on_wheel(self, event):
        print(event)
        pass

    # def _on_pick(self, event):
    #     print(event)