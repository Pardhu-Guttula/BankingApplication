import React from "react";
import { useIntl } from "react-intl";

export default function NavLink({ id, label, active = false, onNavigate = () => {} }) {
  useIntl();

  return (
    <button
      type="button"
      onClick={() => onNavigate(id)}
      className={[
        "h-[33px] rounded-lg px-[5px] text-[13px] leading-[22.5px]",
        "font-medium font-['Outfit',sans-serif]",
        "text-[#314158] hover:bg-black/[0.04] active:bg-black/[0.06]",
        "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#211747]/30",
        active ? "underline underline-offset-[6px]" : "",
      ].join(" ")}
    >
      {label}
    </button>
  );
}