import React from "react";
import { CreditCard, PiggyBank, TrendingUp } from "lucide-react";
import { useIntl } from "react-intl";

import SectionHeader from "./layout/SectionHeader";
import ProductCardsGrid from "./ui/ProductCardsGrid";

const imgIcon = "https://www.figma.com/api/mcp/asset/6c71ae0b-0bc0-45e2-a750-768337ceed57";
const imgVector = "https://www.figma.com/api/mcp/asset/e2bcee18-ec55-433d-83ba-3e49b16d7859";
const imgVector1 = "https://www.figma.com/api/mcp/asset/5f565565-e54e-456b-884f-148e5dd9c4ce";
const imgVector2 = "https://www.figma.com/api/mcp/asset/78d3f356-1205-428a-9c1b-0ae7f86f1ce1";
const imgVector3 = "https://www.figma.com/api/mcp/asset/5a9cfad1-82de-41da-b136-d74a834ca32d";
const imgVector4 = "https://www.figma.com/api/mcp/asset/78b7ef2f-b7ef-4263-9af1-4d8ca2593b21";
const imgVector5 = "https://www.figma.com/api/mcp/asset/febba8a0-86aa-423c-8a63-118f361a9869";
const imgVector6 = "https://www.figma.com/api/mcp/asset/0ee92eb2-f0a6-4f8a-bd87-1ca29bd2c714";

export default function ProductsForYou({
  title,
  actionLabel,
  onViewAll = () => {},
  products,
}) {
  const intl = useIntl();

  const resolvedTitle = title ?? intl.formatMessage({ id: "productsForYou.title" });
  const resolvedActionLabel = actionLabel ?? intl.formatMessage({ id: "productsForYou.viewAll" });

  const resolvedProducts =
    products ??
    [
      {
        id: "premium-savings",
        icon: PiggyBank,
        iconBgColor: "#F0FDF4",
        iconColor: "#16A34A",
        badgeText: intl.formatMessage({ id: "productsForYou.badgeRecommended" }),
        title: intl.formatMessage({ id: "productsForYou.productPremiumSavingsTitle" }),
        description: intl.formatMessage({ id: "productsForYou.productPremiumSavingsDescription" }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
        onCta: () => {},
      },
      {
        id: "personal-loan",
        icon: TrendingUp,
        iconBgColor: "#EFF6FF",
        iconColor: "#2563EB",
        badgeText: intl.formatMessage({ id: "productsForYou.badgePreApproved" }),
        title: intl.formatMessage({ id: "productsForYou.productPersonalLoanTitle" }),
        description: intl.formatMessage({ id: "productsForYou.productPersonalLoanDescription" }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
        onCta: () => {},
      },
      {
        id: "gold-credit-card",
        icon: CreditCard,
        iconBgColor: "#FAF5FF",
        iconColor: "#7C3AED",
        badgeText: intl.formatMessage({ id: "productsForYou.badgeLimitedOffer" }),
        title: intl.formatMessage({ id: "productsForYou.productGoldCreditCardTitle" }),
        description: intl.formatMessage({ id: "productsForYou.productGoldCreditCardDescription" }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
        onCta: () => {},
      },
    ];

  return (
    <section className="w-full bg-white py-0">
      <div className="mx-auto w-full max-w-[1192px] px-0">
        <div className="flex w-full flex-col gap-4">
          <SectionHeader title={resolvedTitle} actionLabel={resolvedActionLabel} onAction={onViewAll} />
          <ProductCardsGrid products={resolvedProducts} />
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