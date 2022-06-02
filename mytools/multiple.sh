#!/bin/bash


# python3.9 src/main.py --input_folder ./imgs2/ &
# python3.9 src/main.py --input_folder ./imgs1/ &
# python3.9 src/main.py --input_folder ./imgs2/ &

# // python3.9 src/main.py --input_folder ./imgs3/
# // python3.9 src/main.py --input_folder ./imgs4/

# rt_launch -w 10 15 -- ./multiple.sh 

000

rt_launch -w 20000 20000 --  python3.9 src/main.py --input_folder ./imgs4/ & 
rt_launch -w 10000 10000 --  python3.9 src/main.py --input_folder ./imgs2/ & 
rt_launch -w 25000 25000 --  python3.9 src/main.py --input_folder ./imgs1/ & 
rt_launch -w 25000 25000 --  python3.9 src/main.py --input_folder ./imgs3/ & 
rt_launch -w 45000 45000 --  python3.9 src/main.py --input_folder ./imgs0/ & 