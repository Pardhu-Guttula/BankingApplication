import React from "react";

export default function BadgePill({ children }) {
  return (
    <span className="inline-flex items-center justify-center rounded-[8px] bg-[#eceef2] px-[9px] py-[3px] text-[11px] font-medium leading-[16px] text-[#030213]">
      {children}
    </span>
  );
}