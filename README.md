
Basic Requirements (optional)
1. Model Description
The arm consists of three segments (s) connected by joints (w).
The first joint is fixed at point w1 = O.
At the end of the last segment, there is a manipulator (M) in the form of a schematically represented hand.
The manipulator and the last segment are also connected by a joint.
Each joint allows free rotation of the segment that follows it.

2. Segment Length
Each segment has a fixed length.

3. Joint Constraints
Each joint has a defined range of permissible angles and a defined rotation speed.

4. Manipulator Orientation Modes
The user can choose one of two manipulator orientation modes:
The manipulator remains locked and moves together with the last segment as a single unit.
The manipulator maintains its orientation while the arm is moving.

5. Continuous Motion
The program demonstrates continuous arm movement within the range defined by the previously set parameters.
--------------------------------------------------------------------------------------------------------------------------------------

Additional Requirements (optional)
a) Create a GUI to facilitate program usage.
b) Allow the user to change the length of each segment during program execution, including setting a segment length to 0.
c) Allow the user to set the rotation speed and angle range for each joint during program execution.
d) Allow the user to change the position of the first joint during program execution.
e) Ensure that for no parameter values do the segments and the manipulator overlap.
