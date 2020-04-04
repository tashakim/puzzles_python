#pip3 install icrawler
from icrawler.builtin import GoogleImageCrawler

keywords = ['cat', 'dog']
for keyword in keywords:
    google_crawler = GoogleImageCrawler(
        parser_threads=2,
        downloader_threads=4,
        storage={'root_dir': 'images/{}'.format(keyword)}
    
    )
    google_crawler.crawl(
        keyword=keyword, max_num=10, min_size=(200, 200))