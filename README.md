# SwiftMarket Analysis
_This project provides a comprehensive analysis of e-commerce data to uncover valuable insights and trends. It offers features for data collection, preprocessing, exploratory analysis, and visualization, making it an essential tool for data analysts and e-commerce professionals..In the project the main goal was to analyzing e-commerce data to identify trends, patterns, and insights.
Visulization of Graphs are prepared on the results,using different libraries_


### Features :
- _Data collection from e-commerce websites [Can prefer the KAGGLE dataset](https://www.kaggle.com/datasets/thedevastator/unlock-profits-with-e-commerce-sales-data)_
- _Data preprocessing and cleaning_
- _Statistical analysis_
- _Visualization of results_


### Libraries :
* _Pandas_
* _Matplotlib_
* _Numpy_
* _Seaborn_


### Sample code :
``` python
# function to read sql query
def read_query(query):
    
    cursor.execute(query)
    rows = cursor.fetchall()
    
    return pd.DataFrame(data=rows, columns=cursor.column_names)


if __name__=='__main__':
    query = 'Show tables;'
    print(query)
    df = read_query(query=query)
    print(df)
```


### Visualization description:
_This repository utilizes graphs as a fundamental tool for data visualization and analysis. They offer a powerful way to represent relationships and dependencies between different data points. In this project, I leverage various graph types_

### Sample Graph :
![Screenshot 2024-05-21 212553](https://github.com/MonikaHussain/ecommerce_analysis/assets/167159347/6984dbb4-e057-4310-a145-d32c8c57bbf7)




### Conclusion:
_In conclusion, this repository provides a comprehensive framework for eCommerce analysis, offering valuable insights into client behavior.  The tools  presented here enable thorough examination of sales data,  paving the way for informed decision-making  in the dynamic landscape of eCommerce. We believe that by harnessing the power of data analytics, businesses can unlock new opportunities, and thrive in the ever-evolving eCommerce ecosystem._


