# Required Packages  
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

# Function to get data  
file_name = 'linear.csv'


def get_data(file_name):
    data = pd.read_csv(file_name)  # here ,use pandas to read cvs file.
    X_parameter = []
    Y_parameter = []
    for single_square_feet, single_price_value in zip(data['area'], data['price']):  # 遍历数据
        X_parameter.append([float(single_square_feet)])  # 存储在相应List列表中
        Y_parameter.append(float(single_price_value))
    return X_parameter, Y_parameter


# Function for Fitting our data to Linear model
def linear_model_main(X_parameters, Y_parameters, predict_value):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)  # train model
    predict_outcome = regr.predict(predict_value)
    predictions = {}
    predictions['intercept'] = regr.intercept_
    predictions['coefficient'] = regr.coef_
    predictions['predicted_value'] = predict_outcome
    return predictions


# Function to show the resutls of linear fit model  
def show_linear_line(X_parameters, Y_parameters):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    plt.scatter(X_parameters, Y_parameters, color='blue')
    plt.plot(X_parameters, regr.predict(X_parameters), color='red', linewidth=4)
    plt.xticks(())
    plt.yticks(())
    plt.show()


# 数据存储成一个.csv文件，可以先用Excel来存储数据，记得写上列名。之后保存的时候另存为csv格式即可。
# 导入csv时需将csv放在py文件同一目录，否则用绝对路径
X, Y = get_data('linear.csv')
predictvalue = 700
result = linear_model_main(X, Y, predictvalue)
print("Intercept value ", result['intercept'])
print("coefficient", result['coefficient'])
print("Predicted value: ", result['predicted_value'])
show_linear_line(X, Y)
