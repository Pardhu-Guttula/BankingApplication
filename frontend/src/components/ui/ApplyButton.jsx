import React from "react";

export default function ApplyButton({ label = "Apply Now", onClick = () => {}, disabled = false }) {
  return (
    <button
      type="button"
      onClick={onClick}
      disabled={disabled}
      className={[
        "w-full h-[36px] rounded-[8px]",
        "bg-[#030213] text-white",
        "text-[14px] leading-[20px] font-medium",
        "transition-colors",
        disabled ? "opacity-60 cursor-not-allowed" : "hover:bg-[#0B1020] active:bg-black",
        "focus:outline-none focus-visible:ring-2 focus-visible:ring-[#155DFC] focus-visible:ring-offset-2",
      ].join(" ")}
    >
      {label}
    </button>
  );
}