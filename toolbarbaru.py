import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os


class tooldemo(QMainWindow):
    def __init__(self, parent=None):
        super(tooldemo, self).__init__(parent)
        tb = self.addToolBar("File")

        new = QAction(QIcon(os.path.dirname(__file__),
                      "add-folder.png"), "membuat file baru", self)
        tb.addAction(new)

        open = QAction(QIcon(os.path.join(os.path.dirname(
            __file__), "open-folder.png")), "open", self)
        tb.addAction(open)

        save = QAction(QIcon(os.path.join(os.path.dirname(
            __file__), "save-folder.png")), "save", self)
        tb.addAction(save)

        tb.actionTriggered[QAction].connect(self.toolbtnpressed)

        tb2 = self.addToolBar("Edit")
        new2 = QAction(QIcon(os.path.join(os.path.dirname(
            __file__), "new-folder.png")), "new", self)
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
