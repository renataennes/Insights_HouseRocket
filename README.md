<img src="/mansion.png">

🏡 House Rocket Business Insights
House Rocket is a digital platform whose business model is based on the purchase and sale of properties using data analysis. The goal is to identify undervalued assets in the Seattle market to maximize profit margins through strategic resale.

📈 The Business Problem
The CEO of House Rocket needs to identify which properties are worth buying and at what price they should be resold. The main challenge is to distinguish "true opportunities" from poor quality listings in a dataset of +21,000 properties.

🛠️ Data Solution & Feature Engineering
To provide a deeper analysis, I developed a custom Value Score metric:

Value Score: A ratio between the average price of the region (Zipcode) and the Price per Sqft of the property.
Price Levels: Categorization of properties into quartiles (Low, Mid-Low, Mid-High, High) to facilitate filtering.
Location Intelligence: Geospatial analysis to identify clusters of undervalued properties.

💡 Strategic Insights & Purchase Recommendations
Based on the data analysis, the following strategy was defined to optimize the portfolio:

1. The "Golden Opportunity" Filter
I recommend purchasing properties that meet these three criteria simultaneously:

Condition: Rated 3 or higher.
Price: Below the median price for that specific Zipcode.
Value Score: High (indicating the property is significantly cheaper than its neighbors per square foot).

2. Seasonality & Timing
Data shows that prices vary by year of construction and renovation status. Properties built before 1950 but with high "Condition" ratings offer the best ROI after minor cosmetic updates.

3. Investment Suggestions
Buy: Properties in Zipcodes with high price appreciation but currently listed 20% below the local average.
Sell: Resale price should be the purchase price + 30% (if the purchase was below the median) or purchase price + 10% (if the purchase was above the median).

🚀 How to Run the Project
Clone the repository: git clone https://github.com/renataennes/Insights_HouseRocket.git

Install dependencies: pip install -r requirements.txt

Run the Dashboard: streamlit run house_application.py

Author: Renata Araújo Ennes

Tools: Python, Pandas, Plotly, Streamlit.
