# Israeli Competitive Landscape for "Marta" (Hebrew-first AI agent over Meta Ads, Audiences and WhatsApp)

> Method note for the report writer: research date 17 Nov 2026. Direct page fetching (WebFetch) was blocked by the session's network allowlist for every domain tried (gambot.co.il, spike.co.il, otomation.io, calcalist.co.il, glassix.com, miaben.co.il). All findings below come from web-search result pages and their snippets/summaries, not from full-page reads. Where a fact rests on a single snippet, it is flagged "(single-snippet)". Many of the most detailed Israeli WhatsApp price comparisons are written by a vendor (Achiya Automation / Achiya Cohen), which is flagged wherever used. USD to ILS conversions marked "≈" assume roughly ₪3.6 per US$ and are my own arithmetic, not sourced.

## Q1. Israeli WhatsApp Business API / bulk messaging / chatbot / inbox products (pricing, targets, customer counts)

### Takeaway
The Israeli WhatsApp layer is crowded: I found 20+ Israeli or Israel-focused vendors, from official Meta BSPs and Tech Providers (InforU, Micropay, Soprano/Unicell, inwise, Glassix) through SMB bot and broadcast platforms (Gambot, Botomati, Hadavar, Taskey, Signals) to enterprise AI contact centers (CommBox, Glassix) and email/SMS suites that added WhatsApp as a paid extra (Smoove, ActiveTrail). Published SMB entry prices cluster around ₪70–₪650 a month plus Meta's per-message fees. None of them manages Meta ads or audiences.

### Cited Findings

