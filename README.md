# ScribbleSolver

## Project Overview

The ScribbleSolver is a web based machine learning model that combines Convolutional Neural Networks (CNNs) and Optical Character Recognition (OCR) technology to recognize and interpret handwritten mathematical equations. This project has resulted in a model that accurately identifies digits and mathematical symbols from handwritten input, effectively translating these into solvable equations.

Our model is highly accurate with a measured accuracy of 98.27%, and a minimized loss function of 0.656%. This showcases the successful application of machine learning techniques to solve complex, real-world problems.

## Dependencies
```bash
Flask==2.1.1
gunicorn==20.1.0
pybase64
Pillow
requires.io
numpy
sympy
opencv-python-headless
regex
tensorflow
keras
```

## Keep in mind:
Scribble:<br>
1. Scribble any one variable equation on the drawing board.<br>
2. Note: The model is trained only on "x", so make sure to use "x" only. It can be trained on more variables but to improve efficiency and simplicity we used x.<br>
3. Make sure there is space between each number so that it recognises easily.<br>
4. Equations should be in the format of "ax²+bx+c=0". Make sure to include "=0" or "=anything" at the end. <br>
5. Cannot handle negative power.<br>
6. Press the solve equation button and wait for few seconds for the roots.<br>
<br>
Enter: <br>
1. Enter the equation in the input field.<br>
2. Equations should be in the format of "ax^2 + bx + c = 0". Make sure to include "=0" or "=anything" at the end. <br>
3. Can handle negative power.<br>
4. Press the solve equation button and wait for few seconds for the roots.<br>
<br>
<img width="1512" alt="Screenshot 2023-07-17 at 5 29 43 AM" src="https://github.com/ritessshhh/ScribbleSolver/assets/81812754/1d3650af-ff15-4a98-88e1-3d9199a8d87c">
The digits are not recognisable when they overlap each other's space.<br>
<img width="1512" alt="Screenshot 2023-07-17 at 5 29 43 AM" src="https://github.com/ritessshhh/ScribbleSolver/assets/81812754/39d66a52-468d-493c-bacd-71e30dd49154">
The digits are recognisable when they are in their own space.<br>

# How to use?
## Scribble:
1. Scribble eqution on the drawing pad.
<img width="1512" alt="Screenshot 2023-07-17 at 5 29 43 AM" src="https://github.com/ritessshhh/ScribbleSolver/assets/81812754/e9f33421-0d25-42b4-a384-152031b64ab0">


2. Press solve equation button to solve.
<img width="1512" alt="Screenshot 2023-07-17 at 5 30 00 AM" src="https://github.com/ritessshhh/ScribbleSolver/assets/81812754/7d1426b6-76e8-4c5b-b846-7a79da31a713">

# Enter:
1. Enter an equation in the input field.
<img width="1512" alt="Screenshot 2023-07-17 at 5 31 00 AM" src="https://github.com/ritessshhh/ScribbleSolver/assets/81812754/ca606a5f-d01e-428a-b009-755cf9c18764">


2. Press solve equation button to solve.
<img width="1512" alt="Screenshot 2023-07-17 at 5 31 17 AM" src="https://github.com/ritessshhh/ScribbleSolver/assets/81812754/9ae7c042-86b4-4a08-89ac-8b0c5c515c74">

# Error:
1. Any wrong input or invalid equations are rejected.<br>
   a. Scribble:
   <img width="1512" alt="Screenshot 2023-07-17 at 5 31 35 AM" src="https://github.com/ritessshhh/ScribbleSolver/assets/81812754/3f224cab-29db-40fa-9bf7-d11dacacf3d3">
   b. Enter:
   <img width="1512" alt="Screenshot 2023-07-17 at 5 31 50 AM" src="https://github.com/ritessshhh/ScribbleSolver/assets/81812754/692e9bb2-04a0-40ff-87d3-082db3bb7e74">


   




## Installation
Clone the repo
```bash
git clone https://github.com/ritessshhh/ScribbleSolver
```

## Model
The model uses a combination of Convolutional Neural Networks (CNNs) for feature extraction from the image inputs, and Optical Character Recognition (OCR) technology for converting the detected features into understandable symbols.

Our CNN architecture consists of a series of convolutional, max pooling, and dense layers, with a final softmax layer for multi-class classification of the different digits and mathematical symbols.

The OCR technology then translates these classified features into a form that can be used to generate a solvable equation.

## Performance
Our model achieved an accuracy of 98.27%, with a minimized loss function of 0.656%. This level of performance demonstrates that our model is highly effective at recognizing and interpreting handwritten mathematical equations.

## Future Work
We are planning to extend this model to recognize more complex mathematical symbols and to work on larger and more complex equations. Feedback and contributions are always welcome.

## License
```
Copyright [2023] [Ritesh Chavan]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
