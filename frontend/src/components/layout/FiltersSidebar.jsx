import React, { useId, useMemo, useState } from "react";
import { useIntl } from "react-intl";
import { Check, SlidersHorizontal } from "lucide-react";
import FilterGroup from "../ui/FilterGroup";
import CheckboxItem from "../ui/CheckboxItem";
import PriceField from "../ui/PriceField";

export default function FiltersSidebar({
  categories,
  selectedCategoryIds,
  minPrice,
  maxPrice,
  onToggleCategory = () => {},
  onChangeMinPrice = () => {},
  onChangeMaxPrice = () => {},
  onApply = () => {},
  onClear = () => {},
}) {
  const intl = useIntl();

  const fallbackCategories = useMemo(
    () => [
      { id: "all", label: intl.formatMessage({ id: "common.all" }), count: null },
      {
        id: "electronics",
        label: intl.formatMessage({ id: "common.electronics" }),
        count: 6,
      },
      {
        id: "jewelery",
        label: intl.formatMessage({ id: "common.jewelery" }),
        count: 4,
      },
      {
        id: "mens-clothing",
        label: intl.formatMessage({ id: "common.mensClothing" }),
        count: 4,
      },
      {
        id: "womens-clothing",
        label: intl.formatMessage({ id: "common.womensClothing" }),
        count: 6,
      },
    ],
    [intl]
  );

  const resolvedCategories = categories?.length ? categories : fallbackCategories;

  const [localSelected, setLocalSelected] = useState(
    Array.isArray(selectedCategoryIds) ? selectedCategoryIds : ["all"]
  );
  const [localMin, setLocalMin] = useState(minPrice ?? "");
  const [localMax, setLocalMax] = useState(maxPrice ?? "");

  const minId = useId();
  const maxId = useId();

  function isChecked(id) {
    return localSelected.includes(id);
  }

  function toggleExclusive(id) {
    const next = [id];
    setLocalSelected(next);
    onToggleCategory(id);
  }

  function handleClear() {
    setLocalSelected(["all"]);
    setLocalMin("");
    setLocalMax("");
    onClear();
  }

  function handleApply() {
    onApply({
      selectedCategoryIds: localSelected,
      minPrice: localMin,
      maxPrice: localMax,
    });
  }

  return (
    <aside className="sticky top-0 w-[280px] shrink-0 rounded-[16px] bg-white p-[24px] shadow-[0px_1px_3px_0px_rgba(0,0,0,0.1),0px_1px_2px_0px_rgba(0,0,0,0.06)]">
      <div className="flex flex-col gap-[16px]">
        <div className="flex items-center justify-between border-b border-[#E2E8F0] pb-[17px]">
          <div className="flex items-center gap-[8px]">
            <SlidersHorizontal className="h-[18px] w-[18px] text-[#1E293B]" />
            <h3 className="text-[18px] font-bold leading-[28.8px] text-[#1E293B]">
              {intl.formatMessage({ id: "filtersSidebar.title" })}
            </h3>
          </div>

          <button
            type="button"
            onClick={handleClear}
            className="text-[13px] font-medium text-[#4361EE] hover:underline focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#4361EE]/40"
          >
            {intl.formatMessage({ id: "common.clear" })}
          </button>
        </div>

        <FilterGroup title={intl.formatMessage({ id: "filtersSidebar.categoriesTitle" })}>
          <div className="pt-[12px]">
            {resolvedCategories.map((c) => {
              const label =
                c.count === null || c.count === undefined
                  ? c.label
                  : `${c.label} (${c.count})`;

              return (
                <CheckboxItem
                  key={c.id}
                  checked={isChecked(c.id)}
                  label={label}
                  onChange={() => toggleExclusive(c.id)}
                />
              );
            })}
          </div>
        </FilterGroup>

        <FilterGroup
          title={intl.formatMessage({ id: "filtersSidebar.priceTitle" })}
          className="pb-[41px]"
        >
          <div className="flex items-center gap-[12px]">
            <PriceField
              label={intl.formatMessage({ id: "common.min" })}
              inputId={minId}
              value={localMin}
              onChange={(v) => {
                setLocalMin(v);
                onChangeMinPrice(v);
              }}
            />
            <span className="pb-[2px] text-[16px] leading-[25.6px] text-[#1E293B]">
              -
            </span>
            <PriceField
              label={intl.formatMessage({ id: "common.max" })}
              inputId={maxId}
              value={localMax}
              onChange={(v) => {
                setLocalMax(v);
                onChangeMaxPrice(v);
              }}
            />
          </div>
        </FilterGroup>

        <button
          type="button"
          onClick={handleApply}
          className="flex w-full items-center justify-center gap-[8px] rounded-[8px] bg-[#4361EE] p-[14px] text-[16px] font-semibold text-white shadow-sm transition-colors hover:bg-[#3653E6] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#4361EE]/40 active:bg-[#2F49D8]"
        >
          <Check className="h-[16px] w-[16px] text-white" strokeWidth={3} />
          {intl.formatMessage({ id: "common.apply" })}
        </button>
      </div>
    </aside>
  );
}