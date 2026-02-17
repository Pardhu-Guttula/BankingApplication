import React from "react";
import { useIntl } from "react-intl";
import { Bell } from "lucide-react";
import BrandMark from "../ui/BrandMark";
import IconButton from "../ui/IconButton";
import UserButton from "../ui/UserButton";

export default function GlobalHeader({
  brandName = "SecureBank",
  userName = "John Doe",
  userInitials = "JD",
  hasNotification = true,
  onBrandClick = () => {},
  onNotificationsClick = () => {},
  onUserClick = () => {},
  brandIconSrc,
}) {
  const intl = useIntl();

  return (
    <header className="w-full border-b border-[#E5E7EB] bg-white">
      <div className="mx-auto flex h-16 w-full items-center justify-between px-6">
        <div className="flex items-center">
          <BrandMark
            onClick={onBrandClick}
            brandName={brandName}
            iconSrc={brandIconSrc}
            ariaLabel={intl.formatMessage({ id: "globalHeader.brandAria" })}
          />
          <span className="sr-only">{brandName}</span>
        </div>

        <div className="flex items-center gap-2">
          <IconButton
            label={intl.formatMessage({ id: "globalHeader.notifications" })}
            onClick={onNotificationsClick}
            hasDot={hasNotification}
          >
            <Bell className="h-4 w-4" aria-hidden="true" />
          </IconButton>

          <UserButton
            userName={userName}
            userInitials={userInitials}
            onClick={onUserClick}
            ariaLabel={intl.formatMessage({ id: "globalHeader.userMenu" })}
          />
        </div>
      </div>
    </header>
  );
}