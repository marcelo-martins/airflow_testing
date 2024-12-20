from airflow.decorators import dag, task
from pyspark import SparkContext
from pyspark.sql import SparkSession
import pandas as pd

@dag(
    schedule=None,
    catchup=False
)

def my_dag2():
    
    @task.pyspark(conn_id="spark_conn")
    def read_data(spark:SparkSession, sc:SparkContext):

        df = spark.read.csv("./include/data.csv", header="true")
        df.show()

    read_data()


my_dag2()