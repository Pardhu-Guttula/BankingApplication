import React from "react";

export default function NavItemRow({
  itemKey,
  label,
  Icon,
  active,
  badgeCount,
  onNavigate = () => {},
  pendingAriaTemplate,
}) {
  return (
    <button
      type="button"
      onClick={() => onNavigate(itemKey)}
      className={[
        "w-full rounded-[10px] px-4",
        "h-11",
        "flex items-center gap-3",
        "text-left",
        "transition-colors",
        active ? "bg-[#EFF6FF]" : "hover:bg-slate-50",
        "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#2563EB] focus-visible:ring-offset-2",
      ].join(" ")}
      aria-current={active ? "page" : undefined}
    >
      <Icon
        className={["h-5 w-5", active ? "text-[#155DFC]" : "text-[#364153]"].join(" ")}
        aria-hidden="true"
      />
      <span
        className={[
          "flex-1 text-[14px] leading-5 tracking-[-0.1504px] font-medium",
          active ? "text-[#155DFC]" : "text-[#364153]",
        ].join(" ")}
      >
        {label}
      </span>

      {typeof badgeCount === "number" ? (
        <span
          className="h-[22px] min-w-[26px] rounded-[8px] bg-[#ECEEF2] px-[9px] py-[3px] text-center text-[12px] leading-4 font-medium text-[#030213]"
          aria-label={
            pendingAriaTemplate
              ? pendingAriaTemplate.replace("{badgeCount}", String(badgeCount))
              : `${badgeCount} pending`
          }
        >
          {badgeCount}
        </span>
      ) : null}
    </button>
  );
}