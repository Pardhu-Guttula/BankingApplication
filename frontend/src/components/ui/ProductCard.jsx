import React from "react";
import { useIntl } from "react-intl";
import IconTile from "./IconTile";
import BadgePill from "./BadgePill";
import PrimaryButton from "./PrimaryButton";

export default function ProductCard({
  icon,
  iconTintBg,
  iconColor,
  badge,
  title,
  description,
  ctaLabel,
  onCta = () => {},
}) {
  const intl = useIntl();

  const resolvedCtaLabel =
    ctaLabel ?? intl.formatMessage({ id: "common.applyNow" });

  return (
    <article className="flex flex-col rounded-[14px] border border-[rgba(0,0,0,0.1)] bg-white p-[16px]">
      <div className="flex items-start justify-between">
        <IconTile
          icon={icon}
          tintBg={iconTintBg}
          iconColor={iconColor}
          ariaLabel={intl.formatMessage(
            { id: "productCard.iconAriaLabel" },
            { title }
          )}
        />
        <BadgePill label={badge} />
      </div>

      <h3 className="mt-[10px] text-[16px] font-medium leading-[24px] tracking-[-0.2px] text-[#0A0A0A]">
        {title}
      </h3>

      <p className="mt-[6px] text-[14px] font-normal leading-[20px] tracking-[-0.2px] text-[#717182]">
        {description}
      </p>

      <div className="mt-[12px]">
        <PrimaryButton label={resolvedCtaLabel} onClick={onCta} />
      </div>
    </article>
  );
}