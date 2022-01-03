import tweepy
import datetime
import time
import apikey2
import requests

while True:
    try:
        year=datetime.datetime.now().year
        month=datetime.datetime.now().month
        day=datetime.datetime.now().day
        full_date=str("{:}".format(year)+"-"+"{:}".format(month)+"-"+"{:}".format(day-1))
        today = datetime.date.today()
        today1 = str(today)
        url=f'https://api.nasa.gov/neo/rest/v1/feed?start_date={full_date}&end_date={today}&api_key={apikey2.key}'
        json=requests.get(url).json()
        # print(json)
        no_of=json['element_count']
        name=json['near_earth_objects'][today1][0]['name']
        size=json['near_earth_objects'][today1][0]['estimated_diameter']['kilometers']['estimated_diameter_max']
        date=json['near_earth_objects'][today1][0]['close_approach_data'][0]['close_approach_date_full']
        velocity=json['near_earth_objects'][today1][0]['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']
        orbit=json['near_earth_objects'][today1][0]['close_approach_data'][0]['orbiting_body']
        missing=json['near_earth_objects'][today1][0]['close_approach_data'][0]['miss_distance']['kilometers']


        fulltw=str("{:}".format(no_of)+" Asteroids approaching earth on ")+str("{:}".format(date)+". One of them is ")+str("{:}".format(name)+" of maximum diameter ")+str("{:.2}".format(size)+" KM with a velocity of ")+str("{:.7}".format(velocity)+" KM/h, missing earth with ")+str("{:.10}".format(missing)+" KMs, Orbiting ")+str("{:}".format(orbit)+".")
        # print(fulltw)
        api_key=apikey2.API_KEY
        api_key_secret=apikey2.API_KEY_SECRET
        access_token=apikey2.ACCESS_TOKEN
        access_token_secret=apikey2.ACCESS_TOKEN_SECRET

        auth= tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)

        api=tweepy.API(auth)

        api.update_status(fulltw+"\n"+ str(datetime.datetime.now()))
        print("Tweet sent...")
    except:
        print("Some error occured!!!")
    time.sleep(1600)