import React, { useState } from "react";
import { useIntl } from "react-intl";
import { Heart, ShoppingCart } from "lucide-react";
import RatingStars from "./RatingStars";

export default function ProductCard({
  imageUrl,
  category,
  title,
  rating,
  reviewCount,
  price,
  href = "#",
  onNavigate = () => {},
  onAddToCart = () => {},
  onToggleWishlist = () => {},
}) {
  const intl = useIntl();
  const [isHovered, setIsHovered] = useState(false);

  return (
    <article
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      style={{
        background: "#FFFFFF",
        borderRadius: 16,
        overflow: "hidden",
        boxShadow: "0px 1px 3px rgba(0,0,0,0.10), 0px 1px 2px rgba(0,0,0,0.06)",
        display: "flex",
        flexDirection: "column",
        minHeight: 520,
      }}
    >
      <div
        style={{
          background: "#F8FAFC",
          height: 280,
          padding: 24,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          position: "relative",
          overflow: "hidden",
        }}
      >
        <img
          src={imageUrl}
          alt={title}
          style={{
            maxHeight: 224,
            maxWidth: 264,
            width: "auto",
            height: "auto",
            objectFit: "contain",
            display: "block",
          }}
        />

        <div
          style={{
            position: "absolute",
            right: 6,
            top: 16,
            opacity: isHovered ? 1 : 0,
            transition: "opacity 150ms ease",
            pointerEvents: isHovered ? "auto" : "none",
          }}
        >
          <button
            type="button"
            onClick={onToggleWishlist}
            aria-label={intl.formatMessage({ id: "productCard.addToWishlist" })}
            style={{
              width: 40,
              height: 40,
              borderRadius: 9999,
              background: "#FFFFFF",
              border: "none",
              boxShadow:
                "0px 4px 6px -1px rgba(0,0,0,0.10), 0px 2px 4px -1px rgba(0,0,0,0.06)",
              display: "inline-flex",
              alignItems: "center",
              justifyContent: "center",
              cursor: "pointer",
            }}
          >
            <Heart size={16} color="#334155" />
          </button>
        </div>
      </div>

      <div
        style={{
          padding: "24px 20px 20px",
          display: "flex",
          flexDirection: "column",
          gap: 1.4,
          flex: 1,
        }}
      >
        <div
          style={{
            fontFamily:
              "Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif",
            fontSize: 12,
            fontWeight: 600,
            letterSpacing: 0.5,
            textTransform: "uppercase",
            color: "#4361EE",
            lineHeight: "19.2px",
            whiteSpace: "nowrap",
          }}
        >
          {category}
        </div>

        <a
          href={href}
          onClick={(e) => {
            e.preventDefault();
            onNavigate(href);
          }}
          style={{
            fontFamily:
              "Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif",
            fontSize: 15,
            fontWeight: 600,
            color: "#1E293B",
            textDecoration: "none",
            lineHeight: "21px",
            minHeight: 42,
            display: "-webkit-box",
            WebkitLineClamp: 2,
            WebkitBoxOrient: "vertical",
            overflow: "hidden",
          }}
        >
          {title}
        </a>

        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: 8,
            paddingTop: 8.6,
          }}
        >
          <RatingStars value={rating} size={13} />
          <div
            style={{
              fontFamily:
                "Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif",
              fontSize: 13,
              fontWeight: 400,
              color: "#64748B",
              lineHeight: "20.8px",
              whiteSpace: "nowrap",
            }}
          >
            ({reviewCount})
          </div>
        </div>

        <div style={{ paddingTop: 10.6, paddingBottom: 14.6 }}>
          <div
            style={{
              fontFamily:
                "Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif",
              fontSize: 20,
              fontWeight: 700,
              color: "#4361EE",
              lineHeight: "32px",
            }}
          >
            {price}
          </div>
        </div>

        <button
          type="button"
          onClick={onAddToCart}
          style={{
            marginTop: "auto",
            width: "100%",
            background: "#4361EE",
            color: "#FFFFFF",
            border: "none",
            borderRadius: 8,
            padding: 12,
            display: "inline-flex",
            alignItems: "center",
            justifyContent: "center",
            gap: 8,
            cursor: "pointer",
            fontFamily:
              "Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif",
            fontSize: 14,
            fontWeight: 600,
          }}
        >
          <ShoppingCart size={14} color="#FFFFFF" />
          {intl.formatMessage({ id: "productCard.addToCart" })}
        </button>
      </div>
    </article>
  );
}