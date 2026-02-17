import React, { useMemo, useState } from "react";
import { useIntl } from "react-intl";
import {
  ClipboardCheck,
  CreditCard,
  FilePlus2,
  History,
  Landmark,
  LayoutDashboard,
  Package,
  PiggyBank,
  Settings,
  Smartphone,
  Wallet,
  FilePlus,
  ClipboardList,
} from "lucide-react";

import GlobalHeader from "./layout/GlobalHeader";
import LeftSidebarNav from "./layout/LeftSidebarNav";
import MainPageHeaderGreeting from "./layout/MainPageHeaderGreeting";
import QuickActionsRow from "./layout/QuickActionsRow";
import AccountsSummarySection from "./layout/AccountsSummarySection";
import ProductsForYouSection from "./layout/ProductsForYouSection";
import RecentRequestsSection from "./layout/RecentRequestsSection";
import ProfileCompletionCTA from "./layout/ProfileCompletionCTA";

const imgIcon11 =
  "https://www.figma.com/api/mcp/asset/26798d2f-cdd8-4d16-8e72-2db5271e77c6";

const imgIcon =
  "https://www.figma.com/api/mcp/asset/584da7f5-626e-473f-a127-ccf526cf084a";
const imgIcon1 =
  "https://www.figma.com/api/mcp/asset/36a8cda0-ecf6-4afd-9533-5ebf9b0c85bf";
const imgIcon2 =
  "https://www.figma.com/api/mcp/asset/e9bda054-4616-4400-a14d-3514b61ba9bb";
const imgIcon3 =
  "https://www.figma.com/api/mcp/asset/defe0f3c-e124-4a50-8292-29e95cf76666";

