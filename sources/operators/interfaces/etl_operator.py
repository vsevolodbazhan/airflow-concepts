from typing import Any


class ETLOperator:
    """
    Interface-only class that serves as a blueprint for
    implementing operators for ETL jobs.
    """

    def extract(self) -> Any:
        """Extract data from a source system.

        Returns
        -------
        Any
            Extracted data.
        """
        raise NotImplementedError()

    def transform(self, data: Any) -> Any:
        """Transform the data.

        Parameters
        ----------
        data : Any
            The data to transform.

        Returns
        -------
        Any
            Transformed data.
        """
        raise NotImplementedError()

    def load(self, data: Any) -> None:
        """Load the data to a target system.

        Parameters
        ----------
        data : Any
            The data to load.
        """
        raise NotImplementedError()
