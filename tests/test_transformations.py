from pyspark.sql import SparkSession
from framework.transformation_engine import apply_transformations

spark = (
    SparkSession.builder
    .master("local[*]")
    .appName("test")
    .getOrCreate()
)

def test_filter():

    data = [
        (1, "John", 40000),
        (2, "Mary", 80000)
    ]

    df = spark.createDataFrame(
        data,
        ["id", "name", "salary"]
    )

    transformations = [
        {
            "type": "filter",
            "condition": "salary > 50000"
        }
    ]

    result = apply_transformations(
        df,
        transformations
    )

    assert result.count() == 1