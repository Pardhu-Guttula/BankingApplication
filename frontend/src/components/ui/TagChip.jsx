import React from "react";
import { useIntl } from "react-intl";

export default function TagChip({ label, onClick = () => {} }) {
  const intl = useIntl();

  return (
    <button
      type="button"
      onClick={() => onClick(label)}
      className="inline-flex h-5 items-center rounded-full bg-[#4F5BFF] px-2.5 text-[11px] font-medium leading-5 text-white shadow-[0_1px_0_rgba(0,0,0,0.06)] transition-colors hover:bg-[#3F4BFF] focus:outline-none focus-visible:ring-2 focus-visible:ring-[#2F2A60]/30"
      aria-label={intl.formatMessage({ id: "tagChip.filterAria" }, { label })}
    >
      {label}
    </button>
  );
}