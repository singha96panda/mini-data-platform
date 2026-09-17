from pyspark.sql import SparkSession
from framework.transformation_engine import apply_transformations

spark = (
    SparkSession.builder
    .master("local[*]")
    .appName("test")
    .getOrCreate()
)

def test_join():

    employee_data = [
        (1, "John", 10),
        (2, "Mary", 20)
    ]

    department_data = [
        (10, "Finance"),
        (20, "HR")
    ]

    employee_df = spark.createDataFrame(
        employee_data,
        ["id", "name", "dept_id"]
    )

    department_df = spark.createDataFrame(
        department_data,
        ["dept_id", "department"]
    )

    transformations = [
        {
            "type": "join",
            "right_df": department_df,
            "join_key": "dept_id",
            "join_type": "left"
        }
    ]

    result = apply_transformations(
        employee_df,
        transformations
    )

    assert result.count() == 2
    assert "department" in result.columns

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