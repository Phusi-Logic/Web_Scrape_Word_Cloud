import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


def gr(number):
    golden_ratio = 1.618033988749
    golden_ratio_number = round(number * golden_ratio)
    return golden_ratio_number


def get_soup(url):
    from bs4 import BeautifulSoup
    import requests
    print(" ")
    print("retreiving html from:    ", url)  # Prints it to check it's right
    clean_url = url.strip()  # Strips the leading and trailing spaces from the string
    source = requests.get(clean_url, headers={'User-Agent': 'Mozilla/5.0'}).content
    got_soup = BeautifulSoup(source, 'html.parser')
    return got_soup


text = get_soup("url").get_text()  # replace "url" with your own url
print(text)


wc_height = 900
wc_width = gr(wc_height)
plt_height = wc_height/100
plt_width = gr(plt_height)
words_to_ignore = ['the', 'of', 'and', 'is','to','in','a','from','by','that', 'with', 'this', 'as', 'an', 'are','its', 'at', 'for', 'you', 'her', 'me', 'I', 'it', 'not']
wordcloud = WordCloud(width=wc_width, height=wc_height, stopwords=words_to_ignore, min_font_size=1, max_words=1000).generate(text)
plt.figure(figsize=(plt_width, plt_height), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()
