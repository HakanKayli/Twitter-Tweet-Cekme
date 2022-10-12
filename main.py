
'''
     Hakan KAYLI
'''

import snscrape.modules.twitter as sntwitter
import psycopg2

#PostgreSql Veritabanı bağlantısı
db = psycopg2.connect(user = "postgres",
                      password = "98753",
                      host = "localhost",
                      port = "5433",
                      database = "twitter")
db.autocommit = True

imlec = db.cursor()

maxTweets = 100

#Twitterdan veri çekme                                    keyword               tarih aralığı
for i,tweet in enumerate(sntwitter.TwitterSearchScraper( 'havelsan + since:2020-01-01 until:2022-10-10').get_items()):
    if i>maxTweets:
        break
    '''
    print(i)
    print(tweet.user.username)
    print(tweet.content)
    print(tweet.date)
    print(tweet.user.location)
    print("\n")
    '''
    #Veritabanına ekleme işlemi
    imlec.execute('''INSERT INTO tweet(username, content, date,location) VALUES (%s, %s, %s, %s)''',(tweet.user.username, tweet.content, tweet.date, tweet.user.location))
    db.commit()

print("Veritabanına Kaydedildi")
db.close()

