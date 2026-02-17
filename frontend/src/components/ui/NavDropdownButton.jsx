import React, { useMemo } from "react";
import { useIntl } from "react-intl";
import { ChevronDown } from "lucide-react";

export default function NavDropdownButton({ id, label, active = false, open = false, onToggle = () => {}, onNavigate = () => {} }) {
  const intl = useIntl();

  const menuItems = useMemo(
    () => [
      { key: "overview", label: intl.formatMessage({ id: "globalHeader.dropdown.overview" }) },
      { key: "browse", label: intl.formatMessage({ id: "globalHeader.dropdown.browse" }) },
      { key: "saved", label: intl.formatMessage({ id: "globalHeader.dropdown.saved" }) },
    ],
    [intl]
  );

  const base =
    "h-[33px] inline-flex items-center gap-1 rounded-md px-[10px] py-[5px] text-[13px] leading-[22.5px] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#211747]/30";
  const activeCls = "bg-[#211747] text-white hover:bg-[#211747]/95 active:bg-[#211747]/90";
  const inactiveCls = "text-[#314158] hover:bg-black/[0.04] active:bg-black/[0.06]";

  return (
    <div className="relative">
      <button
        type="button"
        onClick={() => onToggle(id)}
        className={[base, "font-['Outfit',sans-serif]", active ? activeCls : inactiveCls].join(" ")}
        aria-haspopup="menu"
        aria-expanded={open}
      >
        <span className={active ? "font-normal" : "font-medium"}>{label}</span>
        <ChevronDown className={["h-4 w-4", open ? "rotate-180" : ""].join(" ")} aria-hidden="true" />
      </button>

      {open ? (
        <div
          role="menu"
          className="absolute left-0 top-[calc(100%+8px)] z-20 min-w-[220px] overflow-hidden rounded-xl border border-black/10 bg-white shadow-[0_12px_30px_rgba(0,0,0,0.12)]"
        >
          {menuItems.map((item) => (
            <button
              key={item.key}
              type="button"
              role="menuitem"
              onClick={() => onNavigate(`${id}:${item.key}`)}
              className="flex w-full items-center justify-between px-3 py-2 text-left text-[13px] font-medium text-[#314158] hover:bg-black/[0.04] focus-visible:outline-none focus-visible:bg-black/[0.04]"
            >
              {item.label}
            </button>
          ))}
        </div>
      ) : null}
    </div>
  );
}