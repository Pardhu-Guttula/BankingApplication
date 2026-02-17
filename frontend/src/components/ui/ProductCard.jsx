import React from "react";
import { useIntl } from "react-intl";

import StatusPill from "./StatusPill";
import PrimaryButton from "./PrimaryButton";

export default function ProductCard({
  id,
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

  const resolvedCtaLabel =
    ctaLabel ?? intl.formatMessage({ id: "common.applyNow" });

  return (
    <article className="flex h-full flex-col rounded-[14px] border border-[rgba(0,0,0,0.1)] bg-white p-[24px]">
      <div className="flex flex-1 flex-col gap-[6px]">
        <div className="flex items-start justify-between">
          <div
            className="h-[44px] w-[44px] rounded-[10px]"
            style={{ backgroundColor: iconBg }}
          >
            <div className="flex h-full w-full items-center justify-center">
              <IconComp
                className="h-[20px] w-[20px]"
                style={{ color: iconColor }}
                aria-hidden="true"
              />
            </div>
          </div>
          <StatusPill label={badge} />
        </div>

        <h3 className="text-[18px] font-medium leading-[28px] tracking-[-0.4395px] text-[#0A0A0A]">
          {title}
        </h3>

        <p className="text-[16px] font-normal leading-[24px] tracking-[-0.3125px] text-[#717182]">
          {description}
        </p>
      </div>

      <div className="mt-[24px]">
        <PrimaryButton label={resolvedCtaLabel} onClick={() => onCta(id)} />
      </div>
    </article>
  );
}