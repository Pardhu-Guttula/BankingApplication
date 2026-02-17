import React from "react";
import ProductCard from "./ProductCard";

export default function ProductCardRow({ items = [] }) {
  return (
    <div className="grid w-full grid-cols-3 gap-4">
      {items.map((item) => (
        <ProductCard key={item.id} {...item} />
      ))}
    </div>
  );
}