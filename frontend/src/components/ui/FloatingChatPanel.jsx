import React from "react";
import { useIntl } from "react-intl";
import { MessageSquareText, X } from "lucide-react";

export default function FloatingChatPanel({
  isOpen,
  onClose = () => {},
  title,
  subtitle,
  onPrimaryAction = () => {},
  primaryActionLabel,
}) {
  const intl = useIntl();

  const resolvedTitle = title ?? intl.formatMessage({ id: "assistanceWidget.title" });
  const resolvedSubtitle = subtitle ?? intl.formatMessage({ id: "assistanceWidget.subtitle" });
  const resolvedPrimary = primaryActionLabel ?? intl.formatMessage({ id: "assistanceWidget.primaryAction" });

  return (
    <div
      className={[
        "fixed right-6 top-[62%] z-40",
        "translate-y-[-50%]",
        "w-[320px]",
        "transition-all duration-200 ease-out",
        isOpen ? "opacity-100 pointer-events-auto translate-x-0" : "opacity-0 pointer-events-none translate-x-2",
      ].join(" ")}
      role="dialog"
      aria-modal="false"
      aria-hidden={!isOpen}
      aria-label={intl.formatMessage({ id: "assistanceWidget.panelAria" })}
    >
      <div className="rounded-2xl bg-white shadow-[0px_10px_30px_rgba(0,0,0,0.12)] ring-1 ring-black/5 overflow-hidden">
        <div className="flex items-center justify-between px-4 py-3 bg-[#211747] text-white">
          <div className="flex items-center gap-2">
            <MessageSquareText className="h-5 w-5" aria-hidden="true" />
            <div className="leading-tight">
              <div className="text-[13px] font-medium tracking-[0.2px]">{resolvedTitle}</div>
              <div className="text-[12px] text-white/80">{resolvedSubtitle}</div>
            </div>
          </div>

          <button
            type="button"
            onClick={onClose}
            className="h-8 w-8 rounded-lg grid place-items-center hover:bg-white/10 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-white/70"
            aria-label={intl.formatMessage({ id: "assistanceWidget.closeAria" })}
          >
            <X className="h-4 w-4" aria-hidden="true" />
          </button>
        </div>

        <div className="px-4 py-4">
          <p className="text-[13px] text-[#1D1B20]/70 leading-5">{intl.formatMessage({ id: "assistanceWidget.body" })}</p>

          <button
            type="button"
            onClick={onPrimaryAction}
            className={[
              "mt-4 w-full",
              "h-10 rounded-xl",
              "bg-[#211747] text-white",
              "text-[13px] font-medium tracking-[0.3px]",
              "shadow-[0px_1px_5px_0px_rgba(0,0,0,0.12),0px_2px_2px_0px_rgba(0,0,0,0.14),0px_3px_1px_-2px_rgba(0,0,0,0.2)]",
              "hover:brightness-110 active:brightness-95",
              "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#211747] focus-visible:ring-offset-2",
            ].join(" ")}
          >
            {resolvedPrimary}
          </button>
        </div>
      </div>
    </div>
  );
}