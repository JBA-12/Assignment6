#Verifying the obtained probability distribution.
#Let Pr{X = 0} be Pa
#Let Pr{X = 1} be Pb
#Let Pr{X = 2} be Pc
#Let Pr{X = 3} be Pd

Pa = 125/216
Pb = 75/216
Pc = 15/216
Pd = 1/216

#Checks for the probability condition i.e., less than or equals to 1 and greater than or equals to 0.
if Pa<=1 and Pa>=0:
   "continue"
if Pb<=1 and Pb>=0:
   "continue"
if Pc<=1 and Pc>=0:
   "continue"
if Pd<=1 and Pd>=0:
   "continue"

#Checks whether the sum of probabilities is 1 or not.
p = Pa + Pb + Pc + Pd

if p == 1:
   print("Pr{X = 0} = 125/216, Pr{X = 1} = 75/216, Pr{X = 2} = 15/216, Pr{X = 3} = 1/216")