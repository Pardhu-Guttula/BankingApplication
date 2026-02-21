import React from "react";
import { CreditCard, PiggyBank, TrendingUp } from "lucide-react";
import { useIntl } from "react-intl";
import SectionHeader from "./layout/SectionHeader";
import ProductCard from "./ui/ProductCard";

const imgIcon =
  "https://www.figma.com/api/mcp/asset/a7123217-a075-449d-807d-5d03f2aa46ce";
const imgVector =
  "https://www.figma.com/api/mcp/asset/bb9be317-d6bf-4cfa-941c-ac2aef7d15c2";
const imgVector1 =
  "https://www.figma.com/api/mcp/asset/eb0882c3-bbd8-457b-931a-9c2ef7b5aaf5";
const imgVector2 =
  "https://www.figma.com/api/mcp/asset/ebe3272e-737c-4f0c-a9c8-1d7a8b0969c1";
const imgVector3 =
  "https://www.figma.com/api/mcp/asset/b61c103a-6590-4bb6-9230-5be2134fb626";
const imgVector4 =
  "https://www.figma.com/api/mcp/asset/69aa91c1-dede-428c-b42c-18e8506030e6";
const imgVector5 =
  "https://www.figma.com/api/mcp/asset/25864437-7fa5-4d50-ba4f-c5c9a1756330";
const imgVector6 =
  "https://www.figma.com/api/mcp/asset/72af6a16-c027-40db-8373-8abf86dab73b";

export default function ProductsForYou({
  title,
  products,
  onViewAll = () => {},
  onApply = () => {},
}) {
  const intl = useIntl();

  const resolvedTitle =
    title || intl.formatMessage({ id: "productsForYou.title" });

  const resolvedProducts =
    products ||
    [
      {
        id: "premium-savings",
        icon: PiggyBank,
        iconVariant: "green",
        badgeText: intl.formatMessage({
          id: "productsForYou.product.premiumSavings.badge",
        }),
        title: intl.formatMessage({
          id: "productsForYou.product.premiumSavings.title",
        }),
        description: intl.formatMessage({
          id: "productsForYou.product.premiumSavings.description",
        }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
      },
      {
        id: "personal-loan",
        icon: TrendingUp,
        iconVariant: "blue",
        badgeText: intl.formatMessage({
          id: "productsForYou.product.personalLoan.badge",
        }),
        title: intl.formatMessage({
          id: "productsForYou.product.personalLoan.title",
        }),
        description: intl.formatMessage({
          id: "productsForYou.product.personalLoan.description",
        }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
      },
      {
        id: "gold-credit-card",
        icon: CreditCard,
        iconVariant: "purple",
        badgeText: intl.formatMessage({
          id: "productsForYou.product.goldCreditCard.badge",
        }),
        title: intl.formatMessage({
          id: "productsForYou.product.goldCreditCard.title",
        }),
        description: intl.formatMessage({
          id: "productsForYou.product.goldCreditCard.description",
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

        <div className="grid w-full grid-cols-1 gap-[16px] sm:grid-cols-2 lg:grid-cols-3">
          {resolvedProducts.map((p) => (
            <ProductCard
              key={p.id}
              icon={p.icon}
              iconVariant={p.iconVariant}
              badgeText={p.badgeText}
              title={p.title}
              description={p.description}
              ctaLabel={p.ctaLabel}
              onCta={() => onApply(p.id)}
            />
          ))}
        </div>

        {/* Preserved remote assets from MCP output (not used in production layout) */}
        <div className="hidden">
          <img alt="" src={imgIcon} />
          <img alt="" src={imgVector} />
          <img alt="" src={imgVector1} />
          <img alt="" src={imgVector2} />
          <img alt="" src={imgVector3} />
          <img alt="" src={imgVector4} />
          <img alt="" src={imgVector5} />
          <img alt="" src={imgVector6} />
        </div>
      </div>
    </section>
  );
}