<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg"/>
  <img src="assets/hero-light.svg" width="100%" alt="Harsh Vardhan Singh. AI Engineer, Backend and Distributed Systems, ML Research."/>
</picture>

<p align="center">
  <img src="https://img.shields.io/badge/University%20of%20Delhi-Faculty%20of%20Technology-1e3a8a?style=flat-square" alt="University of Delhi, Faculty of Technology"/>
  <img src="https://img.shields.io/badge/Based%20in-New%20Delhi-0891b2?style=flat-square" alt="Based in New Delhi"/>
  <img src="https://img.shields.io/badge/Open%20to-SDE%20%2F%20AI%20internships-16a34a?style=flat-square" alt="Open to SDE and AI internships"/>
</p>

<!-- Add contact links here, e.g.:
<p align="center">
  <a href="https://www.linkedin.com/in/YOUR-HANDLE"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:you@example.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
</p>
-->

I like the part of engineering where an idea becomes something real people can click on. Lately that means **AI agents with guardrails**: systems where the model reasons, but plain code enforces the rules, audits the output, and keeps things running when a dependency falls over.

**Short on time?** Jump to [the four projects to open first](#the-four-projects-to-open-first), or try a live demo: [Booking Agent](https://booking-agent-lemon.vercel.app) · [ReviveX](https://revive-x-ochre.vercel.app/)

---

## The journey so far

Three lines of work that started separately and are now converging. Read it left to right, then open any chapter for the code.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/journey-dark.svg"/>
  <img src="assets/journey-light.svg" width="100%" alt="Metro map of projects from 2024 to October 2026. The Systems line ends at the Distributed Rate Limiter. The Product and ML research lines meet at Booking Agent. Every project is listed in the chapters below."/>
</picture>

<details>
<summary><b>Chapter 1 · 2024: Learning the fundamentals</b></summary>
<br/>

Algorithms in five languages, a first portfolio, a first backend.

- **[sorting-algorithms](https://github.com/harshsuiiii/sorting-algorithms)**: classic sorts written in C, C++, Java, Python and JavaScript.
- **[twitter-backend](https://github.com/harshsuiiii/twitter-backend-project-deployment)**: a REST API replicating Twitter's core: tweets, likes, followers and full CRUD.
- **[portfolio](https://github.com/harshsuiiii/portfolio)**: where it all started.

</details>

<details>
<summary><b>Chapter 2 · 2025: Real-time and low-level</b></summary>
<br/>

Websockets and auth, then my first look at what happens below the framework.

- **[Real-time Chat](https://github.com/harshsuiiii/Real-time-chat-app)**: MERN and Socket.io chat with JWT auth, online presence and Zustand state.
- **[Matching Engine](https://github.com/harshsuiiii/LOW-LATENCY-TRADING-MATCHING-ENGINE-ORDERBOOK-)**: an exchange-style order book in TypeScript with price-time priority matching, market depth, and VWAP and mid-price quotes.
- **[Aurora DNS](https://github.com/harshsuiiii/aurora-DNS)**: a DNS server from scratch. Parses RFC 1035 packets from raw buffers, with TTL caching, upstream failover and a Pi-hole-style ad blocker.

</details>

<details>
<summary><b>Chapter 3 · Early 2026: Into ML research</b></summary>
<br/>

ML4SCI evaluation tasks for GSoC 2026 on CERN CMS detector data, plus applied deep-learning studies.

- **[Sparse NNs for CMS Jets](https://github.com/harshsuiiii/ML4SCI-Task-2d-Sparse-Neural-Networks-for-End-to-End-Event-Classification)**: a sparsity-aware ResNet that beats a dense CNN baseline by **+6.2 pp accuracy and +6.0 pp AUC** (87.5% and 0.933), then holds up under L1 pruning.
- **[Diffusion vs GAN vs VAE](https://github.com/harshsuiiii/ML4SCI-Diffusion-Models-for-Task-2e-Generative-Modelling-with-Diffusion-GAN-and-VAE)**: three generative models trained on sparse, heavy-tailed CMS jet images and compared with statistical tests.
- **[Fuzzy Pooling](https://github.com/harshsuiiii/Fuzzy_Neural_Network)**: ten CNN pooling strategies evaluated for Bitcoin price prediction, including four novel ones. Adaptive Attention Pooling came out on top.
- **[Customer Churn](https://github.com/harshsuiiii/customer_churn_prediction)**: a class-imbalance study comparing neural nets and tree ensembles, tuned for recall on churners.

</details>

<details>
<summary><b>Chapter 4 · Mid 2026: Putting LLMs inside real products</b></summary>
<br/>

Grounding, compliance and privacy treated as features, not afterthoughts.

- **[Self-Healing RAG](https://github.com/harshsuiiii/Self-healing-RAG)**: a LangGraph pipeline where a critic audits every answer claim by claim. Ungrounded answers trigger bounded query reformulation, then an honest fallback.
- **[legalsummary.ai](https://github.com/harshsuiiii/legalsummary.ai)**: plain-language summaries and clause analysis of legal documents on Next.js and Google Cloud, with PII redaction through Cloud DLP.
- **[OCR Semantic Grader](https://github.com/harshsuiiii/OCR-Semantic-Grader)**: TrOCR reads handwritten answers, Sentence-BERT scores them against model answers, and an agent re-checks borderline cases.
- **[BotForge](https://github.com/harshsuiiii/botforge-saas)**: multi-tenant SaaS to create, embed and monitor AI chatbots, with Google OAuth, AES-256-GCM token encryption, an SSE streaming widget and session analytics.
- **[ReviveX](https://github.com/harshsuiiii/ReviveX)**: a payment-recovery agent on Razorpay's APIs that works out *why* a payment failed and escalates retries under deterministic compliance rules. [Live demo](https://revive-x-ochre.vercel.app/)
- **[NetrAI / PrivAgent](https://github.com/chotushikari/NetrAI)** *(team project)*: a privacy-preserving browser agent that redacts PII on-device before anything reaches the AI.

</details>

<details open>
<summary><b>Chapter 5 · Now: Production-grade systems</b></summary>
<br/>

Typed, tested, observable, and designed to survive failure.

- **[Booking Agent](https://github.com/harshsuiiii/Booking-Agent)**: natural-language flight search for travel agents, with parallel multi-supplier search, normalised offers and human-confirmed booking. [Live demo](https://booking-agent-lemon.vercel.app)
- **[Distributed Rate Limiter](https://github.com/harshsuiiii/rate-limiter)**: one shared limit across N servers using atomic Redis Lua scripts, with four algorithms and a circuit breaker with local fallback when Redis degrades.

</details>

---

## The four projects to open first

<table>
<tr>
<td width="50%" valign="top">

### [Booking Agent](https://github.com/harshsuiiii/Booking-Agent)
Describe a trip in plain language. It searches several suppliers in parallel, normalises every result into one offer format, and prices it in INR with the agency's markup. Booking stays a separate, human-confirmed step.

**Engineering:** strict mypy, property-based tests with Hypothesis, Playwright for the web app, OpenTelemetry tracing.

<img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"/> <img src="https://img.shields.io/badge/Next.js%2016-000?style=flat-square&logo=nextdotjs" alt="Next.js 16"/> <img src="https://img.shields.io/badge/Postgres-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="Postgres"/> <img src="https://img.shields.io/badge/OpenTelemetry-425CC7?style=flat-square&logo=opentelemetry&logoColor=white" alt="OpenTelemetry"/>

[**Live demo →**](https://booking-agent-lemon.vercel.app) <sub>Uses simulated and sandbox fares.</sub>

</td>
<td width="50%" valign="top">

### [Distributed Rate Limiter](https://github.com/harshsuiiii/rate-limiter)
Every decision is one atomic Lua script, timed by the Redis clock, so replicas can't disagree and clock drift can't change limits. It stays up when Redis is slow or down.

**Proof:** 8 connections race 600 requests at a limit of 100, and exactly 100 are admitted for every algorithm.

<img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript"/> <img src="https://img.shields.io/badge/Fastify-000?style=flat-square&logo=fastify" alt="Fastify"/> <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" alt="Redis"/> <img src="https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white" alt="Prometheus"/>

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [ReviveX](https://github.com/harshsuiiii/ReviveX)
An AI agent for recovering failed payments. Gemini writes the message and the reasoning; plain TypeScript enforces the limits: 3 attempts at most, quiet hours from 21:00 to 08:00 IST, and a 60-minute gap between tries.

<img src="https://img.shields.io/badge/Next.js-000?style=flat-square&logo=nextdotjs" alt="Next.js"/> <img src="https://img.shields.io/badge/Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white" alt="Gemini"/> <img src="https://img.shields.io/badge/Razorpay-0C2451?style=flat-square&logo=razorpay&logoColor=white" alt="Razorpay"/>

[**Live demo →**](https://revive-x-ochre.vercel.app/)

</td>
<td width="50%" valign="top">

### [Sparse NNs for CMS Jets](https://github.com/harshsuiiii/ML4SCI-Task-2d-Sparse-Neural-Networks-for-End-to-End-Event-Classification)
A physics-motivated network for CERN detector data, where most cells record zero energy. It masks those empty cells so it learns only from real signal.

**Result:** 87.5% accuracy and 0.933 AUC, **+6.2 pp** and **+6.0 pp** over the dense baseline.

<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch"/> <img src="https://img.shields.io/badge/HEP-CMS%20%40%20LHC-1e3a8a?style=flat-square" alt="High energy physics, CMS at the LHC"/> <img src="https://img.shields.io/badge/ML4SCI-GSoC%202026%20task-0891b2?style=flat-square" alt="ML4SCI GSoC 2026 evaluation task"/>

</td>
</tr>
</table>

---

## Toolbox

Grouped by how recently I've shipped with it. Everything here appears in a repo above.

<table>
<tr><td width="24%"><b>Shipping with now</b></td><td>

<img src="https://skillicons.dev/icons?i=py,ts,fastapi,nextjs,react,tailwind,postgres,redis,supabase,docker,prometheus,gcp,vercel,githubactions&perline=14" alt="Python, TypeScript, FastAPI, Next.js, React, Tailwind, Postgres, Redis, Supabase, Docker, Prometheus, Google Cloud, Vercel, GitHub Actions"/><br/>
<img src="https://img.shields.io/badge/Fastify-000000?style=flat-square&logo=fastify&logoColor=white" alt="Fastify"/> <img src="https://img.shields.io/badge/Playwright-2EAD33?style=flat-square" alt="Playwright"/> <img src="https://img.shields.io/badge/Render-46E3B7?style=flat-square&logo=render&logoColor=black" alt="Render"/>

</td></tr>
<tr><td><b>AI &amp; ML</b></td><td>

<img src="https://skillicons.dev/icons?i=pytorch,sklearn,opencv&perline=14" alt="PyTorch, scikit-learn, OpenCV"/><br/>
<img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langchain&logoColor=white" alt="LangGraph"/> <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black" alt="Hugging Face"/> <img src="https://img.shields.io/badge/Vertex%20AI-4285F4?style=flat-square&logo=googlecloud&logoColor=white" alt="Vertex AI"/> <img src="https://img.shields.io/badge/ChromaDB-FF6B6B?style=flat-square" alt="ChromaDB"/> <img src="https://img.shields.io/badge/Groq%20%C2%B7%20Gemini%20%C2%B7%20OpenAI-412991?style=flat-square" alt="Groq, Gemini, OpenAI"/>

</td></tr>
<tr><td><b>Built with before</b></td><td>

<img src="https://skillicons.dev/icons?i=js,nodejs,express,mongodb,firebase,bun,vite,java,cpp,c,html,css&perline=14" alt="JavaScript, Node.js, Express, MongoDB, Firebase, Bun, Vite, Java, C++, C, HTML, CSS"/><br/>
<img src="https://img.shields.io/badge/Socket.io-010101?style=flat-square&logo=socketdotio&logoColor=white" alt="Socket.io"/> <img src="https://img.shields.io/badge/Razorpay-0C2451?style=flat-square&logo=razorpay&logoColor=white" alt="Razorpay"/>

</td></tr>
</table>

---

## On GitHub right now

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stats-dark.svg"/>
  <img src="assets/stats-light.svg" width="100%" alt="GitHub stats and top languages"/>
</picture>

**Latest pushes**

<!--START_SECTION:pushes-->
- `2026-11-07` **[Auto-Redteaming-Agent](https://github.com/harshsuiiii/Auto-Redteaming-Agent)**
- `2026-10-30` **[rate-limiter](https://github.com/harshsuiiii/rate-limiter)** — One shared limit across N servers, built on atomic Redis Lua scripts
- `2026-10-26` **[botforge-saas](https://github.com/harshsuiiii/botforge-saas)** — Multi-tenant SaaS to create, embed and monitor AI chatbots
- `2026-10-20` **[Booking-Agent](https://github.com/harshsuiiii/Booking-Agent)** — Natural-language flight search for travel agents
- `2026-08-30` **[ReviveX](https://github.com/harshsuiiii/ReviveX)** — AI payment-recovery agent with deterministic compliance rules
<!--END_SECTION:pushes-->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/harshsuiiii/harshsuiiii/output/github-snake-dark.svg"/>
  <img src="https://raw.githubusercontent.com/harshsuiiii/harshsuiiii/output/github-snake.svg" width="100%" alt="Contribution graph with an animated snake eating the green squares"/>
</picture>

<sub>Stats and pushes refresh daily through <a href=".github/workflows/profile.yml">a GitHub Action in this repo</a>. Languages exclude forks and notebook files.</sub>

---

<p align="center"><b>Open to SDE and AI-engineering internships, and research collaborations.</b><br/>If something here caught your eye, let's talk.</p>
