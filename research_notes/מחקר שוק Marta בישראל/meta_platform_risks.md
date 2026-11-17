# Meta Platform, API Access & Platform-Dependency Risks for "Marta" (AI agent acting on customers' Meta Business accounts) — status as of 17 Nov 2026

Method note for the report writer: this session's network blocked direct page fetches of developers.facebook.com and techcrunch.com (DNS blocked by sandbox allowlist). All findings below come from search-engine extraction of those pages plus secondary sources (trade press, vendor blogs, SEC filings, EU sources). Items attributed to Meta docs are from search-extracted text of the cited doc URL, not a full read. Several numeric details (rate limits, thresholds, prices) come from vendor blogs and are flagged as such. Re-verify every number against the cited Meta URL before publishing.

---

## 1. Marketing API access: app type, permissions, access tiers, App Review, Business Verification, rate limits, rules for tools acting on behalf of other businesses

### Takeaway
Meta charges nothing for Marketing API access. But to manage *other* businesses' ad accounts, Marta needs Business Verification, App Review for Advanced Access on each permission (ads_management, ads_read, business_management, etc.), and the top level of the "Marketing API Access Tier". In May 2026 Meta renamed the tier levels from Standard/Advanced to **Limited/Full Access**, and the Full Access bar reportedly dropped to 500 API calls in 15 days with an error rate under 15%. The usual reason ads_management reviews get rejected is that the screencast shows no working flow where an outside client grants access.

