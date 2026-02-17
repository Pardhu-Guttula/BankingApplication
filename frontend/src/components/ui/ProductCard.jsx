import React from "react";
import { useIntl } from "react-intl";
import StatusBadge from "./StatusBadge";

export default function ProductCard({
  icon,
  iconTileBg = "#F0FDF4",
  iconColor = "#16A34A",
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
    <article className="flex flex-col rounded-[12px] border border-black/10 bg-white p-4">
      <div className="flex items-start justify-between">
        <div
          className="flex h-10 w-10 items-center justify-center rounded-[10px]"
          style={{ backgroundColor: iconTileBg }}
          aria-hidden="true"
        >
          <IconComp className="h-5 w-5" style={{ color: iconColor }} />
        </div>

        <StatusBadge label={badge} />
      </div>

      <div className="mt-3">
        <h3 className="text-[16px] font-medium leading-6 tracking-[-0.2px] text-[#0A0A0A]">
          {title}
        </h3>
        <p className="mt-1 text-[14px] font-normal leading-5 tracking-[-0.2px] text-[#717182]">
          {description}
        </p>
      </div>

      <button
        type="button"
        onClick={onCta}
        className="mt-4 h-9 w-full rounded-md bg-[#030213] text-[13px] font-medium leading-5 tracking-[-0.1504px] text-white hover:bg-black focus:outline-none focus-visible:ring-2 focus-visible:ring-black/20"
      >
        {resolvedCtaLabel}
      </button>
    </article>
  );
}