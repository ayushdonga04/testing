import pandas as pd
from io import StringIO

data = """
sale_id,sale_date,product_id,sale_amount,celebrity_id
1,2025-01-10,901,,101
2,2025-01-15,901,1500,101
3,2025-02-03,902,2000.5,102
4,2025-03-12,903,2500.75,103
5,2025-03-20,904,,104
6,2025-02-28,901,1000,101
7,2025-03-25,902,300,102
8,2025-03-30,905,1800,105
9,2025-01-20,903,1200,103
10,2025-02-05,906,500,106
11,2025-03-01,907,2200,107
12,2025-02-15,908,1300,101
13,2025-03-15,909,,102
14,2025-01-25,910,900,108
15,2025-02-20,905,700,105
16,2025-03-28,902,1500,102
17,2024-11-15,901,800,101
18,2024-07-30,902,1000,102
19,2025-04-10,905,2000,105
20,2024-09-05,903,1100,103
"""

# Read data
df = pd.read_csv(StringIO(data))

# Convert sale_date to datetime
df['sale_date'] = pd.to_datetime(df['sale_date'])

# Filter for Q1 2025 and missing sale_amount
q1_missing_sales = df[
    (df['sale_date'] >= '2025-01-01') &
    (df['sale_date'] <= '2025-03-31') &
    (df['sale_amount'].isna())
]

print(q1_missing_sales)
