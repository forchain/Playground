# 1.Customer Orders In A Year -- Medium-1 15 mins

join

filter

# Database Schema

You have two database tables, `customers` and `orders`:

### Table: `customers`

- integer column `customer_id` (primary key)
- text column `customer_name`

### Table: `orders`

- integer column `order_id` (primary key)
- integer column `customer_id` (foreign key referencing `customers.customer_id`)
- integer column `order_total`
- date column `order_date`

# User Task

Write an SQL query to return the `customer_name` and `order_total` of all orders placed in the year 2023. **Do not use the YEAR function**

- Results should be sorted by `customer_name` in ascending order.
- If a customer has multiple orders in 2023, those orders should be listed with ascending `order_total`.

------

# Sample Testcases

## Sample Testcase 1

### Table Data

#### `customers`

| customer_id | customer_name |
| ----------- | ------------- |
| 1           | Alice Johnson |
| 2           | Eva Parker    |
| 3           | Carl Weber    |

#### `orders`

| order_id | customer_id | order_total | order_date |
| -------- | ----------- | ----------- | ---------- |
| 1        | 1           | 200         | 2023-03-10 |
| 2        | 1           | 400         | 2023-04-05 |
| 3        | 2           | 500         | 2022-12-15 |
| 4        | 2           | 300         | 2023-01-20 |
| 5        | 3           | 100         | 2023-07-01 |
| 6        | 3           | 100         | 2023-07-02 |

### Expected Output

```
Alice Johnson|200
Alice Johnson|400
Carl Weber|100
Carl Weber|100
Eva Parker|300
```

------

## Sample Testcase 2

### Table Data

#### `customers`

| customer_id | customer_name |
| ----------- | ------------- |
| 1           | Barry Ellis   |
| 2           | Chloe Evans   |
| 3           | Derek Stone   |

#### `orders`

| order_id | customer_id | order_total | order_date |
| -------- | ----------- | ----------- | ---------- |
| 1        | 1           | 600         | 2023-08-10 |
| 2        | 1           | 300         | 2023-08-11 |
| 3        | 2           | 200         | 2023-06-05 |
| 4        | 2           | 200         | 2023-06-06 |
| 5        | 3           | 400         | 2022-10-20 |
| 6        | 3           | 700         | 2023-02-15 |

### Expected Output

```
Barry Ellis|300
Barry Ellis|600
Chloe Evans|200
Chloe Evans|200
Derek Stone|700
```

AddPreview

# 2.Books Which Start With L -- Medium-1 15 mins

# Database Schema

You have a database with table `books` which has the following columns

- integer column `book_id` (primary key)
- text column book_name

# User Task

Your task is to return the names of books whose names start with L ordered by `book_id`.

# Testcases

## Sample Testcase 1

### Table data

| book_id | book_name                    |
| ------- | ---------------------------- |
| 1       | The Power of Now             |
| 2       | The Electronic Swagman       |
| 3       | Brutal Simplicity of thought |
| 4       | Life Lessons                 |

### Output

```
Life Lessons
```

## Sample Testcase 2

### Table data

| book_id | book_name              |
| ------- | ---------------------- |
| 1       | The Power of Now       |
| 2       | Lean In                |
| 3       | The Electronic Swagman |
| 4       | Leo Sign               |
| 5       | Life Lessons           |

### Output

```
Lean In
Leo Sign
Life Lessons
```

AddPreview

# 3.Books Issued To A User -- Medium-1 15 mins

# Database Schema

You have a database with tables

- `users`
- `books`
- `books_issued`

The `users` table has the following columns:

- integer column `user_id` (primary key)
- text column `name`
- text column `email`
- integer column `phone_number`

The `books` table has the following columns:

- integer column `book_id` (primary key)
- text column `book_name`

The `books_issued` table has the following columns:

- integer column `issue_id` (primary key)
- integer column `book_id` references the `book_id` column of the `books` table (foreign key)
- integer column `user_id` references the `user_id` column of the `users` table (foreign key)
- text column `return_status`
- date column `date_of_issue`

# User Task

Your task is to return the count of number of the books issued to user `Willian Mathew`

# Testcases

## Sample Testcase 1

### Table data

```
users
```

| user_id | name                | email                                             | phone_number |
| ------- | ------------------- | ------------------------------------------------- | ------------ |
| 1       | Alfreds Futterkiste | [alfreds@gmail.com](mailto:alfreds@gmail.com)     | 987654321    |
| 2       | Willian Mathew      | [william@gmail.com](mailto:william@gmail.com)     | 868686888    |
| 3       | David Smith         | [david@gmail.com](mailto:david@gmail.com)         | 798575757    |
| 4       | Alex hales          | [alexhales@gmail.com](mailto:alexhales@gmail.com) | 86888688     |
| 5       | Michael richard     | [michael@gmail.com](mailto:michael@gmail.com)     | 98765443     |

```
books
```

| book_id | book_name                    |
| ------- | ---------------------------- |
| 1       | The Power of Now             |
| 2       | Lean In                      |
| 3       | The Electronic Swagman       |
| 4       | Brutal Simplicity of thought |
| 5       | Life Lessons                 |

```
books_issued
```

| issue_id | book_id | user_id | return_status | date_of_return |
| -------- | ------- | ------- | ------------- | -------------- |
| 1        | 1       | 1       | Yes           | 2017-04-15     |
| 2        | 1       | 3       | No            | 2019-07-19     |
| 3        | 2       | 3       | No            | 2022-11-23     |
| 4        | 3       | 3       | Yes           | 2022-04-15     |
| 5        | 1       | 1       | Yes           | 2022-02-18     |

### Output

```
0
```

## Sample Testcase 2

### Table data

```
users
```

| user_id | name                | email                                             | phone_number |
| ------- | ------------------- | ------------------------------------------------- | ------------ |
| 1       | Alfreds Futterkiste | [alfreds@gmail.com](mailto:alfreds@gmail.com)     | 987654321    |
| 2       | Willian Mathew      | [william@gmail.com](mailto:william@gmail.com)     | 868686888    |
| 3       | David Smith         | [david@gmail.com](mailto:david@gmail.com)         | 798575757    |
| 4       | Alex hales          | [alexhales@gmail.com](mailto:alexhales@gmail.com) | 86888688     |
| 5       | Michael richard     | [michael@gmail.com](mailto:michael@gmail.com)     | 98765443     |

```
books
```

| book_id | book_name                    |
| ------- | ---------------------------- |
| 1       | The Power of Now             |
| 2       | Lean In                      |
| 3       | The Electronic Swagman       |
| 4       | Brutal Simplicity of thought |
| 5       | Life Lessons                 |

```
books_issued
```

| issue_id | book_id | user_id | return_status | date_of_return |
| -------- | ------- | ------- | ------------- | -------------- |
| 1        | 1       | 2       | Yes           | 2017-04-15     |
| 2        | 1       | 2       | No            | 2019-07-19     |
| 3        | 2       | 2       | No            | 2022-11-23     |
| 4        | 3       | 3       | Yes           | 2022-04-15     |
| 5        | 1       | 2       | Yes           | 2022-02-18     |

### Output

```
4
```

AddPreview

# 4.Account Holders With Credit Transactions -- Medium-1 15 mins

join

filter

# Database Schema

You have a database with tables

- `city`
- `accounts`
- `transactions`

The `city` table has the following columns:

- integer column `city_id` (primary key)
- text column `name`

The `accounts` table has the following columns:

- integer column `account_id` (primary key)
- text column `account_name`
- text column `account_type`
- integer column `city_id` references the `city_id` column of the `city` table (foreign key)

The `transactions` table has the following columns:

- integer column `transaction_id` (primary key)
- integer column `account_id` references the `account_id` column of the `accounts` table (foreign key)
- text column `transaction_type`
- text column `account_type`
- integer column `amount`
- date column `date`

# User Task

Your task is to return the name of all account holders having a `Savings` account, living in `New York` with more than `1` credit transaction ordered by `account_id`.

# Testcases

## Sample Testcase 1

### Table Data

```
city
```

| city_id | name        |
| ------- | ----------- |
| 1       | New York    |
| 2       | Los Angeles |
| 3       | Austin      |

```
accounts
```

| account_id | account_name | account_type | city_id |
| ---------- | ------------ | ------------ | ------- |
| 1          | Nathan       | Savings      | 1       |
| 2          | Maria        | Current      | 2       |
| 3          | Rachel       | Savings      | 1       |
| 4          | Rose         | Savings      | 3       |
| 5          | Roger        | Current      | 1       |

```
transactions
```

| transaction_id | account_id | transaction_type | amount | date       |
| -------------- | ---------- | ---------------- | ------ | ---------- |
| 1              | 1          | Credit           | 1000   | 2017-05-27 |
| 2              | 1          | Credit           | 200    | 2017-05-02 |
| 3              | 3          | Credit           | 1500   | 2017-05-27 |
| 4              | 2          | Savings          | 332    | 2017-02-23 |
| 5              | 3          | Credit           | 1700   | 2017-05-21 |

### Output

```
Nathan
Rachel
```

## Sample Testcase 2

### Table Data

```
city
```

| city_id | name     |
| ------- | -------- |
| 1       | New York |
| 2       | Dallas   |
| 3       | Houston  |

```
accounts
```

| account_id | account_name | account_type | city_id |
| ---------- | ------------ | ------------ | ------- |
| 1          | Nathan       | Savings      | 1       |
| 2          | Mira         | Current      | 2       |
| 3          | Rose         | Savings      | 1       |
| 4          | David        | Savings      | 3       |
| 5          | Roger        | Current      | 1       |

```
transactions
```

| transaction_id | account_id | transaction_type | amount | date       |
| -------------- | ---------- | ---------------- | ------ | ---------- |
| 1              | 1          | Credit           | 1000   | 2017-05-27 |
| 2              | 1          | Credit           | 200    | 2017-05-02 |
| 3              | 1          | Credit           | 1500   | 2017-05-27 |
| 4              | 2          | Savings          | 332    | 2017-02-23 |
| 5              | 3          | Credit           | 1700   | 2017-05-21 |

### Output

```
Nathan
```

AddPreview

# 5.Sum Of All Credit Transactions -- Medium-1 15 mins

filter

# Database Schema

You have a database with tables

- `city`
- `accounts`
- `transactions`

The `city` table has the following columns:

- integer column `city_id` (primary key)
- text column `name`

The `accounts` table has the following columns:

- integer column `account_id` (primary key)
- text column `account_name`
- text column `account_type`
- integer column `city_id` references the `city_id` column of the `city` table (foreign key)

The `transactions` table has the following columns:

- integer column `transaction_id` (primary key)
- integer column `account_id` references the `account_id` column of the `accounts` table (foreign key)
- text column `transaction_type`
- text column `account_type`
- integer column `amount`
- date column `date`

# User Task

Your task is to return the sum of all credit transactions on `27th May 2017`

# Testcases

## Sample Testcase 1

### Table data

```
city
```

| city_id | name     |
| ------- | -------- |
| 1       | New York |
| 2       | Paris    |
| 3       | Berlin   |

```
accounts
```

| account_id | account_name | account_type | city_id |
| ---------- | ------------ | ------------ | ------- |
| 1          | Jack         | Savings      | 1       |
| 2          | Alice        | Current      | 2       |
| 3          | Sweeney      | Savings      | 1       |
| 4          | David        | Savings      | 3       |
| 5          | Roger        | Current      | 1       |

```
transactions
```

| transaction_id | account_id | transaction_type | amount | date       |
| -------------- | ---------- | ---------------- | ------ | ---------- |
| 1              | 1          | Credit           | 1000   | 2017-05-27 |
| 2              | 1          | Credit           | 200    | 2017-05-27 |
| 3              | 3          | Credit           | 1500   | 2017-05-27 |
| 4              | 2          | Savings          | 332    | 2017-02-23 |
| 5              | 3          | Credit           | 1700   | 2017-05-21 |

### Output

```
2700
```

## Sample Testcase 2

### Table data

```
city
```

| city_id | name      |
| ------- | --------- |
| 1       | Tokyo     |
| 2       | New York  |
| 3       | Barcelona |

```
accounts
```

| account_id | account_name | account_type | city_id |
| ---------- | ------------ | ------------ | ------- |
| 1          | Nathan       | Savings      | 1       |
| 2          | Mira         | Current      | 2       |
| 3          | Katie        | Savings      | 1       |
| 4          | David        | Savings      | 3       |
| 5          | Roger        | Current      | 1       |

```
transactions
```

| transaction_id | account_id | transaction_type | amount | date       |
| -------------- | ---------- | ---------------- | ------ | ---------- |
| 1              | 1          | Credit           | 1000   | 2017-05-27 |
| 2              | 1          | Credit           | 200    | 2017-05-22 |
| 3              | 3          | Credit           | 1500   | 2017-05-23 |
| 4              | 2          | Savings          | 332    | 2017-02-23 |
| 5              | 3          | Credit           | 1700   | 2017-05-21 |

