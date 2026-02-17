import React from "react";
import { useIntl } from "react-intl";
import IconTile from "./IconTile";
import BadgePill from "./BadgePill";
import PrimaryButton from "./PrimaryButton";

export default function ProductCard({
  icon,
  iconBgVariant,
  badgeText,
  title,
  description,
  ctaLabel,
  onCta = () => {},
}) {
  const intl = useIntl();

  const resolvedCtaLabel =
    ctaLabel || intl.formatMessage({ id: "common.applyNow" });

  return (
    <article className="flex w-full flex-col rounded-[14px] border border-[rgba(0,0,0,0.1)] bg-white p-[16px]">
      <div className="flex flex-col gap-[6px]">
        <div className="flex items-start justify-between">
          <IconTile variant={iconBgVariant} icon={icon} />
          <BadgePill text={badgeText} />
        </div>

        <h3 className="text-[16px] font-medium leading-[24px] tracking-[-0.2px] text-[#0A0A0A]">
          {title}
        </h3>

        <p className="text-[14px] font-normal leading-[20px] tracking-[-0.15px] text-[#717182]">
          {description}
        </p>
      </div>

      <div className="mt-[12px]">
        <PrimaryButton label={resolvedCtaLabel} onClick={onCta} />
      </div>
    </article>
  );
}