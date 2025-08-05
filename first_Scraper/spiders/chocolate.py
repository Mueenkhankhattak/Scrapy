import scrapy

class ChocolateSpider(scrapy.Spider):
    name = "chocolate"
    allowed_domains = ["chocolate.co.uk"]
    start_urls = ["https://www.chocolate.co.uk/collections/luxury-chocolate-bars"]

    def parse(self, response):
        products = response.css(".product-item")  # List of product blocks

        for product in products:
            title = product.css(".product-item-meta__title::text").get()
            price = product.css(".visually-hidden::text").get()

            # Optional: strip whitespace if not None
            if title:
                title = title.strip()
            if price:
                price = price.strip()

            yield {
                "title": title,
                "price": price
            }
