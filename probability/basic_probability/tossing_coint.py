

import random


head = 0
tail = 0
for i in range(1, 1000000):
    coin = random.randint(1, 2)
    if(coin == 1):
        head += 1
    else:
        tail += 1

print("No of head : " + str(head))
print("No of tail : " + str(tail))
