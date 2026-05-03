# LLM Zoomcamp launch / pre-course Q&A - structured FAQ

Source transcripts:

- Pre-course Q&A: https://www.youtube.com/watch?v=8lgiOLMMKcY
- Launch stream: https://www.youtube.com/watch?v=FgnelhEJFj0

These are the questions Alexey answered across the two streams, grouped by topic. The wording is paraphrased and de-duplicated. Items marked "logistics-generic" are candidates for the generic zoomcamp logistics docs; items marked "LLM-specific" belong in the LLM Zoomcamp section. Items marked "FAQ-only" are course-content questions best left to the public FAQ.

---

## Schedule and cohort

What is the official start date of the course?
- The 2025 cohort starts on Monday June 2, 2025. The launch stream airs one week earlier (May 27) because Alexey is travelling on the start date. Materials become accessible from launch-stream day, so participants can begin then if they want.
- Tag: logistics-generic / LLM-specific dates.

How long is the course?
- About 10 weeks: roughly two weeks for module 1, one week per subsequent module, and three weeks for the project. Last cohort ran from July to end of summer; the 2025 cohort starts in June and should finish by end of summer.
- Tag: LLM-specific.

Is the next cohort really running this year? I thought it was next year.
- Last cohort was 2024. The 2025 cohort runs this year, one year on from the previous edition.
- Tag: LLM-specific.

When does enrolment close?
- Registration stays open through the cohort. Sign up via the course GitHub repo's "sign up here" button.
- Tag: logistics-generic.

Can I start the course now / before the official start date?
- Yes. All content is on GitHub; module 1 and its homework are already published. Workshops from previous cohorts are also available.
- Tag: logistics-generic.

What are the steps for enrolling?
- 1. Go to the course GitHub repo, click "sign up here". 2. Show up for the launch stream. 3. Join the DataTalks.Club Slack and the Telegram channel. 4. Follow each module weekly: watch videos, do the homework, eventually submit a project for the certificate.
- Tag: logistics-generic.

What if I just discovered the course / can I still join mid-cohort?
- Yes. This is one of the most-asked questions and the entire flow is described in the cross-cohort logistics docs.
- Tag: logistics-generic.

---

## Curriculum and content changes vs last year

What changed in the curriculum since last year?
- Fewer modules. The "open source LLMs" module was removed and turned into a separate course (Open Source LLM Zoomcamp).
- The previous combined "evaluation and monitoring" module was split into two: a dedicated evaluation module (offline metrics for search and for the full RAG flow) and a dedicated monitoring module (production / online metrics).
- The orchestration module from the previous edition was removed.
- Monitoring tooling switched from Grafana to Phoenix (open-source, from Arize).
- Vector search tooling may switch from Elasticsearch to a different vendor depending on sponsor confirmation.
- Best practices module may receive updates from Timur.
- Tag: LLM-specific (whats-new).

How many modules will the course have?
- Five content modules (intro, vector search, evaluation, monitoring, best practices) plus a project. Optional workshop(s) sit alongside.
- Tag: LLM-specific.

What does the course actually teach (in plain words)?
- Building RAG (retrieval-augmented generation) applications: how to take a knowledge base, index it, retrieve relevant chunks for a user query, send them to an LLM as context, and return a grounded answer. Plus how to evaluate retrieval and the full RAG flow, monitor a deployed system, and apply best-practice techniques.
- Tag: LLM-specific.

Is RAG still relevant in 2025?
- Yes. A year ago RAG was the most common LLM application. Today many providers offer RAG out of the box, but it remains a strong illustrative use case and the focus of this edition. Future cohorts may shift focus.
- Tag: LLM-specific.

Will agentic AI / agents be part of the course?
- No, not in this edition. There may be a workshop on agentic workflows (driven by an external conference workshop Alexey is preparing) and possibly material on agentic search next year. The reasoning: agent tooling changes too fast right now to record stable course content; LLMs themselves stabilised before the LLM Zoomcamp launched, and the same wait-and-see approach applies to agents.
- Tag: LLM-specific.

Will the course cover MCP (Model Context Protocol)?
- No. Same reasoning as agents - too early, tools are still moving.
- Tag: LLM-specific.

Will the course cover LLMOps?
- Partially. The monitoring module covers what is effectively LLMOps for hosted LLMs (request/response monitoring, costs, response times). Deployment of self-hosted LLMs is covered in the separate Open Source LLM Zoomcamp.
- Tag: LLM-specific.

