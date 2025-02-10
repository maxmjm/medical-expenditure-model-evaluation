import pandas

# Read data file
df = pandas.read_csv("medical_charges_with_descriptors.csv")

# Examine file structure
df_structure = df.info()
print(df_structure)

# Describe file contents
df_describe = df.describe()
print(df_describe)
