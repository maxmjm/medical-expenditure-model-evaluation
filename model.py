import pandas

# Read data file
df = pandas.read_csv("medical_charges_with_descriptors.csv")

# Examine file structure
file_structure = df.info()
print(file_structure)
