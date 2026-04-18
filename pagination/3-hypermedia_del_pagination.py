#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get paginated data starting from index to index + page_size
        Increment offset by 1 for each None encountered to return correct data
        """
        indexed_dataset = self.indexed_dataset()

        assert (isinstance(index, int))
        assert (isinstance(page_size, int) and page_size > 0)

        assert 0 <= index < len(indexed_dataset)

        next_index = index
        dataset = []
        offset = 0

        for i in range(index, (index + page_size)):
            while (indexed_dataset.get(i + offset) is None):
                offset += 1
            dataset.append(indexed_dataset.get(i + offset))
            next_index += 1

        return {
            'index': index,
            'data': dataset,
            'page_size': page_size,
            'next_index': next_index + offset
        }
