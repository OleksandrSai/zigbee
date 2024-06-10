import paho.mqtt.client as mqtt
import json

# Параметры MQTT
BROKER_ADDRESS = "localhost"
DEVICE_TOPIC = "zigbee2mqtt/0xa4c1383f2e712be3"
COMMAND_TOPIC = f"{DEVICE_TOPIC}/set"

# Функция для подключения к MQTT брокеру
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Подписка на топик устройства для получения состояния
    client.subscribe(DEVICE_TOPIC)

# Функция для обработки полученных сообщений
def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")

# Создаем MQTT клиента
client = mqtt.Client()
client.on_connect = on_connect
# client.on_message = on_message

# Подключаемся к MQTT брокеру
client.connect(BROKER_ADDRESS, 1883, 60)

# Функция для включения/выключения розетки
def turn_on_plug(state):
    payload = json.dumps({"state": state})
    client.publish(COMMAND_TOPIC, payload)

# Запуск клиента в фоновом режиме
client.loop_start()

if __name__ == "__main__":
    while True:
        state = input('Введите "ON" для включения или "OFF" для выключения розетки: ')
        if state.upper() in ["ON", "OFF"]:
               turn_on_plug(state.upper())
        else:
            print("Неверный ввод. Пожалуйста, введите 'ON' или 'OFF'.")
        
