import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


def checkpoint(message="Does this make sense?"):
    check_it = input(message)


def gr(number):
    golden_ratio = 1.618033988749
    golden_ratio_number = round(number * golden_ratio)
    return golden_ratio_number


wc_height = 900
wc_width = gr(wc_height)
plt_height = wc_height/100
plt_width = gr(plt_height)

filename = "MuchAdoAboutNothing.txt"  # Complete text of Much Ado About Nothing
much_ado_about_nothing = open(filename).read()
words_to_ignore = ['the', 'of', 'and', 'is','to','in','a','from','by','that', 'with', 'this', 'as', 'an', 'are','its', 'at', 'for', 'you', 'her', 'me', 'I', 'it', 'not']
wordcloud = WordCloud(width=wc_width, height=wc_height, stopwords=words_to_ignore, min_font_size=1).generate(much_ado_about_nothing)

plt.figure(figsize=(plt_width, plt_height), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()
