# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TennisItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    player_name = scrapy.Field()
    rank = scrapy.Field()
    first_serve = scrapy.Field()
    ace = scrapy.Field()
    double_fault = scrapy.Field()
    first_serve_points_won = scrapy.Field()
    second_serve_points_won = scrapy.Field()
    break_points_saved = scrapy.Field()
    service_games_won = scrapy.Field()
    total_service_points_won = scrapy.Field()
    first_serve_return_points_won = scrapy.Field()
    second_serve_return_points_won = scrapy.Field()
    break_points_converted = scrapy.Field()
    return_games_won = scrapy.Field()
    return_points_won = scrapy.Field()
    total_points_won = scrapy.Field()
    games_won = scrapy.Field()
    sets_won = scrapy.Field()
    matches_won = scrapy.Field()