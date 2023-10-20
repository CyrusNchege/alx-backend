#!/usr/bin/env python3
"""  Simple helper function """


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of start and end indexes for a given pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end indexes (0-indexed).
    """
    if page <= 1:
        start = 0
    else:
        start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
