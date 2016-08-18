import numpy as np

from scipy.stats import itemfreq

import matplotlib.pyplot as plt
import seaborn as sns

max_focal = 85.0

if __name__ == '__main__':

  data = np.loadtxt('../data/focal_lengths.txt')
  
  # Masks out data that is moderate to super telephoto
  mask_high_foc = np.where(data < max_focal)[0]
  wide_foc_data = data[mask_high_foc]

  
