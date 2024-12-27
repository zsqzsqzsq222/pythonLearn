# -*- coding: gbk -*-

import sys
from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup, QPauseAnimation, QPoint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class PauseAnimationExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("��ͣ����ʾ��")
        self.setGeometry(100, 100, 400, 200)

        # ������ť
        self.button = QPushButton("�����", self)
        self.button.setGeometry(50, 50, 100, 50)

        # ������һ��������ƽ�ư�ť��
        self.move_animation = QPropertyAnimation(self.button, b"pos")
        self.move_animation.setStartValue(QPoint(50, 50))
        self.move_animation.setEndValue(QPoint(250, 50))
        self.move_animation.setDuration(1000)

        # ������ͣ��������ͣ 500 ���룩
        self.pause_animation = QPauseAnimation(5000)  # ��ͣ 500 ����

        # �����ڶ����������ı䰴ť��С��
        self.size_animation = QPropertyAnimation(self.button, b"size")
        self.size_animation.setStartValue(self.button.size())
        self.size_animation.setEndValue(self.button.size() * 2)
        self.size_animation.setDuration(1000)

        # ���������飬������������ͣ������ӵ�����
        self.animation_group = QSequentialAnimationGroup(self)
        self.animation_group.addAnimation(self.move_animation)  # ��һ������
        self.animation_group.addAnimation(self.pause_animation)  # ��ͣ����
        self.animation_group.addAnimation(self.size_animation)  # �ڶ�������

        # ���ð�ť����¼����������������
        self.button.clicked.connect(self.start_animation)

    def start_animation(self):
        self.animation_group.start()  # ����������

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PauseAnimationExample()
    window.show()
    sys.exit(app.exec_())

