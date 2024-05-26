# SwiftMarket Analysis
## Overview :
_SwiftMarket Analysis is a powerful data analytics tool to provide insights into the performance and effectiveness of eCommerce. This Project presents the client's behaviour and problems with the help of visualization of graphs,With SwiftMarket Analysis, businesses can access comprehensive data and metrics to optimize their online sales strategies and drive growth._

![Screenshot 2024-05-26 120655](https://github.com/MonikaHussain/ecommerce_analysis/assets/167159347/acc30e16-1252-4db5-bd6e-69043facc36b)



## Features :
- _Data collection from Website [can prefer KAGGLE link](https://www.kaggle.com/datasets/monikahussain/swiftmarket-dataset)_
- _Visualization of graphs_
- _Problem solving_
- _Use of different Libraries_
- _Businesslike presentation_ 



##  Libraries :
- _Numpy_
- _Pandas_
- _Matplotlip_
- _Seaborn_



## Sample Code:
```
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



## Visualization Description :
_This repository utilizes graohs as a fundamental tool for data visualization and analysis.They offer a powerful way to represent relationships and dependencies between different data points.In this project,I leverage various graph types_


### Sample Graph :

![Screenshot 2024-05-21 212553](https://github.com/MonikaHussain/ecommerce_analysis/assets/167159347/091e5da6-3eeb-4b75-ad30-b572fbee9330)



## Conclusion:
_This project of SwiftMarket analysis has provided valuable insights that can inform strategic decision-making and drive the continued success of the platform. By leveraging these insights and implementing targeted initiatives, SwiftMarket can position itself for sustained growth and competitiveness in the marketplace._







