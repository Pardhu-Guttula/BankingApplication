import React from "react";
import { useIntl } from "react-intl";

export default function IconOrImage({ useImage, alt, src, icon: Icon, className }) {
  useIntl();

  if (useImage && src) {
    return <img alt={alt || ""} src={src} className={className} draggable={false} />;
  }
  if (Icon) return <Icon className={className} aria-hidden="true" />;
  return null;
}