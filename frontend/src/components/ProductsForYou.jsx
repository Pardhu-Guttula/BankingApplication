import React from "react";
import { ArrowRight, CreditCard, PiggyBank, TrendingUp } from "lucide-react";
import { useIntl } from "react-intl";

import SectionHeader from "./layout/SectionHeader";
import ProductCardsRow from "./ui/ProductCardsRow";

const imgIcon = "https://www.figma.com/api/mcp/asset/b7e33d9e-916e-4943-906f-91e7ad130e4c";
const imgVector = "https://www.figma.com/api/mcp/asset/7f688443-0335-4978-8120-b1f61c1da500";
const imgVector1 = "https://www.figma.com/api/mcp/asset/c5f8364e-3e04-4273-9849-077c1c6d7508";
const imgVector2 = "https://www.figma.com/api/mcp/asset/0595e507-ef28-43c5-865d-25d4499c4552";
const imgVector3 = "https://www.figma.com/api/mcp/asset/fbfd7a7b-cb1a-46cd-9853-9ad5e4a1d5ac";
const imgVector4 = "https://www.figma.com/api/mcp/asset/984b2606-efbf-49e9-98e4-a35f0f1f06ff";
const imgVector5 = "https://www.figma.com/api/mcp/asset/ac6e1c65-7d5a-452b-a09f-e9f8ed6e9f17";
const imgVector6 = "https://www.figma.com/api/mcp/asset/286bf144-dbae-4c4b-ae59-553ce6d14729";

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
        id: "premium-savings",
        icon: PiggyBank,
        iconBg: "#F0FDF4",
        iconColor: "#16A34A",
        badge: intl.formatMessage({ id: "productsForYou.badgeRecommended" }),
        title: intl.formatMessage({ id: "productsForYou.premiumSavingsTitle" }),
        description: intl.formatMessage({
          id: "productsForYou.premiumSavingsDescription",
        }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
      },
      {
        id: "personal-loan",
        icon: TrendingUp,
        iconBg: "#EFF6FF",
        iconColor: "#2563EB",
        badge: intl.formatMessage({ id: "productsForYou.badgePreApproved" }),
        title: intl.formatMessage({ id: "productsForYou.personalLoanTitle" }),
        description: intl.formatMessage({
          id: "productsForYou.personalLoanDescription",
        }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
      },
      {
        id: "gold-credit-card",
        icon: CreditCard,
        iconBg: "#FAF5FF",
        iconColor: "#7C3AED",
        badge: intl.formatMessage({ id: "productsForYou.badgeLimitedOffer" }),
        title: intl.formatMessage({ id: "productsForYou.goldCreditCardTitle" }),
        description: intl.formatMessage({
          id: "productsForYou.goldCreditCardDescription",
        }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
      },
    ];

  return (
    <section className="w-full bg-white">
      <div className="mx-auto w-full max-w-[1192px] px-4 sm:px-6 lg:px-0">
        <div className="flex flex-col gap-[16px]">
          <SectionHeader
            title={resolvedTitle}
            actionLabel={intl.formatMessage({ id: "common.viewAll" })}
            onAction={onViewAll}
            actionIcon={ArrowRight}
          />
          <ProductCardsRow products={resolvedProducts} onApply={onApply} />
        </div>
      </div>

      {/* Preserved remote assets from MCP output (not used after icon conversion) */}
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