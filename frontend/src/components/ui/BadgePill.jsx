import React from "react";

export default function BadgePill({ label = "", className = "" }) {
  return (
    <span
      className={[
        "inline-flex items-center justify-center",
        "h-[22px] px-[9px] py-[3px]",
        "rounded-[8px]",
        "bg-[#ECEEF2] text-[#030213]",
        "text-[12px] leading-[16px] font-medium",
        "whitespace-nowrap",
        className,
      ].join(" ")}
    >
      {label}
    </span>
  );
}