# 80. Countries and Capitals

> 难度与建议用时：Medium-2 20 mins

## Problem Statement

There is an array called `countries` that looks like this:

```javascript
countries = ["India", "USA", "countryA", ...]
```

There is an object called `capitals`

```javascript
capitals = {
  "India": "New Delhi", "USA": "Washington DC", "countryA": null
   ...
}
```

If a country doesn't have a capital, its value in the object above is `null`.

There is another object that maps capitals to their populations:

```javascript
const populations = {"New Delhi": 120, "Washington DC": 80}
```

The variables `countries`, `capitals` and `populations` are not accessible to you.

You are given three functions

| Function Name                           | Sync/Async | Returns                    |
| --------------------------------------- | ---------- | -------------------------- |
| `getCountry(countryInd)`                | Sync       | `countries[countryInd]`    |
| `getCapitalFromCountry(countryName)`    | Async      | `capitals[countryName]`    |
| `getPopulationFromCapital(capitalName)` | Sync       | `populations[capitalName]` |

If `countryInd >= countries.length`, `getCountry(countryInd)` returns a null value. If a country doesn't have a capital, `getCapitalFromCountry(countryName)` is rejected with a message "Error".

| Function Call                       | Output                    | Data Type   |
| ----------------------------------- | ------------------------- | ----------- |
| `getCountry(0)`                     | `"India"`                 | String      |
| `getCountry(10000)`                 | `null`                    | Null object |
| `getCapitalFromCountry("India")`    | Resolves to `"New Delhi"` | String      |
| `getCapitalFromCountry("countryA")` | Rejected with `"Error"`   | String      |

### Task

1. Complete the function `solution()`. `solution()` takes the country index as input and returns a string like "India, New Delhi, 120".
2. If the country index is greater than or equal to the length of `countries`, the output must be "No country found at ind = {index}" where index is the input to the function.
3. If the country doesn't have a capital (that is, its capital is null), the output must be "No capital found for country at ind = {index}" where index is the input to the function.

### Example

| Input | Expected Output                         |
| ----- | --------------------------------------- |
| 0     | India, New Delhi, 120                   |
| 1     | USA, Washington DC, 80                  |
| 2     | No capital found for country at ind = 2 |
| 10000 | No country found at ind = 10000         |

#### Explanation for Inputs 1 and 2 above (`0` and `1`)

You can clearly see these values from the `countries`, `capitals` and `populations` objects.

#### Explanation for Input 3 (`2`)

`countries[2] = "countryA"`. You can see from `capitals` that "countryA" doesn't have a capital

#### Explanation for Input 4 (`10000`)

`countries` doesn't have 9999 elements. So, `getCountry()` returns `null`.

## Input & Output

### Input Format

The input is an integer index.

### Output Format

The output must be a string.

## User Task

Your task is to complete the function `solution()`. Do not worry about reading input and printing output. The system does it automatically for you. Just complete the function and return the output.
