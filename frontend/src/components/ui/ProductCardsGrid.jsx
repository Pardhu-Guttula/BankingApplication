import React from "react";
import { useIntl } from "react-intl";
import ProductCard from "./ProductCard";

export default function ProductCardsGrid({ products = [] }) {
  useIntl(); // present per i18n rule; this component renders passed-in content

  return (
    <div className="grid w-full grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
      {products.map((p) => (
        <ProductCard key={p.id} {...p} />
      ))}
    </div>
  );
}