# Project Overview
Analyzed wedding venue data from WedMeGood, a leading Indian wedding planning platform. Tackles user decision fatigue due to the overwhelming number of venue listings and lack of intelligent filtering. Objective: Identify key factors influencing venue popularity—including reviews, price, amenities, and capacity. Aims to improve venue recommendations, enable better marketing strategies, and assist vendors in enhancing their offerings.

# Methodology
Web scraped venue data from six major cities: Delhi-NCR, Mumbai, Pune, Chennai, Lucknow, and Jaipur.

# Extracted features: Name, Ratings, Reviews, Type, Location, Menu_Price, Pax, Rooms, and Amenities.
Performed data cleaning and transformation:
Converted text to numeric values (e.g., price, reviews, amenities count).

Split guest capacity (Pax) into Pax_Min and Pax_Max.

Extracted destination/city from venue locations.

Applied IQR method to remove outliers in relevant numerical fields while preserving meaningful pricing and rating information, but didn't removed outliers from menu price and ratings column because they're needed.

Final output: a cleaned, structured dataset (df2) ready for visual and statistical analysis.

Tools & Future Enhancements
Built using Python and Jupyter Notebook.
Libraries used: Pandas, NumPy, BeautifulSoup, Requests, Matplotlib, Seaborn.

# Python 
- if you want to access Python Data Collection, Cleaning, Analysis (click here)----> [PYTHON - Data Collection, Cleaning, Analysis](https://github.com/Ruchii151/Wedding-Venues-Analysis/tree/main/PYTHON%20-%20Data%20Collection%2C%20Cleaning%2C%20Analysis)
- access PPT from here: https://github.com/Ruchii151/Wedding-Venues-Analysis/blob/main/PYTHON%20-%20Data%20Collection%2C%20Cleaning%2C%20Analysis/Wedding_Halls.pptx

![image](https://github.com/user-attachments/assets/379b5d45-7d03-4f53-b61a-4207c277596b)

![image](https://github.com/user-attachments/assets/b69eccdb-7045-4cab-a342-3320739e7893)



# SQL 

![image](https://github.com/user-attachments/assets/28085670-bd8e-4a63-9acf-3ab96d16d9ea)





# Power BI Report

![Screenshot 2025-06-26 134258](https://github.com/user-attachments/assets/1cbb1f14-321a-42f1-946b-0381e983e589)




