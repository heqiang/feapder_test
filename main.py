import feapder
from feapder import Request, Response


class TestFeapder(feapder.AirSpider):

    def start_requests(self):
        url = "https://www.baidu.com/"
        yield feapder.Request(url=url, callback=self.parse)

    def parse(self, request: Request, response: Response):
        print(response.xpath('//title/text()').extract_first())
        print(response.xpath('//meta[@name="description"]/@content').extract_first())


if __name__ == '__main__':
    TestFeapder(thread_count=1).start()
