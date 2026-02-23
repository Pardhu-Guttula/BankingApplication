import React from "react";
import { ArrowRight } from "lucide-react";
import { useIntl } from "react-intl";

export default function SectionHeader({
  title,
  actionLabel,
  onAction = () => {},
  actionAriaLabel,
}) {
  const intl = useIntl();

  const resolvedActionAriaLabel =
    actionAriaLabel ??
    intl.formatMessage({ id: "sectionHeader.actionAriaLabel" });

  return (
    <header className="flex w-full items-center justify-between">
      <h2 className="text-[18px] font-semibold leading-[24px] tracking-[-0.3px] text-[#0A0A0A]">
        {title}
      </h2>

      <button
        type="button"
        onClick={onAction}
        aria-label={resolvedActionAriaLabel}
        className="inline-flex h-[28px] items-center gap-[10px] rounded-[8px] px-1 text-[13px] font-medium leading-[18px] tracking-[-0.12px] text-[#030213] transition-colors hover:bg-black/[0.04] focus:outline-none focus-visible:ring-2 focus-visible:ring-[#030213]/25 focus-visible:ring-offset-2"
      >
        <span>{actionLabel}</span>
        <ArrowRight className="h-4 w-4" aria-hidden="true" />
      </button>
    </header>
  );
}