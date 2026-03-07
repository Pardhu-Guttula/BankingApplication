import React from 'react';
import { useIntl } from 'react-intl';

export function SecurityNote({ text }) {
  const intl = useIntl();

  return (
    <footer className="text-center">
      <p className="text-[#4a5565] text-[14px] leading-[20px] tracking-[-0.1504px]">
        {text}
      </p>
    </footer>
  );
}