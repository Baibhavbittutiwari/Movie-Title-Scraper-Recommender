import scrapy
import pandas as pd

class MovieSpider(scrapy.Spider):
    name = 'moviespider'
    start_urls = ['https://www.rottentomatoes.com/browse/movies_at_home/sort:popular?page=1']
    page_limit = 5
    current_page = 1
    all_movies = []

    def parse(self, response):
        # Extract data from the response using XPath or CSS selectors
        movie = response.css('.p--small::text').extract()
        movie_titles = [] 
        for i in movie:
            movie_titles.append(i.strip())
        self.all_movies.extend(movie_titles)

        # Process the extracted data and yield items
        items = {'movies': self.all_movies}
        data = pd.DataFrame(items)
        data.to_csv('Movies.csv', index=False)

        yield items

        # Follow the next page if the page limit is not reached
        if self.current_page < self.page_limit:
            self.current_page += 1
            next_page_url = f"https://www.rottentomatoes.com/browse/movies_at_home/sort:popular?page={self.current_page}"
            yield response.follow(next_page_url, self.parse)