Will the course cover guardrails / generating metrics?
- Evaluation: yes. Generating metrics: yes. Guardrails: probably not in this edition.
- Tag: LLM-specific.

Will the course cover chunking?
- Basic chunking concepts are covered. Chunking strategies are something participants are encouraged to experiment with on their own and during the project.
- Tag: LLM-specific.

Will the course cover multimodal embeddings (images + text)?
- Not directly. The course teaches the basics of RAG so that multimodal extensions become a natural project addition.
- Tag: LLM-specific.

Will the course cover graph RAG, agentic RAG, etc?
- The course teaches fundamental RAG without frameworks. Once you understand the concepts you can apply them to graph RAG, agentic RAG, etc., or use a framework if you want.
- Tag: LLM-specific.

Will the course cover LangChain / LangGraph?
- LangChain may show up in the best-practices module (it was used in document re-ranking last year; not yet confirmed for this year). LangGraph for agents: no.
- Tag: LLM-specific.

Will the course cover image generation with LLMs?
- No. Use ChatGPT or similar tools directly if you want to generate images.
- Tag: LLM-specific.

Will the course cover GPU processing / distributed training?
- No. The course treats LLMs as black boxes and focuses on engineering RAG applications around hosted models.
- Tag: LLM-specific.

Will the course cover prompt engineering?
- Not in depth.
- Tag: LLM-specific.

Will the course cover fine-tuning?
- Not in this course. Fine-tuning will be covered in the separate Open Source LLM Zoomcamp.
- Tag: LLM-specific.

Will we build our own LLM?
- No. The course is about LLM (or AI) engineering: using existing hosted models to build applications. There are no plans for a build-your-own-LLM course; better courses already exist for that.
- Tag: LLM-specific.

Will we cover logging user prompts?
- Yes, in the monitoring module.
- Tag: LLM-specific.

Will we use any specific eval tool (Ragas, etc.)?
- No specific Ragas-style framework. The course uses classical IR metrics for retrieval (hit rate, MRR), LLM-as-a-judge for the full RAG flow, and ROUGE for some homework. Phoenix is used for monitoring. Once you know the concepts you can apply any tool.
- Tag: LLM-specific.

What is the difference between ML Zoomcamp and LLM Zoomcamp?
- ML Zoomcamp covers classical machine learning (with some look under the hood at how models work). LLM Zoomcamp covers building applications on top of hosted LLMs and treats the LLM itself as a black box. Different scope, different audience.
- Tag: LLM-specific.

Is the monitoring module similar to the one in MLOps Zoomcamp?
- The idea is the same (monitor a deployed system) but the metrics differ: in MLOps Zoomcamp you monitor an ML model; here you monitor request/response volume, response speed, and cost.
- Tag: LLM-specific.

Will this Open Source course be considered part of the main course / share grades?
- No. The Open Source LLM Zoomcamp is a separate course with separate certification.
- Tag: LLM-specific (open-source course pointer).

Will distributed training be covered in the Open Source course?
- No.
- Tag: LLM-specific (open-source course pointer).

---

## Prerequisites and audience

What are the prerequisites?
- Comfortable programming (any major language; Python preferred).
- Comfortable with the command line.
- Git basics.
- Docker installed and runnable.
- No machine-learning background required. No advanced math required.
- Tag: LLM-specific (intersects with logistics-generic prerequisites).

Do I need to know Python before starting?
- The course uses Python. If you know another language (Java, JavaScript, etc.) you can pick up the basics in a day or two. If you have one to two weeks before the cohort starts, that is enough time.
- Tag: LLM-specific.

Can I enrol without programming experience?
- You can register, but the course will be very hard to follow. Try module 1 to gauge whether you can keep up. If not, build programming basics first.
- Tag: LLM-specific.

Are there hardware requirements?
- No special hardware. The course uses hosted LLMs (OpenAI / Groq / etc.); a normal laptop is enough.
- Tag: LLM-specific.

I'm new to the community / GitHub navigation feels confusing - any tips?
- The repo is the entry point. README → syllabus → click into a module folder → watch the videos in order → follow links and code along. All zoomcamps share this structure. Spend 5 to 10 minutes clicking around module 1 and you will get the pattern.
- Tag: logistics-generic.

I have a machine-learning background. Do I need the precourse search-engine workshop?
- If you can program you are ready for LLM Zoomcamp regardless. The workshop is optional but useful background on how search works (retrieval is half of RAG).
- Tag: LLM-specific.

