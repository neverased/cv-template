import importlib.util
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "scripts" / "generate_cover_letter.py"
SPEC = importlib.util.spec_from_file_location("generate_cover_letter", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class GenerateCoverLetterTests(unittest.TestCase):
    def test_infer_track_prefers_applied_ai_for_agentic_backend_role(self) -> None:
        profile = MODULE.load_profile()
        job_text = (
            "Principal Applied AI Engineer. Build systems involving LLMs, "
            "integrations, multi-step or agentic workflows, internal tools, "
            "TypeScript, Node.js, backend engineering."
        )
        self.assertEqual(MODULE.infer_track(job_text, profile, "auto"), "applied-ai")

    def test_build_paragraphs_for_applied_ai_are_explicit_and_not_generic(self) -> None:
        profile = MODULE.load_profile()
        job_text = (
            "AI-assisted development systems, internal tools, TypeScript, "
            "Node.js, LLM workflows, backend systems."
        )
        paragraph_1, paragraph_2, paragraph_3, matches, domains = MODULE.build_paragraphs(
            "CKSource",
            "Principal Applied AI Engineer",
            profile,
            "applied-ai",
            job_text,
        )
        combined = " ".join([paragraph_1, paragraph_2, paragraph_3])
        self.assertIn("Lexense.ai", combined)
        self.assertIn("Node.js", combined)
        self.assertIn("LLM", combined)
        self.assertIn("CKSource", combined)
        self.assertNotIn("The strongest overlap with your role includes", combined)


if __name__ == "__main__":
    unittest.main()
