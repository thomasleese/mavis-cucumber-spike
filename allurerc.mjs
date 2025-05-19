import { defineConfig } from "allure";

export default defineConfig({
  name: "Manage vaccinations in schools",
  output: "allure-report",
  plugins: {
    awesome: {
      options: {
        singleFile: false,
        reportLanguage: "en",
        groupBy: ["feature"],
      },
    },
  },
  environments: Object.assign(...[
    "desktop_chromium",
    "desktop_firefox",
    "desktop_safari",
    "iphone_15",
    "pixel_7",
  ].map((device) => ({
    [device]: {
      matcher: ({ labels }) =>
        labels.find(({ name, value }) => name === "device" && value === device),
    },
  }))),
});
