import scrapy
import csv

# from scrapy.crawler import CrawlerProcess

# import os

# dirname = os.path.dirname(__file__)
# POSTS_FILE = os.path.join(dirname, '../../posts.csv')

POSTS_FILE = 'posts.csv'


def load_post_urls():
    with open(POSTS_FILE, mode='r') as csv_file:
        urls = [r['url'] for r in csv.DictReader(csv_file)]
    return urls


class ZippySpider(scrapy.Spider):
    name = "posts"
    # start_urls = load_post_urls()[:1]
    start_urls = load_post_urls()

    def parse(self, response):
        yield {
            'title': response.css('.entry-title::text').extract_first(),
            'date': response.css('p.date::text').extract_first(),
            'content': response.css('div.entry p').extract_first(),
            'comments': [self.parse_comment(comment) for comment in response.css('ul.commentlist li')]
        }

    @staticmethod
    def parse_comment(selector):
        comment = selector.css('li div')
        return {
            'author': comment.css('div.comment-author cite::text').extract_first(),
            'date': comment.css('div.comment-meta a::text').extract_first().strip(),
            'content': comment.css('p::text').extract()
        }

# process = CrawlerProcess({
#     'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
# })
#
# process.crawl(ZippySpider)
# process.start()  # the script will block here until the crawling is finished
