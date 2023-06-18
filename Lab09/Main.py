import wikipediaapi


def read_titles(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()


def get_article(title):
    w_api = wikipediaapi.Wikipedia('en')
    page = w_api.page(title)
    if page.exists():
        return page.text
    else:
        return ""

def calculate_average_letter_count():
    title_generator = read_titles("small.txt")
    total_letter_count = 0
    article_count = 0

    for title in title_generator:
        article = get_article(title)
        letter_count = len([letter for letter in article if letter.isalpha()])
        total_letter_count += letter_count
        article_count += 1

    if article_count > 0:
        average_letter_count = total_letter_count / article_count
        yield average_letter_count
    else:
        yield 0


average_letter_generator = calculate_average_letter_count()
average_letter_count = next(average_letter_generator)
print("Average number of distinct letters per article:", average_letter_count)
