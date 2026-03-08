import React from 'react';
import { noop } from '../../utils/noop';

export function LabeledInput({
  id,
  label,
  type = "text",
  value,
  placeholder,
  onChange = noop,
  autoComplete,
  error,
}) {
  return (
    <div className="flex flex-col gap-2">
      <label
        htmlFor={id}
        className="text-[#0a0a0a] text-[14px] leading-[14px] font-medium tracking-[-0.1504px]"
      >
        {label}
      </label>

      <input
        id={id}
        type={type}
        value={value}
        placeholder={placeholder}
        autoComplete={autoComplete}
        onChange={(e) => onChange(e.target.value)}
        aria-invalid={Boolean(error)}
        aria-describedby={error ? `${id}-error` : undefined}
        className={[
          "h-11 w-full rounded-[8px] bg-[#f3f3f5] px-3 py-1 text-[14px] tracking-[-0.1504px] text-[#0a0a0a]",
          "placeholder:text-[#717182]",
          "outline-none ring-0",
          error
            ? "border border-red-500 focus:border-red-500 focus:ring-2 focus:ring-red-200"
            : "border border-transparent focus:border-[#155dfc] focus:ring-2 focus:ring-blue-100",
        ].join(" ")}
      />

      {error ? (
        <p
          id={`${id}-error`}
          className="text-[12px] leading-[16px] text-red-600"
        >
          {error}
        </p>
      ) : null}
    </div>
  );
}
