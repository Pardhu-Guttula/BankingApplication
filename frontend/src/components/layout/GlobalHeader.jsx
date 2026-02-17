import React, { useMemo, useState } from "react";
import { useIntl } from "react-intl";
import BrandBlock from "../ui/BrandBlock";
import NavLink from "../ui/NavLink";
import NavDropdownButton from "../ui/NavDropdownButton";
import UserMenu from "../ui/UserMenu";

export default function GlobalHeader({
  activeNavId = "foundational",
  userName = "John Doe",
  onNavigate = () => {},
  onBrillioClick = () => {},
  onAdamClick = () => {},
  onUserAction = () => {},
  assets,
}) {
  const intl = useIntl();
  const [openMenuId, setOpenMenuId] = useState(null);
  const [userOpen, setUserOpen] = useState(false);

  const links = useMemo(
    () => [
      { id: "strategy", label: intl.formatMessage({ id: "globalHeader.strategyToolkit" }), type: "link" },
      { id: "agent", label: intl.formatMessage({ id: "globalHeader.agentBuilder" }), type: "link" },
      { id: "marketplace", label: intl.formatMessage({ id: "globalHeader.marketplace" }), type: "link" },
      { id: "foundational", label: intl.formatMessage({ id: "globalHeader.foundationalSolutions" }), type: "dropdown" },
      { id: "business", label: intl.formatMessage({ id: "globalHeader.businessSolutions" }), type: "dropdown" },
      { id: "control", label: intl.formatMessage({ id: "globalHeader.controlTower" }), type: "link" },
    ],
    [intl]
  );

  function toggleMenu(id) {
    setUserOpen(false);
    setOpenMenuId((prev) => (prev === id ? null : id));
  }

  function handleNavigate(id) {
    setOpenMenuId(null);
    setUserOpen(false);
    onNavigate(id);
  }

  return (
    <header className="w-full border-b border-black/10 bg-white">
      <div className="mx-auto flex h-[80px] w-full max-w-[1280px] items-center px-10">
        <div className="flex w-full items-center justify-between gap-6">
          <BrandBlock
            onBrillioClick={onBrillioClick}
            onAdamClick={onAdamClick}
            imgBrillioLogoRgb1={assets?.imgBrillioLogoRgb1}
            imgAdamLogo={assets?.imgAdamLogo}
          />

          <nav className="hidden items-center gap-2 md:flex" aria-label="Primary">
            {links.map((item) => {
              if (item.type === "dropdown") {
                const isActive = activeNavId === item.id;
                const isOpen = openMenuId === item.id;

                return (
                  <NavDropdownButton
                    key={item.id}
                    id={item.id}
                    label={item.label}
                    active={isActive}
                    open={isOpen}
                    onToggle={toggleMenu}
                    onNavigate={handleNavigate}
                  />
                );
              }

              return <NavLink key={item.id} id={item.id} label={item.label} active={activeNavId === item.id} onNavigate={handleNavigate} />;
            })}
          </nav>

          <div className="flex items-center gap-3">
            <UserMenu
              userName={userName}
              avatarSrc={assets?.imgAvatarPlaceholder}
              open={userOpen}
              onToggle={() => {
                setOpenMenuId(null);
                setUserOpen((v) => !v);
              }}
              onAction={(actionId) => {
                setUserOpen(false);
                onUserAction(actionId);
              }}
            />
          </div>
        </div>
      </div>
    </header>
  );
}