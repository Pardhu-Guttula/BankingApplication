import React from "react";
import { ArrowRight, CreditCard, PiggyBank, TrendingUp } from "lucide-react";
import { useIntl } from "react-intl";
import SectionHeader from "./layout/SectionHeader";
import ProductCardRow from "./ui/ProductCardRow";

const imgIcon = "https://www.figma.com/api/mcp/asset/ae7cde6f-4185-4114-a269-379ef0b0a698";
const imgVector = "https://www.figma.com/api/mcp/asset/e22af431-71c3-4fd5-8512-c643d62afa8d";
const imgVector1 = "https://www.figma.com/api/mcp/asset/7d5a2248-6db3-43dd-8519-4df3905873e9";
const imgVector2 = "https://www.figma.com/api/mcp/asset/2326ca3b-d22e-41a3-b101-c0f51ab99bd9";
const imgVector3 = "https://www.figma.com/api/mcp/asset/2326ca3b-d22e-41a3-b101-c0f51ab99bd9";
const imgVector4 = "https://www.figma.com/api/mcp/asset/179321b7-8647-4801-880b-e8d9390130c3";
const imgVector5 = "https://www.figma.com/api/mcp/asset/271a6e40-9f52-401c-955e-36d1609686cd";
const imgVector6 = "https://www.figma.com/api/mcp/asset/df92f8dd-e288-45cf-8c93-c9945c88af98";

export default function ProductsForYou({
  title,
  items,
  onViewAll = () => {},
}) {
  const intl = useIntl();

  const resolvedTitle = title ?? intl.formatMessage({ id: "productsForYou.title" });

  const resolvedItems =
    items ??
    [
      {
        id: "savings",
        icon: PiggyBank,
        iconTint: "#f0fdf4",
        badge: intl.formatMessage({ id: "productsForYou.badgeRecommended" }),
        title: intl.formatMessage({ id: "productsForYou.cardSavingsTitle" }),
        description: intl.formatMessage({ id: "productsForYou.cardSavingsDescription" }),
        ctaLabel: intl.formatMessage({ id: "productsForYou.applyNow" }),
        onCta: () => {},
      },
      {
        id: "loan",
        icon: TrendingUp,
        iconTint: "#eff6ff",
        badge: intl.formatMessage({ id: "productsForYou.badgePreApproved" }),
        title: intl.formatMessage({ id: "productsForYou.cardLoanTitle" }),
        description: intl.formatMessage({ id: "productsForYou.cardLoanDescription" }),
        ctaLabel: intl.formatMessage({ id: "productsForYou.applyNow" }),
        onCta: () => {},
      },
      {
        id: "card",
        icon: CreditCard,
        iconTint: "#faf5ff",
        badge: intl.formatMessage({ id: "productsForYou.badgeLimitedOffer" }),
        title: intl.formatMessage({ id: "productsForYou.cardCreditTitle" }),
        description: intl.formatMessage({ id: "productsForYou.cardCreditDescription" }),
        ctaLabel: intl.formatMessage({ id: "productsForYou.applyNow" }),
        onCta: () => {},
      },
    ];

  return (
    <section className="w-full">
      <div className="mx-auto flex w-full max-w-[1192px] flex-col gap-4">
        <SectionHeader
          title={resolvedTitle}
          actionLabel={intl.formatMessage({ id: "common.viewAll" })}
          onAction={onViewAll}
          actionIcon={ArrowRight}
        />

        <ProductCardRow items={resolvedItems} />
      </div>

      <div className="sr-only" aria-hidden="true">
        <img alt="" src={imgIcon} />
        <img alt="" src={imgVector} />
        <img alt="" src={imgVector1} />
        <img alt="" src={imgVector2} />
        <img alt="" src={imgVector3} />
        <img alt="" src={imgVector4} />
        <img alt="" src={imgVector5} />
        <img alt="" src={imgVector6} />
      </div>
    </section>
  );
}