#KEYWORD RESEARCH

import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()

#KEYWORD INTEREST BY REGION

trends.build_payload(kw_list = ["Python"]) #INSERT YOUR TOPIC HERE
data = trends.interest_by_region()
print(data.sample(10))

#VISUALISATION

df = data.sample(15)
df.reset_index().plot(x = "geoName", y = "Python", figsize = (120,16), kind="bar")
plt.show()


