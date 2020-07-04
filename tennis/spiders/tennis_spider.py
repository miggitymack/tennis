from scrapy import Spider, Request
from tennis.items import TennisItem
import json


class TennisSpider(Spider):
    name = "tennis_spider"
    allowed_urls = ['https://www.atptour.com']
    start_urls = [
        'https://www.ultimatetennisstatistics.com/rankingsTableTable?current=1&rowCount=500&sort%5Brank%5D=asc&searchPhrase=&rankType=RANK&season=&date=&_=1593701140932'
    ]

    def parse(self, response):
        player_rows = json.loads(
            response.xpath('//body//p/text()').extract()[0])['rows']
        result_urls = []
        player_id = []
        player_name = []

        for player in player_rows:
            result_urls.append('https://www.ultimatetennisstatistics.com/playerProfileTab?playerId={}'
                .format(player['playerId']))
            player_id.append(player['playerId'])
            player_name.append(player['name'])


        for i, url in enumerate(result_urls):
            yield Request(url=url, callback=self.parse_player_profile_page, meta={'player_id': player_id[i], 'player_name': player_name[i]})

    def parse_player_profile_page(self, response):
        print(response.meta['player_id'], response.meta['player_name'])
        # rank = response.xpath(
        #     '//table[@class="table table-condensed text-nowrap"][1]//td/text()'
        # )[23].extract().split(' ')[0]
        # for player in player_rows:
        #     player_name = player['name']
        # for url in result_urls:
        #     yield Request(url=url,
        #                   meta={'player_name': player_name},
        #                   callback=self.parse_player_profile_page)

    # def parse_player_stats_page(self, response):
    #     result_urls = [
    #         'https://www.ultimatetennisstatistics.com/playerStatsTab?playerId={}'
    #         .format(player['playerId']) for player in player_rows
    #     ]
    #     player_name = response.meta['player_name']
    #     try:
    #         ace = float(
    #             response.xpath(
    #                 '//div[@id="statisticsOverview"]//table//tr//th[1]//text()'
    #             ).extract()[1][:-1])
    #         double_fault = float(
    #             response.xpath(
    #                 '//div[@id="statisticsOverview"]//table//tr//th[1]//text()'
    #             ).extract()[2][:-1])
    #         first_serve = float(
    #             response.xpath(
    #                 '//div[@id="statisticsOverview"]//table//tr//th[1]//text()'
    #             ).extract()[3][:-1])
    #         first_serve_points_won = float(
    #             response.xpath(
    #                 '//div[@id="statisticsOverview"]//table//tr//th[1]//text()'
    #             ).extract()[4][:-1])
    #         second_serve_points_won = float(
    #             response.xpath(
    #                 '//div[@id="statisticsOverview"]//table//tr//th[1]//text()'
    #             ).extract()[5][:-1])
    #         break_points_saved = float(
    #             response.xpath(
    #                 '//div[@id="statisticsOverview"]//table//tr//th[1]//text()'
    #             ).extract()[6][:-1])
    #         service_games_won = float(
    #             response.xpath(
    #                 '//div[@id="statisticsOverview"]//table//tr//th[1]//text()'
    #             ).extract()[7][:-1])
    #         total_service_points_won = float(
    #             response.xpath(
    #                 '//div[@id="statisticsOverview"]//table//tr//th[1]//text()'
    #             ).extract()[8][:-1])
    #         first_serve_return_points_won = float(
    #             response.xpath(
    #                 '//div[@id="statisticsOverview"]//table//tr//th[1]//text()'
    #             ).extract()[11][:-1])
    #         second_serve_return_points_won = float(
    #             response.xpath(
    #                 '//div[@id="statisticsOverview"]//table//tr//th[1]//text()'
    #             ).extract()[12][:-1])
    #         break_points_converted = float(
    #             response.xpath(
    #                 '//div[@id="statisticsOverview"]//table//tr//th[1]//text()'
    #             ).extract()[13][:-1])
    #         return_points_won = float(
    #             response.xpath(
    #                 '//div[@id="statisticsOverview"]//table//tr//th[1]//text()'
    #             ).extract()[14][:-1])
    #         return_games_won = float(
    #             response.xpath(
    #                 '//div[@id="statisticsOverview"]//table//tr//th[1]//text()'
    #             ).extract()[15][:-1])
    #         total_points_won = float(
    #             response.xpath(
    #                 '//div[@id="statisticsOverview"]//table//tr//th[1]//text()'
    #             ).extract()[19][:-1])
    #         games_won = float(
    #             response.xpath(
    #                 '//div[@id="statisticsOverview"]//table//tr//th[1]//text()'
    #             ).extract()[20][:-1])
    #         sets_won = float(
    #             response.xpath(
    #                 '//div[@id="statisticsOverview"]//table//tr//th[1]//text()'
    #             ).extract()[21][:-1])
    #         matches_won = float(
    #             response.xpath(
    #                 '//div[@id="statisticsOverview"]//table//tr//th[1]//text()'
    #             ).extract()[22][:-1])
    #     except:
    #         ace = double_fault = first_serve = first_serve_points_won = second_serve_points_won = break_points_saved = service_games_won = total_service_points_won = first_serve_return_points_won = second_serve_return_points_won = break_points_converted = return_points_won = return_games_won = total_points_won = games_won = sets_won = matches_won = 0

    #     item = TennisItem()
    #     item['player_name'] = player_name
    #     item['ace'] = ace
    #     item['double_fault'] = double_fault
    #     item['first_serve'] = first_serve
    #     item['first_serve_points_won'] = first_serve_points_won
    #     item['second_serve_points_won'] = second_serve_points_won
    #     item['break_points_saved'] = break_points_saved
    #     item['service_games_won'] = service_games_won
    #     item['total_service_points_won'] = total_service_points_won
    #     item['first_serve_return_points_won'] = first_serve_return_points_won
    #     item['second_serve_return_points_won'] = second_serve_return_points_won
    #     item['break_points_converted'] = break_points_converted
    #     item['return_points_won'] = return_points_won
    #     item['return_games_won'] = return_games_won
    #     item['total_points_won'] = total_points_won
    #     item['games_won'] = games_won
    #     item['sets_won'] = sets_won
    #     item['matches_won'] = matches_won

    #     yield item