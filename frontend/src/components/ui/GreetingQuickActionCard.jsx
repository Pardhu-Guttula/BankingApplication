import React from "react";

export default function GreetingQuickActionCard({
  iconSrc,
  label,
  onClick = () => {},
  ariaLabel,
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      aria-label={ariaLabel || label}
      className={[
        "group w-full rounded-[14px] border border-[rgba(0,0,0,0.10)] bg-white p-[1px] text-left",
        "transition-shadow focus:outline-none focus-visible:ring-2 focus-visible:ring-[#2563EB]/40 focus-visible:ring-offset-2",
        "hover:shadow-[0_1px_0_rgba(16,24,40,0.04),0_8px_24px_rgba(16,24,40,0.08)]",
      ].join(" ")}
    >
      <div className="flex h-[128px] w-full flex-col items-center justify-center gap-[12px] rounded-[13px] bg-white">
        <div className="flex h-12 w-12 items-center justify-center rounded-full bg-[#EFF6FF] transition-colors group-hover:bg-[#EAF2FF]">
          <img alt="" src={iconSrc} className="h-6 w-6" />
        </div>
        <div className="text-center text-[14px] font-medium leading-5 tracking-[-0.1504px] text-[#0A0A0A]">
          {label}
        </div>
      </div>
    </button>
  );
}