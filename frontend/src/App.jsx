import React from "react";
import { ArrowRight, CreditCard, PiggyBank, TrendingUp } from "lucide-react";

const imgIcon = "https://www.figma.com/api/mcp/asset/15ab76a7-57b5-4623-85bb-dcdbb4c34fba";
const imgVector = "https://www.figma.com/api/mcp/asset/46144a0f-1e7f-4e0b-b6c5-8d4ab0e57fcb";
const imgVector1 = "https://www.figma.com/api/mcp/asset/17052918-3443-4a43-9b47-a48e3b779af2";
const imgVector2 = "https://www.figma.com/api/mcp/asset/4a52efa6-415d-42d4-8e55-46318eef8ca3";
const imgVector3 = "https://www.figma.com/api/mcp/asset/dcf1c41d-16f9-44a1-8223-8b39b5137baa";
const imgVector4 = "https://www.figma.com/api/mcp/asset/65ef429a-4f1a-4c83-a407-52c6993a252e";
const imgVector5 = "https://www.figma.com/api/mcp/asset/4fcb9439-9bd9-48e9-a3e4-d7202f6c179f";
const imgVector6 = "https://www.figma.com/api/mcp/asset/31f7bf69-b3d6-47a0-bd39-0efe352032f6";

function noop() {}

function BadgePill({ text }) {
  return (
    <span className="inline-flex items-center justify-center rounded-[8px] bg-[#ECEEF2] px-[9px] py-[3px] text-[12px] font-medium leading-[16px] text-[#030213]">
      {text}
    </span>
  );
}

function PrimaryButton({ label, onClick = noop }) {
  return (
    <button
      type="button"
      onClick={onClick}
      className="inline-flex h-[36px] w-full items-center justify-center rounded-[8px] bg-[#030213] text-[14px] font-medium leading-[20px] tracking-[-0.1504px] text-white transition-colors hover:bg-[#0b0f2a] focus:outline-none focus-visible:ring-2 focus-visible:ring-[#030213]/30"
    >
      {label}
    </button>
  );
}

function IconTile({ variant = "green", icon: IconComp }) {
  const bg =
    variant === "green"
      ? "bg-[#F0FDF4]"
      : variant === "blue"
        ? "bg-[#EFF6FF]"
        : "bg-[#FAF5FF]";

  const fg =
    variant === "green"
      ? "text-[#16A34A]"
      : variant === "blue"
        ? "text-[#2563EB]"
        : "text-[#7C3AED]";

  return (
    <div className={`flex h-[44px] w-[44px] items-center justify-center rounded-[10px] ${bg}`}>
      <IconComp className={`h-5 w-5 ${fg}`} aria-hidden="true" />
    </div>
  );
}

function ProductCard({
  icon,
  iconBgVariant,
  badgeText,
  title,
  description,
  ctaLabel = "Apply Now",
  onCta = noop,
}) {
  return (
    <article className="flex min-h-[250px] w-full flex-col justify-between rounded-[14px] border border-black/10 bg-white p-[24px]">
      <div className="flex flex-col gap-[6px]">
        <div className="flex items-start justify-between">
          <IconTile icon={icon} variant={iconBgVariant} />
          <BadgePill text={badgeText} />
        </div>

        <h3 className="pt-[6px] text-[18px] font-medium leading-[28px] tracking-[-0.4395px] text-[#0A0A0A]">
          {title}
        </h3>

        <p className="text-[16px] font-normal leading-[24px] tracking-[-0.3125px] text-[#717182]">
          {description}
        </p>
      </div>

      <div className="pt-[24px]">
        <PrimaryButton label={ctaLabel} onClick={onCta} />
      </div>
    </article>
  );
}

function SectionHeader({ title, actionLabel, onAction = noop }) {
  return (
    <header className="flex w-full items-center justify-between">
      <h2 className="text-[20px] font-bold leading-[28px] tracking-[-0.4492px] text-[#0A0A0A]">
        {title}
      </h2>

      <button
        type="button"
        onClick={onAction}
        className="inline-flex h-[36px] items-center gap-[11px] rounded-[8px] px-2 text-[14px] font-medium leading-[20px] tracking-[-0.1504px] text-[#030213] transition-colors hover:bg-black/5 focus:outline-none focus-visible:ring-2 focus-visible:ring-[#030213]/20"
        aria-label={actionLabel}
      >
        <span>{actionLabel}</span>
        <ArrowRight className="h-4 w-4" aria-hidden="true" />
      </button>
    </header>
  );
}

const defaultProducts = [
  {
    id: "premium-savings",
    icon: PiggyBank,
    iconBgVariant: "green",
    badgeText: "Recommended",
    title: "Premium Savings Account",
    description: "Earn up to 4.5% APY with no minimum balance",
    ctaLabel: "Apply Now",
  },
  {
    id: "personal-loan",
    icon: TrendingUp,
    iconBgVariant: "blue",
    badgeText: "Pre-approved",
    title: "Personal Loan",
    description: "Pre-approved up to $50,000 at 6.9% APR",
    ctaLabel: "Apply Now",
  },
  {
    id: "gold-credit-card",
    icon: CreditCard,
    iconBgVariant: "purple",
    badgeText: "Limited Offer",
    title: "Gold Credit Card",
    description: "0% APR for 12 months + 2% cashback",
    ctaLabel: "Apply Now",
  },
];

export default function ProductsForYouSection({
  title = "Products for You",
  actionLabel = "View All",
  products = defaultProducts,
  onViewAll = noop,
  onApply = noop,
}) {
  return (
    <section className="w-full bg-white">
      <div className="mx-auto flex w-full max-w-[1192px] flex-col gap-[16px]">
        <SectionHeader title={title} actionLabel={actionLabel} onAction={onViewAll} />

        <div className="grid w-full grid-cols-1 gap-[16px] md:grid-cols-2 lg:grid-cols-3">
          {products.map((p) => (
            <ProductCard
              key={p.id}
              icon={p.icon}
              iconBgVariant={p.iconBgVariant}
              badgeText={p.badgeText}
              title={p.title}
              description={p.description}
              ctaLabel={p.ctaLabel}
              onCta={() => onApply(p.id)}
            />
          ))}
        </div>
      </div>
    </section>
  );
}