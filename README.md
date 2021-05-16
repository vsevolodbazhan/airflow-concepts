# Airflow Concepts

Concepts and patterns for [Apache Airflow](https://airflow.apache.org) custom entities.

## Operator Interfaces

### `ETLOperator`

`ETLOperator` is the interface that aims to standardize the approach to creating operators for ETL jobs.

![UML diagram for `ETLOperator` interface.](sources/diagrams/operators/interfaces/etl_operator.png)

## Abstract Operators

### `PandasETLOperator`

`PandasETLOperator` is the abstract operator that partially implements the `ETLOperator` interface by implementing `transform` method, leaving up to the user to implement `extract` and `load` methods.

![UML diagram for `PandasETLOperator` abstract operator.](sources/diagrams/operators/pandas/pandas_etl_operator.png)
