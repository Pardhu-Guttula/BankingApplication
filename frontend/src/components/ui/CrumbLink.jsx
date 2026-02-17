import React from "react";
import { useIntl } from "react-intl";

export default function CrumbLink({ label, href, isCurrent, onNavigate }) {
  useIntl();

  const common = "text-[16px] leading-[1.5] font-['Outfit',sans-serif] transition-colors";
  const active = isCurrent
    ? "font-medium text-[rgba(0,0,0,0.87)]"
    : "font-normal text-[rgba(0,0,0,0.6)] hover:text-[rgba(0,0,0,0.87)]";

  if (!href || isCurrent) {
    return (
      <span aria-current={isCurrent ? "page" : undefined} className={`${common} ${active}`}>
        {label}
      </span>
    );
  }

  return (
    <a
      href={href}
      onClick={(e) => {
        e.preventDefault();
        onNavigate(href);
      }}
      className={`${common} ${active}`}
    >
      {label}
    </a>
  );
}