import React from "react";

export default function QuickActionCard({
  id,
  label,
  Icon,
  onClick = () => {},
  active = false,
  onActiveChange = () => {},
}) {
  return (
    <button
      type="button"
      onClick={() => onClick(id)}
      onMouseEnter={() => onActiveChange(id)}
      onFocus={() => onActiveChange(id)}
      onMouseLeave={() => onActiveChange(null)}
      onBlur={() => onActiveChange(null)}
      className={[
        "group w-full rounded-[14px] border bg-white p-6",
        "flex flex-col items-center justify-center gap-3",
        "transition-colors",
        active ? "border-blue-200 bg-blue-50/30" : "border-black/10 hover:bg-gray-50/60",
        "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-500/40 focus-visible:ring-offset-2",
      ].join(" ")}
      aria-label={label}
    >
      <span
        className={[
          "grid h-12 w-12 place-items-center rounded-full transition-colors",
          active ? "bg-blue-100" : "bg-blue-50 group-hover:bg-blue-100",
        ].join(" ")}
        aria-hidden="true"
      >
        <Icon className="h-6 w-6 text-blue-600" strokeWidth={2} />
      </span>

      <span className="text-center text-[14px] font-medium leading-5 tracking-[-0.1504px] text-[#0A0A0A]">
        {label}
      </span>
    </button>
  );
}