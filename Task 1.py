import pandas as pd

df = pd.read_csv('csv.csv')   # load the CSV file

# calculate total marks and percentage

df["Total"] = df["Subject 1"] + df["Subject 2"] + df["Subject 3"]

df["Percentage"] = (df["Total"] / 300) * 100

df["Percentage"] = df["Percentage"].round(2)   # round to 2 decimals

# function to assign grades


def calculate_grade(pct):
    if pct >= 90:
        return "A"
    elif pct >= 80:
        return "B"
    elif pct >= 70:
        return "C"
    elif pct >= 60:
        return "D"
    else:
        return "F"


df["Grade"] = df["Percentage"].apply(calculate_grade)   # apply grading

df["Percentage"] = df["Percentage"].astype(str) + " %"  # add % sign

# get top 5 students by total marks

top_students = df.sort_values(by="Total", ascending=False).head(5)

print("\nTop 5 Students:")
print(top_students[["Name", "Roll Number", "Total", "Percentage", "Grade"]])

df.to_csv("final_results.csv", index=False)   # save final results to CSV
