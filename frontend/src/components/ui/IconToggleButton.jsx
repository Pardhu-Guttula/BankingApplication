import React from "react";
import { useIntl } from "react-intl";

export default function IconToggleButton({
  active,
  label,
  onClick = () => {},
  children,
}) {
  const intl = useIntl();
  void intl;

  return (
    <button
      type="button"
      aria-pressed={active}
      aria-label={label}
      onClick={onClick}
      className={[
        "h-10 w-10 rounded-[8px] inline-flex items-center justify-center",
        "transition-colors",
        active ? "bg-[#4361EE] text-white" : "bg-[#F1F5F9] text-[#64748B]",
        "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#4361EE]/40 focus-visible:ring-offset-2 focus-visible:ring-offset-white",
      ].join(" ")}
    >
      {children}
    </button>
  );
}