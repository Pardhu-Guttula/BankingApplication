import React from "react";
import { CreditCard, PiggyBank, TrendingUp } from "lucide-react";
import { useIntl } from "react-intl";
import SectionHeader from "./layout/SectionHeader";
import ProductCardsGrid from "./ui/ProductCardsGrid";

const imgIcon =
  "https://www.figma.com/api/mcp/asset/bffbf5dd-411e-4a74-b982-ba209d6aab34";
const imgVector =
  "https://www.figma.com/api/mcp/asset/cad4723f-bd80-4d78-ab5c-afe437975a47";
const imgVector1 =
  "https://www.figma.com/api/mcp/asset/299eec6f-044a-4ce5-b46f-8bb1fe607c3c";
const imgVector2 =
  "https://www.figma.com/api/mcp/asset/ab6f769a-6084-4cc5-9a5e-810a5298657d";
const imgVector3 =
  "https://www.figma.com/api/mcp/asset/ab6f769a-6084-4cc5-9a5e-810a5298657d";
const imgVector4 =
  "https://www.figma.com/api/mcp/asset/f2f8c4ff-1f92-47fc-9d49-749dce9644e5";
const imgVector5 =
  "https://www.figma.com/api/mcp/asset/ea0a3d9e-400f-4689-a0e1-75aa974bd218";
const imgVector6 =
  "https://www.figma.com/api/mcp/asset/a0432b05-c92f-4469-ba09-3011398aaa63";

export default function ProductsForYou({
  title,
  products,
  onViewAll = () => {},
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
        iconTileBg: "#F0FDF4",
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
        iconTileBg: "#EFF6FF",
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
        iconTileBg: "#FAF5FF",
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

  return (
    <section className="w-full">
      <div className="mx-auto w-full max-w-[1192px] px-0 py-0">
        <div className="flex w-full flex-col gap-4">
          <SectionHeader
            title={resolvedTitle}
            actionLabel={intl.formatMessage({ id: "common.viewAll" })}
            onAction={onViewAll}
          />
          <ProductCardsGrid products={resolvedProducts} />
        </div>
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