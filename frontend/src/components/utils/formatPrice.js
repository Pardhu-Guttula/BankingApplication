export default function formatPrice(price) {
  if (typeof price === "number") {
    return price.toLocaleString(undefined, { style: "currency", currency: "USD" });
  }
  return price;
}