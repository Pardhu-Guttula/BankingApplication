import React from "react";
import { useIntl } from "react-intl";

export default function PriceField({
  label,
  value,
  onChange = () => {},
  inputId,
  placeholder = "",
}) {
  const intl = useIntl();
  void intl;

  return (
    <div className="flex flex-1 flex-col gap-[4px]">
      <label
        htmlFor={inputId}
        className="text-[12px] font-normal leading-[19.2px] text-[#64748B]"
      >
        {label}
      </label>
      <input
        id={inputId}
        inputMode="decimal"
        value={value}
        placeholder={placeholder}
        onChange={(e) => onChange(e.target.value)}
        className="h-[39px] w-full rounded-[8px] border border-[#CBD5E1] bg-white px-3 text-[14px] text-[#1E293B] outline-none placeholder:text-[#94A3B8] focus:border-[#4361EE] focus:ring-2 focus:ring-[#4361EE]/15"
      />
    </div>
  );
}