from matplotlib import pyplot
years = [2013,2014,2015,2016,2017,2018,2019,2020]
companyA = [41595, 46000, 48912, 53310, 57200, 58000, 63000, 89000]
pyplot.plot(years, companyA, color='red', linestyle='--', marker='.', markersize=12)
pyplot.grid(True)
pyplot.legend("Company A")
pyplot.show()