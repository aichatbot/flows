from prefect import flow, task, get_run_logger

@task(log_prints=True)
def add_task(x: int, y: int) -> int:
    result = x + y
    return result

@flow(log_prints=True)
def my_minio_flow(a: int, b: int):
    result = add_task(x=a, y=b)
    print(f"Task 'add_task' is: {result}")
    return result

if __name__ == "__main__":
    my_minio_flow(3,2)
