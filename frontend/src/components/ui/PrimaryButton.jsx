import React from "react";
import { useIntl } from "react-intl";

export default function PrimaryButton({
  label,
  onClick = () => {},
  fullWidth = true,
}) {
  const intl = useIntl();

  const resolvedLabel = label ?? intl.formatMessage({ id: "common.submit" });

  return (
    <button
      type="button"
      onClick={onClick}
      className={[
        "inline-flex h-[36px] items-center justify-center rounded-[8px] bg-[#030213] px-4 text-[14px] font-medium leading-[20px] tracking-[-0.1504px] text-white",
        "transition-colors hover:bg-[#0B0D1A] focus:outline-none focus-visible:ring-2 focus-visible:ring-[#030213]/30 focus-visible:ring-offset-2",
        fullWidth ? "w-full" : "",
      ].join(" ")}
    >
      {resolvedLabel}
    </button>
  );
}