# 81. Salary Days Off

> 难度与建议用时：Medium-2 20 mins

data analysis

### Datasets

You are working with the employee data of different companies. Each company's dataset contains a list of employee details in the form of a dictionary. For example, one company's dataset may be of the form:

```python
[
    {'id': 1, 'salary': 3000, 'manager': False, 'num_days_off': 8},
    {'id': 2, 'salary': 5000, 'manager': True, 'num_days_off': 10},
    {'id': 3, 'salary': 6000, 'manager': True, 'num_days_off': 14}
]
```

The fields are self-explanatory. `num_days_off` tells you how many days they took off the previous year.

### Problem Statement

Given a dataset, you must calculate 2 values:

- The maximum salary in a given company
- The **total** number of days taken off by all the managers in a company

### Example

If the dataset consisted of only the three records shown above, the maximum salary would be `6000` and the total number of days off would be `24`.

### Requirement

Finish the function shown in the editor alongside. Replace the comment with your code. `dataset` is a list similar to the list shown in the example above.

Your code must set the values for `max_sal` and `total_num_days_off`.

#### Output

The output must be a tuple. The first variable must be the maximum salary and the next variable must be the total number of days off.

### Constraints

- Each employee entry will have all these 4 properties
- No value will be `None`

### Sample Inputs

If you click on the `Run Tests` button, your code will be run against the data from `dataset_1`. You can use this to see if your code is working fine. If you are confident that it is working fine, you can then submit the code.

**Note**: You cannot enter custom input for this question
