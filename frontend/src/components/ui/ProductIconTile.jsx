import React from "react";
import { useIntl } from "react-intl";

export default function ProductIconTile({ iconBg, icon, ariaLabel }) {
  const intl = useIntl();
  const IconComp = icon;

  const resolvedAriaLabel =
    ariaLabel ?? intl.formatMessage({ id: "common.icon" });

  return (
    <div
      className="h-[44px] w-[44px] rounded-[10px]"
      style={{ backgroundColor: iconBg }}
    >
      <div className="flex h-full w-full items-center justify-center">
        <IconComp aria-label={resolvedAriaLabel} className="h-[20px] w-[20px]" />
      </div>
    </div>
  );
}