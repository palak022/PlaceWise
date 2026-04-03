# PlaceWise: Smart Placement Analytics System

## Overview

PlaceWise is a data analytics project built to analyze student placement data and generate useful insights for colleges and placement cells.

The project uses:

* Python for data generation and cleaning
* SQL for data analysis
* Power BI for dashboard creation

This project helps answer questions like:

* How many students are placed?
* Which branch has the highest placement?
* Which companies hire the most students?
* Does internship experience affect placement?

---

## Technologies Used

* Python
* Pandas
* SQL
* Power BI
* CSV Dataset

---

## Project Structure

```text
PlaceWise/
│
├── generate_data.py
├── placement_data.csv
├── sql_queries.sql
├── dashboard.pbix
├── screenshots/
│   ├── dashboard.png
│   ├── placement_chart.png
│   └── internship_chart.png
└── README.md
```

---

## Dataset Columns

The dataset contains the following fields:

| Column Name      | Description                        |
| ---------------- | ---------------------------------- |
| student_id       | Unique ID of each student          |
| name             | Student name                       |
| branch           | Branch of student                  |
| cgpa             | Student CGPA                       |
| internship       | Number of internships              |
| projects         | Number of projects                 |
| company          | Company in which student is placed |
| package          | Salary package offered             |
| placement_status | Placed / Not Placed                |

---

## Python Work

Python was used to:

* Generate sample placement data
* Clean and organize the dataset
* Export the data into `placement_data.csv`

Example:

```python
import pandas as pd

file = pd.read_csv("placement_data.csv")
print(file.head())
```

---

## SQL Analysis

SQL was used to analyze the dataset.

### Total Students

```sql
SELECT COUNT(*) AS total_students
FROM placement_data;
```

### Placement Percentage

```sql
SELECT
ROUND(
    (SUM(CASE WHEN placement_status = 'Placed' THEN 1 ELSE 0 END) * 100.0)
    / COUNT(*), 2
) AS placement_percentage
FROM placement_data;
```

### Branch-wise Placement

```sql
SELECT branch, COUNT(*) AS placed_students
FROM placement_data
WHERE placement_status = 'Placed'
GROUP BY branch;
```

### Average Package by Branch

```sql
SELECT branch, ROUND(AVG(package),2) AS avg_package
FROM placement_data
WHERE placement_status = 'Placed'
GROUP BY branch;
```

---

## Power BI Dashboard

The dashboard contains:

### KPI Cards

* Total Students
* Placed Students
* Unplaced Students
* Placement Percentage
* Average Package

### Charts

* Placement Distribution Pie Chart
* Branch-wise Placement Chart
* Company-wise Hiring Chart
* Internship Status Pie Chart
* Average Package by Branch

### Filters / Slicers

* Branch
* Company

---

## Power BI DAX Formulas

### Total Students

```DAX
Total Students = COUNT(placement_data[student_id])
```

### Placed Students

```DAX
Placed Students =
CALCULATE(
    COUNT(placement_data[student_id]),
    placement_data[placement_status] = "Placed"
)
```

### Unplaced Students

```DAX
Unplaced Students =
CALCULATE(
    COUNT(placement_data[student_id]),
    placement_data[placement_status] = "Not Placed"
)
```

### Placement Percentage

```DAX
Placement % =
DIVIDE([Placed Students], [Total Students], 0) * 100
```

### Average Package

```DAX
Avg Package = AVERAGE(placement_data[package])
```

### Internship Status Column

```DAX
Internship Status =
IF(
    placement_data[internship] > 0,
    "Has Internship",
    "No Internship"
)
```

---

## Dashboard Insights

From the dashboard, we can understand:

* Total placement percentage of students
* Which branch performs better in placements
* Which companies hire more students
* Whether internship experience improves placement chances
* Average package offered to different branches

---

## Key Features

* Interactive Power BI dashboard
* SQL-based data analysis
* Internship and placement trend analysis
* Branch-wise and company-wise comparison
* Easy to understand visualizations

---

## Future Improvements

This project can be improved further by:

* Connecting Power BI directly with SQL database
* Using real college placement data
* Adding yearly placement comparison
* Creating a web application using Streamlit

---

## Dashboard Preview

![Dashboard](dashboard.png)

---

## Conclusion

PlaceWise is a complete placement analytics project that combines Python, SQL, and Power BI to generate useful placement insights. It is useful for students, placement cells, and colleges to understand placement trends and improve performance.

---

## Author

Palak Pardeshi
B.Tech IoT | Data Analytics & Java Enthusiast
