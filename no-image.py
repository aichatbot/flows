from prefect import flow

@flow(log_prints=True)
def hello_world(name: str):
    print(f"Hello!")

if __name__ == "__main__":
    flow.from_source(
        "https://github.com/aichatbot/brain.git",
        entrypoint="flows/no-image.py:hello_world",
    ).deploy(
        name="no-image-deployment",
        work_pool_name="my-docker-pool",
        build=False
    )
