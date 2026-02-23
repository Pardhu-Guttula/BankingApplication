import React from "react";
import ProductCard from "./ProductCard";

export default function ProductCardGrid({ items }) {
  return (
    <div className="grid w-full grid-cols-1 gap-[16px] md:grid-cols-2 lg:grid-cols-3">
      {items.map((item) => (
        <ProductCard key={item.id} {...item} />
      ))}
    </div>
  );
}