### Cited Findings
- **History of the tiers.** In 2018 Meta cut the Marketing API from three access levels to two, "Development Tier" and "Standard Tier". Dev Tier needed no App Review or Business Verification. Standard Tier needed both. Legacy basic/standard apps were mapped to Standard Tier with ads_read and/or ads_management. — [Meta for Developers blog, 2 Jul 2018](https://developers.facebook.com/ads/blog/post/v2/2018/07/02/marketing-api-tier-simplification/)
- **The 2026 rename (NEW).** Meta's rate-limiting doc says the feature is now called "Marketing API Access Tier". "Standard Access" became **Limited access** and "Advanced Access" became **Full access**. Adding the Marketing API product in the App Dashboard gives an app the Limited tier by default. The permission identifier itself is unchanged, and existing access levels carried over automatically. — [Meta: Marketing API Rate Limiting](https://developers.facebook.com/documentation/ads-commerce/marketing-api/overview/rate-limiting); [Lilach Bullock: Meta Marketing API tiers](https://www.lilachbullock.com/meta-marketing-api/); [meta-ads.si](https://meta-ads.si/what-are-marketing-api-access-tiers/)
- **Date of the rename.** Third-party guides date it to **4 May 2026**. — [com8.io](https://www.com8.io/blog/how-to-get-meta-api-access); [get-ryze.ai](https://www.get-ryze.ai/blog/meta-marketing-api-free-tier-limitations-and-quotas)
- **Full Access threshold (vendor-reported).** It reportedly fell from 1,500 to **500 Marketing API calls in the past 15 days**, with an error rate below **15%**. Some guides still quote 1,500, so the threshold is not settled. — [get-ryze.ai](https://www.get-ryze.ai/blog/meta-marketing-api-free-tier-limitations-and-quotas); [superscale.ai playbook](https://superscale.ai/learn/how-to-automate-meta-ads-ai-agents/)
- **Permission access levels keep the old names.** Individual permissions such as ads_read still use "Standard / Advanced access". The Limited/Full labels apply only to the Marketing API tier. — [get-ryze.ai](https://www.get-ryze.ai/blog/meta-marketing-api-free-tier-limitations-and-quotas)
- **Own accounts vs client accounts.** Meta's authorization page says standard access to ads_read and ads_management is enough only for an app that manages the developer's *own* ad account. Advanced access is needed to manage other people's ad accounts. — [overads.io (quoting Meta's authorization page)](https://overads.io/blog/read-only-ad-access); [adamigo.ai](https://www.adamigo.ai/blog/meta-ads-api-access-levels-for-agencies)
- **Advanced Access applications.** Advanced Access needs a separate application for each permission, and Business Verification is required. — [adamigo.ai](https://www.adamigo.ai/blog/meta-ads-api-access-levels-for-agencies); [Medium: "The Advanced Access Trap"](https://medium.com/@bilal.105.ahmed/facebook-marketing-api-the-advanced-access-trap-that-nearly-killed-my-project-7227ea2ee2c2)
- **Common App Review rejection reasons (2026 guides):**
  - The screencast shows only the developer's own ad account, with no working flow for an outside business to grant access. This is called the most common ads_management rejection.
  - Business Verification is not finished. One guide says such a submission "will be automatically rejected".
  - Weak screencasts, generic privacy policies or vague use cases.
  - Asking for permissions "just in case".
  - App left in development mode, or reviewer test accounts without a tester role.
  — [singhamandeep.com 2026 guide](https://singhamandeep.com/facebook-ads-api-permission-app-review/); [woopsocial.com](https://woopsocial.com/blog/meta-app-review-rejected-2026-fix-guide); [dojolabs.co](https://dojolabs.co/blog/meta-app-review-rejected-what-to-fix/)
- **Review timeline.** A general Meta App Review guide gives **3–7 business days** for a standard review. The figure is not specific to ads_management, and Business Verification adds its own delay. — [saurabhdhar.com](https://www.saurabhdhar.com/blog/meta-app-approval-guide)
- **Partial approvals happen (anecdote).** One app reports that on **28 Jul 2026** Meta approved ads_read and business_management but declined ads_management. — [overads.io](https://overads.io/blog/read-only-ad-access)
- **Rate-limit scoring (Meta doc as quoted by a vendor):**
  - Maximum score is **60** on the development/Limited tier and **9,000** on the standard/Full tier.
  - Decay window is **300 seconds**.
  - Throttling is per ad account.
  - A read call costs 1 point and a write call costs 3 points.
  — [goodmorningco.com](https://goodmorningco.com/blog/meta-marketing-api-rate-limits)
- **Same limits as hourly figures.** Limited works out to about **720 reads/hour per ad account** and Full to about **108,000/hour**. — [get-ryze.ai](https://www.get-ryze.ai/blog/meta-marketing-api-free-tier-limitations-and-quotas)
- **A different, lower figure.** Vendor blogs about AI connectors quote roughly **200 calls/hour per ad account**. This conflicts with the scoring model above and is unverified. — [get-ryze.ai (AI safety post)](https://www.get-ryze.ai/blog/will-connecting-ai-to-ads-account-get-you-banned-2026); [dtcskills.com](https://dtcskills.com/blog/meta-mcp-without-getting-banned)
- **Bulk automated rules (NEW, limited availability).** Since **22 Sep 2026**, developers can set ad rules in bulk through the Marketing API. Meta lists this as limited availability. — [search extraction citing superscale.ai / adsuploader](https://adsuploader.com/blog/meta-ads-updates)

### Inferences
- **The scoring model is consistent.** 60 points per 300 s equals 720 one-point reads per hour, and 9,000 per 300 s equals 108,000 per hour. The two vendor figures therefore agree with each other. The "~200 calls/hour" figure is the outlier.
- **Limited tier is far too low for a multi-tenant agent.** 720 reads per hour per ad account would not support an AI agent that pulls insights and makes edits for many clients, so Full Access is a launch prerequisite.
- **There is a chicken-and-egg problem.** Full Access needs real call volume (500 or 1,500 calls in 15 days) made on Limited access, so Marta must run a pilot with its own or test ad accounts first.
- **Realistic critical path (inference, not a Meta-published SLA).**
  - Business Verification: days to weeks.
  - App Review for each permission: 3–7 business days per round, often 2–3 rounds.
  - Building call volume for Full Access: about 2+ weeks.
  - Total: roughly **4–12 weeks**, with real risk that ads_management is declined on the first attempt.
- **Likely permission set (from background knowledge of Meta's permission reference, NOT re-verified in this session):**
  - Ads: ads_management, ads_read, business_management.
  - Pages: pages_show_list, pages_read_engagement, pages_manage_ads, pages_manage_posts.
  - Lead ads: leads_retrieval.
  - Instagram (Instagram API with Facebook Login): instagram_basic, instagram_content_publish, instagram_manage_comments, instagram_manage_insights.
  - Pixel/CAPI: covered by ads_management / business_management.
  - WhatsApp: whatsapp_business_management, whatsapp_business_messaging.
  - Each permission is a separate App Review submission with its own screencast.
- **Direct cost to Meta is $0.** The real cost is engineering time, compliance documentation (privacy policy, data deletion callback, Data Use Checkup), and delay.

### Gaps
- Could not read Meta's App Review / Access Levels / Business Verification pages directly. No official 2026 SLA for Advanced Access review on ads permissions was found.
- No source confirmed a formal **"Meta Business Partner" / Marketing Partner** requirement for SaaS tools that create ads for other businesses. It appears optional (a badge/program), but this was not verified this session.
- Exact current official numbers for the Full Access threshold (500 vs 1,500) and for the Insights-specific throttle could not be confirmed from Meta's own page.
  - From background knowledge, not re-verified: Insights uses a separate `x-fb-ads-insights-throttle` header, and large queries should use async report runs.
- No first-hand 2026 forum data on approval rates for ads_management.

---

## 2. Custom Audiences, hashing, and 2025–2026 targeting/data restrictions (health, financial, exclusions, special ad categories)

### Takeaway
Customer-list Custom Audiences still work. Data must be normalized and plain-SHA-256 hashed and uploaded via `/{audience_id}/users`. Since 2025, however, Meta has proactively blocked any custom or lookalike audience, and flagged Pixel/CAPI events or custom conversions, that *suggest health conditions or financial status*. Meta also removed detailed-targeting exclusions (fully enforced 15 Jan 2026) and folded "Credit" into a broader **Financial Products and Services** special ad category. An AI agent that names audiences or events automatically ("diabetes_customers", "high_income_list") could get its customers' assets disabled.

### Cited Findings
- **Upload mechanics.** Create an empty custom audience with `subtype=CUSTOM` and `customer_file_source`. Add users with a POST to `/{audience_id}/users` and remove them with a DELETE to the same endpoint. — [Meta: Customer File Custom Audiences](https://developers.facebook.com/docs/marketing-api/audiences/guides/custom-audiences); [v25.0 version](https://developers.facebook.com/docs/marketing-api/audiences/guides/custom-audiences/v25.0)
- **Hashing.** Data must be hashed with **SHA256; other hashing mechanisms are not supported**. Data must be normalized first (trim and lowercase emails, E.164 phone numbers, etc.). A salted hash will never match. — [Meta: Custom Audiences guide](https://developers.facebook.com/docs/marketing-api/audiences/guides/custom-audiences)
- **Batch size (unofficial).** One unofficial integration reference gives a **10,000 users per request** limit. — [nerdistan internal API reference (unofficial)](https://docs-internal.cdp.nerdistan.com.ar/docs/integrations/facebook-ads/api-reference)
- **Health/financial audience blocking (Meta doc).** On **2 Sep 2025** Meta began rolling out "more proactive restrictions". Any custom or lookalike audience that suggests specific health conditions (examples given: arthritis, diabetes) or financial status (credit score, high income) "will be flagged and prevented from being used to run ad campaigns". — [Meta: Customer File Custom Audiences (ads-commerce docs)](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/custom-audiences)
- **Retroactive scope.** A July 2025 trade report said Meta would proactively disable audiences and custom conversions whose names, rules or metadata imply protected traits, *even if previously approved*. Lookalikes seeded from a flagged audience are also disabled. — [Accelerated Digital Media](https://www.accelerateddigitalmedia.com/insights/meta-continues-to-place-new-restrictions-on-health-advertising/); [ilkandigital.com](https://ilkandigital.com/blog/meta-health-wellness-restrictions-2026)
- **Customer List Custom Audiences Terms (secondary, unverified).** One blog says the terms, effective **3 Dec 2025**, prohibit audiences built from data that reflects or implies health, financial, or consumer-report information. — [Tech Savvy Insurance](https://techsavvyinsurance.com/blog/meta-custom-audiences-phi-insurance-agents-2026/)
- **Pixel/CAPI events.** Health-and-wellness-classified advertisers can lose lower-funnel events (e.g., Purchase) for optimization. A further naming rule applies to event, conversion and audience names whether they come via the Pixel or the Conversions API. — [ilkandigital.com](https://ilkandigital.com/blog/meta-health-wellness-restrictions-2026); [wittelsbach.ai](https://www.wittelsbach.ai/blog/meta-says-your-pixel-sends-restricted-data/)
- **Detailed-targeting exclusions removed.**
  - Removed from new ad sets on **31 Mar 2025** and from boosted posts on **10 Jun 2025**.
  - Ad sets still using removed options **stopped delivering on 15 Jan 2026**.
  - Meta's stated rationale: median cost per conversion improved **22.6%** without exclusions.
  — [PPC Land](https://ppc.land/meta-removes-detailed-targeting-exclusions-for-ad-accounts/); [Social Media Today](https://www.socialmediatoday.com/news/meta-removes-detailed-targeting-exclusions-from-ad-campaigns/723389/); [Wicked Reports](https://www.wickedreports.com/blog/meta-removes-detailed-targeting-exclusions-from-ad-campaigns)
- **Special ad categories.**
  - A **Financial Products and Services** category replaces "Credit". `FINANCIAL_PRODUCTS_SERVICES` is a valid `special_ad_categories` value in the Marketing API.
  - Housing, Employment and Financial Products and Services share one set of audience limits. Lookalikes, saved audiences, targeting expansion, bid multipliers, location exclusions and detailed-targeting exclusions are unavailable.
  - Running financial ads without declaring the category leads to rejection.
  — [Meta: Special Ad Category (Marketing API)](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category); [Data Axle](https://www.data-axle.com/resources/blog/meta-special-ad-categories-rules/); [MediaPost](https://www.mediapost.com/publications/article/408262/meta-further-consolidates-ad-targeting-options.)
- **Generative AI tools restricted for some advertisers.** Meta restricted political and regulated-industry advertisers from using its generative-AI ad tools. — [Seeking Alpha](https://seekingalpha.com/news/4031554-meta-restricts-political-advertisers-from-using-generative-ai-ads-tools)

### Inferences
- **Marta needs a sensitive-category guardrail.** The agent should refuse or warn before creating audiences, custom conversions or event names that imply health or financial status. It should also detect when a customer belongs in a Special Ad Category (financial, housing, employment) and set `special_ad_categories` itself.
- **Consent and contracts for list uploads.** Marta uploads customer lists *on behalf of* the advertiser. The advertiser must accept the Custom Audience Terms in its own ad account, and Marta's contract should make the advertiser warrant lawful basis and consent. Israel's Privacy Protection Law (Amendment 13, in force Aug 2025) is relevant here, but it is outside this research's scope.
- **Hash locally.** Marta should hash PII on its side or in the browser before upload and before any LLM sees it. This also limits exposure of raw PII to third-party LLMs (see section 6).

### Gaps
- Could not read the official Custom Audience Terms text (facebook.com/ads/manage/customaudiences/tos.php), so the 3 Dec 2025 terms change is unverified.
- No primary confirmation of the exact health-and-wellness "tier" mechanics, or of which countries they apply in (originally US-focused, January 2025).
- Did not verify current limits on minimum audience size or the number of custom audiences per ad account.

---

## 3. WhatsApp Business Platform: Tech Provider vs Solution Partner, Embedded Signup, pricing (July 2025 → 2026), limits, templates, opt-in, and the general-purpose-AI-chatbot ban

### Takeaway
Marta can integrate as a **Tech Provider**. That requires a Meta app with the WhatsApp use case, Business Verification, App Review, and Embedded Signup v4 (v2/v3 were deprecated 15 Oct 2026). Without a Solution Partner credit line, each customer must add its own payment method.

**Pricing.** Pricing is per-message for template messages (since 1 Jul 2025) and can change only on the first day of a quarter. 2026 changes include a max-price control for marketing messages (beta) and reported new charges for service and utility messages from Oct/Nov 2026. Israel marketing costs about **$0.041–0.042 per message**.

**The AI ban.** Effective 15 Oct 2025 for new users and **15 Jan 2026** for existing users, the WhatsApp Business Solution Terms bar "AI Providers" whose AI is the *primary* functionality. Business-specific bots (support, sales, bookings, order tracking) remain allowed. The EU forced Meta to reopen access in the EEA (interim measures, June 2026). Israel is not covered by that order.

### Cited Findings
**Tech Provider / Solution Partner / Embedded Signup**
- **Tech Provider requirements:**
  - A Meta app with the WhatsApp use case and a connected business portfolio.
  - Business Verification, then App Review.
  - Tech Providers must use **business tokens exclusively**.
  - To work with a Solution Partner (multi-partner solution), Marta needs that partner's app ID.
  — [Meta: Become a Tech Provider](https://developers.facebook.com/documentation/business-messaging/whatsapp/solution-providers/get-started-for-tech-providers); [Meta: Multi-Partner Solutions](https://developers.facebook.com/documentation/business-messaging/whatsapp/solution-providers/multi-partner-solutions)
- **Solution Partner (BSP) requirements.** Must already have a **line of credit** and have accepted the Credit Allocation API terms. Uses a system token to share credit with onboarded customers. — [Meta: Become a Tech Provider / partner docs](https://developers.facebook.com/documentation/business-messaging/whatsapp/solution-providers/get-started-for-tech-providers); [WhatsApp Business: Become a Partner](https://whatsappbusiness.com/partners/become-a-partner/)
- **Billing without a BSP credit line.** Each customer must attach its own payment method before messaging. — [infiq.in glossary (non-official)](https://www.infiq.in/glossary/tech-provider); [Infobip Tech Provider guide](https://www.infobip.com/docs/whatsapp/tech-provider-program/setup-and-integration)
- **Embedded Signup deprecation (NEW, 2026).** "Embedded Signup v2 and v3 will be deprecated on **October 15, 2026**, including their public preview versions. Migrate your integration to v4." — [Meta: Embedded Signup Implementation](https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/implementation/)
- **Coexistence with the WhatsApp Business app.** Existing app users can be onboarded with the WhatsApp Business app (v2.24.17+). This needs Embedded Signup with session logging and skips phone-number registration. — [Meta: Onboard WhatsApp Business app users](https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/)
- **Tech Provider Terms.** Developers may not use Applicable Platform Data for their own purposes or disclose it to third parties except as expressly allowed. Meta can terminate the terms on **30 days' written notice, with or without cause**. — [Meta Tech Provider Terms](https://www.facebook.com/legal/BM-tech-provider-terms)

**Pricing**
- **Per-message model and pricing calendar.** Meta moved to per-message pricing on **1 Jul 2025**. The pricing page reflects updates effective **1 Oct 2026**. Meta may change pricing **only on the 1st day of a quarter**. — [Meta: Pricing on the WhatsApp Business Platform](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing)
- **Max price for marketing (NEW, 2026, beta).** Meta is adding spend controls to the Marketing Messages API, starting with a per-message **max price**. Meta charges that price or lower, so marketing per-message pricing can vary. — [Meta: Marketing Messages pricing](https://developers.facebook.com/documentation/business-messaging/whatsapp/marketing-messages/pricing)
- **Service messages (NEW, Oct 2026, secondary sources).** Starting 1 Oct 2026, Meta reportedly charges for service (user-initiated reply) messages, which were previously free. Chatalog notes Meta had not published a full market-by-market service rate card as of Sep 2026. — [Green-API](https://green-api.com/articles/en/whatsapp-changes-rates-for-companies-and-business/); [Chatarmin](https://chatarmin.com/en/blog/whatsapp-business-costs); [Chatalog](https://docs.chatalog.ai/platform-setup/whatsapp-connection-guide/whatsapp-pricing-update)
- **Utility templates inside the service window (NEW).** These will "also be charged starting **November 1, 2026**". Another secondary source instead says 1 Oct 2026 with 1,000 free per number per month. **This conflicts.** — [Salesforce WhatsApp rate card Nov 2026](https://www.salesforce.com/en-us/wp-content/uploads/sites/4/WhatsApp-Business-Messaging-1000-Nov-2026.docx.pdf)
- **Israel rates (USD, secondary):**

  | Source | Marketing | Utility | Authentication | Notes |
  |---|---|---|---|---|
  | [SleekFlow](https://help.sleekflow.io/en_US/pricing) | $0.0406 | $0.0061 | $0.0061 | |
  | [Gallabox](https://docs.gallabox.com/pricing-and-billing/whatsapp-pricing/rate-card.md) | $0.0406 | $0.0061 | $0.0061 | |
  | [Chatalog](https://docs.chatalog.ai/platform-setup/whatsapp-connection-guide/whatsapp-pricing-update) | $0.0424 | $0.0064 | $0.0064 | Checked against Meta on 15 Sep 2026, ahead of the 1 Oct 2026 update |
  | [Salesforce Nov 2026](https://www.salesforce.com/en-us/wp-content/uploads/sites/4/WhatsApp-Business-Messaging-1000-Nov-2026.docx.pdf) | 43.59 | 6.55 | 6.55 | Unit unclear (likely per 1,000 messages, BSP markup possible); 6.55 also applies to service |

**Limits, quality, templates, opt-in**
- **Messaging limits (tiers).**
  - New portfolios start at **250 unique users per 24h**, then 2,000, 10,000, 100,000 or unlimited, depending on verification and quality.
  - Since **7 Oct 2025** the limit sits at the **business-portfolio level** and is shared by all of its numbers.
  — [Chatarmin: messaging limits](https://chatarmin.com/en/blog/whats-app-messaging-limits); [adnovamarketing](https://adnovamarketing.com/en/blog/whatsapp-api-messaging-limits/)
- **Per-user marketing frequency cap.** Meta limits how many marketing messages each person receives *from all businesses*, based on engagement. Vendors estimate about 2 marketing templates per user per day. Utility and authentication templates are exempt. The cap is reportedly not active for the EEA, UK, Japan and South Korea. — [payperwa.com](https://payperwa.com/blog/whatsapp-marketing-message-limits-frequency-cap-2026); [cloudfigma](https://pulse.cloudfigma.com/guides/whatsapp-marketing-message-limits)
- **US numbers.** WhatsApp "does not currently deliver marketing template messages" to US (+1) numbers (Meta page quoted by a vendor). — [payperwa.com](https://payperwa.com/blog/whatsapp-marketing-message-limits-frequency-cap-2026)
- **Marketing Messages API (MM API).**
  - The `/marketing_messages` endpoint accepts only marketing templates. Marketing can still go via Cloud API `/messages` unless disabled.
  - **Aug 2026 changelog:** businesses onboarded to MM API can disable marketing on Cloud API. `/messages` then rejects Marketing templates with error **131063**.
  - Prerequisites: an approved marketing-category template, an active WABA in an MM-API-eligible country, and a subscribed messages webhook.
  — [Meta WhatsApp changelog](https://developers.facebook.com/documentation/business-messaging/whatsapp/changelog); [Meta: Send Marketing Messages](https://developers.facebook.com/documentation/business-messaging/whatsapp/marketing-messages/send-marketing-messages.md); [Meta: MM API get started](https://developers.facebook.com/documentation/business-messaging/whatsapp/marketing-messages/get-started)
- **Opt-in (secondary summary of Meta policy).** Requires a clear user action, a statement that messages will come via WhatsApp, and consent tied to the phone number. — [auditsocials.com](https://www.auditsocials.com/blog/whatsapp-business-marketing-message-compliance-2026-opt-in-template-categories-per-message-pricing-meta)

**General-purpose AI chatbot ban**
- **The clause (as reproduced by secondary sources).** "Providers and developers of artificial intelligence or machine learning technologies, including but not limited to large language models, generative artificial intelligence platforms, general-purpose artificial intelligence assistants, or similar technologies as determined by Meta in its sole discretion ('AI Providers'), are strictly prohibited from accessing or using the WhatsApp Business Solution … when such technologies are the primary (rather than incidental or ancillary) functionality being made available for use." — [serviceform.com](https://www.serviceform.com/blog/whatsapp-ai-chatbots-in-2026/); [omago.ai](https://www.omago.ai/blog/meta-whatsapp-ai-chatbot-policy-2026-what-changed); [dig.watch](https://dig.watch/updates/meta-changes-whatsapp-terms-to-block-third-party-ai-assistants)
- **Effective dates.** **15 Oct 2025** for new API users and **15 Jan 2026** for existing users. — [TechCrunch, 18 Oct 2025](https://techcrunch.com/2025/10/18/whatssapp-changes-its-terms-to-bar-general-purpose-chatbots-from-its-platform/); [European Commission press release IP/26/310](https://ec.europa.eu/commission/presscorner/api/files/document/print/en/ip_26_310/IP_26_310_EN.pdf)
- **Meta's rationale.** The API was built for business messaging, and general-purpose chatbots were an "unanticipated use case". — [TechCrunch](https://techcrunch.com/2025/10/18/whatssapp-changes-its-terms-to-bar-general-purpose-chatbots-from-its-platform/)
- **Who was affected.** OpenAI (ChatGPT's WhatsApp contact stopped working after 15 Jan 2026) and Perplexity, among others. Meta AI was left as the only general-purpose assistant on WhatsApp. — [9to5Mac](https://9to5mac.com/2025/10/20/whatsapp-bans-ai-chatbots-from-using-its-business-api/); [Gulf News](https://gulfnews.com/technology/no-more-chatgpt-and-perplexity-on-whatsapp-meta-bans-major-ai-chatbots-from-2026-1.500316016)
- **What remains allowed.** AI used for defined business functions: customer support, reservations, order tracking, sales, notifications. — [dig.watch](https://dig.watch/updates/meta-changes-whatsapp-terms-to-block-third-party-ai-assistants); [respond.io](https://respond.io/blog/whatsapp-general-purpose-chatbots-ban)
- **Regulatory pushback (2026):**
  - **Dec 2025:** the EU opened a formal antitrust investigation (case **AT.41034**). — [TechRadar](https://www.techradar.com/pro/eu-launches-antitrust-investigation-into-metas-whatsapp-ai-access-policy); [EC case page AT.41034](https://competition-cases.ec.europa.eu/cases/AT.41034)
  - **Feb 2026:** Statement of Objections signalling interim measures. — [CNBC, 9 Feb 2026](https://www.cnbc.com/2026/02/09/eu-interim-measures-meta-whatsapp-ai-policy-antritrust.html)
  - **Mar 2026:** Meta readmitted rival AI chatbots in Europe *for a fee* of €0.0490–€0.1323 per non-template message, offered for one year. — [TechCrunch, 5 Mar 2026](https://techcrunch.com/2026/03/05/meta-will-allow-rival-ai-chatbots-on-whatsapp-in-europe-but-for-a-fee/); [Reuters via Yahoo](https://finance.yahoo.com/news/meta-allow-ai-rivals-whatsapp-122729247.html)
  - **9 Jun 2026:** the EC imposed **interim measures**. Meta must restore pre-15-Oct-2025 terms (free access) for rival general-purpose AI assistants in the EEA within five working days, until a final decision or June 2029. Meta called it "regulatory overreach" and said it will appeal. — [Houthoff](https://www.houthoff.com/insights/news/a-rare-show-offorce-commission-deploys-interim-measures-against-meta-to-safeguard-ai-competition/); [Quartz](https://qz.com/eu-meta-whatsapp-rival-ai-chatbots-antitrust-061026); [Washington Times](https://www.washingtontimes.com/news/2026/jun/9/5-questions-eus-order-meta-whatsapp-ai-access/); [EU Perspectives](https://euperspectives.eu/2026/06/commission-gives-meta-five-days-to-open-whatsapp-ai-to-competition/)
  - **Italy and Brazil:** Italy (AGCM) had earlier forced opening there. A Brazilian court reinstated an injunction. — [Silicon UK](https://www.silicon.co.uk/e-innovation/artificial-intelligence/meta-whatsapp-ai-628958); [TechCrunch (Brazil)](https://techcrunch.com/?p=3099928)

### Inferences
- **Marta's main WhatsApp use case looks allowed.** In that use case Marta's customers send marketing and utility templates and run *business-specific* AI customer-service bots for their own customers. The AI is incidental to a business's own messaging.
- **A grey zone exists.** If Marta lets *business owners* talk to "Marta" itself over a Marta-owned WhatsApp number (e.g., "launch a campaign for me"), Marta's LLM agent could be seen as an "AI Provider" whose AI is the "primary functionality". The clause is broad ("similar technologies as determined by Meta in its sole discretion"). Lower-risk design options:
  - Keep Marta's main UI on web or mobile.
  - Use WhatsApp only for notifications and approvals (utility templates) to the business owner.
  - Present any WhatsApp interaction as a scoped, single-business support or account-management function, not an open-ended assistant.
- **Israel is outside the EU's protection.** The EU interim measures apply only in the EEA, so the ban applies fully to Israeli customers.
- **Unit economics (inference).** At about $0.041 per Israeli marketing message, 10,000 recipients cost about **$410** in Meta fees per blast, before any Marta or BSP markup. Utility costs about $0.006 each. New service and utility-in-window charges from Oct/Nov 2026 raise the cost of AI customer-service conversations, which used to be free inside the 24h window.
- **Tech Provider path vs adding a BSP.**
  - **Tech Provider only:** faster and cheaper, but each SMB must add a card to its WABA, which adds onboarding friction.
  - **Tech Provider plus a BSP (multi-partner solution):** gives credit-line billing but adds a dependency and a margin.

### Gaps
- Could not read the official WhatsApp Business Solution Terms or the Business Messaging Policy directly. The clause wording comes from secondary reproductions.
- No official Meta statement found that specifically addresses "vertical B2B AI agents for business owners" under the AI Provider clause.
- Whether Meta has filed or won an appeal against the EU interim order, and whether it complied in practice, was not confirmed.
- Official Meta rates for Israel, the service-message rate card, and the exact effective date of utility charges inside the service window (1 Oct vs 1 Nov 2026) are unconfirmed.
- No official current timeline for Tech Provider App Review or for messaging-tier upgrades was found.

---

## 4. Meta's own AI competition: Advantage+, the "fully automated ads by end-2026" goal, Business AI / Business Agent, the Ads Manager AI assistant, the official Ads MCP server

### Takeaway
Meta now offers, **for free**, most of the "AI layer" Marta plans to sell:
- an agentic AI Business Assistant inside Ads Manager that can build ad sets, swap audiences, generate creative and adjust budgets (agentic upgrade announced Oct 2026);
- an **official Ads MCP server and CLI** (open beta since 29 Apr 2026) that lets Claude, ChatGPT and other MCP clients manage campaigns directly;
- a Business Agent used by more than 2 million businesses weekly;
- Advantage+ end-to-end automation, which Meta reportedly targeted for end-2026.

This sharply commoditizes a generic "chat with your Meta ads" product.

### Cited Findings
- **Official Ads MCP server.** Meta's docs describe "Ads AI Connectors" as a family of integrations that expose Meta business surfaces to third-party AI clients through structured, permission-scoped tools. — [Meta: Ads MCP Server overview](https://developers.facebook.com/documentation/ads-commerce/ads-ai-connectors/ads-mcp-server/ads-mcp-server-overview)
- **Launch details.**
  - Open beta from **29 Apr 2026** for eligible advertisers globally.
  - MCP server at **mcp.facebook.com/ads** plus an npm CLI.
  - Supported clients at launch: ChatGPT and Claude, "with more platforms added over time".
  - Free during the beta; long-term pricing not announced.
  — [Digiday](https://digiday.com/marketing/meta-opens-its-ad-ecosystem-to-third-party-ai-tools/); [Common Thread Co.](https://commonthreadco.com/blogs/coachs-corner/meta-ai-mcp-cli-ads-connectors-ecommerce); [affectgroup.com](https://affectgroup.com/blog/meta-ads-ai-connectors/)
- **Capabilities (vendor count).** **29 Marketing API tools** covering reporting, budget changes, campaign edits, catalog work and signal diagnostics, with OAuth permissions the advertiser controls. Read-write: an agent can create campaigns, edit ads, change budgets and pause delivery. — [pasqualepillitteri.it](https://pasqualepillitteri.it/en/news/1707/official-meta-ads-mcp-claude-29-tools-2026); [contextbolt.com](https://contextbolt.com/blog/meta-ads-mcp/); [adspirer.com](https://www.adspirer.com/blog/meta-ads-mcp)
- **Context for the launch.** Reportedly released after advertisers saw ad-account restrictions in early 2026 when connecting AI agents through *unofficial* connectors. Digiday reports no confirmed official link between bans and AI tools. Analysts attribute restrictions to access patterns (browser automation, scraped tokens, anti-detect setups, tight loops of 30+ budget changes per hour), not to AI itself. — [Common Thread Co.](https://commonthreadco.com/blogs/coachs-corner/meta-ai-mcp-cli-ads-connectors-ecommerce); [hyperfx.ai](https://www.hyperfx.ai/blog/will-connecting-claude-to-meta-ads-ban-account-2026); [get-ryze.ai](https://www.get-ryze.ai/blog/will-connecting-ai-to-ads-account-get-you-banned-2026); [dtcskills.com](https://dtcskills.com/blog/meta-mcp-without-getting-banned)
- **AI Business Assistant in Ads Manager.**
  - Rolled out to all advertisers and agencies (beta) around **22–24 Apr 2026**, at no extra cost.
  - Available across Ads Manager, Meta Business Suite and Business Support Home.
  — [MediaPost, 24 Apr 2026](https://www.mediapost.com/publications/article/414547/meta-rolls-out-ai-business-assistant-to-all-advert.html); [Kitchn: April 2026 updates](https://www.kitchn.io/blog/meta-ads-manager-updates-april-2026)
- **Agentic upgrade (Advertising Week NY, ~6–7 Oct 2026).**
  - The assistant can build ad sets, swap targeting audiences, generate creative and adjust budgets in real time through chat.
  - Safeguards reported: new ads start paused, work lands as drafts, and Business Suite rules can block actions such as budget increases above 20%.
  — [adgully](https://www.adgully.com/post/21851/meta-unveils-agentic-ai-capabilities-in-ads-manager-to-automate-campaign-execution); [Common Thread Co. (agentic)](https://commonthreadco.com/blogs/coachs-corner/metas-agentic-ai-now-runs-ads-manager-what-ecommerce-brands-must-do-before-q4); [Common Thread Co. (Advertising Week)](https://commonthreadco.com/blogs/coachs-corner/metas-new-ai-agent-can-now-run-your-ads-what-the-advertising-week-2026-update-means-for-ecommerce-brands)
- **Business Agent scale (primary source).** Meta's 2026 SEC free-writing prospectus says "more than 2 million businesses use our Business Agent weekly" and describes WhatsApp as an increasingly important platform for agents. — [Meta SEC FWP, 2026](https://www.sec.gov/Archives/edgar/data/0001326801/000119312526431036/d116268dfwp.htm)
- **Q3 2026 earnings call (21 Oct 2026):**
  - About 10 million advertisers used at least one generative-AI creative tool in the quarter.
  - Advertisers adopting Meta's recommendations drove about 5% more conversions at the same cost per conversion.
  - The AI Business Assistant is being integrated into Creator Marketing Hub, for "a conversational experience" to plan, create and optimize campaigns.
  - Zuckerberg named business agents among Meta's initial enterprise offerings, with longer-term plans to connect personal and commercial agents.
  - Revenue was $64.6B (+26%).
  — [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/10/21/meta-meta-q3-2026-earnings-call-transcript/); [StockAnalysis transcript](https://stockanalysis.com/stocks/meta/transcripts/718643-q3-2026/); [TradingView/Zacks](https://www.tradingview.com/news/zacks:9b2be09c3094b:0-meta-q3-earnings-call-put-spotlight-on-muse-growth-and-ai-spending/)
- **"Fully automated ads by end-2026".**
  - WSJ reported (June 2025) that Meta aimed to let brands "fully create and target ads using artificial intelligence by the end of next year": the advertiser supplies a product image or URL plus a budget, and Meta generates creative, copy and targeting.
  - This is not an established guaranteed deadline.
  - Advantage+ is the default for Sales, App and Leads campaigns, and manual and Advantage+ creation were merged into one flow by early 2026.
  — [Dataslayer (summarizing WSJ)](https://www.dataslayer.ai/blog/meta-plans-full-ai-advertising-automation-by-2026-what-this-actually-means); [Refonte Learning](https://www.refontelearning.com/blog/meta-advantage-plus-explained); [Breaking Brand](https://www.breakingbrand.com/news/meta-ai-automated-ads-2026)

### Inferences
- **Commoditization risk is HIGH for a generic layer.** Any SMB can already plug Claude or ChatGPT into Meta's official MCP for free, or use Meta's free agentic assistant inside Ads Manager. A thin "LLM + Marketing API" wrapper has little defensible value.
- **Defensible angles (inference):**
  - Hebrew and Israel-local context: local holidays, regulation, Hebrew copywriting quality.
  - Cross-channel orchestration: Meta ads plus WhatsApp plus CRM, plus Google/TikTok, which Meta's tools will never cover.
  - Done-for-you outcomes and service for non-expert SMBs.
  - Guardrails, approvals and compliance (sensitive categories, opt-in).
  - Unified reporting across platforms.
  - Agency or multi-client workflow.
- **Strategic option.** Marta could consume Meta's own MCP server as a tool layer instead of, or alongside, direct Marketing API calls. That reduces "unofficial connector" ban risk but deepens dependency. It is unclear whether a multi-tenant SaaS (as opposed to an advertiser's own AI client) may use the MCP server on clients' behalf (see Gaps).
- **Meta's incentive structure.** Meta's tools optimize for Meta spend. An independent agent can credibly position itself as advertiser-side: budget discipline, cross-platform allocation.

### Gaps
- Could not read Meta's MCP server docs in full. Unknown: the terms of use for SaaS vendors embedding the MCP server, rate limits, whether a Meta developer app is required, and post-beta pricing. One unattributed secondary claim that the server opened to "all developers with a Meta app" on 16 Jul 2026 could not be verified.
- Could not access the original WSJ article (June 2025). No Meta primary statement confirming an end-2026 deadline for fully automated ads.
- Availability of the agentic assistant in Israel or in Hebrew is unknown.

---

## 5. Platform-risk history: third-party tools hurt by Meta API changes, and how they mitigated

### Takeaway
Meta has repeatedly removed or narrowed APIs at short notice, sometimes about 90 days:
- the Groups API in 2024;
- the Instagram Basic Display API in Dec 2024;
- the WhatsApp general-purpose AI ban in 2025–26;
- retiring audience/targeting features (exclusions, sensitive audiences, 2025–26);
- the post-Cambridge-Analytica lockdown in 2018 (from background knowledge, not verified here).

Affected companies either dropped features (Make, Zoho, schedulers), migrated to the newer official API, or sought regulatory relief (OpenAI and others via the EU and Italy).

### Cited Findings
- **Facebook Groups API (2024).**
  - Deprecated in v19.0 (announced 23 Jan 2024) and removed from all versions within 90 days, by about 22 Apr 2024.
  - Social-management tools were hit. Make discontinued its Facebook Groups app.
  — [Gigazine](https://gigazine.net/gsc_news/en/20240206-meta-cuts-third-party-access-facebook-groups); [Ayrshare](https://www.ayrshare.com/blog/facebook-removes-groups-api-access-impact-and-implications/); [Make Community](https://community.make.com/t/due-to-the-deprecation-of-the-facebook-groups-api-we-make-will-be-discontinuing-our-facebook-groups-app/32624); [TechPoint Africa](https://techpoint.africa/2024/02/06/meta-facebook-disrupts-scheduling)
- **Instagram Basic Display API (2024).**
  - From **4 Dec 2024** all requests return errors, leaving no Instagram API for consumer apps.
  - Business and creator use cases had to migrate to the Instagram API (Facebook Login with a linked Page, or the newer Instagram Login for professional accounts).
  — [Meta Developers blog, 4 Sep 2024](https://developers.facebook.com/blog/post/2024/09/04/update-on-instagram-basic-display-api); [Meta: Instagram Basic Display API](https://developers.secure.facebook.com/docs/instagram-basic-display-api); [TechCrunch, 6 Dec 2024](https://techcrunch.com/2024/12/06/instagram-locks-out-developers-of-third-party-consumer-apps); [Behold.so](https://behold.so/updates/basic-display-api-deprecated)
- **WhatsApp AI-provider ban (2025–26).** It shut down ChatGPT and Perplexity on WhatsApp. Mitigation came through regulators: the EU interim measures, Italy's AGCM and a Brazilian court. — see section 3; [Quartz](https://qz.com/eu-meta-whatsapp-rival-ai-chatbots-antitrust-061026)
- **Unofficial AI connectors (2026).** Early-2026 ad-account restrictions were reported for unofficial AI connectors. Meta then offered an official MCP path. — [Common Thread Co.](https://commonthreadco.com/blogs/coachs-corner/meta-ai-mcp-cli-ads-connectors-ecommerce)
- **Graph API v26.0 (29 Jul 2026).** It blocked **47 commerce endpoints**. Several v26 changes extend to *all* Marketing API versions, including unversioned calls, on **27 Oct 2026**. — [PPC Land](https://ppc.land/meta-blocks-47-commerce-endpoints-as-graph-api-v26-0-lands-today/)
- **Metric retirements (2026).** Meta retired metrics in Q2 2026, which affects dashboards built on the Insights API. — [Kitchn: Marketing API Q2 2026 update](https://www.kitchn.io/blog/meta-marketing-api-q2-2026-update)

### Inferences
- **Recurring pattern.** Meta tends to deprecate (a) consumer-data surfaces, (b) features that compete with its own products (general AI chat vs Meta AI), and (c) targeting levers tied to privacy and regulation. Marta touches (b) and (c) directly.
- **Mitigations seen in the market:**
  - Building only on business-scoped, officially supported endpoints.
  - Keeping thin adapters for fast migration.
  - Multi-platform coverage, so no single API removal kills the product.
  - Joining partner programs to get earlier notice.
  - For dominant-platform foreclosure, regulatory channels (EU only; Israel has no equivalent leverage).

### Gaps
- No sourced results this session for the **2018 Cambridge Analytica lockdown**. From background knowledge, not verified here: in April 2018 Facebook paused App Review, cut many APIs and required re-review and Business Verification. Re-verify before use.
- No sourced 2025–26 cases of Marketing API *permission revocations* for specific ad-tech SaaS companies.

---

## 6. Technical considerations: versioning cadence, rate limits, webhooks, tokens, and data use (sending Meta data to third-party LLMs)

### Takeaway
- **Versioning.** Graph and Marketing API versions ship about two to three times a year: v25.0 on 18 Feb 2026, v26.0 on 29 Jul 2026, v27.0 reportedly on 4 Nov 2026. Marketing API versions expire much faster than Graph API versions, roughly 12 months versus about 2 years.
- **Tokens.** Tech Providers must use business/system-user tokens.
- **Data use.** The Platform Terms bind any service provider or sub-processor (including an LLM vendor) to the same requirements in writing. Meta can demand the list of providers and order Marta to stop using one. The terms reportedly restrict using Platform Data to train AI models. The WhatsApp Tech Provider Terms forbid using customer data for Marta's own purposes.

### Cited Findings
- **Release dates.** v25.0 released **18 Feb 2026**. v26.0 released **29 Jul 2026**. v27.0 reportedly released **4 Nov 2026** (single source). — [Kitchn Q2 2026](https://www.kitchn.io/blog/meta-marketing-api-q2-2026-update); [PPC Land](https://ppc.land/meta-blocks-47-commerce-endpoints-as-graph-api-v26-0-lands-today/); [adsuploader Nov 2026](https://adsuploader.com/blog/meta-ads-updates)
- **Expiry dates differ by API.** The Graph API changelog lists v25.0 until **29 Jul 2028**. The Marketing API changelog lists v25.0 until **23 Feb 2027**. v24.0 Marketing API is listed until about **10 Nov 2026** (Graph: 6 Oct 2026, a conflict). v23.0 reached end of life on **9 Jun 2026**. — [Meta: Graph API Versions](https://developers.facebook.com/docs/graph-api/changelog/versions/); [app369 version expiry](https://app369.com/blog/facebook-graph-api-version-expiry-dates-2027/); [useadstudio version tracker](https://useadstudio.com/tools/ad-api-version-tracker)
- **Token rules.**
  - WhatsApp Tech Providers must use **business tokens exclusively**. — [Meta: Become a Tech Provider](https://developers.facebook.com/documentation/business-messaging/whatsapp/solution-providers/get-started-for-tech-providers)
  - Solution Partners use system tokens for credit sharing. — same source
  - Restrictions were tied to "scraped tokens" and browser automation. — [get-ryze.ai](https://www.get-ryze.ai/blog/will-connecting-ai-to-ads-account-get-you-banned-2026)
- **Webhooks.** The MM API requires a subscribed messages webhook. — [Meta: MM API get started](https://developers.facebook.com/documentation/business-messaging/whatsapp/marketing-messages/get-started)
  - Webhook changes appeared in the Q2 2026 Marketing API update. — [Kitchn](https://www.kitchn.io/blog/meta-marketing-api-q2-2026-update)
- **Platform Terms: service providers.**
  - A service provider that brings in another provider must bind it **in writing to the same requirements**.
  - Providers must stop processing and delete data when engagement ends.
  - Meta can request a list of Service Providers and Sub-Service Providers, with the types and volume of Platform Data shared and proof of written agreements, and can require the developer to stop using a provider.
  - Platform Data collected as a Tech Provider is governed by **Section 5.b**.
  — [Meta Platform Terms](https://developers.facebook.com/terms/dfc_platform_terms/); [Meta Platform Terms (index)](https://developers.facebook.com/terms)
- **Developer Policies.** Developers must make sure agreements with other entities do not conflict with Meta's terms. — [Meta Developer Policies](https://developers.facebook.com/devpolicy/)
- **AI training on Platform Data.** Meta's platform policy reportedly restricts third-party developers from using platform data to train AI models without authorization. Secondary sources only; verbatim text not obtained. — [Platform Policy Wiki: train_ai_models](https://www.platform-policy-wiki.com/concepts/train_ai_models/); [ConductAtlas AI-training comparison 2026](https://conductatlas.com/blog/ai-training-data-provisions-comparison-2026/)
- **WhatsApp Tech Provider Terms.** No use of Applicable Platform Data for the developer's own purposes and no disclosure to third parties except as expressly allowed. The developer must represent it has authority from each customer. — [Meta Tech Provider Terms](https://www.facebook.com/legal/BM-tech-provider-terms)
- **Meta's own business terms (Oct 2025).** The word "train" was removed between 15 and 20 Oct 2025. Commentators disagree on whether this is substantive. This concerns what *Meta* does with business data, not developers. — [Snopes](https://www.snopes.com/fact-check/meta-business-accounts-ai-scraping/)

### Inferences
- **Version maintenance.** Plan to upgrade Marketing API versions at least annually, realistically every release, given about 12-month Marketing API lifetimes. Expect cross-version breaking changes (e.g., the v26 changes applied to all versions on 27 Oct 2026). Pin versions explicitly and monitor the changelog.
- **Sending Meta data to OpenAI or Anthropic.** This appears *permissible as a service-provider/processing relationship*, not as onward sharing. Conditions (inference):
  - **Training:** the LLM vendor must contractually not train on the data (zero data retention / no training, e.g., enterprise API terms).
  - **Contracts:** written terms binding the vendor to Meta-equivalent restrictions.
  - **Records:** a list of sub-processors ready for Meta audits.
  - **Minimization:** send the minimum needed, and never raw customer-list PII (hash first).
  - **Fine-tuning:** using customers' Meta data (insights, ad creative, WhatsApp conversations) to fine-tune Marta's own models is a high-risk area and should be avoided or explicitly authorized.
- **Token handling.**
  - Prefer business-integration system-user tokens obtained via Facebook Login for Business / Embedded Signup.
  - Encrypt tokens at rest.
  - Never automate the Ads Manager UI or reuse personal session tokens. This is exactly what the 2026 restriction reports point to.
- **Pace the agent's writes.** Limit budget changes per hour, queue mutations, and use the Insights async API for heavy reporting. This avoids both throttling and "risk system" flags.

### Gaps
- Verbatim Platform Terms text on AI and LLM processing and on Section 5.b (Tech Provider) could not be retrieved. No official Meta FAQ was found that explicitly addresses sending Platform Data to third-party LLM APIs.
- Exact Insights API throttling rules for 2026 (headers, async job limits) and webhook topics for ads (e.g., ad-account and campaign status) were not retrieved.
- v27.0 release date (4 Nov 2026) comes from a single source and is unconfirmed.

---

## 7. Risk register (synthesis for Marta)

### Takeaway
The highest-impact risks are:
1. Commoditization by Meta's own free agentic tools and official MCP server.
2. A failed or partial App Review for ads_management / Full Access, which blocks the core product.
3. WhatsApp AI-Provider policy ambiguity for any Marta-owned conversational WhatsApp interface.
4. Account restrictions caused by agent behaviour.
5. Rising WhatsApp costs.

All are mitigable except Meta's strategic direction, which can only be hedged through differentiation and multi-platform coverage.

### Cited Findings
- **Commoditization:** the official MCP server and agentic assistant. — [Digiday](https://digiday.com/marketing/meta-opens-its-ad-ecosystem-to-third-party-ai-tools/); [adgully](https://www.adgully.com/post/21851/meta-unveils-agentic-ai-capabilities-in-ads-manager-to-automate-campaign-execution); [Meta SEC FWP](https://www.sec.gov/Archives/edgar/data/0001326801/000119312526431036/d116268dfwp.htm)
- **Access gating:** Advanced/Full Access and Business Verification. — [overads.io](https://overads.io/blog/read-only-ad-access); [Meta rate-limiting doc](https://developers.facebook.com/documentation/ads-commerce/marketing-api/overview/rate-limiting)
- **WhatsApp AI clause.** — [dig.watch](https://dig.watch/updates/meta-changes-whatsapp-terms-to-block-third-party-ai-assistants); [TechCrunch](https://techcrunch.com/2025/10/18/whatssapp-changes-its-terms-to-bar-general-purpose-chatbots-from-its-platform/)
- **Account restrictions:** reported for unofficial AI connectors. — [hyperfx.ai](https://www.hyperfx.ai/blog/will-connecting-claude-to-meta-ads-ban-account-2026)
- **Termination right:** Tech Provider Terms allow termination on 30 days' notice without cause. — [Meta Tech Provider Terms](https://www.facebook.com/legal/BM-tech-provider-terms)

### Inferences
Risk register (likelihood and impact are analyst judgments based on the findings above):

| # | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| 1 | Meta's free agentic Ads Manager assistant, official Ads MCP server and Advantage+ automation commoditize Marta's core "AI runs your Meta ads" value | **High** (already shipped Apr–Oct 2026) | **High** | Differentiate on Hebrew/Israel SMB context, cross-channel (Meta + Google + TikTok + WhatsApp + CRM), outcome guarantees and service, approvals and guardrails, multi-client/agency workflows. Consider building on Meta's MCP as a tool rather than competing with it. Avoid positioning as a "thin wrapper". |
| 2 | App Review declines ads_management Advanced Access, or Full Access isn't reached (500/1,500-call threshold, <15% errors) → cannot manage client accounts at scale | **Medium** | **Critical** (blocks the product) | Finish Business Verification first. Build a real client-onboarding flow (Facebook Login for Business) and show it in the screencast. Request minimal permissions, staged. Generate qualifying call volume on pilot accounts. Budget 4–12 weeks and multiple review rounds. |
| 3 | WhatsApp "AI Provider" clause applied to Marta's own conversational assistant on WhatsApp (sole-discretion wording) → WABA/app disabled | **Medium** (if Marta offers a chat-with-Marta WhatsApp number); **Low** (if WhatsApp is used only for customers' templates and business-specific bots) | **High** | Keep Marta's main UI off WhatsApp. Use WhatsApp only for utility notifications and approvals to owners and for customers' scoped business bots. Document the "incidental/ancillary" AI use. Note that EU relief doesn't cover Israel. |
| 4 | Ad-account or app restrictions triggered by agent behaviour (high-frequency budget edits, bulk audience churn, token misuse) or by unofficial access patterns | **Medium** | **High** (customer harm, churn, reputational) | Use only official APIs, system-user/business tokens and Meta's MCP. Throttle writes. Create new ads paused or as drafts. Require human approval for spend increases. Use Meta's rate-limit headers and backoff. |
| 5 | Sensitive-data restrictions disable customers' custom audiences, lookalikes, custom conversions or Pixel/CAPI events (health/financial implication; Special Ad Categories) | **Medium-High** (for health, finance, insurance or real-estate SMBs) | **Medium** | Add a classifier and guardrails on audience, event and conversion names. Detect and auto-set Special Ad Categories. Hash PII client-side (SHA-256 normalized). Get advertiser warranties on list consent. |
| 6 | WhatsApp cost inflation: per-message marketing (~$0.041 in Israel), new service/utility-in-window charges (Oct/Nov 2026), quarterly price changes | **High** (already happening) | **Medium** | Pass Meta fees through transparently. Use the max-price feature (beta) and MM API optimization. Prefer free entry points (Click-to-WhatsApp ads) and utility templates where legitimate. Build a cost dashboard. |
| 7 | WhatsApp delivery limits: 250-user starting tier per portfolio, per-user marketing frequency caps, quality-rating drops, template rejections | **High** | **Medium** | Verify each customer's business early. Warm up tiers. Enforce opt-in capture. Segment and personalize to keep quality high. Pre-check templates with AI for category and policy fit. |
| 8 | API version churn and breaking changes (Marketing API versions live ~12 months; cross-version changes like 27 Oct 2026; metric retirements) | **High** (certain) | **Medium** | Pin versions. Automate changelog monitoring. Run a quarterly upgrade sprint. Keep an abstraction layer. Add contract tests against the sandbox. |
| 9 | Data-use non-compliance: sending Platform Data or WhatsApp content to third-party LLMs without proper sub-processor terms; training on Meta data | **Medium** | **High** (app termination, legal) | Use zero-retention / no-training enterprise LLM terms. Keep written sub-processor agreements mirroring Meta's terms and a sub-processor register for Meta audits. Never fine-tune on customers' Meta data without authorization. Run the annual Data Use Checkup. |
| 10 | Unilateral termination or policy change: Tech Provider Terms terminable on 30 days' notice; history of ~90-day API removals (Groups API 2024, IG Basic Display 2024) | **Low-Medium** (per year) | **Critical** | Multi-platform roadmap so Meta is not 100% of value. Contractual and product contingency plans. Keep a BSP partner as a WhatsApp fallback. Join Meta partner programs for early notice. |
| 11 | Meta-Business-Partner / BSP dependency for billing (Tech Provider without a credit line → each SMB must add a card to its WABA) | **High** | **Low-Medium** (onboarding friction) | Multi-Partner Solution with an Israeli-friendly BSP, or a guided card-setup flow inside Embedded Signup v4 (v2/v3 deprecated 15 Oct 2026). |
| 12 | Regulatory and antitrust shifts (EU interim measures on WhatsApp AI access; possible appeals) change the rules mid-build | **Medium** | **Low** for Israel market (EEA-only) | Monitor EU case AT.41034 and any Israeli Competition Authority interest. Design for the strictest current policy. |

### Gaps
- Likelihood ratings are qualitative analyst judgments. No base-rate data was found on App Review approval rates or on frequency of account restrictions for AI tools.
- Official Meta pages (App Review, Platform Terms full text, WhatsApp Business Solution Terms, MCP terms, Israel rate card) need direct verification. developers.facebook.com and techcrunch.com were not fetchable in this research session.
