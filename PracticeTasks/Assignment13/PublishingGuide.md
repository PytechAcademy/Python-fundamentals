### Step 1: Build and Distribute

1. Open a terminal and navigate to the `datetimeutils` directory.

2. Run the following command to build the package:

   ```
   python setup.py sdist
   ```

3. After the build is successful, you'll find a `dist` directory containing a `.tar.gz` file.

### Step 2: Publish on PyPI

1. Install the `twine` package if you haven't already:

   ```
   pip install twine
   ```

2. Upload your package to PyPI using `twine`:

   ```
   twine upload dist/*
   ```

### Step 3: Using the Published Package

Now you can use your published `datetimeutils` package in other projects. To use the functions you've defined:

```python
from datetimeutils import count_days, get_month

target_date = datetime.date(2023, 8, 31)
days = count_days.days_to_date(target_date)
print(f"Days to target date: {days}")

date = datetime.date(2023, 8, 10)
month = get_month.month_as_string(date)
print(f"Month: {month}")
```


