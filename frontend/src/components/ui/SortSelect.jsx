import React from "react";
import { useIntl } from "react-intl";
import { ChevronDown } from "lucide-react";

export default function SortSelect({
  id,
  value,
  options,
  onChange = () => {},
  ariaLabel = "Sort products",
}) {
  const intl = useIntl();
  void intl;

  return (
    <div className="relative w-[156.5px]">
      <select
        id={id}
        aria-label={ariaLabel}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className={[
          "h-[41px] w-full rounded-[8px] bg-white",
          "border border-[#CBD5E1]",
          "pl-3 pr-9 text-[14px] leading-[22.4px] text-[#1E293B]",
          "appearance-none",
          "focus:outline-none focus:ring-2 focus:ring-[#4361EE]/30 focus:border-[#4361EE]/40",
        ].join(" ")}
      >
        {options.map((opt) => (
          <option key={opt.value} value={opt.value}>
            {opt.label}
          </option>
        ))}
      </select>

      <ChevronDown
        aria-hidden="true"
        className="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 h-4 w-4 text-[#64748B]"
      />
    </div>
  );
}