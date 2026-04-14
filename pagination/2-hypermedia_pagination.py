#!/usr/bin/env python3
"""
Simple Pagination module
Contains Server Class- with methods: dataset(), index_range() and get_page()
"""

import csv
import math
from typing import Any, Dict, List, Tuple, TypedDict


class HyperReponse(TypedDict):
    page_size: int
    page: int
    data: List[List]
    next_page: int | None
    prev_page: int | None
    total_pages: int


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        Parameters: page and page_size
        Return: tuple of (start index, end index)
        """
        # pages are 1-indexed but data is 0-indexed so page - 1
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Parameters: page and page_size
        Return: appropriate page of the dataset e.g correct list of rows
        """
        assert (isinstance(page, int) and page > 0)
        assert (isinstance(page_size, int) and page_size > 0)

        data = self.dataset()

        start, end = self.index_range(page, page_size)

        if start >= len(data):
            return []

        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> HyperReponse:
        """
        Parameters: page and page_size
        Return: appropriate page of the dataset e.g correct list of rows
        """
        returned_data = self.get_page(page, page_size)

        data = self.dataset()
        data_length = len(data)
        total_pages = math.ceil(data_length / page_size)
        start, end = self.index_range(page, page_size)

        if page == 1:
            prev_page = None
        else:
            prev_page = page - 1

        if end >= total_pages:
            next_page = None
        else:
            next_page = page + 1

        return {
            'page_size': len(returned_data),
            'page': page,
            'data': returned_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
