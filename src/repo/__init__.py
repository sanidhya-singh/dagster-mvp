from dagster import Definitions
from repo.jobs import mvp_job


DagsterMVP = Definitions(
    jobs = [mvp_job]
)