# Cross Solver
An interactive Rubik's cube with the cross-solving prompts of the CFOP method

## Demo
![demo](https://github.com/EmperorGesar/Cross-Solver/assets/50392401/784d863c-2d8b-49f9-8a9e-a845f46ead0c)

## Description
- The UI is implemented with the [matplotlib](https://matplotlib.org/) 3D
- The scrambler is provided by the [cubescrambler](https://pypi.org/project/cubescrambler/), which follows the [WCA](https://www.worldcubeassociation.org/regulations/#4b3) standard
- The cross-solving is using the A* algorithm, aimed to yield the total turns less than 8

## Controls
- Press the buttons to interact with the cube
- "Rand" to scramble, "Cross" to solve the cross
- The 12 buttons at the bottom to turn the cube
- White face is D, Blue face is F
- Drag the cube to rotate
