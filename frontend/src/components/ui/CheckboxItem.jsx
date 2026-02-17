import React, { useId } from "react";
import { useIntl } from "react-intl";
import { Check } from "lucide-react";

export default function CheckboxItem({ checked, label, onChange = () => {} }) {
  const intl = useIntl();
  void intl;

  const id = useId();

  return (
    <label
      htmlFor={id}
      className="flex w-full cursor-pointer items-center gap-[12px] py-[8px] select-none"
    >
      <span className="relative inline-flex h-[20px] w-[20px] items-center justify-center">
        <input
          id={id}
          type="checkbox"
          className="peer sr-only"
          checked={!!checked}
          onChange={(e) => onChange(e.target.checked)}
        />
        <span
          className={[
            "h-[20px] w-[20px] rounded-[4px] border-2 transition-colors",
            checked ? "border-[#4361EE] bg-[#4361EE]" : "border-[#CBD5E1] bg-white",
            "peer-focus-visible:outline peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-[#4361EE]/40",
          ].join(" ")}
          aria-hidden="true"
        />
        <Check
          className={[
            "pointer-events-none absolute h-[14px] w-[14px] text-white transition-opacity",
            checked ? "opacity-100" : "opacity-0",
          ].join(" ")}
          strokeWidth={3}
          aria-hidden="true"
        />
      </span>

      <span className="text-[14px] font-normal leading-[22.4px] text-[#1E293B]">
        {label}
      </span>
    </label>
  );
}