import React from "react";
import { CreditCard, PiggyBank, TrendingUp } from "lucide-react";
import { useIntl } from "react-intl";
import SectionHeader from "./layout/SectionHeader";
import ProductCard from "./ui/ProductCard";

const imgIcon = "https://www.figma.com/api/mcp/asset/f432089f-8190-48e2-b802-088fcd1c2651";
const imgVector = "https://www.figma.com/api/mcp/asset/397df746-9c4e-458e-b61c-0403d8951785";
const imgVector1 = "https://www.figma.com/api/mcp/asset/b7c3f6ba-ef8b-4b9a-a004-a92d2e5124cd";
const imgVector2 = "https://www.figma.com/api/mcp/asset/c03112c1-3ce0-4f5e-afb4-0261592efa2f";
const imgVector3 = "https://www.figma.com/api/mcp/asset/ed496eaa-b598-436d-945b-a760d3951267";
const imgVector4 = "https://www.figma.com/api/mcp/asset/c30dfbc5-99e4-4ccb-a481-91fcd40adf6e";
const imgVector5 = "https://www.figma.com/api/mcp/asset/2fa48c00-2211-40a5-a302-d3683614bd8e";
const imgVector6 = "https://www.figma.com/api/mcp/asset/a65d2350-f88a-4908-a0f9-cf0e7282a59e";

export default function ProductsForYou({
  title,
  products,
  onViewAll = () => {},
  onApply = () => {},
}) {
  const intl = useIntl();

  const resolvedTitle =
    title ?? intl.formatMessage({ id: "productsForYou.title" });

  const resolvedProducts =
    products ??
    [
      {
        id: "savings",
        icon: PiggyBank,
        iconBgClass: "bg-[#f0fdf4]",
        iconColorClass: "text-[#16a34a]",
        badgeText: intl.formatMessage({ id: "productsForYou.badgeRecommended" }),
        title: intl.formatMessage({ id: "productsForYou.productSavingsTitle" }),
        description: intl.formatMessage({
          id: "productsForYou.productSavingsDescription",
        }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
      },
      {
        id: "loan",
        icon: TrendingUp,
        iconBgClass: "bg-[#eff6ff]",
        iconColorClass: "text-[#2563eb]",
        badgeText: intl.formatMessage({ id: "productsForYou.badgePreApproved" }),
        title: intl.formatMessage({ id: "productsForYou.productLoanTitle" }),
        description: intl.formatMessage({
          id: "productsForYou.productLoanDescription",
        }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
      },
      {
        id: "card",
        icon: CreditCard,
        iconBgClass: "bg-[#faf5ff]",
        iconColorClass: "text-[#9333ea]",
        badgeText: intl.formatMessage({ id: "productsForYou.badgeLimitedOffer" }),
        title: intl.formatMessage({ id: "productsForYou.productCardTitle" }),
        description: intl.formatMessage({
          id: "productsForYou.productCardDescription",
        }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
      },
    ];

  return (
    <section className="w-full">
      <div className="mx-auto flex w-full max-w-[1192px] flex-col gap-[16px]">
        <SectionHeader
          title={resolvedTitle}
          actionLabel={intl.formatMessage({ id: "common.viewAll" })}
          onAction={onViewAll}
        />

        <div className="grid w-full grid-cols-1 gap-[16px] md:grid-cols-2 lg:grid-cols-3">
          {resolvedProducts.map((p) => (
            <ProductCard
              key={p.id}
              icon={p.icon}
              iconBgClass={p.iconBgClass}
              iconColorClass={p.iconColorClass}
              badgeText={p.badgeText}
              title={p.title}
              description={p.description}
              ctaLabel={p.ctaLabel}
              onCta={() => onApply(p.id)}
            />
          ))}
        </div>
      </div>

      {/* Asset constants preserved from input (not used after icon conversion) */}
      <img src={imgIcon} alt="" className="hidden" />
      <img src={imgVector} alt="" className="hidden" />
      <img src={imgVector1} alt="" className="hidden" />
      <img src={imgVector2} alt="" className="hidden" />
      <img src={imgVector3} alt="" className="hidden" />
      <img src={imgVector4} alt="" className="hidden" />
      <img src={imgVector5} alt="" className="hidden" />
      <img src={imgVector6} alt="" className="hidden" />
    </section>
  );
}