.PHONY: examples cv application-pdfs

CC = lualatex
EXAMPLES_DIR = examples
RESUME_DIR = examples/resume
CV_DIR = examples/cv
RESUME_SRCS = $(shell find $(RESUME_DIR) -name '*.tex')
CV_SRCS = $(shell find $(CV_DIR) -name '*.tex')
SHARED_SRCS = $(wildcard $(EXAMPLES_DIR)/shared/*.tex)

examples: $(foreach x, coverletter coverletter-qa-lead coverletter-qa-automation coverletter-devops-platform cv resume cv-ats cv-ats-qa-automation, $x.pdf)

cv: cv.pdf resume.pdf cv-ats.pdf cv-ats-qa-automation.pdf

application-pdfs: cv
	mkdir -p output/pdf
	cp $(EXAMPLES_DIR)/cv.pdf output/pdf/Wojciech_Bajer_QA_Lead_CV.pdf
	cp $(EXAMPLES_DIR)/cv-ats.pdf output/pdf/Wojciech_Bajer_QA_Lead_ATS.pdf
	cp $(EXAMPLES_DIR)/resume.pdf output/pdf/Wojciech_Bajer_QA_Automation_CV.pdf
	cp $(EXAMPLES_DIR)/cv-ats-qa-automation.pdf output/pdf/Wojciech_Bajer_QA_Automation_ATS.pdf

resume.pdf: $(EXAMPLES_DIR)/resume.tex $(RESUME_SRCS) $(CV_SRCS) $(SHARED_SRCS)
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

cv.pdf: $(EXAMPLES_DIR)/cv.tex $(CV_SRCS) $(SHARED_SRCS) $(EXAMPLES_DIR)/profile-wb.png
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

cv-ats.pdf: $(EXAMPLES_DIR)/cv-ats.tex $(CV_SRCS) $(SHARED_SRCS)
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

cv-ats-qa-automation.pdf: $(EXAMPLES_DIR)/cv-ats-qa-automation.tex $(RESUME_SRCS) $(CV_SRCS) $(SHARED_SRCS)
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

coverletter.pdf: $(EXAMPLES_DIR)/coverletter.tex
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

coverletter-qa-lead.pdf: $(EXAMPLES_DIR)/coverletter-qa-lead.tex
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

coverletter-qa-automation.pdf: $(EXAMPLES_DIR)/coverletter-qa-automation.tex
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

coverletter-devops-platform.pdf: $(EXAMPLES_DIR)/coverletter-devops-platform.tex
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

clean:
	rm -rf $(EXAMPLES_DIR)/*.pdf
