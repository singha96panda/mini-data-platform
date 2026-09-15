from pyspark.sql import SparkSession
from framework.yaml_parser import load_config
from framework.transformation_engine import apply_transformations

config = load_config("configs/employee_etl.yaml")

spark = (
    SparkSession.builder
    .appName("EmployeeETL")
    .getOrCreate()
)

df = spark.read.csv(
    config["source"]["file"],
    header=True,
    inferSchema=True
)

df = apply_transformations(
    df,
    config["transformations"]
)

target_path = config["target"]["file"]

### df.write.mode("overwrite").csv(
###    target_path,
###    header=True
###)

df.show()

spark.stop()