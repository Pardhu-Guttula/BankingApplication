import React from "react";
import { ArrowRight } from "lucide-react";
import { useIntl } from "react-intl";

export default function SectionHeader({
  title,
  actionLabel,
  onAction = () => {},
}) {
  const intl = useIntl();

  const resolvedTitle =
    title || intl.formatMessage({ id: "productsForYou.title" });
  const resolvedActionLabel =
    actionLabel || intl.formatMessage({ id: "common.viewAll" });

  return (
    <header className="flex w-full items-center justify-between gap-4">
      <h2 className="text-[20px] font-bold leading-[28px] tracking-[-0.4492px] text-[#0A0A0A]">
        {resolvedTitle}
      </h2>

      <button
        type="button"
        onClick={onAction}
        className="inline-flex items-center gap-[10px] rounded-[8px] px-2 py-1 text-[14px] font-medium leading-[20px] tracking-[-0.1504px] text-[#030213] transition-colors hover:bg-black/5 focus:outline-none focus-visible:ring-2 focus-visible:ring-[#030213]/20"
        aria-label={resolvedActionLabel}
      >
        <span>{resolvedActionLabel}</span>
        <ArrowRight className="h-4 w-4" aria-hidden="true" />
      </button>
    </header>
  );
}