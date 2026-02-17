import React from "react";
import { useIntl } from "react-intl";

import ProductCard from "./ProductCard";

export default function ProductCardsRow({ products, onApply = () => {} }) {
  const intl = useIntl();

  const resolvedProducts = products ?? [];

  return (
    <div className="grid w-full grid-cols-1 gap-[16px] md:grid-cols-2 lg:grid-cols-3">
      {resolvedProducts.map((p) => (
        <ProductCard
          key={p.id ?? intl.formatMessage({ id: "common.item" })}
          {...p}
          onCta={onApply}
        />
      ))}
    </div>
  );
}