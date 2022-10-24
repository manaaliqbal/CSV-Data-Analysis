"""Dictionary related utility functions."""

__author__ = "730400691"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column_name: str) -> list[str]:
    """Produce a list[str] of all values in a single column whose name is in the second parameter."""
    result: list[str] = []

    for row in table:
        column_value: str = row[column_name]
        result.append(column_value)

    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table represented as a list of rows into one represented as a dictionary of columns."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = table[0]
    for column_name in first_row:
        result[column_name] = column_values(table, column_name)

    return result


def head(column_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column based table with only the first n rows of data for each column."""
    result: dict[str, list[str]] = {}

    for column in column_table:
        if n >= len(column_table[column]):
            return column_table
        number_of_entries: int = 0
        column_list: list[str] = []
        while number_of_entries < n:
            column_list.append(column_table[column][number_of_entries])
            number_of_entries += 1
        
        result[column] = column_list  

    return result


def select(column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}

    for name in column_names:
        column_list: list[str] = []
        if name in column_table: 
            for item in column_table[name]:
                column_list.append(item)
        result[name] = column_list

    return result 


def concat(column_table_one: dict[str, list[str]], column_table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}

    for column_one in column_table_one:
        column_list_one: list[str] = []
        for item_one in column_table_one[column_one]:
            column_list_one.append(item_one)
        result[column_one] = column_list_one

    for column_two in column_table_two:
        column_list_two: list[str] = []
        for item_two in column_table_two[column_two]:
            column_list_two.append(item_two)
        if column_two in result:
            result[column_two] += column_list_two
        else:
            result[column_two] = column_list_two

    return result 


def count(values: list[str]) -> dict[str, int]:
    """Given a list, will produce a dictionary where aech key is a unique value in the given list and each value is the count of how many times that appears."""
    result: dict[str, int] = {}

    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result