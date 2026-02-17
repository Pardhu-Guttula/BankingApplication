import React from "react";
import { useIntl } from "react-intl";

export default function PageButton({ page, isActive, onSelect = () => {} }) {
  const intl = useIntl();
  void intl;

  return (
    <button
      type="button"
      onClick={() => onSelect(page)}
      aria-current={isActive ? "page" : undefined}
      className={[
        "h-11 w-11 rounded-[8px] border text-[14px] font-medium",
        "inline-flex items-center justify-center",
        "transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#4361EE]/30 focus-visible:ring-offset-2 focus-visible:ring-offset-transparent",
        isActive
          ? "bg-[#4361EE] border-[#4361EE] text-white"
          : "bg-white border-[#CBD5E1] text-black hover:bg-[#F8FAFC]",
      ].join(" ")}
    >
      {page}
    </button>
  );
}