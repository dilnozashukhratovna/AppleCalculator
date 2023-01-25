from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont, QIcon
import sys
import os
os.system("cls")

# WINDOW
app = QApplication(sys.argv)
window = QWidget()
window.setStyleSheet("""
    width: 300px;
    background-color: #000;
""")
# window.setGeometry(650,130, 435, 750)
window.setFixedSize(430, 750)
window.move(650, 130)
window.setWindowTitle("Calculator")

# SET BUTTONS
# FIRST LINE
# AC
button_ac = QPushButton("AC", window)
button_ac.setGeometry(20, 200, 90, 90)
button_ac.setStyleSheet("""
    background-color: #aaa;
    color: black;
    border-radius: 45px;
    font-family: fantacy;
    font-size: 30px
""")

# +/-
button_just = QPushButton("+/-", window)
button_just.setGeometry(120, 200, 90, 90)
button_just.setStyleSheet("""
    background-color: #aaa;
    color: black;
    border-radius: 45px;
    font-family: fantacy;
    font-size: 30px
""")

# %
button_percent = QPushButton("%", window)
button_percent.setGeometry(220, 200, 90, 90)
button_percent.setStyleSheet("""
    background-color: #aaa;
    color: black;
    border-radius: 45px;
    font-family: fantacy;
    font-size: 30px
""")

# divide
button_divide = QPushButton("÷", window)
button_divide.setGeometry(320, 200, 90, 90)
button_divide.setStyleSheet("""
    background-color: #FF9500;
    color: white;
    border-radius: 45px;
    font-family: fantacy;
    font-size: 30px
""")


# SECOND LINE
# seven 
button_seven = QPushButton("7", window)
button_seven.setGeometry(20, 305, 90, 90)
button_seven.setStyleSheet("""
    background-color: #3e403e;
    color: white;
    border-radius: 45px;
    font-family: fantacy;
    font-size: 40px
""")
# eight
button_eight = QPushButton("8", window)
button_eight.setGeometry(120, 305, 90, 90)
button_eight.setStyleSheet("""
    background-color: #3e403e;
    color: white;
    border-radius: 45px;
    font-family: fantacy;
    font-size: 40px
""")
# nine
button_nine = QPushButton("9", window)
button_nine.setGeometry(220, 305, 90, 90)
button_nine.setStyleSheet("""
    background-color: #3e403e;
    color: white;
    border-radius: 45px;
    font-family: fantacy;
    font-size: 40px
""")

# multiply
button_multiply = QPushButton("x", window)
button_multiply.setGeometry(320, 305, 90, 90)
button_multiply.setStyleSheet("""
    background-color: #FF9500;
    color: white;
    border-radius: 45px;
    font-family: fantacy;
    font-size: 30px
""")


# THIRD LINE
# four
button_four = QPushButton("4", window)
button_four.setGeometry(20, 410, 90, 90)
button_four.setStyleSheet("""
    background-color: #3e403e;
    color: white;
    border-radius: 45px;
    font-family: fantacy;
    font-size: 40px
""")

# five
button_five = QPushButton("5", window)
button_five.setGeometry(120, 410, 90, 90)
button_five.setStyleSheet("""
    background-color: #3e403e;
    color: white;
    border-radius: 45px;
    font-family: fantacy;
    font-size: 40px
""")

# six
button_six = QPushButton("6", window)
button_six.setGeometry(220, 410, 90, 90)
button_six.setStyleSheet("""
    background-color: #3e403e;
    color: white;
    border-radius: 45px;
    font-family: fantacy;
    font-size: 40px
""")

# minus
button_minus = QPushButton("-", window)
button_minus.setGeometry(320, 410, 90, 90)
button_minus.setStyleSheet("""
    background-color: #FF9500;
    color: white;
    border-radius: 45px;
    font-family: fantacy;
    font-size: 30px
""")


# FOURTH LINE
# one
button_one = QPushButton("1", window)
button_one.setGeometry(20, 515, 90, 90)
button_one.setStyleSheet("""
    background-color: #3e403e;
    color: white;
    border-radius: 45px;
    font-family: fantacy;
    font-size: 40px
""")

# two
button_two = QPushButton("2", window)
button_two.setGeometry(120, 515, 90, 90)
button_two.setStyleSheet("""
    background-color: #3e403e;
    color: white;
    border-radius: 45px;
    font-family: fantacy;
    font-size: 40px
""")

