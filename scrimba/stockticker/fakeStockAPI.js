export function getStockData() {
  const now = new Date();
  const hh = String(now.getHours()).padStart(2, "0");
  const mm = String(now.getMinutes()).padStart(2, "0");
  const ss = String(now.getSeconds()).padStart(2, "0");
  const timestamp = `${hh}:${mm}:${ss}`;

  const price = parseFloat(
    (Math.random() * 3).toFixed(2) /* return a random number between 0 and 3 */,
  );
  return {
    name: "QtechAI",
    sym: "QTA",
    price:
      price /* return a random number between 0 and 3 to two decimal places */,
    time: timestamp /* return a timestamp in this format: hh/mm/ss */,
  };
}
