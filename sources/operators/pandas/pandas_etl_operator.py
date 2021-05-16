from typing import Callable, Dict, Optional

import pandas as pd
from airflow.models.baseoperator import BaseOperator

from sources.operators.interfaces.etl_operator import ETLOperator


class PandasETLOperator(ETLOperator, BaseOperator):
    """Abstract operator based on `pandas.DataFrame` that
    helps to implement operators that perform ETL jobs.

    Parameters
    ----------
    transformation_callable : Optional[Callable]
        Callable that is used to transform extracted data before performing loading.
        **Must** accept `pandas.DataFrame` as its first argument.
    transformation_kwargs : Optional[Dict]
        Keyword arguments that are being passed to `transformation_callable`.
    """

    def __init__(
        self,
        transformation_callable: Optional[Callable],
        transformation_kwargs: Optional[Dict],
        *args,
        **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)

        self._transformation_callable = transformation_callable
        self._transformation_kwargs = transformation_kwargs or {}

    def execute(self, context: Dict) -> None:
        data = self.extract()
        data = self.transform(data=data)
        self.load(data=data)

    def extract(self) -> pd.DataFrame:
        raise NotImplementedError()

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        if self._transformation_callable:
            return self._transformation_callable(data, **self._transformation_kwargs)
        return data

    def load(self, data: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError()
