from __future__ import print_function
import sys

# These methods should be added to your QT classes or called from QT classes to change the default behavior/look/feel
try:
    from PySide.QtCore import *
    from PySide.QtGui import *
except ImportError:
    from PyQt.QtCore import *
    from PyQt.QtGui import *


ANIM_SPEED = 500
ANIM_EASING = QEasingCurve.InQuad


class UiEnhancements(QObject):
    def ui_fade(self, normal=True, closing=False):
        if self.isHidden():
            self.ui_fade_in(normal)
        else:
            self.ui_fade_out(closing)

    def ui_fade_in(self, normal):
        self.setWindowOpacity(0.0)
        self.show()
        if normal:
            self.showNormal()
        else:
            self.show()
        self.anim = QPropertyAnimation(self, "windowOpacity")
        self.anim.setDuration(ANIM_SPEED)
        self.anim.setStartValue(0.0)
        self.anim.setEndValue(1.0)
        self.anim.setEasingCurve(ANIM_EASING)
        self.anim.start()

    def ui_fade_out_complete(self):
        if self.closing:
            sys.exit(1)
        else:
            self.hide()

    def ui_fade_out(self, closing):
        self.anim = QPropertyAnimation(self, "windowOpacity")
        self.anim.setDuration(ANIM_SPEED)
        self.anim.setStartValue(1.0)
        self.anim.setEndValue(0.0)
        self.anim.setEasingCurve(ANIM_EASING)
        self.closing = closing
        self.anim.finished.connect(self.ui_fade_out_complete)
        self.anim.start()

    def ui_frameless(self, stay_on_top=False):
        self.setMask(self.geometry())
        self.setWindowFlags(Qt.X11BypassWindowManagerHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        if stay_on_top:
            self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def ui_transparent(self, color='rgba( 255, 255, 255, 70% );'):
        self.setStyleSheet("background-color: %s;" % color)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def handle_click_move(self):
        pass
