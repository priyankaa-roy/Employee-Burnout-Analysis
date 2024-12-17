# 🧠 Employee-Burnout-Analysis

## 📚 Description
The analysis of the employee dataset was conducted to understand various aspects related to employee mental fatigue and burn rate, segmented by gender, company type, and other relevant factors. This project analyzes **employee burnout** to identify key factors contributing to mental fatigue in the workplace. The dataset includes variables such as employee gender, company type, and mental fatigue scores, and the goal is to explore trends, perform statistical testing, and visualize key insights to help understand the factors affecting employee well-being.

## ⚙️ Features
- **🔧 Data Cleaning:** Handle missing values, convert data types, and prepare the dataset for analysis.
- **📊 Exploratory Data Analysis (EDA):** Generate descriptive statistics, group data, and perform frequency analysis to gain insights.
- **📈 Data Visualization:** Create histograms, bar charts, and box plots to visualize distributions and outliers.
- **🔍 Correlation Analysis:** Visualize relationships between variables using correlation matrices.
- **📉 Statistical Testing:** Conduct hypothesis testing (T-test) to compare mental fatigue scores between male and female employees.

## 🛠️ Tech Stack / Tools Used
- **🐍 Python** (Primary language for data processing and analysis)
- **📊 Pandas** (For data manipulation and cleaning)
- **📉 Matplotlib** (For data visualization)
- **🌐 Seaborn** (For advanced data visualization)
- **🔬 SciPy** (For statistical analysis)
- **📝 Jupyter Notebooks** (For running and documenting the analysis)

## 📥 Installation
Follow these steps to set up the project on your local machine:

1. Clone the repository:
    ```bash
    git clone [https://github.com/yourusername/employee-burnout-analysis.git](https://github.com/priyankaa-roy/Employee-Burnout-Analysis)
    ```
2. Navigate to the project directory:
    ```bash
    cd employee-burnout-analysis
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    If `requirements.txt` is not available, you can install the necessary libraries manually:
    ```bash
    pip install pandas matplotlib seaborn scipy
    ```

## 🏃‍♀️ Usage
Once you have set up the project, you can run the following code snippets to explore and analyze the dataset:

1. **Load and Inspect the Dataset**:
    ```python
    import pandas as pd
    data = pd.read_csv('employee_burnout_analysis-AI 2.csv')  # Update the path if necessary
    print(data.info())  # Inspect the dataset info
    print(data.describe())  # Get summary statistics
    ```

2. **Handle Missing Values**:
    ```python
    data.fillna(data.mean(), inplace=True)  # Fill missing values with the mean for numerical columns
    data.dropna(inplace=True)  # Drop rows with any missing values
    ```

3. **Convert Data Types** (e.g., convert 'Date of Joining' to datetime):
    ```python
    data['Date of Joining'] = pd.to_datetime(data['Date of Joining'])
    ```

4. **Data Exploration**:
    - **Descriptive Statistics**:
      ```python
      print(data.describe())  # View descriptive statistics
      ```

    - **Group Data** (by Gender and Company Type):
      ```python
      grouped_data = data.groupby(['Gender', 'Company Type'])['Mental Fatigue Score'].mean()
      print(grouped_data)
      ```

    - **Frequency Counts** (for categorical variables):
      ```python
      gender_counts = data['Gender'].value_counts()
      company_counts = data['Company Type'].value_counts()
      print(gender_counts)
      print(company_counts)
      ```

5. **Data Visualization**:
    - **Histogram for Mental Fatigue Score**:
      ```python
      import matplotlib.pyplot as plt
      plt.hist(data['Mental Fatigue Score'], bins=20)
      plt.title('Distribution of Mental Fatigue Scores')
      plt.xlabel('Mental Fatigue Score')
      plt.ylabel('Frequency')
      plt.show()
      ```

    - **Bar Chart for Company Type**:
      ```python
      data['Company Type'].value_counts().plot(kind='bar')
      plt.title('Employee Count by Company Type')
      plt.xlabel('Company Type')
      plt.ylabel('Number of Employees')
      plt.show()
      ```

    - **Box Plot for Outliers**:
      ```python
      import seaborn as sns
      sns.boxplot(x='Company Type', y='Mental Fatigue Score', data=data)
      plt.title('Mental Fatigue Score by Company Type')
      plt.show()
      ```

6. **Statistical Analysis**:
    - **Correlation Matrix**:
      ```python
      correlation_matrix = data.corr()
      sns.heatmap(correlation_matrix, annot=True)
      plt.title('Correlation Matrix')
      plt.show()
      ```

    - **Hypothesis Testing** (T-test for Gender vs. Mental Fatigue Score):
      ```python
      from scipy import stats
      male_scores = data[data['Gender'] == 'Male']['Mental Fatigue Score']
      female_scores = data[data['Gender'] == 'Female']['Mental Fatigue Score']

      t_stat, p_value = stats.ttest_ind(male_scores, female_scores)
      print(f'T-statistic: {t_stat}, P-value: {p_value}')
      ```

      **Interpretation**: A low P-value (typically < 0.05) indicates that there is a statistically significant difference in the mental fatigue scores between male and female employees.

## 🤝 Contributing
We welcome contributions to this project! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## 📝 License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments
- Special thanks to the creators of the dataset.
- Libraries like **Pandas**, **Seaborn**, **Matplotlib**, and **SciPy** were crucial in carrying out the analysis and visualization.