I'm a software developer, not a data scientist. Will this course help me?
- Yes. It is essentially AI engineering: using LLMs to build applications. Developers benefit because LLMs help build prototypes faster and the techniques transfer to side projects and to your day job over time.
- Tag: LLM-specific.

I'm a data engineer. How does this course help me?
- AI engineering is largely data engineering in disguise: knowledge bases, ingestion, indexing, reliable connections between services. Your engineering skills transfer directly. The course also gives you exposure to AI tooling that increasingly shows up in data-engineering roles.
- Tag: LLM-specific.

I'm a data scientist. Will I learn new things?
- Many data scientists already work with LLMs at this point. If you do not yet, this course is a strong way to expand your profile. If you do, you will still learn the engineering side.
- Tag: LLM-specific.

I'm a mechanical engineer / career switcher. Can I transition into AI through this course?
- Yes, technically. The skills the course gives you are a starting point; landing a role still depends on your effort outside the course (portfolio, public learning, applications).
- Tag: LLM-specific.

I have no LLM job experience. Any career advice?
- Build projects. Learn in public. Share what you build. Be visible. There is no shortcut for "no experience"; portfolio + visibility is the realistic path.
- Tag: logistics-generic.

I successfully completed the course last year. Should I do it again?
- The application focus (RAG) is the same, but models, tools, and modules have changed. There will also be a competition similar to last year's. Worth retaking if you want to refresh and re-implement with newer tools.
- Tag: LLM-specific.

Should I follow last year's modules or this year's modules?
- For the live cohort: follow this year's modules. If self-paced, either is fine.
- Tag: LLM-specific.

I already understand many RAG variants. Will I benefit?
- Hard to say without knowing your level. Try module 1 to gauge. If it feels familiar, jump straight to the project; identify gaps as you build, and learn just those.
- Tag: LLM-specific.

Are there age limits?
- No. The previous editions had participants in their 30s, 40s, and beyond. This is also a recurring question across all zoomcamps.
- Tag: logistics-generic.

---

## Time and cost

How much time should I budget?
- Around 10 hours per week. Last cohort's actual numbers (visible on the course platform's homework statistics): module 1 ≈ 4 hours of lectures + 3 hours of homework (≈ 7 total). Vector search ≈ 10 hours. Time decreases with stronger CS background.
- Tag: LLM-specific.

How much will it cost to complete the course?
- A few dollars at most. Using OpenAI: a few dollars total (you will struggle to spend even $10 of credit). Using Groq: free for the entire course if you do not hammer it. OpenAI is recommended for familiarity since most paid roles use it.
- Tag: LLM-specific.

How much can I do locally without cloud resources?
- 100% of the course can be done without paid cloud resources. Use Ollama for fully local LLMs, or Groq / OpenAI for hosted-but-cheap.
- Tag: LLM-specific.

Will there be free GPU access this year?
- Not in LLM Zoomcamp - you do not need a GPU. The Open Source LLM Zoomcamp will have free GPU access via Saturn Cloud and AMD partnerships.
- Tag: LLM-specific.

What does "locally" actually mean in this course?
- Hosted/remote: you call an API like OpenAI; the model runs on someone else's infrastructure.
- Local: you run the LLM yourself, either on your laptop or on a rented GPU machine. This is lower-level (PyTorch, Hugging Face, model weights). LLM Zoomcamp focuses on hosted; Open Source LLM Zoomcamp covers local.
- Tag: LLM-specific.

Other than Docker, what tools will I need?
- Jupyter notebooks (installed in module 1). That is roughly it.
- Tag: LLM-specific.

How much does it cost per model with OpenAI?
- Pricing is per million tokens. Roughly: $2 per 1M input words, $8 per 1M output words → about $10 for 1M in + 1M out (rough estimate; tokens != words exactly). Mini and nano models are cheaper.
- Tag: LLM-specific (link to OpenAI pricing).

---

## Tools, models, providers

Can we use any LLM (GPT, Llama, Mistral, etc.)?
- Yes. The course uses OpenAI as the default but you can use any provider. Recommended free option: Groq.
- Tag: LLM-specific.

Will the course use only OpenAI or multiple providers?
- The course examples use OpenAI. Participants are free to swap in any provider for the project. Groq is highlighted as a free alternative; the awesome-llms list in the repo covers more.
- Tag: LLM-specific.

Will any free LLM provider be covered?
- Yes. Groq is mentioned as a free alternative. The repo includes an awesome-llms list of OpenAI-alternative providers.
- Tag: LLM-specific.

