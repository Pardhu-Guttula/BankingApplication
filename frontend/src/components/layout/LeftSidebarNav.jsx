import React, { useState } from "react";
import { useIntl } from "react-intl";
import NavItemRow from "../ui/NavItemRow";
import SupportCard from "../ui/SupportCard";

export default function LeftSidebarNav({
  initialActiveKey = "dashboard",
  onNavigate = () => {},
  onContactSupport = () => {},
  items = [],
}) {
  const intl = useIntl();
  const [activeKey, setActiveKey] = useState(initialActiveKey);

  function handleNavigate(nextKey) {
    setActiveKey(nextKey);
    onNavigate(nextKey);
  }

  return (
    <aside className="w-64 bg-white border-r border-[#E5E7EB] flex flex-col justify-between min-h-[722px]">
      <nav className="w-full px-4 pt-4">
        <div className="flex flex-col gap-1">
          {items.map((item) => (
            <NavItemRow
              key={item.itemKey}
              {...item}
              active={item.itemKey === activeKey}
              onNavigate={handleNavigate}
              pendingAriaTemplate={intl.formatMessage({
                id: "leftSidebarNav.pendingAriaTemplate",
              })}
            />
          ))}
        </div>
      </nav>

      <SupportCard
        onContactSupport={onContactSupport}
        title={intl.formatMessage({ id: "supportCard.title" })}
        subtitle={intl.formatMessage({ id: "supportCard.subtitle" })}
        buttonLabel={intl.formatMessage({ id: "supportCard.contactSupport" })}
      />
    </aside>
  );
}