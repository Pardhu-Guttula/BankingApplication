import React, { useMemo } from "react";
import { useIntl } from "react-intl";
import { Star } from "lucide-react";
import clamp from "../utils/clamp";

export default function StarRating({ value = 4, max = 5, reviewCount = 0 }) {
  const intl = useIntl();
  const safeValue = clamp(Number(value) || 0, 0, max);

  const stars = useMemo(() => {
    const full = Math.floor(safeValue);
    const frac = safeValue - full;
    const hasHalf = frac >= 0.25 && frac < 0.75;
    const filledCount = full + (frac >= 0.75 ? 1 : 0);

    return Array.from({ length: max }).map((_, i) => {
      const isFilled = i < filledCount;
      const isHalf = !isFilled && hasHalf && i === full;

      return (
        <span
          key={i}
          aria-hidden="true"
          className="relative inline-flex h-[14px] w-[14px] text-[#F59E0B]"
        >
          <Star size={14} strokeWidth={2} className="text-[#F59E0B]" />
          {(isFilled || isHalf) && (
            <span
              className="absolute inset-0 overflow-hidden"
              style={{ width: isHalf ? "50%" : "100%" }}
            >
              <Star size={14} strokeWidth={2} fill="currentColor" className="text-[#F59E0B]" />
            </span>
          )}
        </span>
      );
    });
  }, [safeValue, max]);

  return (
    <div className="flex items-center gap-2">
      <div
        aria-label={intl.formatMessage(
          { id: "starRating.ariaRating" },
          { safeValue, max }
        )}
        className="inline-flex items-center gap-[2px]"
      >
        {stars}
      </div>
      <span className="font-sans text-[13px] leading-[20.8px] text-[#64748B]">
        ({reviewCount})
      </span>
    </div>
  );
}