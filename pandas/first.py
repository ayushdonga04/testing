import pandas as pd

data = {
    "guest_id": [None, 2, 3, 4, 1, 5, 6, 1, 1],
    "visit_date": [
        "2024-07-05", "2024-07-06", "2024-07-10", "2024-07-12",
        "2024-07-15", "2024-07-20", "2024-07-25", None, "2024-08-15"
    ],
    "amount_spent": [50, 30, 20.5, 40, 35, 60, 25, 55, 45],
    "park_experience_type": [
        "Attraction", "Dining", None , "Entertainment",
        "Dining", "Attraction", "Retail", "Attraction", None
    ]
}






july_2024=fct_guest_spending[(fct_guest_spending["visit_date"].dt.month==7) &
          (fct_guest_spending["visit_date"].dt.year==2024)]

# Show DataFrame

'''

df1=july_2024.groupby(july_2024["park_experience_type"])

print(df1.describe())

print(df1["amount_spent"].sum()/df1["guest_id"].count())
'''

'''
For guests who visited our parks more than once in August 2024, what is the
difference in spending between their first and their last visit? This investigation,
using sequential analysis,will reveal any shifts in guest spending behavior over multiple visits.
# Step 1: Filter for August 2024
aug_2024 = fct_guest_spending[
    (fct_guest_spending["visit_date"].dt.month == 8) &
    (fct_guest_spending["visit_date"].dt.year == 2024)
]

# Step 2: Find guests with more than one visit
repeat_guests = aug_2024["guest_id"].value_counts()
repeat_guests = repeat_guests[repeat_guests > 1].index

# Step 3: Filter only those guests
repeat_data = aug_2024[aug_2024["guest_id"].isin(repeat_guests)]

# Step 4: Sort by guest_id and visit_date
repeat_data = repeat_data.sort_values(by=["guest_id", "visit_date"])

# Step 5: Group and get first and last spending
spending_diff = repeat_data.groupby("guest_id")["amount_spent"].agg(
    first_spending="first",
    last_spending="last"
)

# Step 6: Calculate difference
spending_diff["spending_difference"] = spending_diff["last_spending"] - spending_diff["first_spending"]

# Step 7: Reset index and print result
spending_diff = spending_diff.reset_index()
print(spending_diff)
'''

'''
In September 2024, how can guests be categorized into distinct spending segments such as Low, Medium, and High based on their total spending? Use the following thresholds for categorization:
-Low: Includes values from $0 up to, but not including, $50.
-Medium: Includes values from $50 up to, but not including, $100.
-High: Includes values from $100 and above.
Exclude guests who did not make any purchases in the period.
# Step 1: Filter data for September 2024
sep_2024 = fct_guest_spending[
    (fct_guest_spending["visit_date"].dt.month == 9) &
    (fct_guest_spending["visit_date"].dt.year == 2024)
]

# Step 2: Group by guest and calculate total spending
guest_spending = sep_2024.groupby("guest_id")["amount_spent"].sum().reset_index()

# Step 3: Exclude guests with no spending (optional if guaranteed no 0)
guest_spending = guest_spending[guest_spending["amount_spent"] > 0]

# Step 4: Define segmentation function
def categorize_spending(amount):
    if amount < 50:
        return "Low"
    elif amount < 100:
        return "Medium"
    else:
        return "High"

# Step 5: Apply categorization
guest_spending["spending_segment"] = guest_spending["amount_spent"].apply(categorize_spending)

# Step 6: Print result
print(guest_spending)
'''

print(fct_guest_spending.dropna())



