import React from "react";
import { useIntl } from "react-intl";
import { CreditCard, PiggyBank, TrendingUp } from "lucide-react";
import SectionHeader from "./layout/SectionHeader";
import ProductCard from "./ui/ProductCard";

const imgIcon = "https://www.figma.com/api/mcp/asset/f9132af7-93cf-4ada-880c-ac114ff9d89a";
const imgVector = "https://www.figma.com/api/mcp/asset/ebc808cb-f10b-46ef-8fd6-b960fb0a4bdd";
const imgVector1 = "https://www.figma.com/api/mcp/asset/e258c38e-2f44-49f0-ae2b-648aa0ed4e5e";
const imgVector2 = "https://www.figma.com/api/mcp/asset/8dc30c87-5c66-4fc7-9574-be3036977f47";
const imgVector3 = "https://www.figma.com/api/mcp/asset/7b0d491a-997c-4ada-880c-ac114ff9d89a";
const imgVector4 = "https://www.figma.com/api/mcp/asset/be4bfb3d-e806-49b0-9bdd-cf8a7381218b";
const imgVector5 = "https://www.figma.com/api/mcp/asset/f59bafbd-117e-4135-b687-3b75e2deac1e";
const imgVector6 = "https://www.figma.com/api/mcp/asset/457e0f04-4d87-44c5-858a-2b1bf7c9e275";

export default function ProductsForYou() {
  const intl = useIntl();

  const title = intl.formatMessage({ id: "productsForYou.title" });
  const actionLabel = intl.formatMessage({ id: "productsForYou.viewAll" });

  const products = [
    {
      id: "savings",
      icon: PiggyBank,
      iconBgClass: "bg-[#F0FDF4]",
      iconColorClass: "text-[#16A34A]",
      badge: intl.formatMessage({ id: "productsForYou.badgeRecommended" }),
      title: intl.formatMessage({ id: "productsForYou.productSavingsTitle" }),
      description: intl.formatMessage({ id: "productsForYou.productSavingsDescription" }),
      ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
    },
    {
      id: "loan",
      icon: TrendingUp,
      iconBgClass: "bg-[#EFF6FF]",
      iconColorClass: "text-[#2563EB]",
      badge: intl.formatMessage({ id: "productsForYou.badgePreApproved" }),
      title: intl.formatMessage({ id: "productsForYou.productLoanTitle" }),
      description: intl.formatMessage({ id: "productsForYou.productLoanDescription" }),
      ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
    },
    {
      id: "card",
      icon: CreditCard,
      iconBgClass: "bg-[#FAF5FF]",
      iconColorClass: "text-[#7C3AED]",
      badge: intl.formatMessage({ id: "productsForYou.badgeLimitedOffer" }),
      title: intl.formatMessage({ id: "productsForYou.productCardTitle" }),
      description: intl.formatMessage({ id: "productsForYou.productCardDescription" }),
      ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
    },
  ];

  const onViewAll = () => {};
  const onProductCta = () => {};

  return (
    <section className="w-full">
      <div className="mx-auto flex w-full max-w-[1192px] flex-col gap-4">
        <SectionHeader title={title} actionLabel={actionLabel} onAction={onViewAll} />

        <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
          {products.map((p) => (
            <ProductCard
              key={p.id}
              icon={p.icon}
              iconBgClass={p.iconBgClass}
              iconColorClass={p.iconColorClass}
              badge={p.badge}
              title={p.title}
              description={p.description}
              ctaLabel={p.ctaLabel}
              onCta={() => onProductCta(p.id)}
            />
          ))}
        </div>
      </div>

      {/* Preserved Figma MCP assets (not used after icon conversion, kept per requirements) */}
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