import React from "react";
import { useIntl } from "react-intl";
import GreetingQuickActionCard from "../ui/GreetingQuickActionCard";

export default function MainPageHeaderGreeting({
  userFirstName = "John",
  titleTemplate,
  subtitle,
  actions = [],
  onOpenNewAccount = () => {},
  onModifyServices = () => {},
  onTrackRequests = () => {},
  onDigitalBanking = () => {},
}) {
  const intl = useIntl();

  const computedTitle =
    titleTemplate ||
    intl.formatMessage({ id: "mainPageHeaderGreeting.welcomeBackTemplate" });

  const computedSubtitle =
    subtitle || intl.formatMessage({ id: "mainPageHeaderGreeting.subtitle" });

  const defaultActions = [
    {
      key: "open",
      label: intl.formatMessage({ id: "mainPageHeaderGreeting.openNewAccount" }),
      onClick: onOpenNewAccount,
    },
    {
      key: "modify",
      label: intl.formatMessage({ id: "mainPageHeaderGreeting.modifyServices" }),
      onClick: onModifyServices,
    },
    {
      key: "track",
      label: intl.formatMessage({ id: "mainPageHeaderGreeting.trackRequests" }),
      onClick: onTrackRequests,
    },
    {
      key: "digital",
      label: intl.formatMessage({ id: "mainPageHeaderGreeting.digitalBanking" }),
      onClick: onDigitalBanking,
    },
  ];

  const data = actions && actions.length ? actions : defaultActions;

  return (
    <section aria-label={intl.formatMessage({ id: "mainPageHeaderGreeting.ariaLabel" })} className="w-full">
      <div className="flex flex-col gap-[24px]">
        <header className="flex flex-col gap-[8px]">
          <h1 className="text-[30px] font-bold leading-[36px] tracking-[0.3955px] text-[#101828]">
            {computedTitle.replace("{userFirstName}", userFirstName)}
          </h1>
          <p className="text-[16px] font-normal leading-[24px] tracking-[-0.3125px] text-[#4A5565]">
            {computedSubtitle}
          </p>
        </header>

        <div className="grid grid-cols-1 gap-[16px] sm:grid-cols-2 lg:grid-cols-4">
          {data.map((a) => (
            <GreetingQuickActionCard
              key={a.key}
              iconSrc={a.iconSrc}
              label={a.label}
              onClick={a.onClick}
            />
          ))}
        </div>
      </div>
    </section>
  );
}