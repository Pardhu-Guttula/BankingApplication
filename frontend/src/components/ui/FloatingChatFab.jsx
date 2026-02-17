import React from "react";
import { useIntl } from "react-intl";
import { BotMessageSquare, X } from "lucide-react";
import IconOrImage from "./IconOrImage";

export default function FloatingChatFab({
  isOpen,
  onToggle = () => {},
  onOpen = () => {},
  onClose = () => {},
  onClick = () => {},
  label,
  useImageIcon = true,
  iconImageSrc,
}) {
  useIntl();

  const handleToggle = () => {
    const next = !isOpen;
    onToggle(next);
    if (next) onOpen();
    else onClose();
    onClick(next);
  };

  return (
    <button
      type="button"
      onClick={handleToggle}
      aria-label={label}
      aria-pressed={isOpen}
      className={[
        "fixed right-6 top-[62%] z-50",
        "h-12 w-12 rounded-[14px]",
        "bg-[#211747] text-white",
        "shadow-[0px_1px_5px_0px_rgba(0,0,0,0.12),0px_2px_2px_0px_rgba(0,0,0,0.14),0px_3px_1px_-2px_rgba(0,0,0,0.2)]",
        "grid place-items-center",
        "transition-transform duration-150 ease-out",
        "hover:scale-[1.03] active:scale-[0.98]",
        "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#211747] focus-visible:ring-offset-2 focus-visible:ring-offset-white",
      ].join(" ")}
    >
      <span className="sr-only">{label}</span>
      <IconOrImage
        useImage={useImageIcon}
        src={iconImageSrc}
        alt=""
        icon={isOpen ? X : BotMessageSquare}
        className={useImageIcon ? "h-7 w-7" : "h-6 w-6"}
      />
    </button>
  );
}