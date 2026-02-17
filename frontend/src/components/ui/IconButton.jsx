import React from "react";

export default function IconButton({ label, onClick = () => {}, children, hasDot = false }) {
  return (
    <button
      type="button"
      onClick={onClick}
      aria-label={label}
      className="relative inline-flex h-9 w-9 items-center justify-center rounded-lg text-[#0A0A0A] hover:bg-[#F3F4F6] focus:outline-none focus-visible:ring-2 focus-visible:ring-[#2563EB] focus-visible:ring-offset-2"
    >
      {children}
      {hasDot ? (
        <span
          className="absolute right-[6px] top-[4px] h-2 w-2 rounded-full bg-[#FB2C36]"
          aria-hidden="true"
        />
      ) : null}
    </button>
  );
}