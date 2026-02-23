import React from "react";

export default function PrimaryButton({ children, onClick = () => {}, ariaLabel }) {
  return (
    <button
      type="button"
      aria-label={ariaLabel}
      onClick={onClick}
      className="inline-flex h-[30px] w-full items-center justify-center rounded-[8px] bg-[#030213] text-[13px] font-medium leading-[18px] tracking-[-0.12px] text-white transition-colors hover:bg-[#0b0b1a] focus:outline-none focus-visible:ring-2 focus-visible:ring-[#030213]/30 focus-visible:ring-offset-2"
    >
      {children}
    </button>
  );
}