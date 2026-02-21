import React from "react";
import { useIntl } from "react-intl";

export default function BadgePill({ label }) {
  const intl = useIntl();

  const resolvedLabel =
    label ?? intl.formatMessage({ id: "badgePill.label" });

  return (
    <span className="inline-flex items-center justify-center rounded-[8px] bg-[#ECEEF2] px-[9px] py-[3px] text-[12px] font-medium leading-[16px] text-[#030213]">
      {resolvedLabel}
    </span>
  );
}