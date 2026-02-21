import React from "react";
import { useIntl } from "react-intl";

export default function PrimaryButton({ label, onClick = () => {} }) {
  const intl = useIntl();
  const resolvedLabel = label || intl.formatMessage({ id: "common.applyNow" });

  return (
    <button
      type="button"
      onClick={onClick}
      className="h-[36px] w-full rounded-[8px] bg-[#030213] text-center text-[14px] font-medium leading-[20px] text-white transition-colors hover:bg-[#0B0D1A] focus:outline-none focus-visible:ring-2 focus-visible:ring-[#030213]/30"
    >
      {resolvedLabel}
    </button>
  );
}