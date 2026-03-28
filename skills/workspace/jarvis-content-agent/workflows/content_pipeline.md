# Content Pipeline Workflow

## Full Pipeline: Research → Outline → Write → Review → Publish

### Step 1: Research (delegate to ResearchSubAgent or self)
1. Xác định topic + target keyword
2. Research 5-10 competitor articles
3. Gather sources, stats, expert quotes
4. Create research brief

### Step 2: Outline
1. Write H1 title (with keyword)
2. Create H2/H3 structure
3. Note key points cho mỗi section
4. Add planned citations [1], [2]
5. **CHECKPOINT**: User approve outline

### Step 3: Write
1. Write section by section
2. Each section: hook → explain → example → transition
3. Insert citations inline
4. **CHECKPOINT after each major section**: "Phần này ổn không?"

### Step 4: Review
1. Read full draft aloud (flow check)
2. SEO check: keyword density, meta, headers
3. Citation verification
4. Grammar + spelling
5. Submit to W8:CriticAgent

### Step 5: Publish
1. Format for target platform
2. Add meta tags, images, alt text
3. Schedule or publish
4. Social media promotion (spawn SocialSubAgent)

## Sub-Agent Spawning
```
Need research? → ResearchSubAgent
Need ad copy / A/B variants? → CopywritingSubAgent  
Need multi-platform adaptation? → SocialSubAgent
```
