import React from 'react';
import { noop } from '../../utils/noop';

export function PrimaryButton({ label, disabled, onClick = noop }) {
  return (
    <button
      type="submit"
      disabled={disabled}
      onClick={(e) => {
        // keep native submit behavior; still allow consumers to hook click
        onClick(e);
      }}
      className={[
        "h-11 w-full rounded-[8px] bg-[#030213] text-white",
        "text-[14px] leading-[20px] font-medium tracking-[-0.1504px]",
        "transition-opacity",
        disabled ? "opacity-60 cursor-not-allowed" : "hover:opacity-95",
        "focus:outline-none focus:ring-2 focus:ring-blue-200 focus:ring-offset-2 focus:ring-offset-white",
      ].join(" ")}
    >
      {label}
    </button>
  );
}
