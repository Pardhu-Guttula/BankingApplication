import React, { useMemo, useState } from "react";
import { useIntl } from "react-intl";
import PageButton from "../ui/PageButton";
import NavButton from "../ui/NavButton";

export default function Pagination({
  page: pageProp,
  totalPages = 2,
  siblingCount = 0,
  onPageChange = () => {},
  onPrev = () => {},
  onNext = () => {},
}) {
  const intl = useIntl();

  const isControlled = typeof pageProp === "number";
  const [pageUncontrolled, setPageUncontrolled] = useState(1);
  const page = isControlled ? pageProp : pageUncontrolled;

  const clampedPage = Math.min(Math.max(1, page), Math.max(1, totalPages));

  const pages = useMemo(() => {
    const total = Math.max(1, totalPages);
    const current = Math.min(Math.max(1, clampedPage), total);

    const windowSize = Math.max(2, 1 + siblingCount * 2);
    const start = Math.max(
      1,
      Math.min(current - siblingCount, total - windowSize + 1)
    );
    const end = Math.min(total, start + windowSize - 1);

    const arr = [];
    for (let p = start; p <= end; p += 1) arr.push(p);
    return arr;
  }, [clampedPage, totalPages, siblingCount]);

  const setPage = (nextPage) => {
    const total = Math.max(1, totalPages);
    const next = Math.min(Math.max(1, nextPage), total);

    if (!isControlled) setPageUncontrolled(next);
    onPageChange(next);
  };

  const canPrev = clampedPage > 1;
  const canNext = clampedPage < Math.max(1, totalPages);

  return (
    <nav
      aria-label="Pagination"
      className="flex w-full items-center justify-center gap-[8px] pt-[20px]"
    >
      <NavButton
        direction="prev"
        disabled={!canPrev}
        onClick={() => {
          if (!canPrev) return;
          onPrev(clampedPage - 1);
          setPage(clampedPage - 1);
        }}
      >
        {intl.formatMessage({ id: "common.prev" })}
      </NavButton>

      <div className="flex items-stretch gap-[4px]" aria-label="Page numbers">
        {pages.map((p) => (
          <PageButton
            key={p}
            page={p}
            isActive={p === clampedPage}
            onSelect={(selected) => setPage(selected)}
          />
        ))}
      </div>

      <NavButton
        direction="next"
        disabled={!canNext}
        onClick={() => {
          if (!canNext) return;
          onNext(clampedPage + 1);
          setPage(clampedPage + 1);
        }}
      >
        {intl.formatMessage({ id: "common.next" })}
      </NavButton>
    </nav>
  );
}