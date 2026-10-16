import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from sklearn.metrics import root_mean_squared_error, mean_squared_error, r2_score
 
def get_data(file, feature1, feature2, sample_size):
	
	# Lager pandas datafram og fjerner rader med manglende data	
	df = pd.read_csv(file, usecols=[feature1, feature2]).dropna()
	# Henter ut n datapunkter
	df_sample = df.sample(n=sample_size, random_state=42)
	
	x = df_sample[feature1]
	y = df_sample[feature2]

	return x, y

def main():

	PATH = "figures"
	if not os.path.exists(PATH):
		os.makedirs(PATH)

	# Henter ut data
	# x - havdybde
	# y - temperatur
	x, y = get_data("bottle.csv", "Depthm", "T_degC", sample_size=2000)
	
	# Perform regression and plot
	x_line = np.linspace(x.min(), x.max(), 100)
	
	filename = "regression_result.txt"
	with open(filename, "w") as f:
		f.write("-Results polynomial regression Temperature vs. Depth-\n\n")
	
	# Utfører polynomial regresjon med flere grader
	for degree in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
		plt.figure()
		plt.scatter(x, y, alpha=0.4, label="Data")
		#plt.gca().invert_yaxis()
		#plt.gca().invert_xaxis()
		plt.xlabel("Depth (meters)", fontsize=15)
		plt.ylabel("Temperature (C)", fontsize=15)
		plt.title("Depth vs. Temperature", fontsize=15)
		plt.grid(True)
	
		# Perform regression
		coeff = np.polyfit(x, y, degree)
		model = np.poly1d(coeff)
		
		# Plott regression line against data
		plt.plot(x_line, model(x_line), linestyle="--", color="r", label=f"Regression line degree {degree}")
		plt.legend(fontsize=15)
		filename_ = os.path.join(PATH, f"regression_line_degree_{degree}.png")
		plt.savefig(filename_)
	
		#plt.show()
		
		r2 = r2_score(y, model(x))
		rmse = root_mean_squared_error(y, model(x))	
		
		#print("--------------------------")
		#print(f"Polynomgrad {degree}")
		#print(f"R²: {r2:.2f}")
		#print(f"RMSE: {rmse:.2f}")
		#print("----------------------------------")
		
		
		with open(filename, "a", encoding="utf-8") as f:
			f.write("--------------------------------------------------\n")
			f.write(f"Polynomial degree {degree}\n")
			f.write(f"R²: {r2:.2f}\n")
			f.write(f"RMSE: {rmse:.2f}\n")
			
		with open(filename, "a", encoding="utf-8") as f:
			f.write("\n")
		
if __name__=="__main__":
	main()






