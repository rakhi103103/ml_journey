# Project 3: Corporate Salary Equity Audit
**Tool:** MySQL 8.0 | **Type:** SQL Portfolio Project

## Business Problem
HR executives need to verify that salary distributions are fair 
across departments, identify top earners, and flag missing or 
incomplete employee records before presenting to leadership.

## Dataset
Custom-built relational dataset with 2 tables:
- `employees` — 15 records (name, salary, dept_id, hire_date, job_title)
- `departments` — 5 departments (Engineering, Finance, Marketing, HR, Sales)

## SQL Concepts Demonstrated
| Concept | Used In |
|---|---|
| `RANK()` + `DENSE_RANK()` | Salary ranking within departments |
| `PARTITION BY` | Independent ranking per department |
| CTE (`WITH` clause) | Isolating top earner per department |
| `COALESCE` | Replacing NULL departments with readable labels |
| `CASE WHEN` | Segmenting employees into salary tiers |
| `LEFT JOIN` | Retaining unassigned contractor records |
| `GROUP BY` + `AVG` | Department-level salary benchmarks |

## Key Findings
- Engineering is the highest paying dept — avg ₹86,200
- HR is the lowest paying dept — avg ₹46,000
- Pay gap between highest and lowest dept: ₹40,200 (87% difference)
- Top earner: Dev Joshi (Engineering) at ₹1,02,000
- 1 contractor flagged with no department — cleaned using COALESCE
- Salary tier breakdown: 2 High / 8 Mid / 4 Low + 1 unassigned

## Files
- `salary_audit.sql` — all 7 queries with comments