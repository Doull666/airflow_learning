# airflow_learning
## 内容介绍：airflow代码开发内容


## airflow执行时间设置
1. 'start_date': 
- datetime(2021,12,23)，开始时间设置为2021/12/23的零点
- airflow.utils.dates.days_ago(1)，开始时间为当前时间的前一天
2. schedule_interval="0 22 * * 5"，执行周期设置为每周五晚上10点整开始执行
3. 具体执行时间：
- 第一次执行，会马上进行调度的初始化
- 第二次执行，会根据调度周期的时间执行


