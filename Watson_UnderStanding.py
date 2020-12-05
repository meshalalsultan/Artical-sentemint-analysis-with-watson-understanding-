import json
from io import BytesIO
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions



authenticator = IAMAuthenticator('{apikey}')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2020-08-01',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('{url}')

response = natural_language_understanding.analyze(
    url='https://www.bloomberg.com/news/articles/2020-12-03/asia-stocks-set-to-slip-dollar-extends-decline-markets-wrap?srnd=premium-middle-east',
    features = Features(keywords=KeywordsOptions(
        sentiment=True,
        emotion=True,
        limit=2))).get_result()

print(json.dumps(response, indent=2))

txt_char = response['usage']['text_characters']
print(f'The Text Character is : {txt_char}')

for t in response['keywords']:
    text=t['text']
    print(f'The Text is : {text}')
    sentiments = t['sentiment']['label']
    print (f'The Sentemint is : {sentiments}')
    scores = t['sentiment']['score']
    print(f'The Score is : {scores}')
    #The Feeling 
    joy = t['emotion']['joy']
    sadness = t['emotion']['sadness']
    fear = t['emotion']['fear']
    disgust = t['emotion']['disgust']
    anger = t['emotion']['anger']
    print(f'The Joy is : {joy}')
    print(f'The Sadness is : {sadness}')
    print(f'The Fear is : {fear}')
    print(f'The Disgust is : {disgust}')
    print(f'The Anger is : {anger}')

# Now i finish featching the sentmint and emotion from url by watson 