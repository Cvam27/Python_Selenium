def customColumn(column_id :int):
    column = f'[id="resultTable"] tr > td:nth-child({column_id})'
    return column


class Locators:
    table = '[id="resultTable"]'