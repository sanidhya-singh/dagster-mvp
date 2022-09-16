from dagster import op
from dagster import AssetMaterialization
import random


@op
def random_number(context) -> int:
    """
    This operation returns a random Integer
    between 0 & 10
    """
    number = random.randint(0, 10)
    return number


@op
def sum_numbers(context, input_1: int, input_2: int) -> int:
    """
    This operation sums two Integers given as input and returns the output
    """
    sum = input_1 + input_2
    context.log.info(sum)
    return sum


@op(out={})
def populate_asset(context, sum: int):
    """
    This operation materializes an Asset with the sum as Metadata
    """
    context.log_event(
        AssetMaterialization(
            asset_key="random_numbers_asset",
            metadata={
                "value": sum
            },
        )
    )
