from PyFlow.UI.Canvas.UINodeBase import UINodeBase
from Qt import QtGui
from Qt.QtWidgets import QLabel


class UIStreamPreviewNode(UINodeBase):
    def __init__(self, raw_node):
        super(UIStreamPreviewNode, self).__init__(raw_node)
        self.resizable = True
        self.Imagelabel = QLabel("test3")
        self.pixmap = QtGui.QPixmap(None)
        self.addWidget(self.Imagelabel)
        self.updateSize()

    def paint(self, painter, option, widget):
        self.updateSize()
        super(UIStreamPreviewNode, self).paint(painter, option, widget)

    def updateSize(self):
        self.pixmap = QtGui.QPixmap(self._rawNode.label.getData())
        scaledPixmap = self.pixmap.scaledToWidth(self.customLayout.geometry().width())
        self.Imagelabel.setPixmap(scaledPixmap)
