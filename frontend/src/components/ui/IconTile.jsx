import React from "react";
import { useIntl } from "react-intl";

export default function IconTile({ icon: IconComp, tintBg, iconColor, ariaLabel }) {
  const intl = useIntl();

  const resolvedAriaLabel =
    ariaLabel ?? intl.formatMessage({ id: "iconTile.ariaLabel" });

  return (
    <div
      className="flex h-[40px] w-[40px] items-center justify-center rounded-[10px]"
      style={{ backgroundColor: tintBg }}
      aria-label={resolvedAriaLabel}
    >
      <IconComp
        className="h-[20px] w-[20px]"
        style={{ color: iconColor }}
        aria-hidden="true"
      />
    </div>
  );
}