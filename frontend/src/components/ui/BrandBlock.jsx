import React from "react";
import { useIntl } from "react-intl";

export default function BrandBlock({ onBrillioClick = () => {}, onAdamClick = () => {}, imgBrillioLogoRgb1, imgAdamLogo }) {
  const intl = useIntl();

  return (
    <div className="flex items-center gap-[29px]">
      <button
        type="button"
        onClick={onBrillioClick}
        className="h-12 w-[87px] shrink-0 rounded-md focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#211747]/30"
        aria-label={intl.formatMessage({ id: "brandBlock.brillioHomeAria" })}
      >
        <img alt="Brillio" className="h-full w-full object-contain" src={imgBrillioLogoRgb1} draggable={false} />
      </button>

      <div className="h-[60px] w-px shrink-0 bg-black/10" aria-hidden="true" />

      <button
        type="button"
        onClick={onAdamClick}
        className="h-10 w-[117px] shrink-0 rounded-md focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#211747]/30"
        aria-label={intl.formatMessage({ id: "brandBlock.adamAria" })}
      >
        <img alt="ADAM" className="h-full w-full object-contain" src={imgAdamLogo} draggable={false} />
      </button>
    </div>
  );
}