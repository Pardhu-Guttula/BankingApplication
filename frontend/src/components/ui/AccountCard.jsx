import React from "react";

export default function AccountCard({
  icon: Icon,
  name,
  balance,
  maskedNumber,
  tone = "default",
  selected = false,
  onClick = () => {},
  onKeyDown = () => {},
}) {
  const balanceTone = tone === "negative" ? "text-[#0a0a0a]" : "text-[#0a0a0a]";

  return (
    <button
      type="button"
      onClick={onClick}
      onKeyDown={onKeyDown}
      className={[
        "group w-full text-left",
        "rounded-[14px] border border-[rgba(0,0,0,0.1)] bg-white p-[24px]",
        "transition-shadow focus:outline-none focus-visible:ring-2 focus-visible:ring-[#155dfc]/40 focus-visible:ring-offset-2",
        "hover:shadow-[0_1px_0_rgba(16,24,40,0.04),0_8px_24px_rgba(16,24,40,0.08)]",
        selected ? "ring-2 ring-[#155dfc]/25" : "",
      ].join(" ")}
      aria-pressed={selected}
    >
      <div className="flex items-center gap-[8px]">
        <span className="flex h-[32px] w-[32px] items-center justify-center rounded-[10px] bg-[#eff6ff]">
          <Icon className="h-[16px] w-[16px] text-[#155dfc]" aria-hidden="true" />
        </span>
        <span className="text-[16px] font-medium leading-[24px] tracking-[-0.3125px] text-[#0a0a0a]">
          {name}
        </span>
      </div>

      <div className="mt-[24px]">
        <div
          className={[
            "text-[24px] font-bold leading-[32px] tracking-[0.0703px]",
            balanceTone,
          ].join(" ")}
        >
          {balance}
        </div>
        <div className="mt-[4px] text-[14px] font-normal leading-[20px] tracking-[-0.1504px] text-[#6a7282]">
          {maskedNumber}
        </div>
      </div>
    </button>
  );
}