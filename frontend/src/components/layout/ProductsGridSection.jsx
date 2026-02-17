import React, { useMemo } from "react";
import { useIntl } from "react-intl";
import ProductCard from "../ui/ProductCard";

export default function ProductsGridSection({
  products: productsProp,
  onAddToCart = () => {},
  onNavigateProduct = () => {},
  onToggleWishlist = () => {},
}) {
  const intl = useIntl();

  const products = useMemo(() => {
    if (productsProp && Array.isArray(productsProp) && productsProp.length)
      return productsProp;

    return [];
  }, [productsProp]);

  return (
    <section aria-label={intl.formatMessage({ id: "productsGridSection.ariaLabel" })} style={{ width: "100%" }}>
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(3, minmax(0, 1fr))",
          gap: 24,
        }}
      >
        {products.map((p) => (
          <ProductCard
            key={p.id}
            imageUrl={p.imageUrl}
            category={p.category}
            title={p.title}
            rating={p.rating}
            reviewCount={p.reviewCount}
            price={p.price}
            href={p.href}
            onNavigate={(href) => onNavigateProduct(p.id, href)}
            onAddToCart={() => onAddToCart(p.id)}
            onToggleWishlist={() => onToggleWishlist(p.id)}
          />
        ))}
      </div>
    </section>
  );
}