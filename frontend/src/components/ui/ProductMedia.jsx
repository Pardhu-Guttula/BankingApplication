import React from "react";
import { useIntl } from "react-intl";

export default function ProductMedia({ imageSrc, alt = "" }) {
  useIntl();

  return (
    <div className="flex h-[300px] w-full items-center justify-center overflow-hidden bg-[#F8FAFC] p-4">
      <img
        src={imageSrc}
        alt={alt}
        className="block h-[200px] w-[140px] max-h-[240px] max-w-[280px] object-contain"
      />
    </div>
  );
}