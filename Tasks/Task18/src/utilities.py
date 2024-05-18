from datetime import datetime
import textwrap


def format_date(date):
    # Parses the input date string into a datetime object
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    # Formats the datetime object into a string like "Month Day, Year"
    formatted_date = date_obj.strftime('%B %d, %Y')
    return formatted_date


def format_string(input, width=35):
    # wraps the in put once max character width has reached
    wrapped_input = textwrap.fill(input, width)
    return wrapped_input
