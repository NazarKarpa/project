import pandas as pd
import numpy as np
from random import*
numbers = [randint(-50,50) for i in range(41)]
s = pd.Series(numbers)
print(s[::-1])



