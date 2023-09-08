# byte_generator
## Contents
* Introduction
* Milestone
* Functions and important varibles
* Running instructions

### Introduction
This is a script that converts an integer into an 8 bit binnary byte. this is then put into a generator function. 
#### The brief
Create a loop which iterates through a generator you define that generates incrementing binary bytes (8 digit numbers containing only ones and zeros) up to 256.

### Milestones
#### Milestone 1: Base 2 tool
Calculating n in 2^n as an integer our base 2 tool. This is conatianed in the cal_base.py and fun_base.py files.

#### Milestone 2: Dec to Bin tool
Using base 2 tool to convert an interger to a binary value. this is contained within the dec_to_bin.py and dec_bin.py

#### Milestone 3: byte generator
Puting code in to a generator. This is the in the byt_gen.py script.

#### Milestone 4
Refactor and optimize code

### Functions and important varibles

b2_fun(t) is for finding n in 2^n, where the argument (t) is the number you want to find floor power of.

decto_byt(b) is for converting a decimal to an eight bit byte binary value, the argument (b) is the decimal integer you want to convert.

lam_fig(b,n) is a lambda function for calculating the difference between 2^n where n is the base 2 floor power and b is the number you calculated it from.

ls_byt is a list that contains all the output.


### Running instructions
python3 byt_gen.py

