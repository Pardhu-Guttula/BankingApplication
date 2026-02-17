import React from "react";
import { useIntl } from "react-intl";

export default function BreadcrumbSeparator() {
  useIntl();

  return (
    <span
      aria-hidden="true"
      className="text-[16px] leading-[1.5] font-['Outfit',sans-serif] font-normal text-[rgba(0,0,0,0.6)] px-[8px]"
    >
      /
    </span>
  );
}