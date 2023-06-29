import time
import numpy as np


msg = "Hello World"
for i in range(0, 5):
    print(msg, i)
    print(np.random.randint(1, 9))
    time.sleep(0.5)
