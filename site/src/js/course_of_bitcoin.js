const ws = new WebSocket('wss://fstream.binance.com/ws/btcusdt@aggTrade')
const bitcoinParagraph = document.querySelector('#bitcoin-rate')

ws.onmessage = (event) => {
  let stockObj = JSON.parse(event.data)
  bitcoinParagraph.innerText = `1 BTC = $${parseFloat(stockObj.p).toFixed(2)}`
}
