"""
generate_charts_smdm.py
Run this in your project folder (where Wholesale Customer.csv, Survey-1.csv,
and "A & B shingles-1.csv" live).
Creates an /images folder with all charts referenced in the README.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import numpy as np
from scipy import stats
import os, warnings
warnings.filterwarnings("ignore")

os.makedirs("images", exist_ok=True)
sns.set_theme(style="whitegrid", palette="muted")
BLUE    = "#2563EB"
GREEN   = "#16A34A"
ORANGE  = "#F59E0B"
RED     = "#DC2626"

# ══════════════════════════════════════════════════════════════════════════════
# PROBLEM 1 — WHOLESALE CUSTOMER DATA
# ══════════════════════════════════════════════════════════════════════════════
wc = pd.read_csv("Wholesale Customer.csv")
wc.columns = wc.columns.str.strip()
print("Wholesale columns:", wc.columns.tolist())

SPEND_COLS = ["Fresh", "Milk", "Grocery", "Frozen", "Detergents_Paper", "Delicassen"]
# Handle alternate column names gracefully
available = [c for c in SPEND_COLS if c in wc.columns]

# ── Chart 1a : Mean spend by Region ──────────────────────────────────────────
if "Region" in wc.columns and available:
    region_map = {1: "Lisbon", 2: "Oporto", 3: "Other"}
    wc["Region_Name"] = wc["Region"].map(region_map).fillna(wc["Region"].astype(str))
    region_spend = wc.groupby("Region_Name")[available].mean()

    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.arange(len(available))
    width = 0.25
    colors = [BLUE, ORANGE, GREEN]
    for i, (region, row) in enumerate(region_spend.iterrows()):
        ax.bar(x + i * width, row.values, width, label=region, color=colors[i % 3])
    ax.set_xticks(x + width)
    ax.set_xticklabels(available, rotation=20, ha="right")
    ax.set_ylabel("Mean Annual Spend (monetary units)")
    ax.set_title("Mean Annual Spend by Product Category & Region", fontsize=14, fontweight="bold")
    ax.legend(title="Region")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig("images/01_spend_by_region.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Chart 1a saved")

# ── Chart 1b : Mean spend by Channel ─────────────────────────────────────────
if "Channel" in wc.columns and available:
    channel_map = {1: "Hotel/Restaurant/Cafe", 2: "Retail"}
    wc["Channel_Name"] = wc["Channel"].map(channel_map).fillna(wc["Channel"].astype(str))
    channel_spend = wc.groupby("Channel_Name")[available].mean()

    fig, ax = plt.subplots(figsize=(9, 5))
    x = np.arange(len(available))
    width = 0.35
    for i, (ch, row) in enumerate(channel_spend.iterrows()):
        ax.bar(x + i * width, row.values, width, label=ch, color=[BLUE, ORANGE][i % 2])
    ax.set_xticks(x + width / 2)
    ax.set_xticklabels(available, rotation=20, ha="right")
    ax.set_ylabel("Mean Annual Spend (monetary units)")
    ax.set_title("Mean Annual Spend by Product Category & Channel", fontsize=14, fontweight="bold")
    ax.legend(title="Channel")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig("images/02_spend_by_channel.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Chart 1b saved")

# ── Chart 1c : Coefficient of Variation (item variability) ───────────────────
if available:
    cv = (wc[available].std() / wc[available].mean() * 100).sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(8, 4))
    bars = ax.bar(cv.index, cv.values, color=[RED if v == cv.max() else BLUE for v in cv.values])
    ax.set_ylabel("Coefficient of Variation (%)")
    ax.set_title("Product Category Variability (CV%)\nHigher = More Inconsistent Spending", fontsize=13, fontweight="bold")
    for bar in bars:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f"{bar.get_height():.1f}%", ha="center", fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig("images/03_variability_cv.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Chart 1c saved")

# ── Chart 1d : Box plots for outlier detection ────────────────────────────────
if available:
    fig, ax = plt.subplots(figsize=(10, 5))
    data_to_plot = [wc[c].dropna().values for c in available]
    bp = ax.boxplot(data_to_plot, patch_artist=True, labels=available,
                    medianprops=dict(color=RED, linewidth=2))
    for patch in bp["boxes"]:
        patch.set_facecolor(BLUE)
        patch.set_alpha(0.5)
    ax.set_ylabel("Annual Spend (monetary units)")
    ax.set_title("Spend Distribution & Outliers by Product Category", fontsize=13, fontweight="bold")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig("images/04_boxplot_outliers.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Chart 1d saved")

# ══════════════════════════════════════════════════════════════════════════════
# PROBLEM 2 — UNIVERSITY SURVEY DATA
# ══════════════════════════════════════════════════════════════════════════════
try:
    sv = pd.read_csv("Survey-1.csv")
    sv.columns = sv.columns.str.strip()
    print("Survey columns:", sv.columns.tolist())

    # ── Chart 2a : GPA distribution ───────────────────────────────────────────
    gpa_col = next((c for c in sv.columns if "gpa" in c.lower()), None)
    if gpa_col:
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.hist(sv[gpa_col].dropna(), bins=20, color=GREEN, edgecolor="white", alpha=0.85)
        ax.axvline(sv[gpa_col].mean(), color=RED, linewidth=2, linestyle="--",
                   label=f"Mean: {sv[gpa_col].mean():.2f}")
        ax.axvline(sv[gpa_col].median(), color=ORANGE, linewidth=2, linestyle=":",
                   label=f"Median: {sv[gpa_col].median():.2f}")
        ax.set_xlabel("GPA")
        ax.set_ylabel("Frequency")
        ax.set_title("GPA Distribution — Clear Mountain State University Survey", fontsize=13, fontweight="bold")
        ax.legend()
        ax.spines[["top", "right"]].set_visible(False)
        plt.tight_layout()
        plt.savefig("images/05_gpa_distribution.png", dpi=150, bbox_inches="tight")
        plt.close()
        print("✓ Chart 2a saved")

    # ── Chart 2b : Gender or major breakdown (any categorical column) ─────────
    cat_cols = sv.select_dtypes(include=["object"]).columns.tolist()
    if cat_cols:
        col = cat_cols[0]
        counts = sv[col].value_counts()
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.bar(counts.index.astype(str), counts.values, color=BLUE, edgecolor="white")
        ax.set_ylabel("Count")
        ax.set_title(f"Distribution by {col}", fontsize=13, fontweight="bold")
        for i, v in enumerate(counts.values):
            ax.text(i, v + 0.3, str(v), ha="center", fontsize=10)
        ax.spines[["top", "right"]].set_visible(False)
        plt.tight_layout()
        plt.savefig("images/06_survey_categorical.png", dpi=150, bbox_inches="tight")
        plt.close()
        print("✓ Chart 2b saved")

    # ── Chart 2c : Confidence interval visualisation ──────────────────────────
    num_cols = sv.select_dtypes(include=[np.number]).columns.tolist()
    if num_cols:
        means, cis, labels = [], [], []
        for c in num_cols[:6]:
            d = sv[c].dropna()
            m = d.mean()
            se = stats.sem(d)
            ci = se * stats.t.ppf(0.975, df=len(d)-1)
            means.append(m)
            cis.append(ci)
            labels.append(c)
        fig, ax = plt.subplots(figsize=(9, 4))
        ax.barh(labels, means, xerr=cis, color=GREEN, alpha=0.7, edgecolor="white",
                error_kw=dict(ecolor=RED, linewidth=2, capsize=5))
        ax.set_xlabel("Mean Value")
        ax.set_title("95% Confidence Intervals — Survey Variables", fontsize=13, fontweight="bold")
        ax.spines[["top", "right"]].set_visible(False)
        plt.tight_layout()
        plt.savefig("images/07_confidence_intervals.png", dpi=150, bbox_inches="tight")
        plt.close()
        print("✓ Chart 2c saved")
except Exception as e:
    print(f"Survey chart error: {e}")

# ══════════════════════════════════════════════════════════════════════════════
# PROBLEM 3 — A & B SHINGLES MANUFACTURING QC
# ══════════════════════════════════════════════════════════════════════════════
try:
    sh = pd.read_csv("A & B shingles-1.csv")
    sh.columns = sh.columns.str.strip()
    print("Shingles columns:", sh.columns.tolist())

    a_col = next((c for c in sh.columns if "a" == c.lower().strip()), None) or sh.columns[0]
    b_col = next((c for c in sh.columns if "b" == c.lower().strip()), None) or sh.columns[1] if len(sh.columns) > 1 else None

    if a_col and b_col:
        A = sh[a_col].dropna()
        B = sh[b_col].dropna()

        # ── Chart 3a : Distribution comparison ───────────────────────────────
        fig, ax = plt.subplots(figsize=(9, 4))
        ax.hist(A, bins=20, alpha=0.6, color=BLUE, label=f"Shingle A (n={len(A)})", edgecolor="white")
        ax.hist(B, bins=20, alpha=0.6, color=ORANGE, label=f"Shingle B (n={len(B)})", edgecolor="white")
        ax.axvline(0.35, color=RED, linewidth=2, linestyle="--", label="Industry standard: 0.35")
        ax.set_xlabel("Moisture Content")
        ax.set_ylabel("Frequency")
        ax.set_title("Moisture Content Distribution — Shingle A vs B", fontsize=13, fontweight="bold")
        ax.legend()
        ax.spines[["top", "right"]].set_visible(False)
        plt.tight_layout()
        plt.savefig("images/08_shingles_distribution.png", dpi=150, bbox_inches="tight")
        plt.close()
        print("✓ Chart 3a saved")

        # ── Chart 3b : Box plot comparison ───────────────────────────────────
        fig, ax = plt.subplots(figsize=(6, 5))
        bp = ax.boxplot([A, B], patch_artist=True, labels=["Shingle A", "Shingle B"],
                        medianprops=dict(color=RED, linewidth=2))
        colors_b = [BLUE, ORANGE]
        for patch, col in zip(bp["boxes"], colors_b):
            patch.set_facecolor(col)
            patch.set_alpha(0.6)
        ax.axhline(0.35, color=RED, linewidth=1.5, linestyle="--", label="Standard: 0.35")
        ax.set_ylabel("Moisture Content")
        ax.set_title("Shingle A vs B — Moisture Content Comparison", fontsize=13, fontweight="bold")
        ax.legend()
        ax.spines[["top", "right"]].set_visible(False)
        plt.tight_layout()
        plt.savefig("images/09_shingles_boxplot.png", dpi=150, bbox_inches="tight")
        plt.close()
        print("✓ Chart 3b saved")

        # ── Print hypothesis test results ─────────────────────────────────────
        t_stat, p_val = stats.ttest_ind(A, B)
        print(f"\n── SHINGLES HYPOTHESIS TEST ──")
        print(f"Mean A: {A.mean():.4f}  |  Mean B: {B.mean():.4f}")
        print(f"Std  A: {A.std():.4f}   |  Std  B: {B.std():.4f}")
        print(f"t-statistic: {t_stat:.4f}  |  p-value: {p_val:.4f}")
        print(f"Conclusion: {'Reject H0 — means differ significantly' if p_val < 0.05 else 'Fail to reject H0 — no significant difference'} (α=0.05)")

        t_a, p_a = stats.ttest_1samp(A, 0.35)
        t_b, p_b = stats.ttest_1samp(B, 0.35)
        print(f"\nOne-sample t-test vs 0.35 standard:")
        print(f"Shingle A: t={t_a:.4f}, p={p_a:.4f} → {'exceeds standard' if p_a < 0.05 and A.mean() > 0.35 else 'meets standard'}")
        print(f"Shingle B: t={t_b:.4f}, p={p_b:.4f} → {'exceeds standard' if p_b < 0.05 and B.mean() > 0.35 else 'meets standard'}")
except Exception as e:
    print(f"Shingles chart error: {e}")

print("\n✅ All charts saved to /images folder.")
print("Update README findings table with the printed stats above.")
