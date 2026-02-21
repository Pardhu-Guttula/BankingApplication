import React from "react";
import { useIntl } from "react-intl";
import IconTile from "./IconTile";
import BadgePill from "./BadgePill";
import PrimaryButton from "./PrimaryButton";

export default function ProductCard({
  icon,
  iconVariant,
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
    <article className="flex min-h-[250px] flex-col justify-between rounded-[14px] border border-[rgba(0,0,0,0.1)] bg-white p-[24px]">
      <div className="flex flex-col gap-[16px]">
        <div className="flex items-start justify-between gap-[12px]">
          <IconTile variant={iconVariant} icon={icon} />
          <BadgePill text={badgeText} />
        </div>

        <div className="flex flex-col gap-[6px]">
          <h3 className="text-[18px] font-medium leading-[28px] tracking-[-0.4395px] text-[#0A0A0A]">
            {title}
          </h3>
          <p className="text-[16px] font-normal leading-[24px] tracking-[-0.3125px] text-[#717182]">
            {description}
          </p>
        </div>
      </div>

      <div className="pt-[24px]">
        <PrimaryButton label={resolvedCtaLabel} onClick={onCta} />
      </div>
    </article>
  );
}