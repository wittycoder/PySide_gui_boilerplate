from __future__ import print_function
import sys

try:
    from PySide.QtCore import *
    from PySide.QtGui import *
except ImportError:
    from PyQt.QtCore import *
    from PyQt.QtGui import *

from mainWindow_ui import Ui_Main
from uiEnhancements import *


class MainDialog(QWidget, Ui_Main, UiEnhancements):
    def __init__(self):
        super(MainDialog, self).__init__()
        self.setupUi(self)

        # Demo - connect up the UI elements to Class methods
        self.inputEdit.textChanged.connect(self.inputChanged)

        # Optional UI look/feel enhancements...
        self.ui_frameless()
        #ui_transparent(self)

        #self.show()  # Either show
        self.ui_fade()  # or fade in

    def accept(self):  # Handle OK from main dialog
        print('Accepted dialog')
        self.ui_fade(closing=True)

    def reject(self):  # Handle Cancel on teh dialog
        print('Rejected dialog')

    def inputChanged(self):
        self.inputLabel.setText(self.inputEdit.text())


def main():
    app = QApplication(sys.argv)
    gui = MainDialog()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
