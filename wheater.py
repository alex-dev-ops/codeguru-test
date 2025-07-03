import requests

def obtener_clima(ciudad, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        clima = datos['weather'][0]['description']
        temperatura = datos['main']['temp']
        sensacion = datos['main']['feels_like']
        humedad = datos['main']['humidity']
        viento = datos['wind']['speed']

        print(f"\n🌍 Clima en {ciudad.capitalize()}:")
        print(f"Clima: {clima}")
        print(f"Temperatura: {temperatura}°C")
        print(f"Sensación térmica: {sensacion}°C")
        print(f"Humedad: {humedad}%")
        print(f"Viento: {viento} m/s")
    else:
        print("❌ No se pudo obtener el clima. Verifica la ciudad o tu API key.")
# 🧪 Ejemplo de uso
if __name__ == "__main__":
    ciudad = input("🔎 Ingresa la ciudad: ")
    api_key = "TU_API_KEY_AQUÍ"  # Reemplaza esto con tu API key real
    obtener_clima(ciudad, api_key)