What vector database / search engine is used?
- Elasticsearch was used last year. This year Quadrant (vector DB) is a sponsor and will appear in the vector search module. Final tooling depends on sponsor confirmation.
- Tag: LLM-specific.

What monitoring tool is used?
- Phoenix (open source, from Arize). It replaces Grafana from last year.
- Tag: LLM-specific.

Can I use a different programming language (e.g. JavaScript) for the project?
- Yes. Python is what the course teaches, so course participants will assume Python is installed. If you submit a project in JavaScript / Node.js, you must document setup explicitly so peer reviewers can run it.
- Tag: LLM-specific.

Can I use a knowledge base in a non-English language?
- Yes. The data can be in any language. The README and project description must be in English so peer reviewers can evaluate.
- Tag: logistics-generic / LLM-specific.

Will there be a competition this year?
- Yes, planned. Last year's competition was a math-problem solving challenge with LLMs. This year's format will be different but similar in spirit.
- Tag: LLM-specific.

---

## Frameworks and abstractions

Do we use any RAG framework (LangChain, LlamaIndex, etc.)?
- No. The course teaches the underlying concepts so that you can pick up any framework afterwards. Frameworks are an option for your project.
- Tag: LLM-specific.

Will we orchestrate LLM applications (Mage, Airflow, etc.)?
- No. The orchestration module from the previous edition was removed to focus on fundamentals.
- Tag: LLM-specific.

---

## Project

What is expected from the project?
- Take what you learned in the course and apply it to your own dataset: a working RAG application end to end. Examples from previous cohorts include food/recipe recommendation, fitness assistant, notation lookup, etc.
- Tag: LLM-specific.

Can I work on the project as a team?
- No. Projects are individual, regardless of who you study with.
- Tag: logistics-generic.

Can I get a study partner?
- Yes - the entire Slack community can be your study partners. Only the project itself is solo.
- Tag: logistics-generic.

Can I start the project now?
- Yes. The platform may not have it open yet, but you can start working from existing project guidelines on GitHub. Look at past student projects for ideas.
- Tag: LLM-specific.

Can I do the homework now?
- Module 1 homework is already published. Module 2 onwards will publish on schedule. You can also do last year's homework as practice; this year's questions will be slightly different.
- Tag: LLM-specific.

What does a complex / good project look like?
- Take a look at past students' projects (e.g. Dario's food-search RAG recipe-recommendation system). They are often modest in scope but well-executed and well-documented.
- Tag: LLM-specific.

---

## Logistics and process

What is the process during the cohort?
- Each week (roughly): a new module → watch the videos → complete the homework → submit on the course platform.
- Tag: logistics-generic.

How many homework points per question?
- One point per correct answer (sometimes two). Plus extra points for FAQ contributions and learning-in-public links.
- Tag: logistics-generic.

How does FAQ contribution work for credit?
- If you (or a peer in Slack) hit a problem not in the FAQ, write the problem and solution into the public FAQ document, then describe what you added in the homework form's "FAQ contribution" field. That earns one extra homework point.
- Tag: logistics-generic.

How does learning-in-public work for credit?
- Every time you learn something, post about it (LinkedIn / X / Facebook), include the course hashtag, tag DTC. Then add the link(s) to the homework form's learning-in-public section. Up to seven links per submission. One point per accepted link.
- Tag: logistics-generic.

What is the Slack workflow?
- Join `#course-llm-zoomcamp`. Use threads (reply-in-thread) for any answer; do not start a new top-level message. Don't tag instructors - others can answer too. Search Slack and the FAQ before posting. Course-related questions belong only in the course channel; questions in `#welcome` etc. will be removed.
- Tag: logistics-generic.

Is Telegram required?
- No. Telegram is announcement-only; a bot reposts those messages to Slack. If you don't want Telegram you can rely on Slack alone, but Telegram is more reliable (Slack's volume can drown out announcements).
- Tag: logistics-generic.

How do I find the videos?
- DataTalks.Club YouTube channel → Playlists. Two relevant playlists: "LLM Zoomcamp" (the canonical pre-recorded content) and "LLM Zoomcamp 2025" (cohort-specific: launch stream, Q&As, office hours). 2024 playlist is also still useful.
- Tag: logistics-generic / LLM-specific.

Where is the cohort-specific material?
- In the GitHub repo under `cohorts/2025/`. Includes the launch stream, course platform link, homework files, schedule.
- Tag: logistics-generic.

