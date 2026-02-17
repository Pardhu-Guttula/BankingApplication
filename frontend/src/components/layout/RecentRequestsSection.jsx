import React from "react";
import { useIntl } from "react-intl";
import { ArrowRight } from "lucide-react";
import RequestRow from "../ui/RequestRow";

export default function RecentRequestsSection({
  title,
  requests = [],
  onViewAll = () => {},
  onRequestClick = () => {},
  viewAllLabel,
  viewAllAriaLabel,
  activeId,
  selectedLiveTemplate,
}) {
  const intl = useIntl();

  const computedTitle = title || intl.formatMessage({ id: "recentRequestsSection.title" });
  const computedViewAll = viewAllLabel || intl.formatMessage({ id: "common.viewAll" });
  const computedViewAllAria =
    viewAllAriaLabel || intl.formatMessage({ id: "recentRequestsSection.viewAllAria" });

  const liveTemplate =
    selectedLiveTemplate ||
    intl.formatMessage({ id: "recentRequestsSection.selectedLiveTemplate" });

  return (
    <section className="w-full bg-white border border-[rgba(0,0,0,0.1)] rounded-[14px]">
      <div className="px-6 pt-6 pb-[6px]">
        <div className="flex items-center justify-between gap-4 h-9">
          <h3 className="text-[16px] leading-[16px] font-medium text-[#0A0A0A]">
            {computedTitle}
          </h3>

          <button
            type="button"
            onClick={onViewAll}
            className={[
              "h-9 px-2 rounded-[8px]",
              "inline-flex items-center gap-[6px]",
              "text-[14px] leading-[20px] font-medium text-[#030213]",
              "hover:bg-[#F3F4F6]",
              "focus:outline-none focus-visible:ring-2 focus-visible:ring-[#2563EB]/40 focus-visible:ring-offset-2 focus-visible:ring-offset-white",
            ].join(" ")}
            aria-label={computedViewAllAria}
          >
            <span>{computedViewAll}</span>
            <ArrowRight className="h-4 w-4" />
          </button>
        </div>
      </div>

      <div className="px-6 pb-6">
        <div className="flex flex-col gap-4">
          {requests.map((r) => (
            <RequestRow
              key={r.id}
              title={r.title}
              timeAgo={r.timeAgo}
              statusLabel={r.statusLabel}
              statusVariant={r.statusVariant}
              onClick={() => onRequestClick(r.id)}
            />
          ))}
        </div>

        <div className="sr-only" aria-live="polite">
          {activeId ? liveTemplate.replace("{activeId}", activeId) : ""}
        </div>
      </div>
    </section>
  );
}