import React, { useMemo, useState } from "react";
import { useIntl } from "react-intl";
import SearchField from "./SearchField";

export default function SearchBar({
  initialValue = "",
  onSearchChange = () => {},
  onSearchSubmit = () => {},
  onSearchClear = () => {},
  placeholder,
  disabled = false,
}) {
  const intl = useIntl();
  const [query, setQuery] = useState(initialValue);

  const resolvedPlaceholder = placeholder ?? intl.formatMessage({ id: "searchBar.placeholder" });

  const handlers = useMemo(
    () => ({
      set: (next) => {
        setQuery(next);
        onSearchChange(next);
      },
      submit: (val) => onSearchSubmit(val),
      clear: () => onSearchClear(),
    }),
    [onSearchChange, onSearchSubmit, onSearchClear]
  );

  return (
    <div className="mx-auto w-full max-w-[1120px]">
      <SearchField
        value={query}
        onChange={handlers.set}
        onSubmit={handlers.submit}
        onClear={handlers.clear}
        placeholder={resolvedPlaceholder}
        disabled={disabled}
      />
    </div>
  );
}