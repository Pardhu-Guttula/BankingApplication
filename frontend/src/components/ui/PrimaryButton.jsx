import React from "react";

export default function PrimaryButton({ children, onClick = () => {}, disabled = false }) {
  return (
    <button
      type="button"
      onClick={onClick}
      disabled={disabled}
      className="h-[34px] w-full rounded-[8px] bg-[#030213] text-center text-[13px] font-medium leading-[18px] tracking-[-0.1504px] text-white transition-colors hover:bg-[#0b0a2a] disabled:cursor-not-allowed disabled:opacity-60"
    >
      {children}
    </button>
  );
}