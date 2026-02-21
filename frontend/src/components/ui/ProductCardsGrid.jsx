import React from "react";
import ProductCard from "./ProductCard";

export default function ProductCardsGrid({ products }) {
  return (
    <div className="grid w-full grid-cols-1 items-stretch gap-4 md:grid-cols-2 lg:grid-cols-3">
      {products.map((p) => (
        <ProductCard key={p.id} {...p} />
      ))}
    </div>
  );
}