import React from "react";
import { useIntl } from "react-intl";

export default function CategoryChip({ label, count, active, onClick = () => {} }) {
  useIntl();

  return (
    <button
      type="button"
      onClick={() => onClick({ label, count })}
      className={[
        "inline-flex items-center gap-2 h-8 rounded-lg border px-3 bg-white",
        active ? "border-[#211747] shadow-[inset_0_0_0_1px_rgba(33,23,71,0.25)]" : "border-[#CAC4D0]",
        "hover:bg-[rgba(33,23,71,0.04)]",
        "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#211747]/30",
      ].join(" ")}
      aria-pressed={active}
    >
      <span
        className="text-[14px] leading-[20px] tracking-[0.1px] font-medium text-[#49454F]"
        style={{ fontFamily: "Outfit, Roboto, Arial, sans-serif", whiteSpace: "nowrap" }}
      >
        {label}
      </span>
      <span
        className="inline-flex items-center justify-center h-[18px] min-w-[18px] px-[6px] rounded-full text-white text-[10px] leading-[10px] font-medium"
        style={{
          backgroundColor: active ? "#211747" : "#BDBDBD",
          fontFamily: "Roboto, Arial, sans-serif",
        }}
      >
        {count}
      </span>
    </button>
  );
}