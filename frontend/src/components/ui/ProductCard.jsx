import React from "react";
import { useIntl } from "react-intl";
import BadgePill from "./BadgePill";
import PrimaryButton from "./PrimaryButton";

export default function ProductCard({
  icon,
  iconBg,
  iconColor,
  badge,
  title,
  description,
  ctaLabel,
  onCta = () => {},
}) {
  const intl = useIntl();

  const IconComp = icon;
  const resolvedCtaLabel = ctaLabel ?? intl.formatMessage({ id: "common.applyNow" });

  return (
    <article className="flex flex-col rounded-[14px] border border-black/10 bg-white p-[16px] shadow-[0_1px_0_rgba(0,0,0,0.02)]">
      <div className="flex flex-col gap-[6px]">
        <div className="flex items-start justify-between">
          <div
            className="flex h-[36px] w-[36px] items-center justify-center rounded-[10px]"
            style={{ backgroundColor: iconBg }}
            aria-hidden="true"
          >
            <IconComp
              className="h-[18px] w-[18px]"
              style={{ color: iconColor }}
              aria-hidden="true"
            />
          </div>

          <BadgePill>{badge}</BadgePill>
        </div>

        <h3 className="pt-[2px] text-[16px] font-medium leading-[22px] tracking-[-0.25px] text-[#0A0A0A]">
          {title}
        </h3>

        <p className="text-[13px] font-normal leading-[18px] tracking-[-0.12px] text-[#717182]">
          {description}
        </p>
      </div>

      <div className="mt-[16px]">
        <PrimaryButton
          ariaLabel={intl.formatMessage(
            { id: "productCard.ctaAriaLabel" },
            { ctaLabel: resolvedCtaLabel, title }
          )}
          onClick={onCta}
        >
          {resolvedCtaLabel}
        </PrimaryButton>
      </div>
    </article>
  );
}