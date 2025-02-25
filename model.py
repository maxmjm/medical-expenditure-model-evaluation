import pandas
import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# Read data file
df = pandas.read_csv("medical_charges_with_descriptors.csv")

# Examine file structure
print("\n")
df_structure = df.info()
print(df_structure)
print("\n")

# Describe file contents
df_describe = df.describe()
print(df_describe)
print("\n")

# Chart settings
sns.set_style("darkgrid")
matplotlib.rcParams["font.size"] = 14
matplotlib.rcParams["figure.figsize"] = (10, 6)
matplotlib.rcParams["figure.facecolor"] = "#00000000"

# Display age distribution of data as a histogram and box-plot
fig1 = px.histogram(df, x="age", marginal="box", nbins=47, title="Distribution of Age") # 47 bins (one for each age 18-64)
fig1.update_layout(bargap=0.1)
fig1.show()

# Display bmi distribution of data as a histogram and box-plot
fig2 = px.histogram(df, x="bmi", marginal="box", color_discrete_sequence=["red"], title="Distribution of BMI")
fig2.update_layout(bargap=0.1)
fig2.show()

# Display medical charges distribution of data as a histogram and box-plot
fig3 = px.histogram(df, x="charges", marginal="box", color="smoker", color_discrete_sequence=["green", "grey"], title="Distribution of Annual Medical Charges")
fig3.update_layout(bargap=0.1)
fig3.show()