export default function BankingDashboardPage() {
  const intl = useIntl();

  const sidebarItems = useMemo(
    () => [
      {
        itemKey: "dashboard",
        label: intl.formatMessage({ id: "leftSidebarNav.dashboard" }),
        Icon: LayoutDashboard,
      },
      {
        itemKey: "products",
        label: intl.formatMessage({ id: "leftSidebarNav.products" }),
        Icon: Package,
      },
      {
        itemKey: "open-account",
        label: intl.formatMessage({ id: "leftSidebarNav.openAccount" }),
        Icon: FilePlus,
      },
      {
        itemKey: "modify-services",
        label: intl.formatMessage({ id: "leftSidebarNav.modifyServices" }),
        Icon: Settings,
      },
      {
        itemKey: "request-status",
        label: intl.formatMessage({ id: "leftSidebarNav.requestStatus" }),
        Icon: ClipboardList,
        badgeCount: 3,
      },
      {
        itemKey: "activity-history",
        label: intl.formatMessage({ id: "leftSidebarNav.activityHistory" }),
        Icon: History,
      },
    ],
    [intl]
  );

  const greetingActions = useMemo(
    () => [
      {
        key: "open",
        iconSrc: imgIcon,
        label: intl.formatMessage({ id: "mainPageHeaderGreeting.openNewAccount" }),
      },
      {
        key: "modify",
        iconSrc: imgIcon1,
        label: intl.formatMessage({ id: "mainPageHeaderGreeting.modifyServices" }),
      },
      {
        key: "track",
        iconSrc: imgIcon2,
        label: intl.formatMessage({ id: "mainPageHeaderGreeting.trackRequests" }),
      },
      {
        key: "digital",
        iconSrc: imgIcon3,
        label: intl.formatMessage({ id: "mainPageHeaderGreeting.digitalBanking" }),
      },
    ],
    [intl]
  );

  const quickActions = useMemo(
    () => [
      {
        id: "open-account",
        label: intl.formatMessage({ id: "quickActionsRow.openNewAccount" }),
        Icon: FilePlus2,
      },
      {
        id: "modify-services",
        label: intl.formatMessage({ id: "quickActionsRow.modifyServices" }),
        Icon: Settings,
      },
      {
        id: "track-requests",
        label: intl.formatMessage({ id: "quickActionsRow.trackRequests" }),
        Icon: ClipboardCheck,
      },
      {
        id: "digital-banking",
        label: intl.formatMessage({ id: "quickActionsRow.digitalBanking" }),
        Icon: Smartphone,
      },
    ],
    [intl]
  );

  const accounts = useMemo(
    () => [
      {
        id: "checking",
        icon: Wallet,
        name: intl.formatMessage({ id: "accountsSummarySection.checkingAccount" }),
        balance: "$12,450.32",
        maskedNumber: "****4521",
        tone: "default",
      },
      {
        id: "savings",
        icon: PiggyBank,
        name: intl.formatMessage({ id: "accountsSummarySection.savingsAccount" }),
        balance: "$45,890.00",
        maskedNumber: "****8934",
        tone: "default",
      },
      {
        id: "credit",
        icon: CreditCard,
        name: intl.formatMessage({ id: "accountsSummarySection.creditCard" }),
        balance: "-$1,234.56",
        maskedNumber: "****2187",
        tone: "negative",
      },
    ],
    [intl]
  );

  const products = useMemo(
    () => [
      {
        id: "premium-savings",
        icon: PiggyBank,
        iconBgClassName: "bg-[#F0FDF4]",
        iconClassName: "text-[#16A34A]",
        badge: intl.formatMessage({ id: "productsForYouSection.recommended" }),
        title: intl.formatMessage({ id: "productsForYouSection.premiumSavingsTitle" }),
        description: intl.formatMessage({
          id: "productsForYouSection.premiumSavingsDescription",
        }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
      },
      {
        id: "personal-loan",
        icon: Landmark,
        iconBgClassName: "bg-[#EFF6FF]",
        iconClassName: "text-[#155DFC]",
        badge: intl.formatMessage({ id: "productsForYouSection.preApproved" }),
        title: intl.formatMessage({ id: "productsForYouSection.personalLoanTitle" }),
        description: intl.formatMessage({
          id: "productsForYouSection.personalLoanDescription",
        }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
      },
      {
        id: "gold-credit-card",
        icon: CreditCard,
        iconBgClassName: "bg-[#FAF5FF]",
        iconClassName: "text-[#9333EA]",
        badge: intl.formatMessage({ id: "productsForYouSection.limitedOffer" }),
        title: intl.formatMessage({ id: "productsForYouSection.goldCreditCardTitle" }),
        description: intl.formatMessage({
          id: "productsForYouSection.goldCreditCardDescription",
        }),
        ctaLabel: intl.formatMessage({ id: "common.applyNow" }),
      },
    ],
    [intl]
  );

  const defaultRequests = useMemo(
    () => [
      {
        id: "savings-opening",
        title: intl.formatMessage({ id: "recentRequestsSection.savingsOpeningTitle" }),
        timeAgo: intl.formatMessage({ id: "recentRequestsSection.savingsOpeningTimeAgo" }),
        statusLabel: intl.formatMessage({ id: "recentRequestsSection.completed" }),
        statusVariant: "completed",
      },
      {
        id: "credit-limit",
        title: intl.formatMessage({ id: "recentRequestsSection.creditLimitTitle" }),
        timeAgo: intl.formatMessage({ id: "recentRequestsSection.creditLimitTimeAgo" }),
        statusLabel: intl.formatMessage({ id: "recentRequestsSection.pending" }),
        statusVariant: "pending",
      },
      {
        id: "personal-loan",
        title: intl.formatMessage({ id: "recentRequestsSection.personalLoanTitle" }),
        timeAgo: intl.formatMessage({ id: "recentRequestsSection.personalLoanTimeAgo" }),
        statusLabel: intl.formatMessage({ id: "recentRequestsSection.inReview" }),
        statusVariant: "review",
      },
    ],
    [intl]
  );

  const [selectedAccountId, setSelectedAccountId] = useState("checking");
  const [selectedProductId, setSelectedProductId] = useState(products[0]?.id);
  const [activeRequestId, setActiveRequestId] = useState(null);

  return (
    <div className="min-h-screen w-full bg-[#F7F8FA]">
      <GlobalHeader
        brandName={intl.formatMessage({ id: "globalHeader.brandName" })}
        userName={intl.formatMessage({ id: "globalHeader.userName" })}
        userInitials={intl.formatMessage({ id: "globalHeader.userInitials" })}
        hasNotification={true}
        brandIconSrc={imgIcon11}
      />

      <div className="w-full grid grid-cols-1 md:grid-cols-[256px_1fr]">
        <LeftSidebarNav
          initialActiveKey="dashboard"
          items={sidebarItems}
          onContactSupport={() => {}}
        />

        <main className="w-full">
          <div className="mx-auto w-full max-w-[1240px] px-6 py-6">
            <div className="flex flex-col gap-6">
              <MainPageHeaderGreeting
                userFirstName={intl.formatMessage({ id: "mainPageHeaderGreeting.userFirstName" })}
                titleTemplate={intl.formatMessage({
                  id: "mainPageHeaderGreeting.welcomeBackTemplate",
                })}
                subtitle={intl.formatMessage({ id: "mainPageHeaderGreeting.subtitle" })}
                actions={greetingActions}
              />

              <QuickActionsRow actions={quickActions} onActionClick={() => {}} />

              <AccountsSummarySection
                title={intl.formatMessage({ id: "accountsSummarySection.title" })}
                accounts={accounts}
                selectedAccountId={selectedAccountId}
                onAccountClick={(id) => setSelectedAccountId(id)}
              />

              <ProductsForYouSection
                title={intl.formatMessage({ id: "productsForYouSection.title" })}
                viewAllLabel={intl.formatMessage({ id: "common.viewAll" })}
                viewAllAriaLabel={intl.formatMessage({ id: "productsForYouSection.viewAllAria" })}
                products={products}
                selectedProductId={selectedProductId}
                onSelectProduct={(id) => setSelectedProductId(id)}
                onApplyProduct={() => {}}
              />

              <RecentRequestsSection
                title={intl.formatMessage({ id: "recentRequestsSection.title" })}
                viewAllLabel={intl.formatMessage({ id: "common.viewAll" })}
                viewAllAriaLabel={intl.formatMessage({ id: "recentRequestsSection.viewAllAria" })}
                requests={defaultRequests}
                activeId={activeRequestId}
                onRequestClick={(id) => setActiveRequestId(id)}
                selectedLiveTemplate={intl.formatMessage({
                  id: "recentRequestsSection.selectedLiveTemplate",
                })}
              />

              <ProfileCompletionCTA
                percent={75}
                title={intl.formatMessage({ id: "profileCompletionCTA.title" })}
                subtitle={intl.formatMessage({ id: "profileCompletionCTA.subtitle" })}
                buttonLabel={intl.formatMessage({ id: "profileCompletionCTA.buttonLabel" })}
                continueLabel={intl.formatMessage({ id: "profileCompletionCTA.continue" })}
                ariaLabel={intl.formatMessage({ id: "profileCompletionCTA.ariaLabel" })}
                progressAriaLabel={intl.formatMessage({
                  id: "profileCompletionCTA.progressAriaLabel",
                })}
                srPercentTemplate={intl.formatMessage({
                  id: "profileCompletionCTA.srPercentTemplate",
                })}
                continueAriaLabel={intl.formatMessage({
                  id: "profileCompletionCTA.continueAriaLabel",
                })}
                onCompleteProfile={() => {}}
                onPercentChange={() => {}}
              />
            </div>
          </div>
        </main>
      </div>
    </div>
  );
}