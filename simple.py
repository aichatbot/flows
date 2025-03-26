from prefect import flow

@flow
def buy(log_prints=True):
    print("Buying securities")


if __name__ == "__main__":
    flow.from_source(
        "https://github.com/aichatbot/flows.git",
        entrypoint="simple.py:buy",
    ).deploy(
        name="no-image-deployment",
        work_pool_name="my-docker-pool",
        build=False
    )
