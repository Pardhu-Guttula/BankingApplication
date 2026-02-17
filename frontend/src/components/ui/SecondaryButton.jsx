import React from "react";

export default function SecondaryButton({
  children,
  onClick = () => {},
  className = "",
  icon: Icon,
  onMouseEnter,
  onMouseLeave,
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      onMouseEnter={onMouseEnter}
      onMouseLeave={onMouseLeave}
      className={[
        "inline-flex items-center justify-center gap-2",
        "h-9 rounded-lg border border-[rgba(0,0,0,0.10)] bg-white px-4",
        "text-sm font-medium text-[#0a0a0a]",
        "shadow-[0_1px_0_rgba(0,0,0,0.02)]",
        "transition-colors",
        "hover:bg-[#f9fafb] active:bg-[#f3f4f6]",
        "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#2563eb] focus-visible:ring-offset-2 focus-visible:ring-offset-transparent",
        className,
      ].join(" ")}
    >
      {Icon ? <Icon className="h-4 w-4 text-[#0a0a0a]" /> : null}
      {children}
    </button>
  );
}