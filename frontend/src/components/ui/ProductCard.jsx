import React from "react";
import ProductMedia from "./ProductMedia";
import ProductMeta from "./ProductMeta";

export default function ProductCard({
  imageSrc,
  category,
  title,
  ratingValue,
  reviewCount,
  price,
  onAddToCart = () => {},
  onNavigateToPdp = () => {},
}) {
  return (
    <article className="flex w-[331px] max-w-full flex-col overflow-hidden rounded-2xl bg-white shadow-[0px_1px_3px_0px_rgba(0,0,0,0.1),0px_1px_2px_0px_rgba(0,0,0,0.06)]">
      <ProductMedia imageSrc={imageSrc} alt={title} />
      <ProductMeta
        category={category}
        title={title}
        ratingValue={ratingValue}
        reviewCount={reviewCount}
        price={price}
        onNavigateToPdp={onNavigateToPdp}
        onAddToCart={onAddToCart}
      />
    </article>
  );
}