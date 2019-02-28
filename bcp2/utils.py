from math import ceil


def calculate_total_of_pages(total, number_of_items_per_page):
    return int(ceil(float(total) / float(number_of_items_per_page)))
