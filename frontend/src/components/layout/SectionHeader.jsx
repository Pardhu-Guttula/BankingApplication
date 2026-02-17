import React from "react";
import { useIntl } from "react-intl";
import { ArrowRight } from "lucide-react";

export default function SectionHeader({ title, actionLabel, onAction = () => {} }) {
  const intl = useIntl();

  return (
    <header className="flex items-center justify-between gap-6">
      <h2 className="text-[20px] font-bold leading-[28px] tracking-[-0.4492px] text-[#0a0a0a]">
        {title}
      </h2>

      <button
        type="button"
        onClick={onAction}
        className="inline-flex h-9 items-center gap-[11px] rounded-[8px] px-2 text-[14px] font-medium leading-[20px] tracking-[-0.1504px] text-[#030213] transition-colors hover:bg-black/5 focus:outline-none focus-visible:ring-2 focus-visible:ring-[#111827]/20"
        aria-label={actionLabel || intl.formatMessage({ id: "productsForYou.viewAll" })}
      >
        <span>{actionLabel}</span>
        <ArrowRight className="h-4 w-4" aria-hidden="true" />
      </button>
    </header>
  );
}