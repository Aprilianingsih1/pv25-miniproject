import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class menudemo(QMainWindow):
    def __init__(self, parent=None):
        super(menudemo, self).__init__(parent)

        bar = self.menuBar()

        file = bar.addMenu("File")

        new = file.addMenu("New")
        new_page = new.addMenu("Page")
        new_page_portrait = new_page.addAction("Portrait")
        new_page_portrait.setShortcut("Ctrl+Shift+N")
        new_page.addAction("Landscape")
        new.addAction("Sheet")

        save = file.addAction("Save")
        save.setShortcut("Ctrl+S")

        edit = file.addMenu("Edit")
        edit.addAction("copy")

        paste = edit.addMenu("Paste")
        paste.addAction("by reference")

        paste_value = QAction("by value", self)
        paste_value.triggered.connect(self.file_edit_paste_value_triggered)
        paste.addAction(paste_value)

        # quit = QAction("QQ", self)
        # file.addAction(quit)

        help = bar.addMenu("Help")
        help.addAction("?")
        help2 = help.addMenu("??")
        help2.addAction("???")
        help2.addAction("????")

        setting = bar.addMenu("Settings")
        setting2 = setting.addMenu("Themes")
        setting2.addAction("Color")
        setting2.addAction("Font")
        setting3 = setting.addMenu("Opening File")
        setting3.addAction("Open in a new tab")
        setting3.addAction("Open in a new windows")

        quit = bar.addMenu("Quit")

        file.triggered[QAction].connect(self.processtrigger)
        help.triggered[QAction].connect(self.processtrigger)
        setting.triggered[QAction].connect(self.processtrigger)
        quit.triggered[QAction].connect(self.showdialog())

        self.setWindowTitle("menu demo")

    def processtrigger(self, q):
        print(q.text() + " is triggered")

    def file_edit_paste_value_triggered(self):
        print("edit paste value triggered")

    def showdialog(self):
        d = QDialog()
        b1 = QPushButton("ok", d)
        b1.move(70, 50)
        d.setWindowTitle("Anda yakin ?")
        d.setWindowModality(Qt.ApplicationModal)
        d.exec_()


def main():
    app = QApplication(sys.argv)
    ex = menudemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
