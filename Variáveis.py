from binance.client import Client  # Importa o Client da biblioteca da Binance

# Substitua estas chaves pela sua chave de API e segredo da Binance
api_key = ''
api_secret = ''

# Inicializando o cliente da Binance
client = Client(api_key, api_secret)

# Obtendo a informação da conta (inclui dados de saldo, etc.)
account_info = client.get_account()

# Inicializa o saldo de USDT
binance_balance = 0.0

# Loop para encontrar o saldo da moeda USDT
for balance in account_info['balance']:
    if balance['asset'] == 'USDT':  # USDT é a stablecoin mais comum
        binance_balance = float(balance['free'])  # Saldo disponível

# Definindo valores para o cálculo
valor1 = 6.53
valor2 = 195.26
percentual = 100

# Calculando a porcentagem e exibindo o resultado formatado
porcentagem = valor1 * valor2 / percentual
print(f"\nCálculo da porcentagem: {valor1} * {valor2} / {percentual} = ${porcentagem:.2f}")

# Cálculo de 'var' com base no saldo da conta Binance
var = porcentagem * 5.81

# Atualizando 'var' com o saldo da conta Binance
var += binance_balance

# Nome do cliente
client_name = 'Solanas Token'

# Exibindo o resultado final
print(f"\nSaldo final para {client_name}: ${var:.2f}")
print(f"Saldo da conta Binance (USDT): ${binance_balance:.2f}")
