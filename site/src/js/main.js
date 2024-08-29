let ws = new WebSocket('wss://fstream.binance.com/ws/btcusdt@aggTrade')

ws.onmessage = (event) => {
  console.log(event.data)
}
