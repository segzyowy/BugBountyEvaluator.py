# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

class BugBountyEvaluator(gl.Contract):
    admin: Address
    report_count: u32
    valid_bounties: u32
    reports: TreeMap[u32, str]

    def __init__(self):
        self.admin = gl.message.sender_address
        self.report_count = u32(0)
        self.valid_bounties = u32(0)
        self.reports = TreeMap()

    @gl.public.write
    def submit_bug_report(
        self,
        researcher_handle: str,
        target_component: str,
        vulnerability_summary: str,
        reproduction_steps: str
    ) -> str:
        self.report_count = u32(self.report_count + 1)
        current_id = self.report_count

        def evaluate_bounty() -> str:
            prompt = f"""
            You are an objective smart contract cybersecurity triage agent.
            Analyze this bug bounty report for technical severity and reproducibility:

            Researcher: {researcher_handle}
            Component: {target_component}
            Summary: {vulnerability_summary}
            Steps: {reproduction_steps}

            Determine severity (CRITICAL, HIGH, MEDIUM, LOW, or INVALID) and award recommendation.
            Return ONLY a valid JSON string:
            {{"severity": "HIGH", "score": 80, "valid": true, "payout_recommendation": 1500, "assessment": "Legitimate logic vulnerability with actionable PoC."}}
            """
            return gl.nondet.exec_prompt(prompt)

        raw_result = gl.eq_principle.strict_eq(evaluate_bounty)
        clean_result = raw_result.strip().replace("```json", "").replace("```", "")

        if '"valid": true' in clean_result.lower():
            self.valid_bounties = u32(self.valid_bounties + 1)

        self.reports[current_id] = clean_result
        return f"Bounty report #{current_id} triaged and stored on-chain."

    @gl.public.view
    def get_report(self, report_id: u32) -> str:
        return self.reports.get(report_id, "Report not found")

    @gl.public.view
    def get_stats(self) -> str:
        return f"Total: {self.report_count} | Validated: {self.valid_bounties}"
