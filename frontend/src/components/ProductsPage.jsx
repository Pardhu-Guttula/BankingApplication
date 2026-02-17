import React, { useMemo, useState } from "react";
import { useIntl } from "react-intl";
import FiltersSidebar from "./layout/FiltersSidebar";
import ProductsToolbar from "./layout/ProductsToolbar";
import Pagination from "./layout/Pagination";
import ProductsGridSection from "./layout/ProductsGridSection";

const imgFjallravenFoldsackNo1BackpackFits15Laptops =
  "https://www.figma.com/api/mcp/asset/a5e9e67b-09ca-405f-b736-0da294c557b6";
const imgMensCasualPremiumSlimFitTShirts =
  "https://www.figma.com/api/mcp/asset/02215831-f950-4f3e-9230-3dc40254d805";
const imgMensCottonJacket =
  "https://www.figma.com/api/mcp/asset/37a10880-4464-472b-85e3-61d4865bf845";
const imgMensCasualSlimFit =
  "https://www.figma.com/api/mcp/asset/ead4cbd8-fddf-4ec6-bad0-77cb6936165f";
const imgJohnHardyWomensLegendsNagaGoldSilverDragonStationChainBracelet =
  "https://www.figma.com/api/mcp/asset/77064129-6422-4fb1-bf8f-6e93a1ca50e4";
const imgSolidGoldPetiteMicropave =
  "https://www.figma.com/api/mcp/asset/cddad938-088e-44e5-a5d0-5e49be6e627c";
const imgWhiteGoldPlatedPrincess =
  "https://www.figma.com/api/mcp/asset/86c63afa-531d-413e-9c6e-140e611f7826";
const imgPiercedOwlRoseGoldPlatedStainlessSteelDouble =
  "https://www.figma.com/api/mcp/asset/eaf80f46-0d3d-4866-92e8-dea2454330d9";
const imgWd2TbElementsPortableExternalHardDriveUsb30 =
  "https://www.figma.com/api/mcp/asset/c12bc3b9-54f2-4353-a762-f99ef847c2a3";
const imgSanDiskSsdPlus1TbInternalSsdSataIii6GbS =
  "https://www.figma.com/api/mcp/asset/23b21abd-d1a7-419d-b6bd-ea0ae0f2a6b8";
const imgSiliconPower256GbSsd3DNandA55SlcCachePerformanceBoostSataIii25 =
  "https://www.figma.com/api/mcp/asset/34f3ef21-5d78-4105-9ff6-5692991e86bf";
const imgWd4TbGamingDriveWorksWithPlaystation4PortableExternalHardDrive =
  "https://www.figma.com/api/mcp/asset/3707d9d7-c247-4195-8233-29f27de5ff6b";

