import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os


class tooldemo(QMainWindow):
    def __init__(self, parent=None):
        super(tooldemo, self).__init__(parent)
        tb = self.addToolBar("File")

        new = QAction(QIcon("add-folder.png"), "membuat file baru", self)
        tb.addAction(new)

        open = QAction(QIcon("open-folder.png"), "open", self)
        tb.addAction(open)

        save = QAction(QIcon("save-folder.png"), "save", self)
        tb.addAction(save)

        tb.actionTriggered[QAction].connect(self.toolbtnpressed)

        tb2 = self.addToolBar("Edit")
        new2 = QAction(QIcon("new-folder.png"), "new", self)
        tb2.addAction(new2)

        self.setWindowTitle("toolbar demo")

    def toolbtnpressed(self, a):
        print("pressed tool button is", a.text())


def main():
    app = QApplication(sys.argv)
    ex = tooldemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