# three
button_three = QPushButton("3", window)
button_three.setGeometry(220, 515, 90, 90)
button_three.setStyleSheet("""
    background-color: #3e403e;
    color: white;
    border-radius: 45px;
    font-family: fantacy;
    font-size: 40px
""")

# plus
button_plus = QPushButton("+", window)
button_plus.setGeometry(320, 515, 90, 90)
button_plus.setStyleSheet("""
    background-color: #FF9500;
    color: white;
    border-radius: 45px;
    font-family: fantacy;
    font-size: 30px
""")


# FIFTH LINE
# zero
button_zero = QPushButton("0", window)
button_zero.setGeometry(20, 620, 190, 90)
button_zero.setStyleSheet("""
    background-color: #3e403e;
    color: white;
    border-radius: 45px;
    font-family: fantacy;
    font-size: 40px
""")

# comma
button_comma = QPushButton(",", window)
button_comma.setGeometry(220, 620, 90, 90)
button_comma.setStyleSheet("""
    background-color: #3e403e;
    color: white;
    border-radius: 45px;
    font-family: fantacy;
    font-size: 40px
""")

# equal
button_equal = QPushButton("=", window)
button_equal.setGeometry(320, 620, 90, 90)
button_equal.setStyleSheet("""
    background-color: #FF9500;
    color: white;
    border-radius: 45px;
    font-family: fantacy;
    font-size: 30px
""")

# MAIN
main = QLabel("0", window)
to_count = main.text()
to_count = ''
main.setGeometry(43, 90, 430, 90)
main.setStyleSheet("""
    color: white;
    font-family: Calibri;
    font-size: 100px
""")



# FUNCTIONS
# one
def one():
    global to_count
    to_count+='1'
    main.setText(to_count)
    
button_one.clicked.connect(one)
# two
def two():
    global to_count
    to_count+='2'
    main.setText(to_count)
button_two.clicked.connect(two)
# three
def three():
    global to_count
    to_count+='3'
    main.setText(to_count)
button_three.clicked.connect(three)
# four
def four():
    global to_count
    to_count+='4'
    main.setText(to_count)
button_four.clicked.connect(four)
# five
def five():
    global to_count
    to_count+='5'
    main.setText(to_count)
button_five.clicked.connect(five)
# six
def six():
    global to_count
    to_count+='6'
    main.setText(to_count)
button_six.clicked.connect(six)
# seven
def seven():
    global to_count
    to_count+='7'
    main.setText(to_count)
button_seven.clicked.connect(seven)
# eight
def eight():
    global to_count
    to_count+='8'
    main.setText(to_count)
button_eight.clicked.connect(eight)
# nine
def nine():
    global to_count
    to_count+='9'
    main.setText(to_count)
button_nine.clicked.connect(nine)
# zero
def zero():
    global to_count
    to_count+='0'
    main.setText(to_count)
button_zero.clicked.connect(zero)
# comma
def comma():
    global to_count
    if to_count == '':
        to_count = '0'
        to_count+='.'
    else:
        to_count+='.'
    main.setText(to_count)
button_comma.clicked.connect(comma)

# LOGICAL OPERATIONS
# +
def plus():
    global to_count
    to_count+='+'
    main.setText(to_count)
button_plus.clicked.connect(plus)
# -
def minus():
    global to_count
    to_count+='-'
    main.setText(to_count)
button_minus.clicked.connect(minus)
# /
def divide():
    global to_count
    to_count+='/'
    main.setText(to_count)
button_divide.clicked.connect(divide)
# *
def multiply():
    global to_count
    to_count+='*'
    main.setText(to_count)
button_multiply.clicked.connect(multiply)
# %
def percent():
    global to_count
    to_count+='%'
    main.setText(to_count)
button_percent.clicked.connect(percent)
# =
def equal():
    try:
        global to_count
        r = eval(to_count)
        main.setText(str(r))
        to_count = str(r)

        ##
    except ZeroDivisionError:
        main.setText("Error!")
        to_count = ''
button_equal.clicked.connect(equal)

# OTHERS
# ac
def ac():
    global to_count
    main.setText(str(0))
    to_count = ''
button_ac.clicked.connect(ac)








































# ICON
window.setWindowIcon(QIcon('C:\\Users\\USER\\Desktop\\OOP_dasturlash\\Sixth_lesson-Application\\HomeWork_25-Jan\\icon.jpg'))
window.show()
sys.exit(app.exec_())