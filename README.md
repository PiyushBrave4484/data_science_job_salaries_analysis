# data_science_job_salaries_analysis
I have done analysis over data scientist salaries data.


Data Science Job Salaries Data Analysis
Using Python, MySql and PowerBI
Steps Followed-

INITIAL STEPS :- Connection , cleaning and preprocessing.

1)	Download data science job salary dataset from Kaggle.
2)	Create a database in MYSQL and imported dataset into it.
3)	In jupyter notebook imported necessary libraries( numpy ,pandas,matplotlib , seaborn).
4)	In jupyter notebook establish connection with MYSQL database where dataset is present.
5)	Data analysing through functions like info(), describe() , isnull().sum() etc.
6)	Outliers identification over numerical columns using box plot.
7)	Use .describe() to check statistical values
8)	Now connect mysql data base with powerbi

MIDDLE STEPS :- Visualization

1)	Use Python for advanced problem statement which include complex statistical operations (I.e. Box plot) 
                	Heat map showing correlation between numerical columns.
                	Line chart showing salary growth since year 2020 by experience level.
                	Box plot showing salary distribution by remote work ratio 2.

2)	Use PowerBI to visualize Basic to Intermediate problem statements

                	Pie chart showing avg. salary by company size
                	Map chart showing top 5 locations by avg. salary
                	Slicer for job title, experience level, work year
                	Bubble chart showing avg. remote ratio vs experience level with bubble size of avg. salary
                	Column chart for top 10 job titles by avg. salary


FINAL STEPS:- Streamlit app and documentation

1)	Import streamlit library 
2)	create user interface code
3)	Create a separate project.app file in the same directory for Streamlit app
4)	Use a simple menu to showcase charts or dashboard

                	Use Home, Python charts > Various charts, Power BI dashboard, and file 	        
                                   Sample Dashboard		
           		                     Pbix file


