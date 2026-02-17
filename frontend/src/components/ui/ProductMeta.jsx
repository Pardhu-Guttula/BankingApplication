import React from "react";
import { useIntl } from "react-intl";
import StarRating from "./StarRating";
import AddToCartButton from "./AddToCartButton";
import formatPrice from "../utils/formatPrice";

export default function ProductMeta({
  category,
  title,
  ratingValue = 4,
  reviewCount = 0,
  price,
  onNavigateToPdp = () => {},
  onAddToCart = () => {},
}) {
  const intl = useIntl();

  return (
    <div className="flex w-full flex-col items-start px-5 pb-5 pt-4">
      <div className="mb-1 font-sans text-[12px] font-semibold uppercase leading-[19.2px] tracking-[0.6px] text-[#4361EE]">
        {category ?? intl.formatMessage({ id: "productMeta.category" })}
      </div>

      <button
        type="button"
        onClick={() => onNavigateToPdp()}
        className="w-full cursor-pointer bg-transparent p-0 text-left font-sans text-[15px] font-semibold leading-[21px] text-[#1E293B]"
        style={{
          border: 0,
          margin: 0,
          display: "-webkit-box",
          WebkitLineClamp: 2,
          WebkitBoxOrient: "vertical",
          overflow: "hidden",
        }}
        aria-label={intl.formatMessage(
          { id: "productMeta.ariaOpenProduct" },
          { title: title ?? "" }
        )}
      >
        {title ?? intl.formatMessage({ id: "productMeta.title" })}
      </button>

      <div className="w-full pt-2">
        <StarRating value={ratingValue} max={5} reviewCount={reviewCount} />
      </div>

      <div className="w-full pb-4 pt-2">
        <div className="font-sans text-[20px] font-bold leading-[28px] text-[#4361EE]">
          {formatPrice(price)}
        </div>
      </div>

      <AddToCartButton onAddToCart={onAddToCart} />
    </div>
  );
}