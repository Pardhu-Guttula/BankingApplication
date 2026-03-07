import React from 'react';
import { User } from 'lucide-react';
import { useIntl } from 'react-intl';

export function AuthCard({ title, description, children }) {
  const intl = useIntl();

  return (
    <section
      aria-label="Authentication"
      className="w-full rounded-[14px] bg-white border border-[#e5e7eb] shadow-[0px_20px_25px_0px_rgba(0,0,0,0.1),0px_8px_10px_0px_rgba(0,0,0,0.1)]"
    >
      <div className="px-6 pt-6 pb-4">
        <div className="flex items-center gap-[6px]">
          <User className="w-5 h-5 text-[#0a0a0a]" aria-hidden="true" />
          <h2 className="text-[#0a0a0a] text-[16px] leading-[16px] font-medium tracking-[-0.3125px]">
            {title}
          </h2>
        </div>
        <p className="mt-3 text-[#717182] text-[16px] leading-[24px] tracking-[-0.3125px]">
          {description}
        </p>
      </div>

      <div className="px-6 pb-6">{children}</div>
    </section>
  );
}