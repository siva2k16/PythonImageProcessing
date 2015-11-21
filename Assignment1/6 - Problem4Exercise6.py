#6. Use rng to write a function that returns the roll of a six-sided die. 
#	30/08/2015		Draft Version
# Random dice print output results

import random
#use random function
randomdice = random.Random()
#roll dice and submit results for every throw 6 runs

for i in range(1,6):
    #specify range start, stop
    dice_output_value = randomdice.randrange(1,7)
    #print output
    print dice_output_value
