from keras.models import load_model
import numpy as np
import cv2
from sympy import *
import re
#%%
model = load_model('model/newModel-7.keras')


class Solver:
    def __init__(self, equation):
        self.equation = str(equation)

    def convertEquationIntoGeneralForm(self):
        self.equation = self.equation.replace('^', '**')
        self.equation = re.sub(r'(\d+)(x)', r'\1*\2', self.equation)
        equalIndx = self.equation.find('=')

        if equalIndx == -1:
            self.equation += '=0'
            equalIndx = len(self.equation) - 1

        leftSide = self.equation[:equalIndx].strip()
        rightSide = self.equation[equalIndx + 1:].strip()

        print("Before processing: ", leftSide, rightSide)

        if rightSide:
            right_expr = sympify(rightSide)
            right_terms = Add.make_args(right_expr)
            flipped_terms = [-1 * term for term in right_terms]
            self.equation = sympify(leftSide) + sum(flipped_terms)
        else:
            self.equation = sympify(leftSide)

        self.equation = str(self.equation) + '=0'
        print("After processing: ", self.equation)

    def solveEquation(self):
        try:
            x = symbols('x')
            print("Before conversion:", self.equation)
            self.convertEquationIntoGeneralForm()
            print("After conversion:", self.equation)

            if "=" in self.equation:
                left, right = self.equation.split("=")
                sympy_eq = Eq(sympify(left), sympify(right))
            else:
                print("Invalid equation.")
                return

            roots = solve(sympy_eq, x)
            decimal_roots = [root.evalf(2) for root in roots]

            return decimal_roots
        except Exception as e:
            print("An error occurred while parsing or solving the equation: ", e)
            return "Equation not readable. Tip: Have more space between each numbers."

def solution(image):

    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    original_height, original_width = img.shape[:2]
    new_width = original_width * 2
    new_height = original_height * 2
    img = cv2.resize(img, (new_width, new_height), interpolation = cv2.INTER_CUBIC)

    img = ~img
    ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ctrs, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
    img_data = []
    rects = []
    for c in cnt:
        x, y, w, h = cv2.boundingRect(c)
        rect = [x, y, w, h]
        rects.append(rect)
    bool_rect = []
    for r in rects:
        l = []
        for rec in rects:
            flag = 0
            if rec != r:
                if r[0] < (rec[0] + rec[2] + 10) and rec[0] < (r[0] + r[2] + 10) and r[1] < (rec[1] + rec[3] + 10) and \
                        rec[1] < (r[1] + r[3] + 10):
                    flag = 1
                l.append(flag)
            if rec == r:
                l.append(0)
        bool_rect.append(l)
    dump_rect = []
    for i in range(0, len(cnt)):
        for j in range(0, len(cnt)):
            if bool_rect[i][j] == 1:
                area1 = rects[i][2] * rects[i][3]
                area2 = rects[j][2] * rects[j][3]
                if area1 == min(area1, area2):
                    dump_rect.append(rects[i])
    final_rect = [i for i in rects if i not in dump_rect]
    for r in final_rect:
        x = r[0]
        y = r[1]
        w = r[2]
        h = r[3]
        im_crop = thresh[y:y + h + 10, x:x + w + 10]

        im_resize = cv2.resize(im_crop, (28, 28))

        im_resize = np.reshape(im_resize, (1, 28, 28))
        img_data.append(im_resize)

    operation = ''
    s = ""
    for i in range(len(img_data)):
        img_data[i] = np.array(img_data[i])
        img_data[i] = img_data[i].reshape(1, 28, 28, 1)
        result = np.argmax(model.predict(img_data[i]), axis=1)

        if result[0] == 0:
            s += '0'
        if result[0] == 1:
            s += '1'
        if result[0] == 2:
            s += '2'
        if result[0] == 3:
            s += '3'
        if result[0] == 4:
            s += '4'
        if result[0] == 5:
            s += '5'
        if result[0] == 6:
            s += '6'
        if result[0] == 7:
            s += '7'
        if result[0] == 8:
            s += '8'
        if result[0] == 9:
            s += '9'
        if result[0] == 10:
            s += '+'
        if result[0] == 11:
            s += '-'
        if result[0] == 12:
            s += 'x'

    print(s)

    StringEquation = ""
    for i in range(len(s)):
        a = s[i]
        if a.isdigit() == False and a.isalpha() == False and i < len(s) - 1:
            if a == s[i + 1] == '-':
                StringEquation += '='
            else:
                StringEquation += a
        if a.isalpha():
            if i > 0 and s[i - 1].isdigit():
                StringEquation += "*" + a
            else:
                StringEquation += a
        if a.isdigit():
            if i > 0:
                if s[i - 1].isdigit():
                    StringEquation += a
                elif s[i - 1].isalpha():
                    StringEquation += "^" + a
                else:
                    StringEquation += a
            else:
                StringEquation += a

    newStr = ""
    l = list(StringEquation)
    for i in range(len(l)):
        if l[i] == "=":
            newStr = l[:i + 1] + l[i + 2:]

    equ = ""
    for i in newStr:
        equ += i
    solution = Solver(equ)
    roots = solution.solveEquation()


    if roots != 'Equation not readable. Tip: Have more space between each numbers.':
      st = []
      for i in roots:
          i = str(i)
          st.append(i)

      roots = ', '.join(st)

    return equ, roots