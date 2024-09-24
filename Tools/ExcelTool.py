import pandas as pd


def get_sheet_names(
        filename: str
) -> str:
    """Get the sheet names of an Excel file"""
    excel_file = pd.ExcelFile(filename)
    sheet_names = excel_file.sheet_names
    return f"These are the sheet names of the file '{filename}':\n\n{sheet_names}"


def get_column_names(
        filename: str
) -> str:
    """Get the column names of an Excel file"""

    df = pd.read_excel(filename, sheet_name=0)  # Read the first sheet

    column_names = '\n'.join(
        df.columns.to_list()
    )

    result = f"These are the column names of the first sheet in the file '{filename}':\n\n{column_names}"
    return result


def get_first_n_rows(
        filename: str,
        n: int = 3
) -> str:
    """Get the first n rows of an Excel file"""

    result = get_sheet_names(filename) + "\n\n"

    result += get_column_names(filename) + "\n\n"

    df = pd.read_excel(filename, sheet_name=0)  # Read the first sheet

    n_lines = '\n'.join(
        df.head(n).to_string(index=False, header=True).split('\n')
    )

    result += f"Here are the first {n} rows of the first sheet in the file '{filename}':\n\n{n_lines}"
    return result
