from airflow.decorators import dag, task
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

@dag(
    schedule=None,
    catchup=False
)

def my_dag():

    read_data = SparkSubmitOperator(
        task_id="read_data",
        application="./include/scripts/read.py",
        conn_id="spark_conn",
        verbose=True
    )

    read_data

my_dag()