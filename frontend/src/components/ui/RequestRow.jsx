import React from "react";
import RequestIcon from "./RequestIcon";
import StatusPill from "./StatusPill";

export default function RequestRow({
  title,
  timeAgo,
  statusLabel,
  statusVariant,
  onClick = () => {},
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={[
        "w-full",
        "bg-[#F9FAFB] rounded-[10px]",
        "h-[76px] px-4",
        "flex items-center justify-between gap-4",
        "text-left",
        "transition-colors",
        "hover:bg-[#F3F4F6]",
        "focus:outline-none focus-visible:ring-2 focus-visible:ring-[#2563EB]/40 focus-visible:ring-offset-2 focus-visible:ring-offset-white",
      ].join(" ")}
    >
      <div className="flex items-center gap-3 min-w-0">
        <RequestIcon variant={statusVariant} />
        <div className="min-w-0">
          <div className="text-[16px] leading-[24px] font-medium text-[#0A0A0A] truncate">
            {title}
          </div>
          <div className="text-[14px] leading-[20px] font-normal text-[#6A7282] truncate">
            {timeAgo}
          </div>
        </div>
      </div>

      <StatusPill label={statusLabel} variant={statusVariant} />
    </button>
  );
}