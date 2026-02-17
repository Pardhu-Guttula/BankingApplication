import React from "react";
import { useIntl } from "react-intl";
import { Star } from "lucide-react";

export default function RatingStars({ value = 0, size = 13 }) {
  const intl = useIntl();

  const full = Math.floor(value);
  const hasHalf = value - full >= 0.5;

  return (
    <div
      style={{ display: "flex", gap: 2, alignItems: "center" }}
      aria-label={intl.formatMessage(
        { id: "ratingStars.ariaLabel" },
        { value }
      )}
    >
      {Array.from({ length: 5 }).map((_, i) => {
        const idx = i + 1;
        const filled = idx <= full;
        const half = !filled && hasHalf && idx === full + 1;

        return (
          <span
            key={i}
            style={{
              position: "relative",
              width: size,
              height: size,
              display: "inline-flex",
              alignItems: "center",
              justifyContent: "center",
            }}
          >
            <Star
              size={size}
              style={{
                color: "#CBD5E1",
                fill: "transparent",
              }}
            />
            {(filled || half) && (
              <span
                style={{
                  position: "absolute",
                  inset: 0,
                  overflow: "hidden",
                  width: half ? "50%" : "100%",
                }}
              >
                <Star
                  size={size}
                  style={{
                    color: "#F59E0B",
                    fill: "#F59E0B",
                  }}
                />
              </span>
            )}
          </span>
        );
      })}
    </div>
  );
}