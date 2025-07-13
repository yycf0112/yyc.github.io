from airflow.decorators import dag, task
from datetime import datetime


@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@monthly",
    catchup=False
)
def my_dag():
    
    @task
    def my_first_task():
        print("Hello from my first task!")
    
    my_first_task()
    
my_dag()
