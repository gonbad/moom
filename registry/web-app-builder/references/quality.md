# Acceptance criteria

- Project ownership: a second Project preserves the first one's specs, source, designs,
  credentials, database volumes and deployment. Resume uses workspace state.
- Source fidelity: behavior traces to the current idea, PRD, schema, UX and scenarios.
- Design fidelity: screenshot pairs for approved screens and states at matching
  viewports demonstrate the React conversion's appearance. Explain any intentional
  owner-approved difference; missing screenshots are an incomplete gate.
- Production assets: compiled Tailwind, fonts, CSS, scripts and images are served by
  the participant's server. No runtime design CDN is required.
- Runtime: API authorization and validation, migrations, error behavior and meaningful
  end-to-end scenarios pass. Testing must not mutate production data.
- Serving: direct navigation/reload reaches each client route; missing assets and API
  endpoints retain correct errors rather than receiving the React shell.
- Deployment: public hostname and trusted HTTPS, redirect/renewal, DB/cache access
  from the real service, restart and recovery are verified.
- Human review: the person checks changed decisions, then the prototype and a complete
  final user journey. Machine success is recorded separately from their acceptance.
