

import pandas as pd
import matplotlib.pyplot as plt

# brings in 2 files
QCOM_file = input("Enter QCOM file:").strip()
AMD_file = input ("Enter AMD file:").strip()

# reads through files
QCOM = pd.read_csv(QCOM_file)
AMD = pd.read_csv(AMD_file)

# sets 'Date' into readable form and filters for specific year
QCOM['Date'] = pd.to_datetime(QCOM['Date'])
QCOM = QCOM[QCOM['Date'].dt.year == 2022]
AMD['Date'] = pd.to_datetime(AMD['Date'])
AMD = AMD[AMD['Date'].dt.year == 2022]

# used.info() to see data types and saw the '$' created an error
# corrects data type so pandas can work w/ it
# cleans string + makes it a float
QCOM['Close/Last'] = pd.to_numeric(QCOM['Close/Last'].str.replace('$','',regex=False))
AMD['Close/Last'] = pd.to_numeric(AMD['Close/Last'].str.replace('$','',regex=False))

# calculate daily return for each stock
QCOM['Return'] = QCOM['Close/Last'].pct_change()
QCOM['Cum'] = (1+QCOM['Return']).cumprod()
AMD['Return'] = AMD['Close/Last'].pct_change()
AMD['Cum'] = (1+AMD['Return']).cumprod()

# filters tables so only desired columns still appear
QCOM = QCOM[['Date', 'Cum']]
AMD = AMD[['Date', 'Cum']]

# merges tables w/ desired info (centered on one specific column)
Comparison_table = pd.merge(QCOM, AMD, on='Date', suffixes=('_QCOM', '_AMD'))

# sets up plot (whats in it and how it should look)
Comparison_table.plot(x = 'Date', y = ['Cum_QCOM', 'Cum_AMD'], figsize=(20,10))
plt.title('Investment Growth: QCOM vs. AMD (2022)')
plt.xlabel('Year')
plt.ylabel('Value of $1 Investment')
plt.grid(True, linestyle='--', alpha = .5)

plt.show()

