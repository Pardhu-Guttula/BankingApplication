import React from "react";
import { ArrowRight } from "lucide-react";
import { useIntl } from "react-intl";

export default function SectionHeader({ title, actionLabel, onAction = () => {}, actionIcon }) {
  const intl = useIntl();

  const ActionIcon = actionIcon;
  const resolvedActionLabel = actionLabel ?? intl.formatMessage({ id: "common.viewAll" });

  return (
    <header className="flex w-full items-center justify-between">
      <h2 className="text-[18px] font-bold leading-[24px] tracking-[-0.3px] text-[#0a0a0a]">{title}</h2>

      <button
        type="button"
        onClick={onAction}
        className="inline-flex h-[28px] items-center gap-[10px] rounded-[8px] px-2 text-[13px] font-medium leading-[18px] tracking-[-0.1px] text-[#030213] transition-colors hover:bg-black/5"
        aria-label={resolvedActionLabel}
      >
        <span>{resolvedActionLabel}</span>
        {ActionIcon ? (
          <ActionIcon className="h-4 w-4" aria-hidden="true" />
        ) : (
          <ArrowRight className="h-4 w-4" aria-hidden="true" />
        )}
      </button>
    </header>
  );
}