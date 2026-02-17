import React from "react";

export default function BrandMark({ onClick = () => {}, brandName = "SecureBank", iconSrc, ariaLabel }) {
  return (
    <button
      type="button"
      onClick={onClick}
      className="flex items-center gap-2 rounded-md focus:outline-none focus-visible:ring-2 focus-visible:ring-[#2563EB] focus-visible:ring-offset-2"
      aria-label={ariaLabel || "Go to home"}
    >
      <span className="flex h-10 w-10 items-center justify-center rounded-[10px] bg-[#155DFC]">
        <img src={iconSrc} alt="" className="h-6 w-6" />
      </span>
      <span className="text-[20px] font-bold leading-7 tracking-[-0.4492px] text-[#0A0A0A]">
        {brandName}
      </span>
    </button>
  );
}