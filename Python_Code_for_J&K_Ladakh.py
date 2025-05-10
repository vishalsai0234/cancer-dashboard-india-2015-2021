import pandas as pd

# Load your CSV file
df = pd.read_csv("cancer_data.csv")

# Filter the rows where state_ut is "Jammu & Kashmir and Ladakh"
jk_ladakh_rows = df[df['state_ut'] == "Jammu & Kashmir and Ladakh"]

# Create two copies of these rows: one for Jammu and Kashmir, one for Ladakh
jk_rows = jk_ladakh_rows.copy()
jk_rows['state_ut'] = "Jammu and Kashmir"
jk_rows['value'] = jk_rows['value'] / 2
jk_rows['upper'] = jk_rows['upper'] / 2
jk_rows['lower'] = jk_rows['lower'] / 2
jk_rows['ci_range'] = jk_rows['ci_range'] / 2

ladakh_rows = jk_ladakh_rows.copy()
ladakh_rows['state_ut'] = "Ladakh"
ladakh_rows['value'] = ladakh_rows['value'] / 2
ladakh_rows['upper'] = ladakh_rows['upper'] / 2
ladakh_rows['lower'] = ladakh_rows['lower'] / 2
ladakh_rows['ci_range'] = ladakh_rows['ci_range'] / 2

# Drop the original combined row
df = df[df['state_ut'] != "Jammu & Kashmir and Ladakh"]

# Append the split rows
df = pd.concat([df, jk_rows, ladakh_rows], ignore_index=True)

# Optional: Save the new file
df.to_csv("cleaned_states.csv", index=False)