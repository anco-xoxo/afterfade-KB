# Backlog Log

Deferred items to revisit when ready.

---

## 1. Google Drive Auto-Sync (GitHub → GDrive)

- **Status:** Pending setup
- **What:** GitHub Action to auto-upload SOP files from `kb/policies/` to shared Google Drive folder
- **Folder ID:** `1EkJP_8WbCTL7xxz3RIT5zbbUEkbKE9U_`
- **Service account:** `anco@imaginxt.info` (needs access to folder)
- **Needs:**
  - [ ] JSON key file from service account
  - [ ] Share Drive folder with `anco@imaginxt.info` as Editor
  - [ ] Add JSON key as GitHub secret `GOOGLE_SERVICE_ACCOUNT_KEY`
- **Priority:** Medium

---

## 2. Dashboard Cross-Device Sync (GitHub API)

- **Status:** Pending implementation
- **What:** Add GitHub API integration to CS Dashboard so daily card data persists across devices (currently browser localStorage only)
- **Approach:** Use GitHub Contents API to read/write `dashboard/data/cards/YYYY-MM-DD.json` files
- **Needs:**
  - [ ] Personal access token or GitHub App with repo write access
  - [ ] Add token as GitHub secret or environment variable
  - [ ] Update `storage.js` to fetch/save via GitHub API
- **Priority:** Low (nice-to-have)
