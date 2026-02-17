import React from "react";
import { useIntl } from "react-intl";
import { Sparkles } from "lucide-react";
import TagChip from "./TagChip";
import clampTextClass from "../utils/clampTextClass";

export default function SolutionCard({ id, title, description, tags, onClick = () => {}, onTagClick = () => {}, iconSrc }) {
  const intl = useIntl();

  return (
    <button
      type="button"
      onClick={() => onClick(id)}
      className="group flex h-[211px] w-full flex-col rounded-[10px] border border-[#E7E7EC] bg-white p-5 text-left shadow-[0_2px_10px_rgba(16,24,40,0.08)] transition-shadow hover:shadow-[0_6px_18px_rgba(16,24,40,0.12)] focus:outline-none focus-visible:ring-2 focus-visible:ring-[#2F2A60]/25"
      aria-label={intl.formatMessage({ id: "solutionCard.openAria" }, { title })}
    >
      <div className="flex items-center gap-3">
        <div className="flex h-9 w-9 items-center justify-center rounded-[8px] bg-[#2F2A60] shadow-[0_2px_6px_rgba(47,42,96,0.25)]">
          {iconSrc ? <img alt="" src={iconSrc} className="h-5 w-5" /> : <Sparkles className="h-5 w-5 text-white" aria-hidden="true" />}
        </div>

        <div className="min-w-0">
          <div className="truncate text-[14px] font-semibold leading-5 text-[#111111]">{title}</div>
        </div>
      </div>

      <div className="mt-3 flex-1">
        <p
          className={`text-[12.5px] leading-[18px] text-[#6B6B75] ${clampTextClass(4)}`}
          style={{
            display: "-webkit-box",
            WebkitLineClamp: 4,
            WebkitBoxOrient: "vertical",
            overflow: "hidden",
          }}
        >
          {description}
        </p>
      </div>

      <div className="mt-4 flex flex-wrap gap-2">
        {(tags || []).map((t) => (
          <TagChip key={t} label={t} onClick={() => onTagClick(t, id)} />
        ))}
      </div>
    </button>
  );
}