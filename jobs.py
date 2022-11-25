import urllib
import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from scrapfly import ScrapflyClient, ScrapeConfig
import pandas as pd
import os


class JobScraper:
    def __init__(self, query, location="United States", age="1") -> None:
        self.base_url = "https://www.indeed.com/jobs?"
        self.scrape_config = self._generate_scrape_config(query=query, location=location, age=age)
        self.scraper = self._get_scrapfly_client()
        
        
    def _generate_scrape_config(self, query, location, age):
        params = {
            'q' : query,
            'l' : "+".join(location.split(" ")),
            'fromage' : age
        }
        url = (self.base_url) + urllib.parse.urlencode(params)

        return ScrapeConfig(url=url, asp=True)

    def _get_scraper(self, content):
        return BeautifulSoup(content, "html.parser")

    def _get_scrapfly_client(self):
        return ScrapflyClient(key="scp-live-673d1c9dee8c4357b86c1a0a69b5f591")

    def load_content(self):

        page = self.scraper.scrape(scrape_config=self.scrape_config)
        print(page)
        # Seeing 403 Response code (Forbidden)
        self.parser = self._get_scraper(content=page)



jobs = JobScraper(query="data")

jobs.load_content()


    

