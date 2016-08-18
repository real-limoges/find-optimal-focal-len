import numpy as np

from scipy.stats import itemfreq

import matplotlib.pyplot as plt
import seaborn as sns

max_focal = 85

def void_generate_itemfreq(d, n):
  '''
  INPUT: Numpy Array of Integers, Top items to see (int)
  OUTPUT: Side effects - Outputs to terminal the top 3 focal lengths 
          and counts 
  '''
  print sorted(itemfreq(d), key = lambda x: x[1], reverse = True)[:n]


def void_histogram(d, title, lim=None):
  '''
  INPUT: Numpy array, title (string), 
         upper bound called lim (int, optional)
  OUTPUT: Saves plot to disk in images folder
  '''
  
  plot = sns.distplot(d)
  plot.set(xlim=(0, lim))

  fig = plot.get_figure()

  fig.savefig('../images/{}.png'.format(title))
  plt.close()

if __name__ == '__main__':

  data = np.loadtxt('../data/focal_lengths.txt').astype(int)
  
  # Masks out data that is moderate to super telephoto
  # Converts focal lengths to integers to make analysis easier
  mask_high_foc = np.where(data < max_focal)[0]
  wide_foc_data = data[mask_high_foc]
 
  print "Most frequent for all focal lengths"
  void_generate_itemfreq(data, 3)

  print "Most frequent wide - normal focal lengths"
  void_generate_itemfreq(wide_foc_data, 3)

  void_histogram(data, "All_Data")
  void_histogram(wide_foc_data, "Wide_To_Normal_Data", max_focal)
