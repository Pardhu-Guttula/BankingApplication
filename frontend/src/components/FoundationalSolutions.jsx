import React, { useMemo, useState } from "react";
import { useIntl } from "react-intl";
import GlobalHeader from "./layout/GlobalHeader";
import Breadcrumbs from "./layout/Breadcrumbs";
import PageTitleIntroSection from "./layout/PageTitleIntroSection";
import AssistanceWidget from "./layout/AssistanceWidget";
import TrendingCategoriesBar from "./ui/TrendingCategoriesBar";
import SearchBar from "./ui/SearchBar";
import CategoryToggleButtons from "./ui/CategoryToggleButtons";
import SolutionsCardGrid from "./ui/SolutionsCardGrid";

const imgBrillioLogoRgb1 = "https://www.figma.com/api/mcp/asset/e27ea95d-da1e-44cf-a9f3-21dca6c13ce2";
const imgAdamLogo = "https://www.figma.com/api/mcp/asset/f8a12db6-b2a0-4144-8d19-4afae4b91770";
const imgAvatarPlaceholder = "https://www.figma.com/api/mcp/asset/da74622d-54cb-488c-9a7d-495525c0dd7e";
const imgChatbotIcon1 = "https://www.figma.com/api/mcp/asset/8c54fa67-398b-451c-9004-9d134fed57ef";
const imgIcon = "https://www.figma.com/api/mcp/asset/4cb05dfa-ac8f-4817-9adf-2871e6b600a5";

export default function FoundationalSolutions() {
  const intl = useIntl();

  const [activeNavId] = useState("foundational");

  const breadcrumbItems = useMemo(
    () => [
      { label: intl.formatMessage({ id: "breadcrumbs.home" }), href: "/" },
      { label: intl.formatMessage({ id: "breadcrumbs.foundationalSolutions" }), href: "/foundational-solutions" },
    ],
    [intl]
  );

  const pageTitle = intl.formatMessage({ id: "pageIntro.title" });
  const pageDescription = intl.formatMessage({ id: "pageIntro.description" });

  const solutionItems = useMemo(
    () => [
      {
        id: "sdlc-end-to-end-demo",
        title: intl.formatMessage({ id: "solutions.sdlcEndToEndDemo.title" }),
        description: intl.formatMessage({ id: "solutions.sdlcEndToEndDemo.description" }),
        tags: [intl.formatMessage({ id: "solutions.tags.sdlcAutomation" })],
        iconSrc: imgIcon,
      },
      {
        id: "app-modernization",
        title: intl.formatMessage({ id: "solutions.appModernization.title" }),
        description: intl.formatMessage({ id: "solutions.appModernization.description" }),
        tags: [
          intl.formatMessage({ id: "solutions.tags.appModernization" }),
          intl.formatMessage({ id: "solutions.tags.cloudMigration" }),
          intl.formatMessage({ id: "solutions.tags.modernization" }),
        ],
        iconSrc: imgIcon,
      },
      {
        id: "architecture-generation",
        title: intl.formatMessage({ id: "solutions.architectureGeneration.title" }),
        description: intl.formatMessage({ id: "solutions.architectureGeneration.description" }),
        tags: [intl.formatMessage({ id: "solutions.tags.cloudArchitecture" })],
        iconSrc: imgIcon,
      },
      {
        id: "architecture-validation",
        title: intl.formatMessage({ id: "solutions.architectureValidation.title" }),
        description: intl.formatMessage({ id: "solutions.architectureValidation.description" }),
        tags: [
          intl.formatMessage({ id: "solutions.tags.cloudGovernance" }),
          intl.formatMessage({ id: "solutions.tags.architectureCompliance" }),
        ],
        iconSrc: imgIcon,
      },
      {
        id: "ai-testing-assist",
        title: intl.formatMessage({ id: "solutions.aiTestingAssist.title" }),
        description: intl.formatMessage({ id: "solutions.aiTestingAssist.description" }),
        tags: [intl.formatMessage({ id: "solutions.tags.qaAutomation" }), intl.formatMessage({ id: "solutions.tags.testing" })],
        iconSrc: imgIcon,
      },
      {
        id: "code-conversion-tool",
        title: intl.formatMessage({ id: "solutions.codeConversionTool.title" }),
        description: intl.formatMessage({ id: "solutions.codeConversionTool.description" }),
        tags: [intl.formatMessage({ id: "solutions.tags.sdlcAutomation" }), intl.formatMessage({ id: "solutions.tags.codeModernisation" })],
        iconSrc: imgIcon,
      },
      {
        id: "cicd-orchestration-tool",
        title: intl.formatMessage({ id: "solutions.cicdOrchestrationTool.title" }),
        description: intl.formatMessage({ id: "solutions.cicdOrchestrationTool.description" }),
        tags: [intl.formatMessage({ id: "solutions.tags.devOpsAutomation" }), intl.formatMessage({ id: "solutions.tags.cicd" })],
        iconSrc: imgIcon,
      },
      {
        id: "agentic-e2e-testing",
        title: intl.formatMessage({ id: "solutions.agenticE2ETesting.title" }),
        description: intl.formatMessage({ id: "solutions.agenticE2ETesting.description" }),
        tags: [intl.formatMessage({ id: "solutions.tags.softwareTesting" })],
        iconSrc: imgIcon,
      },
    ],
    [intl]
  );

  const trendingChips = useMemo(
    () => [
      { label: intl.formatMessage({ id: "trendingCategories.mobile" }), count: 6 },
      { label: intl.formatMessage({ id: "trendingCategories.security" }), count: 8 },
      { label: intl.formatMessage({ id: "trendingCategories.webDevelopment" }), count: 15 },
      { label: intl.formatMessage({ id: "trendingCategories.devOps" }), count: 12 },
      { label: intl.formatMessage({ id: "trendingCategories.aiml" }), count: 10 },
      { label: intl.formatMessage({ id: "trendingCategories.cloud" }), count: 14 },
    ],
    [intl]
  );

  const categoryTabs = useMemo(
    () => [
      { id: "engineering", label: intl.formatMessage({ id: "categoryTabs.engineering" }), count: 8, iconId: "wrench" },
      { id: "operations", label: intl.formatMessage({ id: "categoryTabs.operations" }), count: 6, iconId: "settings" },
      { id: "decisioning", label: intl.formatMessage({ id: "categoryTabs.decisioning" }), count: 6, iconId: "barchart" },
    ],
    [intl]
  );

  return (
    <div className="min-h-screen w-full bg-[#F6F6F8] text-[#111111]">
      <GlobalHeader
        activeNavId={activeNavId}
        userName="John Doe"
        assets={{
          imgBrillioLogoRgb1,
          imgAdamLogo,
          imgAvatarPlaceholder,
        }}
      />

      <Breadcrumbs items={breadcrumbItems} />

      <PageTitleIntroSection title={pageTitle} description={pageDescription} />

      <main className="w-full">
        <section className="mx-auto w-full max-w-[1120px] px-6 py-8">
          <TrendingCategoriesBar chips={trendingChips} />
        </section>

        <section className="mx-auto w-full max-w-[1120px] px-6">
          <SearchBar />
        </section>

        <section className="mx-auto w-full max-w-[1120px] px-6 pt-4">
          <CategoryToggleButtons tabs={categoryTabs} />
        </section>

        <section className="pt-4">
          <SolutionsCardGrid items={solutionItems} />
        </section>
      </main>

      <AssistanceWidget assets={{ imgChatbotIcon1 }} />
    </div>
  );
}