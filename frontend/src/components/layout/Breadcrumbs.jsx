import React from "react";
import { useIntl } from "react-intl";
import CrumbLink from "../ui/CrumbLink";
import BreadcrumbSeparator from "../ui/BreadcrumbSeparator";

export default function Breadcrumbs({
  items = [
    { label: "Home", href: "/" },
    { label: "Foundational Solutions", href: "/foundational-solutions" },
  ],
  onNavigate = () => {},
}) {
  useIntl();

  return (
    <nav aria-label="Breadcrumb" className="w-full bg-white h-[44px] flex items-center">
      <div className="w-full max-w-[1120px] mx-auto px-6">
        <ol className="flex items-center flex-wrap">
          {items.map((item, idx) => {
            const isLast = idx === items.length - 1;
            return (
              <li key={`${item.label}-${idx}`} className="flex items-center">
                <CrumbLink label={item.label} href={item.href} isCurrent={isLast} onNavigate={onNavigate} />
                {!isLast ? <BreadcrumbSeparator /> : null}
              </li>
            );
          })}
        </ol>
      </div>
    </nav>
  );
}