import requests

def get_crypto_price(coin_id="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        price = data[coin_id]["usd"]
        return price
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

coin = "bitcoin"
target_threshold = 60000.0  

current_price = get_crypto_price(coin)

if current_price:
    print(f"Current {coin.capitalize()} Price: ${current_price:,.2f}")
    
    if current_price < target_threshold:
        print(f"ALERT: {coin.capitalize()} is below ${target_threshold:,.2f}!")
    else:
        print(f"{coin.capitalize()} is holding strong above ${target_threshold:,.2f}.")