### Output

```
1000
```

AddPreview

# 6.Total Transaction Amounts Between Dates -- Medium-1 15 mins

aggregate

# Database Schema

You have a database with tables

- `city`
- `accounts`
- `transactions`

The `city` table has the following columns:

- integer column `city_id` (primary key)
- text column `name`

The `accounts` table has the following columns:

- integer column `account_id` (primary key)
- text column `account_name`
- text column `account_type`
- integer column `city_id` references the `city_id` column of the `city` table (foreign key)

The `transactions` table has the following columns:

- integer column `transaction_id` (primary key)
- integer column `account_id` references the `account_id` column of the `accounts` table (foreign key)
- text column `transaction_type`
- text column `account_type`
- integer column `amount`
- date column `date`

# User Task

Your task is to return the sum of amounts of transactions between made `1st May 2017` - `31st May 2017`

# Testcases

## Sample Testcase 1

### Table Data

```
city
```

| city_id | name      |
| ------- | --------- |
| 1       | New York  |
| 2       | New Delhi |
| 3       | Berlin    |

```
accounts
```

| account_id | account_name | account_type | city_id |
| ---------- | ------------ | ------------ | ------- |
| 1          | Nelson       | Savings      | 1       |
| 2          | Mohit        | Current      | 2       |
| 3          | Rachel       | Savings      | 1       |
| 4          | David        | Savings      | 3       |
| 5          | Roger        | Current      | 1       |

```
transactions
```

| transaction_id | account_id | transaction_type | amount | date       |
| -------------- | ---------- | ---------------- | ------ | ---------- |
| 1              | 1          | Credit           | 1000   | 2017-05-27 |
| 2              | 1          | Credit           | 200    | 2017-05-02 |
| 3              | 3          | Credit           | 1500   | 2017-05-27 |
| 4              | 2          | Savings          | 362    | 2017-05-27 |
| 5              | 3          | Credit           | 1700   | 2017-05-21 |

### Output

```
4762
```

## Sample Testcase 2

### Table Data

```
city
```

| city_id | name     |
| ------- | -------- |
| 1       | Berlin   |
| 2       | Helsinki |
| 3       | Paris    |

```
accounts
```

| account_id | account_name | account_type | city_id |
| ---------- | ------------ | ------------ | ------- |
| 1          | Roger        | Savings      | 1       |
| 2          | Rita         | Current      | 2       |
| 3          | Michael      | Savings      | 1       |
| 4          | David        | Savings      | 3       |
| 5          | Roger        | Current      | 1       |

```
transactions
```

| transaction_id | account_id | transaction_type | amount | date       |
| -------------- | ---------- | ---------------- | ------ | ---------- |
| 1              | 1          | Credit           | 1000   | 2017-05-27 |
| 2              | 1          | Credit           | 200    | 2017-01-02 |
| 3              | 3          | Credit           | 1500   | 2017-01-27 |
| 4              | 2          | Savings          | 362    | 2017-01-27 |
| 5              | 3          | Credit           | 1700   | 2017-05-21 |

### Output

```
2700
```

AddPreview

# 7.Book Titles And Author Names -- Medium-1 15 mins

ordering

# Database Schema

You have a database table `books` containing the following columns:

- integer column `id` (primary key)
- text column `title`
- text column `author`

# User Task

Your task is to write two separate queries to do the following:

1. Return a list of titles of all books, sorted alphabetically.
2. Return a list of all authors, sorted alphabetically.

# Testcases

## Sample Testcase 1

### Table data

```
books
```

| id   | title                                       | author              |
| ---- | ------------------------------------------- | ------------------- |
| 1    | Alice in Wonderland                         | Lewis Carroll       |
| 2    | Romeo and Juliet                            | William Shakespeare |
| 3    | The Emperor's New Mind                      | Roger Penrose       |
| 4    | The Extended Phenotype                      | Richard Dawkins     |
| 5    | Flatland: A Romance of Many Dimensions      | Edwin Abbott Abbott |
| 6    | Elements                                    | Euclid              |
| 7    | Philosophiæ Naturalis Principia Mathematica | Isaac Newton        |

### Output

```
Alice in Wonderland
Elements
Flatland: A Romance of Many Dimensions
Philosophiæ Naturalis Principia Mathematica
Romeo and Juliet
The Emperor's New Mind
The Extended Phenotype
Edwin Abbott Abbott
Euclid
Isaac Newton
Lewis Carroll
Richard Dawkins
Roger Penrose
William Shakespeare
```

## Sample Testcase 2

### Table data

```
books
```

| id   | title                 | author              |
| ---- | --------------------- | ------------------- |
| 1    | 1984                  | George Orwell       |
| 2    | Brave New World       | Aldous Huxley       |
| 3    | To Kill a Mockingbird | Harper Lee          |
| 4    | Moby-Dick             | Herman Melville     |
| 5    | Pride and Prejudice   | Jane Austen         |
| 6    | The Great Gatsby      | F. Scott Fitzgerald |
| 7    | War and Peace         | Leo Tolstoy         |

### Output

```
1984
Brave New World
Moby-Dick
Pride and Prejudice
The Great Gatsby
To Kill a Mockingbird
War and Peace
Aldous Huxley
F. Scott Fitzgerald
George Orwell
Harper Lee
Herman Melville
Jane Austen
Leo Tolstoy
```

AddPreview

# 8.Books Issued Between Dates -- Medium-1 15 mins

join

# Database Schema

You have a database with tables

- `users`
- `books`
- `books_issued`

The `users` table has the following columns:

- integer column `user_id` (primary key)
- text column `name`
- text column `email`
- integer column `phone_number`

The `books` table has the following columns:

- integer column `book_id` (primary key)
- text column `book_name`

The `books_issued` table has the following columns:

- integer column `issue_id` (primary key)
- integer column `book_id` references the `book_id` column of the `books` table (foreign key)
- integer column `user_id` references the `user_id` column of the `users` table (foreign key)
- text column `return_status`
- date column `date_of_issue`

# User Task

Your task is to return the distinct names of books ordered by book_id which were issued between `2017-02-01` to `2022-02-28`

# Testcases

## Sample Testcase 1

### Table data

```
users
```

| user_id | name                | email                                             | phone_number |
| ------- | ------------------- | ------------------------------------------------- | ------------ |
| 1       | Alfreds Futterkiste | [alfreds@gmail.com](mailto:alfreds@gmail.com)     | 987654321    |
| 2       | Willian Mathew      | [william@gmail.com](mailto:william@gmail.com)     | 868686888    |
| 3       | David Smith         | [david@gmail.com](mailto:david@gmail.com)         | 798575757    |
| 4       | Alex hales          | [alexhales@gmail.com](mailto:alexhales@gmail.com) | 86888688     |
| 5       | Michael richard     | [michael@gmail.com](mailto:michael@gmail.com)     | 98765443     |

```
books
```

| book_id | book_name                    |
| ------- | ---------------------------- |
| 1       | The Power of Now             |
| 2       | Lean In                      |
| 3       | The Electronic Swagman       |
| 4       | Brutal Simplicity of thought |
| 5       | Life Lessons                 |

```
books_issued
```

| issue_id | book_id | user_id | return_status | date_of_issue |
| -------- | ------- | ------- | ------------- | ------------- |
| 1        | 1       | 1       | Yes           | 2017-04-15    |
| 2        | 1       | 2       | No            | 2019-07-19    |
| 3        | 2       | 2       | No            | 2022-11-23    |
| 4        | 3       | 3       | Yes           | 2022-04-15    |
| 5        | 1       | 1       | Yes           | 2022-02-18    |

### Output

```
The Power of Now
Lean In
```

## Sample Testcase 2

### Table data

```
users
```

| user_id | name                | email                                             | phone_number |
| ------- | ------------------- | ------------------------------------------------- | ------------ |
| 1       | Alfreds Futterkiste | [alfreds@gmail.com](mailto:alfreds@gmail.com)     | 987654321    |
| 2       | Willian Mathew      | [william@gmail.com](mailto:william@gmail.com)     | 868686888    |
| 3       | David Smith         | [david@gmail.com](mailto:david@gmail.com)         | 798575757    |
| 4       | Alex hales          | [alexhales@gmail.com](mailto:alexhales@gmail.com) | 86888688     |
| 5       | Michael richard     | [michael@gmail.com](mailto:michael@gmail.com)     | 98765443     |

```
books
```

| book_id | book_name                    |
| ------- | ---------------------------- |
| 1       | The Power of Now             |
| 2       | Lean In                      |
| 3       | The Electronic Swagman       |
| 4       | Brutal Simplicity of thought |
| 5       | Life Lessons                 |

```
books_issued
```

| issue_id | book_id | user_id | return_status | date_of_issue |
| -------- | ------- | ------- | ------------- | ------------- |
| 1        | 1       | 1       | Yes           | 2022-04-15    |
| 2        | 1       | 2       | No            | 2022-07-19    |
| 3        | 2       | 2       | No            | 2022-11-23    |
| 4        | 3       | 3       | Yes           | 2022-04-15    |
| 5        | 1       | 1       | Yes           | 2022-02-18    |

### Output

```
The Power of Now
```

AddPreview

# 9.Post-2000 A-Ending Authors -- Medium-1 15 mins

join

filter

# Database Schema

You have two database tables, `authors` and `books`, with the following columns:

### Table: `authors`

- integer column `author_id` (primary key)
- text column `author_name` (name of the author)

### Table: `books`

- integer column `book_id` (primary key)
- integer column `author_id` (foreign key referencing `authors.author_id`)
- text column `title` (book title)
- integer column `year_published`

# User Task

Your task is to write a query that returns the titles of all books published after the year 2000, authored by writers whose names end with the letter `'a'`. The results should be sorted by the `author_name` in ascending order, and if multiple books are by the same author, sort those books by `title` in ascending order.

------

# Testcases

## Sample Testcase 1

### Table Data

#### `authors`

| author_id | author_name |
| --------- | ----------- |
| 1         | Emma        |
| 2         | Sophia      |
| 3         | Mark        |

#### `books`

| book_id | author_id | title                | year_published |
| ------- | --------- | -------------------- | -------------- |
| 1       | 1         | Life After Life      | 2013           |
| 2       | 1         | Under the Apple Tree | 1995           |
| 3       | 2         | Another Day          | 2001           |
| 4       | 3         | Z is for Zebra       | 2010           |

### Analysis

1. **Authors whose names end with 'a'**:
   - From the `authors` table, filter authors whose `author_name` ends with the letter `'a'`:
     - Emma (ID: 1), Sophia (ID: 2). Mark is excluded.
2. **Books published after the year 2000**:
   - From the `books` table, filter books where `year_published > 2000`:
     - `Life After Life (2013)`, `Another Day (2001)`, `Z is for Zebra (2010)`.
3. **Combine the two filters**:
   - Match the filtered authors with their books:
     - Emma: `Life After Life (2013)`
     - Sophia: `Another Day (2001)`
4. **Sorting**:
   - Sort results by `author_name` (ascending), then by `title` (ascending) for books by the same author:

### Expected Output

```
Life After Life 
Another Day
```

## Sample Testcase 2

### Table Data

#### `authors`

| author_id | author_name |
| --------- | ----------- |
| 1         | Elena       |
| 2         | Clara       |
| 3         | Anna        |

#### `books`

| book_id | author_id | title          | year_published |
| ------- | --------- | -------------- | -------------- |
| 1       | 1         | Zorro's Escape | 2002           |
| 2       | 1         | Aqua Blue      | 2010           |
| 3       | 2         | Mango Street   | 2005           |
| 4       | 2         | Yellow Moon    | 1999           |
| 5       | 3         | Alpha Beta     | 2021           |

### Analysis

1. **Authors whose names end with 'a'**:
   - From the `authors` table, filter authors whose `author_name` ends with the letter `'a'`:
     - Elena (ID: 1), Clara (ID: 2), Anna (ID: 3).
2. **Books published after the year 2000**:
   - From the `books` table, filter books where `year_published > 2000`:
     - `Zorro's Escape (2002)`, `Aqua Blue (2010)`, `Mango Street (2005)`, `Alpha Beta (2021)`.
3. **Combine the two filters**:
   - Match the filtered authors with their books:
     - Elena: `Zorro's Escape (2002)`, `Aqua Blue (2010)`
     - Clara: `Mango Street (2005)`
     - Anna: `Alpha Beta (2021)`
4. **Sorting**:
   - Sort results by `author_name` (ascending), then by `title` (ascending) for books by the same author.

### Expected Output

```
Alpha Beta 
Mango Street 
Aqua Blue 
Zorro's Escape
```

AddPreview

10.Books Issued With User Details -- Medium-1 15 mins

join

# Database Schema

You have a database with tables

- `users`
- `books`
- `books_issued`

The `users` table has the following columns:

- integer column `user_id` (primary key)
- text column `name`
- text column `email`
- integer column `phone_number`

The `books` table has the following columns:

- integer column `book_id` (primary key)
- text column `book_name`

