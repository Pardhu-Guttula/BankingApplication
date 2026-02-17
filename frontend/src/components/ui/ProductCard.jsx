import React from "react";
import IconTile from "./IconTile";
import BadgePill from "./BadgePill";
import PrimaryButton from "./PrimaryButton";

export default function ProductCard({ icon, iconTint, badge, title, description, ctaLabel, onCta = () => {} }) {
  return (
    <article className="flex h-[214px] w-full flex-col rounded-[14px] border border-[rgba(0,0,0,0.1)] bg-white p-5">
      <div className="flex flex-col gap-[4px]">
        <div className="flex items-start justify-between">
          <IconTile tint={iconTint} icon={icon} ariaLabel={`${title} icon`} />
          <BadgePill>{badge}</BadgePill>
        </div>

        <h3 className="mt-[4px] text-[16px] font-semibold leading-[22px] tracking-[-0.2px] text-[#0a0a0a]">
          {title}
        </h3>

        <p className="text-[13px] font-normal leading-[18px] tracking-[-0.1px] text-[#717182]">{description}</p>
      </div>

      <div className="mt-auto pt-[14px]">
        <PrimaryButton onClick={onCta}>{ctaLabel}</PrimaryButton>
      </div>
    </article>
  );
}