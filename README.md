# 📊 Statistical & Probabilistic Analysis
### Wholesale Sales · University Survey · Manufacturing QC
**Python · SciPy · Pandas · Matplotlib · Seaborn · Hypothesis Testing**
*PG Program in Data Science & Business Analytics — McCombs School of Business, UT Austin*

---

## 📌 Project Overview

This project applies statistical and probabilistic reasoning to draw business inferences from **three real-world case studies**. Each case study moves through a full analytical cycle — descriptive statistics → probability distributions → estimation → hypothesis testing — culminating in data-backed business recommendations.

| Case Study | Domain | Core Technique |
|---|---|---|
| **Wholesale Customer Data** | Retail / Distribution | Descriptive Stats, EDA, Outlier Detection |
| **Clear Mountain State University Survey** | Higher Education | Probability Distributions, Confidence Intervals |
| **A & B Shingles — Manufacturing QC** | Manufacturing | Hypothesis Testing (t-test, equality of means) |

---

## 📂 Datasets

| File | Description |
|---|---|
| `Wholesale Customer.csv` | 440 retailers' annual spend across 6 product categories in 3 Portuguese regions (Lisbon, Oporto, Other) and 2 channels (Hotel/Restaurant, Retail) |
| `Survey-1.csv` | Student survey data from Clear Mountain State University — demographics, GPA, academic behaviour |
| `A & B shingles-1.csv` | Moisture content measurements from two shingle manufacturing batches (A and B) tested against industry standard |

---

## 🛠️ Tools & Techniques

- **Python** (Pandas, NumPy, SciPy, Matplotlib, Seaborn)
- Descriptive statistics: mean, median, std deviation, coefficient of variation
- Outlier detection via IQR and box plots
- Probability & probability distributions (normal distribution, z-scores)
- Confidence interval estimation (95% CI)
- Hypothesis testing: one-sample t-test, two-sample independent t-test
- Decision: reject / fail to reject null hypothesis at α = 0.05

---

## 🔍 Case Study 1 — Wholesale Customer Analysis

**Business Question:** Which region and channel drive the highest spend? Which product category is most volatile, and are there outliers affecting distribution strategy?

### Key Findings

| Insight | Finding |
|---|---|
| **Highest-spending region** | "Other" regions outspend Lisbon and Oporto across most categories |
| **Highest-spending channel** | Hotel/Restaurant/Cafe channel spends significantly more than Retail — driven by Fresh and Frozen |
| **Most variable product** | Delicassen showed the highest Coefficient of Variation — most inconsistent spending behaviour |
| **Most consistent product** | Detergents & Paper had the lowest CV — predictable demand |
| **Outliers** | Fresh and Milk categories contain significant upper-tail outliers, inflating means vs. medians |

### Visualisations

**Mean Spend by Region**
![Spend by Region](images/01_spend_by_region.png)

**Mean Spend by Channel**
![Spend by Channel](images/02_spend_by_channel.png)

**Product Variability (Coefficient of Variation)**
![Variability](images/03_variability_cv.png)

**Outlier Detection (Box Plots)**
![Outliers](images/04_boxplot_outliers.png)

---

## 🔍 Case Study 2 — University Survey Analysis

**Business Question:** What does the student population at Clear Mountain State University look like statistically? What can we infer about the broader student population from this sample?

### Key Findings

| Insight | Finding |
|---|---|
| **GPA distribution** | Approximately normal; mean GPA slightly right-skewed by high performers |
| **Confidence intervals** | 95% CI constructed for key continuous variables — GPA, spending, hours studied |
| **Probability application** | Normal distribution used to estimate the probability of a student falling within a GPA range |
| **Population inference** | Sample statistics used to make point and interval estimates for the full student population |

### Visualisations

**GPA Distribution**
![GPA Distribution](images/05_gpa_distribution.png)

**Categorical Breakdown**
![Survey Categorical](images/06_survey_categorical.png)

