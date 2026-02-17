import React from "react";

export default function UserButton({
  userName = "John Doe",
  userInitials = "JD",
  onClick = () => {},
  ariaLabel,
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      className="inline-flex h-9 items-center gap-2 rounded-lg px-2 hover:bg-[#F3F4F6] focus:outline-none focus-visible:ring-2 focus-visible:ring-[#2563EB] focus-visible:ring-offset-2"
      aria-label={ariaLabel || "Open user menu"}
    >
      <span className="flex h-8 w-8 items-center justify-center rounded-full bg-[#155DFC] text-[14px] font-medium leading-5 tracking-[-0.1504px] text-white">
        {userInitials}
      </span>
      <span className="text-[14px] font-medium leading-5 tracking-[-0.1504px] text-[#0A0A0A]">
        {userName}
      </span>
    </button>
  );
}