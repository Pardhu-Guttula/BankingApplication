import React from "react";
import { CreditCard, PiggyBank, TrendingUp } from "lucide-react";
import { useIntl } from "react-intl";
import SectionHeader from "./layout/SectionHeader";
import ProductCard from "./ui/ProductCard";

const imgIcon = "https://www.figma.com/api/mcp/asset/34911475-6122-4a9f-b9e0-fb189c8f1778";
const imgVector = "https://www.figma.com/api/mcp/asset/7c9ad34b-1638-43ab-8775-df2ff5f34eee";
const imgVector1 = "https://www.figma.com/api/mcp/asset/c5ade51e-c514-43d0-9fbd-f2cae02dc9b4";
const imgVector2 = "https://www.figma.com/api/mcp/asset/2746272a-1812-4f5b-971f-91a6d9fb551f";
const imgVector3 = "https://www.figma.com/api/mcp/asset/831ce065-95a7-4adb-89cf-08fcc7b74385";
const imgVector4 = "https://www.figma.com/api/mcp/asset/ac54d098-d0cb-4e08-9767-1a673eda1a5c";
const imgVector5 = "https://www.figma.com/api/mcp/asset/5792059a-4569-430c-a175-023cd56aead6";
const imgVector6 = "https://www.figma.com/api/mcp/asset/28839d89-c7d7-44f8-9433-c11a1dec2dc3";

export default function ProductsForYou({
  title,
  items,
  onViewAll = () => {},
  onApply = () => {},
}) {
  const intl = useIntl();

  const resolvedTitle =
    title || intl.formatMessage({ id: "productsForYou.title" });

  const resolvedItems =
    items ||
    [
      {
        id: "premium-savings",
        icon: PiggyBank,
        iconBgVariant: "green",
        badgeText: intl.formatMessage({ id: "productsForYou.badge.recommended" }),
        title: intl.formatMessage({ id: "productsForYou.item.premiumSavings.title" }),
        description: intl.formatMessage({
          id: "productsForYou.item.premiumSavings.description",
        }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
      },
      {
        id: "personal-loan",
        icon: TrendingUp,
        iconBgVariant: "blue",
        badgeText: intl.formatMessage({ id: "productsForYou.badge.preApproved" }),
        title: intl.formatMessage({ id: "productsForYou.item.personalLoan.title" }),
        description: intl.formatMessage({
          id: "productsForYou.item.personalLoan.description",
        }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
      },
      {
        id: "gold-credit-card",
        icon: CreditCard,
        iconBgVariant: "purple",
        badgeText: intl.formatMessage({ id: "productsForYou.badge.limitedOffer" }),
        title: intl.formatMessage({ id: "productsForYou.item.goldCreditCard.title" }),
        description: intl.formatMessage({
          id: "productsForYou.item.goldCreditCard.description",
        }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
      },
    ];

  return (
    <section className="w-full bg-white">
      <div className="mx-auto w-full max-w-[1192px] px-0 py-0">
        <div className="flex w-full flex-col gap-[16px]">
          <SectionHeader
            title={resolvedTitle}
            actionLabel={intl.formatMessage({ id: "common.viewAll" })}
            onAction={onViewAll}
          />

          <div className="grid w-full grid-cols-1 gap-[16px] md:grid-cols-2 lg:grid-cols-3">
            {resolvedItems.map((item) => (
              <ProductCard
                key={item.id || item.title}
                icon={item.icon}
                iconBgVariant={item.iconBgVariant}
                badgeText={item.badgeText}
                title={item.title}
                description={item.description}
                ctaLabel={item.ctaLabel}
                onCta={() => onApply(item)}
              />
            ))}
          </div>
        </div>
      </div>

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