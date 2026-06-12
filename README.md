# Cleaning Data&nbsp;&nbsp;

### Objective 
The primary objective of this project is to improve the quality ,accuracy,and reliability of the dataset through a systematic data cleaning process.Real-world datasets often contain missing values ,duplicate records,inconsistent formats,incorrect entries,and other data quality issues that can negatively impact analysis and decison making 
This project aims to identify and address these issues by performing tasks such as handling missing data ,removing duplicate records,correcting inconsistencies,standardizing data formats,and validating data integrity.By cleaning and preprocessing the dataset, the project ensures that the data is accurate,consistent,and ready for furthur analysis,visualization,reporting,or machine learning applications

### Dataset Overview
+ The dataset originally sourced from Kaggle.it contains columns such as id,name,including host details,geographical location,pricing,room types,availability,and customer reviews.
+ The dataset is not completely clean and hence significant data cleaning is required.For example,missing values in columns such as last_reviewand reviews_per_month need to be handled appropritely
+ Outliers in features like price are identified and treated using statistical methods to ensure realistic values.Inconsistent or irrevelant data entries are also removed to improve data quality.
+ The cleaned dataset is then prepared for furthur analysis and modeling.The processed data can be used to analyze pricing trends,room distribution,host activity,and availability patterns across different locations

### Tools and Technologies 
+ Google Colab-Cloud-based environment for writing and executing Python code
+ Python-Programming language used for data cleaning,and analysis.
+ Pandas-Used for data manipulation,cleaning,and preprocessing.
+ NumPy-Used for numerical operations and handling arrays.
+ Microsoft Excel/CSV Files-Data source for the project.
+ Matplotlib-Used for data visualization and plotting charts.
+ Seaborn-Used for creating advanced statistical visualizations.

 ### Steps in Data Cleaning

1.Import Libraries

   + Pandas -> Data handling
   + NumPy -> Numerical computations
     
2.Load Dataset

 + Loaded dataset using 'pd.read_csv()'
 + Displayed initial data

3.Data inspection

 + df.info() -> shows columns,data types,missing values
 + df.describe() -> statistical summary of numerical data

4.Data Cleaning 

 + Removed duplicate rows
 + Identify and handling missing values

5.Standardization
 + Remove spaces
 + Convert to lowercase

6.Outliers Detection
 + Identify extreme values using IDR method for each numerical column

7.Remove Outliers
 + Define a function to filter out extreme values
 + Apply it to all numerical columns

8.Visualize Outliers
 + Use box plots to visually confirm outlier removal
 
    ### Outcome
    + Below is the outcome of dataset after data cleaning.
      <img width="1718" height="481" alt="image" src="https://github.com/user-attachments/assets/14903a3b-a8f1-4036-812a-2d3956e830de" />

      + The data cleaning process significantly improved the quality and reliablity of the dataset
      + By handling missing values ,removing duplicates,and treating outliers, the dataset became more consistent and suitable for analysis
      + After cleaning,the dataset provided better insights into property listings,including pricing trends,room type distribution ,and location-based patterns
      + The cleaned data enabled accurate and meaningful analysis,which can be used for further visualization and decision-making.
      + The project demonstrates the importance of data preprocessing in real-world datasets and highlights how proper data cleaning can enhance the overall performance of analysis and machine learning models
  
