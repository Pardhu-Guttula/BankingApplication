import React, { useMemo, useState } from "react";
import { useIntl } from "react-intl";
import { CheckCircle2, ChevronRight } from "lucide-react";
import { clamp } from "../utils/number";
import ProgressBar from "../ui/ProgressBar";
import SecondaryButton from "../ui/SecondaryButton";

export default function ProfileCompletionCTA({
  percent = 75,
  title,
  subtitle,
  buttonLabel,
  continueLabel,
  ariaLabel,
  progressAriaLabel,
  srPercentTemplate,
  continueAriaLabel,
  onCompleteProfile = () => {},
  onPercentChange = () => {},
}) {
  const intl = useIntl();
  const [isHovered, setIsHovered] = useState(false);
  const pct = useMemo(() => clamp(Number(percent) || 0, 0, 100), [percent]);

  const computedTitle = title || intl.formatMessage({ id: "profileCompletionCTA.title" });
  const computedSubtitle =
    subtitle || intl.formatMessage({ id: "profileCompletionCTA.subtitle" });
  const computedButtonLabel =
    buttonLabel || intl.formatMessage({ id: "profileCompletionCTA.buttonLabel" });
  const computedContinue = continueLabel || intl.formatMessage({ id: "profileCompletionCTA.continue" });
  const computedAria = ariaLabel || intl.formatMessage({ id: "profileCompletionCTA.ariaLabel" });
  const computedProgressAria =
    progressAriaLabel || intl.formatMessage({ id: "profileCompletionCTA.progressAriaLabel" });
  const computedSrPctTemplate =
    srPercentTemplate || intl.formatMessage({ id: "profileCompletionCTA.srPercentTemplate" });
  const computedContinueAria =
    continueAriaLabel || intl.formatMessage({ id: "profileCompletionCTA.continueAriaLabel" });

  return (
    <section
      className={[
        "w-full rounded-[14px] border border-[#bedbff] p-px",
        "bg-gradient-to-r from-[#eff6ff] to-[#faf5ff]",
      ].join(" ")}
      aria-label={computedAria}
    >
      <div className="rounded-[13px] px-6 py-6">
        <div className="flex items-start justify-between gap-6">
          <div className="min-w-0">
            <div className="flex items-center gap-2">
              <h3 className="text-[18px] font-bold leading-7 tracking-[-0.4395px] text-[#0a0a0a]">
                {computedTitle}
              </h3>
              <span className="sr-only">
                {computedSrPctTemplate.replace("{pct}", String(pct))}
              </span>
            </div>
            <p className="mt-1 text-[14px] font-normal leading-5 tracking-[-0.1504px] text-[#4a5565]">
              {computedSubtitle}
            </p>
          </div>

          <div className="shrink-0 text-right">
            <div className="text-[24px] font-bold leading-8 tracking-[0.0703px] text-[#155dfc]">
              {pct}%
            </div>
          </div>
        </div>

        <div className="mt-4">
          <ProgressBar value={pct} onChange={onPercentChange} aria-label={computedProgressAria} />
        </div>

        <div className="mt-6 flex flex-wrap items-center gap-10">
          <SecondaryButton
            onClick={onCompleteProfile}
            className="w-[144px]"
            icon={CheckCircle2}
            onMouseEnter={() => setIsHovered(true)}
            onMouseLeave={() => setIsHovered(false)}
          >
            {computedButtonLabel}
          </SecondaryButton>

          <button
            type="button"
            onClick={onCompleteProfile}
            className={[
              "inline-flex items-center gap-1 text-sm font-medium",
              "text-[#030213] hover:text-[#111827]",
              "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#2563eb] focus-visible:ring-offset-2 focus-visible:ring-offset-transparent",
              isHovered ? "underline underline-offset-4" : "",
            ].join(" ")}
            aria-label={computedContinueAria}
          >
            {computedContinue}
            <ChevronRight className="h-4 w-4" />
          </button>
        </div>
      </div>
    </section>
  );
}