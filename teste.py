from binance.client import Client
from binance.websockets import BinanceSocketManager

# Substitua pelas suas chaves da Testnet
api_key = '8ji1gGK79VspdpvF6BRcykfRrAj03Q9pDXMkd63L4bmPC6XHyux0rmCLIybKRnmN'
api_secret = 'jyunS9yKWKjCIUmKioL4qCPFf8NpvvqJhe6Na7PQh9cRA6G5aMURJJYuzyzNe2MC'

# Inicializa o cliente
client = Client(api_key, api_secret, testnet=True)

# Função para processar mensagens do WebSocket
def process_message(msg):
    print(f"Preço BTC/USDT: {msg['p']} (Hora: {msg['E']})")

# Inicializa o WebSocket
bm = BinanceSocketManager(client)
bm.start_symbol_ticker_socket('BTCUSDT', process_message)

# Mantém o WebSocket rodando
bm.start()

# Para parar manualmente, pressione Ctrl+C
input("Pressione Enter para parar o WebSocket...")
bm.close()