The `books_issued` table has the following columns:

- integer column `issue_id` (primary key)
- integer column `book_id` references the `book_id` column of the `books` table (foreign key)
- integer column `user_id` references the `user_id` column of the `users` table (foreign key)
- text column `return_status`
- date column `date_of_issue`

# User Task

Your task is to return the list of issued book names along with the name of the user who has taken that book ordered by `user_id`

# Testcases

## Sample Testcase 1

### Table data

```
users
```

| user_id | name                | email                                             | phone_number |
| ------- | ------------------- | ------------------------------------------------- | ------------ |
| 1       | Alfreds Futterkiste | [alfreds@gmail.com](mailto:alfreds@gmail.com)     | 987654321    |
| 2       | Willian Mathew      | [william@gmail.com](mailto:william@gmail.com)     | 868686888    |
| 3       | David Smith         | [david@gmail.com](mailto:david@gmail.com)         | 798575757    |
| 4       | Alex hales          | [alexhales@gmail.com](mailto:alexhales@gmail.com) | 86888688     |
| 5       | Michael richard     | [michael@gmail.com](mailto:michael@gmail.com)     | 98765443     |

```
books
```

| book_id | book_name                    |
| ------- | ---------------------------- |
| 1       | The Power of Now             |
| 2       | Leo                          |
| 3       | The Electronic Swagman       |
| 4       | Brutal Simplicity of thought |
| 5       | Life Lessons                 |

```
books_issued
```

| issue_id | book_id | user_id | return_status | date_of_return |
| -------- | ------- | ------- | ------------- | -------------- |
| 1        | 1       | 1       | Yes           | 2017-04-15     |
| 2        | 1       | 2       | No            | 2019-07-19     |
| 3        | 2       | 2       | No            | 2022-11-23     |
| 4        | 3       | 3       | Yes           | 2022-04-15     |
| 5        | 1       | 1       | Yes           | 2022-02-18     |

### Output

```
The Power of Now|Alfreds Futterkiste
The Power of Now|Alfreds Futterkiste
The Power of Now|Willian Mathew
Leo|Willian Mathew
The Electronic Swagman|David Smith
```

## Sample Testcase 2

### Table data

```
users
```

| user_id | name                | email                                             | phone_number |
| ------- | ------------------- | ------------------------------------------------- | ------------ |
| 1       | Alfreds Futterkiste | [alfreds@gmail.com](mailto:alfreds@gmail.com)     | 987654321    |
| 2       | Willian Mathew      | [william@gmail.com](mailto:william@gmail.com)     | 868686888    |
| 3       | Michael             | [michael@gmail.com](mailto:michael@gmail.com)     | 798575757    |
| 4       | Alex hales          | [alexhales@gmail.com](mailto:alexhales@gmail.com) | 86888688     |
| 5       | Michael richard     | [michael@gmail.com](mailto:michael@gmail.com)     | 98765443     |

```
books
```

| book_id | book_name                    |
| ------- | ---------------------------- |
| 1       | The Power of Now             |
| 2       | Leo                          |
| 3       | The Electronic Swagman       |
| 4       | Brutal Simplicity of thought |
| 5       | Life Lessons                 |

```
books_issued
```

| issue_id | book_id | user_id | return_status | date_of_return |
| -------- | ------- | ------- | ------------- | -------------- |
| 1        | 1       | 1       | Yes           | 2017-04-15     |
| 2        | 1       | 2       | No            | 2019-07-19     |
| 3        | 2       | 2       | No            | 2022-11-23     |
| 4        | 3       | 3       | Yes           | 2022-04-15     |
| 5        | 1       | 1       | Yes           | 2022-02-18     |

### Output

```
The Power of Now|Alfreds Futterkiste
The Power of Now|Alfreds Futterkiste
The Power of Now|Willian Mathew
Leo|Willian Mathew
The Electronic Swagman|Michael
```

AddPreview

# 11.Books Never Issued -- Medium-2 15 mins

join

# Database Schema

You have a database with tables

- `users`
- `books`
- `books_issued`

The `users` table has the following columns:

- integer column `user_id` (primary key)
- text column `name`
- text column `email`
- integer column `phone_number`

The `books` table has the following columns:

- integer column `book_id` (primary key)
- text column `book_name`

The `books_issued` table has the following columns:

- integer column `issue_id` (primary key)
- integer column `book_id` references the `book_id` column of the `books` table (foreign key)
- integer column `user_id` references the `user_id` column of the `users` table (foreign key)
- text column `return_status`
- date column `date_of_issue`

# User Task

Your task is to return the names of books which were never issued, ordered by `book_id` .

# Testcases

## Sample Testcase 1

### Table data

```
users
```

| user_id | name                | email                                             | phone_number |
| ------- | ------------------- | ------------------------------------------------- | ------------ |
| 1       | Alfreds Futterkiste | [alfreds@gmail.com](mailto:alfreds@gmail.com)     | 987654321    |
| 2       | Willian Mathew      | [william@gmail.com](mailto:william@gmail.com)     | 868686888    |
| 3       | David Smith         | [david@gmail.com](mailto:david@gmail.com)         | 798575757    |
| 4       | Alex hales          | [alexhales@gmail.com](mailto:alexhales@gmail.com) | 86888688     |
| 5       | Michael richard     | [michael@gmail.com](mailto:michael@gmail.com)     | 98765443     |

```
books
```

| book_id | book_name              |
| ------- | ---------------------- |
| 1       | The Power of Now       |
| 2       | Lean In                |
| 3       | The Electronic Swagman |
| 4       | Life Lessons           |

```
books_issued
```

| issue_id | book_id | user_id | return_status | date_of_return |
| -------- | ------- | ------- | ------------- | -------------- |
| 1        | 1       | 1       | Yes           | 2017-04-15     |
| 2        | 1       | 2       | No            | 2019-07-19     |
| 3        | 2       | 2       | No            | 2022-11-23     |
| 4        | 3       | 3       | Yes           | 2022-04-15     |
| 5        | 1       | 1       | Yes           | 2022-02-18     |

### Output

```
Life Lessons
```

## Sample Testcase 2

### Table data

```
users
```

| user_id | name                | email                                             | phone_number |
| ------- | ------------------- | ------------------------------------------------- | ------------ |
| 1       | Alfreds Futterkiste | [alfreds@gmail.com](mailto:alfreds@gmail.com)     | 987654321    |
| 2       | Willian Mathew      | [william@gmail.com](mailto:william@gmail.com)     | 868686888    |
| 3       | David Smith         | [david@gmail.com](mailto:david@gmail.com)         | 798575757    |
| 4       | Alex hales          | [alexhales@gmail.com](mailto:alexhales@gmail.com) | 86888688     |
| 5       | Michael richard     | [michael@gmail.com](mailto:michael@gmail.com)     | 98765443     |

```
books
```

| book_id | book_name                    |
| ------- | ---------------------------- |
| 1       | The Power of Now             |
| 2       | Lean In                      |
| 3       | The Electronic Swagman       |
| 4       | Brutal Simplicity of thought |
| 5       | Life Lessons                 |

```
books_issued
```

| issue_id | book_id | user_id | return_status | date_of_return |
| -------- | ------- | ------- | ------------- | -------------- |
| 1        | 1       | 1       | Yes           | 2017-04-15     |
| 2        | 1       | 2       | No            | 2019-07-19     |
| 3        | 2       | 4       | No            | 2022-11-23     |
| 4        | 3       | 3       | Yes           | 2022-04-15     |
| 5        | 1       | 5       | Yes           | 2022-02-18     |

### Output

```

```

#### Explanation

All books were issued, so no results are returned

AddPreview

# 12.Maximum Orders -- Medium-2 15 mins

aggregation

join

# Database schema

You have a database, which contains two tables:

- `customers`
- `orders`

The `customers` table contains the following columns:

- integer column `id`
- text column `name`

The `orders` table contains the following columns:

- integer column `id`
- integer column `amount`
- integer column `customer_id` is a foreign key which references the `id` column of the `customers` table

# User Task

Your task is to find the name of the customer who has the maximum number of orders.

# Testcases

## Sample Testcase 1

### Table Data

```
customers
```

| id   | name            |
| ---- | --------------- |
| 1    | Lewis Carroll   |
| 2    | Isaac Newton    |
| 3    | Richard Dawkins |
| 4    | Roger Penrose   |
| 5    | Euclid          |

```
orders
```

| id   | amount | customer_id |
| ---- | ------ | ----------- |
| 1    | 200    | 1           |
| 2    | 450    | 3           |
| 3    | 375    | 1           |
| 4    | 200    | 2           |
| 5    | 375    | 2           |
| 6    | 500    | 2           |
| 7    | 650    | 3           |
| 8    | 1000   | 5           |
| 9    | 800    | 4           |
| 10   | 1000   | 4           |
| 11   | 375    | 2           |

------

### Output

```
Isaac Newton
```

### Explanation

Customer with id `2` has `4` orders which is the maximum. So, `Isaac Newton` is returned.

## Sample Testcase 2

### Table Data

```
customers
```

| id   | name            |
| ---- | --------------- |
| 1    | Lewis Carroll   |
| 2    | Isaac Newton    |
| 3    | Richard Dawkins |
| 4    | Roger Penrose   |
| 5    | Euclid          |

```
orders
```

| id   | amount | customer_id |
| ---- | ------ | ----------- |
| 1    | 200    | 3           |
| 2    | 450    | 3           |
| 3    | 375    | 1           |
| 4    | 200    | 3           |
| 5    | 375    | 2           |
| 6    | 500    | 3           |
| 7    | 650    | 3           |
| 8    | 1000   | 5           |
| 9    | 800    | 4           |
| 10   | 1000   | 4           |
| 11   | 375    | 2           |

------

### Output

```
Richard Dawkins
```

### Explanation

Customer with id `3` has `5` orders which is the maximum. So, `Richard Dawkins` is returned.

AddPreview

# 13.Students Enrolled in Courses -- Medium-2 20 mins

join

aggregation

# Database Schema

You have two tables: `students` and `courses`.

### Table: `students`

- integer column `student_id` (primary key)
- text column `student_name`
- integer column `age`

### Table: `courses`

- integer column `course_id` (primary key)
- integer column `student_id` (foreign key references `students(student_id)`)
- text column `course_name`
- integer column `grade`

------

# User Task

Write an SQL query to find the names of students who have enrolled in more than one course and have scored a grade of 80 or higher in all their courses.

- Sort the results by `student_name` in ascending order.

The output should have a single column:

- `student_name`

------

# Sample Testcases

## Sample Testcase 1

### Table Data

#### `students`

| student_id | student_name | age  |
| ---------- | ------------ | ---- |
| 1          | Alice        | 20   |
| 2          | Bob          | 22   |
| 3          | Carol        | 19   |

#### `courses`

| course_id | student_id | course_name | grade |
| --------- | ---------- | ----------- | ----- |
| 1         | 1          | Math        | 85    |
| 2         | 1          | Science     | 90    |
| 3         | 2          | Math        | 75    |
| 4         | 2          | Science     | 80    |
| 5         | 3          | History     | 88    |

### Analysis

- Alice has enrolled in two courses (Math and Science) and scored >= 80 in both.
- Bob has enrolled in two courses but scored < 80 in Math.
- Carol has only enrolled in one course.

**Expected Output**

```
Alice
```

------

## Sample Testcase 2

### Table Data

#### `students`

| student_id | student_name | age  |
| ---------- | ------------ | ---- |
| 1          | Dave         | 21   |
| 2          | Eve          | 23   |
| 3          | Frank        | 20   |

#### `courses`

| course_id | student_id | course_name | grade |
| --------- | ---------- | ----------- | ----- |
| 1         | 1          | English     | 95    |
| 2         | 1          | History     | 88    |
| 3         | 2          | English     | 70    |
| 4         | 3          | Math        | 85    |
| 5         | 3          | Science     | 90    |

### Analysis

- Dave has enrolled in two courses (English and History) and scored >= 80 in both.
- Eve has only enrolled in one course.
- Frank has enrolled in two courses (Math and Science) and scored >= 80 in both.

**Expected Output**

```
Dave 
Frank
```

AddPreview

# 14.Employees Earning More Than Manager -- Medium-2 20 mins

self-join

# Database Schema

You have a single table, `employees`:

### Table: `employees`

