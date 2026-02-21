import React from "react";
import { useIntl } from "react-intl";

export default function IconTile({ variant = "green", icon: IconComp }) {
  const intl = useIntl();

  const stylesByVariant = {
    green: "bg-[#F0FDF4] text-[#16A34A]",
    blue: "bg-[#EFF6FF] text-[#2563EB]",
    purple: "bg-[#FAF5FF] text-[#7C3AED]",
  };

  if (!IconComp) {
    return (
      <div
        className={`flex h-[44px] w-[44px] items-center justify-center rounded-[10px] ${
          stylesByVariant[variant] || stylesByVariant.green
        }`}
        aria-label={intl.formatMessage({ id: "common.icon" })}
      />
    );
  }

  return (
    <div
      className={`flex h-[44px] w-[44px] items-center justify-center rounded-[10px] ${
        stylesByVariant[variant] || stylesByVariant.green
      }`}
    >
      <IconComp className="h-[20px] w-[20px]" aria-hidden="true" />
    </div>
  );
}