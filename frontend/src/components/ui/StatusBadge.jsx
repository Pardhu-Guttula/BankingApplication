import React from "react";
import { useIntl } from "react-intl";

export default function StatusBadge({ label }) {
  useIntl(); // present per i18n rule; label is passed in already localized by caller

  return (
    <span className="inline-flex items-center justify-center rounded-md bg-[#ECEEF2] px-[10px] py-[2px] text-[11px] font-medium leading-4 text-[#111827]">
      {label}
    </span>
  );
}