import pandas as pd
import random
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def generate_synthetic_data(num_samples=1000): #el data set
    data = []
    for _ in range(num_samples): #kol 7aga randomized 
        hour = random.randint(0, 23)  
        day = random.randint(0, 6)  
        day_of_year = random.randint(0, 364) 
        weather = random.choice([0, 1])  
        road_length = random.randint(1, 10)  
        traffic_speed = random.randint(30, 90) 
        traffic_lights = random.choice([0, 1])  
        event = random.choice([0, 1])  #de m3naha hal feh event haysbb za7ma wla la2
        #haytem el ta3deel 3la el hour w el day w el day of year w el weather 34an mykno4 randomized bal ykono data 7a2e2ea
        
       
        congestion = 0 #dah el mkdar el ba7sb mno hayb2a za7ma wla la2
        if (8 <= hour <= 9 or 17 <= hour <= 18):  
            congestion += 1
        if weather == 1:  
            congestion += 1
        if traffic_speed < 40:  
            congestion += 1
        if traffic_lights == 1:  
            congestion += 1
        if event == 1: 
            congestion += 1

        congestion = min(congestion, 2)
        
        data.append([hour, day, day_of_year, weather, road_length, traffic_speed, traffic_lights, event, congestion])

    return pd.DataFrame(data, columns=["hour", "day", "day_of_year", "weather", "road_length", "traffic_speed", "traffic_lights", "event", "congestion"])

df = generate_synthetic_data(1000)
df.head()

X = df[["hour", "day", "day_of_year", "weather", "road_length", "traffic_speed", "traffic_lights", "event"]]
y = df["congestion"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) #80% training w 20% testing

model = RandomForestClassifier(n_estimators=100, random_state=42) # 100 decision tree
model.fit(X_train, y_train)

y_pred = model.predict(X_test) #goz2 el tok3 beta3o
print("Model Accuracy:", accuracy_score(y_test, y_pred)) #el accuracy beta3 el model

