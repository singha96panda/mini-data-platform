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

    return df