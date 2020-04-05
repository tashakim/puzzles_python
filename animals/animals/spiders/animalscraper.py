import scrapy

class Spider(scrapy.Spider):
	name = "animal_spider"
	url = ["https://www.reddit.com/r/animal/"]

	def parse(self, response):
		links = response.xpath("//img/@src")
		html = ""

		for link in links:
			url = link.get()

			if any(extension in url for extension in [".jpg"]):
				html += """<a href = "{url}"
				target = "_blank">
				<img src="{url}" height = "33%"
				width = "33%">
				<a/>""".format(url = url)

				with open("animal_images.html", "a") as page:
					page.write(html)
					page.close()