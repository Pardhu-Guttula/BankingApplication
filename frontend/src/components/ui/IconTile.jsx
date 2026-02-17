import React from "react";

export default function IconTile({ tint = "#F3F4F6", icon: IconComp, ariaLabel = "Product icon" }) {
  return (
    <div className="flex h-11 w-11 items-center justify-center rounded-[10px]" style={{ backgroundColor: tint }}>
      <IconComp className="h-5 w-5" aria-label={ariaLabel} />
    </div>
  );
}