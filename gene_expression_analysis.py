"""
Gene Expression Analysis: Control vs Cancer
--------------------------------------------
Analyzes fold-change in gene expression between control and cancer samples
for five well-known cancer-associated genes (TP53, BRCA1, EGFR, MYC, KRAS),
flags significantly upregulated genes, and visualizes the comparison as a
grouped bar chart.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. Load expression data into a DataFrame
# ---------------------------------------------------------
data = {
    "Gene": ["TP53", "BRCA1", "EGFR", "MYC", "KRAS"],
    "Control": [12, 8, 15, 10, 7],
    "Cancer": [25, 18, 30, 22, 16],
}

df = pd.DataFrame(data)

# ---------------------------------------------------------
# 2. Calculate Fold Change = Cancer / Control
# ---------------------------------------------------------
df["Fold_Change"] = df["Cancer"] / df["Control"]

print("Gene Expression Data:\n")
print(df.to_string(index=False))

# ---------------------------------------------------------
# 3. Filter genes with Fold Change > 1.8 (upregulated in cancer)
# ---------------------------------------------------------
FOLD_CHANGE_THRESHOLD = 1.8
highly_expressed = df[df["Fold_Change"] > FOLD_CHANGE_THRESHOLD][["Gene", "Fold_Change"]]

print(f"\nHighly Expressed Genes (Fold Change > {FOLD_CHANGE_THRESHOLD}):")
print(highly_expressed.to_string(index=False))

# ---------------------------------------------------------
# 4. Plot grouped bar chart: Control vs Cancer per gene
# ---------------------------------------------------------
genes = df["Gene"].to_numpy()
control_vals = df["Control"].to_numpy()
cancer_vals = df["Cancer"].to_numpy()

x = np.arange(len(genes))
bar_width = 0.35

fig, ax = plt.subplots(figsize=(9, 6))

bars_control = ax.bar(x - bar_width / 2, control_vals, bar_width,
                       label="Control", color="#4C72B0")
bars_cancer = ax.bar(x + bar_width / 2, cancer_vals, bar_width,
                      label="Cancer", color="#C44E52")

# Annotate bars with their values
for bars in (bars_control, bars_cancer):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f"{height:.0f}",
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha="center", va="bottom", fontsize=9)

ax.set_xlabel("Gene", fontsize=11)
ax.set_ylabel("Expression Level", fontsize=11)
ax.set_title("Gene Expression: Control vs Cancer", fontsize=13, fontweight="bold")
ax.set_xticks(x)
ax.set_xticklabels(genes)
ax.legend()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("gene_expression_plot.png", dpi=150)
print("\nChart saved as gene_expression_plot.png")

plt.show()
