import React from "react";
import { CreditCard, PiggyBank, TrendingUp } from "lucide-react";
import { useIntl } from "react-intl";
import SectionHeader from "./layout/SectionHeader";
import ProductCardGrid from "./ui/ProductCardGrid";

const imgIcon = "https://www.figma.com/api/mcp/asset/740c7a58-c0ca-4b93-bd24-87c936508180";
const imgVector = "https://www.figma.com/api/mcp/asset/48986c8b-edca-4095-8d81-17ded5b6fb84";
const imgVector1 = "https://www.figma.com/api/mcp/asset/f4de77b2-d4a2-4b53-b863-977982781547";
const imgVector2 = "https://www.figma.com/api/mcp/asset/e3e35b79-4cfe-4266-8f5a-0ae714ae6b64";
const imgVector3 = "https://www.figma.com/api/mcp/asset/5d4c7058-1a71-4f63-b3eb-902f173fb626";
const imgVector4 = "https://www.figma.com/api/mcp/asset/7e5b4dd1-ec16-4511-8564-39d95595da84";
const imgVector5 = "https://www.figma.com/api/mcp/asset/70b2dac5-aba5-4a47-a457-4a05d71baaed";
const imgVector6 = "https://www.figma.com/api/mcp/asset/721c76be-628b-4759-a794-74a94399695d";

export default function ProductsForYou({
  title,
  items,
  onViewAll = () => {},
}) {
  const intl = useIntl();

  const resolvedTitle =
    title ?? intl.formatMessage({ id: "productsForYou.title" });

  const defaultItems = [
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
      onCta: () => {},
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
      onCta: () => {},
    },
    {
      id: "gold-card",
      icon: CreditCard,
      iconBg: "#FAF5FF",
      iconColor: "#7C3AED",
      badge: intl.formatMessage({ id: "productsForYou.badgeLimitedOffer" }),
      title: intl.formatMessage({ id: "productsForYou.goldCardTitle" }),
      description: intl.formatMessage({
        id: "productsForYou.goldCardDescription",
      }),
      ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
      onCta: () => {},
    },
  ];

  const resolvedItems = items ?? defaultItems;

  return (
    <section
      aria-label={intl.formatMessage({ id: "productsForYou.ariaLabel" })}
      className="w-full bg-white py-0"
    >
      <div className="mx-auto flex w-full max-w-[1192px] flex-col gap-[16px] px-4 sm:px-6 lg:px-0">
        <SectionHeader
          title={resolvedTitle}
          actionLabel={intl.formatMessage({ id: "common.viewAll" })}
          onAction={onViewAll}
        />
        <ProductCardGrid items={resolvedItems} />
      </div>
    </section>
  );
}