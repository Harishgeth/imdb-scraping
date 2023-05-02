import scrapy

class MoviesSpider(scrapy.Spider):
    name = "movies"
    start_urls = ["https://www.imdb.com/chart/top"]

    def parse(self, response):
        for row in response.css("tbody.lister-list tr"):
            title = row.css("td.titleColumn a::text").get().strip()
            year = row.css("td.titleColumn span.secondaryInfo::text").get().strip("()")

            rating = row.css("td.ratingColumn strong::text").get().strip()
            ratings_count = row.css("td.ratingColumn span[name='ir']::text").get()

            if ratings_count is not None:
                ratings_count = ratings_count.strip()
            else:
                ratings_count = "0"

            movie_url = row.css("td.titleColumn a::attr(href)").get()
            movie_id = movie_url.split("/")[-2]

            if not movie_url.startswith("http"):
                movie_url = "http://www.imdb.com" + movie_url

            yield scrapy.Request(
                movie_url,
                callback=self.parse_movie,
                meta={
                    "movie_id": movie_id,
                    "title": title,
                    "year": year,
                    "rating": rating,
                    "ratings_count": ratings_count,
                },
            )

    def parse_movie(self, response):
        movie_id = response.meta["movie_id"]
        title = response.meta["title"]
        year = response.meta["year"]
        rating = response.meta["rating"]
        ratings_count = response.meta["ratings_count"]

        categories = response.css("div.subtext a:not(:last-child)::text").getall()
        actors = response.css("div.credit_summary_item span.itemprop::text").getall()
        description = response.css("div.summary_text::text").get().strip()
        image = response.css("div.poster img::attr(src)").get()

        movie_data = {
            "movie_id": movie_id,
            "title": title,
            "year": year,
            "rating": rating,
            "ratings_count": ratings_count,
            "categories": categories,
            "actors": actors,
            "description": description,
            "image": image,
            "current_recommended_rate": 0.0,
        }

        yield movie_data
