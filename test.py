# -*- coding: gbk -*-

import sys
from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup, QPauseAnimation, QPoint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class PauseAnimationExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("暂停动画示例")
        self.setGeometry(100, 100, 400, 200)

        # 创建按钮
        self.button = QPushButton("点击我", self)
        self.button.setGeometry(50, 50, 100, 50)

        # 创建第一个动画（平移按钮）
        self.move_animation = QPropertyAnimation(self.button, b"pos")
        self.move_animation.setStartValue(QPoint(50, 50))
        self.move_animation.setEndValue(QPoint(250, 50))
        self.move_animation.setDuration(1000)

        # 创建暂停动画（暂停 500 毫秒）
        self.pause_animation = QPauseAnimation(5000)  # 暂停 500 毫秒

        # 创建第二个动画（改变按钮大小）
        self.size_animation = QPropertyAnimation(self.button, b"size")
        self.size_animation.setStartValue(self.button.size())
        self.size_animation.setEndValue(self.button.size() * 2)
        self.size_animation.setDuration(1000)

        # 创建动画组，并将动画和暂停动画添加到组中
        self.animation_group = QSequentialAnimationGroup(self)
        self.animation_group.addAnimation(self.move_animation)  # 第一个动画
        self.animation_group.addAnimation(self.pause_animation)  # 暂停动画
        self.animation_group.addAnimation(self.size_animation)  # 第二个动画

        # 设置按钮点击事件，点击后启动动画
        self.button.clicked.connect(self.start_animation)

    def start_animation(self):
        self.animation_group.start()  # 启动动画组

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PauseAnimationExample()
    window.show()
    sys.exit(app.exec_())

