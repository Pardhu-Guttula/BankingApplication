import React from "react";
import { useIntl } from "react-intl";

export default function FilterGroup({ title, children, className = "" }) {
  const intl = useIntl();
  void intl;

  return (
    <section
      className={["w-full border-b border-[#E2E8F0] pb-[17px]", className].join(
        " "
      )}
    >
      <div className="py-[8px]">
        <h4 className="text-[15px] font-semibold leading-[24px] text-[#1E293B]">
          {title}
        </h4>
      </div>
      {children}
    </section>
  );
}