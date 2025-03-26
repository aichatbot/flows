from prefect import flow

@flow
def hello_world(name: str):
    print(f"Hello!")

if __name__ == "__main__":
    flow.from_source(
        "https://github.com/aichatbot/flows.git",
        entrypoint="no-image.py:hello_world",
    ).deploy(
        name="no-image-deployment",
        work_pool_name="my-docker-pool",
        build=False
    )
