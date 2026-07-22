# 79. Countries and States

> 难度与建议用时：Medium-1 20 mins

## Problem Statement

There is an array called `countries` that looks like this:

```javascript
countries = ["India", "USA",..]
```

There is an object called `states`

```javascript
states = {
  "India": [
              {"name": "Karnataka", "population": 200},
              {"name": "Maharashtra", "population": 130},
              {"name": "Goa", "population": 38},
              {"name": "Telangana", "population": 190},
              {"name": "Manipur", "population": 15}
           ],
  "USA": [
            {"name": "Michigan", "population": 120},
            {"name": "Virginia", "population": 48},
            {"name": "Maine", "population": 90},
            {"name": "Texas", "population": 15}
         ],
   ...
}
```

The variables `countries` and `states` are not accessible to you.

An **asynchronous** function `getCountry(countryIndex)` takes an integer as input and returns a Promise that, when resolved, returns the name of a country as a string. If `countryIndex >= countries.length`, the Promise is rejected with "Error"

Another **async** function `getStates(countryName)` takes a country name as input and returns a Promise that, when resolved, returns a list of states.

| Function Call        | On Settling                                                  | Data Type       |
| -------------------- | ------------------------------------------------------------ | --------------- |
| `getCountry(0)`      | Resolves to `"India"`                                        | String          |
| `getCountry(10000)`  | Rejected with `"Error"`                                      | String          |
| `getStates("India")` | Resolves to `[{"name": "Karnataka", "population": 200},...]` | List of objects |

### Task

Given a country index, you are required to return the name of the state with the largest population. If a country with that index doesn't exist, the function must return the string "ind = {index} invalid" where index is the input passed to the function.

### Example

| Input | Expected Output     |
| ----- | ------------------- |
| 0     | Karnataka           |
| 1     | Michigan            |
| 10000 | ind = 10000 invalid |

#### Explanation for Input 1 (`0`)

In the list of countries, `India` is the 0th-element. You can see that `Karnataka` has the highest population in this list of Indian states.

#### Explanation for Input 2 (`1`)

In the list of countries, `USA` is the 1st-element. You can see that `Michigan` has the highest population in this list of USA states.

## Input & Output

### Input Format

The input is a integer index.

### Output Format

The output must be the name of the most populated state of the country in that list.

## User Task

Your task is to complete the function `solution()`. Do not worry about reading input and printing output. The system does it automatically for you. Just complete the function and return the output.
