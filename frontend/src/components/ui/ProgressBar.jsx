import React from "react";
import { clamp } from "../utils/number";

export default function ProgressBar({
  value = 75,
  onChange = () => {},
  "aria-label": ariaLabel = "Profile completion progress",
}) {
  const pct = clamp(Number(value) || 0, 0, 100);

  return (
    <div className="w-full">
      <div
        className="h-2 w-full rounded-full bg-[rgba(3,2,19,0.20)] overflow-hidden"
        role="progressbar"
        aria-label={ariaLabel}
        aria-valuemin={0}
        aria-valuemax={100}
        aria-valuenow={pct}
        onClick={() => onChange(pct)}
      >
        <div className="h-full rounded-full bg-[#030213]" style={{ width: `${pct}%` }} />
      </div>
    </div>
  );
}