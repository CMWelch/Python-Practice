import numpy as np
import pandas as pd
desired_width=320

pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 15)
sal = pd.read_csv("Salaries.csv")

print(sal)
print(sal.head())
print(sal.info())

#Calculate Average Base Pay
mean = sal["BasePay"].mean()
print(mean)

#Find max over time pay
max_over = sal["OvertimePay"].max()
print(max_over)

#Find Joseph Driscoll's job title and pay
jd_title = sal[sal["EmployeeName"] == "JOSEPH DRISCOLL"]["JobTitle"]
print(jd_title)

jd_pay = sal[sal["EmployeeName"] == "JOSEPH DRISCOLL"]["TotalPayBenefits"]
print(jd_pay)

#Find highest payed employee
most_pay = sal[sal["TotalPayBenefits"] == sal["TotalPayBenefits"].max()]["EmployeeName"]
print(most_pay)

#Find lowest payed employee
least_pay = sal[sal["TotalPayBenefits"] == sal["TotalPayBenefits"].min()]["EmployeeName"]
print(least_pay)

#Average base pay of each year
mean_year = sal.groupby("Year")["BasePay"].mean()
print(mean_year)

#Number of unique jobs
num_jobs = sal["JobTitle"].nunique()
print(num_jobs)

#Top 5 jobs
pop_jobs = sal["JobTitle"].value_counts().head(5)
print(pop_jobs)

#Singular occurance job titles in 2013'
num_ujobs = sum(sal[sal["Year"] == 2013]["JobTitle"].value_counts() == 1)
print(num_ujobs)

#Number of people with Chief in their job title
def in_string(string):
    if "chief" in string.lower().split():
        return True
    else:
        return False

chief = sum(sal["JobTitle"].apply(lambda x: in_string(x)))
print(chief)

