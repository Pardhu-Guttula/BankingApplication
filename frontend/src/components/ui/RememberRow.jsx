import React from 'react';
import { useIntl } from 'react-intl';

export function RememberRow({
  checked,
  onCheckedChange,
  onForgotPassword,
}) {
  const intl = useIntl();

  return (
    <div className="flex items-center justify-between gap-4">
      <label className="inline-flex items-center gap-2 cursor-pointer select-none">
        <input
          type="checkbox"
          checked={checked}
          onChange={(e) => onCheckedChange(e.target.checked)}
          className="h-[13px] w-[13px] rounded-[3px] border border-[#cbd5e1] bg-white accent-[#155dfc]"
        />
        <span className="text-[#4a5565] text-[16px] leading-[24px] font-medium tracking-[-0.3125px]">
          Remember me
        </span>
      </label>

      <button
        type="button"
        onClick={() => onForgotPassword()}
        className="text-[#155dfc] text-[14px] leading-[20px] tracking-[-0.1504px] hover:underline underline-offset-2"
      >
        Forgot password?
      </button>
    </div>
  );
}