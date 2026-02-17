import React from "react";
import { useIntl } from "react-intl";
import { ChevronLeft, ChevronRight } from "lucide-react";

export default function NavButton({
  direction = "prev",
  disabled,
  onClick = () => {},
  children,
}) {
  const intl = useIntl();
  void intl;

  const Icon = direction === "prev" ? ChevronLeft : ChevronRight;

  return (
    <button
      type="button"
      disabled={!!disabled}
      onClick={onClick}
      className={[
        "h-[43px] rounded-[8px] border px-[21px] py-[13px]",
        "inline-flex items-center gap-[8px]",
        "text-[14px] font-medium text-[#334155]",
        "bg-white border-[#CBD5E1]",
        "transition-colors",
        "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#4361EE]/30 focus-visible:ring-offset-2 focus-visible:ring-offset-transparent",
        disabled ? "opacity-50 cursor-not-allowed" : "hover:bg-[#F8FAFC]",
      ].join(" ")}
      aria-disabled={!!disabled}
    >
      {direction === "prev" ? (
        <>
          <Icon className="h-[16px] w-[16px] text-[#334155]" />
          <span className="leading-none">{children}</span>
        </>
      ) : (
        <>
          <span className="leading-none">{children}</span>
          <Icon className="h-[16px] w-[16px] text-[#334155]" />
        </>
      )}
    </button>
  );
}