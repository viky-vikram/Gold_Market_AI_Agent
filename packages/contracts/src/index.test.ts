import { describe, expect, it } from "vitest";

import { API_BASE_PATH, PACKAGE_NAME } from "./index.js";

describe("@aurumiq/contracts workspace package", () => {
  it("resolves from the pnpm workspace", () => {
    expect(PACKAGE_NAME).toBe("@aurumiq/contracts");
  });

  it("declares the /v1 REST base path required by the contracts specification", () => {
    expect(API_BASE_PATH).toBe("/v1");
  });
});
