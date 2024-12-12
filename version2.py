import random
import pandas as pd
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
        weather = random.choice([0, 1])  # 0: Good weather, 1: Bad weather
        road_length = random.randint(1, 10)  
        traffic_speed = random.randint(20, 90) 
        traffic_lights = random.choice([0, 1])  
        event = random.choice([0, 1])  #de m3naha hal feh event haysbb za7ma wla la2
        #haytem el ta3deel 3la el hour w el day w el day of year w el weather 34an mykno4 randomized bal ykono data 7a2e2ea

        congestion = 0  #dah el mkdar el ba7sb mno hayb2a za7ma wla la2

        # Adjusted conditions for more balanced congestion levels
        if (0 <= hour <= 5 or 22 <= hour <= 23) and weather == 0 and traffic_speed >= 40:
            congestion = 0  # Not Crowded
        elif (6 <= hour <= 10 or 16 <= hour <= 20) and weather == 0 and traffic_speed >= 30:
            congestion = 1  # Mildly Crowded
        elif (7 <= hour <= 11 or 15 <= hour <= 21) and (weather == 1 or traffic_speed <= 20):
            congestion = 2  # Moderately Crowded
        else:
            congestion = 3  # Very Crowded

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

#print first 10 samples mn el data set
for i in range(10):
    print(f"Sample {i+1}:")
    print("Features:")
    print(X_test.iloc[i])
    print("Actual Congestion:", y_test.iloc[i])
    print("Predicted Congestion:", y_pred[i])

    if y_pred[i] == 0:
        print("Crowd Level: Not Crowded")
    elif y_pred[i] == 1:
        print("Crowd Level: Mildly Crowded")
    elif y_pred[i] == 2:
        print("Crowd Level: Moderately Crowded")
    else:
        print("Crowd Level: Very Crowded")

    print()
    
#el condiions m7taga tet7sn...