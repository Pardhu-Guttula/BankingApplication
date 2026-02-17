import React from "react";
import { useIntl } from "react-intl";
import ProductCard from "./ui/ProductCard";

const imgWd4TbGamingDriveWorksWithPlaystation4PortableExternalHardDrive =
  "https://www.figma.com/api/mcp/asset/ff942c70-dad6-4cf8-a4a7-9c06d76834f6";

export default function ProductCardPage({ onAddToCart = () => {}, onNavigateToPdp = () => {} }) {
  const intl = useIntl();

  return (
    <section
      aria-label={intl.formatMessage({ id: "productCardPage.ariaProductCard" })}
      className="flex min-h-screen w-full items-center justify-center bg-white p-4"
    >
      <ProductCard
        imageSrc={imgWd4TbGamingDriveWorksWithPlaystation4PortableExternalHardDrive}
        category={intl.formatMessage({ id: "common.categoryElectronics" })}
        title={intl.formatMessage({ id: "productCardPage.productTitle" })}
        ratingValue={4}
        reviewCount={400}
        price={114}
        onAddToCart={onAddToCart}
        onNavigateToPdp={onNavigateToPdp}
      />
    </section>
  );
}