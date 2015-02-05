import pandas as pd
import matplotlib.pyplot as plt

# The data below has been taken from:
# http://data.gov.uk/dataset/statistics_on_obesity_physical_activity_and_diet_england/
# Released under the Open Government License:
# http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/

data = pd.ExcelFile("Obes-phys-acti-diet-eng-2014-tab.xls")
print data.sheet_names

# Read 2nd section, by age
data_age = data.parse(u'7.2', skiprows=4, skipfooter=14)
print data_age

# Rename Unnamed to year
data_age.rename(columns={u'Unnamed: 0': u'Year'}, inplace=True)

# Drop empties and reset index
data_age.dropna(inplace=True)
data_age.set_index('Year', inplace=True)


print "After Clean up:"
print data_age

# plot
data_age.plot()
plt.show()

# Plotting everything cause total to override everything. So drop it.
# Drop the total column and plot
data_age_minus_total = data_age.drop('Total', axis=1)
data_age_minus_total.plot()
plt.show()

plt.close()

# Plot children vs adults
data_age['Under 16'].plot(label="Under 16")
data_age['35-44'].plot(label="35-44")
plt.legend(loc="upper right")
plt.show()
