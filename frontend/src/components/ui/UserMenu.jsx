import React, { useMemo } from "react";
import { useIntl } from "react-intl";
import { ChevronDown } from "lucide-react";

export default function UserMenu({ userName = "John Doe", avatarSrc, open = false, onToggle = () => {}, onAction = () => {} }) {
  const intl = useIntl();

  const items = useMemo(
    () => [
      { id: "profile", label: intl.formatMessage({ id: "userMenu.profile" }) },
      { id: "settings", label: intl.formatMessage({ id: "userMenu.settings" }) },
      { id: "signout", label: intl.formatMessage({ id: "userMenu.signOut" }) },
    ],
    [intl]
  );

  return (
    <div className="relative">
      <button
        type="button"
        onClick={onToggle}
        className="flex items-center gap-[13px] rounded-xl pr-[2px] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#211747]/30"
        aria-haspopup="menu"
        aria-expanded={open}
      >
        <span className="grid h-10 w-10 place-items-center overflow-hidden rounded-full bg-[#eaddff]">
          <img alt="" src={avatarSrc} className="h-6 w-6 object-contain opacity-80" draggable={false} />
        </span>

        <span className="text-[16px] font-medium tracking-[0.15px] text-[#64748b] font-['Outfit',sans-serif]">{userName}</span>

        <ChevronDown className={["h-5 w-5 text-[#64748b]", open ? "rotate-180" : ""].join(" ")} aria-hidden="true" />
      </button>

      {open ? (
        <div
          role="menu"
          className="absolute right-0 top-[calc(100%+10px)] z-20 min-w-[200px] overflow-hidden rounded-xl border border-black/10 bg-white shadow-[0_12px_30px_rgba(0,0,0,0.12)]"
        >
          {items.map((item) => (
            <button
              key={item.id}
              type="button"
              role="menuitem"
              onClick={() => onAction(item.id)}
              className="flex w-full items-center px-3 py-2 text-left text-[13px] font-medium text-[#314158] hover:bg-black/[0.04] focus-visible:outline-none focus-visible:bg-black/[0.04]"
            >
              {item.label}
            </button>
          ))}
        </div>
      ) : null}
    </div>
  );
}