import React from "react";
import BadgePill from "./BadgePill";
import ApplyButton from "./ApplyButton";

export default function ProductCard({
  id,
  icon: Icon,
  iconBgClassName = "bg-[#EFF6FF]",
  iconClassName = "text-[#155DFC]",
  badge,
  title,
  description,
  ctaLabel = "Apply Now",
  onApply = () => {},
  selected = false,
  onSelect = () => {},
}) {
  return (
    <div
      role="button"
      tabIndex={0}
      onClick={() => onSelect(id)}
      onKeyDown={(e) => {
        if (e.key === "Enter" || e.key === " ") onSelect(id);
      }}
      className={[
        "bg-white border border-[rgba(0,0,0,0.1)] rounded-[14px]",
        "p-[24px]",
        "flex flex-col",
        "h-[250px]",
        "transition-shadow",
        selected ? "shadow-[0_0_0_2px_rgba(21,93,252,0.35)]" : "hover:shadow-sm",
        "focus:outline-none focus-visible:ring-2 focus-visible:ring-[#155DFC] focus-visible:ring-offset-2",
      ].join(" ")}
      aria-label={`${title} product card`}
    >
      <div className="flex items-start justify-between">
        <div
          className={[
            "w-[44px] h-[44px] rounded-[10px]",
            "flex items-center justify-center",
            iconBgClassName,
          ].join(" ")}
          aria-hidden="true"
        >
          <Icon className={["w-5 h-5", iconClassName].join(" ")} />
        </div>

        <BadgePill label={badge} />
      </div>

      <div className="mt-[14px]">
        <div className="text-[#0A0A0A] text-[18px] leading-[28px] font-medium tracking-[-0.4395px]">
          {title}
        </div>
        <div className="mt-[6px] text-[#717182] text-[16px] leading-[24px] font-normal tracking-[-0.3125px]">
          {description}
        </div>
      </div>

      <div className="mt-auto">
        <ApplyButton
          label={ctaLabel}
          onClick={(e) => {
            e.stopPropagation();
            onApply(id);
          }}
        />
      </div>
    </div>
  );
}