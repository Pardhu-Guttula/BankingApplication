import React from "react";
import { useIntl } from "react-intl";

import BadgePill from "./BadgePill";
import IconTile from "./IconTile";
import PrimaryButton from "./PrimaryButton";

export default function ProductCard({
  icon,
  iconBgColor,
  iconColor,
  badgeText,
  title,
  description,
  ctaLabel,
  onCta = () => {},
}) {
  const intl = useIntl();

  const resolvedCtaLabel = ctaLabel ?? intl.formatMessage({ id: "common.applyNow" });

  return (
    <article className="flex flex-col rounded-[14px] border border-black/10 bg-white p-4">
      <div className="flex items-start justify-between">
        <IconTile icon={icon} bgColor={iconBgColor} iconColor={iconColor} ariaLabel={`${title} icon`} />
        <BadgePill text={badgeText} />
      </div>

      <div className="mt-2">
        <h3 className="text-[16px] font-medium leading-[24px] tracking-[-0.2px] text-[#0A0A0A]">
          {title}
        </h3>
        <p className="mt-1 text-[13px] font-normal leading-[20px] tracking-[-0.15px] text-[#717182]">
          {description}
        </p>
      </div>

      <div className="mt-4">
        <PrimaryButton label={resolvedCtaLabel} onClick={onCta} />
      </div>
    </article>
  );
}