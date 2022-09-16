from dagster import job
from repo.ops import (
    sum_numbers, random_number,
    populate_asset
)


@job(metadata={"owner": "Sanidhya Singh"})
def mvp_job():
    """
    This job is an MVP for Dagster
    """
    populate_asset(
        sum_numbers(
            random_number(),
            random_number()
        )
    )