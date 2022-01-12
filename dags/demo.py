#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import airflow
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.sensors import ExternalTaskSensor
from airflow.contrib.operators.ssh_operator import SSHOperator
from datetime import datetime,timedelta

reload(sys)
sys.setdefaultencoding('utf-8')

default_args = {
    'owner': 'Doull',
    'depends_on_past': False,
    # 'start_date': airflow.utils.dates.days_ago(1),
    'start_date': datetime(2021,12,23),
    'email': ['xxx@163.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
    'queue': 'bash_queue',
}

# -------------------------------------------------------------------------------
# dag
dag = DAG(
    dag_id='demo',
    default_args=default_args,
    schedule_interval="0 22 * * 5",
    description='data updating')

# -------------------------------------------------------------------------------
# 添加上游依赖 --
pre_depend = ExternalTaskSensor(
    task_id='up-dependent-pre_demo',
    external_dag_id='pre_demo',
    external_task_id='end',
    trigger_rule='all_done',
    dag=dag
)


start = DummyOperator(
    task_id='start',
    dag=dag
)


end = DummyOperator(
    task_id='end',
    dag=dag
)

# -------------------------------------------------------------------------------

demo = SSHOperator(
    task_id="demo",
    ssh_conn_id="ssh_conn",
    command="kinit -kt /tmp/supergroup.keytab supergroup;bash /home/demo.sh ",
    dag=dag
)

pre_depend >> start

start >> demo >> end