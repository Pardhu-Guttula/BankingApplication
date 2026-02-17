import React from "react";
import { useIntl } from "react-intl";

export default function IconTile({ variant = "green", icon: IconComp }) {
  useIntl();

  const variantClasses = {
    green: "bg-[#F0FDF4] text-[#16A34A]",
    blue: "bg-[#EFF6FF] text-[#2563EB]",
    purple: "bg-[#FAF5FF] text-[#7C3AED]",
  };

  return (
    <div
      className={`flex h-[40px] w-[40px] items-center justify-center rounded-[10px] ${
        variantClasses[variant] || variantClasses.green
      }`}
    >
      {IconComp ? (
        <IconComp className="h-[18px] w-[18px]" aria-hidden="true" />
      ) : null}
    </div>
  );
}