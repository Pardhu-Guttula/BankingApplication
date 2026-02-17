import React from "react";

export default function SupportCard({
  onContactSupport = () => {},
  title = "Need Help?",
  subtitle = "Contact our support team 24/7",
  buttonLabel = "Contact Support",
}) {
  return (
    <div className="w-full border-t border-[#E5E7EB] px-4 pt-[17px]">
      <div className="w-full rounded-[10px] bg-[#EFF6FF] px-4 pt-4 pb-4">
        <div className="text-[14px] leading-5 tracking-[-0.1504px] font-medium text-[#0A0A0A]">
          {title}
        </div>
        <div className="mt-1 text-[12px] leading-4 font-normal text-[#4A5565]">
          {subtitle}
        </div>

        <button
          type="button"
          onClick={onContactSupport}
          className={[
            "mt-3 h-8 w-full rounded-[8px]",
            "bg-white border border-[rgba(0,0,0,0.1)]",
            "text-[14px] leading-5 tracking-[-0.1504px] font-medium text-[#0A0A0A]",
            "transition-colors hover:bg-slate-50",
            "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#2563EB] focus-visible:ring-offset-2",
          ].join(" ")}
        >
          {buttonLabel}
        </button>
      </div>
    </div>
  );
}