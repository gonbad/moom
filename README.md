# موم — Moom

موم قالبی آماده برای تبدیل کارهای تکراری به یک روشِ بهترشونده است. آن را در دستیار
کدنویسی باز کنید و بگویید «شروع کنیم». دستیار کارهای فنی را انجام می‌دهد؛ شما ورودی
واقعی، خواسته‌ها و بازخوردتان را می‌آورید.

در Claude Code، OpenCode و Antigravity از `/moom-start` استفاده کنید. در Codex،
مهارت `$moom-start` را بخواهید. فرمان‌ها همراه مخزن آماده‌اند؛ برای دیدن فرمان‌های تازه
ممکن است میزبان به بازخوانی نشست نیاز داشته باشد. درخواست به زبان عادی هم کار می‌کند.

با `moom-job` کار تکراری و اولین نمونهٔ واقعی را مشخص می‌کنیم. یک روش از فهرست
آغازین انتخاب و متناسب می‌شود، یا روش تازه‌ای می‌سازیم. پس از راه‌اندازی موفق، فهرست
آغازین حذف می‌شود و فقط روش خودتان می‌ماند. نسخهٔ شکل‌گرفتهٔ موم را «کندو» می‌نامیم.

هر کندو **یک جابِ جاری** و چند پروژه دارد. اصلاح‌های پروژه‌ها می‌توانند جاب را هم بهتر
کنند. پروژهٔ قبلی هنگام بازگشت از روش جاری استفاده می‌کند؛ خروجی قبلی خودبه‌خود
بازسازی یا منتشر نمی‌شود.

پوشهٔ `docs/` را در Obsidian باز کنید. پرسش‌ها، پاسخ‌ها و تصمیم‌ها آنجا هستند؛
فایل‌های واقعی و خروجی هر پروژه در `projects/` قرار دارند.

| درخواست | فرمان |
| --- | --- |
| شروع و تنظیم زبان | `moom-start` |
| انتخاب کار و پروژهٔ اول | `moom-job` |
| پروژهٔ بعدی | `moom-project` |
| بازگشت به پروژه | `moom-switch` |
| تغییر نسخهٔ پروژه، جاب یا کار مشترک | `moom-iterate` |
| گزارش و رفع ایراد | `moom-issue` |
| دیدن وضعیت و نسخه‌ها | `moom-status`، `moom-versions` |
| به‌روزرسانی خود موم | `moom-update` |
| آماده‌کردن جاب برای اشتراک | `moom-export`، `moom-publish` |

## Repository layout

```text
docs/                 Human discussions, review history, living explanations
  moom/               Guide and review contract
  workspace/          Shared work and coordination
  job/                Job discussions, independent of its executable package
  projects/<id>/      Project living notes and nested version discussions
job/<name>/           Exactly one installed Agent Skill, improving through use
projects/<id>/        Actual inputs, editable sources and deliverables
shared/               Integration or deployment code shared by Projects
registry/             Bootstrap-only starter catalog; removed after successful setup
.moom/core/           Bundled mechanics and canonical Moom procedures
workspace.json        Authoritative selection, versions and review state
```

Moom is self-contained. Its helper uses Python 3.10+ and the standard library; the
assistant provisions task-specific dependencies when needed. No pip-installed Moom
application or separate registry server is required.

This repository is a GitHub template. Create a repository from it, fork it, or download
a release, then open your copy in your assistant. The template itself contains no
installed Job or personal Projects. Moom releases and Job/Project versions are independent.

Read the [guide](docs/moom/guide.md), [review contract](docs/moom/review.md),
[update contract](docs/moom/updates.md), and [contribution instructions](CONTRIBUTING.md).
Native adapter locations follow the [Agent Skills specification](https://agentskills.io/specification),
[Claude Code docs](https://code.claude.com/docs/en/skills),
[Codex skill docs](https://developers.openai.com/codex/skills/),
[OpenCode command docs](https://opencode.ai/docs/commands/), and
[Antigravity skill migration docs](https://antigravity.google/docs/migration/workflows-to-skills/).
Automated tests verify generated files and dispatch; interactive host discovery must
be checked in the host being used before claiming it has been verified.
