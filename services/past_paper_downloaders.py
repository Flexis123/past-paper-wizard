from blueprints import PastPaperDto
from services import PastPaperDownloader
from requests import get


class PapaCambridgeDownloader(PastPaperDownloader):
    def download_past_papers(self, paper: PastPaperDto):
        pass


class XTremePapersDownloader(PastPaperDownloader):
    def download_past_papers(self, paper: PastPaperDto):
        pass

