import React, { useMemo, useState } from "react";
import { useIntl } from "react-intl";
import { BarChart3, Settings, Wrench } from "lucide-react";
import CategoryTabButton from "./CategoryTabButton";

const ICONS = {
  wrench: Wrench,
  settings: Settings,
  barchart: BarChart3,
};

export default function CategoryToggleButtons({
  tabs: tabsProp,
  defaultActiveId = "engineering",
  activeId: controlledActiveId,
  onActiveChange = () => {},
  className = "",
}) {
  const intl = useIntl();

  const tabs = useMemo(
    () =>
      tabsProp ?? [
        { id: "engineering", label: intl.formatMessage({ id: "categoryTabs.engineering" }), count: 8, iconId: "wrench" },
        { id: "operations", label: intl.formatMessage({ id: "categoryTabs.operations" }), count: 6, iconId: "settings" },
        { id: "decisioning", label: intl.formatMessage({ id: "categoryTabs.decisioning" }), count: 6, iconId: "barchart" },
      ],
    [tabsProp, intl]
  );

  const [uncontrolledActiveId, setUncontrolledActiveId] = useState(defaultActiveId);

  const activeId = controlledActiveId !== undefined ? controlledActiveId : uncontrolledActiveId;

  function handleSelect(nextId) {
    if (controlledActiveId === undefined) setUncontrolledActiveId(nextId);
    onActiveChange(nextId);
  }

  return (
    <div className={["w-full", className].join(" ")}>
      <div className="mx-auto flex w-full max-w-[1120px] flex-wrap items-center justify-center gap-4">
        {tabs.map(({ id, label, count, iconId }) => (
          <CategoryTabButton
            key={id}
            id={id}
            label={label}
            count={count}
            Icon={ICONS[iconId]}
            active={id === activeId}
            onSelect={handleSelect}
          />
        ))}
      </div>
    </div>
  );
}