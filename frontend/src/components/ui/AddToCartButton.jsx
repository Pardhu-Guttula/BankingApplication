import React from "react";
import { useIntl } from "react-intl";
import { ShoppingCart } from "lucide-react";

export default function AddToCartButton({ onAddToCart = () => {}, label }) {
  const intl = useIntl();
  const resolvedLabel = label ?? intl.formatMessage({ id: "addToCartButton.label" });

  return (
    <button
      type="button"
      onClick={() => onAddToCart()}
      className="flex h-[44px] w-full cursor-pointer items-center justify-center gap-2 rounded-lg bg-[#4361EE] px-4 text-[14px] font-semibold text-white"
      aria-label={resolvedLabel}
    >
      <ShoppingCart size={16} aria-hidden="true" />
      <span>{resolvedLabel}</span>
    </button>
  );
}