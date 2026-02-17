import React from "react";
import { useIntl } from "react-intl";
import { ArrowRight } from "lucide-react";
import ProductCard from "../ui/ProductCard";

export default function ProductsForYouSection({
  title,
  viewAllLabel,
  viewAllAriaLabel,
  onViewAll = () => {},
  onApplyProduct = () => {},
  products = [],
  selectedProductId,
  onSelectProduct = () => {},
}) {
  const intl = useIntl();

  const computedTitle = title || intl.formatMessage({ id: "productsForYouSection.title" });
  const computedViewAll = viewAllLabel || intl.formatMessage({ id: "common.viewAll" });
  const computedViewAllAria =
    viewAllAriaLabel || intl.formatMessage({ id: "productsForYouSection.viewAllAria" });

  return (
    <section className="w-full">
      <div className="flex items-center justify-between h-[36px]">
        <h2 className="text-[#0A0A0A] text-[20px] leading-[28px] font-bold tracking-[-0.4492px]">
          {computedTitle}
        </h2>

        <button
          type="button"
          onClick={onViewAll}
          className={[
            "h-[36px] px-[10px]",
            "inline-flex items-center gap-[8px]",
            "rounded-[8px]",
            "text-[#030213] text-[14px] leading-[20px] font-medium tracking-[-0.1504px]",
            "hover:bg-[#F3F4F6] active:bg-[#E5E7EB]",
            "focus:outline-none focus-visible:ring-2 focus-visible:ring-[#155DFC] focus-visible:ring-offset-2",
          ].join(" ")}
          aria-label={computedViewAllAria}
        >
          <span>{computedViewAll}</span>
          <ArrowRight className="w-4 h-4" aria-hidden="true" />
        </button>
      </div>

      <div className="mt-[16px] grid grid-cols-1 md:grid-cols-3 gap-[16px]">
        {products.map((p) => (
          <ProductCard
            key={p.id}
            {...p}
            selected={selectedProductId === p.id}
            onSelect={(id) => onSelectProduct(id)}
            onApply={(id) => onApplyProduct(id)}
          />
        ))}
      </div>
    </section>
  );
}