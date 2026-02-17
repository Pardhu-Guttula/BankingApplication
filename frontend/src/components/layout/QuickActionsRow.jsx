import React, { useMemo, useState } from "react";
import { useIntl } from "react-intl";
import QuickActionCard from "../ui/QuickActionCard";

export default function QuickActionsRow({ onActionClick = () => {}, actions: actionsProp }) {
  const intl = useIntl();

  const actions = useMemo(
    () =>
      actionsProp || [
        { id: "open-account", label: intl.formatMessage({ id: "quickActionsRow.openNewAccount" }) },
        { id: "modify-services", label: intl.formatMessage({ id: "quickActionsRow.modifyServices" }) },
        { id: "track-requests", label: intl.formatMessage({ id: "quickActionsRow.trackRequests" }) },
        { id: "digital-banking", label: intl.formatMessage({ id: "quickActionsRow.digitalBanking" }) },
      ],
    [actionsProp, intl]
  );

  const [activeId, setActiveId] = useState(null);

  return (
    <section aria-label={intl.formatMessage({ id: "quickActionsRow.ariaLabel" })} className="w-full">
      <div className="grid w-full grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
        {actions.map(({ id, label, Icon }) => (
          <QuickActionCard
            key={id}
            id={id}
            label={label}
            Icon={Icon}
            active={activeId === id}
            onActiveChange={setActiveId}
            onClick={(actionId) => onActionClick(actionId)}
          />
        ))}
      </div>
    </section>
  );
}