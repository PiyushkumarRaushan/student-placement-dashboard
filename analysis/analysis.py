import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------
# Load Dataset
# -------------------------

base_dir = os.path.dirname(os.path.dirname(__file__))

csv_path = os.path.join(base_dir, "students.csv")

df = pd.read_csv(csv_path)

# -------------------------
# Create Charts Folder
# -------------------------

charts_dir = os.path.join(
    base_dir,
    "static",
    "charts"
)

os.makedirs(
    charts_dir,
    exist_ok=True
)

# -------------------------
# Basic Analysis
# -------------------------

print("\n===== DATASET =====")
print(df.head())

print("\n===== AVERAGE CGPA =====")
print(df["CGPA"].mean())

print("\n===== PLACEMENT COUNT =====")
print(df["Placed"].value_counts())

# -------------------------
# Chart 1
# CGPA Distribution
# -------------------------

plt.figure(figsize=(8,5))

plt.hist(
    df["CGPA"],
    bins=5
)

plt.title("CGPA Distribution")

plt.xlabel("CGPA")

plt.ylabel("Number of Students")

plt.savefig(
    os.path.join(
        charts_dir,
        "cgpa_distribution.png"
    )
)

plt.close()

# -------------------------
# Chart 2
# Placement Distribution
# -------------------------

placement_counts = df["Placed"].value_counts()

plt.figure(figsize=(6,6))

plt.pie(
    placement_counts,
    labels=placement_counts.index,
    autopct="%1.1f%%"
)

plt.title("Placement Distribution")

plt.savefig(
    os.path.join(
        charts_dir,
        "placement_distribution.png"
    )
)

plt.close()

# -------------------------
# Chart 3
# Internships vs Placement
# -------------------------

grouped = df.groupby(
    "Placed"
)["Internships"].mean()

plt.figure(figsize=(6,5))

grouped.plot(
    kind="bar"
)

plt.title(
    "Average Internships by Placement Status"
)

plt.ylabel(
    "Average Internships"
)

plt.savefig(
    os.path.join(
        charts_dir,
        "internships_vs_placement.png"
    )
)

plt.close()

print("\nCharts Generated Successfully!")