export default function ProductsPage() {
  const intl = useIntl();

  const categories = useMemo(
    () => [
      { id: "all", label: intl.formatMessage({ id: "common.all" }), count: null },
      {
        id: "electronics",
        label: intl.formatMessage({ id: "common.electronics" }),
        count: 6,
      },
      {
        id: "jewelery",
        label: intl.formatMessage({ id: "common.jewelery" }),
        count: 4,
      },
      {
        id: "mens-clothing",
        label: intl.formatMessage({ id: "common.mensClothing" }),
        count: 4,
      },
      {
        id: "womens-clothing",
        label: intl.formatMessage({ id: "common.womensClothing" }),
        count: 6,
      },
    ],
    [intl]
  );

  const products = useMemo(
    () => [
      {
        id: "p1",
        imageUrl: imgFjallravenFoldsackNo1BackpackFits15Laptops,
        category: intl.formatMessage({ id: "common.mensClothingLower" }),
        title: intl.formatMessage({ id: "products.p1.title" }),
        rating: 3.5,
        reviewCount: 120,
        price: "$109.95",
        href: "/pdp.html",
      },
      {
        id: "p2",
        imageUrl: imgMensCasualPremiumSlimFitTShirts,
        category: intl.formatMessage({ id: "common.mensClothingLower" }),
        title: intl.formatMessage({ id: "products.p2.title" }),
        rating: 4,
        reviewCount: 259,
        price: "$22.30",
        href: "/pdp.html",
      },
      {
        id: "p3",
        imageUrl: imgMensCottonJacket,
        category: intl.formatMessage({ id: "common.mensClothingLower" }),
        title: intl.formatMessage({ id: "products.p3.title" }),
        rating: 4.5,
        reviewCount: 500,
        price: "$55.99",
        href: "/pdp.html",
      },
      {
        id: "p4",
        imageUrl: imgMensCasualSlimFit,
        category: intl.formatMessage({ id: "common.mensClothingLower" }),
        title: intl.formatMessage({ id: "products.p4.title" }),
        rating: 2,
        reviewCount: 430,
        price: "$15.99",
        href: "/pdp.html",
      },
      {
        id: "p5",
        imageUrl:
          imgJohnHardyWomensLegendsNagaGoldSilverDragonStationChainBracelet,
        category: intl.formatMessage({ id: "common.jeweleryLower" }),
        title: intl.formatMessage({ id: "products.p5.title" }),
        rating: 4.5,
        reviewCount: 400,
        price: "$695.00",
        href: "/pdp.html",
      },
      {
        id: "p6",
        imageUrl: imgSolidGoldPetiteMicropave,
        category: intl.formatMessage({ id: "common.jeweleryLower" }),
        title: intl.formatMessage({ id: "products.p6.title" }),
        rating: 3.5,
        reviewCount: 70,
        price: "$168.00",
        href: "/pdp.html",
      },
      {
        id: "p7",
        imageUrl: imgWhiteGoldPlatedPrincess,
        category: intl.formatMessage({ id: "common.jeweleryLower" }),
        title: intl.formatMessage({ id: "products.p7.title" }),
        rating: 3,
        reviewCount: 400,
        price: "$9.99",
        href: "/pdp.html",
      },
      {
        id: "p8",
        imageUrl: imgPiercedOwlRoseGoldPlatedStainlessSteelDouble,
        category: intl.formatMessage({ id: "common.jeweleryLower" }),
        title: intl.formatMessage({ id: "products.p8.title" }),
        rating: 1.5,
        reviewCount: 100,
        price: "$10.99",
        href: "/pdp.html",
      },
      {
        id: "p9",
        imageUrl: imgWd2TbElementsPortableExternalHardDriveUsb30,
        category: intl.formatMessage({ id: "common.electronicsLower" }),
        title: intl.formatMessage({ id: "products.p9.title" }),
        rating: 3,
        reviewCount: 203,
        price: "$64.00",
        href: "/pdp.html",
      },
      {
        id: "p10",
        imageUrl: imgSanDiskSsdPlus1TbInternalSsdSataIii6GbS,
        category: intl.formatMessage({ id: "common.electronicsLower" }),
        title: intl.formatMessage({ id: "products.p10.title" }),
        rating: 2.5,
        reviewCount: 470,
        price: "$109.00",
        href: "/pdp.html",
      },
      {
        id: "p11",
        imageUrl:
          imgSiliconPower256GbSsd3DNandA55SlcCachePerformanceBoostSataIii25,
        category: intl.formatMessage({ id: "common.electronicsLower" }),
        title: intl.formatMessage({ id: "products.p11.title" }),
        rating: 4.5,
        reviewCount: 319,
        price: "$109.00",
        href: "/pdp.html",
      },
      {
        id: "p12",
        imageUrl: imgWd4TbGamingDriveWorksWithPlaystation4PortableExternalHardDrive,
        category: intl.formatMessage({ id: "common.electronicsLower" }),
        title: intl.formatMessage({ id: "products.p12.title" }),
        rating: 4.5,
        reviewCount: 400,
        price: "$114.00",
        href: "/pdp.html",
      },
    ],
    [intl]
  );

  const [selectedCategoryIds, setSelectedCategoryIds] = useState(["all"]);
  const [minPrice, setMinPrice] = useState("");
  const [maxPrice, setMaxPrice] = useState("");

  const [sortValue, setSortValue] = useState("featured");
  const [viewMode, setViewMode] = useState("grid");

  const [page, setPage] = useState(1);

  function handleApplyFilters(payload) {
    setSelectedCategoryIds(payload.selectedCategoryIds);
    setMinPrice(payload.minPrice);
    setMaxPrice(payload.maxPrice);
  }

  function handleClearFilters() {
    setSelectedCategoryIds(["all"]);
    setMinPrice("");
    setMaxPrice("");
  }

  function handleToggleCategory(id) {
    setSelectedCategoryIds([id]);
  }

  function handleAddToCart(productId) {
    // no-op (preserve behavior)
    void productId;
  }

  function handleNavigateProduct(productId, href) {
    // no-op (preserve behavior)
    void productId;
    void href;
  }

  function handleToggleWishlist(productId) {
    // no-op (preserve behavior)
    void productId;
  }

  return (
    <main className="min-h-screen w-full bg-[#3f3f3f]">
      <div className="mx-auto w-full max-w-[1352px] px-[16px] py-[18px]">
        <div className="flex items-start gap-[32px]">
          <FiltersSidebar
            categories={categories}
            selectedCategoryIds={selectedCategoryIds}
            minPrice={minPrice}
            maxPrice={maxPrice}
            onToggleCategory={handleToggleCategory}
            onChangeMinPrice={setMinPrice}
            onChangeMaxPrice={setMaxPrice}
            onApply={handleApplyFilters}
            onClear={handleClearFilters}
          />

          <section className="flex w-full flex-col gap-[20px]">
            <ProductsToolbar
              sortValue={sortValue}
              onSortChange={setSortValue}
              viewMode={viewMode}
              onViewModeChange={setViewMode}
            />

            <div id="productsContainer" className="w-full">
              <ProductsGridSection
                products={products}
                onAddToCart={handleAddToCart}
                onNavigateProduct={handleNavigateProduct}
                onToggleWishlist={handleToggleWishlist}
              />
            </div>

            <div id="pagination" className="w-full">
              <Pagination
                page={page}
                totalPages={2}
                onPageChange={setPage}
              />
            </div>
          </section>
        </div>
      </div>
    </main>
  );
}