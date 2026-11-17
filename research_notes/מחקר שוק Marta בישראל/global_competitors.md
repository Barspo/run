# Global competitors to "Marta" (Hebrew-first AI agent for Meta Ads, Audiences, Pixel/CAPI, Pages/IG and WhatsApp), as of Nov 2026

> Sourcing note: in this session, WebFetch could not reach any vendor or press host that was tried (ppc.land, techcrunch.com, madgicx.com, adamigo.ai all failed DNS resolution under the session's network allowlist). All findings below come from web-search result summaries and snippets, not from reading the full pages. Most pricing figures come from third-party or competitor-written comparison pages. Treat every price as "reported, verify on vendor page". Where sources conflict, both figures are shown.

## 1. AI-first Meta-ads tools and agents (incl. Claude/ChatGPT MCP connectors): what they do, pricing, funding, traction

### Takeaway
The Meta-ads "AI agent" layer has settled into a crowded band of self-serve tools priced at about $45–$99/month entry and $199–$349/month for agency or unlimited tiers (Madgicx, Bïrch, AdAmigo, Ryze). Enterprise platforms like Smartly charge about 2–5% of ad spend. The biggest change in 2026 is that Meta launched its own **free official MCP server/CLI (Apr 29, 2026)**, so Claude and ChatGPT can operate a Meta ad account directly. That turns "chat with your Meta Ads" into a commodity. None of the tools found offers Hebrew or RTL as a stated feature.

### Cited Findings
**Meta's official "Ads AI Connectors" (MCP + CLI)**
- Meta launched an official ads MCP server in open beta on **April 29, 2026** at `mcp.facebook.com/ads`, together with a CLI installed via npm. Meta calls them "Ads AI Connectors". — [usecarly.com](https://www.usecarly.com/blog/meta-ads-mcp/); [dataally.ai](https://www.dataally.ai/blog/meta-ads-mcp-cli-guide); [adadvisor.ai](https://adadvisor.ai/blog/mcp-facebook-com-ads-official-meta-setup)
- It is reported to expose **29 natural-language tools** covering performance reporting, campaign management, catalog management and "signal diagnostics". The last is the closest match to Pixel/CAPI health checks, but no source explicitly confirms Pixel or audience-creation tools. — [usecarly.com](https://www.usecarly.com/blog/meta-ads-mcp/); [mcp.directory](https://mcp.directory/blog/meta-ads-cli-mcp)
- Meta charges nothing extra for it. The user pays only for the Claude/ChatGPT plan and ad spend. — [contextbolt.com](https://contextbolt.com/blog/meta-ads-mcp/)
- In Claude it is added as a custom connector with Facebook OAuth. In ChatGPT it is added as a custom connector or MCP server in developer mode, and the user approves which ad accounts the agent can reach. — [go9x.com](https://go9x.com/blog/meta-ads-mcp); [admanage.ai](https://admanage.ai/blog/connect-meta-ads-mcp-to-claude)
- On **July 16, 2026**, Meta opened the ads MCP server to developer-app connections and added "ads MCP server rules" that govern what agents may do on an ad account. — [admakeai.com (Aug 2026 changelog)](https://admakeai.com/blog/meta-ads-updates-august-2026)
- One guide warns that MCP writes "have no safety net": actions hit the live account immediately. — [ppc.io](https://ppc.io/blog/facebook-ads-mcp)
- Meta also runs a separate developer MCP at `mcp.facebook.com/devtools`. — [adadvisor.ai](https://adadvisor.ai/blog/mcp-facebook-com-ads-official-meta-setup)

**Pipeboard (third-party Meta Ads MCP, source-available)**
- Source-available Meta Ads MCP on GitHub. Its homepage claims **1,000+ active users** and **$100M+/month in ad spend** managed across Meta, Google and TikTok (self-reported). — [pipeboard.co](https://pipeboard.co/); [GitHub](https://github.com/pipeboard-co/meta-ads-mcp)
- Free plan available. Reported paid tiers conflict: Pro $29.90, Premium $99, Agency $199/month per [gethookd.ai](https://www.gethookd.ai/learn/pipeboard-reviews-pricing-alternatives-is-this-meta-ads-mcp-worth-it/), versus Starter $29 to Agency $129 with 35% off annual per [madgicx.com review](https://madgicx.com/compare/pipeboard-review). Extra ad-account slots reportedly cost $10/month. — [adkit.so](https://adkit.so/alternatives/pipeboard/pricing)
- Pipeboard's own README reportedly calls Meta's official connector "the safest single-platform option". — [contextbolt.com](https://contextbolt.com/blog/meta-ads-mcp/)
- Other third-party Meta Ads MCPs listed: AdPlug, Ryze AI. — [mcpservers.org (AdPlug)](https://mcpservers.org/servers/adplug-app-integrations-meta-ads); [mcpservers.org (Ryze)](https://mcpservers.org/servers/www-get-ryze-ai-meta-ads-mcp)
- Zapier exposes Meta Ads through its MCP as a "paid middleman route". Make/Zapier webhooks are described as one-shot triggers, not conversational agents. — [go9x.com](https://go9x.com/blog/meta-ads-mcp); [admetrics.io](https://www.admetrics.io/post/how-to-run-meta-ads-directly-from-claude-and-chatgpt)

**Madgicx (Israel-HQ'd, global product; Meta-only AI "super app")**
- HQ is listed as **Herzliya, Israel**; some profiles say Tel Aviv. — [startupim.com](https://startupim.com/company/madgicx); [startuphub.ai](https://www.startuphub.ai/startups/madgicx)
- Madgicx's own LLM-info page says pricing is tiered by monthly ad spend and **starts at $45/month**, with monthly, quarterly and annual billing. — [madgicx.com/llm-info](https://madgicx.com/llm-info). Other listings: $44 (aitoolsatlas, Mar 2026) — [aitoolsatlas.ai](https://aitoolsatlas.ai/tools/madgicx/pricing); Pro **$99/month including "AI Chat"** — [Capterra](https://www.capterra.com/p/182983/Madgicx/pricing)
- Core AI features: **AI Marketer**, which audits Meta accounts daily and prepares actions that go live after one-click approval; **AI Chat** for conversational analytics; and an AI Ads Generator that turns a link, image or Ad Library ad into 10+ ads. — [toolsurf.com](https://www.toolsurf.com/madgicx-pricing-2026/); [superscale.ai review](https://superscale.ai/alternatives/madgicx/review)
- Madgicx publishes guidance on connecting Meta Ads to ChatGPT/Claude via MCP. — [madgicx.com blog](https://madgicx.com/blog/connect-meta-ads-to-chatgpt)
- Funding data conflict: CB Insights lists PeakSpan Capital as an investor ([cbinsights](https://www.cbinsights.com/company/madgicx)); Kustiq says "Growth ($6.8M)" ([kustiq.com](https://kustiq.com/company/madgicx.com)); StartupHub says $1.0M ([startuphub.ai](https://www.startuphub.ai/startups/madgicx)). Headcount is estimated at about 46–54. — [kustiq.com](https://kustiq.com/company/madgicx.com)
- A vendor-cited G2 rating is 4.6/5 from 220+ reviews. — [superscale.ai](https://superscale.ai/alternatives/madgicx/review)

**AdAmigo.ai (chat-first "AI agent for Meta ads")**
- Self-described as "the world's first AI agent for Meta advertising". It lets users "manage your Meta ads via simple chat commands" and connects as a Meta Business Technology Partner. — [gethookd.ai](https://www.gethookd.ai/learn/adamigo-ai-reviews-features-pricing-is-this-meta-ads-tool-legit/); [adamigo.ai blog](https://www.adamigo.ai/blog/best-ai-tools-meta-ads)
- Reported pricing is per ad account: **$99/month Entry, $349/month Unlimited**. — [admanage.ai](https://admanage.ai/compare/adamigo-alternative). Another directory says pricing is tiered by ad spend ([softwaresuggest](https://www.softwaresuggest.com/adamigo-ai)), and G2 shows no pricing ([G2](https://www.g2.com/products/adamigo-ai/pricing)).
- Platform scope is disputed: Meta-only per one competitor, Meta and Google per another. — [admanage.ai](https://admanage.ai/compare/adamigo-alternative); [adadvisor.ai](https://adadvisor.ai/blog/adamigo-vs-adadvisor)

**Ryze AI (get-ryze.ai)**
- Flat **$89/month** entry plan with a 7-day trial, covering Google, Meta, TikTok, LinkedIn and 50+ integrations. A third-party guide lists it at $100/month. — [get-ryze.ai/pricing](https://www.get-ryze.ai/pricing); [adkit.so](https://adkit.so/alternatives/ryze/pricing)
- Proposes bid, budget, keyword and creative changes that the owner approves. Also offers an MCP connector with 150+ tools for Claude/ChatGPT. — [toolradar.com](https://toolradar.com/tools/ryze-ai); [mcpservers.org](https://mcpservers.org/servers/www-get-ryze-ai-meta-ads-mcp)
- Operated by Meow AI, LLC, founded 2024. No outside funding found; it is described as "Independent & 100% owned". — [get-ryze.ai/ai-info](https://www.get-ryze.ai/ai-info); [toolradar.com](https://toolradar.com/tools/ryze-ai)

**Bïrch (ex-Revealbot)**
- Revealbot rebranded as Bïrch (revealbot.com redirects to bir.ch). Pricing scales with connected ad spend, starting at about $45–$49/month. Automation rules unlock on the **$99 Pro** plan. — [superscale.ai](https://superscale.ai/alternatives/revealbot/pricing); [madgicx.com review](https://madgicx.com/compare/birch-review); [softwareadvice](https://www.softwareadvice.com/ca/marketing/reveal-profile/)
- Its AI chat reads performance, edits existing Meta ads and drafts rules, but per its help centre **cannot create campaigns**. — [madgicx.com review](https://madgicx.com/compare/birch-review)
- 14-day free trial. — [costbench.com](https://www.costbench.com/software/marketing-automation/birch/)

**Smartly (enterprise)**
- Pricing is not published. It is reported as **about 3–5% of ad spend** (sometimes as low as 2%), with a monthly minimum of about **$4–5K** (about €5K). The fee applies to spend in all connected ad accounts. — [superscale.ai](https://superscale.ai/alternatives/smartly/pricing); [hunchads.com](https://hunchads.com/blog/smartly-pricing); [G2 contract excerpt](https://g2.com/products/smartly-io/pricing)
- Signed an LOI to acquire measurement company **INCRMNTAL** on Mar 17, 2026 (reported closed May 2026). — [AdExchanger](https://www.adexchanger.com/measurement/smartly-is-planning-to-acquire-incrmntal-within-the-next-few-weeks/); [pocketgamer.biz](https://www.pocketgamer.biz/smartly-signs-letter-of-intent-to-acquire-measurement-platform-incrmntal)
- Majority owned by Providence Equity Partners. — [TechCrunch](https://techcrunch.com/?p=1925501). Latka (aggregator) reports about $101M revenue and about 918 employees. — [getlatka.com](https://getlatka.com/companies/smartly.io)

**AdCreative.ai (creative generation)**
- Acquired by **Appier** for **US$38.7M total ($27.3M base)**, announced Feb 2025. It still operates under the AdCreative.ai brand. — [FrenchWeb](https://www.frenchweb.fr/appier-acquiert-la-startup-francaise-adcreative-ai-pour-387-millions-de-dollars/451864); [technode.global](https://technode.global/prnasia/appier-acquires-adcreative-ai-in-strategic-move-to-lead-generative-ai-powered-advertising-and-marketing-innovation)
- Third-party listing (possibly stale): Starter $39/month ($25 annual), Professional $249/month ($149 annual). — [usagepricing.com](https://usagepricing.com/blueprint/adcreative-ai)

**Pencil / Trapica / Marpipe / Albert (creative and older "AI media buyer" generation)**
- Pencil was acquired by **The Brandtech Group**, its 10th acquisition. — [AdExchanger](https://adexchanger.com/ai/the-brandtech-group-snatches-up-generative-ai-ad-platform). Pencil Core is reported at **$14/month**. — [trylapis.com](https://trylapis.com/resources/pencil-ai-alternatives)
- Trapica (Tel Aviv, founded 2017, Techstars) is reported as acquired by Pencil and no longer a standalone brand. This is a single, unverified database source. — [theatdb.com](https://theatdb.com/companies/trapica); [startupim.com](https://startupim.com/company/trapica-labs)
- Marpipe (creative testing): Startup $199/month and Enterprise $999/month per [pricingsaas.com](https://pricingsaas.com/companies/marpipe); lowest paid plan $249/month per a May 2026 snapshot from [xpay.sh](https://www.xpay.sh/saas-pricing/marpipe).
- Albert.ai was acquired by **Zoomd** (announced Mar 28, 2022). It continues as "Albert.ai Agnostic DSP" in 2026 and targets enterprise. — [PR Newswire](https://prnewswire.com/il/news-releases/zoomd-announces-the-acquisition-of-artificial-intelligence-marketing-platform-albert-301511595.html); [ecosistemastartup.com](https://ecosistemastartup.com/zoomd-presenta-albert-ai-su-dsp-de-publicidad-con-ia/)

**Google-first PPC tools with partial Meta coverage**
- Optmyzr: about **$209/month** Essentials (verified Sep 2026 per one source), with spend-based tiers of $209–$899. Another source says about $249. Its AI assistant is "Sidekick", though one comparison found no AI chat on its pricing pages. Meta support is disputed. — [tryatria.com](https://www.tryatria.com/blog/optmyzr-pricing); [groas.ai](https://groas.ai/post/optmyzr-pricing-review-alternatives-2026-cost-features-competitors); [madgicx.com review](https://madgicx.com/compare/optmyzr-review)
- Adzooma: **free plan** with unlimited ad accounts across Google, Microsoft and Meta. — [get-ryze.ai](https://www.get-ryze.ai/blog/adzooma-pricing-2026); [Capterra](https://www.capterra.co.uk/software/188236/adzooma)

**SMB/emerging-market agents and Shopify-app layer**
- Zocket (India) raised a **$3M seed** led by Kalaari Capital. It offers an "agentic suite" of five agents (creative, optimization, competitor intel, audience targeting, brand monitoring), mainly for SMB Meta ads. — [Inc42](https://inc42.com/buzz/adtech-startup-zocket-bags-3-mn-from-kalaari-capital-to-help-smbs-optimise-ad-spends); [G2](https://www.g2.com/products/zocket-2025-10-29/discuss)
- Shopify App Store Meta-ads apps: Agency AI **$59/month**, Adwisely from **$49/month**, AdScale from **$149/month**. — [Agency AI](https://apps.shopify.com/agency-ai); [Adwisely](https://apps.shopify.com/adwisely); [AdScale](https://apps.shopify.com/adscale)
- An independent July 2026 analysis argues that most $1M–$50M DTC brands no longer need Madgicx, AdAmigo or Revealbot for basic budget and targeting jobs, because Meta's native tools now do this for free. — [alexneiman.com](https://alexneiman.com/meta-native-ai-vs-third-party-ad-tools-2026/)

### Inferences
- After Meta's free MCP (Apr 2026), a bare "talk to your Meta Ads in a chat" feature has no moat. Any Israeli SMB with a $20 Claude/ChatGPT plan can already query and edit campaigns, in Hebrew if the LLM handles Hebrew. Marta's value has to come from the parts the MCP does not cover: Hebrew-first UX and copy, guardrails and approval flows (the MCP has "no safety net"), opinionated playbooks for non-experts, and spanning **Ads + Audiences + Pixel/CAPI + WhatsApp + Pages** in one agent. No competitor found offers that full span.
- Third-party agent tools are mostly Meta-ads-only and English-only, and none integrates WhatsApp Business Platform messaging. Madgicx is the closest functional analogue (AI Marketer + AI Chat) and is itself Israeli-HQ'd, so it is the most likely "known name" Israeli advertisers will compare Marta to.
- Price anchors for the "AI Meta-ads agent" job: about $45–$99/month for SMB, about $199–$349/month for agency/unlimited, $0–$30/month for MCP connectors, and 2–5% of spend for enterprise.

### Gaps
- Primary vendor pricing pages could not be fetched (DNS blocked), so all prices are second-hand and several conflict (Pipeboard, AdAmigo, Madgicx, Bïrch).
- No reliable 2025–2026 funding or customer counts were found for AdAmigo, Pipeboard, Bïrch, Ryze, or Madgicx (where data conflicts).
- The exact tool list of Meta's official MCP is unconfirmed: whether it can create Custom/Lookalike audiences or manage Pixel/CAPI, and whether it covers WhatsApp or Pages. One unattributed guide also claimed Claude's connector directory had no Meta entry as of Oct 15, 2026; this is unverified.
- No information was found on any of these tools offering a Hebrew UI or RTL support.
- No 2026 information was found on Marpipe's status, Trapica's acquisition date, or Fluency's round details.

## 2. Meta's own AI offerings that substitute (Advantage+, GenAI creative, Business AI assistant, Business Agent on WhatsApp, end-to-end automation), and availability in Hebrew/Israel

### Takeaway
Meta is building most of Marta's value proposition natively and for free:
- a conversational **AI Business Assistant** in Ads Manager and Business Suite (global since Apr 24, 2026; agentic actions in testing since Oct 2026),
- **Manus** inside Ads Manager,
- Advantage+ end-to-end campaigns (run-rate above $75B as of Q2 2026),
- a **Business Agent** for WhatsApp, IG and Messenger (global launch June 3, 2026),
- a stated goal of fully automated ad creation and targeting by end of 2026.

The gap Marta can exploit is that **Hebrew support for Meta's business-side AI is unconfirmed**. Meta's consumer Meta AI launched in Hebrew in Israel in June 2026, but no source confirms Hebrew in the business assistant, Business Agent, or GenAI ad text and translation tools.

### Cited Findings
**End-to-end automation plan**
- A WSJ report (June 2025) said Meta aims to let brands fully create and target ads with AI by end of 2026: a brand supplies a product image and budget, and Meta's AI generates the ad and chooses the targeting. — [Yahoo Finance](https://finance.yahoo.com/news/meta-automate-ads-end-end-135910411.html?.tsrc=rss); [Quartz](https://qz.com/meta-fully-automate-ai-advertising-2026-1851783320)
- On the Q1 2025 call, Zuckerberg described advertising being redefined "into an AI agent that delivers measurable business results at scale". — [PYMNTS](https://www.pymnts.com/?p=2710442)
- Advantage+ "end-to-end" solutions reached a **>$75B annual revenue run-rate per Q2 2026 prepared remarks**, up from about $60B in Q3 2025. — [paceads.com](https://paceads.com/research/meta-ads-statistics-2026); [valueaddvc.com](https://valueaddvc.com/blog/meta-ai-revenue-how-much-of-facebooks-135b-is-actually-from-ai-products)
- Q3 2026 call (late Oct 2026):
  - "nearly 10 million advertisers used at least one" generative-AI creative tool in Q3;
  - Meta AI Business Assistant was integrated into Creator Marketing Hub;
  - Zuckerberg: "businesses of all sizes are going to use AI agents across… sales, marketing, customer service";
  - Q3 revenue was reported at $64.6B, up 26%.
  
  — [Benzinga transcript](https://www.benzinga.com/news/26/10/62514401/meta-platforms-q3-2026-earnings-call-transcript); [stockanalysis.com transcript](https://stockanalysis.com/stocks/meta/transcripts/718643-q3-2026/); [gloom.sh summary](https://gloom.sh/stocks/meta/transcripts/q3-2026)
- The Marketing API stopped allowing creation or updates of **legacy Advantage+ shopping/app campaigns after May 19, 2026**. On Oct 27, 2026, Meta applied v26.0 removals to all API versions, which hits older third-party integrations. — [segwise.ai](https://segwise.ai/blog/meta-ads-updates); [adadvisor.ai](https://adadvisor.ai/blog/meta-ads-updates-2026)

**AI Business Assistant in Ads Manager (the most direct substitute for Marta)**
- On about **Apr 24, 2026**, Meta rolled out its conversational AI business assistant to advertisers and agencies of all sizes worldwide, in Ads Manager, Business Suite and Business Support Home, at no extra cost. — [MediaPost](https://www.mediapost.com/publications/article/414547/meta-rolls-out-ai-business-assistant-to-all-advert.html); [Social Media Today](https://www.socialmediatoday.com/news/meta-expands-access-to-meta-ai-business-assistant/818263/)
- Launch languages are reported as English, Spanish, French, German, Portuguese and Mandarin, later expanded to "local languages" across the U.S., EMEA, APAC and LATAM. **Hebrew is not named.** — [mediainfoline.com](https://www.mediainfoline.com/techno/meta-ai-business-assistant-expands-globally-more-languages); [medianews4u](https://www.medianews4u.com/meta-expands-ai-business-assistant-globally-with-multilingual-support-for-advertisers/)
- At Advertising Week NY (Oct 6–7, 2026), Meta announced agentic capabilities: generating creative, changing targeting and adjusting budgets from natural-language prompts, with changes staged for approval. These are **in testing**, with broader availability expected through Q4 2026. — [CommonThread](https://commonthreadco.com/blogs/coachs-corner/metas-new-ai-agent-can-now-run-your-ads-what-the-advertising-week-2026-update-means-for-ecommerce-brands); [adgully](https://www.adgully.com/post/21851/meta-unveils-agentic-ai-capabilities-in-ads-manager-to-automate-campaign-execution); [xwork.my](https://www.xwork.my/meta-ai-ads-manager-agentic-malaysia-2026/); [goodmorningco.com](https://goodmorningco.com/blog/meta-ads-update-october-2026)
- **Manus**: Meta announced its acquisition on Dec 29, 2025 (reported at $2B+; terms undisclosed by Meta). Manus has been in Ads Manager's "Tools" menu since about Feb 2026, doing report-building, audience research and campaign analysis. Edits still require advertiser input. — [SBC News](https://sbcnews.co.uk/technology/2026/01/02/meta-acquires-ai-start-up-manus/); [Search Engine Land](https://searchengineland.com/meta-adds-manus-ai-tools-into-ads-manager-469410); [MediaPost](https://www.mediapost.com/publications/article/412845/meta-integrates-manus-ai-in-ads-manager.html)

**Generative-AI creative and Hebrew**
- Meta's GenAI text translation reportedly covers 12 languages (Spanish, Portuguese, French, German, Arabic, Chinese, among others), and image-overlay translation covers 6 Latin-script languages. Hebrew is not listed, and the guide notes Hebrew/Arabic creatives need RTL layouts built in-script. (Attribution to the exact page is unverified because pages could not be opened.) — [ad-radar.dev](https://ad-radar.dev/blog/meta-generative-ai-ad-tools); [trylapis.com](https://www.trylapis.com/resources/create-multilingual-ai-ads)
- Third-party creative tool Lapis advertises generation in 100+ languages, including RTL Hebrew and Arabic. — [trylapis.com](https://www.trylapis.com/resources/create-multilingual-ai-ads)
- Adweek (Oct 2026) reported advertisers pulling Meta ads that had "unwanted AI glow-ups", which signals brand-safety friction with Meta's automatic GenAI enhancements. — [Adweek](https://www.adweek.com/media/advertisers-pull-meta-ads-that-had-unwanted-ai-glow-ups/)

**Business Agent / Business AI on WhatsApp, IG and Messenger**
- On **June 3, 2026** (Conversations, London), Meta launched "Meta Business Agent" globally across WhatsApp Business, IG DMs, Messenger and Business Suite, after about two years of tests in India and Mexico. **More than 1M businesses** already used a Business Agent on WhatsApp/Messenger. A separate **Business Agent Platform** targets enterprises. — [Business Today](https://www.businesstoday.in/technology/artificial-intelligence/story/meta-unveils-ai-business-agent-platform-for-whatsapp-instagram-and-messenger-534739-2026-06-03); [ProPakistani](https://propakistani.pk/2026/06/06/whatsapp-business-gets-ai-agent-to-handle-customer-chats/); [ContentGrip](https://www.contentgrip.com/meta-whatsapp-business-agent/)
- Availability conflict: some outlets say it is open to all businesses, while others say the rollout is gated to eligible businesses in select markets. — [dev.to](https://dev.to/creeta/meta-business-ai-went-global-gated-rollout-paid-plans-tbd-16j0). An Israeli-focused vendor guide says it is waitlisted, not all languages are supported, and the agent language follows the business phone number. — [ariko.ai](https://ariko.ai/en/guide/whatsapp-bot-small-business)
- Pricing: small businesses get it through select tiers of **WhatsApp Business Premium** (tiers unpublished), and large businesses pay **by token usage**. — [omnichat.ai](https://blog.omnichat.ai/meta-business-agent-platform-explained-features-pricing-and-what-the-2026-whatsapp-changes-mean-for-your-business/). Token pricing is reported to start Aug 1, 2026 ([Business Today](https://www.businesstoday.in/technology/artificial-intelligence/story/whatsapp-introduces-token-based-pricing-for-ai-agents-from-august-1-540699-2026-07-03)), and one blog cites $2.00 per 1M tokens ([respond.io blog](https://respond.io/ar/blog/meta-business-agent-pricing.md)). Outlook Business framed the pricing update as one that "favours Meta over third-party chatbots". — [Outlook Business](https://www.outlookbusiness.com/corporate/whatsapp-pricing-update-favours-meta-over-third-party-chatbots)
- Policy: since **Jan 15, 2026**, WhatsApp Business API terms bar **general-purpose** AI chatbots (ChatGPT, Perplexity and similar). Business-specific bots remain allowed. Where regulators require access, Meta charges such bots. — [TechCrunch](https://techcrunch.com/2025/10/18/whatssapp-changes-its-terms-to-bar-general-purpose-chatbots-from-its-platform/); [Neowin](https://www.neowin.net/news/meta-to-begin-charging-for-third-party-ai-chatbots-on-whatsapp-for-some-users/)

**Israel and Hebrew status of Meta AI products**
- **Meta AI (consumer assistant) launched in Israel with Hebrew in June 2026** on WhatsApp, meta.ai, desktop and mobile. — [Ynetnews](https://www.ynetnews.com/tech-and-digital/article/rk008bxwxge); [Yeshiva World](https://www.theyeshivaworld.com/news/israel-news/2569498/meta-ai-arrives-in-israel-hebrew-support-and-whatsapp-integration-officially-launches.html)
- Meta's newer **Muse** assistant is **not available in Israel** (US and Canada only, with no expansion date). — [platindigital.net](https://platindigital.net/en/blog/meta-muse/)
- Shopify's **Campaign Autopilot** (free; plans and runs Meta ads, can create an ad account) is a platform-native substitute for Shopify merchants. It is in early access, and Shop Campaigns is US/CA only. — [Shopify blog](https://www.shopify.com/in/blog/introducing-campaign-autopilot); [techwyse.com](https://www.techwyse.com/news/platform-updates/shopify-campaign-autopilot-ai-marketing-tool-launch)

### Inferences
- Meta is the #1 competitor. Its AI is free, embedded where advertisers already work, and improving quarterly. Marta should position as the **Hebrew-first, cross-surface "operator" layer** that is simpler than Ads Manager and its English-centric assistant. It should treat Meta's own tools (Advantage+, Business Agent) as things Marta configures and explains, not things it competes against.
- The Hebrew gap in Meta's business tools could close quickly. Meta AI already speaks Hebrew for consumers in Israel, and the business assistant is expanding "local languages" across EMEA. Marta's Hebrew advantage could be temporary, likely 6–18 months (speculative). Durable advantages must also include local know-how (Israeli market playbooks, ILS billing, Hebrew support people), WhatsApp + ads orchestration, and trust and guardrails.
- Meta's API churn (legacy ASC/AAC cutoffs, v26 removals) and its new "ads MCP server rules" are a platform risk for any third-party agent. Building on Meta's official MCP/CLI may lower maintenance cost but caps differentiation.

### Gaps
- No primary Meta source was found that lists the languages for the AI Business Assistant, the Business Agent or the GenAI ad text tools, so **Hebrew support for Meta's business AI is unconfirmed either way**. Israel eligibility for the Business Agent and the WhatsApp Business Premium tiers in Israel are also unconfirmed.
- The exact Q3 2026 Advantage+ run-rate was not found; only the Q2 2026 figure of >$75B.
- It is unclear whether WhatsApp's token-based AI pricing applies only to Meta's Business Agent or also to third-party AI bots via BSPs.
- Whether Meta has hit its "fully automated by end-2026" goal is not established. Agentic features were still "in testing" as of Oct–Nov 2026.

## 3. WhatsApp-marketing SaaS with AI (Wati, Respond.io, Gupshup, Interakt, AiSensy, Zoko, Twilio, Trengo, Manychat, Chatfuel, SleekFlow, 360dialog): pricing, Hebrew/RTL, Israel presence

### Takeaway
WhatsApp SaaS pricing clusters at about **$59–$159/month entry or mid tiers and about $279–$349/month top self-serve tiers**. Meta's per-message fees are passed through, sometimes with markups (0% to about 20%), and AI agents are increasingly sold as add-ons or credits. Only **respond.io** has documented Hebrew UI with RTL. Manychat users were still requesting RTL in 2025. Israeli commentary says global platforms treat Hebrew "as an afterthought", which leaves room for local Israeli WhatsApp-bot vendors. None of these platforms manages Meta Ads campaigns or audiences.

### Cited Findings
**Meta's WhatsApp rates in Israel (the pass-through cost floor)**
- Israel: **marketing $0.0353 per delivered message**; utility, authentication and service $0.0053 each. Marketing gets no volume discount. — [formbeep.com (Nov 2026)](https://formbeep.com/whatsapp-api-pricing/); [srileo.com Israel calculator](https://srileo.com/tools/whatsapp-api-pricing-calculator/israel/)
- Structural change on Oct 1, 2026: service replies are charged after 1,000 free per month. The Jul 1, 2026 rate update reportedly did not change Israel. — [edna.io](https://edna.io/resources/whatsapps-new-pricing-structure-what-will-be-charged-starting-october-1-2026/); [sleekflow.io](https://sleekflow.io/en-us/blog/whatsapp-business-price)

**Wati**
- Growth $59 and Pro $119/month on annual billing ($69 and $149 monthly). Business was cut from $349 to **$279/month on May 7, 2026**. — [eesel.ai](https://www.eesel.ai/blog/wati-pricing); [costbench.com changelog](https://costbench.com/changelog/wati-price-decrease-2026-05/)
- Messages carry an estimated **~20% markup over Meta rates** (third-party estimate). — [costbench.com](https://www.costbench.com/software/live-chat/wati/)
- **Astra** AI agent is a separate product: Free / $99 / $399 per month. The Growth plan includes 1 Astra agent. Bundles are India-only. — [sleekflow.io (Astra review)](https://sleekflow.io/blog/wati-astra-ai-review.md); [Wati support](https://support.wati.io/en/articles/17565154-understanding-wati-and-astra-bundle-plans-and-ai-credits)
- About $35M total funding, including a Series B led by Tiger Global and Shopify. — [getmanifest.ai](https://blog.getmanifest.ai/best-whatsapp-automation-tools-ecommerce/). A competitor claims Wati has "over 10,000 customers in 160+ countries". — [wanotifier.com](https://wanotifier.com/?p=3529)

**Respond.io (Malaysia)**
- **$62.5M Series B on June 16, 2026**, led by Camber Partners with Endeavor Catalyst. About $69.5M raised in total. Funds are earmarked for North America and Europe expansion and M&A. — [Pulse 2.0](https://pulse2.com/respond-io-raises-62-5-million-series-b-to-expand-ai-powered-customer-conversation-platform/amp/); [SaaSRise](https://www.saasrise.com/news/respondio-secures-625m-series-b-to-accelerate-ai-messaging-platform-909a2fab-459d-4695-8cac-1ff13076c8dd)
- Starter $79, Growth $159, Advanced $279/month (annual); $99, $199 and $349 monthly. Billing is per Monthly Active Contact. **AI Agents require Growth or higher** and consume AI credits. — [eesel.ai](https://www.eesel.ai/blog/respond-io-pricing); [chatarmin.com](https://chatarmin.com/en/blog/respond-io-pricing)
- **Hebrew is an available platform language and switches the UI to RTL** (changelog, undated). — [respond.io roadmap](https://roadmap.respond.io/changelog/multiple-languages-now-available-on-respondio)

**Manychat (IG/FB/WA DM automation)**
- About **$163M raised** in total. Its 2025 raise is tied to a push into paid AI. — [Voiceflow](https://www.voiceflow.com/articles/manychat)
- New pricing model from **Mar 2, 2026**, with plans from $0 to $199/month. G2 lists a $15 entry. AI is reported as a ~$29/month add-on, though sources conflict on whether it is included in Pro. WhatsApp fees are billed on top. — [Tidio](https://www.tidio.com/blog/manychat-review/); [chatbot.com](https://www.chatbot.com/blog/manychat-pricing/); [G2](https://www.g2.com/products/manychat/pricing); [hackceleration](https://hackceleration.com/labs/manychat-pricing); [chatarmin.com](https://chatarmin.com/en/blog/manychat-pricing)
- A Feb 2025 community request says Manychat **lacks RTL support for Hebrew/Arabic**, particularly in email. No evidence was found that it has shipped. — [Manychat community](https://community.manychat.com/ideas/urgent-request-add-right-to-left-rtl-support-for-hebrew-arabic-5124)

**SleekFlow, AiSensy, Interakt, Zoko, Gupshup**
- SleekFlow uses flat monthly tiers priced by contacts. AI-agent credits are billed per AI reply with no published rate. It positions itself as "AI agent first" against Gupshup's "API infrastructure". — [eesel.ai](https://www.eesel.ai/blog/sleekflow-pricing); [sleekflow.io](https://sleekflow.io/en-us/blog/sleekflow-vs-gupshup)
- AiSensy is quoted at Free / $45 / $99, or $72–80/month for paid plans; the sources conflict. It ranks **#1 WhatsApp BSP in India with a 7.4% share (FY26)**. — [hyperleap.ai](https://hyperleap.ai/comparison/best-whatsapp-automation-tools-2026); [prospeo.io](https://prospeo.io/s/wati-alternatives); [richautomate.in](https://richautomate.in/research/state-of-whatsapp-bsp-india-q2-2026)
- Interakt: Growth plan about ₹2,499/month (~$30). Backed by Jio Haptik/Reliance and India-focused. — [wiserreview.com](https://wiserreview.com/blog/interakt-alternatives/); [bot.space](https://www.bot.space/blog/best-interakt-alternatives)
- Gupshup: Fidelity marked its stake to about **$278M valuation (Jan 31, 2026), more than 80% below the $1.4B of 2021**. It raised $60M+ (led by Globespan and EvolutionX Debt; a little over half equity). Layoffs are reported at about 200 or about 500 (the company disputes this). It is pivoting to domain agents on its own ACE LLM. — [letsdatascience](https://letsdatascience.com/news/fidelity-cuts-gupshup-valuation-to-278-million-47aa4911); [exchange4media](https://www.exchange4media.com/digital-news/gupshup-valuation-falls-sharply-as-fidelity-cuts-stake-value-153545.html); [MIT Sloan ME](https://www.mitsloanme.com/?p=7804); [HRKatha](https://www.hrkatha.com/news/gupshup-lays-off-200-employees-amid-second-restructuring/); [Inc42](https://inc42.com/buzz/exclusive-saas-unicorn-gupshup-fires-500-employees)

**API/BSP layer (markup models)**
- Twilio: **$0.005 per message** platform fee (inbound and outbound) plus Meta fees, with no monthly fee. One table instead says a +20% markup. — [Telnyx (Oct 2026)](https://telnyx.com/resources/best-whatsapp-api-provider); [dev.to](https://dev.to/david_friedman_c2808375c1/whatsapp-business-api-pricing-2026-conversations-fees-and-hidden-costs-kk4)
- 360dialog: **zero per-message markup**, with a monthly fee per number (about €49/month per a third party). — [360dialog pricing](https://360dialog.com/pricing); [ezcontact.ai](https://ezcontact.ai/en/blog/whatsapp-api-pricing-comparison-meta-twilio-360dialog-ezcontact/)
- Chatfuel: **Meta rate +10%**, per its own blog. — [Chatfuel blog](https://sdk.chatfuel.com/blog/whatsapp-business-api-pricing)

**Israel market context**
- A Times of Israel blog maps three "lanes". Global platforms (ManyChat, WATI, Respond.io) have "English-first interfaces, ticket-based support in a different time zone, and Hebrew treated as an afterthought". Israeli self-serve tools with Hebrew interfaces include AllChat, ZapClick, WBSender and SmartRise. — [Times of Israel blogs](https://blogs.timesofisrael.com/israels-whatsapp-bot-market-mapped/)
- Gambot is listed as an official Meta partner with a Hebrew interface, alongside Connectop and others priced in ILS. — [danaiapp.org](https://danaiapp.org/en/blog/whatsapp-bot-comparison-israel)
- New entrant: **Wassist** (London) raised a **$1.1M pre-seed (June 2026, led by Playfair)** for no-code WhatsApp commerce AI agents. — [TechFundingNews](https://techfundingnews.com/openai-wants-shopping-in-chatgpt-wassist-raises-1-1m-to-keep-it-on-whatsapp/)

### Inferences
- These tools compete with Marta's WhatsApp leg (broadcasts, inbox, AI replies) but not with its Meta Ads, Audiences or Pixel leg. An Israeli SMB today would need two or three tools (e.g., Madgicx or Ads Manager, plus Wati or an Israeli WA bot, plus a CRM). A single Hebrew agent spanning these is the clearest whitespace.
- Price anchors for the WhatsApp leg: about $60–$160/month for SMB, and about $280–$350/month for "business" tiers, plus Meta fees. In Israel, 1,000 marketing messages cost about $35 in Meta fees alone ($0.0353 × 1,000). AI add-ons add $29 (Manychat) to $99–$399 (Wati Astra).
- Gupshup's >80% markdown and layoffs suggest pure WhatsApp-API infrastructure is commoditizing, while the AI-agent and orchestration layer (respond.io's $62.5M) is where capital is flowing.

### Gaps
- No Hebrew/RTL information was found for Wati, SleekFlow, AiSensy, Interakt, Zoko, Trengo, Gupshup, Twilio, Chatfuel or 360dialog.
- No information was found on Israeli offices or resellers for any global WhatsApp SaaS.
- No verified 2026 pricing was found for Zoko, Trengo or Gupshup (Gupshup is per-message, contact-sales).
- No reliable 2026 customer counts were found for Wati, AiSensy, Interakt or Zoko.

## 4. All-in-one SMB marketing suites with AI and Meta integration (HubSpot, GoHighLevel, Wix, Shopify, Klaviyo, Hootsuite/Sprout): overlap

### Takeaway
GoHighLevel comes closest to Marta's bundle (Meta ad manager, WhatsApp, an AI "Employee", CRM) but is English-first and agency or reseller oriented. Wix is the Hebrew-native exception, with Hebrew help, Facebook/Instagram Ads inside the dashboard, and an AI Marketing Agent; it is limited to Wix sites. Shopify, Klaviyo and HubSpot each cover a slice (ads autopilot, WhatsApp marketing, AI service agent), and none was found to manage Meta Ads conversationally plus WhatsApp in Hebrew.

### Cited Findings
- **GoHighLevel**: plans at $97, $297 and $497/month. WhatsApp costs about $10/month per sub-account plus Meta fees. "AI Employee" costs $50 or $97/month per sub-account, or pay per use. Usage (SMS, email, AI) is billed on top. — [Apexure (Sep 2026 pricing page summary)](https://www.apexure.com/blog/gohighlevel-pricing); [TimelinesAI](https://timelines.ai/gohighlevel-whatsapp-pricing); [omidsaffari.com](https://omidsaffari.com/blog/gohighlevel-pricing)
- **HubSpot Breeze**: the Customer Agent moved to outcome-based pricing in April 2026, at about **$0.50 per resolved conversation**. It requires Pro or Enterprise tiers (Service Hub seats from $50/month). Credit packs start at $45/month for 5,000 credits. — [myaskai.com](https://myaskai.com/blog/hubspot-breeze-ai-agent-complete-guide-2026); [eesel.ai](https://www.eesel.ai/blog/hubspot-ai-pricing). There is a long-standing community request for RTL rich text in HubSpot. — [HubSpot Community](https://community.hubspot.com/t5/HubSpot-Ideas/RTL-right-to-left-amp-amp-rich-text-functionality/idc-p/243752)
- **Klaviyo**: WhatsApp became a native channel (two-way chat, campaigns, flows, reporting) in a Sep 2025 launch. Its "Customer Agent" now covers WhatsApp, and the "Composer" campaign agent is listed as GA (Sep 2026 page). Meta does not support WhatsApp marketing messages to US numbers. — [Klaviyo blog](https://www.klaviyo.com/blog/klaviyo-whatsapp-product-launch); [Klaviyo AI blog](https://www.klaviyo.com/blog/klaviyo-ai-for-autonomous-marketing-and-customer-service); [Klaviyo WhatsApp page](https://www.klaviyo.com/products/whatsapp)
- **Wix** (Hebrew help centre):
  - The **AI Marketing Agent** covers SEO, social, email and paid ads (it lists Google Ads campaign optimization) and runs on AI credits included in Premium plans (about 150/200/300 actions for Light/Core/Business).
  - **Facebook & Instagram Ads** are run from the Wix dashboard with Wix's AI targeting tool.
  - The third-party AdScale app on the Wix App Market claims "100+ AI agents" running Google and Meta ads.
  
  — [Wix Help (Hebrew) – AI Marketing Agent](https://support.wix.com/he/article/ai-tools-about-the-ai-marketing-agent); [Wix Help (Hebrew) – AI credits](https://support.wix.com/he/article/מידע-על-קרדיטים-ל-ai); [Wix Help (Hebrew) – FB/IG Ads overview](https://support.wix.com/he/article/facebook-instagram-ads-סקירה-כללית); [Wix App Market – AdScale](https://www.wix.com/app-market/adscale-google-ads-shopping)
- **Shopify**: Campaign Autopilot is free and plans and runs Meta, Microsoft, Shop and email campaigns (early access). Shopify Audiences exports audiences to Meta. One vendor reports higher CPMs and modest gains from Audiences. — [ContentGrip](https://www.contentgrip.com/shopify-campaign-autopilot/); [Lebesgue](https://lebesgue.io/facebook-ads/can-shopify-audience-improve-your-meta-ads)
- **SleekFlow vs GoHighLevel**: SleekFlow publishes head-to-head pages, indicating the WhatsApp-SaaS and all-in-one CRM categories overlap. — [sleekflow.io](https://sleekflow.io/blog/sleekflow-vs-gohighlevel)

### Inferences
- For Israeli SMBs already on Wix, Wix's Hebrew-native Facebook/Instagram Ads plus AI Marketing Agent is a meaningful substitute for the "easy Meta ads in Hebrew" promise, though not for WhatsApp Business Platform or Pixel/CAPI depth. (Wix being Israeli-founded is not sourced here.)
- GoHighLevel sets the agency price anchor: $97–$497/month base plus about $10 for WhatsApp plus about $97 for an AI Employee per client. That is a natural reference point if Marta sells to Israeli agencies.

### Gaps
- No 2026 data was found on Hootsuite (OwlyGPT) or Sprout Social AI pricing or Meta-ads features.
- No HubSpot Breeze WhatsApp or Meta-ads agent was found.
- It is unverified whether GoHighLevel's "Ask AI" can now create Meta campaigns conversationally (one summary claimed it; no source was attributable).
- No Hebrew/RTL status was found for GoHighLevel, Klaviyo or Shopify admin AI.

## 5. Category momentum: funding, acquisitions and launches in 2025–2026; failures and shutdowns

### Takeaway
Momentum is strong but consolidating toward platforms. Meta absorbed agent tech (Manus, $2B+ reported) and shipped free native agents and an official MCP. Capital went to messaging-AI orchestration (respond.io $62.5M) and agentic marketing services (Mega, Runable, Cuttable, Different). Point-tool creative startups were acquired (AdCreative.ai by Appier for $38.7M; Pencil by Brandtech; Trapica reportedly folded into Pencil). The clearest distress signal is Gupshup's >80% valuation markdown. No clean "AI Meta-ads agent shut down" story was found; the main risk for third-party tools is Meta's API and policy changes.

### Cited Findings
- **Meta acquires Manus** (announced Dec 29, 2025; $2B+ reported) and puts it in Ads Manager by Feb 2026. — [SBC News](https://sbcnews.co.uk/technology/2026/01/02/meta-acquires-ai-start-up-manus/); [Search Engine Land](https://searchengineland.com/meta-adds-manus-ai-tools-into-ads-manager-469410)
- **Meta Ads AI Connectors (MCP/CLI)** on Apr 29, 2026; **AI Business Assistant global** on Apr 24, 2026; **Business Agent global** on Jun 3, 2026; agentic Ads Manager tests in Oct 2026. — sources in §1–2 above ([usecarly](https://www.usecarly.com/blog/meta-ads-mcp/); [MediaPost](https://www.mediapost.com/publications/article/414547/meta-rolls-out-ai-business-assistant-to-all-advert.html); [Business Today](https://www.businesstoday.in/technology/artificial-intelligence/story/meta-unveils-ai-business-agent-platform-for-whatsapp-instagram-and-messenger-534739-2026-06-03))
- **Respond.io $62.5M Series B** (Jun 2026). — [Pulse 2.0](https://pulse2.com/respond-io-raises-62-5-million-series-b-to-expand-ai-powered-customer-conversation-platform/amp/)
- **Appier acquires AdCreative.ai** for $38.7M (Feb 2025). — [FrenchWeb](https://www.frenchweb.fr/appier-acquiert-la-startup-francaise-adcreative-ai-pour-387-millions-de-dollars/451864)
- **Smartly acquires INCRMNTAL** (LOI Mar 2026). — [AdExchanger](https://www.adexchanger.com/measurement/smartly-is-planning-to-acquire-incrmntal-within-the-next-few-weeks/)
- **Mega** (Brooklyn, multi-agent AI service incl. paid ads) raised an $11.5M Series A in Mar 2026, led by Goodwater. — [CMO Tech](https://cmotech.uk/story/ai-startup-mega-raises-usd-11-5m-to-rival-ad-agencies)
- **Runable** (Bengaluru) raised a $21M Series A for agents that "run ad campaigns across search, social and AI chatbots". — [Dealroom](https://dealroom.co/news/147067-runable-raises-21m-series-a-to-push-ai-agents-past-building-into-growth/)
- **Cuttable** raised a $20M Series A (AI ads across Meta from brand assets), and "Different" raised a $48M seed, per Adweek Oct 2026 newsletter coverage (single source). — [Adweek](https://www.adweek.com/media/advertisers-pull-meta-ads-that-had-unwanted-ai-glow-ups/)
- **Gravity** raised $30.5M to place ads inside AI chatbots, an adjacent "ads in agents" trend. — [Dealroom](https://dealroom.co/news/143606-gravity-raises-30-5m-to-place-ads-inside-ai-chatbots/)
- PPC Land headline: "AI sales and marketing startups raised $3.7B globally in 2026" (not opened). — [ppc.land](https://ppc.land/ai-sales-and-marketing-startups-raised-3-7b-globally-in-2026/)
- **Wassist** $1.1M pre-seed (Jun 2026) for WhatsApp commerce agents. — [TechFundingNews](https://techfundingnews.com/openai-wants-shopping-in-chatgpt-wassist-raises-1-1m-to-keep-it-on-whatsapp/)
- **Distress and exits**:
  - Gupshup valuation was marked down more than 80% to about $278M, with reported layoffs. — [letsdatascience](https://letsdatascience.com/news/fidelity-cuts-gupshup-valuation-to-278-million-47aa4911)
  - Trapica was reportedly absorbed by Pencil and no longer runs standalone. — [theatdb.com](https://theatdb.com/companies/trapica)
  - Revealbot rebranded to Bïrch. — [superscale.ai](https://superscale.ai/alternatives/revealbot/pricing)
  - Albert was sold to Zoomd in 2022. — [PR Newswire](https://prnewswire.com/il/news-releases/zoomd-announces-the-acquisition-of-artificial-intelligence-marketing-platform-albert-301511595.html)
- **Platform-policy shocks**:
  - WhatsApp barred general-purpose AI chatbots on the Business API from Jan 15, 2026. — [TechCrunch](https://techcrunch.com/2025/10/18/whatssapp-changes-its-terms-to-bar-general-purpose-chatbots-from-its-platform/)
  - Legacy ASC/AAC campaigns were cut from the Marketing API after May 19, 2026, and v26 removals were enforced across all versions on Oct 27, 2026. — [segwise.ai](https://segwise.ai/blog/meta-ads-updates); [adadvisor.ai](https://adadvisor.ai/blog/meta-ads-updates-2026)
  - An unverified blog claims Meta flags some external AI tools that connect to the Ads API as unauthorized. — [dashactivateonline.net](https://dashactivateonline.net/meta-ai-ad-accounts-shut-down-ecommerce/)

### Inferences
- The "AI layer over Meta" category is real and funded, but Meta keeps moving up the stack: free assistant, free MCP, Business Agent. Standalone "chat with Meta Ads" startups face margin compression. Survivors differentiate on vertical or geographic focus, multi-platform reach (Ryze, Pipeboard), or services-plus-AI (Mega).
- A localized (Hebrew), cross-surface SMB agent fits the pattern of regional winners such as respond.io (SEA) and AiSensy/Interakt (India), which won on local go-to-market rather than unique technology.

### Gaps
- No explicit 2025–2026 shutdown of a Meta-ads AI agent startup was found.
- Fluency's $40M Series A was mentioned without a source URL or date.
- Cuttable's and Different's details come from a single newsletter summary.

## 6. Pricing models and price anchors (SMB vs agency), plus the comparison table

### Takeaway
Five pricing models dominate:
1. **Flat SaaS tiers scaled by ad spend** (Madgicx, Bïrch, Optmyzr, about $45–$899/month).
2. **Per-ad-account flat fees** (AdAmigo $99/$349; Pipeboard slots).
3. **% of ad spend** for enterprise (Smartly 2–5%, with $4–5K/month minimum).
4. **Per-seat or contact-tiered messaging SaaS plus Meta message fees with 0–20% markup** (Wati, respond.io, Twilio $0.005/msg, Chatfuel +10%).
5. **Usage or outcome pricing for AI** (credits, $0.50 per resolution, tokens).

Meta's native AI is $0, which sets the reference ceiling for "basic" automation.

### Cited Findings
- Spend-tiered SaaS: Madgicx from $45 ([madgicx.com/llm-info](https://madgicx.com/llm-info)); Bïrch $45–$99 ([superscale.ai](https://superscale.ai/alternatives/revealbot/pricing)); Optmyzr $209–$899 ([tryatria.com](https://www.tryatria.com/blog/optmyzr-pricing))
- Per-account: AdAmigo $99/$349 ([admanage.ai](https://admanage.ai/compare/adamigo-alternative)); Pipeboard extra slot $10/month ([adkit.so](https://adkit.so/alternatives/pipeboard/pricing))
- Flat AI-agent subscription: Ryze $89/month ([get-ryze.ai](https://www.get-ryze.ai/pricing))
- % of spend: Smartly 3–5% (some 2%), minimum about $4–5K/month ([superscale.ai](https://superscale.ai/alternatives/smartly/pricing); [hunchads.com](https://hunchads.com/blog/smartly-pricing))
- Messaging pass-through and markup: Wati about +20% (est.) ([costbench](https://www.costbench.com/software/live-chat/wati/)); Twilio $0.005/msg ([Telnyx](https://telnyx.com/resources/best-whatsapp-api-provider)); 360dialog 0% markup plus a per-number fee ([360dialog](https://360dialog.com/pricing)); Chatfuel +10% ([Chatfuel](https://sdk.chatfuel.com/blog/whatsapp-business-api-pricing)); GHL $10/sub-account plus Meta fees ([TimelinesAI](https://timelines.ai/gohighlevel-whatsapp-pricing))
- AI usage and outcome pricing: HubSpot $0.50 per resolved conversation ([myaskai.com](https://myaskai.com/blog/hubspot-breeze-ai-agent-complete-guide-2026)); respond.io AI credits ([chatarmin.com](https://chatarmin.com/en/blog/respond-io-pricing)); Meta Business Agent tokens or Premium tiers ([omnichat.ai](https://blog.omnichat.ai/meta-business-agent-platform-explained-features-pricing-and-what-the-2026-whatsapp-changes-mean-for-your-business/)); Wix AI credits per plan ([Wix Help](https://support.wix.com/he/article/מידע-על-קרדיטים-ל-ai))
- Native free: Meta AI Business Assistant at no extra cost ([MediaPost](https://www.mediapost.com/publications/article/414547/meta-rolls-out-ai-business-assistant-to-all-advert.html)); Meta MCP with no separate charge ([contextbolt.com](https://contextbolt.com/blog/meta-ads-mcp/)); Shopify Campaign Autopilot free ([ContentGrip](https://www.contentgrip.com/shopify-campaign-autopilot/))

### Inferences
- **SMB anchor for an AI Meta-ads agent: about $50–$100/month.** Adding WhatsApp plus an AI agent typically brings a stack to about $150–$250/month before message fees. Agency anchor: about $200–$500/month, or per-client add-ons of about $50–$100. A Hebrew-first bundle (ads + WA + AI) priced at about ₪249–₪499/month for SMB would sit inside the global anchors. (The ILS range is an illustrative inference, not sourced; it needs an FX rate and Israeli willingness-to-pay data.)
- % of spend fits large accounts only. For Israeli SMBs with low monthly spend, flat tiers dominate. Message fees should be passed through transparently, since markups are visible and benchmarked.

### Gaps
- No Israel-specific (ILS) pricing was found for any global vendor.
- It is not known whether any global vendor localizes pricing for Israel or bills in ILS.

### Comparison table
Legend: Y = yes / documented; P = partial; N = no / not found; ? = unknown. HQ marked † is general knowledge, not sourced in this pass. Prices are USD/month as reported by third parties unless noted.

| Name | HQ | Category | Meta Ads mgmt | Audiences (custom/LAL) | WhatsApp | Conversational AI agent | Hebrew / RTL | Pricing (reported) | Funding / traction | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| Meta AI Business Assistant (+Manus) | Menlo Park† | Native platform AI | Y (analysis; agentic edits in testing Oct 2026) | P (AI audience discovery in testing) | N (separate product) | Y | ? Hebrew not listed | Free | Advantage+ E2E >$75B run-rate (Q2'26); ~10M advertisers used GenAI tools Q3'26 | [MediaPost](https://www.mediapost.com/publications/article/414547/meta-rolls-out-ai-business-assistant-to-all-advert.html) |
| Meta Ads MCP / CLI (official) | Menlo Park† | Official LLM connector | Y (29 tools) | ? | N | Via Claude/ChatGPT | Depends on LLM | Free (plus LLM plan) | Open beta Apr 29, 2026 | [usecarly](https://www.usecarly.com/blog/meta-ads-mcp/) |
| Meta Business Agent (WA/IG/Messenger) | Menlo Park† | Native messaging AI agent | N | N | Y | Y | ? (language follows phone #; unconfirmed) | WA Business Premium tiers / tokens (~$2/1M tokens, unverified) | 1M+ businesses at launch (Jun 2026) | [Business Today](https://www.businesstoday.in/technology/artificial-intelligence/story/meta-unveils-ai-business-agent-platform-for-whatsapp-instagram-and-messenger-534739-2026-06-03) |
| Madgicx | Herzliya, IL | AI Meta-ads suite | Y | Y (audience tools) | N | Y (AI Marketer + AI Chat) | N found | From $45 (spend-tiered); Pro $99 | Funding conflicting (PeakSpan; $1–6.8M); ~50 staff | [madgicx llm-info](https://madgicx.com/llm-info) |
| AdAmigo.ai | ? | Chat-first Meta ads agent | Y | ? | N | Y | N found | $99 Entry / $349 Unlimited per ad account | n/f | [admanage.ai](https://admanage.ai/compare/adamigo-alternative) |
| Ryze AI | Meow AI LLC (loc. ?) | Multi-platform ads agent + MCP | Y | ? | N | Y (+150-tool MCP) | N found | $89 | Bootstrapped (self-described) | [get-ryze.ai](https://www.get-ryze.ai/pricing) |
| Bïrch (ex-Revealbot) | ? | Rules + AI chat for Meta | Y (edit, not create) | ? | N | P (chat can't create campaigns) | N found | $45–$99 (spend-tiered) | n/f | [madgicx review](https://madgicx.com/compare/birch-review) |
| Pipeboard | ? | Meta Ads MCP (source-available) | Y (31 tools reported) | ? | N | Via LLM | Depends on LLM | Free; ~$29–$199 | 1,000+ users; $100M+/mo spend (self-reported) | [pipeboard.co](https://pipeboard.co/) |
| Smartly | Helsinki† | Enterprise creative/media automation | Y | Y | N | P | N found | 2–5% of spend; min ~$4–5K | Providence-owned; ~$101M rev (Latka) | [superscale.ai](https://superscale.ai/alternatives/smartly/pricing) |
| AdCreative.ai (Appier) | Paris | GenAI ad creative | P (creative) | N | N | N | N found | $39 / $249 (stale?) | Acquired for $38.7M (2025) | [FrenchWeb](https://www.frenchweb.fr/appier-acquiert-la-startup-francaise-adcreative-ai-pour-387-millions-de-dollars/451864) |
| Pencil (Brandtech) | London† | GenAI ad creative | P | N | N | N | N found | From $14 | Acquired by Brandtech | [AdExchanger](https://adexchanger.com/ai/the-brandtech-group-snatches-up-generative-ai-ad-platform) |
| Marpipe | ? | Creative testing | P | N | N | N | N found | $199–$999 | n/f | [pricingsaas](https://pricingsaas.com/companies/marpipe) |
| Optmyzr | ? | PPC optimization (Google-first) | P (disputed) | ? | N | P (Sidekick) | N found | $209–$899 | n/f | [tryatria](https://www.tryatria.com/blog/optmyzr-pricing) |
| Adzooma | ? | PPC optimization | Y | ? | N | N | N found | Free tier | n/f | [Capterra](https://www.capterra.co.uk/software/188236/adzooma) |
| Albert.ai (Zoomd) | ? | Autonomous enterprise media | Y | ? | N | P | N found | Enterprise | Acquired by Zoomd 2022 | [PR Newswire](https://prnewswire.com/il/news-releases/zoomd-announces-the-acquisition-of-artificial-intelligence-marketing-platform-albert-301511595.html) |
| Zocket | India | SMB Meta-ads agents | Y | Y (audience agent) | N | Y | N found | n/f | $3M seed (Kalaari) | [Inc42](https://inc42.com/buzz/adtech-startup-zocket-bags-3-mn-from-kalaari-capital-to-help-smbs-optimise-ad-spends) |
| Wati (+Astra) | ? | WhatsApp SaaS + AI agent | N | N | Y | Y (Astra) | N found | $59/$119/$279 + ~20% msg markup; Astra $99–$399 | ~$35M raised; claims 10k+ customers | [eesel.ai](https://www.eesel.ai/blog/wati-pricing) |
| Respond.io | Malaysia | Omnichannel messaging + AI agents | N | N | Y | Y (Growth+) | **Y (Hebrew UI, RTL)** | $79/$159/$279 annual ($99/$199/$349 monthly) | $62.5M Series B (Jun 2026) | [respond.io changelog](https://roadmap.respond.io/changelog/multiple-languages-now-available-on-respondio) |
| Manychat | ? | IG/FB/WA DM automation | N | N | Y | P (AI add-on ~$29) | **N (RTL requested 2025)** | $0–$199 + AI add-on + WA fees | ~$163M raised | [Voiceflow](https://www.voiceflow.com/articles/manychat) |
| SleekFlow | Hong Kong† | Omnichannel + AI agent | N | N | Y | Y | N found | Contact-tiered; AI credits per reply | n/f | [eesel.ai](https://www.eesel.ai/blog/sleekflow-pricing) |
| AiSensy | India | WhatsApp marketing SaaS | N | N | Y | P | N found | Free / $45 / $99 (conflicting) | #1 India BSP, 7.4% share FY26 | [richautomate](https://richautomate.in/research/state-of-whatsapp-bsp-india-q2-2026) |
| Interakt (Jio Haptik) | India | WhatsApp commerce SaaS | N | N | Y | P | N found | ~₹2,499 (~$30) | Reliance-backed | [wiserreview](https://wiserreview.com/blog/interakt-alternatives/) |
| Gupshup | India | CPaaS + domain AI agents | N | N | Y | Y (ACE LLM) | N found | Per-message, contact sales | Valuation ~$278M (−80%); $60M+ raise | [letsdatascience](https://letsdatascience.com/news/fidelity-cuts-gupshup-valuation-to-278-million-47aa4911) |
| Twilio | US† | CPaaS/API | N | N | Y | N (build-your-own) | N found | $0.005/msg + Meta | Public co.† | [Telnyx](https://telnyx.com/resources/best-whatsapp-api-provider) |
| 360dialog | Berlin† | WhatsApp BSP/API | N | N | Y | N | N found | 0% markup; ~€49/number | n/f | [360dialog](https://360dialog.com/pricing) |
| Chatfuel | ? | Chatbot builder (WA/IG/FB) | N | N | Y | P | N found | Meta rate +10% on WA | n/f | [Chatfuel](https://sdk.chatfuel.com/blog/whatsapp-business-api-pricing) |
| Zoko / Trengo | ? | WhatsApp commerce / shared inbox | N | N | Y | ? | N found | n/f | n/f | (no reliable data found) |
| GoHighLevel | US† | All-in-one agency CRM | Y (Ad Manager) | ? | Y ($10/sub-acct) | Y (AI Employee $50–$97) | N found | $97/$297/$497 | n/f | [Apexure](https://www.apexure.com/blog/gohighlevel-pricing) |
| HubSpot Breeze | US† | CRM suite + AI agents | P (ads tool; no Meta agent found) | P | N found | Y (Customer Agent) | P (RTL rich-text long requested) | $0.50/resolved conv.; Pro/Ent required | Public co.† | [myaskai](https://myaskai.com/blog/hubspot-breeze-ai-agent-complete-guide-2026) |
| Klaviyo | US† | Email/SMS/WA CRM + AI agents | N (audience sync not verified) | ? | Y | Y (Customer Agent, Composer) | N found | n/f | Public co.† | [Klaviyo](https://www.klaviyo.com/blog/klaviyo-whatsapp-product-launch) |
| Wix | Israel† | Website builder + AI Marketing Agent | Y (FB/IG Ads in dashboard) | P (AI targeting) | N found | Y (AI Marketing Agent, Aria) | **Y (Hebrew help/UI)** | AI credits in Premium plans | Public co.† | [Wix Help (HE)](https://support.wix.com/he/article/ai-tools-about-the-ai-marketing-agent) |
| Shopify (Autopilot/Audiences) | Canada† | Commerce platform AI marketing | Y (Autopilot) | Y (Audiences export) | N | P (Sidekick) | N found | Autopilot free | Public co.† | [ContentGrip](https://www.contentgrip.com/shopify-campaign-autopilot/) |
| Hootsuite / Sprout | ? | Social management + AI | ? | ? | ? | ? | ? | n/f | n/f | (no 2026 data found) |
