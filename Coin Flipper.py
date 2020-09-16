#This program is designed to randomly generate either a 0 or a 1.
#0 being heads and 1 being tails, to resemble a coin flip.
#for now it only calculates the percentage of how many times a 0 or a 1 is generated from a million "flips"
import random
valid = True
numOfFlips = 100000000
h_count = 0
t_count = 0

for i in range(numOfFlips):
    th = random.randint(0, 1)
    if th == 1:
        t_count += 1
    elif th == 0:
        h_count += 1
        
    h_percentage = float(h_count / numOfFlips * 100)
    t_percentage = float(t_count / numOfFlips * 100)

print("heads " + str(h_count))
print("tails " + str(t_count))
print('the average percentage of heads appearing is ' + str(h_percentage) +'%.')
print('the average percentage of tails appearing is ' + str(t_percentage) +'%.')
