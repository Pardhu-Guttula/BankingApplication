import React from "react";
import { ArrowRight } from "lucide-react";
import { useIntl } from "react-intl";

export default function SectionHeader({
  title,
  actionLabel,
  onAction = () => {},
  actionIcon,
}) {
  const intl = useIntl();
  const ActionIcon = actionIcon;

  const resolvedActionLabel =
    actionLabel ?? intl.formatMessage({ id: "common.viewAll" });

  return (
    <header className="flex w-full items-center justify-between gap-4">
      <h2 className="text-[20px] font-bold leading-[28px] tracking-[-0.4492px] text-[#0A0A0A]">
        {title}
      </h2>

      <button
        type="button"
        onClick={onAction}
        className="inline-flex h-[36px] items-center gap-[11px] rounded-[8px] px-2 text-[14px] font-medium leading-[20px] tracking-[-0.1504px] text-[#030213] transition-colors hover:bg-black/5 focus:outline-none focus-visible:ring-2 focus-visible:ring-[#030213]/30 focus-visible:ring-offset-2"
        aria-label={resolvedActionLabel}
      >
        <span>{resolvedActionLabel}</span>
        {ActionIcon ? (
          <ActionIcon className="h-[16px] w-[16px]" aria-hidden="true" />
        ) : (
          <ArrowRight className="h-[16px] w-[16px]" aria-hidden="true" />
        )}
      </button>
    </header>
  );
}