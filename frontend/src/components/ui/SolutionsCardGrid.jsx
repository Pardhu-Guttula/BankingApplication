import React, { useMemo, useState } from "react";
import { useIntl } from "react-intl";
import SolutionCard from "./SolutionCard";

export default function SolutionsCardGrid({
  items: itemsProp,
  onCardClick = () => {},
  onTagClick = () => {},
  onSearchChange = () => {},
  initialSearch = "",
}) {
  useIntl();
  const [search, setSearch] = useState(initialSearch);

  const items = useMemo(() => {
    if (Array.isArray(itemsProp) && itemsProp.length) return itemsProp;
    return [];
  }, [itemsProp]);

  const filtered = useMemo(() => {
    const q = search.trim().toLowerCase();
    if (!q) return items;
    return items.filter((it) => {
      const hay = `${it.title} ${it.description} ${(it.tags || []).join(" ")}`.toLowerCase();
      return hay.includes(q);
    });
  }, [items, search]);

  return (
    <section className="mx-auto w-full max-w-[1120px] px-4 pb-10">
      <div className="grid grid-cols-1 gap-5 md:grid-cols-2 lg:grid-cols-3">
        {filtered.map((card) => (
          <SolutionCard key={card.id} {...card} onClick={onCardClick} onTagClick={onTagClick} />
        ))}
      </div>
    </section>
  );
}