import numpy as np
from matplotlib import use
use('AGG')
from matplotlib.transforms import Bbox
from matplotlib.path import Path
from matplotlib.patches import Rectangle
from matplotlib.pylab import *
from PySide import QtCore,QtGui

rect = Rectangle((-1, -1), 2, 2, facecolor="#aaaaaa")
gca().add_patch(rect)
bbox = Bbox.from_bounds(-1, -1, 2, 2)

for i in range(12):
    vertices = (np.random.random((4, 2)) - 0.5) * 6.0
    vertices = np.ma.masked_array(vertices, [[False, False], [True, True], [False, False], [False, False]])
    path = Path(vertices)
    if path.intersects_bbox(bbox):
        color = 'r'
    else:
        color = 'b'
    plot(vertices[:,0], vertices[:,1], color=color)

app = QtGui.QApplication(sys.argv)
gcf().canvas.draw()

stringBuffer = gcf().canvas.buffer_rgba(0,0)
l, b, w, h = gcf().bbox.bounds

qImage = QtGui.QImage(stringBuffer,
                      w,
                      h,
                      QtGui.QImage.Format_ARGB32)

scene = QtGui.QGraphicsScene()
view = QtGui.QGraphicsView(scene)
pixmap = QtGui.QPixmap.fromImage(qImage)
pixmapItem = QtGui.QGraphicsPixmapItem(pixmap)
scene.addItem(pixmapItem)
view.show()

app.exec_()