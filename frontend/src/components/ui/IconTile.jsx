import React from "react";
import { useIntl } from "react-intl";

export default function IconTile({ icon: IconComp, bgClass, iconClass }) {
  const intl = useIntl();

  return (
    <div
      className={`flex h-11 w-11 items-center justify-center rounded-[10px] ${bgClass}`}
      aria-label={intl.formatMessage({ id: "iconTile.label" })}
    >
      <IconComp className={`h-5 w-5 ${iconClass}`} aria-hidden="true" />
    </div>
  );
}