import csv

input_filename = "CCD0_20231222 .csv"
output_filename = "CCD0_20231222_demo.csv"  # You can change the output file name as needed

with open(input_filename, "r", newline="") as infile:
    reader = csv.DictReader(infile)
    rows = list(reader)

# Check if "Ai返回码" and "G" are in the header
if "Ai返回码" in reader.fieldnames and "G" in reader.fieldnames:
    # Iterate through rows
    for row in rows:
        ai_code_value = int(row["Ai返回码"])

        # Check the value and write the corresponding string in the "G" column
        if ai_code_value == 1:
            row["G"] = "毛刺"
        elif ai_code_value == 2:
            row["G"] = "缺胶"
        elif ai_code_value == 3:
            row["G"] = "挤压"
        elif ai_code_value == 4:
            row["G"] = "斑点"

    # Write the modified rows to a new CSV file
    with open(output_filename, "w", newline="") as outfile:
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # Print the modified rows
    with open(output_filename, "r", newline="") as printfile:
        print(reader.fieldnames)
        print(printfile.read())
else:
    print("Column 'Ai返回码' or 'G' not found in the header.")
