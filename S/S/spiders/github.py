import scrapy


class GithubSpider(scrapy.Spider):
    name = 'github'
    start_urls = [
        'https://github.com/login'
    ]

    def parse(self, response, **kwargs):
        data = {'login': '', 'password': ''}

        return scrapy.FormRequest.form_response(response,
                                                url='https://github.com/session',
                                                formdata=data,
                                                callback=self.after_login)

    def after_login(self, response):
        yield response.follow('https://github.com/username', self.profile)

    def profile(self, response):
        yield {'info': response.css('.p-label').get()}
