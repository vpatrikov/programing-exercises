def generate_hashtag(s):
    if not s or len(s.strip()) == 0:
        return False
    words = s.split()
    capitalized_words = [word.capitalize() for word in words]
    hashtag = '#' + ''.join(capitalized_words)
    return hashtag if len(hashtag) <= 140 else False