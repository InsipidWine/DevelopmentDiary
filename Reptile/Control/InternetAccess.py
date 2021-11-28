# -*- coding: UTF-8 -*-
import requests
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # init
    salary = []
    salary_min = []
    salary_max = []
    company_name = []
    url = 'https://www.lagou.com/jobs/v2/positionAjax.json'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29',
    }
    parm = {
        'first': 'true',
        'needAddtionalResult': 'false',
        'city': '沈阳',
        'px': 'new',
        'pn': '1',
        'kd': 'C++'
    }
    # Get the data
    response_json = requests.get(url=url, params=parm, headers=header).json()
    size = (response_json['content']['positionResult']['resultSize'])
    for num in range(0, size - 1):
        salary.append(response_json['content']['positionResult']['result'][num]['salary'])
        company_name.append(response_json['content']['positionResult']['result'][num]['companyFullName'])
    for num in range(0, size - 1):
        salary_min.append(int(salary[num].split("-")[0].replace('k', '')))
        salary_max.append(int(salary[num].split("-")[1].replace('k', '')))
    # Histogram Set
    plt.rcParams['font.family'] = ['SimHei']
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams["axes.unicode_minus"] = False
    x = np.arange(len(company_name))
    width = 0.4  # 设置数据条宽度
    fig, ax = plt.subplots(1, 1, figsize=(12, 9))
    ax.spines['top'].set_visible(False)  # 不显示图表框的上边框
    ax.spines['right'].set_visible(False)
    p1 = ax.bar(x - width / 2, salary_min, width, label="最低工资",  align="center", alpha=0.5)
    p2 = ax.bar(x + width / 2, salary_max, width, label="最高工资",  align="center", alpha=0.5)
    ax.set_xticks(x)
    ax.set_xticklabels(company_name)
    plt.xticks(fontsize=15, rotation=90)
    plt.title("拉钩 沈阳 C++ Salary")
    plt.legend()
    plt.show()
