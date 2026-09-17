from pyspark.sql.functions import (
    expr,
    sum,
    avg,
    count,
    max,
    min
)


def apply_transformations(df, transformations):

    for transformation in transformations:

        if transformation["type"] == "filter":
            df = df.filter(
                transformation["condition"]
            )

        elif transformation["type"] == "select":
            df = df.select(
                *transformation["columns"]
            )

        elif transformation["type"] == "rename":
            df = df.withColumnRenamed(
                transformation["old_name"],
                transformation["new_name"]
            )

        elif transformation["type"] == "drop":
            df = df.drop(
                *transformation["columns"]
            )

        elif transformation["type"] == "derive":
            df = df.withColumn(
                transformation["column"],
                expr(transformation["expression"])
            )

        elif transformation["type"] == "deduplicate":
            df = df.dropDuplicates()

        elif transformation["type"] == "aggregate":

            group_cols = transformation["group_by"]

            agg_exprs = []

            for agg in transformation["aggregations"]:

                col_name = agg["column"]
                func_name = agg["function"]
                alias = agg["alias"]

                if func_name == "sum":
                    agg_exprs.append(
                        sum(col_name).alias(alias)
                    )

                elif func_name == "avg":
                    agg_exprs.append(
                        avg(col_name).alias(alias)
                    )

                elif func_name == "count":
                    agg_exprs.append(
                        count(col_name).alias(alias)
                    )

                elif func_name == "max":
                    agg_exprs.append(
                        max(col_name).alias(alias)
                    )

                elif func_name == "min":
                    agg_exprs.append(
                        min(col_name).alias(alias)
                    )

            df = df.groupBy(*group_cols).agg(*agg_exprs)

    return df