Will the lessons be live or pre-recorded?
- Pre-recorded, as in other zoomcamps.
- Tag: logistics-generic.

Will there be office hours?
- Probably not for every module. At minimum two are planned: vector search and monitoring. Possibly a third.
- Tag: LLM-specific.

How is the certificate earned?
- Submit a passing project, complete peer reviews. Two weeks for project work + one week for peer review (review three other projects).
- Tag: logistics-generic.

Are there any prerequisites to receive a certificate?
- Submitting a passing project plus peer reviews. Homework is not required for certification but earns leaderboard points.
- Tag: logistics-generic.

Will I have issues if I have never used GitHub?
- Yes, you will need to learn it. There is time before the cohort starts.
- Tag: logistics-generic.

Will course tutorials be live or pre-recorded?
- Pre-recorded, like every other zoomcamp.
- Tag: logistics-generic.

---

## Career questions

Can I get a job after the course?
- Anyone can. Whether you do is up to you - the course gives you the skills, but you still have to apply for jobs and put in the work.
- Tag: logistics-generic.

Which course has the highest job-search ROI?
- No reliable data. Anecdotal "this course got me a job" feedback exists for every course. Pick a course that genuinely interests you - studying a course you don't enjoy is the worst ROI of all.
- Tag: logistics-generic.

Which course is closest to current industry requirements?
- Context-dependent (region, role, market). Search local job postings, identify common requirements, compare to the syllabus. The LLM Zoomcamp covers AI-engineering fundamentals and should map well in most markets.
- Tag: logistics-generic.

Which profile benefits most: data scientist, ML developer, dev, ...?
- All of the above. Engineering profiles get the most direct uplift; data scientists who don't yet work with LLMs benefit the most in terms of "expanding your profile".
- Tag: logistics-generic.

What course suits people in monitoring and observability?
- LLM Zoomcamp's monitoring module covers LLM observability. MLOps Zoomcamp covers ML model monitoring. These are the closest matches in our catalogue.
- Tag: logistics-generic.

---

## Sponsors and supporting the course

Who sponsors the 2025 cohort?
- Arize: machine-learning and LLM monitoring (Phoenix is their open-source product). Long-term community supporter.
- dlthub: ingestion library; will run a workshop on data ingestion for LLMs.
- Quadrant: vector database; appears in the vector-search module. New sponsor for this cohort.
- Tag: LLM-specific (whats-new section).

How can I or my company support the course?
- Companies: contact via Slack DM, email, or reply to the newsletter to discuss sponsorship.
- Individuals: GitHub sponsors page. Recurring or one-off donations are appreciated.
- Companies with training budgets: an invoice can be issued for any amount you want to allocate.
- Tag: logistics-generic.

How can we help promote the course?
- Star the repo on GitHub (helps surface it on GitHub Trending). Like the YouTube videos, subscribe to the channel, engage in live chat. Share with your network.
- Tag: logistics-generic.

---

## Open Source LLM Zoomcamp (separate course)

What happened to the open source LLMs module?
- It was removed from LLM Zoomcamp and turned into a standalone course (Open Source LLM Zoomcamp), expanded to two modules with more time per module.
- Tag: LLM-specific.

When does the Open Source LLM Zoomcamp run?
- Late June or early July (run in parallel to LLM Zoomcamp).
- Tag: LLM-specific.

What does it cover?
- Running open-source LLMs locally / on rented GPUs (Llama, Mistral, DeepSeek, etc.), partial coverage of deployment, and fine-tuning. Last year's content is being rewritten because the model landscape has changed (DeepSeek, new Llama versions).
- Tag: LLM-specific.

Will it be considered part of LLM Zoomcamp / share certification?
- No. Separate course, separate certification.
- Tag: LLM-specific.

---

## AI Dev Tools Zoomcamp (forthcoming course)

What is the AI Dev Tools Zoomcamp?
- A new course planned for around September 2025, focused on using AI tools (Cursor, Claude, ChatGPT, etc.) for development - and on building agents as part of the course. Driven by 2,100 signups in a community-interest survey.
- Tag: logistics-generic.

---

## Bot and FAQ usage

What is the LLM Zoomcamp bot?
- A bot built by community member Alex Lainov (predates the course) that answers participants' questions using the public FAQ and Slack history. The bot inspired the LLM Zoomcamp itself.
- Tag: LLM-specific.

How should I use the FAQ document?
- Search it first when you have a problem - many issues are already documented with their fixes. If your problem isn't there, ask in Slack and contribute the answer back.
- Tag: logistics-generic.

