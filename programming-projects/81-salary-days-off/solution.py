def solution(dataset):
    max_sal = max(employee["salary"] for employee in dataset)
    total_num_days_off = sum(
        employee["num_days_off"] for employee in dataset if employee["manager"]
    )
    return max_sal, total_num_days_off
