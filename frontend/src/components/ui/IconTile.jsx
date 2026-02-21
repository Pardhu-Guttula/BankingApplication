import React from "react";

export default function IconTile({ icon: Icon, bgColor = "#F3F4F6", iconColor = "#111827", ariaLabel }) {
  return (
    <div
      className="flex h-10 w-10 items-center justify-center rounded-[10px]"
      style={{ backgroundColor: bgColor }}
      aria-label={ariaLabel}
    >
      <Icon className="h-[18px] w-[18px]" style={{ color: iconColor }} aria-hidden="true" />
    </div>
  );
}