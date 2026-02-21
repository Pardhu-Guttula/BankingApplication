import React from "react";
import { useIntl } from "react-intl";
import BadgePill from "./BadgePill";
import PrimaryButton from "./PrimaryButton";

export default function ProductCard({
  icon: Icon,
  iconBgClass,
  iconColorClass,
  badgeText,
  title,
  description,
  ctaLabel,
  onCta = () => {},
}) {
  const intl = useIntl();

  const resolvedCtaLabel =
    ctaLabel ?? intl.formatMessage({ id: "common.applyNow" });

  return (
    <article className="flex min-h-[250px] w-full flex-col justify-between rounded-[14px] border border-[rgba(0,0,0,0.1)] bg-white p-[24px]">
      <div className="flex flex-col gap-[6px]">
        <div className="flex items-start justify-between">
          <div
            className={[
              "flex h-[44px] w-[44px] items-center justify-center rounded-[10px]",
              iconBgClass,
            ].join(" ")}
          >
            <Icon
              className={["h-[20px] w-[20px]", iconColorClass].join(" ")}
              aria-hidden="true"
            />
          </div>
          <BadgePill text={badgeText} />
        </div>

        <h3 className="text-[18px] font-medium leading-[28px] tracking-[-0.4395px] text-[#0a0a0a]">
          {title}
        </h3>

        <p className="text-[16px] font-normal leading-[24px] tracking-[-0.3125px] text-[#717182]">
          {description}
        </p>
      </div>

      <div className="pt-[24px]">
        <PrimaryButton label={resolvedCtaLabel} onClick={onCta} />
      </div>
    </article>
  );
}