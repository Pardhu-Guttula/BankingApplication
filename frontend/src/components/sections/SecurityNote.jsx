import React from 'react';

export function SecurityNote({ text }) {
  return (
    <footer className="text-center">
      <p className="text-[#4a5565] text-[14px] leading-[20px] tracking-[-0.1504px]">
        {text}
      </p>
    </footer>
  );
}
