# ScribbleSolver

## Project Overview

The ScribbleSolver is a machine learning model that combines Convolutional Neural Networks (CNNs) and Optical Character Recognition (OCR) technology to recognize and interpret handwritten mathematical equations. This project has resulted in a model that accurately identifies digits and mathematical symbols from handwritten input, effectively translating these into solvable equations.

Our model is highly accurate with a measured accuracy of 98.27%, and a minimized loss function of 0.656%. This showcases the successful application of machine learning techniques to solve complex, real-world problems.

## Dependencies
Python (>=3.7) <br>
TensorFlow (>=2.4.0) <br>
Keras (>=2.3.0) <br>
OpenCV (>=4.1.0) <br>
Numpy (>=1.19.5) <br>
Matplotlib (>=3.3.2) <br>

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