- integer column `emp_id` (primary key)
- text column `emp_name` (name of the employee)
- integer column `manager_id` (ID of the employee's manager; references `emp_id`)
- integer column `salary`

# User Task

Write an SQL query to return the names of employees who earn **more than their manager**.

- Sort the results by the employee's name in ascending order.

The output should have a single column:

- `emp_name`

------

# Sample Testcases

## Sample Testcase 1

### Table Data

#### `employees`

| emp_id | emp_name | manager_id | salary |
| ------ | -------- | ---------- | ------ |
| 1      | Alice    | NULL       | 50000  |
| 2      | Bob      | 1          | 60000  |
| 3      | Carol    | 1          | 45000  |
| 4      | David    | 2          | 70000  |
| 5      | Eve      | 2          | 55000  |

### Analysis

- Alice is a manager, but no one manages her (manager_id = NULL).
- Bob and Carol are managed by Alice:
  - Bob earns more (60000 > 50000).
  - Carol does not (45000 < 50000).
- David and Eve are managed by Bob:
  - David earns more (70000 > 60000).
  - Eve does not (55000 < 60000).

**Expected Output**

```
Bob 
David
```

## Sample Testcase 2

### Table Data

#### `employees`

| emp_id | emp_name | manager_id | salary |
| ------ | -------- | ---------- | ------ |
| 1      | Frank    | NULL       | 80000  |
| 2      | Grace    | 1          | 75000  |
| 3      | Heidi    | 1          | 85000  |
| 4      | Ivan     | 3          | 70000  |
| 5      | Judy     | 3          | 90000  |

### Analysis

- Frank is a manager, but no one manages him (manager_id = NULL).
- Grace and Heidi are managed by Frank:
  - Grace does not earn more (75000 < 80000).
  - Heidi earns more (85000 > 80000).
- Ivan and Judy are managed by Heidi:
  - Ivan does not earn more (70000 < 85000).
  - Judy earns more (90000 > 85000).

**Expected Output**

```
Heidi 
Judy
```

AddPreview

# 15.Social Media Query -- Medium-2 20 mins

join

subquery

# Database Schema

Consider a database schema for a social media platform with three tables:

- `users`
- `posts`
- `likes`

The `users` table has the following columns:

- integer column `user_id` (primary key)
- text column username

The `posts` table has the following columns:

- integer column `post_id` (primary key)
- integer column `user_id` references the `user_id` column of the `users` table (foreign key)
- text column `post_content`

The `likes` table has the following columns:

- integer column `like_id` (primary key)
- integer column `user_id` references the `user_id` column of the `users` table (foreign key)
- integer column `post_id` references the `post_id` column of the `posts` table (foreign key)

# User Task

Write an SQL query to find the users who have liked **all** the posts created by user with username `Harry` ordered by `user_id`

# Testcases

## Sample Testcase 1

### Table Data

```
users
```

| user_id | username |
| ------- | -------- |
| 1       | Harry    |
| 2       | George   |
| 3       | Charles  |
| 4       | Meghan   |
| 5       | Kate     |

```
posts
```

| post_id | user_id | post_content |
| ------- | ------- | ------------ |
| 1       | 1       | Post A       |
| 2       | 1       | Post B       |
| 3       | 2       | Post C       |
| 4       | 3       | Post D       |
| 5       | 3       | Post E       |

```
likes
```

| like_id | user_id | post_id |
| ------- | ------- | ------- |
| 1       | 2       | 1       |
| 2       | 3       | 1       |
| 3       | 4       | 1       |
| 4       | 2       | 2       |
| 5       | 3       | 2       |
| 6       | 4       | 2       |
| 7       | 1       | 3       |
| 8       | 3       | 3       |
| 9       | 4       | 3       |

### Output

```
George
Charles
Meghan
```

## Sample Testcase 2

### Table Data

```
users
```

| user_id | username |
| ------- | -------- |
| 1       | Harry    |
| 2       | George   |
| 3       | Charles  |
| 4       | Meghan   |
| 5       | Kate     |

```
posts
```

| post_id | user_id | post_content |
| ------- | ------- | ------------ |
| 1       | 1       | Post A       |
| 2       | 1       | Post B       |
| 3       | 2       | Post C       |
| 4       | 3       | Post D       |
| 5       | 3       | Post E       |

```
likes
```

| like_id | user_id | post_id |
| ------- | ------- | ------- |
| 1       | 5       | 1       |
| 2       | 3       | 1       |
| 3       | 4       | 1       |
| 4       | 5       | 2       |
| 5       | 3       | 2       |
| 6       | 4       | 2       |
| 7       | 2       | 2       |
| 8       | 3       | 3       |
| 9       | 4       | 3       |

### Output

```
Charles
Meghan
Kate
```

AddPreview

# 16.Regional Spending Analysis -- Hard-1 20 mins

join

aggregation

# Database Schema

You have two tables, `users` and `transactions`:

### Table: `users`

- integer column `user_id` (primary key)
- text column `user_name` (name of the user)
- text column `region` (region where the user is located)

### Table: `transactions`

- integer column `transaction_id` (primary key)
- integer column `user_id` (foreign key referencing `users.user_id`)
- integer column `amount` (amount of the transaction in dollars)
- date column `transaction_date` (date of the transaction)

------

# User Task

Write an SQL query to calculate the **cumulative spending per user** for each transaction they made, grouped by `region`.
For each region, output the user’s name (`user_name`), their total spending (`total_spending`), and the date of their last transaction (`last_transaction_date`).
Only include users who have spent more than $10,000 cumulatively.

Sort the results by `region` alphabetically, `total_spending` in descending order, and then by `last_transaction_date` in descending order.

The output should include the following columns:

- `region`
- `user_name`
- `total_spending`
- `last_transaction_date`

------

# Sample Testcases

## Sample Testcase 1

### Table Data

#### `users`

| user_id | user_name | region |
| ------- | --------- | ------ |
| 1       | Alice     | North  |
| 2       | Bob       | North  |
| 3       | Carol     | South  |
| 4       | Dave      | West   |

#### `transactions`

| transaction_id | user_id | amount | transaction_date |
| -------------- | ------- | ------ | ---------------- |
| 1              | 1       | 5000   | 2024-01-15       |
| 2              | 1       | 7000   | 2024-02-20       |
| 3              | 2       | 8000   | 2024-03-05       |
| 4              | 3       | 6000   | 2024-02-10       |
| 5              | 3       | 6000   | 2024-03-01       |
| 6              | 4       | 4000   | 2024-01-25       |

### Analysis

- Calculate cumulative spending for each user:
  - Alice: 5000 + 7000 = 12000 (meets the $10,000 threshold).
  - Bob: 8000 (does not meet the threshold).
  - Carol: 6000 + 6000 = 12000 (meets the threshold).
  - Dave: 4000 (does not meet the threshold).
- For the qualifying users:
  - Alice (North): Total spending = 12000, last transaction date = 2024-02-20.
  - Carol (South): Total spending = 12000, last transaction date = 2024-03-01.

**Expected Output**

```
North|Alice|12000|2024-02-20 
South|Carol|12000|2024-03-01
```

------

## Sample Testcase 2

### Table Data

#### `users`

| user_id | user_name | region |
| ------- | --------- | ------ |
| 1       | Frank     | East   |
| 2       | Grace     | West   |
| 3       | Heidi     | East   |
| 4       | Ivan      | West   |

#### `transactions`

| transaction_id | user_id | amount | transaction_date |
| -------------- | ------- | ------ | ---------------- |
| 1              | 1       | 7000   | 2024-01-10       |
| 2              | 1       | 4000   | 2024-02-05       |
| 3              | 2       | 3000   | 2024-03-15       |
| 4              | 2       | 4000   | 2024-04-10       |
| 5              | 3       | 2000   | 2024-02-12       |
| 6              | 4       | 10000  | 2024-01-25       |

### Analysis

- Calculate cumulative spending for each user:
  - Frank: 7000 + 4000 = 11000 (meets the $10,000 threshold).
  - Grace: 3000 + 4000 = 7000 (does not meet the threshold).
  - Heidi: 2000 (does not meet the threshold).
  - Ivan: 10000 (meets the $10,000 threshold).
- For the qualifying users:
  - Frank (East): Total spending = 11000, last transaction date = 2024-02-05.
  - Ivan (West): Total spending = 10000, last transaction date = 2024-01-25.

**Expected Output**

```
East|Frank|11000|2024-02-05 
West|Ivan|10000|2024-01-25
```

AddPreview

# 17.Departmental Overspending -- Hard-1 20 mins

aggregation

## Database Schema

You have two tables, `departments` and `expenses`:

### Table: `departments`

- integer column `dept_id` (primary key)
- text column `dept_name` (name of the department)
- integer column `annual_budget` (total annual budget for the department)

### Table: `expenses`

- integer column `expense_id` (primary key)
- integer column `dept_id` (foreign key referencing `departments.dept_id`)
- integer column `amount` (amount of the expense)
- date column `expense_date` (date the expense was recorded)

------

## User Task

Write an SQL query to find departments that have exceeded their annual budget.

For each department:

1. Calculate the **total expenses** incurred.
2. Determine how much they have **overspent** (`overspend = total_expenses - annual_budget`).

Only include departments where **total_expenses > annual_budget**.

Sort the results by:

- The **overspend** amount in descending order.
- The department name alphabetically in case of a tie.

The output should include:

- `dept_name`
- `total_expenses`
- `overspend`

------

## Sample Testcases

### Sample Testcase 1

#### Table Data

##### `departments`

| dept_id | dept_name | annual_budget |
| ------- | --------- | ------------- |
| 1       | HR        | 50000         |
| 2       | IT        | 80000         |
| 3       | Marketing | 60000         |

##### `expenses`

| expense_id | dept_id | amount | expense_date |
| ---------- | ------- | ------ | ------------ |
| 1          | 1       | 20000  | 2024-01-10   |
| 2          | 1       | 40000  | 2024-02-15   |
| 3          | 2       | 50000  | 2024-03-01   |
| 4          | 2       | 40000  | 2024-03-15   |
| 5          | 3       | 25000  | 2024-02-20   |
| 6          | 3       | 30000  | 2024-03-05   |

------

#### Analysis

1. **HR**:
   - Total expenses = `20000 + 40000 = 60000`.
   - Annual budget = `50000`.
   - Overspend = `60000 - 50000 = 10000`.
   - Total expenses exceed the annual budget → Include.
2. **IT**:
   - Total expenses = `50000 + 40000 = 90000`.
   - Annual budget = `80000`.
   - Overspend = `90000 - 80000 = 10000`.
   - Total expenses exceed the annual budget → Include.
3. **Marketing**:
   - Total expenses = `25000 + 30000 = 55000`.
   - Annual budget = `60000`.
   - Overspend = `55000 - 60000 = -5000`.
   - Total expenses do not exceed the annual budget → Exclude.

------

#### Expected Output

```
HR|60000|10000 
IT|90000|10000
```

------

### Sample Testcase 2

#### Table Data

##### `departments`

| dept_id | dept_name  | annual_budget |
| ------- | ---------- | ------------- |
| 1       | Marketing  | 60000         |
| 2       | Operations | 100000        |

##### `expenses`

| expense_id | dept_id | amount | expense_date |
| ---------- | ------- | ------ | ------------ |
| 1          | 1       | 25000  | 2024-02-10   |
| 2          | 1       | 40000  | 2024-03-01   |
| 3          | 2       | 50000  | 2024-01-15   |
| 4          | 2       | 60000  | 2024-02-20   |

------

#### Analysis

1. **Marketing**:
   - Total expenses = `25000 + 40000 = 65000`.
   - Annual budget = `60000`.
   - Overspend = `65000 - 60000 = 5000`.
   - Total expenses exceed the annual budget → Include.
2. **Operations**:
   - Total expenses = `50000 + 60000 = 110000`.
   - Annual budget = `100000`.
   - Overspend = `110000 - 100000 = 10000`.
   - Total expenses exceed the annual budget → Include.

------

#### Expected Output

```
Operations|110000|10000 
Marketing|65000|5000
```

AddPreview

# 18.Product Discount Analysis -- Hard-2 30 mins

CTE

join

aggregation

------

## Database Schema

### Table: `products`

- integer column `product_id` (primary key)
- text column `product_name` (name of the product)
- integer column `price` (price of the product)

### Table: `sales`

- integer column `sale_id` (primary key)
- integer column `product_id` (foreign key referencing `products.product_id`)
- integer column `quantity` (number of units sold)
- date column `sale_date` (date of the sale)

### Table: `discounts`

- integer column `discount_id` (primary key)
- integer column `product_id` (foreign key referencing `products.product_id`)
- integer column `discount_percentage` (discount percentage applied to the product)
- date column `start_date` (start date of the discount period)
- date column `end_date` (end date of the discount period)

------

## User Task

Write an SQL query to identify products that generated **total revenue greater than $50,000** during periods when discounts of **20% or more** were applied.

For these products, return:

1. `product_name` (name of the product)
2. `total_revenue` (total revenue during qualifying discount periods)

Sort the results by:

1. `total_revenue` in descending order.
2. `product_name` alphabetically in case of ties.

Note: Use `CAST(NUM) AS INTEGER` to convert a number to an integer.

------

## Sample Testcases

### Sample Testcase 1

#### Table Data

##### `products`

| product_id | product_name | price |
| ---------- | ------------ | ----- |
| 1          | Laptop       | 2000  |
| 2          | Smartphone   | 1000  |

##### `sales`

| sale_id | product_id | quantity | sale_date  |
| ------- | ---------- | -------- | ---------- |
| 1       | 1          | 30       | 2024-01-15 |
| 2       | 2          | 60       | 2024-01-20 |

##### `discounts`

| discount_id | product_id | discount_percentage | start_date | end_date   |
| ----------- | ---------- | ------------------- | ---------- | ---------- |
| 1           | 1          | 25                  | 2024-01-10 | 2024-01-30 |
| 2           | 2          | 20                  | 2024-01-15 | 2024-01-25 |

#### Analysis

- **Laptop**:
  - Sold 30 units during the discount period of 25% between `2024-01-10` and `2024-01-30`.
  - Revenue = 30 × (2000 × 0.75) = 45,000. **Does not qualify.**
- **Smartphone**:
  - Sold 60 units during the discount period of 20% between `2024-01-15` and `2024-01-25`.
  - Revenue = 60 × (1000 × 0.8) = 48,000. **Does not qualify.**

#### Expected Output

```

```

------

### Sample Testcase 2

#### Table Data

##### `products`

| product_id | product_name | price |
| ---------- | ------------ | ----- |
| 1          | TV           | 3000  |
| 2          | Refrigerator | 2000  |

##### `sales`

| sale_id | product_id | quantity | sale_date  |
| ------- | ---------- | -------- | ---------- |
| 1       | 1          | 25       | 2024-03-01 |
| 2       | 2          | 40       | 2024-03-10 |

##### `discounts`

| discount_id | product_id | discount_percentage | start_date | end_date   |
| ----------- | ---------- | ------------------- | ---------- | ---------- |
| 1           | 1          | 30                  | 2024-02-28 | 2024-03-10 |
| 2           | 2          | 20                  | 2024-03-05 | 2024-03-15 |

#### Analysis

- **TV**:
  - Sold 25 units during the discount period of 30% between `2024-02-28` and `2024-03-10`.
  - Revenue = 25 × (3000 × 0.7) = 52,500. **Qualifies.**
- **Refrigerator**:
  - Sold 40 units during the discount period of 20% between `2024-03-05` and `2024-03-15`.
  - Revenue = 40 × (2000 × 0.8) = 64,000. **Qualifies.**

#### Expected Output

```
Refrigerator|64000 
TV|52500
```

AddPreview

# 19.Departmental Expense Analysis -- Hard-2 30 mins

join

aggregation

## Database Schema

You have three tables, `departments`, `employees`, and `expenses`:

### Table: `departments`

- integer column `dept_id` (primary key)
- text column `dept_name` (name of the department)

### Table: `employees`

- integer column `emp_id` (primary key)
- integer column `dept_id` (foreign key referencing `departments.dept_id`)
- text column `emp_name` (name of the employee)

### Table: `expenses`

- integer column `expense_id` (primary key)
- integer column `emp_id` (foreign key referencing `employees.emp_id`)
- integer column `amount` (amount of the expense)
- date column `expense_date` (date of the expense)

------

## User Task

Write an SQL query to find the **total expenses for each department** along with the **highest individual expense** recorded by any employee in that department.

Include only departments where:

1. The total expenses exceed **$50,000**.
2. At least one employee in the department has recorded an individual expense of **$10,000 or more**.

For each department that meets the criteria, return:

- `dept_name` (name of the department)
- `total_expenses` (sum of all expenses in the department)
- `max_individual_expense` (highest expense by any single employee in the department)

Sort the results by `total_expenses` in descending order. In case of a tie, sort by `dept_name` alphabetically.

------

## Sample Testcases

### Sample Testcase 1

#### Table Data

##### `departments`

| dept_id | dept_name |
| ------- | --------- |
| 1       | HR        |
| 2       | IT        |

##### `employees`

| emp_id | dept_id | emp_name |
| ------ | ------- | -------- |
| 1      | 1       | Alice    |
| 2      | 1       | Bob      |
| 3      | 2       | Carol    |
| 4      | 2       | David    |

##### `expenses`

| expense_id | emp_id | amount | expense_date |
| ---------- | ------ | ------ | ------------ |
| 1          | 1      | 20000  | 2024-01-10   |
| 2          | 1      | 40000  | 2024-02-15   |
| 3          | 2      | 5000   | 2024-01-20   |
| 4          | 3      | 25000  | 2024-02-25   |
| 5          | 4      | 30000  | 2024-03-10   |

------

#### Analysis

1. **HR**:
   - Total expenses = `20000 + 40000 = 60000`.
   - Highest individual expense = `40000` (Alice).
   - **Qualifies** because:
     - Total expenses exceed $50,000.
     - At least one individual expense (Alice) is $10,000 or more.
2. **IT**:
   - Total expenses = `25000 + 30000 = 55000`.
   - Highest individual expense = `30000` (David).
   - **Qualifies** because:
     - Total expenses exceed $50,000.
     - At least one individual expense (David) is $10,000 or more.

------

#### Expected Output

```
HR|60000|40000 
IT|55000|30000
```

### Sample Testcase 2

#### Table Data

##### `departments`

| dept_id | dept_name  |
| ------- | ---------- |
| 1       | Marketing  |
| 2       | Operations |

##### `employees`

| emp_id | dept_id | emp_name |
| ------ | ------- | -------- |
| 1      | 1       | Frank    |
| 2      | 1       | Grace    |
| 3      | 2       | Heidi    |
| 4      | 2       | Ivan     |

##### `expenses`

| expense_id | emp_id | amount | expense_date |
| ---------- | ------ | ------ | ------------ |
| 1          | 1      | 30000  | 2024-02-10   |
| 2          | 1      | 30000  | 2024-02-15   |
| 3          | 3      | 20000  | 2024-01-20   |
| 4          | 4      | 10000  | 2024-03-10   |

------

#### Analysis

1. **Marketing**:
   - Total expenses = `30000 + 30000 = 60000`.
   - Highest individual expense = `30000` (Frank).
   - **Qualifies** because:
     - Total expenses exceed $50,000.
     - At least one individual expense (Frank) is $10,000 or more.
2. **Operations**:
   - Total expenses = `20000 + 10000 = 30000`.
   - Highest individual expense = `20000` (Heidi).
   - **Does not qualify** because:
     - Total expenses are less than $50,000.

------

#### Expected Output

```
Marketing|60000|30000
```

AddPreview

20.Employee Distribution by Salary Range -- Hard-2 20 mins

conditional aggregation

join

# Database Schema

You have two tables, `departments` and `employees`:

### Table: `departments`

- integer column `dept_id` (primary key)
- text column `dept_name` (name of the department)

### Table: `employees`

- integer column `emp_id` (primary key)
- text column `emp_name` (name of the employee)
- integer column `salary`
- integer column `dept_id` (foreign key referencing `departments.dept_id`)

# User Task

Write an SQL query to calculate the following for each department:

- The **total number of employees** in the department (`total_employees`).
- The **number of employees earning between 40000 and 60000 inclusive** (`mid_salary_employees`).
- The **number of employees earning more than 60000** (`high_salary_employees`).

Only include departments where there are at least **2 mid-salary or high-salary employees combined**.

Sort the results by `dept_name` alphabetically.

The output should have the following columns:

- `dept_name`
- `total_employees`
- `mid_salary_employees`
- `high_salary_employees`

------

# Sample Testcases

## Sample Testcase 1

### Table Data

#### `departments`

| dept_id | dept_name   |
| ------- | ----------- |
| 1       | Engineering |
| 2       | HR          |
| 3       | Marketing   |

#### `employees`

| emp_id | emp_name | salary | dept_id |
| ------ | -------- | ------ | ------- |
| 1      | Alice    | 60000  | 1       |
| 2      | Bob      | 55000  | 1       |
| 3      | Carol    | 40000  | 1       |
| 4      | David    | 45000  | 2       |
| 5      | Eve      | 50000  | 2       |
| 6      | Frank    | 48000  | 3       |
| 7      | Grace    | 52000  | 3       |

### Analysis

1. Engineering:

- Total Employees: 3 (Alice, Bob, Carol)
- Mid-Salary Employees (40000 to 60000): 3 (Alice, Bob, Carol)
- High-Salary Employees (> 60000): 0

Since mid_salary_employees + high_salary_employees = 2 >= 2, this department is included.

1. HR:

- Total Employees: 2 (David, Eve)
- Mid-Salary Employees (40000 to 60000): 2 (David, Eve)
- High-Salary Employees (> 60000): 0

Since mid_salary_employees + high_salary_employees = 2 >= 2, this department is included.

1. Marketing:

- Total Employees: 2 (Frank, Grace)
- Mid-Salary Employees (40000 to 60000): 1 (Frank)
- High-Salary Employees (> 60000): 0

Since mid_salary_employees + high_salary_employees = 1 < 2, this department is excluded.

### Expected Output

```
|Engineering|3|3|0|
|HR|2|2|0|
```

------

## Sample Testcase 2

### Table Data

#### `departments`

| dept_id | dept_name |
| ------- | --------- |
| 1       | Sales     |
| 2       | Support   |

#### `employees`

| emp_id | emp_name | salary | dept_id |
| ------ | -------- | ------ | ------- |
| 1      | John     | 75000  | 1       |
| 2      | Kelly    | 80000  | 1       |
| 3      | Liam     | 70000  | 1       |
| 4      | Morgan   | 50000  | 2       |
| 5      | Nina     | 45000  | 2       |

### Analysis

1. Sales:

- Total Employees: 3 (John, Kelly, Liam)
- Mid-Salary Employees (40000 to 60000): 0
- High-Salary Employees (> 60000): 3 (John, Kelly, Liam)

Since mid_salary_employees + high_salary_employees = 3 >= 2, this department is included.

1. Support:

- Total Employees: 2 (Morgan, Nina)
- Mid-Salary Employees (40000 to 60000): 2 (Morgan, Nina)
- High-Salary Employees (> 60000): 0

Since mid_salary_employees + high_salary_employees = 2 >= 2, this department is included.

### Expected Output

```
Sales|3|0|3|
Support|2|2|0|
```

AddPreview

# 21.Departmental Spending Breakdown -- Hard-2 30 mins

join

conditional aggregation

## Database Schema

You have two tables: `departments` and `expenses`.

### Table: `departments`

- integer column `dept_id` (primary key)
- text column `dept_name` (name of the department)

### Table: `expenses`

- integer column `expense_id` (primary key)
- integer column `dept_id` (foreign key referencing `departments.dept_id`)
- integer column `amount` (expense amount in dollars)
- text column `expense_type` (type of the expense, e.g., 'Travel', 'Supplies', 'Miscellaneous')

------

## User Task

Write an SQL query to find departments where:

1. **Travel expenses** account for at least **50% of departmental spending**.
2. The department has **at least 2 distinct expense types** (e.g., 'Travel' and 'Supplies').

For each qualifying department, return:

1. `dept_name`
2. `travel_expenses` (total amount spent on 'Travel' expenses)
3. `total_expenses` (total departmental spending)
4. `distinct_expense_types` (number of distinct expense types in the department)

Sort the results by:

1. `distinct_expense_types` in descending order.
2. `dept_name` alphabetically in case of ties.

------

## Sample Testcases

### Sample Testcase 1

#### Table Data

##### `departments`

| dept_id | dept_name |
| ------- | --------- |
| 1       | HR        |
| 2       | IT        |
| 3       | Finance   |

##### `expenses`

| expense_id | dept_id | amount | expense_type  |
| ---------- | ------- | ------ | ------------- |
| 1          | 1       | 5000   | Travel        |
| 2          | 1       | 2000   | Supplies      |
| 3          | 1       | 3000   | Miscellaneous |
| 4          | 2       | 10000  | Travel        |
| 5          | 2       | 8000   | Supplies      |
| 6          | 3       | 2000   | Travel        |
| 7          | 3       | 10000  | Supplies      |

#### Analysis

- **HR**:
  - Travel expenses = (5000).
  - Total expenses = (5000 + 2000 + 3000 = 10000).
  - Distinct expense types = (3).
  - Travel percentage = (5000 / 10000 = 50%). Qualifies.
- **IT**:
  - Travel expenses = (10000).
  - Total expenses = (10000 + 8000 = 18000).
  - Distinct expense types = (2).
  - Travel percentage = (10000 / 18000 ≈ 55.56%). Qualifies.
- **Finance**:
  - Travel expenses = (2000).
  - Total expenses = (2000 + 10000 = 12000).
  - Distinct expense types = (2).
  - Travel percentage = (2000 / 12000 ≈ 16.67%). Does not qualify.

#### Expected Output

```
HR|5000|10000|3 
IT|10000|18000|2
```

### Sample Testcase 2

#### Table Data

##### `departments`

| dept_id | dept_name  |
| ------- | ---------- |
| 1       | Logistics  |
| 2       | Marketing  |
| 3       | Operations |

##### `expenses`

| expense_id | dept_id | amount | expense_type  |
| ---------- | ------- | ------ | ------------- |
| 1          | 1       | 12000  | Travel        |
| 2          | 1       | 6000   | Miscellaneous |
| 3          | 2       | 15000  | Travel        |
| 4          | 2       | 10000  | Supplies      |
| 5          | 3       | 8000   | Travel        |
| 6          | 3       | 15000  | Supplies      |
| 7          | 3       | 7000   | Miscellaneous |

#### Analysis

- **Logistics**:
  - Travel expenses = (12000).
  - Total expenses = (12000 + 6000 = 18000).
  - Distinct expense types = (2).
  - Travel percentage = (12000 / 18000 = 66.67%). Qualifies.
- **Marketing**:
  - Travel expenses = (15000).
  - Total expenses = (15000 + 10000 = 25000).
  - Distinct expense types = (2).
  - Travel percentage = (15000 / 25000 = 60%). Qualifies.
- **Operations**:
  - Travel expenses = (8000).
  - Total expenses = (8000 + 15000 + 7000 = 30000).
  - Distinct expense types = (3).
  - Travel percentage = (8000 / 30000 ≈ 26.67%). Does not qualify.

#### Expected Output

```
Logistics|12000|18000|2 
Marketing|15000|25000|2
```

AddPreview

# 22.Products Above Average Revenue -- Hard-2 30 mins

join

aggregation

# Database Schema

You have two database tables, `orders` and `products`:

### Table: `orders`

- integer column `order_id` (primary key)
- integer column `product_id` (foreign key referencing `products.product_id`)
- integer column `quantity` (quantity of the product ordered)

### Table: `products`

- integer column `product_id` (primary key)
- text column `product_name`
- integer column `price` (price of the product)

# User Task

Write an SQL query to return the names of products that have been ordered for a **total revenue greater than the average revenue of all products**.

- Total revenue for a product is calculated as `SUM(quantity * price)` for all its orders.
- Sort the results by `product_name` in ascending order.

The output should have a single column:

- `product_name`

------

# Sample Testcases

## Sample Testcase 1

### Table Data

#### `orders`

| order_id | product_id | quantity |
| -------- | ---------- | -------- |
| 1        | 1          | 10       |
| 2        | 1          | 5        |
| 3        | 2          | 2        |
| 4        | 3          | 20       |
| 5        | 4          | 3        |

#### `products`

| product_id | product_name | price |
| ---------- | ------------ | ----- |
| 1          | Widget       | 100   |
| 2          | Gadget       | 200   |
| 3          | Thingamajig  | 50    |
| 4          | Doohickey    | 500   |

### Analysis

1. Calculate total revenue for each product:

- Widget: `(10 + 5) * 100 = 1500`
- Gadget: `2 * 200 = 400`
- Thingamajig: `20 * 50 = 1000`
- Doohickey: `3 * 500 = 1500`
- Average revenue: `(1500 + 400 + 1000 + 1500) / 4 = 1100`

1. Products with revenue > 1100:

- Widget (1500)
- Doohickey (1500)

1. Sort alphabetically:

- Doohickey
- Widget

### Expected Output

```
Doohickey
Widget
```

------

## Sample Testcase 2

### Table Data

#### `orders`

| order_id | product_id | quantity |
| -------- | ---------- | -------- |
| 1        | 1          | 10       |
| 2        | 1          | 5        |
| 3        | 2          | 2        |
| 4        | 2          | 10       |
| 5        | 3          | 5        |
| 6        | 3          | 3        |
| 7        | 4          | 7        |

#### `products`

| product_id | product_name | price |
| ---------- | ------------ | ----- |
| 1          | Widget       | 100   |
| 2          | Gadget       | 200   |
| 3          | Thingamajig  | 150   |
| 4          | Doohickey    | 300   |

### Analysis

1. **Calculate Total Revenue for Each Product:**
   - Widget:
     `Total Revenue = (10 + 5) * 100 = 1500`
   - Gadget:
     `Total Revenue = (2 + 10) * 200 = 2400`
   - Thingamajig:
     `Total Revenue = (5 + 3) * 150 = 1200`
   - Doohickey:
     `Total Revenue = 7 * 300 = 2100`
   - Average Revenue = (1500 + 2400 + 1200 + 2100) / 4 = 7200 / 4 = 1800
2. **Filter Products with Revenue Greater Than Average (1800):**

- Gadget
- Doohickey

1. Sort Alphabetically

- Doohickey
- Gadget

### Expected Output

```
Doohickey
Gadget 
```

AddPreview

# 23.Departmental Top Scorer -- Expert-1 40 mins

window function

ranking

partitioning

------

## Database Schema

You manage a database of employees and their performance metrics. The database consists of two tables: `employees` and `performance`.

### Table: `employees`

- integer column `emp_id` (primary key)
- text column `emp_name` (name of the employee)
- text column `department` (name of the employee's department)

### Table: `performance`

- integer column `record_id` (primary key)
- integer column `emp_id` (foreign key referencing `employees.emp_id`)
- integer column `score` (performance score, ranging from 1 to 100)
- integer column `hours_worked` (total hours worked by the employee in that record)

------

## User Task

Write an SQL query to find the **top-performing employee** in each department based on the following criteria:

1. Select the employee with the **highest total score** in each department.
2. If two or more employees have the same highest total score, choose the one who has worked the most total hours across all their performance records.
3. If there is still a tie, select the employee whose name comes first alphabetically.

The output should include:

- `department`
- `emp_name`
- `total_score`
- `total_hours`

### Constraints:

- Sort the results by `department` alphabetically.

------

## Sample Testcases

### Sample Testcase 1

#### Table Data

##### `employees`

| emp_id | emp_name | department  |
| ------ | -------- | ----------- |
| 1      | Alice    | Engineering |
| 2      | Bob      | Engineering |
| 3      | Cathy    | HR          |

##### `performance`

| record_id | emp_id | score | hours_worked |
| --------- | ------ | ----- | ------------ |
| 1         | 1      | 95    | 40           |
| 2         | 1      | 90    | 50           |
| 3         | 2      | 95    | 45           |
| 4         | 2      | 95    | 55           |
| 5         | 3      | 85    | 60           |
| 6         | 3      | 80    | 50           |

------

#### Expected Output:

```
Engineering|Bob|190|100 
HR|Cathy|165|110
```

------

### Sample Testcase 2

#### Table Data

##### `employees`

| emp_id | emp_name | department |
| ------ | -------- | ---------- |
| 1      | Ethan    | Sales      |
| 2      | Frank    | Sales      |
| 3      | Grace    | Marketing  |

##### `performance`

| record_id | emp_id | score | hours_worked |
| --------- | ------ | ----- | ------------ |
| 1         | 1      | 88    | 30           |
| 2         | 1      | 92    | 40           |
| 3         | 2      | 90    | 50           |
| 4         | 2      | 90    | 45           |
| 5         | 3      | 85    | 70           |
| 6         | 3      | 85    | 60           |

------

#### Expected Output:

```
Sales|Frank|180|95 
Marketing|Grace|170|130
```

AddPreview

# 24.Employee With Most Working Hours -- Expert-1 20 mins

ranking

window function

# Database Schema

You have two tables, `employees` and `projects`:

### Table: `employees`

- integer column `emp_id` (primary key)
- text column `emp_name` (name of the employee)
- text column `department` (department of the employee)

### Table: `projects`

- integer column `project_id` (primary key)
- integer column `emp_id` (foreign key referencing `employees.emp_id`)
- text column `project_name` (name of the project)
- integer column `hours_worked` (hours the employee worked on the project)
- date column `start_date` (start date of the project)

# User Task

Write an SQL query to find the **top 3 employees** who worked the **most total hours** across all their projects that started after Jan 1st, 2023

In the case of a tie in total hours worked, sort the employees:

1. First by the number of distinct projects they worked on (higher first).
2. Then alphabetically by their name.

The output should include the employee name (`emp_name`), their total hours worked (`total_hours`), and the number of distinct projects they contributed to (`project_count`).

The output should have three columns:

- `emp_name`
- `total_hours`
- `project_count`

------

# Sample Testcases

## Sample Testcase 1

### Table Data

#### `employees`

| emp_id | emp_name | department |
| ------ | -------- | ---------- |
| 1      | Alice    | HR         |
| 2      | Bob      | IT         |
| 3      | Carol    | Finance    |
| 4      | David    | IT         |

#### `projects`

| project_id | emp_id | project_name   | hours_worked | start_date |
| ---------- | ------ | -------------- | ------------ | ---------- |
| 1          | 1      | Recruitment    | 20           | 2023-01-15 |
| 2          | 1      | Training       | 30           | 2023-02-10 |
| 3          | 2      | DevOps         | 50           | 2023-03-20 |
| 4          | 3      | Auditing       | 25           | 2023-01-05 |
| 5          | 3      | Budgeting      | 30           | 2023-04-10 |
| 6          | 4      | Infrastructure | 40           | 2022-12-15 |

### Analysis

- Only projects starting after Jan 1st, 2023 are included. So, the valid projects are:
  - Alice: Recruitment (20) + Training (30) = 50 hours, 2 projects.
  - Bob: DevOps (50) = 50 hours, 1 project.
  - Carol: Auditing (25) + Budgeting (30) = 55 hours, 2 projects.
  - David: No projects qualify (start date is outside range).

**Expected Output**

```
Carol|55|2 
Alice|50|2 
Bob |50|1
```

------

## Sample Testcase 2

### Table Data

#### `employees`

| emp_id | emp_name | department |
| ------ | -------- | ---------- |
| 1      | Frank    | Sales      |
| 2      | Grace    | IT         |
| 3      | Heidi    | Finance    |
| 4      | Ivan     | Marketing  |
| 5      | Judy     | Sales      |

#### `projects`

| project_id | emp_id | project_name | hours_worked | start_date |
| ---------- | ------ | ------------ | ------------ | ---------- |
| 1          | 1      | SalesPitch   | 60           | 2023-11-01 |
| 2          | 2      | ServerSetup  | 45           | 2023-10-10 |
| 3          | 3      | Auditing     | 50           | 2023-08-20 |
| 4          | 4      | Campaigns    | 30           | 2022-11-05 |
| 5          | 5      | ColdCalling  | 40           | 2023-09-15 |
| 6          | 5      | Outreach     | 30           | 2023-12-01 |

### Analysis

- Only projects starting after Jan 1st, 2023 are included.
  - Frank: SalesPitch (60) = 60 hours, 1 project.
  - Grace: ServerSetup (45) = 45 hours, 1 project.
  - Heidi: Auditing (50) = 50 hours, 1 project.
  - Ivan: No projects qualify (start date is outside range).
  - Judy: ColdCalling (40) + Outreach (30) = 70 hours, 2 projects.

**Expected Output**

```
Judy|70|2 
Frank|60|1 
Heidi|50|1
```

AddPreview

# 25.Department Max Salaries -- Expert-1 30 mins

CTE

aggregation

# Database Schema

You have two database tables, `departments` and `employees`:

### Table: `departments`

- integer column `dept_id` (primary key)
- text column `dept_name`

### Table: `employees`

- integer column `emp_id` (primary key)
- text column `emp_name`
- integer column `salary`
- integer column `dept_id` (foreign key referencing `departments.dept_id`)

# User Task

Write an SQL query that returns each department's name and the **maximum salary** of its employees who earn more than 50000.

- Only include departments where at least two employees meet this salary condition.
- Sort the results by the maximum salary in ascending order.

------

# Sample Testcases

## Sample Testcase 1

### Table Data

#### `departments`

| dept_id | dept_name   |
| ------- | ----------- |
| 1       | Marketing   |
| 2       | Engineering |
| 3       | Finance     |

#### `employees`

| emp_id | emp_name      | salary | dept_id |
| ------ | ------------- | ------ | ------- |
| 1      | Alice Johnson | 60000  | 1       |
| 2      | Bob Williams  | 70000  | 1       |
| 3      | Carol Smith   | 52000  | 2       |
| 4      | David Andrews | 48000  | 2       |
| 5      | Ellen Reeves  | 75000  | 3       |
| 6      | Frank Nelson  | 76000  | 3       |
| 7      | Gary Thompson | 55000  | 3       |

### Analysis

- Marketing: Alice(60000), Bob(70000) both >50000. Max salary = 70000
- Engineering: Carol(52000 >50000), David(48000 ≤50000), only one qualifies → exclude
- Finance: Ellen(75000), Frank(76000), Gary(55000) all >50000. Max salary = 76000

Include departments with ≥2 employees >50000: Marketing (max=70000), Finance (max=76000)

Sort by max salary ascending.

### Expected Output

```
Marketing|70000 
Finance|76000
```

------

## Sample Testcase 2

### Table Data

#### `departments`

| dept_id | dept_name  |
| ------- | ---------- |
| 1       | HR         |
| 2       | Operations |
| 3       | Design     |

#### `employees`

| emp_id | emp_name      | salary | dept_id |
| ------ | ------------- | ------ | ------- |
| 1      | Hannah Clark  | 51000  | 1       |
| 2      | Ian Davis     | 52000  | 1       |
| 3      | Jack Erickson | 80000  | 2       |
| 4      | Laura Foster  | 82000  | 2       |
| 5      | Mona Gray     | 49000  | 2       |
| 6      | Nick Howard   | 53000  | 3       |

### Analysis

- HR: Hannah(51000), Ian(52000) both >50000. Max = 52000
- Operations: Jack(80000), Laura(82000) >50000, Mona(49000 ≤50000 excluded). Max = 82000
- Design: Nick(53000) only one >50000 → exclude

Include: HR(max=52000), Operations(max=82000)

Sort ascending by max salary.

### Expected Output

```
HR|52000 
Operations|82000
```

AddPreview

# 26.Top 3 Customers (with ties) -- Expert-1 30 mins

aggregation

ranking

# Database Schema

You have a single table, `orders`:

### Table: `orders`

- integer column `order_id` (primary key)
- integer column `customer_id` (ID of the customer who placed the order)
- date column `order_date` (date when the order was placed)
- integer column `order_amount` (amount of the order in dollars)

# User Task

Write an SQL query to find the **top 3 customers** who have spent the highest total amount across all their orders, along with the total amount spent. If there is a tie for the third position, include all customers who tied.

- Sort the results by the `total_amount` in descending order. In case of a tie, sort by `customer_id` in ascending order.

The output should have the following columns:

- `customer_id`
- `total_amount`

------

# Sample Testcases

## Sample Testcase 1

### Table Data

#### `orders`

| order_id | customer_id | order_date | order_amount |
| -------- | ----------- | ---------- | ------------ |
| 1        | 101         | 2024-01-01 | 300          |
| 2        | 102         | 2024-01-02 | 200          |
| 3        | 101         | 2024-01-03 | 150          |
| 4        | 103         | 2024-01-04 | 400          |
| 5        | 104         | 2024-01-05 | 100          |
| 6        | 103         | 2024-01-06 | 300          |

### Analysis

- Customer 101: 300 + 150 = 450
- Customer 102: 200
- Customer 103: 400 + 300 = 700
- Customer 104: 100

Top 3 customers by total amount are:

- 103 (700)
- 101 (450)
- 102 (200)

**Expected Output**

```
103|700 
101|450 
102|200
```

## Sample Testcase 2

### Table Data

#### `orders`

| order_id | customer_id | order_date | order_amount |
| -------- | ----------- | ---------- | ------------ |
| 1        | 201         | 2024-01-01 | 500          |
| 2        | 202         | 2024-01-02 | 300          |
| 3        | 203         | 2024-01-03 | 300          |
| 4        | 204         | 2024-01-04 | 200          |
| 5        | 205         | 2024-01-05 | 300          |
| 6        | 202         | 2024-01-06 | 200          |

### Analysis

- Customer 201: 500
- Customer 202: 300 + 200 = 500
- Customer 203: 300
- Customer 204: 200
- Customer 205: 300

Top 3 customers by total amount are:

- 201 (500)
- 202 (500)
- 203 (300)
- 205 (300)

**Expected Output**

```
201|500 
202|500 
203|300
205|300
```

AddPreview

# 27.Top Performers by Department -- Expert-1 30 mins

window function

ranking

partitioning

# Database Schema

You have two database tables, `departments` and `employees`:

### Table: `departments`

- integer column `dept_id` (primary key)
- text column `dept_name` (name of the department)

### Table: `employees`

- integer column `emp_id` (primary key)
- text column `emp_name` (name of the employee)
- integer column `dept_id` (foreign key referencing `departments.dept_id`)
- integer column `performance_score` (employee's performance score)

# User Task

Write an SQL query to find the **top two performers** from each department based on their `performance_score`.

- If there is a tie in `performance_score`, sort the results by `emp_name` alphabetically.
- Include the department name, employee name, and their performance score in the result.

The output should have the following columns:

- `dept_name`
- `emp_name`
- `performance_score`

Sort the results by `dept_name` alphabetically and, within each department, by `performance_score` in descending order, then by `emp_name` alphabetically.

------

# Sample Testcases

## Sample Testcase 1

### Table Data

#### `departments`

| dept_id | dept_name   |
| ------- | ----------- |
| 1       | Engineering |
| 2       | HR          |
| 3       | Marketing   |

#### `employees`

| emp_id | emp_name | dept_id | performance_score |
| ------ | -------- | ------- | ----------------- |
| 1      | Alice    | 1       | 85                |
| 2      | Bob      | 1       | 92                |
| 3      | Carol    | 1       | 85                |
| 4      | David    | 2       | 88                |
| 5      | Eve      | 2       | 80                |
| 6      | Frank    | 2       | 88                |
| 7      | Grace    | 3       | 90                |
| 8      | Hannah   | 3       | 85                |
| 9      | Ian      | 3       | 75                |

### Analysis

1. **Engineering Department**:
   - Employees: Bob (92), Alice (85)
   - Sorted by `performance_score` descending: Bob (92), Alice (85)
   - Top 2 Performers: Bob (92), Alice (85)
2. **HR Department**:
   - Employees: David (88), Frank (88)
   - Sorted by `performance_score` descending: David (88), Frank (88)
   - Since their `performance_score` is tied, they are sorted alphabetically by `emp_name`.
   - Top 2 Performers: David (88), Frank (88)
3. **Marketing Department**:
   - Employees: Grace (90), Hannah (85)
   - Sorted by `performance_score` descending: Grace (90), Hannah (85)
   - Top 2 Performers: Grace (90), Hannah (85)

------

### Expected Output

```
Engineering|Bob|92 
Engineering|Alice|85 
HR|David|88 
HR|Frank|88 
Marketing|Grace|90 
Marketing|Hannah|85
```

------

## Sample Testcase 2

### Table Data

#### `departments`

| dept_id | dept_name |
| ------- | --------- |
| 1       | Sales     |
| 2       | Support   |

#### `employees`

| emp_id | emp_name | dept_id | performance_score |
| ------ | -------- | ------- | ----------------- |
| 1      | John     | 1       | 95                |
| 2      | Kelly    | 1       | 80                |
| 3      | Liam     | 1       | 95                |
| 4      | Morgan   | 2       | 87                |
| 5      | Nina     | 2       | 87                |
| 6      | Oliver   | 2       | 85                |

### Analysis

1. **Sales Department**:
   - Employees: John (95), Liam (95)
   - Sorted by `performance_score` descending: John (95), Liam (95)
   - Since their `performance_score` is tied, they are sorted alphabetically by `emp_name`.
   - Top 2 Performers: John (95), Liam (95)
2. **Support Department**:
   - Employees: Morgan (87), Nina (87)
   - Sorted by `performance_score` descending: Morgan (87), Nina (87)
   - Since their `performance_score` is tied, they are sorted alphabetically by `emp_name`.
   - Top 2 Performers: Morgan (87), Nina (87)

------

### Expected Output

```
Sales|John|95 
Sales|Liam|95 
Support|Morgan|87 
Support|Nina|87
```

AddPreview

# 28.Store Sales Leaderboard -- Expert-2 30 mins

window function

ranking

partitioning

## Database Schema

You manage a sales system with two tables: `stores` and `sales`.

### Table: `stores`

- integer column `store_id` (primary key)
- text column `store_name` (name of the store)
- text column `region` (region of the store)

### Table: `sales`

- integer column `sale_id` (primary key)
- integer column `store_id` (foreign key referencing `stores.store_id`)
- integer column `amount` (amount of the sale in dollars)

------

## User Task

Write an SQL query to calculate a **regional sales leaderboard** for all stores. For each store in every region:

1. Assign a **rank** to each store based on their total sales within the region (highest to lowest). If two stores have the same total sales, rank them alphabetically by their name.
2. Calculate the **cumulative sales** for each region, up to the current store's rank.
3. Include only stores where the **total sales** are greater than `5000`.

The output should include:

- `region`
- `store_name`
- `rank`
- `total_sales`
- `cumulative_sales`

### Constraints:

- Sort the output by `region` alphabetically, then by `rank` in ascending order.

------

## Sample Testcases

### Sample Testcase 1

#### Table Data

##### `stores`

| store_id | store_name   | region |
| -------- | ------------ | ------ |
| 1        | Alpha Mart   | North  |
| 2        | Beta Bazaar  | North  |
| 3        | Gamma Goods  | North  |
| 4        | Delta Deals  | South  |
| 5        | Omega Outlet | South  |

##### `sales`

| sale_id | store_id | amount |
| ------- | -------- | ------ |
| 1       | 1        | 3000   |
| 2       | 1        | 4000   |
| 3       | 2        | 2000   |
| 4       | 2        | 6000   |
| 5       | 3        | 8000   |
| 6       | 4        | 7000   |
| 7       | 5        | 2000   |
| 8       | 5        | 5000   |

------

#### Analysis:

1. **North Region**:
   - Alpha Mart: Total Sales = (3000 + 4000 = 7000).
   - Beta Bazaar: Total Sales = (2000 + 6000 = 8000).
   - Gamma Goods: Total Sales = (8000).
   - **Rank**:
     - Beta Bazaar: Rank = 1. (Rank 1 because it is sorted by store_name)
     - Gamma Goods: Rank = 2.
     - Alpha Mart: Rank = 3.
   - **Cumulative Sales**:
     - Beta Bazaar: Cumulative Sales = (8000).
     - Gamma Goods: Cumulative Sales = (8000 + 8000 = 16000).
     - Alpha Mart: Cumulative Sales = (16000 + 7000 = 23000).
2. **South Region**:
   - Delta Deals: Total Sales = (7000).
   - Omega Outlet: Total Sales = (2000 + 5000 = 7000).
   - **Rank**:
     - Delta Deals: Rank = 1 (alphabetical tiebreaker).
     - Omega Outlet: Rank = 2.
   - **Cumulative Sales**:
     - Delta Deals: Cumulative Sales = (7000).
     - Omega Outlet: Cumulative Sales = (7000 + 7000 = 14000).

------

#### Expected Output:

```
North|Beta Bazaar|1|8000|8000 
North|Gamma Goods|2|8000|16000 
North Alpha|Mart|3|7000|23000 
South|Delta Deals|1|7000|7000
South|Omega Outlet|2|7000|14000
```

### Sample Testcase 2

#### Table Data

##### `stores`

| store_id | store_name | region |
| -------- | ---------- | ------ |
| 1        | A-Mart     | East   |
| 2        | B-Store    | East   |
| 3        | C-Shop     | West   |
| 4        | D-Depot    | West   |
| 5        | E-Hub      | West   |

##### `sales`

| sale_id | store_id | amount |
| ------- | -------- | ------ |
| 1       | 1        | 6000   |
| 2       | 1        | 5000   |
| 3       | 2        | 3000   |
| 4       | 2        | 4000   |
| 5       | 3        | 8000   |
| 6       | 4        | 7000   |
| 7       | 5        | 9000   |

------

#### Expected Output

```
East|A-Mart|1|11000|11000 
East|B-Store|2|7000|18000
West|E-Hub|1|9000|9000 
West|C-Shop|2|8000|17000 
West|D-Depot|3|7000|24000
```

AddPreview

# 29.Recursive Hierarchy Insights -- Expert-2 30 mins

recursive CTE

aggregation

## Database Schema

You have two tables: `employees` and `hierarchy`.

### Table: `employees`

- integer column `emp_id` (primary key)
- text column `emp_name` (name of the employee)

### Table: `hierarchy`

- integer column `emp_id` (ID of the employee; references `employees.emp_id`)
- integer column `manager_id` (ID of the employee's manager; references `employees.emp_id`)

------

## User Task

Write an SQL query to calculate the **total number of employees reporting directly and indirectly** to each manager, including the manager themselves. For simplicity:

- A manager is anyone who has at least one direct report in the `hierarchy` table.
- Include managers who report to another manager (mid-level managers).

The output should include:

- `manager_id`
- `manager_name`
- `total_reports` (total employees directly and indirectly reporting to the manager, including the manager).

### Constraints:

- Sort the results by `total_reports` in descending order, and in case of ties, by `manager_name` alphabetically.

------

## Sample Testcases

### Sample Testcase 1

#### Table Data

##### `employees`

| emp_id | emp_name |
| ------ | -------- |
| 1      | Alice    |
| 2      | Bob      |
| 3      | Carol    |
| 4      | David    |
| 5      | Ethan    |
| 6      | Frank    |

##### `hierarchy`

| emp_id | manager_id |
| ------ | ---------- |
| 2      | 1          |
| 3      | 1          |
| 4      | 2          |
| 5      | 2          |
| 6      | 3          |

------

#### Analysis

1. **Alice (manager_id = 1)**:
   - Direct reports: Bob, Carol.
   - Indirect reports:
     - Bob's direct reports: David, Ethan.
     - Carol's direct reports: Frank.
   - Total employees = (1 (Alice) + 2 (Bob, Carol) + 3 (David, Ethan, Frank) = 6).
2. **Bob (manager_id = 2)**:
   - Direct reports: David, Ethan.
   - Total employees = (1 (Bob) + 2 (David, Ethan) = 3).
3. **Carol (manager_id = 3)**:
   - Direct report: Frank.
   - Total employees = (1 (Carol) + 1 (Frank) = 2).

------

#### Expected Output

```
1|Alice|6
2|Bob|3 
3|Carol|2
```

### Sample Testcase 2

#### Table Data

##### `employees`

| emp_id | emp_name |
| ------ | -------- |
| 1      | Grace    |
| 2      | Hannah   |
| 3      | Ian      |
| 4      | Jack     |
| 5      | Kate     |

##### `hierarchy`

| emp_id | manager_id |
| ------ | ---------- |
| 2      | 1          |
| 3      | 1          |
| 4      | 2          |
| 5      | 2          |

------

#### Analysis

1. **Grace (manager_id = 1)**:
   - Direct reports: Hannah, Ian.
   - Indirect reports:
     - Hannah's direct reports: Jack, Kate.
   - Total employees = (1 (Grace) + 2 (Hannah, Ian) + 2 (Jack, Kate) = 5).
2. **Hannah (manager_id = 2)**:
   - Direct reports: Jack, Kate.
   - Total employees = (1 (Hannah) + 2 (Jack, Kate) = 3).
3. **Ian (manager_id = 3)**:
   - No direct reports.

------

#### Expected Output

```
1|Grace|5 
2|Hannah|3 
```

AddPreview

30.Department Collaboration Metrics -- Expert-2 30 mins

set operations

aggregation

------

## Database Schema

You have two tables: `departments` and `collaborations`.

### Table: `departments`

- integer column `dept_id` (primary key)
- text column `dept_name` (name of the department)

### Table: `collaborations`

- integer column `collab_id` (primary key)
- integer column `dept_id_1` (ID of the first department, references `departments.dept_id`)
- integer column `dept_id_2` (ID of the second department, references `departments.dept_id`)
- integer column `hours_worked` (total hours worked together by the two departments)

------

## User Task

Write an SQL query to calculate the **collaboration metrics** for each department:

1. For each department, find:
   - `total_hours` worked with other departments (sum of all hours where the department was either `dept_id_1` or `dept_id_2`).
   - `unique_collaborations` count (number of distinct departments this department collaborated with).
2. A department should only be included in the results if:
   - It has collaborated with **at least 3 distinct departments**.
   - It has contributed to **at least 100 total hours** of collaboration.

The output should include:

- `dept_name`
- `total_hours`
- `unique_collaborations`

### Constraints:

- Sort the results by:
  1. `total_hours` in descending order.
  2. `dept_name` alphabetically in case of ties.

------

## Sample Testcases

### Sample Testcase 1

#### Table Data

##### `departments`

| dept_id | dept_name  |
| ------- | ---------- |
| 1       | HR         |
| 2       | IT         |
| 3       | Finance    |
| 4       | Marketing  |
| 5       | Operations |

##### `collaborations`

| collab_id | dept_id_1 | dept_id_2 | hours_worked |
| --------- | --------- | --------- | ------------ |
| 1         | 1         | 2         | 40           |
| 2         | 1         | 3         | 60           |
| 3         | 1         | 4         | 20           |
| 4         | 2         | 3         | 50           |
| 5         | 2         | 5         | 30           |
| 6         | 3         | 4         | 40           |
| 7         | 4         | 5         | 70           |

------

#### Analysis

1. **HR (dept_id = 1)**:
   - `total_hours` = (40 + 60 + 20 = 120).
   - Collaborated with (2, 3, 4) → (3) distinct departments.
   - **Qualifies**.
2. **IT (dept_id = 2)**:
   - `total_hours` = (40 + 50 + 30 = 120).
   - Collaborated with (1, 3, 5) → (3) distinct departments.
   - **Qualifies**.
3. **Finance (dept_id = 3)**:
   - `total_hours` = (60 + 50 + 40 = 150).
   - Collaborated with (1, 2, 4) → (3) distinct departments.
   - **Qualifies**.
4. **Marketing (dept_id = 4)**:
   - `total_hours` = (20 + 40 + 70 = 130).
   - Collaborated with (1, 3, 5) → (3) distinct departments.
   - **Qualifies**.
5. **Operations (dept_id = 5)**:
   - `total_hours` = (30 + 70 = 100).
   - Collaborated with (2, 4) → (2) distinct departments.
   - **Does not qualify**.

------

#### Expected Output

```
Finance|150|3 
Marketing|130|3 
HR|120|3 
IT|120|3
```

------

### Sample Testcase 2

#### Table Data

##### `departments`

| dept_id | dept_name                |
| ------- | ------------------------ |
| 1       | Sales                    |
| 2       | Support                  |
| 3       | Logistics                |
| 4       | Research and Development |
| 5       | Legal                    |

##### `collaborations`

| collab_id | dept_id_1 | dept_id_2 | hours_worked |
| --------- | --------- | --------- | ------------ |
| 1         | 1         | 2         | 50           |
| 2         | 1         | 3         | 80           |
| 3         | 1         | 4         | 20           |
| 4         | 2         | 3         | 60           |
| 5         | 2         | 5         | 40           |
| 6         | 3         | 4         | 90           |
| 7         | 4         | 5         | 30           |

------

#### Analysis

1. **Sales (dept_id = 1)**:
   - `total_hours` = (50 + 80 + 20 = 150).
   - Collaborated with (2, 3, 4) → (3) distinct departments.
   - **Qualifies**.
2. **Support (dept_id = 2)**:
   - `total_hours` = (50 + 60 + 40 = 150).
   - Collaborated with (1, 3, 5) → (3) distinct departments.
   - **Qualifies**.
3. **Logistics (dept_id = 3)**:
   - `total_hours` = (80 + 60 + 90 = 230).
   - Collaborated with (1, 2, 4) → (3) distinct departments.
   - **Qualifies**.
4. **Research and Development (dept_id = 4)**:
   - `total_hours` = (20 + 90 + 30 = 140).
   - Collaborated with (1, 3, 5) → (3) distinct departments.
   - **Qualifies**.
5. **Legal (dept_id = 5)**:
   - `total_hours` = (40 + 30 = 70).
   - Collaborated with (2, 4) → (2) distinct departments.
   - **Does not qualify**.

------

#### Expected Output

```
Logistics|230|3 
Support|150|3 
Sales|150|3 
Research and Development|140|3
```

AddPreview

# 31.Highest Sales By Product -- Expert-2 30 mins

CTE

conditional aggregation

# Database Schema

You have a table `sales` that tracks daily sales across various stores:

### Table: `sales`

- integer column `store_id` (ID of the store)
- text column `product` (name of the product sold)
- integer column `quantity` (quantity of the product sold)
- date column `sale_date` (date of the sale)

------

# User Task

Write an SQL query to find the store(s) with the highest total sales (in terms of `quantity`) for each product during the last week of recorded sales in the database.

- If multiple stores have the same highest total sales for a product, include all of them.
- Sort the output by `product` in ascending order and then by `store_id` in ascending order.

The output should have the following columns:

- `product`
- `store_id`
- `total_sales`

------

# Sample Testcases

## Sample Testcase 1

### Table Data

#### `sales`

| store_id | product | quantity | sale_date  |
| -------- | ------- | -------- | ---------- |
| 1        | Apples  | 50       | 2024-12-20 |
| 2        | Apples  | 60       | 2024-12-21 |
| 3        | Apples  | 60       | 2024-12-21 |
| 1        | Oranges | 30       | 2024-12-20 |
| 2        | Oranges | 50       | 2024-12-21 |
| 1        | Apples  | 10       | 2024-12-22 |

### Analysis

- The last week of recorded sales ends on 2024-12-22.
- Total sales per store during the last week:
  - For Apples:
    - Store 1: 50 + 10 = 60
    - Store 2: 60
    - Store 3: 60
    - Highest sales: 60 (Store 2 and Store 3).
  - For Oranges:
    - Store 1: 30
    - Store 2: 50
    - Highest sales: 50 (Store 2).

**Expected Output**

```
Apples 2 60 
Apples 3 60 
Oranges 2 50
```

------

## Sample Testcase 2

### Table Data

#### `sales`

| store_id | product | quantity | sale_date  |
| -------- | ------- | -------- | ---------- |
| 1        | Bananas | 100      | 2024-11-25 |
| 2        | Bananas | 150      | 2024-11-26 |
| 1        | Bananas | 100      | 2024-11-27 |
| 3        | Grapes  | 200      | 2024-11-27 |
| 2        | Grapes  | 200      | 2024-11-28 |
| 1        | Grapes  | 100      | 2024-11-28 |

### Analysis

- The last week of recorded sales ends on 2024-11-28.
- Total sales per store during the last week:
  - For Bananas:
    - Store 1: 100 + 100 = 200
    - Store 2: 150
    - Highest sales: 200 (Store 1).
  - For Grapes:
    - Store 3: 200
    - Store 2: 200
    - Store 1: 100
    - Highest sales: 200 (Store 3 and Store 2).

**Expected Output**

```
Bananas 1 200 
Grapes 2 200 
Grapes 3 200
```

AddPreview

# 32.Department Task Load Analysis -- Expert-2 30 mins

window function

ranking

partitioning

## Database Schema

You manage a task tracking system with two tables: `departments` and `tasks`.

### Table: `departments`

- integer column `dept_id` (primary key)
- text column `dept_name` (name of the department)

### Table: `tasks`

- integer column `task_id` (primary key)
- integer column `dept_id` (foreign key referencing `departments.dept_id`)
- text column `task_type` (type of the task; e.g., 'critical', 'major', 'minor')
- integer column `task_count` (number of tasks of this type assigned to the department)

------

## User Task

Write an SQL query to calculate the **task distribution metrics** for each department, with the following requirements:

1. **Total Tasks**: Calculate the total number of tasks assigned to each department.
2. **Distinct Task Types**: Count the number of distinct task types (`task_type`) in each department.
3. **Largest Task Type**: Identify the task type with the highest `task_count` in each department.
   - If two task types have the same `task_count`, choose the one that comes first alphabetically.

Include only departments where:

- The **total number of tasks** is greater than `50`.

The output should include:

- `dept_name`
- `total_tasks`
- `distinct_task_types`
- `largest_task_type`
- `largest_task_count`

### Constraints:

- Sort the results by `total_tasks` in descending order. If there is a tie, sort alphabetically by `dept_name`.

------

## Sample Testcases

### Sample Testcase 1

#### Table Data

##### `departments`

| dept_id | dept_name   |
| ------- | ----------- |
| 1       | Research    |
| 2       | Development |
| 3       | Marketing   |

##### `tasks`

| task_id | dept_id | task_type | task_count |
| ------- | ------- | --------- | ---------- |
| 1       | 1       | critical  | 30         |
| 2       | 1       | major     | 20         |
| 3       | 1       | minor     | 10         |
| 4       | 2       | critical  | 25         |
| 5       | 2       | major     | 30         |
| 6       | 2       | minor     | 5          |
| 7       | 3       | critical  | 20         |
| 8       | 3       | major     | 15         |

------

#### Analysis:

1. **Research**:
   - Total Tasks = (30 + 20 + 10 = 60).
   - Distinct Task Types = (3) (critical, major, minor).
   - Largest Task Type = `critical` (30 tasks).
2. **Development**:
   - Total Tasks = (25 + 30 + 5 = 60).
   - Distinct Task Types = (3) (critical, major, minor).
   - Largest Task Type = `major` (30 tasks).
3. **Marketing**:
   - Total Tasks = (20 + 15 = 35).
   - **Does not qualify** (total tasks ≤ 50).

------

#### Expected Output:

```
Development|60|3|major|30 
Research|60|3|critical|30
```

### Sample Testcase 2

#### Table Data

##### `departments`

| dept_id | dept_name |
| ------- | --------- |
| 1       | HR        |
| 2       | IT        |
| 3       | Finance   |

##### `tasks`

| task_id | dept_id | task_type | task_count |
| ------- | ------- | --------- | ---------- |
| 1       | 1       | critical  | 40         |
| 2       | 1       | major     | 15         |
| 3       | 2       | critical  | 35         |
| 4       | 2       | minor     | 20         |
| 5       | 3       | major     | 30         |
| 6       | 3       | minor     | 25         |

------

#### Analysis:

1. **HR**:
   - Total Tasks = (40 + 15 = 55).
   - Distinct Task Types = (2) (critical, major).
   - Largest Task Type = `critical` (40 tasks).
2. **IT**:
   - Total Tasks = (35 + 20 = 55).
   - Distinct Task Types = (2) (critical, minor).
   - Largest Task Type = `critical` (35 tasks).
3. **Finance**:
   - Total Tasks = (30 + 25 = 55).
   - Distinct Task Types = (2) (major, minor).
   - Largest Task Type = `major` (30 tasks).

------

#### Expected Output:

```
Finance|55|2|major|30 
HR|55|2|critical|40 
IT|55|2|critical|35
```