
import pandas as pd
import numpy as np
# Step 1: Read the final_output.xlsx file into a DataFrame
final_df = pd.read_excel('final_output.xlsx')

# Step 2: Create a pivot table
pivot_table = final_df.pivot_table(index='Edited By', columns='Status', aggfunc='size', fill_value=0)

# Rename columns to match required headers
pivot_table.columns = ['Breached', 'Not Breached']

# Step 3: Calculate 'Grand Total'
pivot_table['Grand Total'] = pivot_table['Breached'] + pivot_table['Not Breached']

# Round off 'SLA %' to 2 decimal places
pivot_table['SLA %'] = ((pivot_table['Not Breached'] / pivot_table['Grand Total']) * 100).round(2)

# Reset index to move 'Edited By' to the headers
pivot_table.reset_index(inplace=True)

# Convert pivot table to HTML without the index
html_table = pivot_table.to_html(classes='table table-striped', index=False)


# Step 6: Write the HTML table to an HTML file
with open('pivot_table.html', 'w') as f:
    f.write(html_table)
