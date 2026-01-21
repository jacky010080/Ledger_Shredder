"""
Utility for formatting tables with borders and aligned columns.
"""

def format_table(rows, headers):
    """
    Return a formatted table string with borders and aligned columns.
    """

    num_cols = len(headers)

    # Compute column widths
    col_widths = []
    for col in range(num_cols):
        max_width = len(headers[col])
        for row in rows:
            max_width = max(max_width, len(str(row[col])))
        col_widths.append(max_width)

    # Borders
    top_border = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"
    header_border = top_border

    # Header row
    header_cells = []
    for i in range(num_cols):
        header_cells.append(" " + headers[i].ljust(col_widths[i]) + " ")
    header_line = "|" + "|".join(header_cells) + "|"

    # Data rows
    data_lines = []
    for row in rows:
        row_cells = []
        for i in range(num_cols):
            value = str(row[i])

            if headers[i] in ("Amount", "Total"):
                value = value.rjust(col_widths[i])
            else:
                value = value.ljust(col_widths[i])

            row_cells.append(" " + value + " ")

        data_lines.append("|" + "|".join(row_cells) + "|")

    return "\n".join([top_border, header_line, header_border] + data_lines + [top_border])