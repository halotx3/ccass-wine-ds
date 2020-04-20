# use this file with following script in Juypter notebook.
# with open('./share/common.py') as fin:
#    exec(fin.read())

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# import seaborn here because otherwise it will mess up warnings
import seaborn as sns
import warnings
import logging

# https://github.com/tensorflow/tensorflow/issues/8340#issuecomment-332212742
# disabling tensorflow warnings, feel free to uncomment out the next 2 lines if you want to suppress warnings
# logging.getLogger("tensorflow").disabled = True
# warnings.simplefilter("ignore")

pd.set_option("display.max_rows", 13)
pd.set_option('display.max_columns', 8)
pd.set_option("display.latex.repr", False)
pd.set_option('max_colwidth', 30)