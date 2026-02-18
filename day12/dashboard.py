import matplotlib.pyplot as plt

# Data for bar chart
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

# Data for line chart (monthly sales trend example)
months = [1, 2, 3, 4, 5]
monthly_sales = [200, 350, 400, 500, 650]

# Create figure

# Subplot 1: Bar Chart
plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Product Category")
plt.ylabel("Sales Units")

# Subplot 2: Line Plot
plt.subplot(1, 2, 2)
plt.plot(months, monthly_sales)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales Units")

# Prevent overlap
plt.tight_layout()

# Display
plt.show()
