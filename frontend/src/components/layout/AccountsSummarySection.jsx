import React from "react";
import { useIntl } from "react-intl";
import AccountCard from "../ui/AccountCard";

export default function AccountsSummarySection({
  title,
  accounts = [],
  selectedAccountId,
  onAccountClick = () => {},
}) {
  const intl = useIntl();
  const computedTitle = title || intl.formatMessage({ id: "accountsSummarySection.title" });

  return (
    <section aria-label={computedTitle} className="w-full">
      <h2 className="text-[20px] font-bold leading-[28px] tracking-[-0.4492px] text-[#0a0a0a]">
        {computedTitle}
      </h2>

      <div className="mt-[16px] grid grid-cols-1 gap-[16px] md:grid-cols-3">
        {accounts.map((account) => (
          <AccountCard
            key={account.id}
            {...account}
            selected={selectedAccountId === account.id}
            onClick={() => onAccountClick(account.id)}
            onKeyDown={(e) => {
              if (e.key === "Enter" || e.key === " ") {
                e.preventDefault();
                onAccountClick(account.id);
              }
            }}
          />
        ))}
      </div>
    </section>
  );
}