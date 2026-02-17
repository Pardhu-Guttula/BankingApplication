import React, { useId, useMemo, useState } from "react";
import { useIntl } from "react-intl";
import SortSelect from "../ui/SortSelect";
import IconToggleButton from "../ui/IconToggleButton";
import { LayoutGrid, List } from "lucide-react";

export default function ProductsToolbar({
  showing = 12,
  total = 20,
  sortValue: sortValueProp,
  sortOptions: sortOptionsProp,
  onSortChange = () => {},
  viewMode: viewModeProp,
  onViewModeChange = () => {},
}) {
  const intl = useIntl();
  const sortSelectId = useId();

  const sortOptions = useMemo(
    () =>
      sortOptionsProp || [
        { value: "featured", label: intl.formatMessage({ id: "productsToolbar.sort.featured" }) },
        { value: "price-asc", label: intl.formatMessage({ id: "productsToolbar.sort.priceAsc" }) },
        { value: "price-desc", label: intl.formatMessage({ id: "productsToolbar.sort.priceDesc" }) },
        { value: "rating-desc", label: intl.formatMessage({ id: "productsToolbar.sort.rating" }) },
        { value: "name-asc", label: intl.formatMessage({ id: "productsToolbar.sort.nameAsc" }) },
      ],
    [sortOptionsProp, intl]
  );

  const isSortControlled = sortValueProp !== undefined;
  const [sortValueUncontrolled, setSortValueUncontrolled] = useState(
    sortOptions[0]?.value || "featured"
  );
  const sortValue = isSortControlled ? sortValueProp : sortValueUncontrolled;

  const isViewControlled = viewModeProp !== undefined;
  const [viewModeUncontrolled, setViewModeUncontrolled] = useState("grid");
  const viewMode = isViewControlled ? viewModeProp : viewModeUncontrolled;

  function handleSortChange(next) {
    if (!isSortControlled) setSortValueUncontrolled(next);
    onSortChange(next);
  }

  function handleViewModeChange(next) {
    if (!isViewControlled) setViewModeUncontrolled(next);
    onViewModeChange(next);
  }

  return (
    <div
      className={[
        "w-full shrink-0",
        "bg-white rounded-[12px]",
        "px-5 py-4",
        "shadow-[0px_1px_3px_0px_rgba(0,0,0,0.1),0px_1px_2px_0px_rgba(0,0,0,0.06)]",
        "flex items-center justify-between gap-[519px]",
      ].join(" ")}
      data-name="div.products-toolbar"
    >
      <span className="text-[#475569] text-[14px] leading-[22.4px] whitespace-nowrap">
        <span className="font-normal">
          {intl.formatMessage({ id: "productsToolbar.showingPrefix" })}
        </span>
        <span className="font-bold">{showing}</span>
        <span className="font-normal">
          {intl.formatMessage({ id: "productsToolbar.of" })}
        </span>
        <span className="font-bold">{total}</span>
        <span className="font-normal">
          {intl.formatMessage({ id: "productsToolbar.productsSuffix" })}
        </span>
      </span>

      <div
        className="flex items-center gap-[20px] shrink-0"
        data-name="div.toolbar-right"
      >
        <div
          className="flex items-center gap-[10px] shrink-0"
          data-name="div.sort-by"
        >
          <label
            htmlFor={sortSelectId}
            className="text-[#475569] text-[14px] leading-[22.4px] whitespace-nowrap"
          >
            {intl.formatMessage({ id: "productsToolbar.sortLabel" })}
          </label>

          <SortSelect
            id={sortSelectId}
            value={sortValue}
            options={sortOptions}
            onChange={handleSortChange}
            ariaLabel="Sort products"
          />
        </div>

        <div
          className="flex items-start gap-1 shrink-0"
          data-name="div.view-toggle"
        >
          <IconToggleButton
            active={viewMode === "grid"}
            label={intl.formatMessage({ id: "productsToolbar.gridView" })}
            onClick={() => handleViewModeChange("grid")}
          >
            <LayoutGrid className="h-4 w-4" aria-hidden="true" />
          </IconToggleButton>

          <IconToggleButton
            active={viewMode === "list"}
            label={intl.formatMessage({ id: "productsToolbar.listView" })}
            onClick={() => handleViewModeChange("list")}
          >
            <List className="h-4 w-4" aria-hidden="true" />
          </IconToggleButton>
        </div>
      </div>
    </div>
  );
}