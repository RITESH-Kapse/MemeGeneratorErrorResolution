from typing import List

from QuoteEngine import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Class to parse .txt files """
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file at the given path and return QuoteModel objects"""
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest exception")

        file = open(path, "r")
        quotes = []

        for line in file.readlines():
            line = line.strip('\n\r').strip()
            line_length = len(line)
            if line_length > 0:
                parsed_line = line.split(' - ')
                new_quote = QuoteModel(parsed_line[0], parsed_line[1])
                quotes.append(new_quote)

        file.close()
        return quotes