import React, { useId } from "react";
import { useIntl } from "react-intl";
import { Search, X } from "lucide-react";

export default function SearchField({
  value,
  onChange = () => {},
  placeholder,
  onClear = () => {},
  onSubmit = () => {},
  disabled = false,
}) {
  const intl = useIntl();
  const inputId = useId();
  const hasValue = (value || "").length > 0;

  const resolvedPlaceholder = placeholder ?? intl.formatMessage({ id: "searchBar.placeholder" });

  return (
    <form
      className="w-full"
      role="search"
      onSubmit={(e) => {
        e.preventDefault();
        onSubmit(value);
      }}
    >
      <label htmlFor={inputId} className="sr-only">
        {intl.formatMessage({ id: "searchField.label" })}
      </label>

      <div
        className={[
          "group flex h-10 w-full items-center rounded-full border bg-white",
          "border-[#D9D9D9]",
          "shadow-[0_1px_0_rgba(0,0,0,0.02)]",
          "transition-colors",
          disabled ? "opacity-60" : "hover:border-[#C9C9C9]",
          "focus-within:border-[#2F2A60] focus-within:ring-2 focus-within:ring-[#2F2A60]/15",
        ].join(" ")}
      >
        <div className="flex items-center pl-4 pr-2">
          <Search className="h-4 w-4 text-[#6B6B75]" aria-hidden="true" />
        </div>

        <input
          id={inputId}
          type="search"
          value={value}
          disabled={disabled}
          onChange={(e) => onChange(e.target.value)}
          placeholder={resolvedPlaceholder}
          className={["h-full w-full bg-transparent pr-2 text-[13px] text-[#1D1B20] outline-none", "placeholder:text-[#6B6B75]"].join(" ")}
        />

        <div className="flex items-center gap-1 pr-2">
          {hasValue && !disabled && (
            <button
              type="button"
              onClick={() => {
                onChange("");
                onClear();
              }}
              className={[
                "inline-flex h-8 w-8 items-center justify-center rounded-full",
                "text-[#6B6B75] hover:bg-[#F3F3F6] hover:text-[#1D1B20]",
                "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#2F2A60]/25",
              ].join(" ")}
              aria-label={intl.formatMessage({ id: "searchField.clearAria" })}
            >
              <X className="h-4 w-4" aria-hidden="true" />
            </button>
          )}
        </div>
      </div>
    </form>
  );
}