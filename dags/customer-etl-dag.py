from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="customer_etl",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    run_customer_etl = BashOperator(
        task_id="run_customer_etl",
        bash_command="""
        python -m jobs.spark_job configs/customer_etl.yaml
        """
    )