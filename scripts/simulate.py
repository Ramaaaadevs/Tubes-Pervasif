import json
import os
import random
import time

import paho.mqtt.client as mqtt
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "..", "backend", ".env"))

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(os.getenv("MQTT_USER"), os.getenv("MQTT_PASS"))
client.connect(os.getenv("MQTT_HOST", "localhost"), int(os.getenv("MQTT_PORT", 1883)))
client.loop_start()

soil = 60.0
while True:
    soil = max(0.0, soil - random.uniform(0.2, 1.5))
    payload = {
        "id": "plant01",
        "ts": int(time.time()),
        "soil": round(soil, 1),
        "temp": round(random.uniform(26, 35), 1),
        "hum": random.randint(55, 85),
        "light": random.randint(200, 20000),
        "tank": True,
        "pump": False,
    }
    client.publish("plant/plant01/telemetry", json.dumps(payload))
    print(payload)
    time.sleep(3)
