import React from "react";
import { useIntl } from "react-intl";

export default function PrimaryButton({ children, onClick = () => {}, ariaLabel }) {
  const intl = useIntl();

  return (
    <button
      type="button"
      aria-label={ariaLabel || intl.formatMessage({ id: "primaryButton.ariaLabel" })}
      onClick={onClick}
      className="inline-flex h-[36px] w-full items-center justify-center rounded-[10px] bg-[#030213] px-4 text-[14px] font-medium leading-[20px] tracking-[-0.1504px] text-white transition-colors hover:bg-[#0B0D1A] focus:outline-none focus-visible:ring-2 focus-visible:ring-[#111827]/20"
    >
      {children}
    </button>
  );
}