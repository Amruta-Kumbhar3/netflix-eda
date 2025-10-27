🎬 **Netflix Exploratory Data Analysis (EDA)**

A Python-based data analysis project that explores Netflix Movies and TV Shows to uncover trends in genres, production countries, and content growth using pandas, matplotlib, and WordCloud.

📊 **Project Overview**

##The main goals of this EDA project were:

##To understand how Netflix content is distributed by type, genre, and release year

-To analyze country-wise content trends

-To identify top actors and directors

-To visualize the overall content growth over time

🧰 **Tech Stack**
Category	Tools Used
Programming	Python
Data Analysis	pandas, numpy
Visualization	matplotlib, wordcloud
Environment	Jupyter Notebook / VS Code

🚀 **Features & Analysis**

✅ Handling missing values in the dataset

📈 Distribution of Movies vs TV Shows

🌎 Top countries producing Netflix content

🎭 WordCloud visualization of genres

🎬 Most frequent actors and directors

🕒 Year-wise content growth trend

🗂️ **Dataset Information**

Dataset used: [Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)

File: netflix_titles.csv

Columns include:

type, title, director, cast, country, release_year, rating, duration, listed_in, and description.

⚠️ The dataset file is ignored in this repository (.gitignore) due to size and licensing.
Please download it separately from Kaggle and place it in your project folder.

🧮 How to Run Locally
# Clone the repository
git clone https://github.com/Amruta-Kumbhar3/netflix-eda.git

# Move into the project folder
cd netflix-eda

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # (on Windows)

# Install dependencies
pip install pandas matplotlib seaborn wordcloud

# Run the Python file
python Netflix.py

📸 **Example Visualizations**

Movie vs TV Show distribution (Pie Chart) ![Movie vs TV Show distribution](https://raw.githubusercontent.com/Amruta-Kumbhar3/netflix-eda/main/screenshots/Figure_2.png)


Genre WordCloud ![Genre WordCloud](https://raw.githubusercontent.com/Amruta-Kumbhar3/netflix-eda/main/screenshots/Figure_3.png)


Top 10 Countries Producing Netflix Content (Bar Chart) ![Top 10 Countries Producing Netflix Content (Bar Chart)](https://raw.githubusercontent.com/Amruta-Kumbhar3/netflix-eda/main/screenshots/Figure_4.png)

Year-wise Content Growth (Line Chart) ![Year-wise Content Growth (Line Chart)](https://raw.githubusercontent.com/Amruta-Kumbhar3/netflix-eda/main/screenshots/Figure_5.png)

🌱 **First Project Note**

This is one of my early Python data analysis projects, where I explored real-world data and practiced data cleaning, visualization, and insight extraction.

Through this, I learned:

How to handle missing values in large datasets

How to visualize data effectively with Matplotlib and WordCloud

How to interpret trends and tell stories from data
