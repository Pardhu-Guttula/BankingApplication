import React from "react";

export default function BadgePill({ children }) {
  return (
    <span className="inline-flex items-center justify-center rounded-full bg-[#ECEEF2] px-[10px] py-[2px] text-[11px] font-medium leading-[16px] text-[#030213]">
      {children}
    </span>
  );
}