import { getStockData } from "./fakeStockAPI.js";

// Initialize previousPrice to null
let previousPrice = null;

// Function to fetch new stock data and update the display
function updateStock() {
  const stockData = getStockData(); // Fetch fresh data
  renderStockTicker(stockData);
}

// Set interval to update every 1.5 seconds (1500 milliseconds)
setInterval(updateStock, 1500);

// Initial call to display data immediately
updateStock();

// Function to render the stock data
function renderStockTicker(stockData) {
  const stockDisplayName = document.getElementById("name");
  const stockDisplaySymbol = document.getElementById("symbol");
  const stockDisplayPrice = document.getElementById("price");
  const stockDisplayPriceIcon = document.getElementById("price-icon");
  const stockDisplayTime = document.getElementById("time");

  // Update name, symbol, and timestamp
  stockDisplayName.textContent = stockData.name;
  stockDisplaySymbol.textContent = stockData.sym;
  stockDisplayTime.textContent = stockData.time;

  // Update price
  stockDisplayPrice.textContent = stockData.price.toFixed(2);

  // Determine the triangle icon based on price change
  if (previousPrice === null) {
    // No previous data, default to grey right arrow
    stockDisplayPriceIcon.innerHTML = "►"; // right arrow
    stockDisplayPriceIcon.style.color = "grey";
  } else if (stockData.price > previousPrice) {
    // Price increased - green up arrow
    stockDisplayPriceIcon.innerHTML = "▲";
    stockDisplayPriceIcon.style.color = "green";
  } else if (stockData.price < previousPrice) {
    // Price decreased - red down arrow
    stockDisplayPriceIcon.innerHTML = "▼";
    stockDisplayPriceIcon.style.color = "red";
  } else {
    // No change - grey right arrow
    stockDisplayPriceIcon.innerHTML = "►";
    stockDisplayPriceIcon.style.color = "grey";
  }

  // Update previousPrice for next comparison
  previousPrice = stockData.price;
}
