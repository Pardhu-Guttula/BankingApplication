import React from "react";
import { ArrowRight } from "lucide-react";
import { useIntl } from "react-intl";

export default function SectionHeader({ title, actionLabel, onAction = () => {} }) {
  const intl = useIntl();

  const resolvedTitle = title ?? intl.formatMessage({ id: "sectionHeader.title" });
  const resolvedActionLabel = actionLabel ?? intl.formatMessage({ id: "sectionHeader.actionLabel" });

  return (
    <header className="flex w-full items-center justify-between">
      <h2 className="text-[18px] font-bold leading-[24px] tracking-[-0.3px] text-[#0A0A0A]">
        {resolvedTitle}
      </h2>

      <button
        type="button"
        onClick={onAction}
        className="inline-flex h-8 items-center gap-2 rounded-[8px] px-2 text-[13px] font-medium leading-[18px] tracking-[-0.15px] text-[#030213] transition-colors hover:bg-black/5 focus:outline-none focus-visible:ring-2 focus-visible:ring-[#030213]/30"
        aria-label={resolvedActionLabel}
      >
        <span>{resolvedActionLabel}</span>
        <ArrowRight className="h-4 w-4" aria-hidden="true" />
      </button>
    </header>
  );
}