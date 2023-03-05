#!/usr/bin/env python

from epa.envirofacts import Envirofacts

from .table_lookup import table_lookup
from .table_column_lookup import table_column_lookup
from .column_table_lookup import column_table_lookup


class TRI(Envirofacts):
    """Python wrapper for the EPA's TRI API."""

    def __init__(self):
        super(TRI, self).__init__()
        self.table_lookup = table_lookup
        self.table_column_lookup = table_column_lookup
        self.column_table_lookup = column_table_lookup

    def tri_query(self, table_lst, column=None, value=None, **kwargs):
        """
        General-purpose TRI query function allowing queries on 1-3 tables.
        """
        if not table_lst or len(table_lst) > 3:
            raise ValueError("table_lst must contain 1-3 table names")
        return self._resolve_call(table_lst, column, value, **kwargs)