**95% Confidence Intervals — Key Variables**
![Confidence Intervals](images/07_confidence_intervals.png)

---

## 🔍 Case Study 3 — A & B Shingles Manufacturing QC

**Business Question:** Do Shingle A and Shingle B meet the industry moisture content standard of ≤ 0.35? Are the two batches statistically equivalent in quality?

### Hypotheses Tested

**Test 1 — Shingle A vs Industry Standard (0.35)**
- H₀: μ_A ≤ 0.35 (meets standard)
- H₁: μ_A > 0.35 (exceeds standard)

**Test 2 — Shingle B vs Industry Standard (0.35)**
- H₀: μ_B ≤ 0.35 (meets standard)
- H₁: μ_B > 0.35 (exceeds standard)

**Test 3 — Equality of Means (A vs B)**
- H₀: μ_A = μ_B (batches are statistically equal)
- H₁: μ_A ≠ μ_B (batches differ significantly)

> **Note:** Before running the equality of means test, the Levene test for equal variances was checked as a prerequisite assumption.

### Key Findings

| Test | Result |
|---|---|
| Shingle A vs 0.35 standard | Update after running `generate_charts_smdm.py` |
| Shingle B vs 0.35 standard | Update after running `generate_charts_smdm.py` |
| A vs B equality of means | Update after running `generate_charts_smdm.py` |

> Run `python generate_charts_smdm.py` — the script prints exact t-statistics, p-values, and conclusions to your terminal.

### Visualisations

**Moisture Content Distribution — A vs B**
![Shingles Distribution](images/08_shingles_distribution.png)

**Box Plot Comparison**
![Shingles Boxplot](images/09_shingles_boxplot.png)

---

## 📁 Repository Structure

```
📦 Statistical-Probabilistic-Analysis/
 ┣ 📓 SMDM-Mohammed Sultan Nazeer.ipynb         — Full analysis notebook
 ┣ 📄 SMDM Project - Mohammed Sultan Nazeer.pdf — Detailed written report
 ┣ 📄 Wholesale Customer.csv                    — Dataset 1
 ┣ 📄 Survey-1.csv                              — Dataset 2
 ┣ 📄 A & B shingles-1.csv                      — Dataset 3
 ┣ 🐍 generate_charts_smdm.py                   — Script to regenerate all charts
 ┣ 📁 images/                                   — Chart PNGs for this README
 ┗ 📄 README.md
```

---

## ▶️ How to Run

```bash
# 1. Clone the repo
git clone https://github.com/Mdsltn/Statistical-Probabilistic-Analysis-of-Store-Sales-University-Survey-Manufacturing-data.git
cd Statistical-Probabilistic-Analysis-of-Store-Sales-University-Survey-Manufacturing-data

# 2. Install dependencies
pip install pandas matplotlib seaborn numpy scipy

# 3. Open the notebook
jupyter notebook "SMDM-Mohammed Sultan Nazeer.ipynb"

# 4. Or regenerate charts + print hypothesis test results
python generate_charts_smdm.py
```

---

## 💡 Business Takeaways

- **For the wholesale distributor:** Focus inventory and logistics investment on the Hotel/Restaurant channel, particularly Fresh and Frozen categories. Delicassen demand is highly unpredictable — safety stock buffers are warranted.
- **For the university:** The survey data enables statistically valid inferences about the broader student population, supporting resource allocation decisions on student services.
- **For the manufacturer:** The hypothesis tests provide a rigorous, defensible quality verdict on each shingle batch — exactly the kind of evidence-based decision support that reduces recall and warranty risk.

---

## 👤 Author

**Mohammed Sultan**
Data Analyst | 11+ years Enterprise SaaS | Bengaluru, India
[LinkedIn](https://linkedin.com/in/mdsltn) · [GitHub](https://github.com/Mdsltn)

*Part of a data analytics portfolio built during the PG Program in Data Science & Business Analytics (McCombs School of Business, UT Austin)*
