from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QRadioButton, QLabel, QGroupBox, QButtonGroup, QMessageBox)

import random

class Question():
    def __init__(self, text, right_answer, wrong1, wrong2, wrong3):
        self.text = text
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions = [
    Question('?', '?', '?', '?', '?'),
    Question('Снег?', 'да', 'нет', 'наверное', 'незн'),
    Question('Дождь?', 'нет', 'да', 'наверное', 'незн'),
    Question('Cолнце?', 'да', 'незн', 'нет', 'наверное'),
    Question('Ночь?', 'нет', 'да', 'наверное ', 'незн'),
    Question('День?', 'да', 'нет', 'наверное', 'незн'),
    Question('Тепло?', 'нет', 'нет', 'незн', 'наверное'),
    Question('Холодно?', 'да', 'нет', 'незн', 'наверное'),
    Question('Да?', 'да', 'нет', 'наверное ', 'незн'),
    Question('Нет?', 'нет', 'да', 'наверное', 'незн'),
]




def ask(q: Question):
    question_text.setText(q.text)
    random.shuffle(buttons)
    buttons[0].setText(q.right_answer)
    buttons[1].setText(q.wrong1)
    buttons[2].setText(q.wrong2)
    buttons[3].setText(q.wrong3) 


def show_answers():
    if button_group.checkedButton() == None:
        return
    btn.setText('след. вопрос')
    for rbtn in buttons:
        if rbtn.isChecked():
            if rbtn.text() == buttons[0].text():
                rbtn.setStyleSheet('color: green;')
                main_win.score += 1
            else:
                rbtn.setStyleSheet('color: red;')
                buttons[0].setStyleSheet('color: green;')
            break
    

def show_question():
    btn.setText('да')
    button_group.setExclusive(False)
    for rbtn in buttons:
        rbtn.setStyleSheet('')
        rbtn.setChecked(False)
    button_group.setExclusive(True)
    next_question()

def next_question():
    if main_win.q_index >= len(questions):
        main_win.q_index = 0
        random.shuffle(questions)
        show_score()
        main_win.score = 0
    q = questions[main_win.q_index]
    main_win.q_index += 1
    ask(q)



def start_test():
    if btn.text() == 'да':
        show_answers()
    else:
        show_question()


def show_score():
    percent = main_win.score / main_win.total * 100 
    percent = round(percent, 1)
    text = 'Уважаемый пользователь!\n'
    text += f'Вы правильно ответили на {main_win.score} из {main_win.total} вопросов\n'
    text += f'Процент правильных ответов: {percent}%.\n'
    text += 'Тест начнется заново!'

    msg = QMessageBox()
    msg.setWindowTitle('Результат тестирования')
    msg.setText(text)
    msg.exec()



app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('MemoCard')
main_win.resize(640, 360)
main_win.q_index = 0
main_win.total = len(questions)
main_win.score = 0


question_text = QLabel('Какой национальности не существует?')
grp_box = QGroupBox('Варианты ответов')
button_group = QButtonGroup()
radio1 = QRadioButton('Энцы')
radio2 = QRadioButton('Cмурфы')
radio3 = QRadioButton('Чулымцы')
radio4 = QRadioButton('Алеуты')
btn = QPushButton('да')
result_text = QLabel('Ваш результат: 5 из 5')

button_group.addButton(radio1)
button_group.addButton(radio2)
button_group.addButton(radio3)
button_group.addButton(radio4)



main_layout = QVBoxLayout()
main_h1 = QHBoxLayout()
main_h2 = QHBoxLayout()
main_h3 = QHBoxLayout()
grp_main_layout = QHBoxLayout()
grp_v1 = QVBoxLayout()
grp_v2 = QVBoxLayout()



grp_v1.addWidget(radio1)
grp_v1.addWidget(radio2)
grp_v2.addWidget(radio3)
grp_v2.addWidget(radio4)
grp_main_layout.addLayout(grp_v1)
grp_main_layout.addLayout(grp_v2)
grp_box.setLayout(grp_main_layout)

main_h1.addWidget(question_text, alignment=Qt.AlignCenter)
main_h2.addWidget(grp_box)
main_h3.addStretch(1)
main_h3.addWidget(btn, stretch=2)
main_h3.addStretch(1)
main_layout.addLayout(main_h1)
main_layout.addLayout(main_h2)
main_layout.addLayout(main_h3)
main_win.setLayout(main_layout)

btn.clicked.connect(start_test)

buttons = [radio1, radio2, radio3, radio4]
random.shuffle(questions)
ask(questions[main_win.q_index])
main_win.q_index += 1


main_win.show()
app.exec()