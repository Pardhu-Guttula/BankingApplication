import React, { useMemo, useState } from "react";
import { useIntl } from "react-intl";
import { BarChart3 } from "lucide-react";
import CategoryChip from "./CategoryChip";

export default function TrendingCategoriesBar({
  chips: chipsProp,
  defaultActiveLabel = "",
  onChipSelect = () => {},
}) {
  const intl = useIntl();

  const chips = useMemo(
    () =>
      chipsProp ?? [
        { label: intl.formatMessage({ id: "trendingCategories.mobile" }), count: 6 },
        { label: intl.formatMessage({ id: "trendingCategories.security" }), count: 8 },
        { label: intl.formatMessage({ id: "trendingCategories.webDevelopment" }), count: 15 },
        { label: intl.formatMessage({ id: "trendingCategories.devOps" }), count: 12 },
        { label: intl.formatMessage({ id: "trendingCategories.aiml" }), count: 10 },
        { label: intl.formatMessage({ id: "trendingCategories.cloud" }), count: 14 },
      ],
    [chipsProp, intl]
  );

  const initial = useMemo(() => {
    if (defaultActiveLabel) return defaultActiveLabel;
    return chips?.[0]?.label || "";
  }, [chips, defaultActiveLabel]);

  const [activeLabel, setActiveLabel] = useState(initial);

  return (
    <div className="w-full rounded-lg bg-white px-[26px] py-3">
      <div className="flex w-full items-center gap-4">
        <div className="flex items-center gap-2 shrink-0">
          <BarChart3 className="h-[18px] w-[18px] text-[#22C55E]" aria-hidden="true" />
          <span
            className="text-[14px] leading-[24px] tracking-[0.15px] text-black whitespace-nowrap"
            style={{ fontFamily: "Outfit, Roboto, Arial, sans-serif", fontWeight: 400 }}
          >
            {intl.formatMessage({ id: "trendingCategories.title" })}
          </span>
        </div>

        <div className="h-6 w-px bg-[#D9D9D9] shrink-0" aria-hidden="true" />

        <div className="flex flex-1 items-center justify-start gap-[11px] flex-wrap">
          {chips.map((chip) => (
            <CategoryChip
              key={chip.label}
              label={chip.label}
              count={chip.count}
              active={activeLabel === chip.label}
              onClick={(selected) => {
                setActiveLabel(selected.label);
                onChipSelect(selected);
              }}
            />
          ))}
        </div>
      </div>
    </div>
  );
}