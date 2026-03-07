import React from 'react';
import { Building2 } from 'lucide-react';

export function BrandHeader({ title, subtitle }) {
  return (
    <header className="flex flex-col gap-[8px] items-center justify-center text-center">
      <div
        className="w-16 h-16 rounded-[16px] bg-[#155dfc] flex items-center justify-center"
        aria-hidden="true"
      >
        <Building2 className="w-8 h-8 text-white" />
      </div>

      <h1 className="text-[#101828] text-[30px] leading-[36px] font-bold tracking-[0.3955px]">
        {title}
      </h1>
      <p className="text-[#4a5565] text-[16px] leading-[24px] tracking-[-0.3125px]">
        {subtitle}
      </p>
    </header>
  );
}
