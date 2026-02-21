import React from "react";
import { CreditCard, PiggyBank, TrendingUp } from "lucide-react";
import { useIntl } from "react-intl";
import SectionHeader from "./layout/SectionHeader";
import ProductCard from "./ui/ProductCard";

const imgIcon =
  "https://www.figma.com/api/mcp/asset/791d69a6-a25a-4ffb-a748-a08a23a31f5c";
const imgVector =
  "https://www.figma.com/api/mcp/asset/c45ea885-c7c4-4252-b911-f79631025873";
const imgVector1 =
  "https://www.figma.com/api/mcp/asset/e699adb3-a670-4763-a41d-a38cc56e9480";
const imgVector2 =
  "https://www.figma.com/api/mcp/asset/8f077b70-1e50-4d92-a174-6100aea858ec";
const imgVector3 =
  "https://www.figma.com/api/mcp/asset/ee3badb4-27b9-4dca-888d-ec3c73d71218";
const imgVector4 =
  "https://www.figma.com/api/mcp/asset/e4563f8f-4733-434a-8f64-19791c0a33af";
const imgVector5 =
  "https://www.figma.com/api/mcp/asset/6368ab3a-b69c-459d-9532-18f9c427c2bc";
const imgVector6 =
  "https://www.figma.com/api/mcp/asset/85ccfc87-e212-47fd-bd57-ed911fdccb25";

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
        iconTintBg: "#F0FDF4",
        iconColor: "#22C55E",
        badge: intl.formatMessage({ id: "productsForYou.badgeRecommended" }),
        title: intl.formatMessage({ id: "productsForYou.productSavingsTitle" }),
        description: intl.formatMessage({
          id: "productsForYou.productSavingsDescription",
        }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
      },
      {
        id: "loan",
        icon: TrendingUp,
        iconTintBg: "#EFF6FF",
        iconColor: "#3B82F6",
        badge: intl.formatMessage({ id: "productsForYou.badgePreApproved" }),
        title: intl.formatMessage({ id: "productsForYou.productLoanTitle" }),
        description: intl.formatMessage({
          id: "productsForYou.productLoanDescription",
        }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
      },
      {
        id: "card",
        icon: CreditCard,
        iconTintBg: "#FAF5FF",
        iconColor: "#A855F7",
        badge: intl.formatMessage({ id: "productsForYou.badgeLimitedOffer" }),
        title: intl.formatMessage({ id: "productsForYou.productCardTitle" }),
        description: intl.formatMessage({
          id: "productsForYou.productCardDescription",
        }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
      },
    ];

  return (
    <section className="w-full bg-white py-0">
      <div className="mx-auto w-full max-w-[1192px] px-0">
        <div className="flex w-full flex-col gap-[16px]">
          <SectionHeader title={resolvedTitle} onAction={onViewAll} />

          <div className="grid grid-cols-1 gap-[16px] md:grid-cols-2 lg:grid-cols-3">
            {resolvedProducts.map((p) => (
              <ProductCard
                key={p.id}
                icon={p.icon}
                iconTintBg={p.iconTintBg}
                iconColor={p.iconColor}
                badge={p.badge}
                title={p.title}
                description={p.description}
                ctaLabel={p.ctaLabel}
                onCta={() => onApply(p.id)}
              />
            ))}
          </div>
        </div>
      </div>

      <div className="hidden">
        <img src={imgIcon} alt="" />
        <img src={imgVector} alt="" />
        <img src={imgVector1} alt="" />
        <img src={imgVector2} alt="" />
        <img src={imgVector3} alt="" />
        <img src={imgVector4} alt="" />
        <img src={imgVector5} alt="" />
        <img src={imgVector6} alt="" />
      </div>
    </section>
  );
}