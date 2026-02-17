import React from "react";
import { useIntl } from "react-intl";

export default function CategoryTabButton({ id, label, count, Icon, active, onSelect = () => {} }) {
  useIntl();

  return (
    <button
      type="button"
      onClick={() => onSelect(id)}
      aria-pressed={active}
      className={[
        "group inline-flex h-9 items-center justify-center gap-2 rounded-full px-4",
        "text-[13px] font-medium leading-none",
        "transition-colors duration-150",
        "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#2F2A60]/35 focus-visible:ring-offset-2 focus-visible:ring-offset-white",
        active
          ? "bg-[#2F2A60] text-white shadow-[0_6px_14px_rgba(17,17,17,0.12)]"
          : "bg-white text-[#2F2A60] ring-1 ring-[#D9D9D9] hover:bg-[#F6F6F8]",
      ].join(" ")}
    >
      <span className={["inline-flex h-5 w-5 items-center justify-center rounded-md", active ? "text-white" : "text-[#2F2A60]"].join(" ")} aria-hidden="true">
        <Icon className="h-[18px] w-[18px]" />
      </span>

      <span className="whitespace-nowrap">
        {label} ({count})
      </span>
    </button>
  );
}