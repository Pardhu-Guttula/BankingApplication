import React from "react";

export default function StatusPill({ label, variant }) {
  const stylesByVariant = {
    completed: "bg-[#030213] text-white border-transparent",
    pending: "bg-[#ECEEF2] text-[#030213] border-transparent",
    review: "bg-white text-[#0A0A0A] border-[rgba(0,0,0,0.1)]",
  };

  return (
    <span
      className={[
        "inline-flex items-center justify-center",
        "h-[22px] px-[9px] py-[3px] rounded-[8px]",
        "text-[12px] leading-[16px] font-medium",
        "border",
        stylesByVariant[variant] || stylesByVariant.review,
      ].join(" ")}
    >
      {label}
    </span>
  );
}