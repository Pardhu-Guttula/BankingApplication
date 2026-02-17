import React from "react";
import { useIntl } from "react-intl";

export default function BadgePill({ children }) {
  const intl = useIntl();

  return (
    <span
      className="inline-flex items-center justify-center rounded-full bg-[#EEF0F4] px-[9px] py-[3px] text-[12px] font-medium leading-[16px] text-[#374151]"
      aria-label={intl.formatMessage({ id: "badgePill.label" })}
    >
      {children}
    </span>
  );
}