**Meta's own per-message cost in Israel (the floor under every vendor price)**
- Meta's Israel rate card, effective 1 July 2026: US$0.0353 per marketing message and US$0.0053 per utility message, as cited by Spike — [Spike blog](https://www.spike.co.il/blog/whatsapp-business-pricing)
- Rough shekel estimate: a marketing message costs about 12–15 agorot, a utility message about 5–6 agorot, and a service message inside the 24-hour window is free — [Otomation](https://www.otomation.io/blog/whatsapp-api-cost-israel/)
- Conflict on service-message charges. Achiya says that from 1 Oct 2026 every service message above the free quota costs US$0.0053 in Israel — [Achiya Automation](https://achiya-automation.com/blog/whatsapp-api-pricing-october-2026/). Ariko says the first 1,000 replies a month per number are free and each reply after that costs US$0.0053 — [Ariko](https://ariko.ai/en/guide/whatsapp-bot-cost). Spike says service messages were completely free until Sept 2026 — [Spike](https://www.spike.co.il/blog/whatsapp-business-pricing). Treat the dates as unconfirmed.
- Meta moved from per-conversation to per-message billing (one source dates this to 1 Jan 2026) — [Go4whatsup](https://www.go4whatsup.com/blog/whatsapp-api-pricing)
- Israeli anti-spam law: in 2020 the Supreme Court confirmed that WhatsApp messages fall under the same rules as SMS, so marketing messages need consent — [Achiya Cohen, ToI blog](https://blogs.timesofisrael.com/israels-whatsapp-bot-market-mapped/); InforU also notes Meta requires recipients' consent — [InforU broadcast lists](https://www.inforu.co.il/features/%D7%A8%D7%A9%D7%99%D7%9E%D7%AA-%D7%AA%D7%A4%D7%95%D7%A6%D7%94-%D7%91%D7%95%D7%95%D7%90%D7%98%D7%A1%D7%90%D7%A4/)

**Official BSPs and Meta Tech Providers based in Israel**
- **InforU (אינפורו)**: calls itself a Meta-authorized BSP serving "over 30,000 organizations" (self-reported, number of organizations overall rather than WhatsApp users). Offers WhatsApp API and WhatsApp broadcast lists. I found no public ILS price list — [InforU WhatsApp API](https://www.inforu.co.il/features/whatsapp-api/); [InforU WhatsApp Business](https://www.inforu.co.il/features/%D7%95%D7%95%D7%90%D7%98%D7%A1%D7%90%D7%A4-%D7%91%D7%99%D7%96%D7%A0%D7%A1/)
- **Micropay**: describes itself as a Meta Tech Provider offering WhatsApp Business through Meta's official API. Price not found — [Micropay](https://site.micropay.co.il/whatsapp.php)
- **Soprano (Unicell)**: "one platform, one API, all distribution channels". It says Israeli businesses must work through an official provider and covers business verification and template approval. Price not found — [Unicell/Soprano](https://unicell.co.il/%D7%A1%D7%95%D7%A4%D7%A8%D7%A0%D7%95/)
- **inwise**: WhatsApp marketing and operations for organizations via the official WhatsApp Business API with Meta-approved templates. Price not found — [inwise](https://www.inwise.co.il/%D7%95%D7%95%D7%90%D7%98%D7%A1%D7%90%D7%A4/)
- **Glassix**: Israeli, founded 2015 in Tel Aviv by Guy Shalom (CEO) and Yoad Rashty (CTO). An "AI-native autonomous contact center" with GPT-4 chatbots, a WhatsApp chatbot, WhatsApp Flows, broadcasts/bulk messaging and open APIs — [Built In](https://builtin.com/company/glassix); [CB Insights](https://www.cbinsights.com/company/glassix-1); [SourceForge](https://sourceforge.net/software/product/Glassix)
  - Pricing: from US$49 per user per month (≈₪175), with a free trial — [Capterra Israel](https://www.capterra.co.il/software/1052241/glassix). Achiya lists US$49–65 per user per month, "enterprise-oriented" — [Achiya comparison](https://achiya-automation.com/en/blog/whatsapp-bot-providers-israel-2026/). The ToI blog puts Glassix in the contact-center category at "thousands of shekels a month, priced per seat" — [ToI blog](https://blogs.timesofisrael.com/what-israeli-smbs-really-pay-for-automation/). Glassix's pricing page shows Starter and Growth tiers and a row reading "Region: Worldwide (except Israel)", which suggests Israeli pricing is handled separately (ambiguous) — [Glassix pricing](https://glassix.com/pricing)
  - WhatsApp numbers are not enabled by default because they require billing setup on Glassix's side — [Glassix docs](https://docs.glassix.com/docs/connecting-a-whatsapp-number-embedded-sign-up-guide)
  - Listed in Fireberry's solution catalog — [Fireberry catalog](https://www.fireberry.com/solution-catalog/glassix)
  - I found no customer count.
- **CommBox**: Israeli, founded 2013. An enterprise AI omnichannel customer-engagement platform with WhatsApp at its core, offered as cloud, isolated cloud or on-premise — [Built In](https://builtin.com/company/commbox); [CommBox](https://www.commbox.io/commbox-conversational-ai-for-virtual-agents-omnichannel-engagement-platform)
  - Named customers: Clalit (1,000 clinics and 4,000 agents on one WhatsApp number, 47% of requests automated); Clal Insurance (57% automated, 2,000+ agents); Pelephone (claimed 2x agent productivity). All figures are vendor-reported — [CommBox Pelephone](https://commbox.io/customers/pelephone); [Case study](https://www.casestudies.com/company/commbox/case-study/pelephone-telecom-boosts-agent-productivity-by-2x-with-lightning-fast-service-via-whatsapp); [CommBox autonomous enterprise](https://www.commbox.io/?p=2287)
  - Claims to control "the majority of the Israeli market" (self-published, unverified) — [CommBox](https://www.commbox.io/?p=2287)

**SMB WhatsApp bot and broadcast platforms (Israeli)**
- **Gambot** (gambot.co.il): an Israeli WhatsApp Business API platform for building bots, managing chats and sending campaigns — [Achiya comparison](https://achiya-automation.com/en/blog/whatsapp-bot-providers-israel-2026/)
  - Plans as of July 2026, before VAT: Growth ₪179/month (up to 1,000 broadcast messages), Pro ₪359 (up to 5,000), Business ₪645, Enterprise by quote. Extra blocks of 1,000 messages are priced separately — [Gambot price list](https://gambot.co.il/PriceList/); [Achiya](https://achiya-automation.com/en/blog/whatsapp-bot-providers-israel-2026/)
  - Managed one-time broadcast: ₪2.00 per message for up to 1,000 messages, falling to ₪0.90 at 20,001+, Meta fees included, 500-message minimum — [Gambot managed broadcast](https://gambot.co.il/PriceList/ManagedBroadcast/)
  - Custom development ₪555/hour plus VAT; consultation call ₪400 plus VAT — [Achiya](https://achiya-automation.com/en/blog/whatsapp-bot-providers-israel-2026/)
  - Conflict: a Danai comparison saw USD pricing that varied by location, with Growth shown at US$59/month billed annually when viewed from Israel — [Danai](https://danaiapp.org/en/blog/whatsapp-bot-comparison-israel)
- **Botomati**: free up to 500 messages a month — [Achiya](https://achiya-automation.com/en/blog/whatsapp-bot-providers-israel-2026/)
- **WBsender**: bulk messaging only, "not a real conversational bot" (per a competitor) — [Achiya](https://achiya-automation.com/en/blog/whatsapp-bot-providers-israel-2026/)
- **Signals**: three products. JAKO is a cloud system "connected directly to Meta for AI bots and marketing campaigns"; Push is desktop software for campaigns and basic bots; MaxBot is multichannel (WhatsApp, email, SMS, Telegram, Instagram, Viber). No price found — [Achiya automation companies 2026](https://achiya-automation.com/en/blog/automation-companies-israel-2026/)
- **Automatix (אוטומטיקס)**: Rehovot, founded 2024. Automations, "digital employees" and WhatsApp bots; managed service from ₪500/month — [B144 listing](https://www.b144.co.il/b144_sip/401D0D1A4370655D411C0C1B43/); [Achiya](https://achiya-automation.com/en/blog/automation-companies-israel-2026/)
- **Hadavar (הדוור)**: WhatsApp API package from ₪90 plus VAT a month, with a 7-day free trial — [Hadavar](https://www.hadavar.co.il/product/%D7%A9%D7%9C%D7%99%D7%97%D7%AA-%D7%95%D7%95%D7%98%D7%A1%D7%90%D7%A4-%D7%9E%D7%90%D7%9C%D7%9E%D7%A0%D7%98%D7%95%D7%A8-%D7%95%D7%95%D7%A7%D7%95%D7%9E%D7%A8%D7%A1-%D7%95%D7%90%D7%A4%D7%9C%D7%99%D7%A7/)
- **Taskey**: WhatsApp module at ₪70 per number per month, connected through a third-party API provider — [Taskey](https://taskey.co.il/%D7%9E%D7%95%D7%93%D7%95%D7%9C-%D7%95%D7%95%D7%90%D7%98%D7%A1%D7%90%D7%A4-api/)
- **Ariko.ai**: plans at US$99 / $149 / $199 / $399 a month before VAT (≈₪355–1,435), Meta message charges included — [Ariko](https://ariko.ai/en/guide/whatsapp-bot-cost)
- **DanAI**: a chatbot that supports Hebrew and English. Integrations include WhatsApp and Facebook Business Suite. No ILS price found — [Capterra](https://www.capterra.ca/software/1107748/DanAI)
- **Achiya Automation** (custom studio, Ashdod): custom build owned outright for a one-time ₪3,500–12,000 plus ₪100–300/month hosting — [ToI blog](https://blogs.timesofisrael.com/israels-whatsapp-bot-market-mapped/)
- **019 (019SMS)**: SMS API, plus a "019 WhatsApp" app on Make that needs an active 019 account and API token. No price found — [019 docs](https://docs.019sms.co.il); [Make 019 WhatsApp](https://apps.make.com/whatsapp-019)
- **Green-API** (Hebrew site): an unofficial WhatsApp gateway. Unofficial QR-based tools carry a risk of the number being blocked — [Green-API he](https://green-api.com/he); [Wiseflow](https://wiseflow.co.il/whatsapp-api/)
- **Spike** (spike.co.il) and **Otomation** (otomation.io) publish Israeli WhatsApp pricing guides and appear to be WhatsApp tool vendors. Their own products and prices could not be verified because the pages were not fetchable — [Spike](https://www.spike.co.il/blog/whatsapp-business-pricing); [Otomation](https://www.otomation.io/blog/whatsapp-api-cost-israel/)

**Israeli email/SMS marketing suites with WhatsApp**
- **Smoove**: Israeli (Petah Tikva), founded 2013 by Yonatan Shachar; about 26 employees (aggregator); no funding data — [Startupim](https://startupim.com/company/smoove); [Bouncewatch](https://bouncewatch.com/company/smooveio). WhatsApp for marketing, service and operational messages — [Smoove WhatsApp](https://www.smoove.io/whatsapp-for-business/). The pricing page lists WhatsApp as a paid extra ("בתשלום נוסף"); the amount was not visible — [Smoove pricing](https://www.smoove.io/pricing/)
- **ActiveTrail**: Israeli email/SMS/automation platform with a "how to choose a WhatsApp marketing system" guide. No WhatsApp price found. SMS packages run from US$41 for 500 to US$344 for 5,000 (≈₪150–1,240; may be outdated). 30-day free trial — [ActiveTrail blog](https://www.activetrail.com/?p=64768); [Top10 review](https://www.top10.com/email-marketing/reviews/activetrail); [ActiveTrail llms.txt](https://www.activetrail.com/llms.txt)
- **Responder (רב מסר)**: Hebrew-only email autoresponder. The only WhatsApp links found are third-party Zapier zaps that send a WhatsApp message on a new subscriber — [Zapier](https://zapier.com/apps/responder/integrations/whatsapp-notifications/1659211/send-whatsapp-notifications-messages-when-new-subscribers-are-added-in-responder-rb-msr)
- **Pulseem (פולסים)**: no evidence of a WhatsApp API product found in search; the only page returned covered call tracking and segmentation — [Pulseem](https://site.pulseem.co.il/?p=3912)

**Israeli CRMs that touch WhatsApp and Meta leads**
- **Fireberry (formerly Powerlink)**: Israeli CRM with a WhatsApp add-on for sending messages from the CRM — [Fireberry WhatsApp](https://www.fireberry.com/features/whatsapp). It imports Facebook leads in real time — [Fireberry integrations](https://fireberry.com/help/integrations). Partner app "Pingmee AI" adds a WhatsApp/Facebook/Instagram omnichannel inbox — [Fireberry catalog](https://www.fireberry.com/solution-catalog/pingmee-ai-omnichannel-platform-for-fireberry). Pricing from US$25/month, Standard US$35 per user per month (≈₪90–125), with a three-seat minimum on Standard; both figures may be outdated — [Software Advice](https://www.softwareadvice.com/business-management/powerlink-profile/); [Prospeo](https://prospeo.io/s/fireberry-pricing-reviews-pros-and-cons)
- **monday.com CRM** (Israeli): Facebook Lead Ads reach monday through Zapier or Make templates, and those templates can also trigger WhatsApp messages — [Zapier](https://zapier.com/apps/facebook-lead-ads/integrations/monday); [Make](https://make.com/en/integrations/facebook-lead-ads/monday). A community post says monday has a native WhatsApp integration (unverified) — [monday community](https://community.monday.com/t/whatsapp-crm-integration/79679)
- **Pushleads**: a CRM connecting WhatsApp, email, SMS and ads. Listed on Capterra Israel with a free version; integrates with Facebook Business Suite, Google Ads and TikTok. Israeli origin not verified — [Capterra IL](https://www.capterra.co.il/software/1112384/Pushleads)
- **Lead.im (Leadim)**: lead platform for agencies and lead generators, with mail/SMS, ad-system connections, lead distribution, CRM and call-center features. No WhatsApp mention, no price — [SourceForge](https://sourceforge.net/software/product/Lead.im)

**Market price bands (vendor-authored estimates)**
- 2026 Israeli list prices: ₪79–299/month for a basic menu bot, ₪300–999 with CRM connectors, ₪1,000–2,500/month for a free-language AI agent — [Achiya comparison](https://achiya-automation.com/en/blog/whatsapp-bot-providers-israel-2026/)
- SaaS route: ₪179–645/month plus a ₪500–1,500 setup fee — [Achiya ToI](https://blogs.timesofisrael.com/israels-whatsapp-bot-market-mapped/)
- Published starting prices range from limited free plans to about ₪500 a month, mostly before VAT — [Danai](https://danaiapp.org/en/blog/whatsapp-bot-comparison-israel)
- An SMB with about 200 conversations a month typically pays ₪200–500/month for Cloud API infrastructure (fees plus provider), plus the automation subscription — [Autias guide](https://autias.pages.dev/en/blog/whatsapp-cloud-api-guide/)

### Inferences
- WhatsApp sending is a commodity in Israel. Many players have official BSP or Tech Provider status, prices are published, and SMB entry points sit at ₪70–₪360 a month. Marta cannot win on WhatsApp plumbing; its edge has to be the conversational, cross-channel layer.
- Vendors fall into three groups: pipes (BSPs, SMS carriers), SMB bot/broadcast builders (Gambot, Botomati, Hadavar), and enterprise AI contact centers (CommBox, Glassix). All of them treat WhatsApp as a messaging or service channel. None treats it as one leg of a paid-ads funnel together with audiences.
- InforU's "30,000+ organizations" and CommBox's "majority of Israeli market" claims suggest the established players already hold the enterprise and mid-market WhatsApp relationships.

### Gaps
- No public ILS prices were found for InforU, inwise, Micropay, Soprano, Smoove (WhatsApp add-on), ActiveTrail (WhatsApp), Signals or CommBox. They are probably sales-led.
- Customer counts for Glassix, Gambot, Smoove, ActiveTrail and Responder were not found.
- I could not reach the Meta Business Partner Directory or WhatsApp BSP list filtered to Israel (page fetching blocked), so official partner status rests on vendors' own claims.
- "Botit" and "SMS4Free" returned no relevant results.
- Spike and Otomation are probably vendors, but their products were not verified.

## Q2. Israeli products that help SMBs run Facebook/Instagram ads (self-serve, lead sync, AI agents for Meta ads)

### Takeaway
Israel has some globally relevant Meta-ads AI companies, but they are English-language and aimed at e-commerce or enterprise: Madgicx (SMB/e-commerce), AdgeAI (enterprise, acquired by Publicis in 2026), AdScale, StoreYa, and Trapica (now defunct). There is also a thin layer of small Hebrew-first SMB tools and agency-built "AI systems" (Kampi, Ultrads, ADAM by מיה ובן, MIA by קפטן דיגיטל, appy OS) that are mostly unverified single-site claims. The biggest new threat is Meta itself: its official Ads MCP/AI Connectors (April 2026) let Claude and ChatGPT run Meta ads in natural language, including in Hebrew.

### Cited Findings

**Israeli AI tools for Meta ads (global products)**
- **Madgicx**: Israeli, founded 2018 (one profile says 2017), headquartered in Herzliya/Tel Aviv, founded by Yahav Hartman (CEO) and Idan Beker (CTO). Described as a "super app for Meta ads" for e-commerce, with predictive AI, an AI Ad Generator and AI ROI tools. Headcount estimates range from about 46 to 51–200 — [CB Insights](https://www.cbinsights.com/company/madgicx); [Startupim](https://startupim.com/company/madgicx); [StartupHub](https://www.startuphub.ai/startups/madgicx)
  - Pricing: a single "Madgicx Pro" plan priced by ad-spend bracket (seven brackets from under $1K to $30K+). Entry price is cited at US$44–99/month (≈₪160–355), Tracking add-on US$49/month, 7-day trial. "AI Marketer" is included in the plan — [Toolradar](https://toolradar.com/tools/madgicx/pricing); [Ryze](https://www.get-ryze.ai/blog/madgicx-pricing-2026); [Superscale review](https://superscale.ai/alternatives/madgicx/review)
  - I found no evidence of a Hebrew UI or Israeli-SMB focus.
- **AdgeAI**: Israeli and bootstrapped. Builds autonomous AI agents for marketing and growth teams in large organizations, integrating with Salesforce and Google Ads. Acquired by Publicis Groupe in March 2026, about US$100M per Calcalist (other outlets say undisclosed). Founders Eyal and Asaf Ben Shalom. It was in Meta's AI accelerator in Israel; past clients include P&G, Meta and Tula — [Calcalistech](https://www.calcalistech.com/ctechnews/article/r1wr00eto11x); [Marketing Dive](https://www.marketingdive.com/news/publicis-acquires-adgeai-to-sift-quality-creative-from-content-glut/814675/); [Calcalist he](https://www.calcalist.co.il/calcalistech/article/bjjmexfj11g). It is enterprise-focused and does not serve SMBs.
- **AdScale**: based in Yokneam, Israel. A fully automated AI ad platform for Facebook, Instagram and Google aimed at e-commerce. Shopify app from US$149–169/month (≈₪535–610). Founding date conflicts, and CB Insights marks it "Dead" while its Shopify app looks active — [Startupim](https://startupim.com/company/adscale); [CB Insights](https://www.cbinsights.com/company/adscale/); [Shopify app (he)](https://apps.shopify.com/adscale?locale=he)
- **StoreYa (Traffic Booster)**: AI-run Google, Shopping, Facebook and Instagram campaigns for small online stores. Basic US$120/month with ad budget included; Pro US$1,000/month adds Facebook/YouTube ads (≈₪430–3,600). Israeli origin was not confirmed in these results, and I found no Hebrew or Israel-specific offering — [Shopify](https://apps.shopify.com/traffic-booster); [BigCommerce](https://bigcommerce.com/apps/traffic-booster)
- **Trapica**: Tel Aviv, founded 2017 (Michael Teitelman, Yoav Melamed). AI ad automation for Facebook, Instagram and Google. Acquired; no longer a standalone product — [theatdb](https://theatdb.com/companies/trapica)
- **Albert.ai**: autonomous advertising for brands with US$100k+ annual budgets, custom pricing. Israeli origin rests on a low-reliability aggregator — [Madgicx compare](https://madgicx.com/compare/adscale-vs-albert-ai); [aitoolsonar](https://aitoolsonar.pages.dev/tools/albert-ai)
- **Marketeam.ai**: Tel Aviv. An "agentic Integrated Marketing Environment" with named agents (Ella for social media, aimed at SMBs; Maya, Jane, Daniel). US$3M seed in Jan 2025, US$5M total. A third-party directory says it connects to Meta Ads and Google Ads (unverified) — [PR Newswire](https://prnewswire.com/news-releases/marketeamai-launches-ella-the-autonomous-ai-social-media-marketing-agent-for-smbs-marking-the-first-step-in-marketeamais-ambitious-rollout-of-specialized-ai-marketing-agents-302105518.html); [Israel Innovation Authority](https://innovationisrael.org.il/en/importWinner/516425782); [ToolMage](https://www.toolmage.com/zh-hans/tool/marketeamai/). Mako describes it as making, scheduling and publishing social content with user approval, aimed at SMBs, so content rather than ad-budget management — [Mako](https://www.mako.co.il/nexter-news/Article-ad252bedf1f0591026.htm)
- Other Israeli ad-tech raises in 2026 are not Meta-SMB tools. Velocity (US$27M seed) places ads inside AI apps; enso (US$15M) works on AI-search visibility — [Techmeme/Axios](https://www.techmeme.com/260708/p18); [Ynetnews](https://www.ynetnews.com/business/article/h1fs0ra5gg)

**Wix (Israeli, Hebrew UI)**
- "Facebook & Instagram Ads with Wix" is still documented, including in Hebrew. It lets you create a campaign from the site dashboard, sets up a new Meta Ads account for you, and Wix's AI/"smart algorithm" adjusts the ads — [Wix he FAQ](https://support.wix.com/he/article/facebook-ads-%D7%A9%D7%90%D7%9C%D7%95%D7%AA-%D7%A0%D7%A4%D7%95%D7%A6%D7%95%D7%AA); [Wix overview](https://support.wix.com/en/article/facebook-instagram-ads-an-overview); [Wix smart algorithm](https://support.wix.com/en/article/about-wixs-smart-algorithm)
- A third-party guide claims a 15% Wix service fee on native Meta ads, versus 0% in Ads Manager (unverified) — [dev.to guide](https://dev.to/getkoro_app/2026-guide-high-performance-facebook-ads-for-wix-stores-dkb)
- The Wix AI assistant also builds email campaigns (Hebrew help article) — [Wix he](https://support.wix.com/he/article/email-marketing-%D7%99%D7%A6%D7%99%D7%A8%D7%AA-%D7%A7%D7%9E%D7%A4%D7%99%D7%99%D7%9F-%D7%9E%D7%99%D7%99%D7%9C%D7%99%D7%9D-%D7%91%D7%A2%D7%96%D7%A8%D7%AA-ai)

**Hebrew-first SMB "AI campaign" tools and agency systems (mostly single-snippet, unverified)**
- **Kampi (kampi.co.il)**: Israeli platform that plans, creates and publishes Facebook/Instagram content. Basic ₪149/month (no paid campaigns); Pro from ₪298/month including paid-campaign management (single-snippet; a second search could not find it) — [Kampi](https://www.kampi.co.il/)
- **Ultrads (ultrads.ai)**: Hebrew platform that generates and publishes Facebook/Instagram ads (and Google), monthly subscription with no commitment. Price not shown (single-snippet) — [Ultrads](https://ultrads.ai/)
- **ADAM by מיה ובן (miaben.co.il)**: an "AI agent" for marketing a business on autopilot, controlled from mobile, with ROI calculation, lead management and budget control. ₪290/month (single-snippet; page not fetchable) — [miaben ADAM](https://miaben.co.il/ai-adam/)
- **MIA by קפטן דיגיטל (Captain Digital)**: an AI system that manages, writes, designs and publishes on Facebook and Instagram. Price not found — [Captain Digital](https://captaindigital.co.il/social-media)
- **appy OS (Appy Creative Digital)**: a digital agency with its own AI system connected to site, social and campaigns that shifts budget away from waste. Agency service, not self-serve — [appy](https://www.appy.co.il/)
- **WebitNow AI** (agency, "leads on autopilot") — [WebitNow](https://webitnow.ai/); **expert-digital** "AI agent for campaign analysis" — [expert-digital](https://www.expert-digital.co.il/ai-campaign-optimization/)

**Meta itself as the direct substitute**
- Meta launched official "Ads AI Connectors" on 29 April 2026: a beta HTTP MCP server and a CLI with 29 tools covering ad accounts, catalogs, datasets and insights. With it, Claude or ChatGPT can create ads, edit ad sets and change budgets in natural language. Free, OAuth-based; write actions reportedly need approval, though another source warns there is no undo or draft mode — [PPC Land](https://ppc.land/meta-opens-its-ad-system-to-claude-and-chatgpt-with-new-ai-connectors/); [Pillitteri guide](https://pasqualepillitteri.it/en/news/1707/official-meta-ads-mcp-claude-29-tools-2026); [mcp.directory](https://mcp.directory/blog/meta-ads-cli-mcp)
- A Hebrew blog markets this to Israeli SMBs: "you can now talk to your campaigns in Hebrew" via Claude Pro at about ₪80/month (blog claim) — [bestai.co.il](https://bestai.co.il/articles/meta-mcp-claude-desktop-small-business-2026)
- Third-party Meta Ads MCP servers (Ryze AI, PaidSync, Adspirer, Markifact) also exist — [mcpservers Ryze](https://mcpservers.org/servers/www-get-ryze-ai-meta-ads-mcp); [Markifact PR](https://www.wboc.com/online_features/press_releases/markifact-launches-meta-ads-mcp-for-claude-chatgpt-and-ai-agents/article_8a6ba33f-c364-5470-9f3a-ef3fcc1db542.html)
- In early 2026 Meta merged its manual and AI campaign flows into one interface. At Cannes 2026 it previewed an end-to-end system that builds creative, targeting and budget from a product URL — [Adwave (via search summary)](https://adwave.com/resources/facebook-advertising-for-small-business)
- **Meta Business Agent** (June 2026): an AI agent businesses can place in WhatsApp, Messenger and Instagram that answers questions, recommends catalog products, books appointments and qualifies leads. Setup and initial use are free for now — [Gadgety (he)](https://www.gadgety.co.il/363382/meta-business-agent-launched/); [The Star](https://www.thestar.com.my/tech/tech-news/2026/06/03/meta-enters-enterprise-ai-race-with-new-business-agent)
- Meta AI launched in Israel with native Hebrew in WhatsApp in early July 2026 — [Ynetnews](https://www.ynetnews.com/tech-and-digital/article/rk008bxwxge)
- Calcalist covered Meta's Israeli office pitching its AI ad tools to Israeli advertisers — [Calcalist](https://www.calcalist.co.il/article/synqqbbrjg)

### Inferences
- Israel produced the leading AI tool for Meta ads (Madgicx), but it is English-language, built for e-commerce media buyers, and has no WhatsApp leg. AdgeAI is now part of Publicis and serves enterprises. Neither competes for a Hebrew-speaking local SMB.
- The Hebrew-first SMB tools (Kampi, Ultrads, ADAM) look small and content- or ad-creation-centric. I found no evidence that any of them builds custom or lookalike audiences, manages Pixel/CAPI, or sends WhatsApp.
- The biggest risk is horizontal. Meta's free official MCP plus any Hebrew-capable LLM (Claude, ChatGPT) already gives a technical SMB a conversational Hebrew interface to Ads Manager. Meta's Business Agent and Hebrew Meta AI cover the WhatsApp conversation side for free. Marta's defensibility therefore rests on non-expert UX, guardrails (approval, undo, budget caps that the MCP reportedly lacks), local playbooks, and joining ads, audiences and WhatsApp into one flow.

### Gaps
- Kampi, Ultrads and ADAM could not be verified beyond one search snippet each. Pricing, feature depth (audiences, Pixel) and customer counts are unknown.
- I could not confirm whether Madgicx offers Hebrew UI or support, or how many Israeli customers it has.
- StoreYa's and Albert's Israeli origin was not confirmed by the sources retrieved.
- Meta's official MCP endpoint differs between sources (mcp.facebook.com/ads vs mcp.meta.com/ads/<business-id>), and its Hebrew behaviour has not been verified.

## Q3. Israeli-founded global players: which are Israeli, and do they serve Israeli SMBs in Hebrew?

### Takeaway
Madgicx, AdgeAI, AdScale, Trapica (defunct), Marketeam.ai, Glassix, CommBox, Wix, monday.com and Fireberry are Israeli. Only Wix, Fireberry, CommBox and (probably) Glassix clearly serve Israeli customers in Hebrew. AdCreative.ai has a Hebrew-localized site, but I did not establish its origin.

### Cited Findings
- Madgicx: Israeli (Herzliya/Tel Aviv), English product aimed at global e-commerce — [CB Insights](https://www.cbinsights.com/company/madgicx); [Startupim](https://startupim.com/company/madgicx)
- AdgeAI: Israeli, enterprise, acquired by Publicis 2026 — [Calcalistech](https://www.calcalistech.com/ctechnews/article/r1wr00eto11x)
- AdScale: Yokneam, Israel; e-commerce; Shopify app also listed in Hebrew locale — [Startupim](https://startupim.com/company/adscale); [Shopify he](https://apps.shopify.com/adscale?locale=he)
- Trapica: Tel Aviv, absorbed after acquisition — [theatdb](https://theatdb.com/companies/trapica)
- Marketeam.ai: Tel Aviv — [Israel Innovation Authority](https://innovationisrael.org.il/en/importWinner/516425782)
- Glassix: Tel Aviv, 2015 — [Built In](https://builtin.com/company/glassix). Listed in the Israeli Fireberry catalog and on Capterra Israel — [Fireberry](https://www.fireberry.com/solution-catalog/glassix); [Capterra IL](https://www.capterra.co.il/software/1052241/glassix)
- CommBox: Israeli, 2013, serves Clalit, Clal and Pelephone — [Built In](https://builtin.com/company/commbox); [CommBox Pelephone](https://commbox.io/customers/pelephone)
- Wix: Hebrew help center for Facebook & Instagram Ads — [Wix he](https://support.wix.com/he/article/facebook-instagram-ads-סקירה-כללית)
- AdCreative.ai runs a Hebrew-language site (he.adcreative.ai) — [AdCreative he](https://he.adcreative.ai/ai-advertising)
- Global non-Israeli comparison point: Mega (Brooklyn) raised US$11.5M in March 2026 for AI agents that replace the local marketing agency for SMBs (ads, SEO, websites) — [Forbes](https://www.forbes.com/sites/charliefink/2026/03/09/ai-agents-take-aim-at-the-local-marketing-agency-as-mega-raises-115-million/)

### Inferences
- Israel's strong Meta-ads AI companies sell abroad and in English. The Hebrew-speaking SMB is served mainly by Wix's built-in ads (a website add-on with a limited "boost" model), by WhatsApp vendors, and by agencies. This supports a Hebrew-first niche.
- Mega shows that "AI agent replaces the agency for SMBs" is a fundable thesis globally. No Israeli equivalent was found.

### Gaps
- Origins of AdCreative.ai, StoreYa and Albert were not confirmed here. (Lemonade, Taboola and Outbrain are not relevant, as the brief notes.)
- I did not check whether monday.com offers native Meta ads management (it appears to offer only lead sync through Zapier or Make).
- Hebrew support in Madgicx and Marketeam is unknown.

## Q4. Local service substitutes: agency and freelancer pricing in Israel (Meta campaign management and WhatsApp services)

### Takeaway
The human alternative Marta competes with costs roughly ₪1,500–₪3,500 a month for a freelancer and ₪2,000–₪5,000+ for a local agency (up to ₪10,000–20,000+ for large agencies), or 10–25% of ad spend, before VAT and before media budget. WhatsApp bots cost ₪79–₪2,500 a month as SaaS or ₪3,500–₪12,000 one-time as a custom build.

### Cited Findings
- Israeli marketing blogs give the following bands. The search summary did not map each figure to a specific URL, so treat them as a pooled range from [thecyborg](https://thecyborg.co.il/magazine/facebook-ads-cost-israel/), [airdigital](https://airdigital.co.il/digital-marketing-cost-israel/), [digiassets](https://digiassets.co.il/tools/facebook-ads-budget-calculator/), [buildoai](https://buildoai.com/blog/facebook-ads-management-cost), [danielzrihen](https://danielzrihen.co.il/internet-marketing-price/), [container](https://www.container.org.il/%D7%9B%D7%9E%D7%94-%D7%A2%D7%95%D7%9C%D7%94-%D7%A7%D7%9E%D7%A4%D7%99%D7%99%D7%9F-%D7%91%D7%A4%D7%99%D7%99%D7%A1%D7%91%D7%95%D7%A7/), [meshulav](https://meshulav.co.il/%D7%90%D7%99%D7%9A-%D7%9C%D7%91%D7%97%D7%95%D7%A8-%D7%A1%D7%95%D7%9B%D7%A0%D7%95%D7%AA-%D7%A7%D7%99%D7%93%D7%95%D7%9D-%D7%91%D7%A4%D7%99%D7%99%D7%A1%D7%91%D7%95%D7%A7/):
  - Freelancer management ₪1,500–3,500/month; entry-level freelancers ₪800–1,800; experienced ₪1,500–5,000
  - Local agency ₪2,000–5,000/month; boutique ₪2,000–3,500; large agencies ₪4,000–10,000+ (strategy, copy, creative and management included)
  - Percentage model: 10–20%, or 15–25%, of the media budget
  - One comparison table is higher: freelancers ₪2,000–8,000, agencies ₪4,000–20,000+
  - The digiassets figures are before VAT. Several sources stress that the fee is separate from the media budget paid to Meta.
- A concrete package: BestLinks sells monthly Facebook campaign management at ₪2,500 — [BestLinks](https://shop.bestlinks.co.il/services/facebookAds)
- Global benchmark: local-business agencies charge about US$500–2,500+ a month; small businesses spend about US$200–1,000 a month on media — [Clicksgeek](https://clicksgeek.com/facebook-ads-management-cost/); [Adwave](https://adwave.com/resources/facebook-advertising-for-small-business)
- Meta ad prices rose 14% year over year in Q3 2026 — [Singlegrain](https://www.singlegrain.com/?p=81379)
- WhatsApp services:
  - Custom bot: ₪3,500 basic, about ₪6,500 mid-tier with CRM, ₪12,000+ full AI agent; or ₪3,500–12,000 one-time plus ₪100–300/month hosting — [Achiya ToI](https://blogs.timesofisrael.com/israels-whatsapp-bot-market-mapped/)
  - An ROI example cites ₪5,000 bot setup — [ToI blog](https://blogs.timesofisrael.com/what-israeli-smbs-really-pay-for-automation/)
  - One case study reports ₪800/month across three branches — [dev.to](https://dev.to/aibuddy_il/small-business-automation-what-to-automate-first-israel-2026-2oi6)
  - Managed WhatsApp broadcast ₪0.90–2.00 per message, Meta fees included — [Gambot](https://gambot.co.il/PriceList/ManagedBroadcast/)
  - Managed automation from ₪500/month (Automatix) — [Achiya](https://achiya-automation.com/en/blog/automation-companies-israel-2026/)
  - LLM cost for a bot handling about 200 messages a day fell from about ₪150 to about ₪60 a month (Q2 2026) — [ToI blog](https://blogs.timesofisrael.com/israels-quiet-q2-2026-bot-pricing-reset/)

### Inferences
- An SMB that buys both services today, an ads freelancer (₪1,500–3,500) plus a WhatsApp bot or broadcast tool (₪179–999), pays about ₪1,700–4,500 a month before media. A Marta price point of a few hundred shekels a month would undercut that by roughly 5–10x. It would also sit above pure tools such as Gambot Growth (₪179) or Kampi (₪149–298), so it needs to justify itself by doing work the SMB would otherwise pay a human for.
- Agency fees are sticky because agencies bundle creative and strategy. Marta's substitute claim is strongest for the ₪800–3,500 freelancer tier.

### Gaps
- No independent survey of Israeli agency fees was found; all figures come from agency or vendor blogs.
- No pricing was found for agencies that bundle Meta ads with WhatsApp marketing.

## Q5. Where is the gap: does any Israeli product combine Meta Ads + Audiences + WhatsApp in one Hebrew conversational AI interface?

### Takeaway
I found no Israeli product that combines Meta Ads management, audience building (custom/lookalike, Pixel/CAPI) and WhatsApp Business Platform messaging behind one Hebrew conversational AI agent for non-experts. The closest partial overlaps are Signals JAKO (Meta-connected AI bots plus "marketing campaigns", most likely WhatsApp campaigns), Pushleads (CRM with WhatsApp plus ads integrations), Wix (Hebrew Meta-ads add-on plus its own inbox and email AI) and Fireberry plus partners (Meta lead import plus WhatsApp). The real competitor for the conversational part is the free combination of Meta's official Ads MCP, a Hebrew LLM, and Meta's free Business Agent for WhatsApp.

### Cited Findings
- Signals' JAKO is a cloud system "connected directly to Meta for AI bots and marketing campaigns" (scope of "campaigns" unclear) — [Achiya](https://achiya-automation.com/en/blog/automation-companies-israel-2026/)
- Pushleads connects WhatsApp, email, SMS and ads, and integrates with Facebook Business Suite, Google Ads and TikTok — [Capterra IL](https://www.capterra.co.il/software/1112384/Pushleads)
- Fireberry imports Facebook leads in real time and has a WhatsApp add-on — [Fireberry integrations](https://fireberry.com/help/integrations); [Fireberry WhatsApp](https://www.fireberry.com/features/whatsapp)
- Wix creates Meta campaigns from the dashboard, in Hebrew — [Wix he](https://support.wix.com/he/article/facebook-instagram-ads-יצירת-קמפיין)
- Meta Ads MCP (free, 29 tools) plus Claude or ChatGPT gives natural-language control of Meta ads — [PPC Land](https://ppc.land/meta-opens-its-ad-system-to-claude-and-chatgpt-with-new-ai-connectors/). It is marketed in Hebrew to Israeli SMBs — [bestai.co.il](https://bestai.co.il/articles/meta-mcp-claude-desktop-small-business-2026)
- Meta Business Agent covers WhatsApp, Messenger and IG conversations, free for now — [Gadgety](https://www.gadgety.co.il/363382/meta-business-agent-launched/)
- An Israeli bot-market commentator says the market has no single "best WhatsApp bot company", only three different product types sharing one app — [ToI blog](https://blogs.timesofisrael.com/israels-whatsapp-bot-market-mapped/)

### Inferences
- **Approximate count** (from this research; see the table below):
  - About 22 Israeli or Israel-focused WhatsApp messaging, bot and inbox products, including CRMs with WhatsApp add-ons
  - About 13 Israeli Meta-ads or AI-marketing products: 6 global or enterprise (Madgicx, AdgeAI, AdScale, StoreYa?, Trapica-defunct, Albert?) and about 7 local Hebrew SMB tools or agency systems (Wix ads, Kampi, Ultrads, ADAM, MIA, appy OS, Marketeam)
  - 0 products found doing Ads + Audiences + WhatsApp in a Hebrew conversational agent
- **Gap statement:** the Israeli market is split into WhatsApp vendors with no ads capability and ads tools with no WhatsApp leg. Audience work (custom/lookalike audiences built from WhatsApp or CRM lists, Pixel/CAPI health) is served by nobody local for non-experts. That joined-up loop (ad, then lead, then WhatsApp follow-up, then retargeting audience) is what Marta could own.
- **Threat statement:** the gap is closing from above. Meta's free MCP plus Hebrew LLMs, Meta Business Agent, and Meta's own AI campaign flows (URL-to-campaign) could make Marta's "talk instead of clicking" pitch generic. Marta's differentiation probably has to be safety rails (approvals, budget caps, undo), Hebrew SMB playbooks, cross-channel orchestration, and compliance (Israeli spam law consent for WhatsApp marketing).

### Gaps
- I could not verify feature depth (audiences, Pixel/CAPI) for any local SMB tool. Kampi, Ultrads, ADAM and Signals JAKO deserve direct demos.
- I could not check the Meta Business Partner Directory for Israel-based Tech Providers building ads plus WhatsApp combinations.
- Facebook-group discussions (e.g. Israeli marketer groups) were not searchable through the tools available.

### Summary inventory table

Legend: Y = yes, P = partial or claimed, N = no evidence found, ? = unverified. ILS conversions marked ≈ are my own at about ₪3.6/$.

| Name | Israeli? | Category | Meta Ads? | Audiences? | WhatsApp? | AI chat interface? | Hebrew? | Price range (ILS) | Source URL |
|---|---|---|---|---|---|---|---|---|---|
| Glassix | Y (Tel Aviv, 2015) | AI contact center / WhatsApp BSP-style inbox | N | N | Y (bots, Flows, broadcasts) | Y (GPT bots for end-customers, not for the operator) | likely (Israeli; not confirmed) | US$49–65/user/mo (≈₪175–235); ToI: "thousands ₪/mo" | https://www.capterra.co.il/software/1052241/glassix |
| CommBox | Y (2013) | Enterprise AI omnichannel / WhatsApp | N | N | Y | Y (customer-facing AI agents) | Y (Clalit, Pelephone) | Quote only | https://builtin.com/company/commbox |
| InforU | Y | Multichannel messaging, Meta BSP (claims 30k+ orgs) | N | N | Y (API, broadcast lists) | N | Y | Not published | https://www.inforu.co.il/features/whatsapp-api/ |
| Micropay | Y | SMS/WhatsApp, Meta Tech Provider | N | N | Y | N | Y | Not published | https://site.micropay.co.il/whatsapp.php |
| Soprano (Unicell) | Y | Multichannel messaging API | N | N | Y | N | Y | Not published | https://unicell.co.il/%D7%A1%D7%95%D7%A4%D7%A8%D7%A0%D7%95/ |
| inwise | Y | Email/SMS/WhatsApp marketing | N | N | Y (official API) | N | Y | Not published | https://www.inwise.co.il/%D7%95%D7%95%D7%90%D7%98%D7%A1%D7%90%D7%A4/ |
| Gambot | Y | WhatsApp bot + broadcast SaaS | N | N | Y | P (bot builder) | Y | ₪179 / ₪359 / ₪645 /mo + VAT; managed ₪0.90–2.00/msg | https://gambot.co.il/PriceList/ |
| Botomati | Y? | WhatsApp bot | N | N | Y | P | Y? | Free ≤500 msgs/mo | https://achiya-automation.com/en/blog/whatsapp-bot-providers-israel-2026/ |
| WBsender | Y? | WhatsApp bulk sender | N | N | Y (bulk) | N | Y? | n/a | https://achiya-automation.com/en/blog/whatsapp-bot-providers-israel-2026/ |
| Signals (JAKO/Push/MaxBot) | Y | WhatsApp AI bots + campaigns, multichannel | P? ("connected to Meta… marketing campaigns", unclear) | N | Y | P (AI bots) | Y? | Not found | https://achiya-automation.com/en/blog/automation-companies-israel-2026/ |
| Automatix | Y (Rehovot, 2024) | Managed automations/WhatsApp bots | N | N | Y | P | Y | from ₪500/mo | https://www.b144.co.il/b144_sip/401D0D1A4370655D411C0C1B43/ |
| Hadavar | Y | WhatsApp API package | N | N | Y | N | Y | from ₪90/mo + VAT | https://www.hadavar.co.il/product/%D7%A9%D7%9C%D7%99%D7%97%D7%AA-%D7%95%D7%95%D7%98%D7%A1%D7%90%D7%A4-%D7%9E%D7%90%D7%9C%D7%9E%D7%A0%D7%98%D7%95%D7%A8-%D7%95%D7%95%D7%A7%D7%95%D7%9E%D7%A8%D7%A1-%D7%95%D7%90%D7%A4%D7%9C%D7%99%D7%A7/ |
| Taskey | Y | Task/CRM with WhatsApp module | N | N | Y (3rd-party API) | N | Y | ₪70/number/mo | https://taskey.co.il/%D7%9E%D7%95%D7%93%D7%95%D7%9C-%D7%95%D7%95%D7%90%D7%98%D7%A1%D7%90%D7%A4-api/ |
| Ariko.ai | Y? (Israel-focused) | WhatsApp AI bot SaaS | N | N | Y | Y (AI bot) | Y? | US$99–399/mo + VAT (≈₪355–1,435) incl. Meta fees | https://ariko.ai/en/guide/whatsapp-bot-cost |
| DanAI | Y? | Chatbot (Hebrew/English) | N (FB Business Suite integration) | N | Y | Y | Y | Not found | https://www.capterra.ca/software/1107748/DanAI |
| Achiya Automation | Y (Ashdod) | Custom WhatsApp bot studio | N | N | Y | Y (custom AI agents) | Y | ₪3,500–12,000 one-time + ₪100–300/mo | https://blogs.timesofisrael.com/israels-whatsapp-bot-market-mapped/ |
| 019 (019SMS) | Y | SMS carrier/API (+ WhatsApp app on Make) | N | N | P | N | Y | Not found | https://apps.make.com/whatsapp-019 |
| Smoove | Y (Petah Tikva, 2013) | Email/SMS marketing automation | N (lead-gen pages) | N | Y (paid add-on) | N | Y | WhatsApp extra cost; amount not found | https://www.smoove.io/pricing/ |
| ActiveTrail | Y | Email/SMS marketing automation | N | N | P (WhatsApp marketing content; price not found) | N | Y | SMS US$41–344 (≈₪150–1,240); WhatsApp n/a | https://www.activetrail.com/?p=64768 |
| Responder (רב מסר) | Y | Email autoresponder | N | N | P (via Zapier only) | N | Y (Hebrew-only) | Not found | https://zapier.com/apps/responder/integrations/whatsapp-notifications/1659211/send-whatsapp-notifications-messages-when-new-subscribers-are-added-in-responder-rb-msr |
| Pulseem | Y | Email/SMS marketing | N | N | N (no evidence) | N | Y | Not found | https://site.pulseem.co.il/?p=3912 |
| Fireberry (ex-Powerlink) | Y | CRM | P (Facebook lead import) | N | Y (add-on; Pingmee AI partner) | N | Y | US$25–35/user/mo (≈₪90–125), 3-seat min | https://www.fireberry.com/features/whatsapp |
| monday.com CRM | Y | Work OS/CRM | P (FB Lead Ads via Zapier/Make) | N | P (via integrations; native claimed) | N | Y | Not researched | https://zapier.com/apps/facebook-lead-ads/integrations/monday |
| Pushleads | ? | CRM + WhatsApp/SMS/ads | P (FB Business Suite integration) | N | Y | N | ? | Free tier listed | https://www.capterra.co.il/software/1112384/Pushleads |
| Lead.im | Y? | Lead management for agencies | P (ad-system connections) | N | N | N | Y? | Not found | https://sourceforge.net/software/product/Lead.im |
| Madgicx | Y (Herzliya, 2018) | AI Meta-ads platform (e-com) | Y | Y? (not verified here) | N | P ("AI Marketer") | N (no evidence) | US$44–99+/mo by spend (≈₪160–355+) | https://toolradar.com/tools/madgicx/pricing |
| AdgeAI | Y (acq. Publicis 2026) | Enterprise AI marketing agents | P (Google Ads, Salesforce; Meta ties) | ? | N | Y (agents) | N | Enterprise | https://www.calcalistech.com/ctechnews/article/r1wr00eto11x |
| AdScale | Y (Yokneam) | AI ads for e-com (FB/IG/Google) | Y | ? | N | N | P (Hebrew Shopify listing) | US$149–169/mo (≈₪535–610) | https://startupim.com/company/adscale |
| StoreYa Traffic Booster | ? (not confirmed) | AI ads for small stores | Y (Pro tier) | ? | N | N | N | US$120–1,000/mo incl. budget (≈₪430–3,600) | https://apps.shopify.com/traffic-booster |
| Trapica | Y (defunct standalone) | AI ad targeting | Y | Y? | N | N | N | n/a | https://theatdb.com/companies/trapica |
| Albert.ai | ? (low-reliability source) | Enterprise autonomous ads | Y | ? | N | N | N | Custom, $100k+/yr budgets | https://madgicx.com/compare/adscale-vs-albert-ai |
| Marketeam.ai | Y (Tel Aviv) | AI marketing agents (social content) | P? (directory claim) | N | N | Y (agents) | ? | Not found | https://prnewswire.com/news-releases/marketeamai-launches-ella-the-autonomous-ai-social-media-marketing-agent-for-smbs-marking-the-first-step-in-marketeamais-ambitious-rollout-of-specialized-ai-marketing-agents-302105518.html |
| Wix (FB & IG Ads by Wix) | Y | Website builder with native Meta ads | Y (creates new ad account, AI optimisation) | P (Wix algorithm) | N (not found) | P (AI assistant for email) | Y | Media spend (+ claimed 15% fee) | https://support.wix.com/he/article/facebook-instagram-ads-סקירה-כללית |
| Kampi | Y | Hebrew SMB social + paid campaigns | P (Pro tier) | ? | N | ? | Y | ₪149 basic / ₪298 Pro per mo (single-snippet) | https://www.kampi.co.il/ |
| Ultrads | Y? | Hebrew AI ad generation/publishing (FB/IG/Google) | Y | ? | N | ? | Y | Monthly, no commitment (price n/a) | https://ultrads.ai/ |
| ADAM (מיה ובן) | Y | "AI agent" for SMB marketing | P (budgets, ROI) | ? | ? | P | Y | ₪290/mo (single-snippet) | https://miaben.co.il/ai-adam/ |
| MIA (קפטן דיגיטל) | Y | AI social/ads system (agency) | P | ? | N | ? | Y | Not found | https://captaindigital.co.il/social-media |
| appy OS (Appy Creative) | Y | Agency with own AI optimisation | P | ? | N | N | Y | Agency retainer | https://www.appy.co.il/ |
| Meta Ads MCP + Claude/ChatGPT | N (Meta/US) | Official AI connector (substitute) | Y (29 tools) | Y? (datasets/audiences, not verified) | N | Y | Y (via LLM) | Free MCP + LLM sub (~₪80/mo Claude Pro per blog) | https://ppc.land/meta-opens-its-ad-system-to-claude-and-chatgpt-with-new-ai-connectors/ |
| Meta Business Agent | N (Meta) | AI agent in WhatsApp/IG/Messenger | N | N | Y | Y | ? (Meta AI Hebrew launched Jul 2026) | Free for now | https://www.gadgety.co.il/363382/meta-business-agent-launched/ |
| Freelancer / agency (substitute) | Y | Human service | Y | Y | sometimes | N | Y | Freelancer ₪800–5,000/mo; agency ₪2,000–10,000+/mo; or 10–25% of spend | https://thecyborg.co.il/magazine/facebook-ads-cost-israel/ |
