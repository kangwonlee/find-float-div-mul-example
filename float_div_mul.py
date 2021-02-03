import numpy as np
import pandas as pd


def main():

  num_r = np.arange(1, 20+1)
  den_r = num_r

  num, den = np.meshgrid(num_r, den_r)
  num = num.flatten()
  den = den.flatten()

  div = num / den
  mul_den = div * den
  df = pd.DataFrame(
    index=['num', 'den', 'div', 'mul'],
    data=[
        num, den, div, mul_den,
    ]
  ).T

  df['div str'] = df['div'].astype('str').str.strip('0')
  df['div len'] = df['div str'].apply(len)
  df['mul str'] = df['mul'].astype('str').str.strip('0')
  df['mul len'] = df['mul str'].apply(len)
  
  return df.sort_values('mul len', ascending=False)


if "__main__" == __name__:
  print(main())
