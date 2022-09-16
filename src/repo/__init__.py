from dagster import repository
from repo.jobs import mvp_job


@repository
def DagsterMVP():
    return [mvp_job]