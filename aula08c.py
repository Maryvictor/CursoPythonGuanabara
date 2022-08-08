import emoji

print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize('Oie! :sunglasses:', language='alias', variant="emoji_type"))
print(emoji.emojize("Python is fun :red_heart:", variant="text_type"))
print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
print(emoji.emojize("Python is fun __thumbs_up__", delimiters = ("__", "__")))

