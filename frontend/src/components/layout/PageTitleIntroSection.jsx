import React from "react";
import { useIntl } from "react-intl";

export default function PageTitleIntroSection({ title, description, onTitleClick = () => {}, onDescriptionClick = () => {} }) {
  const intl = useIntl();

  const resolvedTitle = title ?? intl.formatMessage({ id: "pageIntro.title" });
  const resolvedDescription = description ?? intl.formatMessage({ id: "pageIntro.description" });

  return (
    <section aria-label="Page title and introduction" className="w-full border-b border-black/10 bg-white">
      <div className="mx-auto flex w-full max-w-[1280px] flex-col items-center px-6 py-10 sm:px-10">
        <div className="flex w-full max-w-[955px] flex-col items-center gap-[15px] text-center">
          <h1 className="font-['Outfit',sans-serif] text-[40px] font-semibold leading-none text-black" onClick={onTitleClick}>
            {resolvedTitle}
          </h1>

          <p
            className="font-['Outfit',sans-serif] text-[16px] font-normal leading-5 tracking-[0.15px] text-[#64748b]"
            onClick={onDescriptionClick}
          >
            {resolvedDescription}
          </p>
        </div>
      </div>
    </section>
  );
}