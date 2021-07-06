from QuoteEngine.PDFImporter import PDFImporter
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxImporter import DocxImporter
from .CSVImporter import CSVImporter
from .PDFImporter import PDFImporter
from .TextIngestor import TextIngestor

class Ingestor(IngestorInterface):
    Ingestors = [DocxImporter, CSVImporter, PDFImporter, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for Ingestor in cls.Ingestors:
            if Ingestor.can_ingest(path):
                return Ingestor.parse(path)