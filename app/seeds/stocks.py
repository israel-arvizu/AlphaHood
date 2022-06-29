from app.models import db, Stock


# Adds a demo user, you can add other users here if you want
def seed_stocks():

    AOS = Stock(
        name='A. O. Smith Corporation',
        ticker='AOS',
        marketCap=8608466944,
        dayHigh=56.75,
        dayLow=54.99,
        currentPrice=55.18,
        longBusinessSummary='A. O. Smith Corporation manufactures and markets residential and commercial gas, heat pump and electric water heaters, boilers, tanks, and water treatment products in North America, China, Europe, and India. It operates through two segments, North America and Rest of World. The company offers water heaters for residences, restaurants, hotels and motels, office buildings, laundries, car washes, and small businesses; commercial boilers for hospitals, schools, hotels, and other large commercial buildings, as well as residential boilers for homes, apartments, and condominiums; and water treatment products comprising point-of-entry water softeners, well water solutions, and whole-home water filtration products, on-the-go filtration bottles, point-of-use carbon, and reverse osmosis products for residences, restaurants, hotels, and offices. It also provides food and beverage filtration products; expansion tanks, commercial solar water heating systems, swimming pool and spa heaters, and related products and parts; and heat pumps, electric wall-hung, gas tankless, combi-boiler, heat pump and solar water heaters. The company offers its products primarily under the A. O. Smith, State, Lochinvar, and water softener brands. It distributes its products through independent wholesale plumbing distributors, as well as through retail channels consisting of hardware and home center chains, and manufacturer representative firms; and offers Aquasana branded products directly to consumers through e-commerce, as well as other online retailers. A. O. Smith Corporation was founded in 1874 and is headquartered in Milwaukee, Wisconsin.',
        fullTimeEmployees=13700,
        city='Milwaukee',
        state='WI',
        trailingPE=17.341295,
        dividendYield=0.0211,
        averageVolume=1129427,
        regularMarketOpen=55.94,
        volume=1107374,
        fiftyTwoWeekHigh=86.74,
        fiftyTwoWeekLow=51.91,
        recommendationKey='hold',
        industry='Specialty Industrial Machinery'
    )
    db.session.add(AOS)

    ABT = Stock(
        name='Abbott Laboratories',
        ticker='ABT',
        marketCap=187298054144,
        dayHigh=109.93,
        dayLow=106.9,
        currentPrice=106.97,
        longBusinessSummary="Abbott Laboratories, together with its subsidiaries, discovers, develops, manufactures, and sells health care products worldwide. It operates in four segments: Established Pharmaceutical Products, Diagnostic Products, Nutritional Products, and Medical Devices. The Established Pharmaceutical Products segment provides generic pharmaceuticals for the treatment of pancreatic exocrine insufficiency, irritable bowel syndrome or biliary spasm, intrahepatic cholestasis or depressive symptoms, gynecological disorder, hormone replacement therapy, dyslipidemia, hypertension, hypothyroidism, Ménière's disease and vestibular vertigo, pain, fever, inflammation, and migraine, as well as provides anti-infective clarithromycin, influenza vaccine, and products to regulate physiological rhythm of the colon. The Diagnostic Products segment offers laboratory systems in the areas of immunoassay, clinical chemistry, hematology, and transfusion; molecular diagnostics systems that automate the extraction, purification, and preparation of DNA and RNA from patient samples, as well as detect and measure infectious agents; point of care systems; cartridges for testing blood; rapid diagnostics lateral flow testing products; molecular point-of-care testing for HIV, SARS-CoV-2, influenza A and B, RSV, and strep A; cardiometabolic test systems; drug and alcohol test, and remote patient monitoring and consumer self-test systems; and informatics and automation solutions for use in laboratories. The Nutritional Products segment provides pediatric and adult nutritional products. The Medical Devices segment offers rhythm management, electrophysiology, heart failure, vascular, and structural heart devices for the treatment of cardiovascular diseases; and diabetes care products, as well as neuromodulation devices for the management of chronic pain and movement disorders. Abbott Laboratories was founded in 1888 and is based in North Chicago, Illinois.",
        fullTimeEmployees=113000,
        city='North Chicago',
        state='IL',
        trailingPE=24.830547,
        dividendYield=0.0183,
        averageVolume=5486616,
        regularMarketOpen=109.25,
        volume=3989519,
        fiftyTwoWeekHigh=142.6,
        fiftyTwoWeekLow=101.24,
        recommendationKey='buy',
        industry='Medical Devices'
    )
    db.session.add(ABT)

    ABBV = Stock(
        name='AbbVie Inc.',
        ticker='ABBV',
        marketCap=269466615808,
        dayHigh=155.115,
        dayLow=151.39,
        currentPrice=152.49,
        longBusinessSummary="AbbVie Inc. discovers, develops, manufactures, and sells pharmaceuticals in the worldwide. The company offers HUMIRA, a therapy administered as an injection for autoimmune and intestinal Behçet's diseases; SKYRIZI to treat moderate to severe plaque psoriasis in adults; RINVOQ, a JAK inhibitor for the treatment of moderate to severe active rheumatoid arthritis in adult patients; IMBRUVICA to treat adult patients with chronic lymphocytic leukemia (CLL), small lymphocytic lymphoma (SLL), and VENCLEXTA, a BCL-2 inhibitor used to treat adults with CLL or SLL; and MAVYRET to treat patients with chronic HCV genotype 1-6 infection. It also provides CREON, a pancreatic enzyme therapy for exocrine pancreatic insufficiency; Synthroid used in the treatment of hypothyroidism; Linzess/Constella to treat irritable bowel syndrome with constipation and chronic idiopathic constipation; Lupron for the palliative treatment of advanced prostate cancer, endometriosis and central precocious puberty, and patients with anemia caused by uterine fibroids; and Botox therapeutic. In addition, the company offers ORILISSA, a nonpeptide small molecule gonadotropin-releasing hormone antagonist for women with moderate to severe endometriosis pain; Duopa and Duodopa, a levodopa-carbidopa intestinal gel to treat Parkinson's disease; Lumigan/Ganfort, a bimatoprost ophthalmic solution for the reduction of elevated intraocular pressure (IOP) in patients with open angle glaucoma (OAG) or ocular hypertension; Ubrelvy to treat migraine with or without aura in adults; Alphagan/ Combigan, an alpha-adrenergic receptor agonist for the reduction of IOP in patients with OAG; and Restasis, a calcineurin inhibitor immunosuppressant to increase tear production, as well as other eye care products. AbbVie Inc. has a research collaboration with Dragonfly Therapeutics, Inc. The company was incorporated in 2012 and is headquartered in North Chicago, Illinois.",
        fullTimeEmployees=50000,
        city='North Chicago',
        state='IL',
        trailingPE=21.87491,
        dividendYield=0.040799998,
        averageVolume=7352337,
        regularMarketOpen=153.17,
        volume=5176195,
        fiftyTwoWeekHigh=175.91,
        fiftyTwoWeekLow=105.56,
        recommendationKey='buy',
        industry='Drug Manufacturers—General'
    )
    db.session.add(ABBV)

    ABMD = Stock(
        name='Abiomed, Inc.',
        ticker='ABMD',
        marketCap=11349056512,
        dayHigh=257.01,
        dayLow=248.85,
        currentPrice=249.08,
        longBusinessSummary='Abiomed, Inc. engages in the research, development, and sale of medical devices to assist or replace the pumping function of the failing heart. It also provides a continuum of care to heart failure patients. The company offers Impella 2.5, a percutaneous micro heart pump with integrated motor and sensors; and Impella CP, a device for use by interventional cardiologists to support patients in the cath lab, as well as by cardiac surgeons in the heart surgery suite. It also provides Impella 5.0, Impella LD, and Impella 5.5, which are percutaneous micro heart pumps with integrated motors and sensors for use primarily in the heart surgery suite; Impella RP, a percutaneous catheter-based axial flow pump; Impella SmartAssist platform that includes optical sensor technology for improved pump positioning and the use of algorithms that enable improved native heart assessment during the weaning process; Impella Connect, a cloud-based technology that enables secure and remote viewing of the automated impella controller for physicians and hospital staffs; and OXY-1 System, a portable external respiratory assistance device. In addition, the company is developing Impella ECP, a pump for blood flow of greater than three liters per minute; Impella XR Sheath, a sheath that expands and recoils allowing small bore access and closure with Impella heart pumps; Impella BTR, a percutaneous micro heart pump with integrated motors and sensors; and preCARDIA, a catheter-mounted superior vena cava therapy system designed to rapidly treat acutely decompensated heart failure. Abiomed, Inc. sells its products through direct sales and clinical support personnel in the Germany, France, United States, Japan, Europe, Canada, Latin America, the Asia-Pacific, and the Middle East. The company was founded in 1981 and is headquartered in Danvers, Massachusetts.',
        fullTimeEmployees=2003,
        city='Danvers',
        state='MA',
        trailingPE=83.58389,
        dividendYield=None,
        averageVolume=315822,
        regularMarketOpen=254.66,
        volume=187699,
        fiftyTwoWeekHigh=379.3,
        fiftyTwoWeekLow=219.85,
        recommendationKey='buy',
        industry='Medical Devices'
    )
    db.session.add(ABMD)

    ATVI = Stock(
        name='Activision Blizzard, Inc.',
        ticker='ATVI',
        marketCap=60329943040,
        dayHigh=78.24,
        dayLow=76.945,
        currentPrice=77.16,
        longBusinessSummary="Activision Blizzard, Inc., together with its subsidiaries, develops and publishes interactive entertainment content and services in the Americas, Europe, the Middle East, Africa, and the Asia Pacific. The company operates through three segments: Activision, Blizzard, and King. It develops and distributes content and services on video game consoles, personal computers, and mobile devices, including subscription, full-game, and in-game sales, as well as by licensing software to third-party or related-party companies that distribute Activision and Blizzard products. The company also maintains a proprietary online gaming service, Battle.net that facilitates digital distribution of content, online social connectivity, and the creation of user-generated content. In addition, it operates esports leagues and offer digital advertising content; and provides warehousing, logistics, and sales distribution services to third-party publishers of interactive entertainment software, as well as manufacturers of interactive entertainment hardware products. The company's key product franchises include Call of Duty, World of Warcraft, Diablo, Hearthstone, Overwatch, Overwatch League, and Candy Crush. It serves retailers and distributors, including mass-market retailers, consumer electronics stores, discount warehouses, and game specialty stores through third-party distribution and licensing arrangements. The company is headquartered in Santa Monica, California.",
        fullTimeEmployees=9800,
        city='Santa Monica',
        state='CA',
        trailingPE=24.50302,
        dividendYield=0.0063,
        averageVolume=5657972,
        regularMarketOpen=78.095,
        volume=4153026,
        fiftyTwoWeekHigh=95.99,
        fiftyTwoWeekLow=56.4,
        recommendationKey='buy',
        industry='Electronic Gaming & Multimedia'
    )
    db.session.add(ATVI)

    ADM = Stock(
        name='Archer-Daniels-Midland Company',
        ticker='ADM',
        marketCap=42760175616,
        dayHigh=78.29,
        dayLow=75.66,
        currentPrice=75.99,
        longBusinessSummary="Archer-Daniels-Midland Company procures, transports, stores, processes, and merchandises agricultural commodities, products, and ingredients in the United States, Switzerland, Cayman Islands, Brazil, Mexico, the United Kingdom, and internationally. The company operates through three segments: Ag Services and Oilseeds, Carbohydrate Solutions, and Nutrition. It procures, stores, cleans, and transports agricultural raw materials, such as oilseeds, corn, wheat, milo, oats, and barley. The company also engages in the agricultural commodity and feed product import, export, and distribution; and structured trade finance activities. In addition, it offers vegetable oils and protein meals; ingredients for the food, feed, energy, and industrial customers; crude vegetable oils, salad oils, margarine, shortening, and other food products; and partially refined oils to produce biodiesel and glycols for use in chemicals, paints, and other industrial products. Further, the company provides peanuts, peanut-derived ingredients, and cotton cellulose pulp; sweeteners, corn and wheat starches, syrup, glucose, wheat flour, and dextrose; alcohol and other food and animal feed ingredients; ethyl alcohol and ethanol; corn gluten feed and meal; distillers' grains; and citric acids. Additionally, the company provides natural flavors, flavor systems, natural colors, proteins, emulsifiers, soluble fiber, polyols, hydrocolloids, and natural health and nutrition products, including probiotics, prebiotics, enzymes, and botanical extracts; and other specialty food and feed ingredients; edible beans; formula feeds, and animal health and nutrition products; and contract and private label pet treats and foods. It also offers futures commission merchant; commodity brokerage services; cash margins and securities pledged to commodity exchange clearinghouses; and cash pledged as security under certain insurance arrangements. The company was founded in 1902 and is headquartered in Chicago, Illinois.",
        fullTimeEmployees=39218,
        city='Chicago',
        state='IL',
        trailingPE=13.991898,
        dividendYield=0.0202,
        averageVolume=4059216,
        regularMarketOpen=76.56,
        volume=2538500,
        fiftyTwoWeekHigh=98.88,
        fiftyTwoWeekLow=56.91,
        recommendationKey='buy',
        industry='Farm Products'
    )
    db.session.add(ADM)

    ADBE = Stock(
        name='Adobe Inc.',
        ticker='ADBE',
        marketCap=172760170496,
        dayHigh=382.97,
        dayLow=364.87,
        currentPrice=365.63,
        longBusinessSummary='Adobe Inc. operates as a diversified software company worldwide. It operates through three segments: Digital Media, Digital Experience, and Publishing and Advertising. The Digital Media segment offers products, services, and solutions that enable individuals, teams, and enterprises to create, publish, and promote content; and Document Cloud, a unified cloud-based document services platform. Its flagship product is Creative Cloud, a subscription service that allows members to access its creative products. This segment serves content creators, workers, marketers, educators, enthusiasts, communicators, and consumers. The Digital Experience segment provides an integrated platform and set of applications and services that enable brands and businesses to create, manage, execute, measure, monetize, and optimize customer experiences from analytics to commerce. This segment serves marketers, advertisers, agencies, publishers, merchandisers, merchants, web analysts, data scientists, developers, and executives across the C-suite. The Publishing and Advertising segment offers products and services, such as e-learning solutions, technical document publishing, web conferencing, document and forms platform, web application development, and high-end printing, as well as Advertising Cloud offerings. The company offers its products and services directly to enterprise customers through its sales force and local field offices, as well as to end users through app stores and through its website at adobe.com. It also distributes products and services through a network of distributors, value-added resellers, systems integrators, software vendors and developers, retailers, and original equipment manufacturers. The company was formerly known as Adobe Systems Incorporated and changed its name to Adobe Inc. in October 2018. Adobe Inc. was founded in 1982 and is headquartered in San Jose, California.',
        fullTimeEmployees=25988,
        city='San Jose',
        state='CA',
        trailingPE=35.706055,
        dividendYield=None,
        averageVolume=3295998,
        regularMarketOpen=381,
        volume=2602217,
        fiftyTwoWeekHigh=699.54,
        fiftyTwoWeekLow=338,
        recommendationKey='buy',
        industry='Software—Infrastructure'
    )
    db.session.add(ADBE)

    ADP = Stock(
        name='Automatic Data Processing, Inc.',
        ticker='ADP',
        marketCap=89422921728,
        dayHigh=220.3975,
        dayLow=213.92,
        currentPrice=214.06,
        longBusinessSummary='Automatic Data Processing, Inc. provides cloud-based human capital management solutions worldwide. It operates in two segments, Employer Services and Professional Employer Organization (PEO). The Employer Services segment offers strategic, cloud-based platforms, and human resources (HR) outsourcing solutions. Its offerings include payroll, benefits administration, talent management, HR management, workforce management, insurance, retirement, and compliance services. The PEO Services segment provides HR outsourcing solutions to small and mid-sized businesses through a co-employment model. This segment offers benefits package, protection and compliance, talent engagement, comprehensive outsourcing, and recruitment process outsourcing services. The company was founded in 1949 and is headquartered in Roseland, New Jersey.',
        fullTimeEmployees=56000,
        city='Roseland',
        state='NJ',
        trailingPE=31.57227,
        dividendYield=0.0191,
        averageVolume=1890517,
        regularMarketOpen=218.72,
        volume=1412779,
        fiftyTwoWeekHigh=248.96,
        fiftyTwoWeekLow=192.26,
        recommendationKey='hold',
        industry='Staffing & Employment Services'
    )
    db.session.add(ADP)

    AFL = Stock(
        name='Aflac Incorporated',
        ticker='AFL',
        marketCap=36008824832,
        dayHigh=57.1899,
        dayLow=55.865,
        currentPrice=55.9,
        longBusinessSummary='Aflac Incorporated, through its subsidiaries, provides supplemental health and life insurance products. It operates through two segments, Aflac Japan and Aflac U.S. The Aflac Japan segment offers cancer, medical, nursing care income support, GIFT, and whole and term life insurance products, as well as WAYS and child endowment plans under saving type insurance products in Japan. The Aflac U.S. segment provides cancer, accident, short-term disability, critical illness, hospital indemnity, dental, vision, long-term care and disability, and term and whole life insurance products in the United States. It sells its products through sales associates, brokers, independent corporate agencies, individual agencies, and affiliated corporate agencies. The company was founded in 1955 and is based in Columbus, Georgia.',
        fullTimeEmployees=12447,
        city='Columbus',
        state='GA',
        trailingPE=9.178982,
        dividendYield=0.030199999,
        averageVolume=2746748,
        regularMarketOpen=56.62,
        volume=2327915,
        fiftyTwoWeekHigh=67.2,
        fiftyTwoWeekLow=51.28,
        recommendationKey='hold',
        industry='Insurance—Life'
    )
    db.session.add(AFL)

    A = Stock(
        name='Agilent Technologies, Inc.',
        ticker='A',
        marketCap=34966757376,
        dayHigh=121.24,
        dayLow=116.72,
        currentPrice=117.06,
        longBusinessSummary="Agilent Technologies, Inc. provides application focused solutions to the life sciences, diagnostics, and applied chemical markets worldwide. The Life Sciences and Applied Markets segment offers liquid chromatography systems and components; liquid chromatography mass spectrometry systems; gas chromatography systems and components; gas chromatography mass spectrometry systems; inductively coupled plasma mass spectrometry instruments; atomic absorption instruments; microwave plasma-atomic emission spectrometry instruments; inductively coupled plasma optical emission spectrometry instruments; raman spectroscopy; cell analysis plate based assays; flow cytometer; real-time cell analyzer; cell imaging systems; microplate reader; laboratory software; information management and analytics; laboratory automation and robotic systems; dissolution testing; vacuum pumps, and measurement technologies. The Diagnostics and Genomics segment provides arrays for DNA mutation detection, genotyping, gene copy number determination, identification of gene rearrangements, DNA methylation profiling, gene expression profiling, next generation sequencing, target enrichment and genetic data management, and interpretation support software; and produces synthesized oligonucleotide. It also offers immunohistochemistry in situ hybridization, and hematoxylin and eosin staining and special staining; consumables, and software for quality control analysis of nucleic acid samples; and reagents for use in turbidimetry and flow cytometry, as well as develops liquid-based pharmacodiagnostics. The Agilent CrossLab segment provides GC and LC columns, sample preparation products, custom chemistries, and laboratory instrument supplies; and startup, operational, training, compliance support, software as a service, asset management, and consultation services. The company markets its products through direct sales, distributors, resellers, manufacturer's representatives, and electronic commerce. Agilent Technologies, Inc. was incorporated in 1999 and is headquartered in Santa Clara, California.",
        fullTimeEmployees=17400,
        city='Santa Clara',
        state='CA',
        trailingPE=28.241255,
        dividendYield=0.0074,
        averageVolume=2044011,
        regularMarketOpen=120.45,
        volume=1267970,
        fiftyTwoWeekHigh=179.57,
        fiftyTwoWeekLow=112.52,
        recommendationKey='none',
        industry='Diagnostics & Research'
    )
    db.session.add(A)

    APD = Stock(
        name='Air Products and Chemicals, Inc.',
        ticker='APD',
        marketCap=53782167552,
        dayHigh=248.5,
        dayLow=241.915,
        currentPrice=242.51,
        longBusinessSummary='Air Products and Chemicals, Inc. provides atmospheric gases, process and specialty gases, equipment, and services worldwide. The company produces atmospheric gases, including oxygen, nitrogen, and argon; process gases, such as hydrogen, helium, carbon dioxide, carbon monoxide, syngas; specialty gases; and equipment for the production or processing of gases comprising air separation units and non-cryogenic generators for customers in various industries, including refining, chemical, gasification, metals, manufacturing, food and beverage, electronics, magnetic resonance imaging, energy production and refining, and metals. It also designs and manufactures equipment for air separation, hydrocarbon recovery and purification, natural gas liquefaction, and liquid helium and liquid hydrogen transport and storage. Air Products and Chemicals, Inc. has a strategic collaboration with Baker Hughes Company to develop hydrogen compression systems. The company was founded in 1940 and is headquartered in Allentown, Pennsylvania.',
        fullTimeEmployees=20000,
        city='Allentown',
        state='PA',
        trailingPE=24.154383,
        dividendYield=0.0269,
        averageVolume=1183322,
        regularMarketOpen=245.89,
        volume=778747,
        fiftyTwoWeekHigh=316.39,
        fiftyTwoWeekLow=216.24,
        recommendationKey='buy',
        industry='Specialty Chemicals'
    )
    db.session.add(APD)

    AKAM = Stock(
        name='Akamai Technologies, Inc.',
        ticker='AKAM',
        marketCap=14810577920,
        dayHigh=95.105,
        dayLow=92.25,
        currentPrice=92.39,
        longBusinessSummary='Akamai Technologies, Inc. provides cloud services for securing, delivering, and optimizing content and business applications over the internet in the United States and internationally. The company offers cloud solutions to keep infrastructure, websites, applications, application programming interfaces, and users safe from various cyberattacks and online threats while enhancing performance. It also provides web and mobile performance solutions to enable dynamic websites and applications; media delivery solutions, including video streaming and video player services, game and software delivery, broadcast operations, authoritative domain name system, resolution, and data and analytics; and edge compute solutions to enable developers to deploy and distribute code at the edge. In addition, the company offers carrier offerings, including cybersecurity protection, parental controls, DNS infrastructure and content delivery solutions; and an array of service and support to assist customers with integrating, configuring, optimizing, and managing its offerings. It sells its solutions through direct sales and service organizations, as well as through various channel partners. Akamai Technologies, Inc. was incorporated in 1998 and is headquartered in Cambridge, Massachusetts.',
        fullTimeEmployees=9180,
        city='Cambridge',
        state='MA',
        trailingPE=24.816008,
        dividendYield=None,
        averageVolume=1788009,
        regularMarketOpen=94.6,
        volume=1245456,
        fiftyTwoWeekHigh=123.25,
        fiftyTwoWeekLow=86.99,
        recommendationKey='buy',
        industry='Software—Infrastructure'
    )
    db.session.add(AKAM)

    ALK = Stock(
        name='Alaska Air Group, Inc.',
        ticker='ALK',
        marketCap=5142031360,
        dayHigh=42.8,
        dayLow=40.6805,
        currentPrice=40.78,
        longBusinessSummary='Alaska Air Group, Inc., through its subsidiaries, provides passenger and cargo air transportation services. The company operates through three segments: Mainline, Regional, and Horizon. It flies to approximately 120 destinations throughout North America. Alaska Air Group, Inc. was founded in 1932 and is based in Seattle, Washington.',
        fullTimeEmployees=21582,
        city='Seattle',
        state='WA',
        trailingPE=11.160372,
        dividendYield=None,
        averageVolume=1955245,
        regularMarketOpen=41.54,
        volume=1179241,
        fiftyTwoWeekHigh=63.76,
        fiftyTwoWeekLow=38.19,
        recommendationKey='buy',
        industry='Airlines'
    )
    db.session.add(ALK)

    ALB = Stock(
        name='Albemarle Corporation',
        ticker='ALB',
        marketCap=26138449920,
        dayHigh=232.78,
        dayLow=222.215,
        currentPrice=223.19,
        longBusinessSummary='Albemarle Corporation develops, manufactures, and markets engineered specialty chemicals worldwide. It operates through three segments: Lithium, Bromine, and Catalysts. The Lithium segment offers lithium compounds, including lithium carbonate, lithium hydroxide, lithium chloride, and lithium specialties; and reagents, such as butyllithium and lithium aluminum hydride for use in lithium batteries for consumer electronics and electric vehicles, high performance greases, thermoplastic elastomers for car tires, rubber soles, plastic bottles, catalysts for chemical reactions, organic synthesis processes in the areas of steroid chemistry and vitamins, life sciences, pharmaceutical industry, and other markets. It also provides cesium products for the chemical and pharmaceutical industries; zirconium, barium, and titanium products for pyrotechnical applications that include airbag initiators; technical services for the handling and use of reactive lithium products; and lithium-containing by-products recycling services. The Bromine segment offers bromine and bromine-based fire safety solutions; specialty chemicals, including elemental bromine, alkyl and inorganic bromides, brominated powdered activated carbon, and other bromine fine chemicals for use in chemical synthesis, oil and gas well drilling and completion fluids, mercury control, water purification, beef and poultry processing, and other industrial applications; and other specialty chemicals, such as tertiary amines for surfactants, biocides, and disinfectants and sanitizers. The Catalysts segment provides hydroprocessing, isomerization, and akylation catalysts; fluidized catalytic cracking catalysts and additives; and organometallics and curatives. The company serves the energy storage, petroleum refining, consumer electronics, construction, automotive, lubricants, pharmaceuticals, and crop protection markets. Albemarle Corporation was founded in 1887 and is headquartered in Charlotte, North Carolina.',
        fullTimeEmployees=6000,
        city='Charlotte',
        state='NC',
        trailingPE=94.173004,
        dividendYield=0.0069999998,
        averageVolume=1359479,
        regularMarketOpen=226,
        volume=1584952,
        fiftyTwoWeekHigh=291.48,
        fiftyTwoWeekLow=163.2,
        recommendationKey='buy',
        industry='Specialty Chemicals'
    )
    db.session.add(ALB)

    ARE = Stock(
        name='Alexandria Real Estate Equities, Inc.',
        ticker='ARE',
        marketCap=23585001472,
        dayHigh=148.527,
        dayLow=144.23,
        currentPrice=144.5,
        longBusinessSummary='Alexandria Real Estate Equities, Inc. (NYSE:ARE), an S&P 500<sup>®</sup> urban office real estate investment trust ("REIT"), is the first, longest-tenured, and pioneering owner, operator, and developer uniquely focused on collaborative life science, technology, and agtech campuses in AAA innovation cluster locations, with a total market capitalization of $31.9 billion as of December 31, 2020, and an asset base in North America of 49.7 million square feet ("SF"). The asset base in North America includes 31.9 million RSF of operating properties and 3.3 million RSF of Class A properties undergoing construction, 7.1 million RSF of near-term and intermediate-term development and redevelopment projects, and 7.4 million SF of future development projects. Founded in 1994, Alexandria pioneered this niche and has since established a significant market presence in key locations, including Greater Boston, San Francisco, New York City, San Diego, Seattle, Maryland, and Research Triangle. Alexandria has a longstanding and proven track record of developing Class A properties clustered in urban life science, technology, and agtech campuses that provide our innovative tenants with highly dynamic and collaborative environments that enhance their ability to successfully recruit and retain world-class talent and inspire productivity, efficiency, creativity, and success. Alexandria also provides strategic capital to transformative life science, technology, and agtech companies through our venture capital platform. We believe our unique business model and diligent underwriting ensure a high-quality and diverse tenant base that results in higher occupancy levels, longer lease terms, higher rental income, higher returns, and greater long-term asset value.',
        fullTimeEmployees=559,
        city='Pasadena',
        state='CA',
        trailingPE=54.323307,
        dividendYield=0.0359,
        averageVolume=1094419,
        regularMarketOpen=146.51,
        volume=1403266,
        fiftyTwoWeekHigh=224.95,
        fiftyTwoWeekLow=130,
        recommendationKey='buy',
        industry='REIT—Office'
    )
    db.session.add(ARE)

    ALGN = Stock(
        name='Align Technology, Inc.',
        ticker='ALGN',
        marketCap=19064627200,
        dayHigh=254.76,
        dayLow=241.44,
        currentPrice=241.92,
        longBusinessSummary="Align Technology, Inc., a medical device company, designs, manufactures, and markets Invisalign clear aligners and iTero intraoral scanners and services for orthodontists and general practitioner dentists, and restorative and aesthetic dentistry. It operates in two segments, Clear Aligner; and Scanners and Services. The Clear Aligner segment consists of comprehensive products, including Invisalign comprehensive treatment that addresses the orthodontic needs of teenage patients, such as mandibular advancement, compliance indicators, and compensation for tooth eruption; and Invisalign First Phase I and Invisalign First Comprehensive Phase 2 package for younger patients generally between the ages of seven and ten years, which is a mixture of primary/baby and permanent teeth. This segment's non-comprehensive products comprise Invisalign moderate, lite and express packages, and Invisalign go; and non-case products include retention products, Invisalign training fees, and sales of ancillary products, such as cleaning material, and adjusting tools used by dental professionals during the course of treatment. The Scanners and Services segment offers iTero scanner, a single hardware platform with software options for restorative or orthodontic procedures; restorative software for general practitioner dentists, prosthodontists, periodontists, and oral surgeons; and software for orthodontists for digital records storage, orthodontic diagnosis, and for the fabrication of printed models and retainers. This segment also provides computer-aided design and computer-aided manufacturing services; ancillary products, such as disposable sleeves for the wand; iTero model and dies; third party scanners and digital scans; Invisalign outcome simulator, a chair-side and cloud-based application for the iTero scanner; Invisalign progress assessment tool; and TimeLapse technology, which allows doctors or practitioners to compare a patient's historic 3D scans to the present-day scan. The company sells its products in the United States, Switzerland, China, and internationally. Align Technology, Inc. was incorporated in 1997 and is headquartered in Tempe, Arizona.",
        fullTimeEmployees=23625,
        city='Tempe',
        state='AZ',
        trailingPE=27.234041,
        dividendYield=None,
        averageVolume=1120067,
        regularMarketOpen=251.51,
        volume=696475,
        fiftyTwoWeekHigh=737.45,
        fiftyTwoWeekLow=225.86,
        recommendationKey='buy',
        industry='Medical Devices'
    )
    db.session.add(ALGN)

    LNT = Stock(
        name='Alliant Energy Corporation',
        ticker='LNT',
        marketCap=14554735616,
        dayHigh=58.68,
        dayLow=57.98,
        currentPrice=58.03,
        longBusinessSummary='Alliant Energy Corporation operates as a utility holding company that provides regulated electricity and natural gas services. It operates through three segments: Utility Electric Operations, Utility Gas Operations, and Utility Other. The company, through its subsidiary, Interstate Power and Light Company (IPL), primarily generates and distributes electricity, and distributes and transports natural gas to retail customers in Iowa; sells electricity to wholesale customers in Minnesota, Illinois, and Iowa; and generates and distributes steam in Cedar Rapids, Iowa. Alliant Energy Corporation, through its other subsidiary, Wisconsin Power and Light Company (WPL), generates and distributes electricity, and distributes and transports natural gas to retail customers in Wisconsin; and sells electricity to wholesale customers in Wisconsin. As of December 31, 2021, IPL supplied electric and natural gas service to approximately 500,000 and 225,000 retail customers respectively; and WPL supplied electric and natural gas service to approximately 485,000 and 200,000 retail customers, respectively. It serves retail customers in the farming, agriculture, industrial manufacturing, chemical, and packaging and food industries. In addition, the company owns and operates a short-line rail freight service in Iowa; a barge, rail, and truck freight terminal on the Mississippi River; and a rail-served warehouse in Iowa, as well as offers freight brokerage services. Further, it holds interests in a 347 megawatt (MW) natural gas-fired electric generating unit near Sheboygan Falls, Wisconsin; and a 225 MW wind farm located in Oklahoma. The company was incorporated in 1981 and is headquartered in Madison, Wisconsin.',
        fullTimeEmployees=3313,
        city='Madison',
        state='WI',
        trailingPE=21.365978,
        dividendYield=0.031,
        averageVolume=1798269,
        regularMarketOpen=58.15,
        volume=1237861,
        fiftyTwoWeekHigh=65.37,
        fiftyTwoWeekLow=54.2,
        recommendationKey='buy',
        industry='Utilities—Regulated Electric'
    )
    db.session.add(LNT)

    ALL = Stock(
        name='The Allstate Corporation',
        ticker='ALL',
        marketCap=34565361664,
        dayHigh=128.07,
        dayLow=125.61,
        currentPrice=125.7,
        longBusinessSummary='The Allstate Corporation, together with its subsidiaries, provides property and casualty, and other insurance products in the United States and Canada. The company operates through Allstate Protection; Protection Services; Allstate Health and Benefits; and Run-off Property-Liability segments. The Allstate Protection segment offers private passenger auto and homeowners insurance; specialty auto products, including motorcycle, trailer, motor home, and off-road vehicle insurance; other personal lines products, such as renter, condominium, landlord, boat, umbrella, and manufactured home and stand-alone scheduled personal property; and commercial lines products under the Allstate and Encompass brand names. The Protection Services segment provides consumer product protection plans and related technical support for mobile phones, consumer electronics, furniture, and appliances; finance and insurance products, including vehicle service contracts, guaranteed asset protection waivers, road hazard tire and wheel, and paint and fabric protection; roadside assistance; device and mobile data collection services; data and analytic solutions using automotive telematics information; and identity protection services. This segment offers its products under various brands including Allstate Protection Plans, Allstate Dealer Services, Allstate Roadside Services, Arity, and Allstate Identity Protection. The Allstate Health and Benefits provides life, accident, critical illness, short-term disability, and other health insurance products. The Run-off Property-Liability offers property and casualty insurance. It sells its products through call centers, agencies, financial specialists, independent agents, brokers, wholesale partners, and affinity groups, as well as through online and mobile applications. The Allstate Corporation was founded in 1931 and is based in Northbrook, Illinois.',
        fullTimeEmployees=54300,
        city='Northbrook',
        state='IL',
        trailingPE=11.084656,
        dividendYield=0.0269,
        averageVolume=1804624,
        regularMarketOpen=127.22,
        volume=1341251,
        fiftyTwoWeekHigh=144.46,
        fiftyTwoWeekLow=106.11,
        recommendationKey='buy',
        industry='Insurance—Property & Casualty'
    )
    db.session.add(ALL)

    GOOGL = Stock(
        name='Alphabet Inc.',
        ticker='GOOGL',
        marketCap=1487013806080,
        dayHigh=2346.19,
        dayLow=2236.96,
        currentPrice=2240.15,
        longBusinessSummary='Alphabet Inc. provides various products and platforms in the United States, Europe, the Middle East, Africa, the Asia-Pacific, Canada, and Latin America. It operates through Google Services, Google Cloud, and Other Bets segments. The Google Services segment offers products and services, including ads, Android, Chrome, hardware, Gmail, Google Drive, Google Maps, Google Photos, Google Play, Search, and YouTube. It is also involved in the sale of apps and in-app purchases and digital content in the Google Play store; and Fitbit wearable devices, Google Nest home products, Pixel phones, and other devices, as well as in the provision of YouTube non-advertising services. The Google Cloud segment offers infrastructure, platform, and other services; Google Workspace that include cloud-based collaboration tools for enterprises, such as Gmail, Docs, Drive, Calendar, and Meet; and other services for enterprise customers. The Other Bets segment sells health technology and internet services. The company was founded in 1998 and is headquartered in Mountain View, California.',
        fullTimeEmployees=163906,
        city='Mountain View',
        state='CA',
        trailingPE=21.580366,
        dividendYield=None,
        averageVolume=1911306,
        regularMarketOpen=2316.05,
        volume=1710148,
        fiftyTwoWeekHigh=3030.93,
        fiftyTwoWeekLow=2037.69,
        recommendationKey='buy',
        industry='Internet Content & Information'
    )
    db.session.add(GOOGL)

    GOOG = Stock(
        name='Alphabet Inc.',
        ticker='GOOG',
        marketCap=1477365858304,
        dayHigh=2357.13,
        dayLow=2248.88,
        currentPrice=2251.43,
        longBusinessSummary='Alphabet Inc. provides various products and platforms in the United States, Europe, the Middle East, Africa, the Asia-Pacific, Canada, and Latin America. It operates through Google Services, Google Cloud, and Other Bets segments. The Google Services segment offers products and services, including ads, Android, Chrome, hardware, Gmail, Google Drive, Google Maps, Google Photos, Google Play, Search, and YouTube. It is also involved in the sale of apps and in-app purchases and digital content in the Google Play store; and Fitbit wearable devices, Google Nest home products, Pixel phones, and other devices, as well as in the provision of YouTube non-advertising services. The Google Cloud segment offers infrastructure, platform, and other services; Google Workspace that include cloud-based collaboration tools for enterprises, such as Gmail, Docs, Drive, Calendar, and Meet; and other services for enterprise customers. The Other Bets segment sells health technology and internet services. The company was founded in 1998 and is headquartered in Mountain View, California.',
        fullTimeEmployees=163906,
        city='Mountain View',
        state='CA',
        trailingPE=20.35927,
        dividendYield=None,
        averageVolume=1535167,
        regularMarketOpen=2327.02,
        volume=1394155,
        fiftyTwoWeekHigh=3042,
        fiftyTwoWeekLow=2044.16,
        recommendationKey='strong_buy',
        industry='Internet Content & Information'
    )
    db.session.add(GOOG)

    MO = Stock(
        name='Altria Group, Inc.',
        ticker='MO',
        marketCap=78198087680,
        dayHigh=44.11,
        dayLow=43.01,
        currentPrice=43.19,
        longBusinessSummary='Altria Group, Inc., through its subsidiaries, manufactures and sells smokeable and oral tobacco products in the United States. The company provides cigarettes primarily under the Marlboro brand; cigars and pipe tobacco principally under the Black & Mild brand; and moist smokeless tobacco products under the Copenhagen, Skoal, Red Seal, and Husky brands, as well as provides on! oral nicotine pouches. It sells its tobacco products primarily to wholesalers, including distributors; and large retail organizations, such as chain stores. Altria Group, Inc. was founded in 1822 and is headquartered in Richmond, Virginia.',
        fullTimeEmployees=6000,
        city='Richmond',
        state='VA',
        trailingPE=26.175756,
        dividendYield=0.0834,
        averageVolume=11946725,
        regularMarketOpen=43.72,
        volume=8498370,
        fiftyTwoWeekHigh=57.05,
        fiftyTwoWeekLow=41,
        recommendationKey='hold',
        industry='Tobacco'
    )
    db.session.add(MO)

    AMZN = Stock(
        name='Amazon.com, Inc.',
        ticker='AMZN',
        marketCap=1092730617856,
        dayHigh=114.85,
        dayLow=107.13,
        currentPrice=107.4,
        longBusinessSummary='Amazon.com, Inc. engages in the retail sale of consumer products and subscriptions in North America and internationally. The company operates through three segments: North America, International, and Amazon Web Services (AWS). It sells merchandise and content purchased for resale from third-party sellers through physical and online stores. The company also manufactures and sells electronic devices, including Kindle, Fire tablets, Fire TVs, Rings, and Echo and other devices; provides Kindle Direct Publishing, an online service that allows independent authors and publishers to make their books available in the Kindle Store; and develops and produces media content. In addition, it offers programs that enable sellers to sell their products on its websites, as well as its stores; and programs that allow authors, musicians, filmmakers, Twitch streamers, skill and app developers, and others to publish and sell content. Further, the company provides compute, storage, database, analytics, machine learning, and other services, as well as fulfillment, advertising, publishing, and digital content subscriptions. Additionally, it offers Amazon Prime, a membership program, which provides free shipping of various items; access to streaming of movies and series; and other services. The company serves consumers, sellers, developers, enterprises, and content creators. Amazon.com, Inc. was incorporated in 1994 and is headquartered in Seattle, Washington.',
        fullTimeEmployees=1622000,
        city='Seattle',
        state='WA',
        trailingPE=51.51079,
        dividendYield=None,
        averageVolume=87643001,
        regularMarketOpen=113.5,
        volume=73274005,
        fiftyTwoWeekHigh=188.654,
        fiftyTwoWeekLow=101.26,
        recommendationKey='buy',
        industry='Internet Retail'
    )
    db.session.add(AMZN)

    AMD = Stock(
        name='Advanced Micro Devices, Inc.',
        ticker='AMD',
        marketCap=130904793088,
        dayHigh=86.73,
        dayLow=80.43,
        currentPrice=80.78,
        longBusinessSummary='Advanced Micro Devices, Inc. operates as a semiconductor company worldwide. The company operates in two segments, Computing and Graphics; and Enterprise, Embedded and Semi-Custom. Its products include x86 microprocessors as an accelerated processing unit, chipsets, discrete and integrated graphics processing units (GPUs), data center and professional GPUs, and development services; and server and embedded processors, and semi-custom System-on-Chip (SoC) products, development services, and technology for game consoles. The company provides processors for desktop and notebook personal computers under the AMD Ryzen, AMD Ryzen PRO, Ryzen Threadripper, Ryzen Threadripper PRO, AMD Athlon, AMD Athlon PRO, AMD FX, AMD A-Series, and AMD PRO A-Series processors brands; discrete GPUs for desktop and notebook PCs under the AMD Radeon graphics, AMD Embedded Radeon graphics brands; and professional graphics products under the AMD Radeon Pro and AMD FirePro graphics brands. It also offers Radeon Instinct, Radeon PRO V-series, and AMD Instinct accelerators for servers; chipsets under the AMD trademark; microprocessors for servers under the AMD EPYC; embedded processor solutions under the AMD Athlon, AMD Geode, AMD Ryzen, AMD EPYC, AMD R-Series, and G-Series processors brands; and customer-specific solutions based on AMD CPU, GPU, and multi-media technologies, as well as semi-custom SoC products. It serves original equipment manufacturers, public cloud service providers, original design manufacturers, system integrators, independent distributors, online retailers, and add-in-board manufacturers through its direct sales force, independent distributors, and sales representatives. The company was incorporated in 1969 and is headquartered in Santa Clara, California.',
        fullTimeEmployees=15500,
        city='Santa Clara',
        state='CA',
        trailingPE=30.311445,
        dividendYield=None,
        averageVolume=107799738,
        regularMarketOpen=85.71,
        volume=94650512,
        fiftyTwoWeekHigh=164.46,
        fiftyTwoWeekLow=79.43,
        recommendationKey='buy',
        industry='Semiconductors'
    )
    db.session.add(AMD)

    AEE = Stock(
        name='Ameren Corporation',
        ticker='AEE',
        marketCap=23137138688,
        dayHigh=90.4,
        dayLow=89.055,
        currentPrice=89.6,
        longBusinessSummary='Ameren Corporation, together with its subsidiaries, operates as a public utility holding company in the United States. It operates through four segments: Ameren Missouri, Ameren Illinois Electric Distribution, Ameren Illinois Natural Gas, and Ameren Transmission. The company engages in the rate-regulated electric generation, transmission, and distribution activities; and rate-regulated natural gas distribution and transmission businesses. It primarily generates electricity through coal, nuclear, and natural gas, as well as renewable sources, such as hydroelectric, wind, methane gas, and solar. The company serves residential, commercial, and industrial customers. Ameren Corporation was founded in 1881 and is headquartered in St. Louis, Missouri.',
        fullTimeEmployees=9116,
        city='Saint Louis',
        state='MO',
        trailingPE=22.974358,
        dividendYield=0.026500002,
        averageVolume=1461700,
        regularMarketOpen=89.36,
        volume=1581358,
        fiftyTwoWeekHigh=99.2,
        fiftyTwoWeekLow=79.35,
        recommendationKey='buy',
        industry='Utilities—Regulated Electric'
    )
    db.session.add(AEE)

    AEP = Stock(
        name='American Electric Power Company, Inc.',
        ticker='AEP',
        marketCap=48827764736,
        dayHigh=96.19,
        dayLow=94.82,
        currentPrice=95.08,
        longBusinessSummary='American Electric Power Company, Inc., an electric public utility holding company, engages in the generation, transmission, and distribution of electricity for sale to retail and wholesale customers in the United States. It operates through Vertically Integrated Utilities, Transmission and Distribution Utilities, AEP Transmission Holdco, and Generation & Marketing segments. The company generates electricity using coal and lignite, natural gas, nuclear, hydro, solar, wind, and other energy sources. It also supplies and markets electric power at wholesale to other electric utility companies, rural electric cooperatives, municipalities, and other market participants. American Electric Power Company, Inc. was incorporated in 1906 and is headquartered in Columbus, Ohio.',
        fullTimeEmployees=16688,
        city='Columbus',
        state='OH',
        trailingPE=18.21456,
        dividendYield=0.033800002,
        averageVolume=2862501,
        regularMarketOpen=95.09,
        volume=2318449,
        fiftyTwoWeekHigh=104.81,
        fiftyTwoWeekLow=80.22,
        recommendationKey='buy',
        industry='Utilities—Regulated Electric'
    )
    db.session.add(AEP)

    AXP = Stock(
        name='American Express Company',
        ticker='AXP',
        marketCap=107077599232,
        dayHigh=149.51,
        dayLow=141.85,
        currentPrice=142.19,
        longBusinessSummary="American Express Company, together with its subsidiaries, provides charge and credit payment card products, and travel-related services worldwide. The company operates through three segments: Global Consumer Services Group, Global Commercial Services, and Global Merchant and Network Services. Its products and services include payment and financing products; network services; accounts payable expense management products and services; and travel and lifestyle services. The company's products and services also comprise merchant acquisition and processing, servicing and settlement, point-of-sale marketing, and information products and services for merchants; and fraud prevention services, as well as the design and operation of customer loyalty programs. It sells its products and services to consumers, small businesses, mid-sized companies, and large corporations through mobile and online applications, third-party vendors and business partners, direct mail, telephone, in-house sales teams, and direct response advertising. American Express Company was founded in 1850 and is headquartered in New York, New York.",
        fullTimeEmployees=64000,
        city='New York',
        state='NY',
        trailingPE=14.2246895,
        dividendYield=0.014400001,
        averageVolume=3376162,
        regularMarketOpen=146.08,
        volume=2535633,
        fiftyTwoWeekHigh=199.55,
        fiftyTwoWeekLow=136.49,
        recommendationKey='buy',
        industry='Credit Services'
    )
    db.session.add(AXP)

    AIG = Stock(
        name='American International Group, Inc.',
        ticker='AIG',
        marketCap=41043468288,
        dayHigh=53.41,
        dayLow=51.77,
        currentPrice=51.81,
        longBusinessSummary="American International Group, Inc. offers insurance products for commercial, institutional, and individual customers in North America and internationally. The company's General Insurance segment provides general liability, environmental, commercial automobile liability, workers' compensation, casualty, and crisis management insurance products; commercial, industrial, and energy-related property insurance; and aerospace, political risk, trade credit, portfolio solutions, crop, and marine insurance. It also provides professional liability insurance products for a range of businesses and risks, including directors and officers, mergers and acquisitions, fidelity, employment practices, fiduciary liability, cyber risk, kidnap and ransom, and errors and omissions insurance. In addition, this segment offers personal auto and property insurance, such as auto, homeowners, umbrella, yacht, fine art, and collections; voluntary and sponsor-paid personal accident; supplemental health products; extended warranty insurance products; and travel insurance products. Its Life and Retirement segment offers variable annuities, index and fixed annuities, and retail mutual funds; and financial planning and advisory services; record-keeping, plan administrative, and compliance services; and term life and universal life insurance. It also provides stable value wrap products, and structured settlement and pension risk transfer annuities; and corporate- and bank-owned life insurance and guaranteed investment contracts. This segment sells its products through independent marketing organizations, independent insurance agents, financial advisors, direct marketing, banks, and broker-dealers. The company was founded in 1919 and is headquartered in New York, New York.",
        fullTimeEmployees=36600,
        city='New York',
        state='NY',
        trailingPE=4.481834,
        dividendYield=0.0247,
        averageVolume=5362850,
        regularMarketOpen=52.69,
        volume=3494445,
        fiftyTwoWeekHigh=65.73,
        fiftyTwoWeekLow=44.54,
        recommendationKey='buy',
        industry='Insurance—Diversified'
    )
    db.session.add(AIG)

    AMT = Stock(
        name='American Tower Corporation',
        ticker='AMT',
        marketCap=117535809536,
        dayHigh=260.48,
        dayLow=252.15,
        currentPrice=252.93,
        longBusinessSummary='American Tower Corporation, one of the largest global REITs, is a leading independent owner, operator and developer of multitenant communications real estate with a portfolio of approximately 219,000 communications sites. For more information about American Tower, please visit the Earnings Materials and Investor Presentations sections of our investor relations website at www.americantower.com.',
        fullTimeEmployees=6378,
        city='Boston',
        state='MA',
        trailingPE=43.835354,
        dividendYield=0.0221,
        averageVolume=2160550,
        regularMarketOpen=260,
        volume=1601688,
        fiftyTwoWeekHigh=303.72,
        fiftyTwoWeekLow=220,
        recommendationKey='buy',
        industry='REIT—Specialty'
    )
    db.session.add(AMT)

    AWK = Stock(
        name='American Water Works Company, Inc.',
        ticker='AWK',
        marketCap=26372360192,
        dayHigh=149.51,
        dayLow=144.9765,
        currentPrice=145.1,
        longBusinessSummary='American Water Works Company, Inc., through its subsidiaries, provides water and wastewater services in the United States. It offers water and wastewater services to approximately 1,700 communities in 14 states serving approximately 3.4 million active customers. The company serves residential customers; commercial customers, including food and beverage providers, commercial property developers and proprietors, and energy suppliers; fire service and private fire customers; industrial customers, such as large-scale manufacturers, mining, and production operations; public authorities comprising government buildings and other public sector facilities, such as schools and universities; and other utilities and community water and wastewater systems. It also provides water and wastewater services on various military installations; and undertakes contracts with municipal customers, primarily to operate and manage water and wastewater facilities, as well as offers other related services. In addition, the company operates approximately 80 surface water treatment plants; 480 groundwater treatment plants; 160 wastewater treatment plants; 52,500 miles of transmission, distribution, and collection mains and pipes; 1,100 groundwater wells; 1,700 water and wastewater pumping stations; 1,300 treated water storage facilities; and 76 dams. It serves approximately 14 million people with drinking water, wastewater, and other related services in 24 states. American Water Works Company, Inc. was founded in 1886 and is headquartered in Camden, New Jersey.',
        fullTimeEmployees=6400,
        city='Camden',
        state='NJ',
        trailingPE=20.532051,
        dividendYield=0.0199,
        averageVolume=925022,
        regularMarketOpen=149.09,
        volume=763805,
        fiftyTwoWeekHigh=189.65,
        fiftyTwoWeekLow=129.45,
        recommendationKey='hold',
        industry='Utilities—Regulated Water'
    )
    db.session.add(AWK)

    AMP = Stock(
        name='Ameriprise Financial, Inc.',
        ticker='AMP',
        marketCap=26790199296,
        dayHigh=252.775,
        dayLow=243.64,
        currentPrice=243.76,
        longBusinessSummary='Ameriprise Financial, Inc., through its subsidiaries, provides various financial products and services to individual and institutional clients in the United States and internationally. It operates through four segments: Advice & Wealth Management, Asset Management, Retirement & Protection Solutions, and Corporate & Other. The Advice & Wealth Management segment provides financial planning and advice; brokerage products and services for retail and institutional clients; discretionary and non-discretionary investment advisory accounts; mutual funds; insurance and annuities products; cash management and banking products; and face-amount certificates. The Asset Management segment offers investment management and advice, and investment products to retail, high net worth, and institutional clients through unaffiliated third-party financial institutions and institutional sales force. This segment products also include U.S. mutual funds and their non-U.S. equivalents, exchange-traded funds, variable product funds underlying insurance, and annuity separate accounts; and institutional asset management products, such as traditional asset classes, separately managed accounts, individually managed accounts, collateralized loan obligations, hedge funds, collective funds, and property and infrastructure funds. The Retirement & Protection Solutions segment provides variable annuity products to individual clients, as well as life and DI insurance products to retail clients. The company was formerly known as American Express Financial Corporation and changed its name to Ameriprise Financial, Inc. in September 2005. Ameriprise Financial, Inc. was founded in 1894 and is headquartered in Minneapolis, Minnesota.',
        fullTimeEmployees=12000,
        city='Minneapolis',
        state='MN',
        trailingPE=9.367458,
        dividendYield=0.020599999,
        averageVolume=639064,
        regularMarketOpen=250.66,
        volume=587450,
        fiftyTwoWeekHigh=332.37,
        fiftyTwoWeekLow=233.16,
        recommendationKey='buy',
        industry='Asset Management'
    )
    db.session.add(AMP)

    ABC = Stock(
        name='AmerisourceBergen Corporation',
        ticker='ABC',
        marketCap=29993150464,
        dayHigh=150,
        dayLow=143.15,
        currentPrice=143.19,
        longBusinessSummary="AmerisourceBergen Corporation sources and distributes pharmaceutical products in the United States and internationally. Its Pharmaceutical Distribution segment distributes brand-name and generic pharmaceuticals, over-the-counter healthcare products, home healthcare supplies and equipment, and related services to various healthcare providers, including acute care hospitals and health systems, independent and chain retail pharmacies, mail order pharmacies, medical clinics, long-term care and alternate site pharmacies, and other customers. It also provides pharmacy management, staffing, and other consulting services; supply management software to retail and institutional healthcare providers; and packaging solutions to various institutional and retail healthcare providers. In addition, this segment distributes plasma and other blood products, injectable pharmaceuticals, vaccines, and other specialty products; provides other services primarily to physicians who specialize in various disease states, primarily oncology, as well as to other healthcare providers, including hospitals and dialysis clinics; and offers data analytics, outcomes research, and additional services for biotechnology and pharmaceutical manufacturers. The company's Other segment provides integrated manufacturer services, such as clinical trial support, product post-approval, and commercialization support; specialty transportation and logistics services for the biopharmaceutical industry; and sells pharmaceuticals, vaccines, parasiticides, diagnostics, micro feed ingredients, and various other products to customers in the companion animal and production animal markets, as well as demand-creating sales force services to manufacturers. AmerisourceBergen Corporation was incorporated in 2001 and is headquartered in Conshohocken, Pennsylvania.",
        fullTimeEmployees=38000,
        city='Conshohocken',
        state='PA',
        trailingPE=17.466455,
        dividendYield=0.0128,
        averageVolume=1581291,
        regularMarketOpen=148.9,
        volume=1731808,
        fiftyTwoWeekHigh=167.19,
        fiftyTwoWeekLow=111.34,
        recommendationKey='buy',
        industry='Medical Distribution'
    )
    db.session.add(ABC)

    AME = Stock(
        name='AMETEK, Inc.',
        ticker='AME',
        marketCap=25427810304,
        dayHigh=113.71,
        dayLow=109.91,
        currentPrice=110.12,
        longBusinessSummary="AMETEK, Inc. manufactures and sells electronic instruments and electromechanical devices worldwide. It operates in two segments, Electronic Instruments (EIG) and Electromechanical (EMG). The company's EIG segment offers advanced instruments for the process, aerospace, power, and industrial markets; process and analytical instruments for the oil and gas, petrochemical, pharmaceutical, semiconductor, automation, and food and beverage industries; and instruments to the laboratory equipment, ultra-precision manufacturing, medical, and test and measurement markets. This segment also provides power quality monitoring and metering devices, uninterruptible power supplies, programmable power equipment, electromagnetic compatibility test equipment, gas turbines, and environmental health and safety market sensors, dashboard instruments for heavy trucks and other vehicles, and instrumentation and controls for the food and beverage industries; and aircraft and engine sensors, monitoring systems, power supplies, fuel and fluid measurement systems, and data acquisition systems for the aerospace industry. Its EMG segment offers engineered electrical connectors and electronics packaging to protect sensitive devices and mission-critical electronics; precision motion control products for data storage, medical devices, business equipment, automation, and other applications; high-purity powdered metals, strips and foils, specialty clad metals, and metal matrix composites; motor-blower systems and heat exchangers for use in thermal management, military, commercial aircraft, and military ground vehicles; and motors for use in commercial appliances, fitness equipment, food and beverage machines, hydraulic pumps, and industrial blowers. This segment also operates a network of aviation maintenance, repair, and overhaul facilities. In addition, the company offers clinical and educational communication solutions. AMETEK, Inc. was founded in 1930 and is headquartered in Berwyn, Pennsylvania.",
        fullTimeEmployees=18500,
        city='Berwyn',
        state='PA',
        trailingPE=24.580359,
        dividendYield=0.0078,
        averageVolume=1145341,
        regularMarketOpen=113.12,
        volume=998359,
        fiftyTwoWeekHigh=148.07,
        fiftyTwoWeekLow=106.17,
        recommendationKey='buy',
        industry='Specialty Industrial Machinery'
    )
    db.session.add(AME)

    AMGN = Stock(
        name='Amgen Inc.',
        ticker='AMGN',
        marketCap=137160900608,
        dayHigh=247.58,
        dayLow=243.39,
        currentPrice=243.51,
        longBusinessSummary="Amgen Inc. discovers, develops, manufactures, and delivers human therapeutics worldwide. It focuses on inflammation, oncology/hematology, bone health, cardiovascular disease, nephrology, and neuroscience areas. The company's products include Enbrel to treat plaque psoriasis, rheumatoid arthritis, and psoriatic arthritis; Neulasta that reduces the chance of infection due a low white blood cell count in patients cancer; Prolia to treat postmenopausal women with osteoporosis; Xgeva for skeletal-related events prevention; Otezla for the treatment of adult patients with plaque psoriasis, psoriatic arthritis, and oral ulcers associated with Behçet's disease; Aranesp to treat a lower-than-normal number of red blood cells and anemia; KYPROLIS to treat patients with relapsed or refractory multiple myeloma; and Repatha, which reduces the risks of myocardial infarction, stroke, and coronary revascularization. It also markets Nplate, Vectibix, MVASI, Parsabiv, EPOGEN, KANJINTI, BLINCYTO, Aimovig, EVENITY, AMGEVITATM, Sensipar/Mimpara, NEUPOGEN, IMLYGIC, Corlanor, and AVSOLA. Amgen Inc. serves healthcare providers, including physicians or their clinics, dialysis centers, hospitals, and pharmacies. It distributes its products through pharmaceutical wholesale distributors, as well as direct-to-consumer channels. It has collaboration agreements with Novartis Pharma AG; UCB; Bayer HealthCare LLC; BeiGene, Ltd.; Eli Lilly and Company; Datos Health; and Verastem, Inc. to evaluate VS-6766 in combination with lumakrastm (Sotorasib) in patients with KRAS G12C-mutant non-small cell lung cancer. It has an agreement with Kyowa Kirin Co., Ltd. to jointly develop and commercialize KHK4083, a Phase 3-ready anti-OX40 fully human monoclonal antibody for the treatment of atopic dermatitis and other autoimmune diseases; and research and development collaboration with Neumora Therapeutics, Inc. and Plexium, Inc. Amgen Inc. was incorporated in 1980 and is headquartered in Thousand Oaks, California.",
        fullTimeEmployees=24200,
        city='Thousand Oaks',
        state='CA',
        trailingPE=25.101534,
        dividendYield=0.0319,
        averageVolume=3310046,
        regularMarketOpen=245.93,
        volume=2378148,
        fiftyTwoWeekHigh=258.45,
        fiftyTwoWeekLow=198.64,
        recommendationKey='hold',
        industry='Drug Manufacturers—General'
    )
    db.session.add(AMGN)

    APH = Stock(
        name='Amphenol Corporation',
        ticker='APH',
        marketCap=38646771712,
        dayHigh=66.87,
        dayLow=64.61,
        currentPrice=64.72,
        longBusinessSummary='Amphenol Corporation, together with its subsidiaries, primarily designs, manufactures, and markets electrical, electronic, and fiber optic connectors in the United States, China, and internationally. It operates through three segments: Harsh Environment Solutions, Communications Solutions, and Interconnect and Sensor Systems. The company offers connectors and connector systems, including harsh environment data, power, high-speed, fiber optic, and radio frequency interconnect products; busbars and power distribution systems; and other connectors. It also provides value-add products, such as backplane interconnect systems, cable assemblies and harnesses, and cable management products; other products comprising flexible and rigid printed circuit boards, hinges, other mechanical, and production related products. In addition, the company offers consumer device, network infrastructure, and other antennas; coaxial, power, and specialty cables; and sensors and sensor-based products. It sells its products through its sales force, independent representatives, and a network of electronics distributors to original equipment manufacturers, electronic manufacturing services companies, original design manufacturers, and service providers in the automotive, broadband communication, commercial aerospace, industrial, information technology and data communication, military, mobile device, and mobile network markets. Amphenol Corporation was founded in 1932 and is headquartered in Wallingford, Connecticut.',
        fullTimeEmployees=90000,
        city='Wallingford',
        state='CT',
        trailingPE=24.023756,
        dividendYield=0.0126,
        averageVolume=2473454,
        regularMarketOpen=66.47,
        volume=1713433,
        fiftyTwoWeekHigh=88.45,
        fiftyTwoWeekLow=61.67,
        recommendationKey='buy',
        industry='Electronic Components'
    )
    db.session.add(APH)

    ADI = Stock(
        name='Analog Devices, Inc.',
        ticker='ADI',
        marketCap=78006403072,
        dayHigh=153.14,
        dayLow=148.37,
        currentPrice=148.49,
        longBusinessSummary='Analog Devices, Inc. designs, manufactures, tests, and markets integrated circuits (ICs), software, and subsystems that leverage analog, mixed-signal, and digital signal processing technologies. The company provides data converter products, which translate real-world analog signals into digital data, as well as translates digital data into analog signals; power management and reference products for power conversion, driver monitoring, sequencing, and energy management applications in the automotive, communications, industrial, and high-end consumer markets; and power ICs include performance, integration, and software design simulation tools for accurate power supply designs. It also offers high-performance amplifiers to condition analog signals; and radio frequency and microwave ICs to support cellular infrastructure; and microelectromechanical systems technology solutions, including accelerometers used to sense acceleration, gyroscopes for sense rotation, inertial measurement units to sense multiple degrees of freedom, and broadband switches for radio and instrument systems, as well as isolators. In addition, the company offers digital signal processing and system products for high-speed numeric calculations. It serves clients in the industrial, automotive, consumer, instrumentation, aerospace, and communications markets through a direct sales force, third-party distributors, and independent sales representatives in the United States, the rest of North and South America, Europe, Japan, China, and rest of Asia, as well as through its Website. Analog Devices, Inc. was incorporated in 1965 and is headquartered in Wilmington, Massachusetts.',
        fullTimeEmployees=24700,
        city='Wilmington',
        state='MA',
        trailingPE=42.916187,
        dividendYield=0.019199999,
        averageVolume=3621933,
        regularMarketOpen=151.41,
        volume=2611843,
        fiftyTwoWeekHigh=191.95,
        fiftyTwoWeekLow=141.69,
        recommendationKey='buy',
        industry='Semiconductors'
    )
    db.session.add(ADI)

    ANSS = Stock(
        name='ANSYS, Inc.',
        ticker='ANSS',
        marketCap=20952934400,
        dayHigh=251.75,
        dayLow=239.94,
        currentPrice=240.14,
        longBusinessSummary='ANSYS, Inc. develops and markets engineering simulation software and services worldwide. It offers ANSYS Workbench, a framework upon which its multiphysics engineering simulation technologies are built and enables engineers to simulate the interactions between structures, heat transfer, fluids, electronics, and optical elements in a unified engineering simulation environment; high-performance computing product suite; power analysis and optimization software suite that manages the power budget, power delivery integrity, and power-induced noise in an electronic design; and structural analysis product suite that provides simulation tools for product design and optimization. The company also provides electronics product suite that offers field simulation software for designing electronic and electromechanical products; SCADE product suite, a solution for embedded software simulation, code production, and automated certification; fluids product suite that enables modeling of fluid flow and other related physical phenomena; Ansys Granta products to give access to material intelligence; photonic design and simulation tools; and optical sensor and closed-loop, and real-time simulation, as well as safety-certified embedded software solutions. In addition, the company provides Discovery product family for use in the simulation of product design; and academic product suite used in research and teaching settings, which allows students to become familiar with its simulation software. It serves engineers, designers, researchers, and students in the aerospace and defense, automotive transportation and mobility, construction, consumer products, energy, healthcare, high-tech, industrial equipment, materials and chemical processing, and sports industries. The company was founded in 1970 and is headquartered in Canonsburg, Pennsylvania.',
        fullTimeEmployees=5100,
        city='Canonsburg',
        state='PA',
        trailingPE=45.156075,
        dividendYield=None,
        averageVolume=548624,
        regularMarketOpen=250.75,
        volume=528779,
        fiftyTwoWeekHigh=413.89,
        fiftyTwoWeekLow=225.92,
        recommendationKey='hold',
        industry='Software—Application'
    )
    db.session.add(ANSS)

    ANTM = Stock(
        name='Anthem, Inc.',
        ticker='ANTM',
        marketCap=117129404416,
        dayHigh=485.745,
        dayLow=466.74,
        currentPrice=482.58,
        longBusinessSummary='Anthem, Inc., through its subsidiaries, operates as a health benefits company in the United States. It operates through four segments: Commercial & Specialty Business, Government Business, IngenioRx, and Other. The company offers a spectrum of network-based managed care health benefit plans to large and small groups, individuals, Medicaid, and Medicare markets. Its managed care plans include preferred provider organizations; health maintenance organizations; point-of-service plans; traditional indemnity plans and other hybrid plans, including consumer-driven health plans; and hospital only and limited benefit products. The company also provides a range of managed care services to self-funded customers, including claims processing, underwriting, stop loss insurance, actuarial services, provider network access, medical management, disease management, wellness programs, and other administrative services. In addition, it offers an array of specialty and other insurance products and services, such as pharmacy benefits management, dental, vision, life and disability insurance benefits, and analytics-driven personal health care. Further, the company provides services to the federal government in connection with the Federal Employee Program; and operates as a licensee of the Blue Cross and Blue Shield Association. As of December 31, 2021, it served 45 million medical members through its affiliated health plans. The company was formerly known as WellPoint, Inc. and changed its name to Anthem, Inc. in December 2014. Anthem, Inc. was founded in 1944 and is headquartered in Indianapolis, Indiana.',
        fullTimeEmployees=98200,
        city='Indianapolis',
        state='IN',
        trailingPE=21.710455,
        dividendYield=0.0105,
        averageVolume=1192212,
        regularMarketOpen=469.53,
        volume=1274535,
        fiftyTwoWeekHigh=533.68,
        fiftyTwoWeekLow=355.43,
        recommendationKey='buy',
        industry='Healthcare Plans'
    )
    db.session.add(ANTM)

    APA = Stock(
        name='APA Corporation',
        ticker='APA',
        marketCap=13113254912,
        dayHigh=39.85,
        dayLow=37.92,
        currentPrice=38.77,
        longBusinessSummary='APA Corporation, through its subsidiaries, explores for, develops, and produces oil and gas properties. It has operations in the United States, Egypt, and the United Kingdom, as well as has exploration activities offshore Suriname. The company also operates gathering, processing, and transmission assets in West Texas, as well as holds ownership in four Permian-to-Gulf Coast pipelines. APA Corporation was founded in 1954 and is based in Houston, Texas.',
        fullTimeEmployees=2253,
        city='Houston',
        state='TX',
        trailingPE=5.7633414,
        dividendYield=0.0127,
        averageVolume=9352267,
        regularMarketOpen=38.89,
        volume=9115567,
        fiftyTwoWeekHigh=51.95,
        fiftyTwoWeekLow=15.55,
        recommendationKey='buy',
        industry='Oil & Gas E&P'
    )
    db.session.add(APA)

    AAPL = Stock(
        name='Apple Inc.',
        ticker='AAPL',
        marketCap=2224493953024,
        dayHigh=143.422,
        dayLow=137.325,
        currentPrice=137.44,
        longBusinessSummary='Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide. It also sells various related services. In addition, the company offers iPhone, a line of smartphones; Mac, a line of personal computers; iPad, a line of multi-purpose tablets; AirPods Max, an over-ear wireless headphone; and wearables, home, and accessories comprising AirPods, Apple TV, Apple Watch, Beats products, HomePod, and iPod touch. Further, it provides AppleCare support services; cloud services store services; and operates various platforms, including the App Store that allow customers to discover and download applications and digital content, such as books, music, video, games, and podcasts. Additionally, the company offers various services, such as Apple Arcade, a game subscription service; Apple Music, which offers users a curated listening experience with on-demand radio stations; Apple News+, a subscription news and magazine service; Apple TV+, which offers exclusive original content; Apple Card, a co-branded credit card; and Apple Pay, a cashless payment service, as well as licenses its intellectual property. The company serves consumers, and small and mid-sized businesses; and the education, enterprise, and government markets. It distributes third-party applications for its products through the App Store. The company also sells its products through its retail and online stores, and direct sales force; and third-party cellular network carriers, wholesalers, retailers, and resellers. Apple Inc. was incorporated in 1977 and is headquartered in Cupertino, California.',
        fullTimeEmployees=154000,
        city='Cupertino',
        state='CA',
        trailingPE=22.395308,
        dividendYield=0.0069999998,
        averageVolume=95182072,
        regularMarketOpen=142.695,
        volume=66928031,
        fiftyTwoWeekHigh=182.94,
        fiftyTwoWeekLow=129.04,
        recommendationKey='buy',
        industry='Consumer Electronics'
    )
    db.session.add(AAPL)

    AMAT = Stock(
        name='Applied Materials, Inc.',
        ticker='AMAT',
        marketCap=82662359040,
        dayHigh=98.91,
        dayLow=94.74,
        currentPrice=95.02,
        longBusinessSummary='Applied Materials, Inc. provides manufacturing equipment, services, and software to the semiconductor, display, and related industries. It operates through three segments: Semiconductor Systems, Applied Global Services, and Display and Adjacent Markets. The Semiconductor Systems segment develops, manufactures, and sells various manufacturing equipment that is used to fabricate semiconductor chips or integrated circuits. This segment also offers various technologies, including epitaxy, ion implantation, oxidation/nitridation, rapid thermal processing, physical vapor deposition, chemical vapor deposition, chemical mechanical planarization, electrochemical deposition, atomic layer deposition, etching, and selective deposition and removal, as well as metrology and inspection tools. The Applied Global Services segment provides integrated solutions to optimize equipment and fab performance and productivity comprising spares, upgrades, services, remanufactured earlier generation equipment, and factory automation software for semiconductor, display, and other products. The Display and Adjacent Markets segment offers products for manufacturing liquid crystal displays; organic light-emitting diodes; and other display technologies for TVs, monitors, laptops, personal computers, electronic tablets, smart phones, and other consumer-oriented devices. The company operates in the United States, China, Korea, Taiwan, Japan, Southeast Asia, and Europe. Applied Materials, Inc. was incorporated in 1967 and is headquartered in Santa Clara, California.',
        fullTimeEmployees=30100,
        city='Santa Clara',
        state='CA',
        trailingPE=12.703208,
        dividendYield=0.0107,
        averageVolume=8346127,
        regularMarketOpen=98.11,
        volume=6420725,
        fiftyTwoWeekHigh=167.06,
        fiftyTwoWeekLow=87.62,
        recommendationKey='buy',
        industry='Semiconductor Equipment & Materials'
    )
    db.session.add(AMAT)

    ANET = Stock(
        name='Arista Networks, Inc.',
        ticker='ANET',
        marketCap=29273399296,
        dayHigh=100.05,
        dayLow=95.11,
        currentPrice=95.26,
        longBusinessSummary="Arista Networks, Inc. develops, markets, and sells cloud networking solutions in the Americas, Europe, the Middle East, Africa, and the Asia-Pacific. The company's cloud networking solutions consist of extensible operating systems, a set of network applications, as well as gigabit Ethernet switching and routing platforms. It also provides post contract customer support services, such as technical support, hardware repair and parts replacement beyond standard warranty, bug fix, patch, and upgrade services. The company serves a range of industries comprising internet companies, service providers, financial services organizations, government agencies, media and entertainment companies, and others. It markets and sells its products through distributors, system integrators, value-added resellers, and original equipment manufacturer partners, as well as through its direct sales force. The company was formerly known as Arastra, Inc. and changed its name to Arista Networks, Inc. in October 2008. Arista Networks, Inc. was incorporated in 2004 and is headquartered in Santa Clara, California.",
        fullTimeEmployees=2993,
        city='Santa Clara',
        state='CA',
        trailingPE=38.67641,
        dividendYield=None,
        averageVolume=1959312,
        regularMarketOpen=98.89,
        volume=1384052,
        fiftyTwoWeekHigh=148.57,
        fiftyTwoWeekLow=85.18,
        recommendationKey='buy',
        industry='Computer Hardware'
    )
    db.session.add(ANET)

    AJG = Stock(
        name='Arthur J. Gallagher & Co.',
        ticker='AJG',
        marketCap=33823623168,
        dayHigh=167.38,
        dayLow=162.55,
        currentPrice=163.18,
        longBusinessSummary="Arthur J. Gallagher & Co., together with its subsidiaries, provides insurance brokerage, consulting, third-party claims settlement, and administration services in the United States, Australia, Bermuda, Canada, the Caribbean, New Zealand, India, and the United Kingdom. It operates through Brokerage and Risk Management segments. The Brokerage segment consists of retail and wholesale insurance brokerage operations; assists retail brokers and other non-affiliated brokers in the placement of specialized and hard-to-place insurance; acts as a brokerage wholesaler, managing general agent, and managing general underwriter for distributing specialized insurance coverage's to underwriting enterprises. This segment also performs activities, including marketing, underwriting, issuing policies, collecting premiums, appointing and supervising other agents, paying claims, and negotiating reinsurance; and offers brokerage and consulting services to businesses and organizations, including commercial, not-for-profit, and public entities, as well as individuals in the areas of insurance placement, risk of loss management, and management of employer sponsored benefit programs. The Risk Management segment provides contract claim settlement and administration services to enterprises and public entities; and claims management, loss control consulting, and insurance property appraisal services. The company offers its services through a network of correspondent insurance brokers and consultants. It serves commercial, industrial, public, religious, and not-for-profit entities. The company was incorporated in 1927 and is headquartered in Rolling Meadows, Illinois.",
        fullTimeEmployees=39876,
        city='Rolling Meadows',
        state='IL',
        trailingPE=35.30506,
        dividendYield=0.0126,
        averageVolume=954311,
        regularMarketOpen=166.01,
        volume=859511,
        fiftyTwoWeekHigh=187.02,
        fiftyTwoWeekLow=135.5,
        recommendationKey='buy',
        industry='Insurance Brokers'
    )
    db.session.add(AJG)

    AIZ = Stock(
        name='Assurant, Inc.',
        ticker='AIZ',
        marketCap=9856968704,
        dayHigh=176.36,
        dayLow=172.97,
        currentPrice=173,
        longBusinessSummary='Assurant, Inc., together with its subsidiaries, provides lifestyle and housing solutions that support, protect, and connect consumer purchases in North America, Latin America, Europe, and the Asia Pacific. The company operates through two segments: Global Lifestyle and Global Housing. The Global Lifestyle segment offers mobile device solutions, and extended service products and related services for mobile devices, consumer electronics, and appliances; vehicle protection and related services; and credit protection and other insurance products. The Global Housing segment provides lender-placed homeowners insurance, manufactured housing, and flood insurance; and renters insurance and related products, as well as voluntary manufactured housing insurance, voluntary homeowners insurance, and other specialty products. The company was formerly known as Fortis, Inc. and changed its name to Assurant, Inc. in February 2004. Assurant, Inc. was founded in 1892 and is headquartered in New York, New York.',
        fullTimeEmployees=15600,
        city='New York',
        state='NY',
        trailingPE=7.642356,
        dividendYield=0.015,
        averageVolume=484898,
        regularMarketOpen=174.46,
        volume=360543,
        fiftyTwoWeekHigh=194.12,
        fiftyTwoWeekLow=144.18,
        recommendationKey='buy',
        industry='Insurance—Specialty'
    )
    db.session.add(AIZ)

    T = Stock(
        name='AT&T Inc.',
        ticker='T',
        marketCap=147176013824,
        dayHigh=21.06,
        dayLow=20.6,
        currentPrice=20.61,
        longBusinessSummary="AT&T Inc. provides telecommunications, media, and technology services worldwide. Its Communications segment offers wireless voice and data communications services; and sells handsets, wireless data cards, wireless computing devices, and carrying cases and hands-free devices through its own company-owned stores, agents, and third-party retail stores. It also provides data, voice, security, cloud solutions, outsourcing, and managed and professional services, as well as customer premises equipment for multinational corporations, small and mid-sized businesses, governmental, and wholesale customers. In addition, this segment offers broadband fiber and legacy telephony voice communication services to residential customers. It markets its communications services and products under the AT&T, Cricket, AT&T PREPAID, and AT&T Fiber brand names. The company's Latin America segment provides wireless services in Mexico; and video services in Latin America. This segment markets its services and products under the AT&T and Unefon brand names. The company was formerly known as SBC Communications Inc. and changed its name to AT&T Inc. in 2005. AT&T Inc. was incorporated in 1983 and is headquartered in Dallas, Texas.",
        fullTimeEmployees=203160,
        city='Dallas',
        state='TX',
        trailingPE=159.76746,
        dividendYield=0.0559,
        averageVolume=52514274,
        regularMarketOpen=20.93,
        volume=24769643,
        fiftyTwoWeekHigh=22.167673,
        fiftyTwoWeekLow=16.63142,
        recommendationKey='hold',
        industry='Telecom Services'
    )
    db.session.add(T)

    ATO = Stock(
        name='Atmos Energy Corporation',
        ticker='ATO',
        marketCap=14683808768,
        dayHigh=112.17,
        dayLow=110.465,
        currentPrice=110.65,
        longBusinessSummary='Atmos Energy Corporation, together with its subsidiaries, engages in the regulated natural gas distribution, and pipeline and storage businesses in the United States. It operates through two segments, Distribution, and Pipeline and Storage. The Distribution segment is involved in the regulated natural gas distribution and related sales operations in eight states. This segment distributes natural gas to approximately three million residential, commercial, public authority, and industrial customers. As of September 30, 2021, it owned 71,921 miles of underground distribution and transmission mains. The Pipeline and Storage segment engages in the pipeline and storage operations. This segment transports natural gas for third parties and manages five underground storage reservoirs in Texas; and provides ancillary services to the pipeline industry, including parking arrangements, lending, and inventory sales. As of September 30, 2021, it owned 5,699 miles of gas transmission lines. Atmos Energy Corporation was founded in 1906 and is headquartered in Dallas, Texas.',
        fullTimeEmployees=4684,
        city='Dallas',
        state='TX',
        trailingPE=21.611328,
        dividendYield=0.0241,
        averageVolume=982561,
        regularMarketOpen=111.05,
        volume=500187,
        fiftyTwoWeekHigh=122.96,
        fiftyTwoWeekLow=85.8,
        recommendationKey='buy',
        industry='Utilities—Regulated Gas'
    )
    db.session.add(ATO)

    ADSK = Stock(
        name='Autodesk, Inc.',
        ticker='ADSK',
        marketCap=38893424640,
        dayHigh=186.19,
        dayLow=176.31,
        currentPrice=176.81,
        longBusinessSummary='Autodesk, Inc. provides 3D design, engineering, and entertainment software and services worldwide. The company offers AutoCAD Civil 3D, a surveying, design, analysis, and documentation solution for civil engineering, including land development, transportation, and environmental projects; BIM 360, a construction management cloud-based software; AutoCAD, a software for professional design, drafting, detailing, and visualization; AutoCAD LT, a drafting and detailing software; computer-aided manufacturing (CAM) software for computer numeric control machining, inspection, and modelling for manufacturing; Fusion 360, a 3D CAD, CAM, and computer-aided engineering tool; and Industry Collections tools for professionals in architecture, engineering and construction, product design and manufacturing, and media and entertainment collection industries. It also provides Inventor tools for 3D mechanical design, simulation, analysis, tooling, visualization, and documentation; Vault, a data management software to manage data in one central location, accelerate design processes, and streamline internal/external collaboration; Maya and 3ds Max software products that offer 3D modeling, animation, effects, rendering, and compositing solutions; and ShotGrid, a cloud-based software for review and production tracking in the media and entertainment industry. It sells its products and services to customers directly, as well as through a network of resellers and distributors. Autodesk, Inc. was incorporated in 1982 and is headquartered in San Rafael, California.',
        fullTimeEmployees=12600,
        city='San Rafael',
        state='CA',
        trailingPE=29.826248,
        dividendYield=None,
        averageVolume=1858411,
        regularMarketOpen=186.62,
        volume=1533928,
        fiftyTwoWeekHigh=344.39,
        fiftyTwoWeekLow=163.2,
        recommendationKey='buy',
        industry='Software—Application'
    )
    db.session.add(ADSK)

    AZO = Stock(
        name='AutoZone, Inc.',
        ticker='AZO',
        marketCap=43854909440,
        dayHigh=2195.5723,
        dayLow=2116.51,
        currentPrice=2125.33,
        longBusinessSummary='AutoZone, Inc. retails and distributes automotive replacement parts and accessories. The company offers various products for cars, sport utility vehicles, vans, and light trucks, including new and remanufactured automotive hard parts, maintenance items, accessories, and non-automotive products. Its products include A/C compressors, batteries and accessories, bearings, belts and hoses, calipers, chassis, clutches, CV axles, engines, fuel pumps, fuses, ignition and lighting products, mufflers, radiators, starters and alternators, thermostats, and water pumps, as well as tire repairs. In addition, the company offers maintenance products, such as antifreeze and windshield washer fluids; brake drums, rotors, shoes, and pads; brake and power steering fluids, and oil and fuel additives; oil and transmission fluids; oil, cabin, air, fuel, and transmission filters; oxygen sensors; paints and accessories; refrigerants and accessories; shock absorbers and struts; spark plugs and wires; and windshield wipers. Further, it provides air fresheners, cell phone accessories, drinks and snacks, floor mats and seat covers, interior and exterior accessories, mirrors, performance products, protectants and cleaners, sealants and adhesives, steering wheel covers, stereos and radios, tools, and wash and wax products, as well as towing services. Additionally, the company provides a sales program that offers commercial credit and delivery of parts and other products; sells automotive diagnostic and repair software under the ALLDATA brand through alldata.com and alldatadiy.com; and automotive hard parts, maintenance items, accessories, and non-automotive products through autozone.com. As of November 20, 2021, it operated 6,066 stores in the United States; 666 stores in Mexico; and 53 stores in Brazil. The company was founded in 1979 and is based in Memphis, Tennessee.',
        fullTimeEmployees=65100,
        city='Memphis',
        state='TN',
        trailingPE=20.72098,
        dividendYield=None,
        averageVolume=196875,
        regularMarketOpen=2168,
        volume=194174,
        fiftyTwoWeekHigh=2267.4,
        fiftyTwoWeekLow=1486.97,
        recommendationKey='buy',
        industry='Specialty Retail'
    )
    db.session.add(AZO)

    AVB = Stock(
        name='AvalonBay Communities, Inc.',
        ticker='AVB',
        marketCap=27537358848,
        dayHigh=202.12,
        dayLow=196.6,
        currentPrice=197.06,
        longBusinessSummary="As of December 31, 2020, the Company owned or held a direct or indirect ownership interest in 291 apartment communities containing 86,025 apartment homes in 11 states and the District of Columbia, of which 18 communities were under development and one community was under redevelopment. The Company is an equity REIT in the business of developing, redeveloping, acquiring and managing apartment communities in leading metropolitan areas in New England, the New York/New Jersey Metro area, the Mid-Atlantic, the Pacific Northwest, and Northern and Southern California, as well as in the Company's expansion markets consisting of Southeast Florida and Denver, Colorado (the 'Expansion Markets').",
        fullTimeEmployees=2839,
        city='Arlington',
        state='VA',
        trailingPE=27.237041,
        dividendYield=0.0307,
        averageVolume=868385,
        regularMarketOpen=199.09,
        volume=456073,
        fiftyTwoWeekHigh=259.05,
        fiftyTwoWeekLow=183.35,
        recommendationKey='hold',
        industry='REIT—Residential'
    )
    db.session.add(AVB)

    AVY = Stock(
        name='Avery Dennison Corporation',
        ticker='AVY',
        marketCap=13588413440,
        dayHigh=169.24,
        dayLow=163.915,
        currentPrice=164.12,
        longBusinessSummary="Avery Dennison Corporation manufactures and markets pressure-sensitive materials and products in the United States, Europe, Asia, Latin America, and internationally. The company's Label and Graphic Materials segment offers pressure-sensitive label and packaging materials; and graphics and reflective products under the Fasson, JAC, Avery Dennison, and Mactac brands, as well as durable cast and reflective films. It provides its products to the home and personal care, beer and beverage, durables, pharmaceutical, wine and spirits, and food market segments; architectural, commercial sign, digital printing, and other related market segments; construction, automotive, and fleet transportation market segments, as well as traffic and safety applications; and sign shops, commercial printers, and designers. The company's Retail Branding and Information Solutions segment designs, manufactures, and sells brand embellishments, graphic tickets, tags and labels, and sustainable packaging solutions, as well as offers creative services; radio-frequency identification products; visibility and loss prevention solutions; price ticketing and marking solutions; care, content, and country of origin compliance solutions; and brand protection and security solutions. It serves retailers, brand owners, apparel manufacturers, distributors, and industrial customers. The company's Industrial and Healthcare Materials segment offers tapes; pressure-sensitive adhesive based materials and converted products; medical fasteners; and performance polymers under the Fasson, Avery Dennison, and Yongle brands. It serves automotive, electronics, building and construction, general industrial, personal care, and medical markets. The company was formerly known as Avery International Corporation and changed its name to Avery Dennison Corporation in 1990. Avery Dennison Corporation was founded in 1935 and is headquartered in Glendale, California.",
        fullTimeEmployees=36000,
        city='Glendale',
        state='CA',
        trailingPE=18.425957,
        dividendYield=0.0172,
        averageVolume=630711,
        regularMarketOpen=167.65,
        volume=405491,
        fiftyTwoWeekHigh=229.24,
        fiftyTwoWeekLow=151.62,
        recommendationKey='buy',
        industry='Business Equipment & Supplies'
    )
    db.session.add(AVY)

    BKR = Stock(
        name='Baker Hughes Company',
        ticker='BKR',
        marketCap=26159937536,
        dayHigh=30.455,
        dayLow=29.575,
        currentPrice=30.07,
        longBusinessSummary='Baker Hughes Company provides a portfolio of technologies and services to energy and industrial value chain worldwide. It operates through four segments: Oilfield Services (OFS), Oilfield Equipment (OFE), Turbomachinery & Process Solutions (TPS), and Digital Solutions (DS). The OFS segment offers exploration, drilling, wireline, evaluation, completion, production, and intervention services; and drilling and completions fluids, wireline services, downhole completion tools and systems, wellbore intervention tools and services, pressure pumping systems, oilfield and industrial chemicals, and artificial lift technologies for oil and natural gas, and oilfield service companies. The OFE segment provides subsea and surface wellheads, pressure control and production systems and services, flexible pipe systems for offshore and onshore applications, and life-of-field solutions, including well intervention and decommissioning solutions; and services related to onshore and offshore drilling and production operations. The TPS segment provides equipment and related services for mechanical-drive, compression, and power-generation applications across the oil and gas industry. Its product portfolio includes drivers, compressors, and turnkey solutions; and pumps, valves, and compressed natural gas and small-scale liquefied natural gas solutions. This segment serves upstream, midstream, downstream, onshore, offshore, and industrial customers. The DS segment provides sensor-based process measurements, machine health and condition monitoring, asset strategy and management, control systems, as well as non-destructive testing and inspection, and pipeline integrity solutions. The company was formerly known as Baker Hughes, a GE company and changed its name to Baker Hughes Company in October 2019. Baker Hughes Company is based in Houston, Texas.',
        fullTimeEmployees=55000,
        city='Houston',
        state='TX',
        trailingPE=167.05554,
        dividendYield=0.0226,
        averageVolume=10886966,
        regularMarketOpen=30,
        volume=6434795,
        fiftyTwoWeekHigh=39.78,
        fiftyTwoWeekLow=19.23,
        recommendationKey='buy',
        industry='Oil & Gas Equipment & Services'
    )
    db.session.add(BKR)

    BAC = Stock(
        name='Bank of America Corporation',
        ticker='BAC',
        marketCap=264018395136,
        dayHigh=33.495,
        dayLow=32.185,
        currentPrice=32.26,
        longBusinessSummary="Bank of America Corporation, through its subsidiaries, provides banking and financial products and services for individual consumers, small and middle-market businesses, institutional investors, large corporations, and governments worldwide. Its Consumer Banking segment offers traditional and money market savings accounts, certificates of deposit and IRAs, noninterest-and interest-bearing checking accounts, and investment accounts and products; and credit and debit cards, residential mortgages, and home equity loans, as well as direct and indirect loans, such as automotive, recreational vehicle, and consumer personal loans. The company's Global Wealth & Investment Management segment offers investment management, brokerage, banking, and trust and retirement products and services; and wealth management solutions, as well as customized solutions, including specialty asset management services. Its Global Banking segment provides lending products and services, including commercial loans, leases, commitment facilities, trade finance, and commercial real estate and asset-based lending; treasury solutions, such as treasury management, foreign exchange, and short-term investing options and merchant services; working capital management solutions; and debt and equity underwriting and distribution, and merger-related and other advisory services. The company's Global Markets segment offers market-making, financing, securities clearing, settlement, and custody services, as well as risk management products using interest rate, equity, credit, currency and commodity derivatives, foreign exchange, fixed-income, and mortgage-related products. As of December 31, 2021, it served approximately 67 million consumer and small business clients with approximately 4,200 retail financial centers; approximately 16,000 ATMs; and digital banking platforms with approximately 41 million active users. The company was founded in 1784 and is based in Charlotte, North Carolina.",
        fullTimeEmployees=208000,
        city='Charlotte',
        state='NC',
        trailingPE=9.658683,
        dividendYield=0.0239,
        averageVolume=50893327,
        regularMarketOpen=32.83,
        volume=49700463,
        fiftyTwoWeekHigh=50.11,
        fiftyTwoWeekLow=30.86,
        recommendationKey='buy',
        industry='Banks—Diversified'
    )
    db.session.add(BAC)

    BBWI = Stock(
        name='Bath & Body Works, Inc.',
        ticker='BBWI',
        marketCap=7473967104,
        dayHigh=31.49,
        dayLow=28.915,
        currentPrice=29,
        longBusinessSummary='Bath & Body Works, Inc. operates a specialty retailer of home fragrance, body care, and soaps and sanitizer products. The company sells its products under the Bath & Body Works, White Barn, and other brand names through specialty retail stores and websites located in the United States and Canada, as well as through international stores operated by partners under franchise, license, and wholesale arrangements. As of January 29, 2022, it operated 1,755 company-operated retail stores and 338 international partner-operated stores. The company was formerly known as L Brands, Inc. and changed its name to Bath & Body Works, Inc. in August 2021. Bath & Body Works, Inc. was founded in 1963 and is headquartered in Columbus, Ohio.',
        fullTimeEmployees=8800,
        city='Columbus',
        state='OH',
        trailingPE=5.0513844,
        dividendYield=0.015700001,
        averageVolume=5610567,
        regularMarketOpen=31.01,
        volume=4033347,
        fiftyTwoWeekHigh=82,
        fiftyTwoWeekLow=28.89,
        recommendationKey='none',
        industry='Specialty Retail'
    )
    db.session.add(BBWI)

    BAX = Stock(
        name='Baxter International Inc.',
        ticker='BAX',
        marketCap=32670218240,
        dayHigh=67.1,
        dayLow=65.18,
        currentPrice=65.25,
        longBusinessSummary="Baxter International Inc., through its subsidiaries, develops and provides a portfolio of healthcare products worldwide. The company offers peritoneal dialysis and hemodialysis, and additional dialysis therapies and services; intravenous therapies, infusion pumps, administration sets, and drug reconstitution devices; remixed and oncology drug platforms, inhaled anesthesia and critical care products and pharmacy compounding services; parenteral nutrition therapies and related products; biological products and medical devices used in surgical procedures for hemostasis, tissue sealing and adhesion prevention; and continuous renal replacement therapies and other organ support therapies focused in the intensive care unit. It also provides connected care solutions, including devices, software, communications, and integration technologies; integrated patient monitoring and diagnostic technologies to help diagnose, treat, and manage a various illness and diseases, including respiratory therapy, cardiology, vision screening, and physical assessment; surgical video technologies, tables, lights, pendants, precision positioning devices and other accessories. In addition, the company offers contracted services to various pharmaceutical and biopharmaceutical companies. Its products are used in hospitals, kidney dialysis centers, nursing homes, rehabilitation centers, doctors' offices, and patients at home under physician supervision. The company sells its products through direct sales force, as well as through independent distributors, drug wholesalers, and specialty pharmacy or other alternate site providers in approximately 100 countries. It has an agreement with Celerity Pharmaceutical, LLC to develop acute care generic injectable premix and oncolytic molecules. Baxter International Inc. was incorporated in 1931 and is headquartered in Deerfield, Illinois.",
        fullTimeEmployees=60000,
        city='Deerfield',
        state='IL',
        trailingPE=27.462122,
        dividendYield=0.0159,
        averageVolume=3301433,
        regularMarketOpen=67,
        volume=2548930,
        fiftyTwoWeekHigh=89.7,
        fiftyTwoWeekLow=63.25,
        recommendationKey='buy',
        industry='Medical Instruments & Supplies'
    )
    db.session.add(BAX)

    BDX = Stock(
        name='Becton, Dickinson and Company',
        ticker='BDX',
        marketCap=69701566464,
        dayHigh=251.46,
        dayLow=244.39,
        currentPrice=244.53,
        longBusinessSummary="Becton, Dickinson and Company develops, manufactures, and sells medical supplies, devices, laboratory equipment, and diagnostic products for healthcare institutions, physicians, life science researchers, clinical laboratories, pharmaceutical industry, and the general public worldwide. The company's BD Medical segment offers peripheral intravenous (IV) and advanced peripheral catheters, central lines, acute dialysis catheters, vascular care and preparation products, needle-free IV connectors and extensions sets, closed-system drug transfer devices, hazardous drug detections, hypodermic syringes and needles, anesthesia needles and trays, enteral syringes, and sharps disposal systems; IV medication and infusion therapy delivery systems, medication compounding workflow systems, automated medication dispensing and supply management systems, and medication inventory optimization and tracking systems; syringes, pen needles, and other products for diabetes; and prefillable drug delivery systems. Its BD Life Sciences segment provides specimen and blood collection products; automated blood and tuberculosis culturing, molecular testing, microorganism identification and drug susceptibility, and liquid-based cytology systems, as well as rapid diagnostic assays, microbiology laboratory automation products, and plated media products; and fluorescence-activated cell sorters and analyzers, antibodies and kits, reagent systems, and solutions for single-cell gene expression analysis, as well as clinical oncology, immunological, and transplantation diagnostic/monitoring reagents and analyzers. The company's BD Interventional segment offers hernia and soft tissue repair, biological and bioresorbable grafts, biosurgery, and other surgical products; surgical infection prevention, surgical and laparoscopic instrumentation products; peripheral intervention products; and urology and critical care products. The company was founded in 1897 and is based in Franklin Lakes, New Jersey.",
        fullTimeEmployees=75000,
        city='Franklin Lakes',
        state='NJ',
        trailingPE=35.69781,
        dividendYield=0.0139999995,
        averageVolume=1164320,
        regularMarketOpen=250.53,
        volume=850684,
        fiftyTwoWeekHigh=277.29,
        fiftyTwoWeekLow=229.39513,
        recommendationKey='buy',
        industry='Medical Instruments & Supplies'
    )
    db.session.add(BDX)

    WRB = Stock(
        name='W. R. Berkley Corporation',
        ticker='WRB',
        marketCap=12204056576,
        dayHigh=70.42,
        dayLow=68.79,
        currentPrice=69.09,
        longBusinessSummary="W. R. Berkley Corporation, an insurance holding company, operates as a commercial lines writer in the United States and internationally. It operates in two segments, Insurance and Reinsurance & Monoline Excess. The Insurance segment underwrites commercial insurance business, including premises operations, commercial automobile, property, products liability, and general and professional liability lines. It also provides workers' compensation insurance products; accident and health insurance and reinsurance products; insurance for commercial risks; specialty environmental products for contractors, consultants, and property owners and facilities operators; specialized insurance coverages for fine arts and jewelry exposures; umbrella and excess liability coverage products; and liquor liability and inland marine coverage for small to medium-sized insureds. In addition, this segment offers directors and officers, and surety risk products, as well as products for technology, and life sciences and travel industries; cyber risk solutions; casualty, group life, and crime and fidelity related insurance products; personal lines insurance solutions, including home, condo/co-op, auto, and collectibles; automobile, law enforcement, public officials and educator's legal, and employment practices liability, as well as incidental medical insurance products; and at-risk and alternative risk insurance program management services. The Reinsurance & Monoline Excess segment provides other insurance companies and self-insureds with assistance in managing their net risk through reinsurance on a portfolio basis through treaty reinsurance or on an individual basis through facultative reinsurance. W. R. Berkley Corporation was founded in 1967 and is based in Greenwich, Connecticut.",
        fullTimeEmployees=7681,
        city='Greenwich',
        state='CT',
        trailingPE=12.415093,
        dividendYield=0.0050999997,
        averageVolume=1643666,
        regularMarketOpen=69.71,
        volume=1167569,
        fiftyTwoWeekHigh=72.32,
        fiftyTwoWeekLow=47.13333,
        recommendationKey='buy',
        industry='Insurance—Property & Casualty'
    )
    db.session.add(WRB)

    BBY = Stock(
        name='Best Buy Co., Inc.',
        ticker='BBY',
        marketCap=16562623488,
        dayHigh=71.98,
        dayLow=68.67,
        currentPrice=68.85,
        longBusinessSummary="Best Buy Co., Inc. retails technology products in the United States and Canada. The company operates in two segments, Domestic and International. Its stores provide computing products, such as desktops, notebooks, and peripherals; mobile phones comprising related mobile network carrier commissions; networking products; tablets covering e-readers; smartwatches; and consumer electronics consisting of digital imaging, health and fitness, home theater, portable audio comprising headphones and portable speakers, and smart home products. The company's stores also offer appliances, such as dishwashers, laundry, ovens, refrigerators, blenders, coffee makers, and vacuums; entertainment products consisting of drones, peripherals, movies, music, and toys, as well as gaming hardware and software, and virtual reality and other software products; and other products, such as baby, food and beverage, luggage, outdoor living, and sporting goods. In addition, it provides consultation, delivery, design, health-related, installation, memberships, repair, set-up, technical support, and warranty-related services. The company offers its products through stores and websites under the Best Buy, Best Buy Ads, Best Buy Business, Best Buy Health, CST, Current Health, Geek Squad, Lively, Magnolia, Best Buy Mobile, Pacific Kitchen, Home, and Yardbird, as well as domain names bestbuy.com, currenthealth.com, lively.com, yardbird.com, and bestbuy.ca. As of January 30, 2022, it had 1,144 stores. The company was formerly known as Sound of Music, Inc. The company was incorporated in 1966 and is headquartered in Richfield, Minnesota.",
        fullTimeEmployees=57750,
        city='Richfield',
        state='MN',
        trailingPE=6.656676,
        dividendYield=0.040799998,
        averageVolume=3499556,
        regularMarketOpen=71.72,
        volume=2546837,
        fiftyTwoWeekHigh=141.97,
        fiftyTwoWeekLow=67.66,
        recommendationKey='hold',
        industry='Specialty Retail'
    )
    db.session.add(BBY)

    BIO = Stock(
        name='Bio-Rad Laboratories, Inc.',
        ticker='BIO',
        marketCap=14808255488,
        dayHigh=513.4548,
        dayLow=495.05,
        currentPrice=495.16,
        longBusinessSummary="Bio-Rad Laboratories, Inc. manufactures, and distributes life science research and clinical diagnostic products in the United States, Europe, Asia, Canada, and Latin America. The company operates through Life Science and Clinical Diagnostics segments. The Life Science segment develops, manufactures, and markets a range of reagents, apparatus, and laboratory instruments that are used in research techniques, biopharmaceutical production processes, and food testing regimes. It focuses on selected segments of the life sciences market in proteomics, genomics, biopharmaceutical production, cellular biology, and food safety. This segment serves universities and medical schools, industrial research organizations, government agencies, pharmaceutical manufacturers, biotechnology researchers, food producers, and food testing laboratories. The Clinical Diagnostics segment designs, manufactures, sells, and supports test systems, informatics systems, test kits, and specialized quality controls for clinical laboratories in the diagnostics market. This segment offers reagents, instruments, and software, which address specific niches within the in vitro diagnostics test market. It sells its products to reference laboratories, hospital laboratories, state newborn screening facilities, physicians' office laboratories, and transfusion laboratories. In addition, the company offers products and systems to separate complex chemical and biological materials, as well as to identify, analyze, and purify components. The company offers its products through its direct sales force, as well as through distributors, agents, brokers, and resellers. Bio-Rad Laboratories, Inc. was founded in 1952 and is headquartered in Hercules, California.",
        fullTimeEmployees=7900,
        city='Hercules',
        state='CA',
        trailingPE=2.245868,
        dividendYield=None,
        averageVolume=220766,
        regularMarketOpen=506.06,
        volume=164805,
        fiftyTwoWeekHigh=832.7,
        fiftyTwoWeekLow=462.61,
        recommendationKey='strong_buy',
        industry='Medical Devices'
    )
    db.session.add(BIO)

    TECH = Stock(
        name='Bio-Techne Corporation',
        ticker='TECH',
        marketCap=13596567552,
        dayHigh=356.29,
        dayLow=345.765,
        currentPrice=346.01,
        longBusinessSummary='Bio-Techne Corporation, together with its subsidiaries, develops, manufactures, and sells life science reagents, instruments, and services for the research, and diagnostics and bioprocessing markets worldwide. The company operates through two segments, Protein Sciences, and Diagnostics and Genomics. The Protein Sciences segment provides biological reagents used in various aspects of life science research, diagnostics, and cell and gene therapy, such as cytokines and growth factors, antibodies, small molecules, tissue culture sera, and cell selection technologies. This segment also offers proteomic analytical tools for automated western blot and multiplexed ELISA workflow consists of manual and automated protein analysis instruments and immunoassays for use in quantifying proteins in various biological fluids. The Diagnostics and Genomics segment provides diagnostic products, including controls, calibrators, and diagnostic assays for regulated diagnostics market, exosome-based molecular diagnostic assays, advanced tissue-based in-situ hybridization assays for spatial genomic and tissue biopsy analysis, and genetic and oncology kits for research and clinical applications; and nucleic acid analysis products for use in diagnostic or research applications, as well as instruments and process control products for hematology, blood chemistry, blood gases, and coagulation controls and reagents used in various diagnostic applications. It offers its products under R&D Systems, Novus Biologicals, Tocris Biosciences, ProteinSimple, Advanced Cell Diagnostics, and ExosomeDx brands. Bio-Techne Corporation has a clinical research collaboration with Carterra Inc. for the study of COVID-19 variants. The company was formerly known as Techne Corporation and changed its name to Bio-Techne Corporation in November 2014. Bio-Techne Corporation was founded in 1976 and is headquartered in Minneapolis, Minnesota.',
        fullTimeEmployees=2700,
        city='Minneapolis',
        state='MN',
        trailingPE=79.78096,
        dividendYield=0.0034999999,
        averageVolume=260282,
        regularMarketOpen=353.07,
        volume=172476,
        fiftyTwoWeekHigh=543.85,
        fiftyTwoWeekLow=318.07,
        recommendationKey='buy',
        industry='Biotechnology'
    )
    db.session.add(TECH)

    BIIB = Stock(
        name='Biogen Inc.',
        ticker='BIIB',
        marketCap=29747298304,
        dayHigh=213.88,
        dayLow=202.33,
        currentPrice=202.51,
        longBusinessSummary="Biogen Inc. discovers, develops, manufactures, and delivers therapies for treating neurological and neurodegenerative diseases. The company offers TECFIDERA, VUMERITY, AVONEX, PLEGRIDY, TYSABRI, and FAMPYRA for multiple sclerosis (MS); SPINRAZA for spinal muscular atrophy; and FUMADERM to treat plaque psoriasis. It also provides BENEPALI, an etanercept biosimilar referencing ENBREL; ADUHELM for the treatment of Alzheimer's disease; IMRALDI, an adalimumab biosimilar referencing HUMIRA; and FLIXABI, an infliximab biosimilar referencing REMICADE. In addition, the company offers RITUXAN for treating non-Hodgkin's lymphoma, chronic lymphocytic leukemia (CLL), rheumatoid arthritis, two forms of ANCA-associated vasculitis, and pemphigus vulgaris; RITUXAN HYCELA for non-Hodgkin's lymphoma and CLL; GAZYVA to treat CLL and follicular lymphoma; and OCREVUS for treating relapsing MS and primary progressive MS; and other anti-CD20 therapies. Further, it develops BIIB135, BIIB061, BIIB091, and BIIB107 for MS and neuroimmunology; Aducanumab, Lecanemab, BIIB076, and BIIB080 to treat Alzheimer's disease and dementia; BIIB067, BIIB078, BIIB105, BIIB100, and BIIB110 to treat neuromuscular disorders; BIIB124, BIIB094, BIIB118, BIIB101, and BIIB122 for treating Parkinson's disease and movement disorders; BIIB125 and BIIB104 for treating neuropsychiatry; Dapirolizumab pegol and BIIB059 to treat immunology related diseases; BIIB093 and BIIB131 to treat acute neurology; BIIB074 for neuropathic pain; and BYOOVIZ, BIIB800, and SB15 biosimilars, which are under various stages of development. The company has collaboration and license agreements with Acorda Therapeutics, Inc.; Alkermes Pharma Ireland Limited; Denali Therapeutics Inc.; Eisai Co., Ltd.; Genentech, Inc.; Neurimmune SubOne AG; Ionis Pharmaceuticals, Inc.; Samsung Bioepis Co., Ltd.; Sangamo Therapeutics, Inc.; and Sage Therapeutics, Inc. Biogen Inc. was founded in 1978 and is headquartered in Cambridge, Massachusetts.",
        fullTimeEmployees=9610,
        city='Cambridge',
        state='MA',
        trailingPE=19.820887,
        dividendYield=None,
        averageVolume=1108848,
        regularMarketOpen=213.75,
        volume=1259182,
        fiftyTwoWeekHigh=372.12,
        fiftyTwoWeekLow=187.16,
        recommendationKey='buy',
        industry='Drug Manufacturers—General'
    )
    db.session.add(BIIB)

    BLK = Stock(
        name='BlackRock, Inc.',
        ticker='BLK',
        marketCap=95574016000,
        dayHigh=648,
        dayLow=626.495,
        currentPrice=629.12,
        longBusinessSummary='BlackRock, Inc. is a publicly owned investment manager. The firm primarily provides its services to institutional, intermediary, and individual investors including corporate, public, union, and industry pension plans, insurance companies, third-party mutual funds, endowments, public institutions, governments, foundations, charities, sovereign wealth funds, corporations, official institutions, and banks. It also provides global risk management and advisory services. The firm manages separate client-focused equity, fixed income, and balanced portfolios. It also launches and manages open-end and closed-end mutual funds, offshore funds, unit trusts, and alternative investment vehicles including structured funds. The firm launches equity, fixed income, balanced, and real estate mutual funds. It also launches equity, fixed income, balanced, currency, commodity, and multi-asset exchange traded funds. The firm also launches and manages hedge funds. It invests in the public equity, fixed income, real estate, currency, commodity, and alternative markets across the globe. The firm primarily invests in growth and value stocks of small-cap, mid-cap, SMID-cap, large-cap, and multi-cap companies. It also invests in dividend-paying equity securities. The firm invests in investment grade municipal securities, government securities including securities issued or guaranteed by a government or a government agency or instrumentality, corporate bonds, and asset-backed and mortgage-backed securities. It employs fundamental and quantitative analysis with a focus on bottom-up and top-down approach to make its investments. The firm employs liquidity, asset allocation, balanced, real estate, and alternative strategies to make its investments. In real estate sector, it seeks to invest in Poland and Germany. The firm benchmarks the performance of its portfolios against various S&P, Russell, Barclays, MSCI, Citigroup, and Merrill Lynch indices. BlackRock, Inc. was founded in 1988 and is based in New York City with additional offices in Boston, Massachusetts; London, United Kingdom; Gurgaon, India; Hong Kong; Greenwich, Connecticut; Princeton, New Jersey; Edinburgh, United Kingdom; Sydney, Australia; Taipei, Taiwan; Singapore; Sao Paulo, Brazil; Philadelphia, Pennsylvania; Washington, District of Columbia; Toronto, Canada; Wilmington, Delaware; and San Francisco, California.',
        fullTimeEmployees=18400,
        city='New York',
        state='NY',
        trailingPE=16.728802,
        dividendYield=0.0317,
        averageVolume=1011945,
        regularMarketOpen=642.4,
        volume=517806,
        fiftyTwoWeekHigh=973.16,
        fiftyTwoWeekLow=575.6,
        recommendationKey='buy',
        industry='Asset Management'
    )
    db.session.add(BLK)

    BK = Stock(
        name='The Bank of New York Mellon Corporation',
        ticker='BK',
        marketCap=35394686976,
        dayHigh=44.05,
        dayLow=42.75,
        currentPrice=42.86,
        longBusinessSummary='The Bank of New York Mellon Corporation provides a range of financial products and services in the United States and internationally. The company operates through Securities Services, Market and Wealth Services, Investment and Wealth Management, and Other segments. The Securities Services segment offers custody, trust and depositary, accounting, exchange-traded funds, middle-office solutions, transfer agency, services for private equity and real estate funds, foreign exchange, securities lending, liquidity/lending services, prime brokerage, and data analytics. This segment also provides trustee, paying agency, fiduciary, escrow and other financial, issuer, and support services for brokers and investors. The Market and Wealth Services segment offers clearing and custody, investment, wealth and retirement solutions, technology and enterprise data management, trading, and prime brokerage services; and clearance and collateral management services. This segment also provides integrated cash management solutions, including payments, foreign exchange, liquidity management, receivables processing and payables management, and trade finance and processing services. The Investment and Wealth Management segment offers investment management strategies and distribution of investment products, investment management, custody, wealth and estate planning, private banking, investment, and information management services. The Other segment engages in the provision of leasing, corporate treasury, derivative and other trading, corporate and bank-owned life insurance, renewable energy investment, and business exit services. It serves central banks and sovereigns, financial institutions, asset managers, insurance companies, corporations, local authorities and high net-worth individuals, and family offices. The company was founded in 1784 and is headquartered in New York, New York.',
        fullTimeEmployees=49600,
        city='New York',
        state='NY',
        trailingPE=10.919745,
        dividendYield=0.0313,
        averageVolume=5107483,
        regularMarketOpen=43.54,
        volume=2921812,
        fiftyTwoWeekHigh=64.63,
        fiftyTwoWeekLow=40.26,
        recommendationKey='buy',
        industry='Asset Management'
    )
    db.session.add(BK)

    BKNG = Stock(
        name='Booking Holdings Inc.',
        ticker='BKNG',
        marketCap=75485159424,
        dayHigh=1953.8073,
        dayLow=1835.33,
        currentPrice=1838.42,
        longBusinessSummary='Booking Holdings Inc. provides travel and restaurant online reservation and related services worldwide. The company operates Booking.com, which offers online accommodation reservations; Rentalcars.com that provides online rental car reservation services; Priceline, which offer online travel reservation services, and consumers hotel, flight, and rental car reservation services, as well as vacation packages, cruises, and hotel distribution services. It also operates Agoda that provides online accommodation reservation services, as well as flight, ground transportation and activities reservation services. In addition, the company operates KAYAK, an online price comparison service that allows consumers to search and compare travel itineraries and prices, comprising airline ticket, accommodation reservation, and rental car reservation information; and OpenTable for booking online restaurant reservations. Further, it offers travel-related insurance products, and restaurant management services to consumers, travel service providers, and restaurants. The company was formerly known as The Priceline Group Inc. and changed its name to Booking Holdings Inc. in February 2018. The company was founded in 1997 and is headquartered in Norwalk, Connecticut.',
        fullTimeEmployees=20097,
        city='Norwalk',
        state='CT',
        trailingPE=198.74811,
        dividendYield=None,
        averageVolume=424101,
        regularMarketOpen=1921.76,
        volume=395635,
        fiftyTwoWeekHigh=2715.66,
        fiftyTwoWeekLow=1795.01,
        recommendationKey='buy',
        industry='Travel Services'
    )
    db.session.add(BKNG)

    BWA = Stock(
        name='BorgWarner Inc.',
        ticker='BWA',
        marketCap=8643744768,
        dayHigh=36.65,
        dayLow=35.77,
        currentPrice=36.05,
        longBusinessSummary='BorgWarner Inc. provides solutions for combustion, hybrid, and electric vehicles worldwide. The company operates through four segments: Air Management, E-Propulsion & Drivetrain, Fuel Injection, and Aftermarket. The Air Management segment offers turbochargers, eBoosters, eTurbos, timing systems, emissions systems, thermal systems, gasoline ignition technology, smart remote actuators, powertrain sensors, canisters, cabin heaters, battery modules and systems, battery packs, battery heaters, and battery charging. The E-Propulsion & Drivetrain segment provides rotating electrical components, power electronics, control modules, software, friction, and mechanical products for automatic transmissions and torque-management products. The Fuel Injection segment develops and manufactures gasoline and diesel fuel injection components and systems. The Aftermarket segment sells products and services to independent aftermarket customers and original equipment service customers. This segment provides a range of solutions, including fuel injection, electronics and engine management, maintenance, and test equipment and vehicle diagnostics. The company sells its products to original equipment manufacturers of light vehicles, which comprise passenger cars, sport-utility vehicles, vans, and light trucks; commercial vehicles, including medium-duty and heavy-duty trucks, and buses; and off-highway vehicles, such as agricultural and construction machinery, and marine applications, as well as to tier one vehicle systems suppliers and the aftermarket for light, commercial, and off-highway vehicles. The company was formerly known as Borg-Warner Automotive, Inc. BorgWarner Inc. was incorporated in 1987 and is headquartered in Auburn Hills, Michigan.',
        fullTimeEmployees=49300,
        city='Auburn Hills',
        state='MI',
        trailingPE=11.237531,
        dividendYield=0.0177,
        averageVolume=2088732,
        regularMarketOpen=36.09,
        volume=2534353,
        fiftyTwoWeekHigh=50.09,
        fiftyTwoWeekLow=32.58,
        recommendationKey='buy',
        industry='Auto Parts'
    )
    db.session.add(BWA)

    BXP = Stock(
        name='Boston Properties, Inc.',
        ticker='BXP',
        marketCap=14277320704,
        dayHigh=94.785,
        dayLow=91.26,
        currentPrice=91.4,
        longBusinessSummary="Boston Properties (NYSE:BXP) is the largest publicly-held developer and owner of Class A office properties in the United States, concentrated in five markets - Boston, Los Angeles, New York, San Francisco and Washington, DC. The Company is a fully integrated real estate company, organized as a real estate investment trust (REIT), that develops, manages, operates, acquires and owns a diverse portfolio of primarily Class A office space. The Company's portfolio totals 51.2 million square feet and 196 properties, including six properties under construction/redevelopment.",
        fullTimeEmployees=743,
        city='Boston',
        state='MA',
        trailingPE=44.716244,
        dividendYield=0.0348,
        averageVolume=896569,
        regularMarketOpen=93.53,
        volume=1059795,
        fiftyTwoWeekHigh=133.11,
        fiftyTwoWeekLow=88.02,
        recommendationKey='buy',
        industry='REIT—Office'
    )
    db.session.add(BXP)

    BSX = Stock(
        name='Boston Scientific Corporation',
        ticker='BSX',
        marketCap=53437124608,
        dayHigh=38.27,
        dayLow=37.4,
        currentPrice=37.5,
        longBusinessSummary='Boston Scientific Corporation develops, manufactures, and markets medical devices for use in various interventional medical specialties worldwide. It operates through three segments: MedSurg, Rhythm and Neuro, and Cardiovascular. The company offers devices to diagnose and treat gastrointestinal and pulmonary conditions; devices to treat various urological and pelvic conditions; implantable cardioverter and implantable cardiac resynchronization therapy defibrillators; pacemakers and implantable cardiac resynchronization therapy pacemakers; and remote patient management systems. It also provides medical technologies to diagnose and treat rate and rhythm disorders of the heart comprising 3-D cardiac mapping and navigation solutions, ablation catheters, diagnostic catheters, mapping catheters, intracardiac ultrasound catheters, delivery sheaths, and other accessories; spinal cord stimulator systems for the management of chronic pain; indirect decompression systems; and deep brain stimulation systems. In addition, the company offers interventional cardiology products, including drug-eluting coronary stent systems used in the treatment of coronary artery disease; percutaneous coronary interventions products to treat atherosclerosis; intravascular catheter-directed ultrasound imaging catheters, fractional flow reserve devices, and systems for use in coronary arteries and heart chambers, as well as various peripheral vessels; and structural heart therapies. Further, it provides stents, balloon catheters, wires, and atherectomy systems to treat arterial diseases; thrombectomy and acoustic pulse thrombolysis systems, wires, and stents to treat venous diseases; and peripheral embolization devices, radioactive microspheres, ablation systems, cryotherapy ablation systems, and micro and drainage catheters to treat cancer. The company was incorporated in 1979 and is headquartered in Marlborough, Massachusetts.',
        fullTimeEmployees=41000,
        city='Marlborough',
        state='MA',
        trailingPE=48.76463,
        dividendYield=None,
        averageVolume=8878425,
        regularMarketOpen=38.04,
        volume=9275120,
        fiftyTwoWeekHigh=47.5,
        fiftyTwoWeekLow=34.98,
        recommendationKey='buy',
        industry='Medical Devices'
    )
    db.session.add(BSX)

    AVGO = Stock(
        name='Broadcom Inc.',
        ticker='AVGO',
        marketCap=205797048320,
        dayHigh=514.15,
        dayLow=498.105,
        currentPrice=498.45,
        longBusinessSummary='Broadcom Inc. designs, develops, and supplies various semiconductor devices with a focus on complex digital and mixed signal complementary metal oxide semiconductor based devices and analog III-V based products worldwide. The company operates in two segments, Semiconductor Solutions and Infrastructure Software. It provides set-top box system-on-chips (SoCs); cable, digital subscriber line, and passive optical networking central office/consumer premise equipment SoCs; wireless local area network access point SoCs; Ethernet switching and routing merchant silicon products; embedded processors and controllers; serializer/deserializer application specific integrated circuits; optical and copper, and physical layers; and fiber optic transmitter and receiver components. The company also offers RF front end modules, filters, and power amplifiers; Wi-Fi, Bluetooth, and global positioning system/global navigation satellite system SoCs; custom touch controllers; serial attached small computer system interface, and redundant array of independent disks controllers and adapters; peripheral component interconnect express switches; fiber channel host bus adapters; read channel based SoCs; custom flash controllers; preamplifiers; and optocouplers, industrial fiber optics, and motion control encoders and subsystems. Its products are used in various applications, including enterprise and data center networking, home connectivity, set-top boxes, broadband access, telecommunication equipment, smartphones and base stations, data center servers and storage systems, factory automation, power generation and alternative energy systems, and electronic displays. Broadcom Inc. was incorporated in 2018 and is headquartered in San Jose, California.',
        fullTimeEmployees=20000,
        city='San Jose',
        state='CA',
        trailingPE=33.23,
        dividendYield=0.0279,
        averageVolume=2448450,
        regularMarketOpen=512.61,
        volume=1566143,
        fiftyTwoWeekHigh=677.76,
        fiftyTwoWeekLow=455.71,
        recommendationKey='buy',
        industry='Semiconductors'
    )
    db.session.add(AVGO)

    BR = Stock(
        name='Broadridge Financial Solutions, Inc.',
        ticker='BR',
        marketCap=16456151040,
        dayHigh=148.07,
        dayLow=141.07,
        currentPrice=141.16,
        longBusinessSummary="Broadridge Financial Solutions, Inc. provides investor communications and technology-driven solutions for the financial services industry worldwide. The company's Investor Communication Solutions segment processes and distributes proxy materials to investors in equity securities and mutual funds, as well as facilitates related vote processing services; and offers ProxyEdge, an electronic proxy delivery and voting solution. It also distributes regulatory reports, class action, and corporate action/reorganization event information, as well as tax reporting solutions; and provides content management, composition, and omni-channel distribution of regulatory, marketing, and transactional information, as well as mutual fund trade processing services. This segment offers data and analytics solutions; solutions for public corporations and mutual funds; financial reporting document composition and management solutions; SEC disclosure and filing services; registrar, stock transfer, and record-keeping services; and omni-channel customer communications solutions, as well as operates Broadridge Communications Cloud platform that creates, delivers, and manages communications and customer engagement activities. The company's Global Technology and Operations segment offers desktop productivity tools, data aggregation, performance reporting, portfolio management, order capture and execution, trade confirmation, margin, cash management, clearance and settlement, asset servicing, reference data management, reconciliations, securities financing and collateral optimization, compliance and regulatory reporting, and portfolio accounting and custody-related services. It also provides business process outsourcing services; technology solutions, such as portfolio management, compliance, and operational workflow solutions; and capital market and wealth management solutions. The company was founded in 1962 and is headquartered in Lake Success, New York.",
        fullTimeEmployees=13704,
        city='Lake Success',
        state='NY',
        trailingPE=30.32438,
        dividendYield=0.0184,
        averageVolume=451385,
        regularMarketOpen=146.93,
        volume=507141,
        fiftyTwoWeekHigh=185.4,
        fiftyTwoWeekLow=132.4,
        recommendationKey='hold',
        industry='Information Technology Services'
    )
    db.session.add(BR)

    BRO = Stock(
        name='Brown & Brown, Inc.',
        ticker='BRO',
        marketCap=16298862592,
        dayHigh=59.9,
        dayLow=57.68,
        currentPrice=57.71,
        longBusinessSummary="Brown & Brown, Inc. markets and sells insurance products and services in the United States, Bermuda, Canada, Ireland, the United Kingdom, and the Cayman Islands. It operates through four segments: Retail, National Programs, Wholesale Brokerage, and Services. The Retail segment offers property and casualty, employee benefits insurance products, personal insurance products, specialties insurance products, loss control survey and analysis, consultancy, and claims processing services. It serves commercial, public and quasi-public entities, professional, and individual customers. The National Programs segment offers professional liability and related package insurance products for dentistry, legal, eyecare, insurance, financial, physicians, real estate title professionals, as well as supplementary insurance products related to weddings, events, medical facilities, and cyber liabilities. This segment also offers outsourced product development, marketing, underwriting, actuarial, compliance, and claims and other administrative services to insurance carrier partners; and commercial and public entity-related programs, and flood insurance products. It serves through independent agents. The Wholesale Brokerage segment markets and sells excess and surplus commercial and personal lines insurance through independent agents and brokers. The Services segment offers third-party claims administration and medical utilization management services in the workers' compensation and all-lines liability arenas, Medicare Set-aside, Social Security disability, Medicare benefits advocacy, and claims adjusting services. The company was founded in 1939 and is headquartered in Daytona Beach, Florida.",
        fullTimeEmployees=12023,
        city='Daytona Beach',
        state='FL',
        trailingPE=28.164957,
        dividendYield=0.0070999996,
        averageVolume=1859638,
        regularMarketOpen=59.1,
        volume=1061097,
        fiftyTwoWeekHigh=74,
        fiftyTwoWeekLow=52.18,
        recommendationKey='hold',
        industry='Insurance Brokers'
    )
    db.session.add(BRO)

    CHRW = Stock(
        name='C.H. Robinson Worldwide, Inc.',
        ticker='CHRW',
        marketCap=13137785856,
        dayHigh=105.16,
        dayLow=100.8,
        currentPrice=101.07,
        longBusinessSummary='C.H. Robinson Worldwide, Inc., together with its subsidiaries, provides freight transportation services and logistics solutions to companies in various industries worldwide. The company operates in two segments, North American Surface Transportation and Global Forwarding. It offers transportation and logistics services, such as truckload; less than truckload transportation brokerage services, which include the shipment of single or multiple pallets of freight; intermodal transportation that comprise the shipment service of freight in containers or trailers by a combination of truck and rail; and non-vessel ocean common carrier and freight forwarding services, as well as organizes air shipments and provides door-to-door services. The company also offers customs broker services; and other logistics services, such as fee-based managed, warehousing, small parcel, and other services. It has contractual relationships with approximately 85,000 transportation companies, including motor carriers, railroads, and air and ocean carriers. In addition, the company is involved in buying, selling, and/or marketing of fresh produce, including fresh fruits, vegetables, and other value-added perishable items under the Robinson Fresh name. Further, it provides transportation management services or managed TMS; and other surface transportation services. The company offers its fresh produce to grocery retailers, restaurants, produce wholesalers, and foodservice distributors through a network of independent produce growers and suppliers. C.H. Robinson Worldwide, Inc. was founded in 1905 and is headquartered in Eden Prairie, Minnesota.',
        fullTimeEmployees=17258,
        city='Eden Prairie',
        state='MN',
        trailingPE=17.901169,
        dividendYield=0.0208,
        averageVolume=1307448,
        regularMarketOpen=104.28,
        volume=1037314,
        fiftyTwoWeekHigh=115.99,
        fiftyTwoWeekLow=84.67,
        recommendationKey='buy',
        industry='Integrated Freight & Logistics'
    )
    db.session.add(CHRW)

    CDNS = Stock(
        name='Cadence Design Systems, Inc.',
        ticker='CDNS',
        marketCap=41604403200,
        dayHigh=155.37,
        dayLow=149.51,
        currentPrice=150.12,
        longBusinessSummary="Cadence Design Systems, Inc. provides software, hardware, services, and reusable integrated circuit (IC) design blocks worldwide. The company offers functional verification services, including emulation and prototyping hardware. Its functional verification offering consists of JasperGold, a formal verification platform; Xcelium, a parallel logic simulation platform; Palladium, an enterprise emulation platform; and Protium, a prototyping platform for chip verification. The company also provides digital IC design and sign off products, including Genus logic synthesis and Joules RTL power solutions, as well as Modus software solution to reduce systems-on-chip design-for-test time; physical implementation tools, such as place and route, optimization, and multiple patterning preparation; and signoff products to signoff the design as ready for silicon manufacturing. In addition, it offers custom IC design and simulation products to create schematic and physical representations of circuits down to the transistor level for analog, mixed-signal, custom digital, memory, and radio frequency designs; and system design and analysis products to develop printed circuit boards and IC packages, as well as to analyze electromagnetic, electro-thermal, and other multi-physics effects. Further, the company provides intellectual property (IP) products comprising pre-verified and customizable functional blocks to integrate into customer's ICs; and verification IP and memory models to emulate and model the expected behavior and interaction of standard industry system interface protocols. Additionally, it offers services related to methodology, education, and hosted design solutions, as well as technical support and maintenance services. The company serves 5G communications, aerospace and defense, automotive, industrial and healthcare, mobile, consumer, and hyperscale computing markets. Cadence Design Systems, Inc. was incorporated in 1987 and is headquartered in San Jose, California.",
        fullTimeEmployees=9300,
        city='San Jose',
        state='CA',
        trailingPE=60.532257,
        dividendYield=None,
        averageVolume=1637333,
        regularMarketOpen=154.39,
        volume=1161715,
        fiftyTwoWeekHigh=192.7,
        fiftyTwoWeekLow=132.32,
        recommendationKey='buy',
        industry='Software—Application'
    )
    db.session.add(CDNS)

    CPT = Stock(
        name='Camden Property Trust',
        ticker='CPT',
        marketCap=13774111744,
        dayHigh=137.95,
        dayLow=134.5,
        currentPrice=134.78,
        longBusinessSummary="Camden Property Trust, an S&P 400 Company, is a real estate company primarily engaged in the ownership, management, development, redevelopment, acquisition, and construction of multifamily apartment communities. Camden owns interests in and operates 167 properties containing 56,850 apartment homes across the United States. Upon completion of 7 properties currently under development, the Company's portfolio will increase to 59,104 apartment homes in 174 properties. Camden has been recognized as one of the 100 Best Companies to Work For® by FORTUNE magazine for 13 consecutive years, most recently ranking #18. The Company also received a Glassdoor Employees' Choice Award in 2020, ranking #25 for large U.S. companies.",
        fullTimeEmployees=1700,
        city='Houston',
        state='TX',
        trailingPE=113.2605,
        dividendYield=0.025799999,
        averageVolume=1352729,
        regularMarketOpen=136.52,
        volume=514594,
        fiftyTwoWeekHigh=180.37,
        fiftyTwoWeekLow=125.17,
        recommendationKey='buy',
        industry='REIT—Residential'
    )
    db.session.add(CPT)

    CPB = Stock(
        name='Campbell Soup Company',
        ticker='CPB',
        marketCap=14450232320,
        dayHigh=48.44,
        dayLow=47.595,
        currentPrice=47.89,
        longBusinessSummary="Campbell Soup Company, together with its subsidiaries, manufactures and markets food and beverage products the United States and internationally. The company operates through Meals & Beverages and Snacks segments. The Meals & Beverages segment engages in the retail and foodservice businesses in the United States and Canada. This segment provides Campbell's condensed and ready-to-serve soups; Swanson broth and stocks; Pacific Foods broth, soups, and non-dairy beverages; Prego pasta sauces; Pace Mexican sauces; Campbell's gravies, pasta, beans, and dinner sauces; Swanson canned poultry; Plum baby food and snacks; V8 juices and beverages; and Campbell's tomato juice. The Snacks segment retails Pepperidge Farm cookies, crackers, fresh bakery, and frozen products; Milano cookies and Goldfish crackers; and Snyder's of Hanover pretzels, Lance sandwich crackers, Cape Cod and Kettle Brand potato chips, Late July snacks, Snack Factory Pretzel Crisps, Pop Secret popcorn, Emerald nuts, and other snacking products. This segment is also involved in the retail business in Latin America. It sells its products through retail food chains, mass discounters and merchandisers, club stores, convenience stores, drug stores, and dollar stores, as well as e-commerce and other retail, commercial, and non-commercial establishments, and independent contractor distributors. The company was founded in 1869 and is headquartered in Camden, New Jersey.",
        fullTimeEmployees=14100,
        city='Camden',
        state='NJ',
        trailingPE=15.34444,
        dividendYield=0.0293,
        averageVolume=2601183,
        regularMarketOpen=48.33,
        volume=2187992,
        fiftyTwoWeekHigh=51.94,
        fiftyTwoWeekLow=39.76,
        recommendationKey='hold',
        industry='Packaged Foods'
    )
    db.session.add(CPB)

    COF = Stock(
        name='Capital One Financial Corporation',
        ticker='COF',
        marketCap=46188498944,
        dayHigh=113.325,
        dayLow=108.19,
        currentPrice=108.52,
        longBusinessSummary='Capital One Financial Corporation operates as the financial services holding company for the Capital One Bank (USA), National Association; and Capital One, National Association, which provides various financial products and services in the United States, Canada, and the United Kingdom. It operates through three segments: Credit Card, Consumer Banking, and Commercial Banking. The company accepts checking accounts, money market deposits, negotiable order of withdrawals, savings deposits, and time deposits. Its loan products include credit card loans; auto and retail banking loans; and commercial and multifamily real estate, and commercial and industrial loans. The company also offers credit and debit card products; online direct banking services; and treasury management and depository services. It serves consumers, small businesses, and commercial clients through digital channels, branches, cafés, and other distribution channels located in New York, Louisiana, Texas, Maryland, Virginia, New Jersey, and California. Capital One Financial Corporation was founded in 1988 and is headquartered in McLean, Virginia.',
        fullTimeEmployees=51500,
        city='McLean',
        state='VA',
        trailingPE=4.058491,
        dividendYield=0.020599999,
        averageVolume=2837517,
        regularMarketOpen=111.58,
        volume=1689708,
        fiftyTwoWeekHigh=177.95,
        fiftyTwoWeekLow=98.54,
        recommendationKey='buy',
        industry='Credit Services'
    )
    db.session.add(COF)

    CAH = Stock(
        name='Cardinal Health, Inc.',
        ticker='CAH',
        marketCap=15165830144,
        dayHigh=55.38,
        dayLow=53.615,
        currentPrice=53.82,
        longBusinessSummary='Cardinal Health, Inc. operates as an integrated healthcare services and products company in the United States, Canada, Europe, Asia, and internationally. It provides customized solutions for hospitals, healthcare systems, pharmacies, ambulatory surgery centers, clinical laboratories, physician offices, and patients in the home. The company operates in two segments, Pharmaceutical and Medical. The Pharmaceutical segment distributes branded and generic pharmaceutical, specialty pharmaceutical, and over-the-counter healthcare and consumer products. The segment also provides services to pharmaceutical manufacturers and healthcare providers for specialty pharmaceutical products; operates nuclear pharmacies and radiopharmaceutical manufacturing facilities; repackages generic pharmaceuticals and over-the-counter healthcare products; and offers medication therapy management and patient outcomes services to hospitals, other healthcare providers, and payers, as well as provides pharmacy management services to hospitals. The Medical segment manufactures, sources, and distributes Cardinal Health branded medical, surgical, and laboratory products and devices that include exam and surgical gloves; needles, syringe and sharps disposals; compressions; incontinences; nutritional delivery products; wound care products; single-use surgical drapes, gowns, and apparels; fluid suction and collection systems; urology products; operating room supply products; and electrode product lines. The segment also distributes a range of national brand products, including medical, surgical, and laboratory products; provides supply chain services and solutions to hospitals, ambulatory surgery centers, clinical laboratories, and other healthcare providers; and assembles and sells sterile, and non-sterile procedure kits. It has a collaboration agreement with Journey Biosciences, Inc. Cardinal Health, Inc. was founded in 1979 and is headquartered in Dublin, Ohio.',
        fullTimeEmployees=44000,
        city='Dublin',
        state='OH',
        trailingPE=13.892617,
        dividendYield=0.0357,
        averageVolume=2618085,
        regularMarketOpen=55,
        volume=1381606,
        fiftyTwoWeekHigh=64.53,
        fiftyTwoWeekLow=45.85,
        recommendationKey='hold',
        industry='Medical Distribution'
    )
    db.session.add(CAH)

    KMX = Stock(
        name='CarMax, Inc.',
        ticker='KMX',
        marketCap=15280716800,
        dayHigh=99.6398,
        dayLow=94.35,
        currentPrice=94.4,
        longBusinessSummary='CarMax, Inc., together with its subsidiaries, operates as a retailer of used vehicles in the United States. The company operates through two segments, CarMax Sales Operations and CarMax Auto Finance. It offers customers a range of makes and models of used vehicles, including domestic, imported, and luxury vehicles, as well as hybrid and electric vehicles; and extended protection plans to customers at the time of sale, as well as sells vehicles that are approximately 10 years old and has more than 100,000 miles through wholesale auctions. The company also provides reconditioning and vehicle repair services; and financing alternatives for retail customers across a range of credit spectrum through its CarMax Auto Finance and arrangements with various financial institutions. As of February 28, 2022, it operated approximately 230 used car stores. CarMax, Inc. was founded in 1993 and is based in Richmond, Virginia.',
        fullTimeEmployees=32647,
        city='Richmond',
        state='VA',
        trailingPE=13.004546,
        dividendYield=None,
        averageVolume=2051680,
        regularMarketOpen=98.16,
        volume=1917496,
        fiftyTwoWeekHigh=155.98,
        fiftyTwoWeekLow=84.37,
        recommendationKey='buy',
        industry='Auto & Truck Dealerships'
    )
    db.session.add(KMX)

    CARR = Stock(
        name='Carrier Global Corporation',
        ticker='CARR',
        marketCap=31188396032,
        dayHigh=36.97,
        dayLow=35.91,
        currentPrice=35.99,
        longBusinessSummary='Carrier Global Corporation provides heating, ventilating, and air conditioning (HVAC), refrigeration, fire, security, and building automation technologies worldwide. It operates through three segments: HVAC, Refrigeration, and Fire & Security. The HVAC segment provides products, controls, services, and solutions to meet the heating, cooling, and ventilation needs of residential and commercial customers. Its products include air conditioners, heating systems, controls, and aftermarket components, as well as aftermarket repair and maintenance services and building automation solutions. The Refrigeration segment offers transport refrigeration and monitoring products and services, as well as digital solutions for trucks, trailers, shipping containers, intermodal applications, food retail, and warehouse cooling; and commercial refrigeration solutions, such as refrigerated cabinets, freezers, systems, and controls. The Fire & Security segment provides various residential, commercial, and industrial technologies, including fire, flame, gas, smoke, and carbon monoxide detection; portable fire extinguishers; fire suppression systems; intruder alarms; access control systems; video management systems; and electronic controls. Its other fire and security service offerings comprise audit, design, installation, and system integration, as well as aftermarket maintenance and repair and monitoring services. The company offers its products under the Autronica, Det-Tronics, Edwards, Fireye, GST, Kidde, LenelS2, Marioff, Onity, and Supra; Carrier, Automated Logic, Bryant, CIAT, Day & Night, Heil, NORESCO, and Riello; and Carrier Commercial Refrigeration, Carrier Transicold, and Sensitech brands. The company was incorporated in 2019 and is headquartered in Palm Beach Gardens, Florida.',
        fullTimeEmployees=58000,
        city='Palm Beach Gardens',
        state='FL',
        trailingPE=14.436422,
        dividendYield=0.0153,
        averageVolume=5089806,
        regularMarketOpen=36.23,
        volume=5035748,
        fiftyTwoWeekHigh=58.89,
        fiftyTwoWeekLow=34.12,
        recommendationKey='buy',
        industry='Building Products & Equipment'
    )
    db.session.add(CARR)

    CTLT = Stock(
        name='Catalent, Inc.',
        ticker='CTLT',
        marketCap=18341083136,
        dayHigh=111.06,
        dayLow=107.09,
        currentPrice=107.14,
        longBusinessSummary='Catalent, Inc., together with its subsidiaries, develops and manufactures solutions for drugs, protein-based biologics, cell and gene therapies, and consumer health products worldwide. It operates through four segments: Biologics, Softgel and Oral Technologies, Oral and Specialty Delivery, and Clinical Supply Services. The Softgel and Oral Technologies segment provides formulation, development, and manufacturing services for soft capsules for use in a range of customer products, such as prescription drugs, over-the-counter medications, dietary supplements, unit-dose cosmetics, and animal health medicinal preparations. The Biologics segment provides biologic cell-line; develops and manufactures cell therapy and viral based gene therapy; formulation, development, and manufacturing for parenteral dose forms, including vials, prefilled syringes, vials, and cartridges; and analytical development and testing services. The Oral and Specialty Delivery segment offers formulation, development, and manufacturing across a range of technologies along with integrated downstream clinical development and commercial supply solutions. This segment also offers oral delivery solutions platform comprising pre-clinical screening, formulation, analytical development, and current good manufacturing practices services. The Clinical Supply Services segment offers manufacturing, packaging, storage, distribution, and inventory management for drugs and biologics clinical trials. It also offers FastChain demand-led clinical supply services. The company serves pharmaceutical, biotechnology, and consumer health companies; and companies in other healthcare market segments, such as animal health and medical devices, as well as in cosmetics industries. Catalent, Inc. was incorporated in 2007 and is headquartered in Somerset, New Jersey.',
        fullTimeEmployees=17300,
        city='Somerset',
        state='NJ',
        trailingPE=33.723637,
        dividendYield=None,
        averageVolume=1260927,
        regularMarketOpen=110.21,
        volume=745045,
        fiftyTwoWeekHigh=142.64,
        fiftyTwoWeekLow=86.34,
        recommendationKey='buy',
        industry='Drug Manufacturers—Specialty & Generic'
    )
    db.session.add(CTLT)

    CAT = Stock(
        name='Caterpillar Inc.',
        ticker='CAT',
        marketCap=101394169856,
        dayHigh=193.1,
        dayLow=187.44,
        currentPrice=187.44,
        longBusinessSummary="Caterpillar Inc. manufactures and sells construction and mining equipment, diesel and natural gas engines, and industrial gas turbines worldwide. Its Construction Industries segment offers asphalt pavers, backhoe loaders, compactors, cold planers, compact track and multi-terrain loaders, excavators, motorgraders, pipelayers, road reclaimers, site prep tractors, skid steer loaders, telehandlers, and utility vehicles; mini, small, medium, and large excavators; compact, small, and medium wheel loaders; track-type tractors and loaders; and wheel excavators. The Resource Industries segment provides electric rope shovels, draglines, hydraulic shovels, rotary drills, hard rock vehicles, track-type tractors, mining trucks, longwall miners, wheel loaders, off-highway trucks, articulated trucks, wheel tractor scrapers, wheel dozers, fleet management, landfill compactors, soil compactors, machinery components, autonomous ready vehicles and solutions, select work tools, and safety services and mining performance solutions. The Energy & Transportation segment offers reciprocating engines, generator sets, integrated systems and solutions, turbines and turbine-related services, remanufactured reciprocating engines and components, centrifugal gas compressors, diesel-electric locomotives and components, and other rail-related products and services for marine, oil and gas, industrial, and electric power generation sectors. The company's Financial Products segment provides operating and finance leases, installment sale contracts, working capital loans, and wholesale financing plans; and insurance and risk management products for vehicles, power generation facilities, and marine vessels. The All Other operating segment manufactures filters and fluids, undercarriage, ground engaging tools, etc. The company was formerly known as Caterpillar Tractor Co. and changed its name to Caterpillar Inc. in 1986. The company was founded in 1925 and is headquartered in Deerfield, Illinois.",
        fullTimeEmployees=107700,
        city='Deerfield',
        state='IL',
        trailingPE=20.05135,
        dividendYield=0.0217,
        averageVolume=3213506,
        regularMarketOpen=189.97,
        volume=3325848,
        fiftyTwoWeekHigh=237.9,
        fiftyTwoWeekLow=176.02,
        recommendationKey='buy',
        industry='Farm & Heavy Construction Machinery'
    )
    db.session.add(CAT)

    CBOE = Stock(
        name='Cboe Global Markets, Inc.',
        ticker='CBOE',
        marketCap=12164766720,
        dayHigh=116.125,
        dayLow=113.24,
        currentPrice=114.07,
        longBusinessSummary='Cboe Global Markets, Inc., through its subsidiaries, operates as an options exchange worldwide. It operates through five segments: Options, North American Equities, Futures, Europe and Asia Pacific, and Global FX. The Options segment trades in listed market indices. The North American Equities segment trades in listed U.S. and Canadian equities. This segment also offers exchange-traded products (ETP) transaction and ETP listing services. The Futures segment trades in futures. The Europe and Asia Pacific segment offers pan-European listed equities and derivatives transaction services, ETPs, exchange-traded commodities, and international depository receipts, as well as ETP listings and clearing services. The Global FX segment provides institutional foreign exchange (FX) trading and non-deliverable forward FX transactions services. The company has strategic relationships with S&P Dow Jones Indices, LLC; FTSE International Limited; Frank Russell Company; MSCI Inc.; and DJI Opco, LLC. The company was formerly known as CBOE Holdings, Inc. and changed its name to Cboe Global Markets, Inc. in October 2017. Cboe Global Markets, Inc. was founded in 1973 and is headquartered in Chicago, Illinois.',
        fullTimeEmployees=1196,
        city='Chicago',
        state='IL',
        trailingPE=27.263384,
        dividendYield=0.0176,
        averageVolume=657093,
        regularMarketOpen=114.31,
        volume=398871,
        fiftyTwoWeekHigh=139,
        fiftyTwoWeekLow=103.82,
        recommendationKey='buy',
        industry='Financial Data & Stock Exchanges'
    )
    db.session.add(CBOE)

    CBRE = Stock(
        name='CBRE Group, Inc.',
        ticker='CBRE',
        marketCap=24584562688,
        dayHigh=75.43,
        dayLow=73.3,
        currentPrice=73.46,
        longBusinessSummary='CBRE Group, Inc. operates as a commercial real estate services and investment company worldwide. It operates through three segments: Advisory Services, Global Workplace Solutions, and Real Estate Investments segments. The Advisory Services segment provides strategic advice and execution to owners, investors, and occupiers of real estate in connection with leasing; property sales and mortgage services under the CBRE Capital Markets brand; property and project management services, including construction management, marketing, building engineering, accounting, and financial services for owners of and investors in office, industrial, and retail properties; and valuation services that include market value appraisals, litigation support, discounted cash flow analyses, and feasibility studies, as well as consulting services, such as property condition reports, hotel advisory, and environmental consulting. The Global Workplace Solutions segment offers facilities management, project management, and transaction management services. The Real Estate Investments segment provides investment management services under the CBRE Investment Management brand to pension funds, insurance companies, sovereign wealth funds, foundations, endowments, and other institutional investors; development services under the Trammell Crow Company brand primarily to users of and investors in commercial real estate; and flexible-space solutions under the CBRE Hana brand. The company was founded in 1906 and is headquartered in Dallas, Texas.',
        fullTimeEmployees=105000,
        city='Dallas',
        state='TX',
        trailingPE=17.123543,
        dividendYield=None,
        averageVolume=2224682,
        regularMarketOpen=74.67,
        volume=1563382,
        fiftyTwoWeekHigh=111,
        fiftyTwoWeekLow=67.68,
        recommendationKey='buy',
        industry='Real Estate Services'
    )
    db.session.add(CBRE)

    CDW = Stock(
        name='CDW Corporation',
        ticker='CDW',
        marketCap=21630175232,
        dayHigh=166.74,
        dayLow=159.13,
        currentPrice=159.37,
        longBusinessSummary='CDW Corporation provides information technology (IT) solutions in the United States, the United Kingdom, and Canada. It operates through three segments: Corporate, Small Business, and Public. The company offers discrete hardware and software products and services, as well as integrated IT solutions, including on-premise, hybrid, and cloud capabilities across data center and networking, digital workspace, and security. Its hardware products comprise notebooks/mobile devices, network communications, desktop computers, video monitors, enterprise and data storage, and others; and software products consists of application suites, security, virtualization, operating systems, and network management. The company also provides advisory and design, software development, implementation, managed, professional, configuration, and telecom services, as well as warranties; mission critical software, systems, and network solutions; and implementation and installation, and repair services to its customers through various third-party service providers. It serves government, education, and healthcare customers; and small, medium, and large business customers. The company was founded in 1984 and is headquartered in Vernon Hills, Illinois.',
        fullTimeEmployees=13900,
        city='Vernon Hills',
        state='IL',
        trailingPE=22.396008,
        dividendYield=0.0117999995,
        averageVolume=893425,
        regularMarketOpen=165.72,
        volume=680693,
        fiftyTwoWeekHigh=208.71,
        fiftyTwoWeekLow=154.13,
        recommendationKey='buy',
        industry='Information Technology Services'
    )
    db.session.add(CDW)

    CE = Stock(
        name='Celanese Corporation',
        ticker='CE',
        marketCap=13392222208,
        dayHigh=126.67,
        dayLow=122.24,
        currentPrice=123.01,
        longBusinessSummary='Celanese Corporation, a technology and specialty materials company, manufactures and sells high performance engineered polymers in the United States and internationally. The company operates through three segments: Engineered Materials, Acetate Tow, and Acetyl Chain. The Engineered Materials segment develops, produces, and supplies specialty polymers for automotive and medical applications, as well as for use in industrial products and consumer electronics. It also offers acesulfame potassium, a sweetener for use in various beverages, confections, and dairy products; and food protection ingredients, such as potassium sorbate and sorbic acid for use in foods, beverages, and personal care products. The Acetate Tow segment provides acetate tows and flakes for use in filter products applications. The Acetyl Chain segment produces and supplies acetyl products, including acetic acid, vinyl acetate monomers, acetic anhydride, and acetate esters that are used as starting materials for colorants, paints, adhesives, coatings, and pharmaceuticals; and organic solvents and intermediates for pharmaceutical, agricultural, and chemical products. It also offers vinyl acetate-based emulsions for use in paints and coatings, adhesives, construction, glass fiber, textiles, and paper applications; and ethylene vinyl acetate resins and compounds, as well as low-density polyethylene for use in flexible packaging films, lamination film products, hot melt adhesives, automotive parts, and carpeting applications. In addition, it manufactures ultra-high molecular weight polyethylene. Celanese Corporation was founded in 1918 and is headquartered in Irving, Texas.',
        fullTimeEmployees=8500,
        city='Irving',
        state='TX',
        trailingPE=4.9616814,
        dividendYield=0.0191,
        averageVolume=980370,
        regularMarketOpen=125.16,
        volume=1105523,
        fiftyTwoWeekHigh=176.5,
        fiftyTwoWeekLow=118.13,
        recommendationKey='buy',
        industry='Chemicals'
    )
    db.session.add(CE)

    CNC = Stock(
        name='Centene Corporation',
        ticker='CNC',
        marketCap=49206808576,
        dayHigh=86.98,
        dayLow=84.07,
        currentPrice=84.33,
        longBusinessSummary="Centene Corporation operates as a multi-national healthcare enterprise that provides programs and services to under-insured and uninsured individuals in the United States. Its Managed Care segment offers health plan coverage to individuals through government subsidized programs, including Medicaid, the State children's health insurance program, long-term services and support, foster care, and medicare-medicaid plans, which cover dually eligible individuals, as well as aged, blind, or disabled programs. Its health plans include primary and specialty physician care, inpatient and outpatient hospital care, emergency and urgent care, prenatal care, laboratory and X-ray, home-based primary care, transportation assistance, vision care, dental care, telehealth, immunization, specialty pharmacy, therapy, social work, nurse advisory, and care coordination services, as well as prescriptions and limited over-the-counter drugs, medical equipment, and behavioral health and abuse services. This segment also offers various individual, small group, and large group commercial healthcare products to employers and directly to members. The company's Specialty Services segment provides pharmacy benefits management services; nurse advice line and after-hours support services; vision and dental services, as well as staffing services to correctional systems and other government agencies; and services to Military Health System eligible beneficiaries. This segment offers its services and products to state programs, correctional facilities, healthcare organizations, employer groups, and other commercial organizations. The company provides its services through primary and specialty care physicians, hospitals, and ancillary providers. Centene Corporation was founded in 1984 and is headquartered in St. Louis, Missouri.",
        fullTimeEmployees=72500,
        city='Saint Louis',
        state='MO',
        trailingPE=67.51802,
        dividendYield=None,
        averageVolume=2837030,
        regularMarketOpen=85.33,
        volume=2403626,
        fiftyTwoWeekHigh=89.92,
        fiftyTwoWeekLow=59.67,
        recommendationKey='buy',
        industry='Healthcare Plans'
    )
    db.session.add(CNC)

    CNP = Stock(
        name='CenterPoint Energy, Inc.',
        ticker='CNP',
        marketCap=18293710848,
        dayHigh=29.61,
        dayLow=29.045,
        currentPrice=29.09,
        longBusinessSummary='CenterPoint Energy, Inc. operates as a public utility holding company in the United States. The company operates through Electric and Natural Gas segments. The Electric segment includes electric transmission and distribution services to electric customers and electric generation assets, as well as assets in the wholesale power market. The Natural Gas segment provides natural gas distribution services, as well as home appliance maintenance and repair services to customers in Minnesota; and home repair protection plans to natural gas customers in Arkansas, Indiana, Mississippi, Ohio, Oklahoma, and Texas and Louisiana through a third party. This segment also engages in the sale of regulated intrastate natural gas, and transportation and storage of natural gas for residential, commercial, industrial, and transportation customers. As of December 31, 2021, it served approximately 2.7 million metered customers; owned 239 substation sites with a total installed rated transformer capacity of 71,241 megavolt amperes; operated approximately 1,00,000 linear miles of natural gas distribution and transmission mains; and owned and operated 285 miles of intrastate pipeline in Louisiana, Texas, and Oklahoma. The company was founded in 1866 and is headquartered in Houston, Texas.',
        fullTimeEmployees=9418,
        city='Houston',
        state='TX',
        trailingPE=18.493326,
        dividendYield=0.0219,
        averageVolume=5086704,
        regularMarketOpen=29.17,
        volume=3928661,
        fiftyTwoWeekHigh=33,
        fiftyTwoWeekLow=24.23,
        recommendationKey='buy',
        industry='Utilities—Regulated Electric'
    )
    db.session.add(CNP)

    CF = Stock(
        name='CF Industries Holdings, Inc.',
        ticker='CF',
        marketCap=18835195904,
        dayHigh=90.74,
        dayLow=86.87,
        currentPrice=87.82,
        longBusinessSummary='CF Industries Holdings, Inc. manufactures and sells hydrogen and nitrogen products for energy, fertilizer, emissions abatement, and other industrial activities worldwide. Its principal products include anhydrous ammonia, granular urea, urea ammonium nitrate, and ammonium nitrate products. The company also offers diesel exhaust fluid, urea liquor, nitric acid, and aqua ammonia products; and compound fertilizer products with nitrogen, phosphorus, and potassium. It primarily serves cooperatives, independent fertilizer distributors, traders, wholesalers, and industrial users. The company was founded in 1946 and is headquartered in Deerfield, Illinois.',
        fullTimeEmployees=2970,
        city='Deerfield',
        state='IL',
        trailingPE=63.63768,
        dividendYield=0.0154,
        averageVolume=3722224,
        regularMarketOpen=88.65,
        volume=2231271,
        fiftyTwoWeekHigh=113.49,
        fiftyTwoWeekLow=43.19,
        recommendationKey='buy',
        industry='Agricultural Inputs'
    )
    db.session.add(CF)

    CRL = Stock(
        name='Charles River Laboratories International, Inc.',
        ticker='CRL',
        marketCap=10976007168,
        dayHigh=226.76,
        dayLow=217.29,
        currentPrice=217.5,
        longBusinessSummary='Charles River Laboratories International, Inc., a non-clinical contract research organization, provides drug discovery, non-clinical development, and safety testing services in the United States, Europe, Canada, the Asia Pacific, and internationally. It operates through three segments: Research Models and Services (RMS), Discovery and Safety Assessment (DSA), and Manufacturing Solutions (Manufacturing). The RMS segment produces and sells rodent research model strains and purpose-bred rats and mice for use by researchers. This segment also provides a range of services to assist its clients in supporting the use of research models in research and screening non-clinical drug candidates, including research models, genetically engineered models and services, insourcing solutions, and research animal diagnostic services. The DSA segment offers early and in vivo discovery services for the identification and validation of novel targets, chemical compounds, and antibodies through delivery of non-clinical drug and therapeutic candidates ready for safety assessment; and safety assessment services, such as toxicology, pathology, safety pharmacology, bioanalysis, drug metabolism, and pharmacokinetics services. The Manufacturing segment provides in vitro methods for conventional and rapid quality control testing of sterile and non-sterile pharmaceuticals and consumer products. This segment also offers specialized testing of biologics that are outsourced by pharmaceutical and biotechnology companies; and avian vaccine services that provide specific-pathogen-free (SPF) fertile chicken eggs, SPF chickens, and diagnostic products used to manufacture vaccines. The company also provides contract vivarium operation services to biopharmaceutical clients. Charles River Laboratories International, Inc. was founded in 1947 and is headquartered in Wilmington, Massachusetts.',
        fullTimeEmployees=18600,
        city='Wilmington',
        state='MA',
        trailingPE=28.169926,
        dividendYield=None,
        averageVolume=549593,
        regularMarketOpen=225.86,
        volume=320333,
        fiftyTwoWeekHigh=460.21,
        fiftyTwoWeekLow=203.37,
        recommendationKey='buy',
        industry='Diagnostics & Research'
    )
    db.session.add(CRL)

    SCHW = Stock(
        name='The Charles Schwab Corporation',
        ticker='SCHW',
        marketCap=121319792640,
        dayHigh=65.61,
        dayLow=63.965,
        currentPrice=64.17,
        longBusinessSummary='The Charles Schwab Corporation, together with its subsidiaries, provides wealth management, securities brokerage, banking, asset management, custody, and financial advisory services. The company operates in two segments, Investor Services and Advisor Services. The Investor Services segment provides retail brokerage, investment advisory, banking and trust, retirement plan, and other corporate brokerage services; equity compensation plan sponsors full-service recordkeeping for stock plans, stock options, restricted stock, performance shares, and stock appreciation rights; and retail investor and mutual fund clearing services, as well as compliance solutions. The Advisor Services segment offers custodial, trading, banking, and support services; and retirement business and corporate brokerage retirement services. This segment provides brokerage accounts with equity and fixed income, margin lending, options, and futures and forex trading; cash management capabilities comprising third-party certificates of deposit; third-party and proprietary mutual funds; plus mutual fund trading and clearing services; and exchange-traded funds (ETFs), including proprietary and third-party ETFs. It also offers advice solutions, such as managed portfolios of proprietary and third-party mutual funds and ETFs, separately managed accounts, customized personal advice for tailored portfolios, and specialized planning and portfolio management. In addition, this segment provides banking products and services, including checking and savings accounts, first lien residential real estate mortgage loans, home equity lines of credit, and pledged asset lines; and trust services comprising trust custody services, personal trust reporting services, and administrative trustee services. As of December 31, 2021, the Company had approximately 400 domestic branch offices in 48 states and the District of Columbia, as well as locations in Puerto Rico, the United Kingdom, Hong Kong, and Singapore. The Charles Schwab Corporation was incorporated in 1971 and is headquartered in Westlake, Texas.',
        fullTimeEmployees=34200,
        city='Westlake',
        state='TX',
        trailingPE=24.427101,
        dividendYield=0.012200001,
        averageVolume=9206216,
        regularMarketOpen=65.14,
        volume=7136935,
        fiftyTwoWeekHigh=96.24,
        fiftyTwoWeekLow=59.35,
        recommendationKey='buy',
        industry='Capital Markets'
    )
    db.session.add(SCHW)

    CHTR = Stock(
        name='Charter Communications, Inc.',
        ticker='CHTR',
        marketCap=81941372928,
        dayHigh=474.5,
        dayLow=456.48,
        currentPrice=457.03,
        longBusinessSummary='Charter Communications, Inc. operates as a broadband connectivity and cable operator company serving residential and commercial customers in the United States. The company offers subscription-based video services, including video on demand, high-definition television, digital video recorder, pay-per-view services. It provides Internet services, such as security suite that protects computers from viruses and spyware, and threats from malicious actors; in-home WiFi, which provides customers with high performance wireless routers to enhance their in-home wireless Internet experience; out-of-home WiFi; and Spectrum WiFi services, as well as video services. The company also offers voice communications services using voice over Internet protocol technology; and broadband communications solutions, such as Internet access, data networking, fiber connectivity, video entertainment, and business telephone services to cellular towers and office buildings for business and carrier organizations. In addition, it provides mobile services; offers video programming, static IP and business WiFi, email and security, and multi-line telephone services, as well as Web-based service management; sells local advertising across various platforms for networks, such as TBS, CNN, and ESPN; sells advertising inventory to local sports and news channels; and offers Audience App for optimizes linear inventory. Further, the company offers communications products and managed service solutions; data connectivity services to mobile and wireline carriers on a wholesale basis; and owns and operates regional sports and news networks. It serves approximately 32 million customers in 41 states. The company was founded in 1993 and is headquartered in Stamford, Connecticut.',
        fullTimeEmployees=93700,
        city='Stamford',
        state='CT',
        trailingPE=20.828054,
        dividendYield=None,
        averageVolume=1504906,
        regularMarketOpen=468.41,
        volume=799488,
        fiftyTwoWeekHigh=825.62,
        fiftyTwoWeekLow=407.75,
        recommendationKey='buy',
        industry='Entertainment'
    )
    db.session.add(CHTR)

    CVX = Stock(
        name='Chevron Corporation',
        ticker='CVX',
        marketCap=289037844480,
        dayHigh=152.185,
        dayLow=148.11,
        currentPrice=149.94,
        longBusinessSummary='Chevron Corporation, through its subsidiaries, engages in integrated energy and chemicals operations worldwide. The company operates in two segments, Upstream and Downstream. The Upstream segment is involved in the exploration, development, production, and transportation of crude oil and natural gas; processing, liquefaction, transportation, and regasification associated with liquefied natural gas; transportation of crude oil through pipelines; and transportation, storage, and marketing of natural gas, as well as operates a gas-to-liquids plant. The Downstream segment engages in refining crude oil into petroleum products; marketing crude oil, refined products, and lubricants; manufacturing and marketing of renewable fuels; transporting crude oil and refined products by pipeline, marine vessel, motor equipment, and rail car; and manufacturing and marketing of commodity petrochemicals, plastics for industrial uses, and fuel and lubricant additives. It is also involved in the cash management and debt financing activities; insurance operations; real estate activities; and technology businesses. The company was formerly known as ChevronTexaco Corporation and changed its name to Chevron Corporation in 2005. Chevron Corporation was founded in 1879 and is based in San Ramon, California.',
        fullTimeEmployees=42595,
        city='San Ramon',
        state='CA',
        trailingPE=28.985117,
        dividendYield=0.033800002,
        averageVolume=11185691,
        regularMarketOpen=150.88,
        volume=8883191,
        fiftyTwoWeekHigh=182.4,
        fiftyTwoWeekLow=92.86,
        recommendationKey='buy',
        industry='Oil & Gas Integrated'
    )
    db.session.add(CVX)

    CMG = Stock(
        name='Chipotle Mexican Grill, Inc.',
        ticker='CMG',
        marketCap=36262871040,
        dayHigh=1346.17,
        dayLow=1287.5,
        currentPrice=1288.87,
        longBusinessSummary='Chipotle Mexican Grill, Inc., together with its subsidiaries, owns and operates Chipotle Mexican Grill restaurants. As of February 15, 2022, it owned and operated approximately 3,000 restaurants in the United States, Canada, the United Kingdom, France, Germany, and rest of Europe. The company was founded in 1993 and is headquartered in Newport Beach, California.',
        fullTimeEmployees=100000,
        city='Newport Beach',
        state='CA',
        trailingPE=51.7473,
        dividendYield=None,
        averageVolume=253538,
        regularMarketOpen=1331.85,
        volume=175953,
        fiftyTwoWeekHigh=1958.55,
        fiftyTwoWeekLow=1196.28,
        recommendationKey='buy',
        industry='Restaurants'
    )
    db.session.add(CMG)

    CHD = Stock(
        name='Church & Dwight Co., Inc.',
        ticker='CHD',
        marketCap=22782498816,
        dayHigh=92.7,
        dayLow=90.985,
        currentPrice=91.13,
        longBusinessSummary="Church & Dwight Co., Inc. develops, manufactures, and markets household, personal care, and specialty products. It operates through three segments: Consumer Domestic, Consumer International, and Specialty Products Division. The company offers cat litters, carpet deodorizers, laundry detergents, and baking soda, as well as other baking soda based products under the ARM & HAMMER brand; condoms, lubricants, and vibrators under the TROJAN brand; stain removers, cleaning solutions, laundry detergents, and bleach alternatives under the OXICLEAN brand; battery-operated and manual toothbrushes under the SPINBRUSH brand; home pregnancy and ovulation test kits under the FIRST RESPONSE brand; depilatories under the NAIR brand; oral analgesics under the ORAJEL brand; laundry detergents under the XTRA brand; gummy dietary supplements under the L'IL CRITTERS and VITAFUSION brands; dry shampoos under the BATISTE brand; water flossers and replacement showerheads under the WATERPIK brand; FLAWLESS products; cold shortening and relief products under the ZICAM brand; and oral care products under the THERABREATH brand. Its specialty products include animal productivity products, such as MEGALAC rumen bypass fat, a supplement that enables cows to maintain energy levels during the period of high milk production; BIO-CHLOR and FERMENTEN, which are used to reduce health issues associated with calving, as well as provides needed protein; and CELMANAX refined functional carbohydrate, a yeast-based prebiotic. The company offers sodium bicarbonate; and cleaning and deodorizing products. It sells its consumer products through supermarkets, mass merchandisers, wholesale clubs, drugstores, convenience stores, home stores, dollar and other discount stores, pet and other specialty stores, and websites and other e-commerce channels; and specialty products to industrial customers and livestock producers through distributors. The company was founded in 1846 and is headquartered in Ewing, New Jersey.",
        fullTimeEmployees=5100,
        city='Ewing',
        state='NJ',
        trailingPE=27.800486,
        dividendYield=0.0107,
        averageVolume=1444914,
        regularMarketOpen=92.56,
        volume=838314,
        fiftyTwoWeekHigh=105.28,
        fiftyTwoWeekLow=80.34,
        recommendationKey='hold',
        industry='Household & Personal Products'
    )
    db.session.add(CHD)

    CI = Stock(
        name='Cigna Corporation',
        ticker='CI',
        marketCap=88229445632,
        dayHigh=271.4,
        dayLow=264.77,
        currentPrice=266.21,
        longBusinessSummary="Cigna Corporation provides insurance and related products and services in the United States. Its Evernorth segment provides a range of coordinated and point solution health services, including pharmacy, benefits management, care delivery and management, and intelligence solutions to health plans, employers, government organizations, and health care providers. The company's Cigna Healthcare segment offers medical, pharmacy, behavioral health, dental, vision, health advocacy programs, and other products and services for insured and self-insured customers; Medicare Advantage, Medicare Supplement, and Medicare Part D plans for seniors, as well as individual health insurance plans to on and off the public exchanges; and health care coverage in its international markets, as well as health care benefits for mobile individuals and employees of multinational organizations. The company also offers permanent insurance contracts sold to corporations to provide coverage on the lives of certain employees for financing employer-paid future benefit obligations. It distributes its products and services through insurance brokers and consultants; directly to employers, unions and other groups, or individuals; and private and public exchanges. The company was founded in 1792 and is headquartered in Bloomfield, Connecticut.",
        fullTimeEmployees=72226,
        city='Bloomfield',
        state='CT',
        trailingPE=11.079618,
        dividendYield=0.0173,
        averageVolume=1638291,
        regularMarketOpen=268.46,
        volume=1297882,
        fiftyTwoWeekHigh=273.58,
        fiftyTwoWeekLow=191.74,
        recommendationKey='buy',
        industry='Healthcare Plans'
    )
    db.session.add(CI)

    CINF = Stock(
        name='Cincinnati Financial Corporation',
        ticker='CINF',
        marketCap=18956625920,
        dayHigh=119.57,
        dayLow=117.58,
        currentPrice=117.64,
        longBusinessSummary="Cincinnati Financial Corporation, together with its subsidiaries, provides property casualty insurance products in the United States. The company operates through five segments: Commercial Lines Insurance, Personal Lines Insurance, Excess and Surplus Lines Insurance, Life Insurance, and Investments. The Commercial Lines Insurance segment offers coverage for commercial casualty, commercial property, commercial auto, and workers' compensation. It also provides director and officer liability insurance, contract and commercial surety bonds, and fidelity bonds; and machinery and equipment coverage. The Personal Lines Insurance segment offers personal auto insurance; homeowner insurance; and dwelling fire, inland marine, personal umbrella liability, and watercraft coverages to individuals. The Excess and Surplus Lines Insurance segment offers commercial casualty insurance that covers businesses for third-party liability from accidents occurring on their premises or arising out of their operations, such as injuries sustained from products; and commercial property insurance, which insures buildings, inventory, equipment, and business income from loss or damage due to various causes, such as fire, wind, hail, water, theft, and vandalism. The Life Insurance segment provides term life insurance products; universal life insurance products; worksite products, such as term life; and whole life insurance products. The Investments segment invests in fixed-maturity investments, including taxable and tax-exempt bonds, and redeemable preferred stocks; and equity investments comprising common and nonredeemable preferred stocks. The company also offers commercial leasing and financing services; and insurance brokerage services. Cincinnati Financial Corporation was founded in 1950 and is headquartered in Fairfield, Ohio.",
        fullTimeEmployees=5166,
        city='Fairfield',
        state='OH',
        trailingPE=7.575016,
        dividendYield=0.0219,
        averageVolume=611046,
        regularMarketOpen=118.16,
        volume=446766,
        fiftyTwoWeekHigh=143.22,
        fiftyTwoWeekLow=108.88,
        recommendationKey='hold',
        industry='Insurance—Property & Casualty'
    )
    db.session.add(CINF)

    CTAS = Stock(
        name='Cintas Corporation',
        ticker='CTAS',
        marketCap=38510137344,
        dayHigh=383.995,
        dayLow=370.52,
        currentPrice=371.49,
        longBusinessSummary='Cintas Corporation provides corporate identity uniforms and related business services primarily in the United States, Canada, and Latin America. It operates through Uniform Rental and Facility Services, First Aid and Safety Services, and All Other segments. The company rents and services uniforms and other garments, including flame resistant clothing, mats, mops and shop towels, and other ancillary items; and provides restroom cleaning services and supplies, as well as sells uniforms. It also offers first aid and safety services, and fire protection products and services. The company provides its products and services through its distribution network and local delivery routes, or local representatives to small service and manufacturing companies, as well as major corporations. Cintas Corporation was founded in 1968 and is headquartered in Cincinnati, Ohio.',
        fullTimeEmployees=40000,
        city='Cincinnati',
        state='OH',
        trailingPE=34.712204,
        dividendYield=0.0101,
        averageVolume=513279,
        regularMarketOpen=380.93,
        volume=299624,
        fiftyTwoWeekHigh=461.44,
        fiftyTwoWeekLow=343.86,
        recommendationKey='buy',
        industry='Specialty Business Services'
    )
    db.session.add(CTAS)

    CSCO = Stock(
        name='Cisco Systems, Inc.',
        ticker='CSCO',
        marketCap=181610299392,
        dayHigh=44.4713,
        dayLow=42.99,
        currentPrice=43.06,
        longBusinessSummary='Cisco Systems, Inc. designs, manufactures, and sells Internet Protocol based networking and other products related to the communications and information technology industry in the Americas, Europe, the Middle East, Africa, the Asia Pacific, Japan, and China. It provides infrastructure platforms, including networking technologies of switching, routing, wireless, and data center products that are designed to work together to deliver networking capabilities, and transport and/or store data. The company also offers collaboration products comprising unified communications, Cisco TelePresence, and conferencing, as well as the Internet of Things and analytics software. In addition, it provides security products, such as network security, cloud and email security, identity and access management, advanced threat protection, and unified threat management products. Further, the company offers a range of service and support options for its customers, including technical support and advanced services. It serves businesses of various sizes, public institutions, governments, and service providers. The company sells its products and services directly, as well as through systems integrators, service providers, other resellers, and distributors. Cisco Systems, Inc. has strategic alliances with other companies. Cisco Systems, Inc. was incorporated in 1984 and is headquartered in San Jose, California.',
        fullTimeEmployees=79500,
        city='San Jose',
        state='CA',
        trailingPE=16.007435,
        dividendYield=0.0307,
        averageVolume=24600203,
        regularMarketOpen=43.91,
        volume=19947340,
        fiftyTwoWeekHigh=64.29,
        fiftyTwoWeekLow=41.02,
        recommendationKey='buy',
        industry='Communication Equipment'
    )
    db.session.add(CSCO)

    C = Stock(
        name='Citigroup Inc.',
        ticker='C',
        marketCap=93677379584,
        dayHigh=49.11,
        dayLow=46.94,
        currentPrice=47.21,
        longBusinessSummary='Citigroup Inc., a diversified financial services holding company, provides various financial products and services to consumers, corporations, governments, and institutions in North America, Latin America, Asia, Europe, the Middle East, and Africa. The company operates in two segments, Global Consumer Banking (GCB) and Institutional Clients Group (ICG). The GCB segment offers traditional banking services to retail customers through retail banking, Citi-branded cards, and Citi retail services. It also provides various banking, credit card, lending, and investment services through a network of local branches, offices, and electronic delivery systems. The ICG segment offers wholesale banking products and services, including fixed income and equity sales and trading, foreign exchange, prime brokerage, derivative, equity and fixed income research, corporate lending, investment banking and advisory, private banking, cash management, trade finance, and securities services to corporate, institutional, public sector, and high-net-worth clients. As of December 31, 2020, it operated 2,303 branches primarily in the United States, Mexico, and Asia. Citigroup Inc. was founded in 1812 and is headquartered in New York, New York.',
        fullTimeEmployees=228000,
        city='New York',
        state='NY',
        trailingPE=4.471491,
        dividendYield=0.0428,
        averageVolume=24994375,
        regularMarketOpen=48.4,
        volume=21260479,
        fiftyTwoWeekHigh=74.64,
        fiftyTwoWeekLow=45.4,
        recommendationKey='buy',
        industry='Banks—Diversified'
    )
    db.session.add(C)

    CFG = Stock(
        name='Citizens Financial Group, Inc.',
        ticker='CFG',
        marketCap=15658589184,
        dayHigh=38.0775,
        dayLow=36.625,
        currentPrice=36.74,
        longBusinessSummary='Citizens Financial Group, Inc. operates as the bank holding company for Citizens Bank, National Association that provides retail and commercial banking products and services to individuals, small businesses, middle-market companies, corporations, and institutions in the United States. The company operates in two segments, Consumer Banking and Commercial Banking. The Consumer Banking segment offers deposit products, mortgage and home equity lending products, credit cards, business loans, wealth management, and investment services; and auto, education, and point-of-sale finance loans, as well as digital deposit products. This segment serves its customers through telephone service centers, as well as through its online and mobile platforms. The Commercial Banking segment provides various financial products and solutions, including lending and leasing, deposit and treasury management services, foreign exchange, and interest rate and commodity risk management solutions, as well as syndicated loans, corporate finance, mergers and acquisitions, and debt and equity capital markets services. This segment serves government banking, not-for-profit, healthcare, technology, professionals, oil and gas, asset finance, franchise finance, asset-based lending, commercial real estate, private equity, and sponsor finance industries. It operates approximately 900 branches in 11 states in the New England, as well as Mid-Atlantic and Midwest regions; 114 retail and commercial non-branch offices in national markets; and approximately 3,000 automated teller machines. The company was formerly known as RBS Citizens Financial Group, Inc. and changed its name to Citizens Financial Group, Inc. in April 2014. Citizens Financial Group, Inc. was founded in 1828 and is headquartered in Providence, Rhode Island.',
        fullTimeEmployees=17463,
        city='Providence',
        state='RI',
        trailingPE=7.3775105,
        dividendYield=0.041100003,
        averageVolume=6913408,
        regularMarketOpen=37.42,
        volume=4750247,
        fiftyTwoWeekHigh=57,
        fiftyTwoWeekLow=34.5,
        recommendationKey='buy',
        industry='Banks—Regional'
    )
    db.session.add(CFG)

    CLX = Stock(
        name='The Clorox Company',
        ticker='CLX',
        marketCap=16824859648,
        dayHigh=138.8,
        dayLow=136.565,
        currentPrice=136.94,
        longBusinessSummary="The Clorox Company manufactures and markets consumer and professional products worldwide. It operates through four segments: Health and Wellness, Household, Lifestyle, and International. The Health and Wellness segment offers cleaning products, such as laundry additives and home care products primarily under the Clorox, Clorox2, Scentiva, Pine-Sol, Liquid-Plumr, Tilex, and Formula 409 brand names; professional cleaning and disinfecting products under the CloroxPro, Clorox Healthcare, and Clorox Total 360 brand names; professional food service products under the Hidden Valley brand name; and vitamins, minerals and supplement products under the RenewLife, Natural Vitality, NeoCell, and Rainbow Light brand names in the United States. The Household segment provides cat litter products under the Fresh Step, Scoop Away, and Ever Clean brand names; bags and wraps under the Glad brand name; and grilling products under the Kingsford and Kingsford Match Light brand names in the United States. The Lifestyle segment offers dressings, dips, seasonings, and sauces primarily under the Hidden Valley brand name; natural personal care products under the Burt's Bees brand name; and water-filtration systems and filters under the Brita brand name in the United States. The International segment provides laundry additives; home care products; water-filtration systems and filters; digestive health products; grilling products; cat litter products; food products; bags and wraps; natural personal care products; and professional cleaning and disinfecting products internationally primarily under the Clorox, Ayudin, Clorinda, Poett, Pine-Sol, Glad, Brita, RenewLife, Ever Clean and Burt's Bees brand names. The Clorox Company sells its products primarily through mass retailers, grocery outlets, warehouse clubs, dollar stores, home hardware centers, third-party and owned e-commerce channels, military stores, and distributors, as well as a direct sales force. The company was founded in 1913 and is headquartered in Oakland, California.",
        fullTimeEmployees=9000,
        city='Oakland',
        state='CA',
        trailingPE=39.498127,
        dividendYield=0.0293,
        averageVolume=1459675,
        regularMarketOpen=138.05,
        volume=951712,
        fiftyTwoWeekHigh=191.75,
        fiftyTwoWeekLow=120.5,
        recommendationKey='hold',
        industry='Household & Personal Products'
    )
    db.session.add(CLX)

    CME = Stock(
        name='CME Group Inc.',
        ticker='CME',
        marketCap=74079322112,
        dayHigh=212.09,
        dayLow=205.42,
        currentPrice=206.12,
        longBusinessSummary='CME Group Inc., together with its subsidiaries, operates contract markets for the trading of futures and options on futures contracts worldwide. It offers futures and options products based on interest rates, equity indexes, foreign exchange, agricultural commodities, energy, and metals, as well as fixed income products. The company also provides clearing house services, including clearing, settling, and guaranteeing futures and options contracts, and cleared swaps products traded through its exchanges; and trade processing and risk mitigation services. In addition, the company offers a range of market data services, including real-time and historical data services. It serves professional traders, financial institutions, institutional and individual investors, corporations, manufacturers, producers, governments, and central banks. The company was formerly known as Chicago Mercantile Exchange Holdings Inc. and changed its name to CME Group Inc. in July 2007. CME Group Inc. was founded in 1898 and is headquartered in Chicago, Illinois.',
        fullTimeEmployees=3480,
        city='Chicago',
        state='IL',
        trailingPE=30.401178,
        dividendYield=0.02,
        averageVolume=1651654,
        regularMarketOpen=209.55,
        volume=1220394,
        fiftyTwoWeekHigh=256.94,
        fiftyTwoWeekLow=185.79,
        recommendationKey='hold',
        industry='Financial Data & Stock Exchanges'
    )
    db.session.add(CME)

    CMS = Stock(
        name='CMS Energy Corporation',
        ticker='CMS',
        marketCap=19282231296,
        dayHigh=67.13,
        dayLow=66.2,
        currentPrice=66.56,
        longBusinessSummary='CMS Energy Corporation operates as an energy company primarily in Michigan. The company operates through three segments: Electric Utility; Gas Utility; and Enterprises. The Electric Utility segment is involved in the generation, purchase, transmission, distribution, and sale of electricity. This segment generates electricity through coal, wind, gas, renewable energy, oil, and nuclear sources. Its distribution system comprises 208 miles of high-voltage distribution overhead lines; 4 miles of high-voltage distribution underground lines; 4,428 miles of high-voltage distribution overhead lines; 19 miles of high-voltage distribution underground lines; 82,474 miles of electric distribution overhead lines; 9,395 miles of underground distribution lines; 1,093 substations; and 3 battery facilities. The Gas Utility segment engages in the purchase, transmission, storage, distribution, and sale of natural gas, which includes 2,392 miles of transmission lines; 15 gas storage fields; 28,065 miles of distribution mains; and 8 compressor stations. The Enterprises segment is involved in the independent power production and marketing, including the development and operation of renewable generation. It serves 1.9 million electric and 1.8 million gas customers, including residential, commercial, and diversified industrial customers. The company was incorporated in 1987 and is headquartered in Jackson, Michigan.',
        fullTimeEmployees=8504,
        city='Jackson',
        state='MI',
        trailingPE=22.06165,
        dividendYield=0.026500002,
        averageVolume=1920754,
        regularMarketOpen=66.38,
        volume=1300676,
        fiftyTwoWeekHigh=73.76,
        fiftyTwoWeekLow=58.51,
        recommendationKey='hold',
        industry='Utilities—Regulated Electric'
    )
    db.session.add(CMS)

    KO = Stock(
        name='The Coca-Cola Company',
        ticker='KO',
        marketCap=269013467136,
        dayHigh=63.75,
        dayLow=62.105,
        currentPrice=62.28,
        longBusinessSummary='The Coca-Cola Company, a beverage company, manufactures, markets, and sells various nonalcoholic beverages worldwide. The company provides sparkling soft drinks; flavored and enhanced water, and sports drinks; juice, dairy, and plantbased beverages; tea and coffee; and energy drinks. It also offers beverage concentrates and syrups, as well as fountain syrups to fountain retailers, such as restaurants and convenience stores. The company sells its products under the Coca-Cola, Diet Coke/Coca-Cola Light, Coca-Cola Zero Sugar, Fanta, Fresca, Schweppes, Sprite, Thums Up, Aquarius, Ciel, dogadan, Dasani, glacéau smartwater, glacéau vitaminwater, Ice Dew, I LOHAS, Powerade, Topo Chico, AdeS, Del Valle, fairlife, innocent, Minute Maid, Minute Maid Pulpy, Simply, Ayataka, BODYARMOR, Costa, FUZE TEA, Georgia, and Gold Peak brands. It operates through a network of independent bottling partners, distributors, wholesalers, and retailers, as well as through bottling and distribution operators. The company was founded in 1886 and is headquartered in Atlanta, Georgia.',
        fullTimeEmployees=79000,
        city='Atlanta',
        state='GA',
        trailingPE=30.664698,
        dividendYield=0.026800001,
        averageVolume=18343474,
        regularMarketOpen=63.08,
        volume=13140457,
        fiftyTwoWeekHigh=67.2,
        fiftyTwoWeekLow=52.28,
        recommendationKey='buy',
        industry='Beverages—Non-Alcoholic'
    )
    db.session.add(KO)

    CTSH = Stock(
        name='Cognizant Technology Solutions Corporation',
        ticker='CTSH',
        marketCap=36189499392,
        dayHigh=70.44,
        dayLow=68.02,
        currentPrice=68.11,
        longBusinessSummary='Cognizant Technology Solutions Corporation, a professional services company, provides consulting and technology, and outsourcing services in North America, Europe, and internationally. It operates through four segments: Financial Services; Healthcare; Products and Resources; and Communications, Media and Technology. The company offers customer experience enhancement, robotic process automation, analytics, and AI services in areas, such as digital lending, fraud detection, and next generation payments; the shift towards consumerism, outcome-based contracting, digital health, delivering integrated seamless, omni-channel, and patient-centered experience; and services that drive operational improvements in areas, such as clinical development, pharmacovigilance, and manufacturing, as well as claims processing, enrollment, membership, and billing to healthcare providers and payers, and life sciences companies, including pharmaceutical, biotech, and medical device companies. It also provides solution to manufacturers, retailers and travel and hospitality companies, as well as companies providing logistics, energy and utility services; and digital content, the creation of personalized user experience, and acceleration of digital engineering services to information, media and entertainment, and communications and technology companies. The company was founded in 1994 and is headquartered in Teaneck, New Jersey.',
        fullTimeEmployees=330600,
        city='Teaneck',
        state='NJ',
        trailingPE=19.212976,
        dividendYield=0.0147,
        averageVolume=3076251,
        regularMarketOpen=69.97,
        volume=2856550,
        fiftyTwoWeekHigh=93.47,
        fiftyTwoWeekLow=65.24,
        recommendationKey='buy',
        industry='Information Technology Services'
    )
    db.session.add(CTSH)

    CL = Stock(
        name='Colgate-Palmolive Company',
        ticker='CL',
        marketCap=66483929088,
        dayHigh=80.37,
        dayLow=78.765,
        currentPrice=78.88,
        longBusinessSummary="Colgate-Palmolive Company, together with its subsidiaries, manufactures and sells consumer products worldwide. The company operates through two segments, Oral, Personal and Home Care; and Pet Nutrition. The Oral, Personal and Home Care segment offers toothpaste, toothbrushes, mouthwash, bar and liquid hand soaps, shower gels, shampoos, conditioners, deodorants and antiperspirants, skin health products, dishwashing detergents, fabric conditioners, household cleaners, and other related items. This segment markets and sells its products under various brands, which include Colgate, Darlie, elmex, hello, meridol, Sorriso, Tom's of Maine, Irish Spring, Palmolive, Protex, Sanex, Softsoap, Lady Speed Stick, Speed Stick, EltaMD, Filorga, PCA SKIN, Ajax, Axion, Fabuloso, Murphy, Suavitel, Soupline, and Cuddly to a range of traditional and eCommerce retailers, wholesalers, and distributors. It also includes pharmaceutical products for dentists and other oral health professionals. The Pet Nutrition segment offers pet nutrition products for everyday nutritional needs under the Hill's Science Diet brand; and a range of therapeutic products to manage disease conditions in dogs and cats under the Hill's Prescription Diet brand. This segment markets and sells its products through pet supply retailers, veterinarians, and eCommerce retailers. Colgate-Palmolive Company was founded in 1806 and is headquartered in New York, New York.",
        fullTimeEmployees=33800,
        city='New York',
        state='NY',
        trailingPE=25.121017,
        dividendYield=0.024,
        averageVolume=5585320,
        regularMarketOpen=80,
        volume=3193786,
        fiftyTwoWeekHigh=85.61,
        fiftyTwoWeekLow=72.2,
        recommendationKey='hold',
        industry='Household & Personal Products'
    )
    db.session.add(CL)

    CMCSA = Stock(
        name='Comcast Corporation',
        ticker='CMCSA',
        marketCap=178781847552,
        dayHigh=40.57,
        dayLow=39.1,
        currentPrice=39.13,
        longBusinessSummary="Comcast Corporation operates as a media and technology company worldwide. It operates through Cable Communications, Media, Studios, Theme Parks, and Sky segments. The Cable Communications segment offers broadband, video, voice, wireless, and other services to residential and business customers under the Xfinity brand; and advertising services. The Media segment operates NBCUniversal's television and streaming platforms, including national, regional, and international cable networks, the NBC and Telemundo broadcast, and Peacock networks. The Studios segment operates NBCUniversal's film and television studio production and distribution operations. The Theme Parks segment operates Universal theme parks in Orlando, Florida; Hollywood, California; Osaka, Japan; and Beijing, China. The Sky segment offers direct-to-consumer services, such as video, broadband, voice and wireless phone services, and content business operates entertainment networks, the Sky News broadcast network, and Sky Sports networks. The company also owns the Philadelphia Flyers, as well as the Wells Fargo Center arena in Philadelphia, Pennsylvania; and provides streaming service, such as Peacock. Comcast Corporation was founded in 1963 and is headquartered in Philadelphia, Pennsylvania.",
        fullTimeEmployees=189000,
        city='Philadelphia',
        state='PA',
        trailingPE=12.586041,
        dividendYield=0.025999999,
        averageVolume=24547551,
        regularMarketOpen=40.03,
        volume=14736157,
        fiftyTwoWeekHigh=61.8,
        fiftyTwoWeekLow=37.56,
        recommendationKey='buy',
        industry='Entertainment'
    )
    db.session.add(CMCSA)

    CMA = Stock(
        name='Comerica Incorporated',
        ticker='CMA',
        marketCap=10057817088,
        dayHigh=78.17,
        dayLow=76.38,
        currentPrice=76.69,
        longBusinessSummary='Comerica Incorporated, through its subsidiaries, provides various financial products and services. It operates through Commercial Bank, Retail Bank, Wealth Management, and Finance segments. The Commercial Bank segment offers various products and services, including commercial loans and lines of credit, deposits, cash management, capital market products, international trade finance, letters of credit, foreign exchange management services, and loan syndication services for small and middle market businesses, multinational corporations, and governmental entities. The Retail Bank segment provides personal financial services, such as consumer lending, consumer deposit gathering, and mortgage loan origination. This segment also offers various consumer products that include deposit accounts, installment loans, credit cards, student loans, home equity lines of credit, and residential mortgage loans, as well as commercial products and services to micro-businesses. The Wealth Management segment provides products and services comprising fiduciary, private banking, retirement, investment management and advisory, and investment banking and brokerage services. This segment also sells annuity products, as well as life, disability, and long-term care insurance products. The Finance segment engages in the securities portfolio, and asset and liability management activities. It operates in Texas, California, Michigan, Arizona, Florida, Canada, and Mexico. The company was formerly known as DETROITBANK Corporation and changed its name to Comerica Incorporated in July 1982. Comerica Incorporated was founded in 1849 and is headquartered in Dallas, Texas.',
        fullTimeEmployees=7484,
        city='Dallas',
        state='TX',
        trailingPE=9.549247,
        dividendYield=0.0357,
        averageVolume=1480364,
        regularMarketOpen=76.99,
        volume=838044,
        fiftyTwoWeekHigh=102.09,
        fiftyTwoWeekLow=63.07,
        recommendationKey='buy',
        industry='Banks—Regional'
    )
    db.session.add(CMA)

    CAG = Stock(
        name='Conagra Brands, Inc.',
        ticker='CAG',
        marketCap=16280677376,
        dayHigh=34.425,
        dayLow=33.85,
        currentPrice=33.94,
        longBusinessSummary="Conagra Brands, Inc., together with its subsidiaries, operates as a consumer packaged goods food company in North America. The company operates through Grocery & Snacks, Refrigerated & Frozen, International, and Foodservice segments. The Grocery & Snacks segment primarily offers shelf stable food products in various retail channels in the United States. The Refrigerated & Frozen segment provides temperature-controlled food products in various retail channels in the United States. The International segment offers food products in various temperature states in retail and foodservice channels outside of the United States. The Foodservice segment offers food products, including meals, entrees, sauces, and various custom-manufactured culinary products packaged for sale to restaurants and other foodservice establishments in the United States. The company sells its products under the Birds Eye, Duncan Hines, Healthy Choice, Marie Callender's, Reddi-wip, Slim Jim, Angie's BOOMCHICKAPOP, Duke's, Earth Balance, Gardein, and Frontera brands. The company was formerly known as ConAgra Foods, Inc. and changed its name to Conagra Brands, Inc. in November 2016. Conagra Brands, Inc. was incorporated in 1919 and is headquartered in Chicago, Illinois.",
        fullTimeEmployees=18600,
        city='Chicago',
        state='IL',
        trailingPE=13.679968,
        dividendYield=0.0348,
        averageVolume=4294088,
        regularMarketOpen=34.16,
        volume=3585897,
        fiftyTwoWeekHigh=36.97,
        fiftyTwoWeekLow=30.06,
        recommendationKey='hold',
        industry='Packaged Foods'
    )
    db.session.add(CAG)

    COP = Stock(
        name='ConocoPhillips',
        ticker='COP',
        marketCap=125590421504,
        dayHigh=97.065,
        dayLow=93.56,
        currentPrice=95.22,
        longBusinessSummary="ConocoPhillips explores for, produces, transports, and markets crude oil, bitumen, natural gas, liquefied natural gas (LNG), and natural gas liquids worldwide. It primarily engages in the conventional and tight oil reservoirs, shale gas, heavy oil, LNG, oil sands, and other production operations. The company's portfolio includes unconventional plays in North America; conventional assets in North America, Europe, Asia, and Australia; various LNG developments; oil sands assets in Canada; and an inventory of conventional and unconventional exploration prospects. ConocoPhillips was founded in 1917 and is headquartered in Houston, Texas.",
        fullTimeEmployees=9900,
        city='Houston',
        state='TX',
        trailingPE=25.825874,
        dividendYield=0.0187,
        averageVolume=8085032,
        regularMarketOpen=94.98,
        volume=8672254,
        fiftyTwoWeekHigh=124.08,
        fiftyTwoWeekLow=51.41,
        recommendationKey='buy',
        industry='Oil & Gas E&P'
    )
    db.session.add(COP)

    ED = Stock(
        name='Consolidated Edison, Inc.',
        ticker='ED',
        marketCap=33294856192,
        dayHigh=94.765,
        dayLow=93.815,
        currentPrice=94.12,
        longBusinessSummary='Consolidated Edison, Inc., through its subsidiaries, engages in the regulated electric, gas, and steam delivery businesses in the United States. It offers electric services to approximately 3.5 million customers in New York City and Westchester County; gas to approximately 1.1 million customers in Manhattan, the Bronx, parts of Queens, and Westchester County; and steam to approximately 1,555 customers in parts of Manhattan. The company also supplies electricity to approximately 0.3 million customers in southeastern New York and northern New Jersey; and gas to approximately 0.1 million customers in southeastern New York. In addition, it operates 533 circuit miles of transmission lines; 15 transmission substations; 64 distribution substations; 87,564 in-service line transformers; 3,924 pole miles of overhead distribution lines; and 2,291 miles of underground distribution lines, as well as 4,350 miles of mains and 377,971 service lines for natural gas distribution. Further, the company owns, operates, and develops renewable and energy infrastructure projects; and provides energy-related products and services to wholesale and retail customers, as well as invests in electric and gas transmission projects. It primarily sells electricity to industrial, commercial, residential, and government customers. The company was founded in 1823 and is based in New York, New York.',
        fullTimeEmployees=13871,
        city='New York',
        state='NY',
        trailingPE=27.879148,
        dividendYield=0.033099998,
        averageVolume=1844482,
        regularMarketOpen=93.98,
        volume=1575107,
        fiftyTwoWeekHigh=101.12,
        fiftyTwoWeekLow=71.17,
        recommendationKey='underperform',
        industry='Utilities—Regulated Electric'
    )
    db.session.add(ED)

    STZ = Stock(
        name='Constellation Brands, Inc.',
        ticker='STZ',
        marketCap=46034755584,
        dayHigh=252.07,
        dayLow=244.69,
        currentPrice=245.52,
        longBusinessSummary="Constellation Brands, Inc., together with its subsidiaries, produces, imports, markets, and sells beer, wine, and spirits in the United States, Canada, Mexico, New Zealand, and Italy. It provides beer primarily under the Corona Extra, Corona Premier, Corona Familiar, Corona Light, Corona Refresca, Corona Hard Seltzer, Modelo Especial, Modelo Negra, Modelo Chelada, Pacifico, and Victoria brands. The company offers wine under the 7 Moons, Cook's California Champagne, Cooper & Thief, Crafters Union, Kim Crawford, Meiomi, Mount Veeder, Ruffino, SIMI, The Dreaming Tree, Charles Smith, The Prisoner Wine Company, Robert Mondavi, My Favorite Neighbor, and Schrader; and spirits under the Casa Noble, Copper & Kings, High West, Mi CAMPO, Nelson's Green Brier, and SVEDKA brands. It provides its products to wholesale distributors, retailers, on-premise locations, and state alcohol beverage control agencies. Constellation Brands, Inc. was founded in 1945 and is headquartered in Victor, New York.",
        fullTimeEmployees=10000,
        city='Victor',
        state='NY',
        trailingPE=63.409092,
        dividendYield=0.012999999,
        averageVolume=1054903,
        regularMarketOpen=248.47,
        volume=681171,
        fiftyTwoWeekHigh=261.52,
        fiftyTwoWeekLow=207.35,
        recommendationKey='buy',
        industry='Beverages—Wineries & Distilleries'
    )
    db.session.add(STZ)

    COO = Stock(
        name='The Cooper Companies, Inc.',
        ticker='COO',
        marketCap=15518063616,
        dayHigh=325.56,
        dayLow=313.42,
        currentPrice=314.08,
        longBusinessSummary="The Cooper Companies, Inc., together with its subsidiaries, develops, manufactures, and markets contact lens wearers. The company operates in two segments, CooperVision and CooperSurgical. The CooperVision segment offers spherical lense, including lenses that correct near and farsightedness; and toric and multifocal lenses comprising lenses correcting vision challenges, such as astigmatism, presbyopia, myopia, ocular dryness and eye fatigues in the Americas, Europe, Middle East, Africa, and Asia Pacific. The CooperSurgical segment focuses on family and women's health care, which provides medical devices, fertility, genomics, diagnostics, and contraception to health care professionals and patients worldwide. It offers surgical and office products, including PARAGARD, uterine manipulators, retractors, closure products, point of care products, LEEP products, endosee, and illuminate and fetal pillows; fertility products and services, such as fertility consumables and equipment, and embryo options and preimplantation genetic testing. The Cooper Companies, Inc. was founded in 1958 and is headquartered in San Ramon, California.",
        fullTimeEmployees=12000,
        city='San Ramon',
        state='CA',
        trailingPE=5.3089924,
        dividendYield=0.0002,
        averageVolume=345582,
        regularMarketOpen=323.43,
        volume=316265,
        fiftyTwoWeekHigh=463.59,
        fiftyTwoWeekLow=297.34,
        recommendationKey='buy',
        industry='Medical Instruments & Supplies'
    )
    db.session.add(COO)

    CPRT = Stock(
        name='Copart, Inc.',
        ticker='CPRT',
        marketCap=25817913344,
        dayHigh=113.33,
        dayLow=108.65,
        currentPrice=108.85,
        longBusinessSummary="Copart, Inc. provides online auctions and vehicle remarketing services in the United States, Canada, the United Kingdom, Brazil, the Republic of Ireland, Germany, Finland, the United Arab Emirates, Oman, Bahrain, and Spain. It offers a range of services for processing and selling vehicles over the internet through its virtual bidding third generation internet auction-style sales technology to vehicle sellers, insurance companies, banks and finance companies, charities, fleet operators, dealers, vehicle rental companies, and individuals. The company's services include online seller access, salvage estimation, estimating, end-of-life vehicle processing, virtual insured exchange, transportation, vehicle inspection stations, on-demand reporting, title processing and procurement, loan payoff, flexible vehicle processing programs, buy it now, member network, sales process, and dealer services. Its services also comprise services to sell vehicles through CashForCars.com; U-Pull-It service that allows buyer to remove valuable parts and sell the remaining parts and car body; copart 360, an online technology for posting vehicle images; membership tiers for those registering to buy vehicles through Copart.com; and virtual queue to secure a place in line while visiting one of its locations. The company sells its products principally to licensed vehicle dismantlers, rebuilders, repair licensees, used vehicle dealers, and exporters, as well as to the public. The company was incorporated in 1982 and is headquartered in Dallas, Texas.",
        fullTimeEmployees=8600,
        city='Dallas',
        state='TX',
        trailingPE=26.228914,
        dividendYield=None,
        averageVolume=1213112,
        regularMarketOpen=112.47,
        volume=863453,
        fiftyTwoWeekHigh=161.12,
        fiftyTwoWeekLow=102.21,
        recommendationKey='buy',
        industry='Auto & Truck Dealerships'
    )
    db.session.add(CPRT)

    GLW = Stock(
        name='Corning Incorporated',
        ticker='GLW',
        marketCap=27735760896,
        dayHigh=33.78,
        dayLow=32.47,
        currentPrice=32.5,
        longBusinessSummary="Corning Incorporated engages in display technologies, optical communications, environmental technologies, specialty materials, and life sciences businesses worldwide. The company's Display Technologies segment offers glass substrates for liquid crystal displays and organic light-emitting diodes used in televisions, notebook computers, desktop monitors, tablets, and handheld devices. Its Optical Communications segment provides optical fibers and cables; and hardware and equipment products, including cable assemblies, fiber optic hardware and connectors, optical components and couplers, closures, network interface devices, and other accessories. This segment also offers its products to businesses, governments, and individuals. Its Specialty Materials segment manufactures products that provide material formulations for glass, glass ceramics, crystals, precision metrology instruments, software; as well as ultra-thin and ultra-flat glass wafers, substrates, tinted sunglasses, and radiation shielding products. This segment serves various industries, including mobile consumer electronics, semiconductor equipment optics and consumables; aerospace and defense optics; radiation shielding products, sunglasses, and telecommunications components. The company's Environmental Technologies segment offers ceramic substrates and filter products for emissions control in mobile, gasoline, and diesel applications. The company's Life Sciences segment offers laboratory products comprising consumables, such as plastic vessels, liquid handling plastics, specialty surfaces, cell culture media, and serum, as well as general labware and equipment under the Corning, Falcon, Pyrex, and Axygen brands. The company was formerly known as Corning Glass Works and changed its name to Corning Incorporated in April 1989. Corning Incorporated was founded in 1851 and is headquartered in Corning, New York.",
        fullTimeEmployees=61200,
        city='Corning',
        state='NY',
        trailingPE=32.370518,
        dividendYield=0.0304,
        averageVolume=5283904,
        regularMarketOpen=33.47,
        volume=3647465,
        fiftyTwoWeekHigh=43.47,
        fiftyTwoWeekLow=30.96,
        recommendationKey='buy',
        industry='Electronic Components'
    )
    db.session.add(GLW)

    CTVA = Stock(
        name='Corteva, Inc.',
        ticker='CTVA',
        marketCap=39557890048,
        dayHigh=55.72,
        dayLow=53.9,
        currentPrice=54.27,
        longBusinessSummary='Corteva, Inc. operates in the agriculture business. It operates through two segments, Seed and Crop Protection. The Seed segment develops and supplies advanced germplasm and traits that produce optimum yield for farms. It offers trait technologies that enhance resistance to weather, disease, insects, and herbicides used to control weeds, as well as food and nutritional characteristics. This segment also provides digital solutions that assist farmer decision-making with a view to optimize product selection, and maximize yield and profitability. The Crop Protection segment offers products that protect against weeds, insects and other pests, and diseases, as well as enhances crop health above and below ground through nitrogen management and seed-applied technologies. This segment provides herbicides, insecticides, nitrogen stabilizers, and pasture and range management herbicides. It serves agricultural input industry. The company operates in the United States, Canada, Latin America, the Asia Pacific, Europe, the Middle East, and Africa. Corteva, Inc. was incorporated in 2018 and is headquartered in Indianapolis, Indiana.',
        fullTimeEmployees=21000,
        city='Indianapolis',
        state='IN',
        trailingPE=24.645779,
        dividendYield=0.0104,
        averageVolume=4677580,
        regularMarketOpen=54.89,
        volume=4367654,
        fiftyTwoWeekHigh=64.03,
        fiftyTwoWeekLow=40.6,
        recommendationKey='buy',
        industry='Agricultural Inputs'
    )
    db.session.add(CTVA)

    COST = Stock(
        name='Costco Wholesale Corporation',
        ticker='COST',
        marketCap=207796666368,
        dayHigh=487.24,
        dayLow=467.89,
        currentPrice=468.61,
        longBusinessSummary='Costco Wholesale Corporation, together with its subsidiaries, engages in the operation of membership warehouses in the United States, Puerto Rico, Canada, the United Kingdom, Mexico, Japan, Korea, Australia, Spain, France, Iceland, China, and Taiwan. It offers branded and private-label products in a range of merchandise categories. The company offers sundries, dry groceries, candies, coolers, freezers, liquor, and tobacco and deli products; appliances, electronics, health and beauty aids, hardware, garden and patio products, sporting goods, tires, toys and seasonal products, office supplies, automotive care products, postages, tickets, apparel, small appliances, furniture, domestics, housewares, special order kiosks, and jewelry; and meat, produce, service deli, and bakery products. It also operates pharmacies, opticals, food courts, hearing-aid centers, and tire installation centers, as well as 636 gas stations; and offers business delivery, travel, same-day grocery, and various other services online in various countries. As of August 29, 2021, the company operated 815 membership warehouses, including 564 in the United States and Puerto Rico, 105 in Canada, 39 in Mexico, 30 in Japan, 29 in the United Kingdom, 16 in South Korea, 14 in Taiwan, 12 in Australia, 3 in Spain, 1 in Iceland, 1 in France, and 1 in China. It also operates e-commerce websites in the United States, Canada, the United Kingdom, Mexico, South Korea, Taiwan, Japan, and Australia. The company was formerly known as Costco Companies, Inc. and changed its name to Costco Wholesale Corporation in August 1999. Costco Wholesale Corporation was founded in 1976 and is based in Issaquah, Washington.',
        fullTimeEmployees=288000,
        city='Issaquah',
        state='WA',
        trailingPE=40.293205,
        dividendYield=0.0072000003,
        averageVolume=2992241,
        regularMarketOpen=483.5,
        volume=1684230,
        fiftyTwoWeekHigh=612.27,
        fiftyTwoWeekLow=393.88,
        recommendationKey='buy',
        industry='Discount Stores'
    )
    db.session.add(COST)

    CTRA = Stock(
        name='Coterra Energy Inc.',
        ticker='CTRA',
        marketCap=22527975424,
        dayHigh=27.829,
        dayLow=27.02,
        currentPrice=27.69,
        longBusinessSummary='Coterra Energy Inc., an independent oil and gas company, engages in the development, exploration and production of oil, natural gas, and natural gas liquids in the United States. It primarily focuses on the Marcellus Shale with approximately 177,000 net acres in the dry gas window of the play located in Susquehanna County, Pennsylvania. The company also holds Permian Basin properties with approximately 306,000 net acres; and Anadarko Basin properties located in Oklahoma with approximately 182,000 net acres. In addition, it operates natural gas and saltwater disposal gathering systems in Texas. The company sells its natural gas to industrial customers, local distribution companies, oil and gas marketers, major energy companies, pipeline companies, and power generation facilities. As of December 31, 2021, it had proved reserves of approximately 2,892,582 thousand barrels of oil equivalent, which include 189,429 thousand barrels of oil and other liquid hydrocarbons, 14,895 billion cubic feet of natural gas, and 220,615 thousand barrels of natural gas liquids. The company was incorporated in 1989 and is headquartered in Houston, Texas.',
        fullTimeEmployees=936,
        city='Houston',
        state='TX',
        trailingPE=31.501707,
        dividendYield=0.0201,
        averageVolume=11053448,
        regularMarketOpen=27.43,
        volume=10134293,
        fiftyTwoWeekHigh=36.55,
        fiftyTwoWeekLow=14.28,
        recommendationKey='buy',
        industry='Oil & Gas E&P'
    )
    db.session.add(CTRA)

    CCI = Stock(
        name='Crown Castle International Corp.',
        ticker='CCI',
        marketCap=72865103872,
        dayHigh=174.15,
        dayLow=167.875,
        currentPrice=168.59,
        longBusinessSummary='Crown Castle owns, operates and leases more than 40,000 cell towers and approximately 80,000 route miles of fiber supporting small cells and fiber solutions across every major U.S. market. This nationwide portfolio of communications infrastructure connects cities and communities to essential data, technology and wireless service - bringing information, ideas and innovations to the people and businesses that need them. For more information on Crown Castle, please visit www.crowncastle.com.',
        fullTimeEmployees=5000,
        city='Houston',
        state='TX',
        trailingPE=58.7217,
        dividendYield=0.033299997,
        averageVolume=1726816,
        regularMarketOpen=174.01,
        volume=1734364,
        fiftyTwoWeekHigh=209.87,
        fiftyTwoWeekLow=153.7,
        recommendationKey='buy',
        industry='REIT—Specialty'
    )
    db.session.add(CCI)

    CSX = Stock(
        name='CSX Corporation',
        ticker='CSX',
        marketCap=64631934976,
        dayHigh=30.1376,
        dayLow=29.08,
        currentPrice=29.14,
        longBusinessSummary='CSX Corporation, together with its subsidiaries, provides rail-based freight transportation services. The company offers rail services; and transportation of intermodal containers and trailers, as well as other transportation services, such as rail-to-truck transfers and bulk commodity operations. It transports chemicals, agricultural and food products, automotive, minerals, forest products, fertilizers, and metals and equipment; and coal, coke, and iron ore to electricity-generating power plants, steel manufacturers, and industrial plants, as well as exports coal to deep-water port facilities. The company also offers intermodal transportation services through a network of approximately 30 terminals transporting manufactured consumer goods in containers; and drayage services, including the pickup and delivery of intermodal shipments. It serves the automotive industry with distribution centers and storage locations, as well as connects non-rail served customers through transferring products, such as plastics and ethanol from rail to trucks. The company operates approximately 19,500 route mile rail network, which serves various population centers in 23 states east of the Mississippi River, the District of Columbia, and the Canadian provinces of Ontario and Quebec, as well as owns and leases approximately 3,500 locomotives. It also serves production and distribution facilities through track connections. CSX Corporation was incorporated in 1978 and is headquartered in Jacksonville, Florida.',
        fullTimeEmployees=21000,
        city='Jacksonville',
        state='FL',
        trailingPE=18.338577,
        dividendYield=0.012,
        averageVolume=16439082,
        regularMarketOpen=29.82,
        volume=12107095,
        fiftyTwoWeekHigh=38.63,
        fiftyTwoWeekLow=28.44,
        recommendationKey='buy',
        industry='Railroads'
    )
    db.session.add(CSX)

    CMI = Stock(
        name='Cummins Inc.',
        ticker='CMI',
        marketCap=28042854400,
        dayHigh=201.25,
        dayLow=195.5,
        currentPrice=196.06,
        longBusinessSummary='Cummins Inc. designs, manufactures, distributes, and services diesel and natural gas engines, electric and hybrid powertrains, and related components worldwide. It operates through five segments: Engine, Distribution, Components, Power Systems, and New Power. The company offers diesel and natural gas-powered engines under the Cummins and other customer brands for the heavy and medium-duty truck, bus, recreational vehicle, light-duty automotive, construction, mining, marine, rail, oil and gas, defense, and agricultural markets; and offers new parts and services, as well as remanufactured parts and engines. It also provides power generation systems, high-horsepower engines, heavy and medium duty engines, application engineering services, custom-designed assemblies, retail and wholesale aftermarket parts, and in-shop and field-based repair services. In addition, the company offers emission solutions; turbochargers; air and fuel filters, fuel water separators, lube and hydraulic filters, coolants, fuel additives, and other filtration systems; and electronic control modules, sensors, and supporting software, as well as new, replacement, and remanufactured fuel systems. Further, it provides automated transmissions; standby and prime power generators, controls, paralleling systems, and transfer switches, as well as A/C generator/alternator products under the Stamford and AVK brands; and electrified power systems with components and subsystems, including battery, fuel cell, and hydrogen production technologies. Additionally, it offers filtration, aftertreatment, controls systems, air handling systems, automated transmissions, electric power generation systems, and batteries. The company sells its products to original equipment manufacturers, distributors, dealers, and other customers. The company was formerly known as Cummins Engine Company and changed its name to Cummins Inc. in 2001. Cummins Inc. was founded in 1919 and is headquartered in Columbus, Indiana.',
        fullTimeEmployees=59900,
        city='Columbus',
        state='IN',
        trailingPE=12.889356,
        dividendYield=0.028800001,
        averageVolume=981861,
        regularMarketOpen=197.33,
        volume=692919,
        fiftyTwoWeekHigh=247.48,
        fiftyTwoWeekLow=184.28,
        recommendationKey='buy',
        industry='Specialty Industrial Machinery'
    )
    db.session.add(CMI)

    CVS = Stock(
        name='CVS Health Corporation',
        ticker='CVS',
        marketCap=123029594112,
        dayHigh=95.95,
        dayLow=92.9439,
        currentPrice=93.2,
        longBusinessSummary="CVS Health Corporation provides health services in the United States. The company's Health Care Benefits segment offers traditional, voluntary, and consumer-directed health insurance products and related services. It serves employer groups, individuals, college students, part-time and hourly workers, health plans, health care providers, governmental units, government-sponsored plans, labor groups, and expatriates. Its Pharmacy Services segment offers pharmacy benefit management solutions, including plan design and administration, formulary management, retail pharmacy network management, mail order pharmacy, specialty pharmacy and infusion, clinical, and disease and medical spend management services. It serves employers, insurance companies, unions, government employee groups, health plans, prescription drug plans, Medicaid managed care plans, plans offered on public health insurance and private health insurance exchanges, other sponsors of health benefit plans, and individuals. This segment operates retail specialty pharmacy stores; and specialty mail-order, mail-order dispensing, and compounding pharmacies, as well as branches for infusion and enteral nutrition services. The company's Retail/LTC segment sells prescription and over-the-counter drugs, consumer health and beauty products, and personal care products; and provides health care services through its MinuteClinic walk-in medical clinics. This segment also distributes prescription drugs; and provides related pharmacy consulting and other ancillary services to care facilities and other care settings. As of December 31, 2021, it operated approximately 9,900 retail locations and 1,200 MinuteClinic locations, as well as online retail pharmacy websites, LTC pharmacies, and onsite pharmacies. The company was formerly known as CVS Caremark Corporation and changed its name to CVS Health Corporation in September 2014. CVS Health Corporation was founded in 1963 and is headquartered in Woonsocket, Rhode Island.",
        fullTimeEmployees=216000,
        city='Woonsocket',
        state='RI',
        trailingPE=16.268108,
        dividendYield=0.0226,
        averageVolume=5591516,
        regularMarketOpen=94.93,
        volume=4598249,
        fiftyTwoWeekHigh=111.25,
        fiftyTwoWeekLow=79.33,
        recommendationKey='buy',
        industry='Healthcare Plans'
    )
    db.session.add(CVS)

    DHI = Stock(
        name='D.R. Horton, Inc.',
        ticker='DHI',
        marketCap=23465203712,
        dayHigh=68.66,
        dayLow=65.85,
        currentPrice=65.88,
        longBusinessSummary="D.R. Horton, Inc. operates as a homebuilding company in East, North, Southeast, South Central, Southwest, and Northwest regions in the United States. It engages in the acquisition and development of land; and construction and sale of residential homes in 31 states and 98 markets under the names of D.R. Horton, America's Builder, Express Homes, Emerald Homes, and Freedom Homes. The company constructs and sells single-family detached homes; and attached homes, such as town homes, duplexes, and triplexes. It also provides mortgage financing services; and title insurance policies, and examination and closing services, as well as engages in the residential lot development business. In addition, the company develops, constructs, owns, leases, and sells multi-family and single-family rental properties; owns non-residential real estate, including ranch land and improvements; and owns and operates energy related assets. It primarily serves homebuyers. D.R. Horton, Inc. was founded in 1978 and is headquartered in Arlington, Texas.",
        fullTimeEmployees=11788,
        city='Arlington',
        state='TX',
        trailingPE=5.7738824,
        dividendYield=0.013099999,
        averageVolume=4106406,
        regularMarketOpen=68.17,
        volume=3083802,
        fiftyTwoWeekHigh=110.45,
        fiftyTwoWeekLow=59.25,
        recommendationKey='buy',
        industry='Residential Construction'
    )
    db.session.add(DHI)

    DHR = Stock(
        name='Danaher Corporation',
        ticker='DHR',
        marketCap=179987660800,
        dayHigh=258.63,
        dayLow=251.16,
        currentPrice=251.88,
        longBusinessSummary="Danaher Corporation designs, manufactures, and markets professional, medical, industrial, and commercial products and services worldwide. The company operates through three segments: Life Sciences, Diagnostics, and Environmental & Applied Solutions. The Life Sciences segment provides mass spectrometers; flow cytometry, genomics, lab automation, centrifugation, particle counting and characterization; microscopes; genomics consumables; and Gene and Cell Therapy. This segment also offers bioprocess technologies, consumables, and services; and filtration, separation, and purification technologies to the pharmaceutical and biopharmaceutical, food and beverage, medical, and life sciences companies, as well as universities, medical schools and research institutions, and various industrial manufacturers. The Diagnostics segment provides chemistry, immunoassay, microbiology, and automation systems, as well as hematology, molecular, acute care, and pathology diagnostics products. This segment offers clinical instruments, reagents, consumables, software, and services for hospitals, physicians' offices, reference laboratories, and other critical care settings. The Environmental & Applied Solutions segment offers instrumentation, consumables, software, services, and disinfection systems to analyze, treat, and manage ultra-pure, potable, industrial, waste, ground, source, and ocean water in residential, commercial, industrial, and natural resource applications. This segment also provides instruments, software, services, and consumables for various color and appearance management, packaging design and quality management, packaging converting, printing, marking, coding, and traceability applications for consumer, pharmaceutical, and industrial products. The company was formerly known as Diversified Mortgage Investors, Inc. and changed its name to Danaher Corporation in 1984. Danaher Corporation was founded in 1969 and is headquartered in Washington, the District of Columbia.",
        fullTimeEmployees=78000,
        city='Washington',
        state='DC',
        trailingPE=31.956356,
        dividendYield=0.004,
        averageVolume=2795448,
        regularMarketOpen=256.36,
        volume=1651647,
        fiftyTwoWeekHigh=333.96,
        fiftyTwoWeekLow=233.71,
        recommendationKey='buy',
        industry='Diagnostics & Research'
    )
    db.session.add(DHR)

    DRI = Stock(
        name='Darden Restaurants, Inc.',
        ticker='DRI',
        marketCap=14938253312,
        dayHigh=123.44,
        dayLow=114.93,
        currentPrice=115.1,
        longBusinessSummary="Darden Restaurants, Inc., through its subsidiaries, owns and operates full-service restaurants in the United States and Canada. As of May 30, 2021, it owned and operated 1,834 restaurants, which included 875 under the Olive Garden, 533 under the LongHorn Steakhouse, 170 under the Cheddar's Scratch Kitchen, 81 under the Yard House, 63 under The Capital Grille, 44 under the Seasons 52, 42 under the Bahama Breeze, and 26 under the Eddie V's Prime Seafood brands. The company was founded in 1968 and is based in Orlando, Florida.",
        fullTimeEmployees=156883,
        city='Orlando',
        state='FL',
        trailingPE=16.45461,
        dividendYield=0.0344,
        averageVolume=1231369,
        regularMarketOpen=122.02,
        volume=1473850,
        fiftyTwoWeekHigh=164.28,
        fiftyTwoWeekLow=110.96,
        recommendationKey='buy',
        industry='Restaurants'
    )
    db.session.add(DRI)

    DVA = Stock(
        name='DaVita Inc.',
        ticker='DVA',
        marketCap=8284470272,
        dayHigh=83.27,
        dayLow=80.92,
        currentPrice=81.3,
        longBusinessSummary='DaVita Inc. provides kidney dialysis services for patients suffering from chronic kidney failure. The company operates kidney dialysis centers and provides related lab services in outpatient dialysis centers. It also provides outpatient, hospital inpatient, and home-based hemodialysis services; owns clinical laboratories that provide routine laboratory tests for dialysis and other physician-prescribed laboratory tests for ESRD patients; and management and administrative services to outpatient dialysis centers. In addition, the company provides disease management services to 16,000 patients in risk-based integrated care arrangements and 7,000 patients in other integrated care arrangements; vascular access services; clinical research programs; physician services; and comprehensive kidney care services. As of December 31, 2021, it provided dialysis and administrative services in the United States through a network of 2,815 outpatient dialysis centers serving approximately 203,100 patients; and operated 339 outpatient dialysis centers located in 10 countries outside of the United States serving approximately 39,900 patients. Further, the company provides acute inpatient dialysis services in approximately 850 hospitals and related laboratory services in the United States. The company was formerly known as DaVita HealthCare Partners Inc. and changed its name to DaVita Inc. in September 2016. DaVita Inc. was incorporated in 1994 and is headquartered in Denver, Colorado.',
        fullTimeEmployees=69000,
        city='Denver',
        state='CO',
        trailingPE=9.494337,
        dividendYield=None,
        averageVolume=924764,
        regularMarketOpen=81.5,
        volume=1293518,
        fiftyTwoWeekHigh=136.48,
        fiftyTwoWeekLow=74.97,
        recommendationKey='hold',
        industry='Medical Care Facilities'
    )
    db.session.add(DVA)

    DE = Stock(
        name='Deere & Company',
        ticker='DE',
        marketCap=95037947904,
        dayHigh=320.18,
        dayLow=308.48,
        currentPrice=309.16,
        longBusinessSummary='Deere & Company manufactures and distributes various equipment worldwide. The company operates through four segments: Production and Precision Agriculture, Small Agriculture and Turf, Construction and Forestry, and Financial Services. The Production and Precision Agriculture segment provides mid-size tractors, combines, cotton pickers and strippers, sugarcane harvesters, harvesting front-end equipment, sugarcane loaders, pull-behind scrapers, and tillage and seeding equipment, as well as application equipment, including sprayers and nutrient management, and soil preparation machinery for grain growers. The Small Agriculture and Turf segment offers utility tractors, and related loaders and attachments; turf and utility equipment, including riding lawn equipment, commercial mowing equipment, golf course equipment, and utility vehicles, as well as implements for mowing, tilling, snow and debris handling, aerating, residential, commercial, golf, and sports turf care applications; other outdoor power products; and hay and forage equipment. This segment also resells products from other manufacturers. It serves dairy and livestock producers, crop producers, and turf and utility customers. The Construction and Forestry segment provides a range of backhoe loaders, crawler dozers and loaders, four-wheel-drive loaders, excavators, motor graders, articulated dump trucks, landscape and skid-steer loaders, milling machines, pavers, compactors, rollers, crushers, screens, asphalt plants, log skidders, log feller bunchers, log loaders and forwarders, log harvesters, and attachments; and roadbuilding equipment. The Financial Services segment finances sales and leases agriculture and turf, and construction and forestry equipment. It also offers wholesale financing to dealers of the foregoing equipment; and extended equipment warranties, as well as finances retail revolving charge accounts. Deere & Company was founded in 1837 and is headquartered in Moline, Illinois.',
        fullTimeEmployees=75550,
        city='Moline',
        state='IL',
        trailingPE=16.280148,
        dividendYield=0.0115,
        averageVolume=1874974,
        regularMarketOpen=318.39,
        volume=1761848,
        fiftyTwoWeekHigh=446.76,
        fiftyTwoWeekLow=295.59,
        recommendationKey='buy',
        industry='Farm & Heavy Construction Machinery'
    )
    db.session.add(DE)

    XRAY = Stock(
        name='DENTSPLY SIRONA Inc.',
        ticker='XRAY',
        marketCap=7832689664,
        dayHigh=37.28,
        dayLow=35.815,
        currentPrice=35.83,
        longBusinessSummary='DENTSPLY SIRONA Inc. designs, develops, manufactures, distributes, and sells various dental products and technologies for professional dental market worldwide. It offers dental equipment, including treatment centers, imaging equipment, motorized dental handpieces, and other instruments; imaging equipment; treatment centers comprising basic dentist chairs, sophisticated chair-based units with integrated diagnostic, hygiene and ergonomic functionalities, and specialist centers; and lab equipment, such as amalgamators, mixing machines, and porcelain furnaces. The company also provides dental CAD/CAM products, digital impressions intraoral scanners, mills, and services; and orthodontic products, including high frequency vibration technology device under the name VPro, dentist-directed clear aligner solutions under the name SureSmile, and direct-to-consumer clear aligner solutions under the name Byte; dental implant products, bone regenerative and restorative solutions, and educational programs; and urology catheters and other healthcare-related consumable products. In addition, it offers endodontic products comprising endodontic instruments and materials, drills, filers, sealers, irrigation needles, and other tools or single-use solutions; restorative products that include dental prosthetics, such as artificial teeth, dental ceramics, digital dentures, precious metal dental alloys, and crown and bridge porcelain products; small equipment products comprise intraoral curing light systems, dental diagnostic systems, and ultrasonic scalers and polishers; and dental supplies, including dental anesthetics, prophylaxis paste, dental sealants, impression materials, teeth whiteners, and topical fluoride. The company was formerly known as DENTSPLY International Inc. and changed its name to DENTSPLY SIRONA Inc. in February 2016. DENTSPLY SIRONA Inc. was founded in 1899 and is headquartered in Charlotte, North Carolina.',
        fullTimeEmployees=15000,
        city='Charlotte',
        state='NC',
        trailingPE=18.838066,
        dividendYield=0.013099999,
        averageVolume=2544264,
        regularMarketOpen=36.97,
        volume=1216916,
        fiftyTwoWeekHigh=66.98,
        fiftyTwoWeekLow=33.78,
        recommendationKey='hold',
        industry='Medical Instruments & Supplies'
    )
    db.session.add(XRAY)

    DVN = Stock(
        name='Devon Energy Corporation',
        ticker='DVN',
        marketCap=40254418944,
        dayHigh=60.49,
        dayLow=58.0534,
        currentPrice=59.46,
        longBusinessSummary='Devon Energy Corporation, an independent energy company, primarily engages in the exploration, development, and production of oil, natural gas, and natural gas liquids in the United States. It operates approximately 5,134 gross wells. Devon Energy Corporation was incorporated in 1971 and is headquartered in Oklahoma City, Oklahoma.',
        fullTimeEmployees=1600,
        city='Oklahoma City',
        state='OK',
        trailingPE=29.523336,
        dividendYield=0.0739,
        averageVolume=12138690,
        regularMarketOpen=59.18,
        volume=18388029,
        fiftyTwoWeekHigh=79.4,
        fiftyTwoWeekLow=24.05,
        recommendationKey='buy',
        industry='Oil & Gas E&P'
    )
    db.session.add(DVN)

    DXCM = Stock(
        name='DexCom, Inc.',
        ticker='DXCM',
        marketCap=7240073216,
        dayHigh=78.69,
        dayLow=74.48,
        currentPrice=74.7,
        longBusinessSummary="DexCom, Inc., a medical device company, focuses on the design, development, and commercialization of continuous glucose monitoring (CGM) systems in the United States and internationally. The company provides its systems for use by people with diabetes, as well as for use by healthcare providers. Its products include DexCom G6, an integrated CGM system for diabetes management; Dexcom Real-Time API, which enables invited third-party developers to integrate real-time CGM data into their digital health applications and devices; Dexcom ONE, that is designed to replace finger stick blood glucose testing for diabetes treatment decisions; and Dexcom Share, a remote monitoring system. The company's products candidature comprises Dexcom G7, a next generation G7 CGM system. DexCom, Inc. has a collaboration and license agreement with Verily Life Sciences LLC and Verily Ireland Limited to develop blood-based or interstitial glucose monitoring products. The company markets its products directly to endocrinologists, physicians, and diabetes educators. DexCom, Inc. was incorporated in 1999 and is headquartered in San Diego, California.",
        fullTimeEmployees=6300,
        city='San Diego',
        state='CA',
        trailingPE=14.089023,
        dividendYield=None,
        averageVolume=3683011,
        regularMarketOpen=77.15,
        volume=2226136,
        fiftyTwoWeekHigh=164.8625,
        fiftyTwoWeekLow=66.8925,
        recommendationKey='buy',
        industry='Medical Devices'
    )
    db.session.add(DXCM)

    FANG = Stock(
        name='Diamondback Energy, Inc.',
        ticker='FANG',
        marketCap=23516516352,
        dayHigh=131.43,
        dayLow=125.805,
        currentPrice=129.8,
        longBusinessSummary="Diamondback Energy, Inc., an independent oil and natural gas company, focuses on the acquisition, development, exploration, and exploitation of unconventional and onshore oil and natural gas reserves in the Permian Basin in West Texas. It focuses on the development of the Spraberry and Wolfcamp formations of the Midland basin; and the Wolfcamp and Bone Spring formations of the Delaware basin, which are part of the Permian Basin in West Texas and New Mexico. As of December 31, 2021, the company's total acreage position was approximately 524,700 gross acres in the Permian Basin; and estimated proved oil and natural gas reserves were 1,788,991 thousand barrels of crude oil equivalent. It also held working interests in 5,289 gross producing wells, as well as royalty interests in 6,455 additional wells. In addition, the company owns mineral interests approximately 930,871 gross acres and 27,027 net royalty acres in the Permian Basin and Eagle Ford Shale; and owns, operates, develops, and acquires midstream infrastructure assets, including 866 miles of crude oil gathering pipelines, natural gas gathering pipelines, and an integrated water system in the Midland and Delaware Basins of the Permian Basin. Diamondback Energy, Inc. was founded in 2007 and is headquartered in Midland, Texas.",
        fullTimeEmployees=870,
        city='Midland',
        state='TX',
        trailingPE=50.683327,
        dividendYield=0.022,
        averageVolume=2862458,
        regularMarketOpen=128.745,
        volume=3335725,
        fiftyTwoWeekHigh=162.24,
        fiftyTwoWeekLow=65.93,
        recommendationKey='buy',
        industry='Oil & Gas E&P'
    )
    db.session.add(FANG)

    DLR = Stock(
        name='Digital Realty Trust, Inc.',
        ticker='DLR',
        marketCap=38186377216,
        dayHigh=138.11,
        dayLow=134.16,
        currentPrice=134.56,
        longBusinessSummary="Digital Realty supports the world's leading enterprises and service providers by delivering the full spectrum of data center, colocation and interconnection solutions. PlatformDIGITALR, the company's global data center platform, provides customers a trusted foundation and proven Pervasive Datacenter Architecture PDxTM solution methodology for scaling digital business and efficiently managing data gravity challenges. Digital Realty's global data center footprint gives customers access to the connected communities that matter to them with more than 284 facilities in 48 metros across 23 countries on six continents.",
        fullTimeEmployees=3030,
        city='Austin',
        state='TX',
        trailingPE=56.752422,
        dividendYield=0.0372,
        averageVolume=1512782,
        regularMarketOpen=137.49,
        volume=978481,
        fiftyTwoWeekHigh=178.22,
        fiftyTwoWeekLow=124.11,
        recommendationKey='buy',
        industry='REIT—Office'
    )
    db.session.add(DLR)

    DFS = Stock(
        name='Discover Financial Services',
        ticker='DFS',
        marketCap=28519225344,
        dayHigh=101.41,
        dayLow=96.89,
        currentPrice=97.31,
        longBusinessSummary='Discover Financial Services, through its subsidiaries, provides digital banking products and services, and payment services in the United States. It operates in two segments, Digital Banking and Payment Services. The Digital Banking segment offers Discover-branded credit cards to individuals; private student loans, personal loans, home loans, and other consumer lending; and direct-to-consumer deposit products comprising savings accounts, certificates of deposit, money market accounts, IRA certificates of deposit, IRA savings accounts and checking accounts, and sweep accounts. The Payment Services segment operates the PULSE, an automated teller machine, debit, and electronic funds transfer network; and Diners Club International, a payments network that issues Diners Club branded charge cards and/or provides card acceptance services, as well as offers payment transaction processing and settlement services. The company was incorporated in 1960 and is based in Riverwoods, Illinois.',
        fullTimeEmployees=16700,
        city='Riverwoods',
        state='IL',
        trailingPE=5.8185835,
        dividendYield=0.0229,
        averageVolume=1853200,
        regularMarketOpen=100.11,
        volume=1625289,
        fiftyTwoWeekHigh=135.69,
        fiftyTwoWeekLow=88.02,
        recommendationKey='buy',
        industry='Credit Services'
    )
    db.session.add(DFS)

    DISH = Stock(
        name='DISH Network Corporation',
        ticker='DISH',
        marketCap=9587179520,
        dayHigh=19.27,
        dayLow=18.0791,
        currentPrice=18.13,
        longBusinessSummary='DISH Network Corporation, together with its subsidiaries, provides pay-TV services in the United States. The company operates in two segments, Pay-TV and Wireless. It offers video services under the DISH TV brand; and programming packages that include programming through national broadcast networks, local broadcast networks, and national and regional cable networks, as well as regional and specialty sports channels, premium movie channels, and Latino and international programming packages. The company also provides access to movies and television shows through TV or Internet-connected devices; and dishanywhere.com and mobile applications on Internet-connected devices to view authorized content, search program listings, and remotely control certain features of their DVRs. In addition, it offers Sling TV services, including Sling domestic, Sling International, Sling Latino, Sling Orange, and Sling Blue services that require an Internet connection and are available on streaming-capable devices, such as streaming media devices, TVs, tablets, computers, game consoles, and phones, as well as market SLING TV services to consumers who do not subscribe to traditional satellite and cable pay-TV services. Further, the company provides wireless subscribers consumer plans with no annual service contracts, as well as monthly service plans, including high-speed data and unlimited talk and text. As of December 31, 2021, it had 10.707 million pay-TV subscribers in the United States, including 8.221 million DISH TV subscribers and 2.486 million SLING TV subscribers. The company offers receiver systems and programming through direct sales channels, as well as independent third parties, such as small retailers, direct marketing groups, local and regional consumer electronics stores, retailers, and telecommunications companies. DISH Network Corporation was founded in 1980 and is headquartered in Englewood, Colorado.',
        fullTimeEmployees=14500,
        city='Englewood',
        state='CO',
        trailingPE=4.359221,
        dividendYield=None,
        averageVolume=4541282,
        regularMarketOpen=18.9,
        volume=2798536,
        fiftyTwoWeekHigh=46.31,
        fiftyTwoWeekLow=16.2,
        recommendationKey='buy',
        industry='Entertainment'
    )
    db.session.add(DISH)

    DIS = Stock(
        name='The Walt Disney Company',
        ticker='DIS',
        marketCap=174349942784,
        dayHigh=100.4,
        dayLow=95.78,
        currentPrice=95.92,
        longBusinessSummary='The Walt Disney Company, together with its subsidiaries, operates as an entertainment company worldwide. It operates through two segments, Disney Media and Entertainment Distribution; and Disney Parks, Experiences and Products. The company engages in the film and episodic television content production and distribution activities, as well as operates television broadcast networks under the ABC, Disney, ESPN, Freeform, FX, Fox, National Geographic, and Star brands; and studios that produces motion pictures under the Walt Disney Pictures, Twentieth Century Studios, Marvel, Lucasfilm, Pixar, and Searchlight Pictures banners. It also offers direct-to-consumer streaming services through Disney+, Disney+ Hotstar, ESPN+, Hulu, and Star+; sale/licensing of film and television content to third-party television and subscription video-on-demand services; theatrical, home entertainment, and music distribution services; staging and licensing of live entertainment events; and post-production services by Industrial Light & Magic and Skywalker Sound. In addition, the company operates theme parks and resorts, such as Walt Disney World Resort in Florida; Disneyland Resort in California; Disneyland Paris; Hong Kong Disneyland Resort; and Shanghai Disney Resort; Disney Cruise Line, Disney Vacation Club, National Geographic Expeditions, and Adventures by Disney as well as Aulani, a Disney resort and spa in Hawaii; licenses its intellectual property to a third party for the operations of the Tokyo Disney Resort; and provides consumer products, which include licensing of trade names, characters, visual, literary, and other IP for use on merchandise, published materials, and games. Further, it sells branded merchandise through retail, online, and wholesale businesses; and develops and publishes books, comic books, and magazines. The Walt Disney Company was founded in 1923 and is based in Burbank, California.',
        fullTimeEmployees=152000,
        city='Burbank',
        state='CA',
        trailingPE=87.678246,
        dividendYield=None,
        averageVolume=13448559,
        regularMarketOpen=99.74,
        volume=15169496,
        fiftyTwoWeekHigh=187.58,
        fiftyTwoWeekLow=92.01,
        recommendationKey='buy',
        industry='Entertainment'
    )
    db.session.add(DIS)

    DG = Stock(
        name='Dollar General Corporation',
        ticker='DG',
        marketCap=56438947840,
        dayHigh=250.89,
        dayLow=243.33,
        currentPrice=243.58,
        longBusinessSummary="Dollar General Corporation, a discount retailer, provides various merchandise products in the southern, southwestern, Midwestern, and eastern United States. It offers consumable products, including paper and cleaning products, such as paper towels, bath tissues, paper dinnerware, trash and storage bags, disinfectants, and laundry products; packaged food comprising cereals, pasta, canned soups, fruits and vegetables, condiments, spices, sugar, and flour; and perishables that include milk, eggs, bread, refrigerated and frozen food, beer, and wine. The company's consumable products also comprise snacks, such as candies, cookies, crackers, salty snacks, and carbonated beverages; health and beauty products, including over-the-counter medicines and personal care products, such as soaps, body washes, shampoos, cosmetics, and dental hygiene and foot care products; pet supplies and pet food; and tobacco products. In addition, it offers seasonal products comprising holiday items, toys, batteries, small electronics, greeting cards, stationery, prepaid phones and accessories, gardening supplies, hardware, and automotive and home office supplies; and home products that include kitchen supplies, cookware, small appliances, light bulbs, storage containers, frames, candles, craft supplies and kitchen, and bed and bath soft goods. Further, the company provides apparel, which comprise casual everyday apparel for infants, toddlers, girls, boys, women, and men, as well as socks, underwear, disposable diapers, shoes, and accessories. As of February 25, 2022, it operated 18,190 stores in 47 states in the United States. The company was formerly known as J.L. Turner & Son, Inc. and changed its name to Dollar General Corporation in 1968. Dollar General Corporation was founded in 1939 and is based in Goodlettsville, Tennessee.",
        fullTimeEmployees=163000,
        city='Goodlettsville',
        state='TN',
        trailingPE=23.808035,
        dividendYield=0.0095,
        averageVolume=2175450,
        regularMarketOpen=247.18,
        volume=1120893,
        fiftyTwoWeekHigh=262.21,
        fiftyTwoWeekLow=183.25,
        recommendationKey='buy',
        industry='Discount Stores'
    )
    db.session.add(DG)

    DLTR = Stock(
        name='Dollar Tree, Inc.',
        ticker='DLTR',
        marketCap=34546495488,
        dayHigh=160.24,
        dayLow=152.745,
        currentPrice=153.57,
        longBusinessSummary="Dollar Tree, Inc. operates discount variety retail stores. It operates in two segments, Dollar Tree and Family Dollar. The Dollar Tree segment offers merchandise at the fixed price of $ 1.25. It provides consumable merchandise, including candy and food, and health and personal care, as well as everyday consumables, such as household paper and chemicals, and frozen and refrigerated food; variety merchandise comprising toys, durable housewares, gifts, stationery, party goods, greeting cards, softlines, arts and crafts supplies, and other items; and seasonal goods that include Christmas, Easter, Halloween, and Valentine's Day merchandise. As of January 29, 2022, this segment operated 8,061 stores under the Dollar Tree and Dollar Tree Canada brands, as well as 15 distribution centers in the United States and 2 distribution centers in Canada. The Family Dollar segment operates general merchandise retail discount stores that offer consumable merchandise, which comprise food and beverages, tobacco, health and personal care, household chemicals, paper products, hardware and automotive supplies, diapers, batteries, and pet food and supplies; and home products, including housewares, home décor, and giftware, as well as domestics, such as comforters, sheets, and towels. It also provides apparel and accessories merchandise comprising clothing, fashion accessories, and shoes; and seasonal and electronics merchandise that include Christmas, Easter, Halloween, and Valentine's Day merchandise, as well as personal electronics, which comprise pre-paid cellular phones and services, stationery and school supplies, and toys. As of January 29, 2022, this segment operated 8,016 stores under the Family Dollar brand; and 11 distribution centers. The company was founded in 1986 and is based in Chesapeake, Virginia.",
        fullTimeEmployees=61886,
        city='Chesapeake',
        state='VA',
        trailingPE=25.844835,
        dividendYield=None,
        averageVolume=2548466,
        regularMarketOpen=156.9,
        volume=1594685,
        fiftyTwoWeekHigh=177.19,
        fiftyTwoWeekLow=84.26,
        recommendationKey='buy',
        industry='Discount Stores'
    )
    db.session.add(DLTR)

    D = Stock(
        name='Dominion Energy, Inc.',
        ticker='D',
        marketCap=63602073600,
        dayHigh=79.38,
        dayLow=78.4,
        currentPrice=78.53,
        longBusinessSummary="Dominion Energy, Inc. produces and distributes energy. The company operates through four segments: Dominion Energy Virginia, Gas Distribution, Dominion Energy South Carolina, and Contracted Assets. The Dominion Energy Virginia segment generates, transmits, and distributes regulated electricity to residential, commercial, industrial, and governmental customers in Virginia and North Carolina. The Gas Distribution segment engages in the regulated natural gas gathering, storage, transportation, distribution, and sales activities, as well as distributes nonregulated renewable natural gas. This segment serves residential, commercial, and industrial customers. The Dominion Energy South Carolina segment generates, transmits, and distributes electricity and natural gas to residential, commercial, and industrial customers in South Carolina. The Contracted Assets segment is involved in the energy marketing and price risk activities. As of December 31, 2021, the company's portfolio of assets included approximately 30.2 gigawatt of electric generating capacity; 10,700 miles of electric transmission lines; 78,000 miles of electric distribution lines; and 95,700 miles of gas distribution mains and related service facilities. It serves approximately 7 million customers. The company sells electricity at wholesale prices to rural electric cooperatives and municipalities, as well as into wholesale electricity markets. The company was formerly known as Dominion Resources, Inc. and changed its name to Dominion Energy, Inc. in May 2017. Dominion Energy, Inc. was incorporated in 1983 and is headquartered in Richmond, Virginia.",
        fullTimeEmployees=17100,
        city='Richmond',
        state='VA',
        trailingPE=24.765059,
        dividendYield=0.0319,
        averageVolume=3524029,
        regularMarketOpen=78.85,
        volume=3149921,
        fiftyTwoWeekHigh=88.78,
        fiftyTwoWeekLow=70.37,
        recommendationKey='buy',
        industry='Utilities—Regulated Electric'
    )
    db.session.add(D)

    DPZ = Stock(
        name="Domino's Pizza, Inc.",
        ticker='DPZ',
        marketCap=14206332928,
        dayHigh=399.3761,
        dayLow=390.21,
        currentPrice=390.71,
        longBusinessSummary="Domino's Pizza, Inc., through its subsidiaries, operates as a pizza company in the United States and internationally. It operates through three segments: U.S. Stores, International Franchise, and Supply Chain. The company offers pizzas under the Domino's brand name through company-owned and franchised stores. It also provides oven-baked sandwiches, pasta, boneless chicken and chicken wings, bread and dips side items, desserts, and soft drink products. As of January 2, 2022, the company operated approximately 18,800 stores in 90 markets. Domino's Pizza, Inc. was founded in 1960 and is based in Ann Arbor, Michigan.",
        fullTimeEmployees=7400,
        city='Ann Arbor',
        state='MI',
        trailingPE=29.655407,
        dividendYield=0.0128999995,
        averageVolume=550409,
        regularMarketOpen=396.42,
        volume=449407,
        fiftyTwoWeekHigh=567.57,
        fiftyTwoWeekLow=321.15,
        recommendationKey='buy',
        industry='Restaurants'
    )
    db.session.add(DPZ)

    DOV = Stock(
        name='Dover Corporation',
        ticker='DOV',
        marketCap=17534492672,
        dayHigh=124.86,
        dayLow=121.51,
        currentPrice=121.78,
        longBusinessSummary='Dover Corporation provides equipment and components, consumable supplies, aftermarket parts, software and digital solutions, and support services worldwide. The Engineered Products segment provides various equipment, component, software, solution, and services that are used in aftermarket vehicle service, solid waste handling, industrial automation, aerospace and defense, industrial winch and hoist, and fluid dispensing end-market. This segment also offers manual and power clamp, rotary and linear mechanical indexer, conveyor, pick and place unit, glove port, and manipulator, as well as end-of-arm robotic gripper, slide, and end effector. Its Clean Energy & Fueling segment offers component, equipment, and software and service solution enabling safe transport of traditional and clean fuel, and other hazardous substance along with supply chain, as well as operation of convenience retail, retail fueling, and vehicle wash establishment. The Imaging and Identification segment provides precision marking and coding; packaging intelligence; product traceability equipment; brand protection; and digital textile printing equipment, as well as related consumable, software, and service to packaged and consumer good, pharmaceutical, industrial manufacturing, fashion and apparel, and other end-market. Its Pumps and Process Solutions segment manufactures specialty pump, connector, and flow meter, fluid connecting solution, plastics and polymer processing equipment, and engineered components for rotating and reciprocating machines. The Climate & Sustainability Technologies segment manufactures refrigeration system, refrigeration display case, commercial glass refrigerator and freezer door, and brazed plate heat exchanger for industrial heating and cooling, and residential climate control applications. It sells its products directly and through a network of distributors. The company was incorporated in 1947 and is headquartered in Downers Grove, Illinois.',
        fullTimeEmployees=25000,
        city='Downers Grove',
        state='IL',
        trailingPE=18.767145,
        dividendYield=0.0150999995,
        averageVolume=1013532,
        regularMarketOpen=124.55,
        volume=1038305,
        fiftyTwoWeekHigh=184.05,
        fiftyTwoWeekLow=117.17,
        recommendationKey='buy',
        industry='Specialty Industrial Machinery'
    )
    db.session.add(DOV)

    DOW = Stock(
        name='Dow Inc.',
        ticker='DOW',
        marketCap=38851923968,
        dayHigh=54.14,
        dayLow=52.37,
        currentPrice=52.53,
        longBusinessSummary='Dow Inc. provides various materials science solutions for packaging, infrastructure, mobility, and consumer applications in the United States, Canada, Europe, the Middle East, Africa, India, the Asia Pacific, and Latin America. It operates through Packaging & Specialty Plastics, Industrial Intermediates & Infrastructure, and Performance Materials & Coatings segments. The Packaging & Specialty Plastics segment provides ethylene, and propylene and aromatics products; and polyethylene, polyolefin elastomers, ethylene vinyl acetate, and ethylene propylene diene monomer rubbers. The Industrial Intermediates & Infrastructure segment offers ethylene oxides, propylene oxides, propylene glycol and polyether polyols, aromatic isocyanates and polyurethane systems, coatings, adhesives, sealants, elastomers, and composites. This segment also provides caustic soda, and ethylene dichloride and vinyl chloride monomers; and cellulose ethers, redispersible latex powders, and acrylic emulsions. The Performance Materials and Coatings segment provides architectural paints and coatings, and industrial coatings that are used in maintenance and protective industries, wood, metal packaging, traffic markings, thermal paper, and leather; performance silicones and specialty materials; and silicone feedstocks and intermediates. It also engages in property and casualty insurance, as well as reinsurance business. Dow Inc. was incorporated in 2018 and is headquartered in Midland, Michigan.',
        fullTimeEmployees=35700,
        city='Midland',
        state='MI',
        trailingPE=6.817651,
        dividendYield=0.0418,
        averageVolume=5788100,
        regularMarketOpen=52.8,
        volume=4973976,
        fiftyTwoWeekHigh=71.86,
        fiftyTwoWeekLow=50.42,
        recommendationKey='buy',
        industry='Chemicals'
    )
    db.session.add(DOW)

    DTE = Stock(
        name='DTE Energy Company',
        ticker='DTE',
        marketCap=24260433920,
        dayHigh=126.18,
        dayLow=124.6,
        currentPrice=125.23,
        longBusinessSummary="DTE Energy Company engages in the utility operations. The company's Electric segment generates, purchases, distributes, and sells electricity to approximately 2.3 million residential, commercial, and industrial customers in southeastern Michigan. It generates electricity through fossil-fuel, hydroelectric pumped storage, and nuclear plants, as well as wind and other renewable assets. This segment owns and operates approximately 698 distribution substations and 449,800 line transformers. The company's Gas segment purchases, stores, transports, distributes, and sells natural gas to approximately 1.3 million residential, commercial, and industrial customers throughout Michigan; and sells storage and transportation capacity. This segment has approximately 20,000 miles of distribution mains; 1,304,000 service pipelines; and 1,305,000 active meters, as well as owns approximately 2,000 miles of transmission pipelines. The company's Power and Industrial Projects segment offers metallurgical coke; pulverized coal and petroleum coke to the steel, pulp and paper, and other industries; and power, steam and chilled water production, and wastewater treatment services, as well as supplies compressed air to industrial customers. Its Energy Trading segment engages in power, natural gas, and environmental marketing and trading; structured transactions; and the optimization of contracted natural gas pipeline transportation and storage positions. The company was founded in 1903 and is headquartered in Detroit, Michigan.",
        fullTimeEmployees=10400,
        city='Detroit',
        state='MI',
        trailingPE=27.736435,
        dividendYield=0.0273,
        averageVolume=1052148,
        regularMarketOpen=125.11,
        volume=802347,
        fiftyTwoWeekHigh=140.23,
        fiftyTwoWeekLow=108.22,
        recommendationKey='buy',
        industry='Utilities—Regulated Electric'
    )
    db.session.add(DTE)

    DUK = Stock(
        name='Duke Energy Corporation',
        ticker='DUK',
        marketCap=81319550976,
        dayHigh=106.83,
        dayLow=105.36,
        currentPrice=105.7,
        longBusinessSummary='Duke Energy Corporation, together with its subsidiaries, operates as an energy company in the United States. It operates through three segments: Electric Utilities and Infrastructure, Gas Utilities and Infrastructure, and Commercial Renewables. The Electric Utilities and Infrastructure segment generates, transmits, distributes, and sells electricity in the Carolinas, Florida, and the Midwest; and uses coal, hydroelectric, natural gas, oil, renewable generation, and nuclear fuel to generate electricity. It also engages in the wholesale of electricity to municipalities, electric cooperative utilities, and load-serving entities. This segment serves approximately 8.2 million customers in 6 states in the Southeast and Midwest regions of the United States covering a service territory of approximately 91,000 square miles; and owns approximately 50,259 megawatts (MW) of generation capacity. The Gas Utilities and Infrastructure segment distributes natural gas to residential, commercial, industrial, and power generation natural gas customers; and owns, operates, and invests in pipeline transmission and natural gas storage facilities. It has approximately 1.6 million customers, including 1.1 million customers in North Carolina, South Carolina, and Tennessee, as well as 550,000 customers in southwestern Ohio and northern Kentucky. The Commercial Renewables segment acquires, owns, develops, builds, and operates wind and solar renewable generation projects, including nonregulated renewable energy and energy storage services to utilities, electric cooperatives, municipalities, and corporate customers. It has 23 wind, 178 solar, and 2 battery storage facilities, as well as 71 fuel cell locations with a capacity of 3,554 MW across 22 states. The company was formerly known as Duke Energy Holding Corp. and changed its name to Duke Energy Corporation in April 2005. The company was founded in 1904 and is headquartered in Charlotte, North Carolina.',
        fullTimeEmployees=27605,
        city='Charlotte',
        state='NC',
        trailingPE=27.033247,
        dividendYield=0.036,
        averageVolume=2925629,
        regularMarketOpen=105.76,
        volume=2131942,
        fiftyTwoWeekHigh=116.33,
        fiftyTwoWeekLow=95.48,
        recommendationKey='buy',
        industry='Utilities—Regulated Electric'
    )
    db.session.add(DUK)

    DRE = Stock(
        name='Duke Realty Corporation',
        ticker='DRE',
        marketCap=21175259136,
        dayHigh=57.71,
        dayLow=55.47,
        currentPrice=55.6,
        longBusinessSummary='Duke Realty Corporation owns and operates approximately 159 million rentable square feet of industrial assets in 20 major logistics markets. Duke Realty Corporation is publicly traded on the NYSE under the symbol DRE and is a member of the S&P 500 Index.',
        fullTimeEmployees=340,
        city='Indianapolis',
        state='IN',
        trailingPE=22.8243,
        dividendYield=0.0209,
        averageVolume=3304025,
        regularMarketOpen=56.56,
        volume=2884633,
        fiftyTwoWeekHigh=66.22,
        fiftyTwoWeekLow=47.03,
        recommendationKey='none',
        industry='REIT—Industrial'
    )
    db.session.add(DRE)

    DD = Stock(
        name='DuPont de Nemours, Inc.',
        ticker='DD',
        marketCap=29702903808,
        dayHigh=58.84,
        dayLow=57.09,
        currentPrice=57.33,
        longBusinessSummary='DuPont de Nemours, Inc. provides technology-based materials and solutions in the United States, Canada, the Asia Pacific, Latin America, Europe, the Middle East, and Africa. It operates through three segments: Electronics & Industrial, Mobility & Materials, and Water & Protection. The Electronics & Industrial segment supplies materials and printing systems to the advanced printing industry; and materials and solutions for the fabrication of semiconductors and integrated circuits addressing front-end and back-end of the manufacturing process. This segment also provides semiconductor and advanced packaging materials; dielectric and metallization solutions for chip packaging; and silicones for light emitting diode packaging and semiconductor applications; permanent and process chemistries for the fabrication of printed circuit boards to include laminates and substrates, electroless, and electrolytic metallization solutions, as well as patterning solutions, and materials and metallization processes for metal finishing, decorative, and industrial applications. In addition, it offers various materials to manufacture rigid and flexible displays for organic light emitting diode, and other display applications, as well as provides high performance parts, and specialty silicone elastomers, and lubricants. The Mobility & Materials segment provides engineering resins, silicone encapsulants, pastes, filaments, and advanced films to engineers and designers in the transportation, electronics, renewable energy, industrial, and consumer end-markets. The Water & Protection segment provides engineered products and integrated systems for worker safety, water purification and separation, transportation, energy, medical packaging and building materials. The company was formerly known as DowDuPont Inc. and changed its name to DuPont de Nemours, Inc. in June 2019. DuPont de Nemours, Inc. is headquartered in Wilmington, Delaware.',
        fullTimeEmployees=28000,
        city='Wilmington',
        state='DE',
        trailingPE=5.298032,
        dividendYield=0.020599999,
        averageVolume=3027120,
        regularMarketOpen=58.01,
        volume=2292816,
        fiftyTwoWeekHigh=85.16,
        fiftyTwoWeekLow=54.59,
        recommendationKey='buy',
        industry='Specialty Chemicals'
    )
    db.session.add(DD)

    DXC = Stock(
        name='DXC Technology Company',
        ticker='DXC',
        marketCap=7897603072,
        dayHigh=33.12,
        dayLow=31.19,
        currentPrice=31.31,
        longBusinessSummary="DXC Technology Company, together with its subsidiaries, provides information technology services and solutions primarily in North America, Europe, Asia, and Australia. It operates in two segments, Global Business Services (GBS) and Global Infrastructure Services (GIS). The GBS segment offers a portfolio of analytics services and extensive partner ecosystem that help its customers to gain rapid insights, automate operations, and accelerate their digital transformation journeys; and software engineering and solutions that enable businesses to run and manage their mission-critical functions, transform their operations, and develop new ways of doing business. It also uses various technologies and methods to accelerate the creation, modernization, delivery, and maintenance of secure applications allowing customers to innovate faster while reducing risk, time to market, and total cost of ownership. In addition, this segment offers business process services, which include integration and optimization of front and back office processes, and agile process automation. The GIS segment adapts legacy apps to cloud, migrate the right workloads, and securely manage their multi-cloud environments; and offers security solutions help predict attacks, proactively respond to threats, and ensure compliance, as well as to protect data, applications, and infrastructure. It also provides IT outsourcing services support infrastructure, applications, and workplace IT operations, including hardware, software, physical/virtual end-user devices, collaboration tools, and IT support services. In addition, this segment offers workplace and mobility services to fit its customer's employee, business, and IT needs from intelligent collaboration; and modern device management, digital support services, Internet of Things, and mobility services. The company has a strategic collaboration with Microsoft. DXC Technology Company was founded in 1959 and is headquartered in Tysons, Virginia.",
        fullTimeEmployees=134000,
        city='Tysons',
        state='VA',
        trailingPE=20.598684,
        dividendYield=None,
        averageVolume=1976914,
        regularMarketOpen=32.73,
        volume=897326,
        fiftyTwoWeekHigh=44.18,
        fiftyTwoWeekLow=27.28,
        recommendationKey='hold',
        industry='Information Technology Services'
    )
    db.session.add(DXC)

    EMN = Stock(
        name='Eastman Chemical Company',
        ticker='EMN',
        marketCap=12322770944,
        dayHigh=93.87,
        dayLow=91.05,
        currentPrice=91.66,
        longBusinessSummary="Eastman Chemical Company operates as a specialty materials company in the United States and internationally. The company's Additives & Functional Products segment offers hydrocarbon and rosin resins; organic acid-based solutions; amine derivative-based building blocks; metam-based soil fumigants, thiram and ziram based fungicides, and plant growth regulators; specialty coalescent, specialty and commodity solvents, paint additives, and specialty polymers; heat transfer and aviation fluids; insoluble sulfur and anti-degradant rubber additives; and performance resins. It serves transportation, personal care, wellness, food, feed, agriculture, building and construction, water treatment, energy, consumables, durables, and electronics markets. Its Advanced Materials segment provides copolyesters, cellulosic biopolymers, cellulose esters, polyvinyl butyral (PVB) sheets, and window and protective films, and aftermarket applied film products for value-added end uses in the transportation, durables, electronics, building and construction, medical and pharma, and consumables markets. The company's Chemical Intermediates segment offers methylamines and salts higher amines and solvents; Olefin and acetyl derivatives, ethylene, and commodity solvents; and primary non-phthalate and phthalate plasticizers, and niche non- phthalate plasticizers to the industrial chemicals and processing, building and construction, health and wellness, and agrochemicals. Its Fibers segment provides cellulose acetate tow, triacetin, cellulose acetate flake, acetic acid, and acetic anhydride for use in filtration media primarily cigarette filters; natural and solution dyed acetate yarns for use in consumables, and health and wellness markets; and wet-laid nonwoven media, specialty and engineered papers, and cellulose acetate fibers for transportation, industrial, agriculture and mining, and aerospace markets. Eastman Chemical Company was founded in 1920 and is headquartered in Kingsport, Tennessee.",
        fullTimeEmployees=14000,
        city='Kingsport',
        state='TN',
        trailingPE=24.600107,
        dividendYield=0.0295,
        averageVolume=1104154,
        regularMarketOpen=93.02,
        volume=1695091,
        fiftyTwoWeekHigh=129.48,
        fiftyTwoWeekLow=85.94,
        recommendationKey='buy',
        industry='Chemicals'
    )
    db.session.add(EMN)

    EBAY = Stock(
        name='eBay Inc.',
        ticker='EBAY',
        marketCap=26699069440,
        dayHigh=44.47,
        dayLow=42.61,
        currentPrice=42.65,
        longBusinessSummary="eBay Inc. operates marketplace platforms that connect buyers and sellers in the United States and internationally. The company's Marketplace platform includes its online marketplace at ebay.com and the eBay suite of mobile apps. Its platforms enable users to list, buy, sell, and pay for items through various online, mobile, and offline channels that include retailers, distributors, liquidators, import and export companies, auctioneers, catalog and mail-order companies, directories, search engines, commerce participants, shopping channels, and networks. The company was founded in 1995 and is headquartered in San Jose, California.",
        fullTimeEmployees=10800,
        city='San Jose',
        state='CA',
        trailingPE=2.3330233,
        dividendYield=0.0191,
        averageVolume=7315866,
        regularMarketOpen=43.4,
        volume=5112958,
        fiftyTwoWeekHigh=81.19,
        fiftyTwoWeekLow=40.52,
        recommendationKey='buy',
        industry='Internet Retail'
    )
    db.session.add(EBAY)


    ECL = Stock(
        name="Ecolab Inc.",
        ticker="ECL",
        marketCap=43790913536,
        dayHigh=158.605,
        dayLow=153.02,
        currentPrice=153.3,
        longBusinessSummary="Ecolab Inc. provides water, hygiene, and infection prevention solutions and services in the United States and internationally. The company operates through Global Industrial, Global Institutional & Specialty, and Global Healthcare & Life Sciences segments. The Global Industrial segment offers water treatment and process applications, and cleaning and sanitizing solutions to manufacturing, food and beverage processing, transportation, chemical, metals and mining, power generation, pulp and paper, commercial laundry, petroleum, refining, and petrochemical industries. The Global Institutional & Specialty segment provides specialized cleaning and sanitizing products to the foodservice, hospitality, lodging, government and education, and retail industries. Its Global Healthcare & Life Sciences segment offers specialized cleaning and sanitizing products to the healthcare, personal care, and pharmaceutical industries, such as infection prevention and surgical solutions, and end-to-end cleaning and contamination control solutions under the Ecolab, Microtek, and Anios brand names. The company's Other segment offers pest elimination services to detect, eliminate, and prevent pests, such as rodents and insects in restaurants, food and beverage processors, educational and healthcare facilities, hotels, quick service restaurant and grocery operations, and other institutional and commercial customers. This segment also provides colloidal silica for binding and polishing applications in semiconductor, catalyst, and aerospace component manufacturing, as well as chemical industries; and products and services that manage wash process through custom designed programs, premium products, dispensing equipment, water and energy management, and reduction, as well as real time data management. It sells its products through field sales and corporate account personnel, distributors, and dealers. The company was founded in 1923 and is headquartered in Saint Paul, Minnesota.",
        fullTimeEmployees=47000,
        city="Saint Paul",
        state="MN",
        trailingPE=39.91148,
        dividendYield=0.0137,
        averageVolume=1278303,
        regularMarketOpen=157.46,
        volume=846009,
        fiftyTwoWeekHigh=238.93,
        fiftyTwoWeekLow=143.82,
        recommendationKey="buy",
        industry="Specialty Chemicals"
    )
    db.session.add(ECL)

    EIX = Stock(
        name="Edison International",
        ticker="EIX",
        marketCap=23783067648,
        dayHigh=64.02,
        dayLow=62.3,
        currentPrice=62.39,
        longBusinessSummary="Edison International, through its subsidiaries, generates and distributes electric power. It delivers electricity to 15 million residential, commercial, industrial, public authorities, agricultural, and other customers across Southern, Central, and Coastal California. The company also provides energy solutions to commercial and industrial users. Its transmission facilities consist of lines ranging from 55 kV to 500 kV and substations; and distribution system consists of approximately 39,000 circuit-miles of overhead lines, approximately 31,000 circuit-miles of underground lines, and 800 substations. The company was founded in 1886 and is headquartered in Rosemead, California.",
        fullTimeEmployees=13003,
        city="Rosemead",
        state="CA",
        trailingPE=40.64495,
        dividendYield=0.0464,
        averageVolume=1878143,
        regularMarketOpen=63.66,
        volume=1638378,
        fiftyTwoWeekHigh=73.32,
        fiftyTwoWeekLow=54.14,
        recommendationKey="buy",
        industry="Utilities—Regulated Electric"
    )
    db.session.add(EIX)

    EW = Stock(
        name="Edwards Lifesciences Corporation",
        ticker="EW",
        marketCap=58898567168,
        dayHigh=98.22,
        dayLow=94.605,
        currentPrice=94.73,
        longBusinessSummary="Edwards Lifesciences Corporation provides products and technologies for structural heart disease, and critical care and surgical monitoring in the United States, Europe, Japan, and internationally. It offers transcatheter heart valve replacement products for the minimally invasive replacement of heart valves; and transcatheter heart valve repair and replacement products to treat mitral and tricuspid valve diseases. The company also provides the PASCAL and Cardioband transcatheter valve repair systems for minimally-invasive therapy. In addition, it offers surgical structural heart solutions, such as aortic surgical valve under the INSPIRIS name; KONECT RESILIA, a pre-assembled aortic tissue valved conduit for patients who require replacement of the valve, root, and ascending aorta; and HARPOON Beating Heart Mitral Valve Repair System for patients with degenerative mitral regurgitation. Further, the company provides critical care solutions, including advanced hemodynamic monitoring systems to measure a patient's heart function and fluid status in surgical and intensive care settings; and Acumen Hypotension Prediction Index software that alerts clinicians in advance of a patient developing dangerously low blood pressure. The company distributes its products through a direct sales force and independent distributors. Edwards Lifesciences Corporation was founded in 1958 and is headquartered in Irvine, California.",
        fullTimeEmployees=15700,
        city="Irvine",
        state="CA",
        trailingPE=38.98354,
        dividendYield=None,
        averageVolume=2964851,
        regularMarketOpen=97.27,
        volume=3701756,
        fiftyTwoWeekHigh=131.73,
        fiftyTwoWeekLow=85.58,
        recommendationKey="buy",
        industry="Medical Devices"
    )
    db.session.add(EW)

    EA = Stock(
        name="Electronic Arts Inc.",
        ticker="EA",
        marketCap=35080888320,
        dayHigh=126.57,
        dayLow=122.62,
        currentPrice=122.88,
        longBusinessSummary="Electronic Arts Inc. develops, markets, publishes, and distributes games, content, and services for game consoles, PCs, mobile phones, and tablets worldwide. It develops and publishes games and services across various genres, such as sports, racing, first-person shooter, action, role-playing, and simulation primarily under the Battlefield, The Sims, Apex Legends, Need for Speed, and license games from others, including FIFA, Madden NFL, UFC, and Star Wars brands. The company licenses its games to third parties to distribute and host its games. It markets and sells its games and services through digital distribution and retail channels, as well as directly to mass market retailers, specialty stores, and distribution arrangements. Electronic Arts Inc. was incorporated in 1982 and is headquartered in Redwood City, California.",
        fullTimeEmployees=12900,
        city="Redwood City",
        state="CA",
        trailingPE=45.51111,
        dividendYield=0.0062,
        averageVolume=2755100,
        regularMarketOpen=125.911,
        volume=3250519,
        fiftyTwoWeekHigh=147.76,
        fiftyTwoWeekLow=109.24,
        recommendationKey="buy",
        industry="Electronic Gaming & Multimedia"
    )
    db.session.add(EA)

    LLY = Stock(
        name="Eli Lilly and Company",
        ticker="LLY",
        marketCap=301789806592,
        dayHigh=329.065,
        dayLow=316.76,
        currentPrice=317.62,
        longBusinessSummary="Eli Lilly and Company discovers, develops, and markets human pharmaceuticals worldwide. It offers Basaglar, Humalog, Humalog Mix 75/25, Humalog U-100, Humalog U-200, Humalog Mix 50/50, insulin lispro, insulin lispro protamine, insulin lispro mix 75/25, Humulin, Humulin 70/30, Humulin N, Humulin R, and Humulin U-500 for diabetes; and Jardiance, Trajenta, and Trulicity for type 2 diabetes. The company provides Alimta for non-small cell lung cancer (NSCLC) and malignant pleural mesothelioma; Cyramza for metastatic gastric cancer, gastro-esophageal junction adenocarcinoma, metastatic NSCLC, metastatic colorectal cancer, and hepatocellular carcinoma; Erbitux for colorectal cancers, and various head and neck cancers; Retevmo for metastatic NSCLC, medullary thyroid cancer, and thyroid cancer; Tyvyt for relapsed or refractory classic Hodgkin's lymph and non-squamous NSCLC; and Verzenio for HR+, HER2- metastatic breast cancer, node positive, and early breast cancer. It offers Olumiant for rheumatoid arthritis; and Taltz for plaque psoriasis, psoriatic arthritis, ankylosing spondylitis, and non-radiographic axial spondylarthritis. The company offers Cymbalta for depressive disorder, diabetic peripheral neuropathic pain, generalized anxiety disorder, fibromyalgia, and chronic musculoskeletal pain; Emgality for migraine prevention and episodic cluster headache; and Zyprexa for schizophrenia, bipolar I disorder, and bipolar maintenance. Its Bamlanivimab and etesevimab, and Bebtelovimab for COVID-19; Cialis for erectile dysfunction and benign prostatic hyperplasia; and Forteo for osteoporosis. The company has collaborations with Incyte Corporation; Boehringer Ingelheim Pharmaceuticals, Inc.; AbCellera Biologics Inc.; Junshi Biosciences; Regor Therapeutics Group; Lycia Therapeutics, Inc.; Kumquat Biosciences Inc.; Entos Pharmaceuticals Inc.; and Foghorn Therapeutics Inc. Eli Lilly and Company was founded in 1876 and is headquartered in Indianapolis, Indiana.",
        fullTimeEmployees=35000,
        city="Indianapolis",
        state="IN",
        trailingPE=47.20868,
        dividendYield=0.013200001,
        averageVolume=3099670,
        regularMarketOpen=326.52,
        volume=2642418,
        fiftyTwoWeekHigh=330.85,
        fiftyTwoWeekLow=220.2,
        recommendationKey="buy",
        industry="Drug Manufacturers—General"
    )
    db.session.add(LLY)

    EMR = Stock(
        name="Emerson Electric Co.",
        ticker="EMR",
        marketCap=48422879232,
        dayHigh=84.11,
        dayLow=81.39,
        currentPrice=81.52,
        longBusinessSummary="Emerson Electric Co., a technology and engineering company, provides various solutions for customers in industrial, commercial, and residential markets in the Americas, Asia, the Middle East, Africa, and Europe. The company operates through Automation Solutions, and Commercial & Residential Solutions segments. The Automation Solutions segment offers measurement and analytical instrumentation, industrial valves and equipment, and process control software and systems. It serves oil and gas, refining, chemicals, power generation, life sciences, food and beverage, automotive, pulp and paper, metals and mining, and municipal water supplies markets. The Commercial & Residential Solutions segment offers residential and commercial heating and air conditioning products, such as reciprocating and scroll compressors; system protector and flow control devices; standard, programmable, and Wi-Fi thermostats; monitoring equipment and electronic controls for gas and electric heating systems; gas valves for furnaces and water heaters; ignition systems for furnaces; sensors and thermistors for home appliances; and temperature sensors and controls. It also provides reciprocating, scroll, and screw compressors; precision flow controls; system diagnostics and controls; and environmental control systems. In addition, this segment offers air conditioning, refrigeration, and lighting control technologies, as well as facility design and product management, site commissioning, facility monitoring, and energy modeling services; tools for professionals and homeowners; and appliance solutions. Emerson Electric Co. was incorporated in 1890 and is headquartered in Saint Louis, Missouri.",
        fullTimeEmployees=86700,
        city="Saint Louis",
        state="MO",
        trailingPE=17.054392,
        dividendYield=0.026500002,
        averageVolume=3074350,
        regularMarketOpen=83.09,
        volume=2730307,
        fiftyTwoWeekHigh=105.99,
        fiftyTwoWeekLow=76.77,
        recommendationKey="buy",
        industry="Specialty Industrial Machinery"
    )
    db.session.add(EMR)

    ENPH = Stock(
        name="Enphase Energy, Inc.",
        ticker="ENPH",
        marketCap=25743087616,
        dayHigh=207.19,
        dayLow=189.41,
        currentPrice=190.65,
        longBusinessSummary="Enphase Energy, Inc., together with its subsidiaries, designs, develops, manufactures, and sells home energy solutions for the solar photovoltaic industry in the United States and internationally. The company offers semiconductor-based microinverter, which converts energy at the individual solar module level, and combines with its proprietary networking and software technologies to provide energy monitoring and control services. It also offers AC battery storage systems; Envoy communications gateway; and Enlighten cloud-based monitoring service, as well as other accessories. The company sells its solutions to solar distributors; and directly to large installers, original equipment manufacturers, strategic partners, and homeowners, as well as through its legacy product upgrade program or online store. Enphase Energy, Inc. was incorporated in 2006 and is headquartered in Fremont, California.",
        fullTimeEmployees=2260,
        city="Fremont",
        state="CA",
        trailingPE=162.39352,
        dividendYield=None,
        averageVolume=2625756,
        regularMarketOpen=206.17,
        volume=2432882,
        fiftyTwoWeekHigh=282.46,
        fiftyTwoWeekLow=113.4,
        recommendationKey="buy",
        industry="Solar"
    )
    db.session.add(ENPH)

    ETR = Stock(
        name="Entergy Corporation",
        ticker="ETR",
        marketCap=22747381760,
        dayHigh=113.33,
        dayLow=111.561,
        currentPrice=111.85,
        longBusinessSummary="Entergy Corporation, together with its subsidiaries, engages in the production and distribution of electricity in the United States. It operates in two segments, Utility and Entergy Wholesale Commodities. The Utility segment generates, transmits, distributes, and sells electric power in portions of Arkansas, Louisiana, Mississippi, and Texas, including the City of New Orleans; and distributes natural gas. The Entergy Wholesale Commodities segment is involved in the ownership, operation, and decommissioning of nuclear power plants located in the northern United States; sale of electric power to wholesale customers; provision of services to other nuclear power plant owners; and ownership of interests in non-nuclear power plants that sell electric power to wholesale customers. The company generates electricity through gas, nuclear, coal, hydro, and solar power sources. It sells energy to retail power providers, utilities, electric power co-operatives, power trading organizations, and other power generation companies. Its power plants have approximately 26,000 megawatts (MW) of electric generating capacity, which include 6,000 MW of nuclear power. The company delivers electricity to 3 million utility customers in Arkansas, Louisiana, Mississippi, and Texas. Entergy Corporation was founded in 1913 and is based in New Orleans, Louisiana.",
        fullTimeEmployees=12500,
        city="New Orleans",
        state="LA",
        trailingPE=21.337275,
        dividendYield=0.038599998,
        averageVolume=1171404,
        regularMarketOpen=112.55,
        volume=1251630,
        fiftyTwoWeekHigh=126.82,
        fiftyTwoWeekLow=98.5,
        recommendationKey="buy",
        industry="Utilities—Regulated Electric"
    )
    db.session.add(ETR)

    EOG = Stock(
        name="EOG Resources, Inc.",
        ticker="EOG",
        marketCap=69295710208,
        dayHigh=119.919,
        dayLow=115.74,
        currentPrice=118.31,
        longBusinessSummary="EOG Resources, Inc., together with its subsidiaries, explores for, develops, produces, and markets crude oil, and natural gas and natural gas liquids. Its principal producing areas are in New Mexico and Texas in the United States; and the Republic of Trinidad and Tobago. As of December 31, 2021, it had total estimated net proved reserves of 3,747 million barrels of oil equivalent, including 1,548 million barrels (MMBbl) of crude oil and condensate reserves; 829 MMBbl of natural gas liquid reserves; and 8,222 billion cubic feet of natural gas reserves. The company was formerly known as Enron Oil & Gas Company. EOG Resources, Inc. was incorporated in 1985 and is headquartered in Houston, Texas.",
        fullTimeEmployees=2800,
        city="Houston",
        state="TX",
        trailingPE=15.774667,
        dividendYield=0.0254,
        averageVolume=4235451,
        regularMarketOpen=117.7,
        volume=4812676,
        fiftyTwoWeekHigh=147.99,
        fiftyTwoWeekLow=62.81,
        recommendationKey="buy",
        industry="Oil & Gas E&P"
    )
    db.session.add(EOG)

    EPAM = Stock(
        name="EPAM Systems, Inc.",
        ticker="EPAM",
        marketCap=17803139072,
        dayHigh=327.35,
        dayLow=308.88,
        currentPrice=311.51,
        longBusinessSummary="EPAM Systems, Inc. provides digital platform engineering and software development services worldwide. The company offers engineering services, including requirements analysis and platform selection, customization, cross-platform migration, implementation, and integration; infrastructure management services, such as software development, testing, and maintenance with private, public, and mobile infrastructures for application, database, network, server, storage, and systems operations management, as well as monitoring, incident notification, and resolution services; and maintenance and support services. It also provides operation solutions comprising integrated engineering practices and smart automation; and optimization solutions that include software application testing, test management, automation, and consulting services to enable customers enhance their existing software testing and quality assurance practices, as well as other testing services that identify threats and close loopholes to protect its customers' business systems from information loss. In addition, the company offers business, experience, technology, data, and technical advisory consulting services; and digital and service design solutions, which comprise strategy, design, creative, and program management services, as well as physical product development, such as artificial intelligence, robotics, and virtual reality. It serves the financial services, travel and consumer, software and hi-tech, business information and media, life sciences and healthcare, and other industries. The company was founded in 1993 and is headquartered in Newtown, Pennsylvania.",
        fullTimeEmployees=61600,
        city="Newtown",
        state="PA",
        trailingPE=39.886044,
        dividendYield=None,
        averageVolume=781445,
        regularMarketOpen=319.48,
        volume=472712,
        fiftyTwoWeekHigh=725.4,
        fiftyTwoWeekLow=168.59,
        recommendationKey="buy",
        industry="Information Technology Services"
    )
    db.session.add(EPAM)

    EFX = Stock(
        name="Equifax Inc.",
        ticker="EFX",
        marketCap=21955463168,
        dayHigh=186.66,
        dayLow=178.83,
        currentPrice=179.47,
        longBusinessSummary="Equifax Inc. provides information solutions and human resources business process automation outsourcing services for businesses, governments, and consumers. The company operates through three segments: Workforce Solutions, U.S. Information Solutions (USIS), and International. The Workforce Solutions segment offers employment, income, criminal history, and social security number verification services, as well as payroll-based transaction, employment tax management, and identity theft protection products. The USIS segment provides consumer and commercial information services, such as credit information and credit scoring, credit modeling and portfolio analytics, locate, fraud detection and prevention, identity verification, and other consulting; mortgage services; financial marketing services; identity management services; credit monitoring products; and online information, decisioning technology solutions, as well as portfolio management, mortgage reporting, and consumer credit information services. The International segment offers information service products, which include consumer and commercial services, such as credit and financial information, and credit scoring and modeling; and credit and other marketing products and services, as well as offers information, technology, and other services to support debt collections and recovery management. The company serves customers in financial services, mortgage, employers, consumer, commercial, telecommunication, retail, automotive, utility, brokerage, healthcare, and insurance industries, as well as state, federal, and local governments. It operates in the United States, Canada, Australia, New Zealand, India, the United Kingdom, Spain, Portugal, Argentina, Chile, Costa Rica, Ecuador, El Salvador, Honduras, Mexico, Paraguay, Peru, Uruguay, Brazil, the Republic of Ireland, Russia, Cambodia, Malaysia, Singapore, and the United Arab Emirates. The company was founded in 1899 and is headquartered in Atlanta, Georgia.",
        fullTimeEmployees=13000,
        city="Atlanta",
        state="GA",
        trailingPE=29.040455,
        dividendYield=0.0089,
        averageVolume=1075151,
        regularMarketOpen=184.76,
        volume=577497,
        fiftyTwoWeekHigh=300.11,
        fiftyTwoWeekLow=169.25,
        recommendationKey="buy",
        industry="Consulting Services"
    )
    db.session.add(EFX)

    EQIX = Stock(
        name="Equinix, Inc.",
        ticker="EQIX",
        marketCap=62401806336,
        dayHigh=690.46,
        dayLow=667.64,
        currentPrice=669.1,
        longBusinessSummary="Equinix (Nasdaq: EQIX) is the world's digital infrastructure company, enabling digital leaders to harness a trusted platform to bring together and interconnect the foundational infrastructure that powers their success. Equinix enables today's businesses to access all the right places, partners and possibilities they need to accelerate advantage. With Equinix, they can scale with agility, speed the launch of digital services, deliver world-class experiences and multiply their value.",
        fullTimeEmployees=11124,
        city="Redwood City",
        state="CA",
        trailingPE=123.678375,
        dividendYield=0.0185,
        averageVolume=499398,
        regularMarketOpen=687.93,
        volume=295406,
        fiftyTwoWeekHigh=885.26,
        fiftyTwoWeekLow=606.12,
        recommendationKey="buy",
        industry="REIT—Specialty"
    )
    db.session.add(EQIX)

    EQR = Stock(
        name="Equity Residential",
        ticker="EQR",
        marketCap=28300595200,
        dayHigh=74.36,
        dayLow=72.32,
        currentPrice=72.55,
        longBusinessSummary="Equity Residential is committed to creating communities where people thrive. The Company, a member of the S&P 500, is focused on the acquisition, development and management of residential properties located in and around dynamic cities that attract high quality long-term renters. Equity Residential owns or has investments in 305 properties consisting of 78,568 apartment units, located in Boston, New York, Washington, D.C., Seattle, San Francisco, Southern California and Denver.",
        fullTimeEmployees=2400,
        city="Chicago",
        state="IL",
        trailingPE=20.968208,
        dividendYield=0.033800002,
        averageVolume=1824588,
        regularMarketOpen=73.48,
        volume=1343251,
        fiftyTwoWeekHigh=94.32,
        fiftyTwoWeekLow=67.48,
        recommendationKey="hold",
        industry="REIT—Residential"
    )
    db.session.add(EQR)

    ESS = Stock(
        name="Essex Property Trust, Inc.",
        ticker="ESS",
        marketCap=17851844608,
        dayHigh=270.55,
        dayLow=263.92,
        currentPrice=264.02,
        longBusinessSummary="Essex Property Trust, Inc., an S&P 500 company, is a fully integrated real estate investment trust (REIT) that acquires, develops, redevelops, and manages multifamily residential properties in selected West Coast markets. Essex currently has ownership interests in 246 apartment communities comprising approximately 60,000 apartment homes with an additional 6 properties in various stages of active development.",
        fullTimeEmployees=1739,
        city="San Mateo",
        state="CA",
        trailingPE=43.7264,
        dividendYield=0.0344,
        averageVolume=424772,
        regularMarketOpen=266.86,
        volume=405037,
        fiftyTwoWeekHigh=363.36,
        fiftyTwoWeekLow=250.62,
        recommendationKey="buy",
        industry="REIT—Residential"
    )
    db.session.add(ESS)

    EL = Stock(
        name="The Estée Lauder Companies Inc.",
        ticker="EL",
        marketCap=91970396160,
        dayHigh=268.6,
        dayLow=256.31,
        currentPrice=257.37,
        longBusinessSummary="The Estée Lauder Companies Inc. manufactures, markets, and sells skin care, makeup, fragrance, and hair care products worldwide. The company offers a range of skin care products, including moisturizers, serums, cleansers, toners, body care, exfoliators, acne care and oil correctors, facial masks, cleansing devices, and sun care products; and makeup products, such as lipsticks, lip glosses, mascaras, foundations, eyeshadows, nail polishes, and powders, as well as compacts, brushes, and other makeup tools. It also provides fragrance products in various forms comprising eau de parfum sprays and colognes, as well as lotions, powders, creams, candles, and soaps; and hair care products that include shampoos, conditioners, styling products, treatment, finishing sprays, and hair color products, as well as sells ancillary products and services. The company offers its products under Estée Lauder, Aramis, Clinique, Lab Series, Origins, M·A·C, Bobbi Brown, La Mer, Aveda, Jo Malone London, Bumble and bumble, Darphin, Smashbox, Le Labo, Editions de Parfums Frédéric Malle, GLAMGLOW, By Kilian, BECCA, Too Faced, Dr. Jart+, DECIEM, and The Ordinary brands. It also holds license arrangements for Tommy Hilfiger, Donna Karan New York, DKNY, Michael Kors, and Ermenegildo Zegna brands. The company sells its products through department stores, specialty-multi retailers, upscale perfumeries and pharmacies, and salons and spas; freestanding stores; its own and authorized retailer websites; third-party online malls; stores in airports; and in-flight and duty-free shops. The company was founded in 1946 and is headquartered in New York, New York.",
        fullTimeEmployees=44640,
        city="New York",
        state="NY",
        trailingPE=28.118649,
        dividendYield=0.0097,
        averageVolume=1710062,
        regularMarketOpen=261.09,
        volume=1597599,
        fiftyTwoWeekHigh=374.2,
        fiftyTwoWeekLow=225.39,
        recommendationKey="buy",
        industry="Household & Personal Products"
    )
    db.session.add(EL)

    ETSY = Stock(
        name="Etsy, Inc.",
        ticker="ETSY",
        marketCap=9411891200,
        dayHigh=80.5,
        dayLow=73.946,
        currentPrice=74.04,
        longBusinessSummary="Etsy, Inc. operates two-sided online marketplaces that connect buyers and sellers primarily in the United States, the United Kingdom, Germany, Canada, Australia, France, and India. Its primary marketplace is Etsy.com that connects artisans and entrepreneurs with various consumers. The company also offers Reverb, a musical instrument marketplace; Depop, a fashion resale marketplace; and Elo7, a Brazil-based marketplace for handmade and unique items. In addition, it offers various seller services, including Etsy Payments, a payment processing service; Etsy Ads, an advertising platform; and Shipping Labels, which allows sellers in the United States, Canada, the United Kingdom, Australia, and India to purchase discounted shipping labels. Further, the company provides various seller tools, including Shop Manager dashboard, a centralized hub for Etsy sellers to track orders, manage inventory, view metrics and statistics, and have conversations with their customers; and Sell on Etsy, an application to enable enhanced onboarding and video uploading. Additionally, it offers Etsy seller analytics pages that provides insights regarding traffic acquisition for their shops; Targeted Offers, a sales and promotions tool, and social media tool; and accounting and bookkeeping services. The company also provides educational resources comprising blog posts, video tutorials, Etsy Seller Handbook, Etsy.com online forums, and insights; Etsy Teams, a platform to build personal relationships with other Etsy sellers; and a Star Seller program. As of December 31, 2021, it connected a total of 7.5 million active sellers to 96.3 million active buyers; and had 120 million items for sale. The company was formerly known as Indieco, Inc changed its name to Etsy, Inc. in June 2006. Etsy, Inc. was founded in 2005 and is headquartered in Brooklyn, New York.",
        fullTimeEmployees=2576,
        city="Brooklyn",
        state="NY",
        trailingPE=24.68,
        dividendYield=None,
        averageVolume=4920690,
        regularMarketOpen=79.11,
        volume=3937281,
        fiftyTwoWeekHigh=307.75,
        fiftyTwoWeekLow=67.01,
        recommendationKey="buy",
        industry="Internet Retail"
    )
    db.session.add(ETSY)

    EVRG = Stock(
        name="Evergy, Inc.",
        ticker="EVRG",
        marketCap=14856404992,
        dayHigh=65.79,
        dayLow=64.7,
        currentPrice=64.74,
        longBusinessSummary="Evergy, Inc., together with its subsidiaries, engages in the generation, transmission, distribution, and sale of electricity in Kansas and Missouri, the United States. It generates electricity through coal, hydroelectric, landfill gas, uranium, and natural gas and oil sources, as well as solar, wind, other renewable sources. The company has approximately 10,100 circuit miles of transmission lines; 39,800 circuit miles of overhead distribution lines; and 13,000 circuit miles of underground distribution lines. It serves approximately 1,620,400 customers, including residences, commercial firms, industrials, municipalities, and other electric utilities. Evergy, Inc. was incorporated in 2017 and is headquartered in Kansas City, Missouri.",
        fullTimeEmployees=4930,
        city="Kansas City",
        state="MO",
        trailingPE=18.392044,
        dividendYield=0.0352,
        averageVolume=1213287,
        regularMarketOpen=65.24,
        volume=651579,
        fiftyTwoWeekHigh=73.13,
        fiftyTwoWeekLow=59.34,
        recommendationKey="buy",
        industry="Utilities—Regulated Electric"
    )
    db.session.add(EVRG)

    ES = Stock(
        name="Eversource Energy",
        ticker="ES",
        marketCap=28769724416,
        dayHigh=85.4,
        dayLow=83.35,
        currentPrice=83.42,
        longBusinessSummary="Eversource Energy, a public utility holding company, engages in the energy delivery business. The company operates through Electric Distribution, Electric Transmission, Natural Gas Distribution, and Water Distribution segments. It is involved in the transmission and distribution of electricity; solar power facilities; and distribution of natural gas. The company operates regulated water utilities that provide water services to approximately 226,000 customers. It serves residential, commercial, industrial, municipal and fire protection, and other customers in Connecticut, Massachusetts, and New Hampshire. The company was formerly known as Northeast Utilities and changed its name to Eversource Energy in April 2015. Eversource Energy is based in Springfield, Massachusetts.",
        fullTimeEmployees=9227,
        city="Springfield",
        state="MA",
        trailingPE=22.18617,
        dividendYield=0.030299999,
        averageVolume=1510535,
        regularMarketOpen=84.46,
        volume=2214091,
        fiftyTwoWeekHigh=94.63,
        fiftyTwoWeekLow=77.07,
        recommendationKey="hold",
        industry="Utilities—Regulated Electric"
    )
    db.session.add(ES)

    EXC = Stock(
        name="Exelon Corporation",
        ticker="EXC",
        marketCap=42928594944,
        dayHigh=44.405,
        dayLow=43.6,
        currentPrice=43.88,
        longBusinessSummary="Exelon Corporation, a utility services holding company, engages in the energy generation, delivery, and marketing businesses in the United States and Canada. It owns nuclear, fossil, wind, hydroelectric, biomass, and solar generating facilities. The company also sells electricity to wholesale and retail customers; and sells natural gas, renewable energy, and other energy-related products and services. Additionally, it is involved in the purchase and regulated retail sale of electricity and natural gas; and transmission and distribution of electricity, and distribution of natural gas to retail customers. Further, the company offers support services, including legal, human resources, information technology, financial, supply management, accounting, engineering, customer operations, distribution and transmission planning, asset management, system operations, and power procurement services. It serves distribution utilities, municipalities, cooperatives, and financial institutions, as well as commercial, industrial, governmental, and residential customers. Exelon Corporation was incorporated in 1999 and is headquartered in Chicago, Illinois.",
        fullTimeEmployees=31518,
        city="Chicago",
        state="IL",
        trailingPE=25.660818,
        dividendYield=0.028900001,
        averageVolume=6925238,
        regularMarketOpen=43.97,
        volume=5864274,
        fiftyTwoWeekHigh=50.71,
        fiftyTwoWeekLow=31.512127,
        recommendationKey="buy",
        industry="Utilities—Diversified"
    )
    db.session.add(EXC)

    EXPD = Stock(
        name="Expeditors International of Washington, Inc.",
        ticker="EXPD",
        marketCap=16572793856,
        dayHigh=101.755,
        dayLow=97.15,
        currentPrice=97.83,
        longBusinessSummary="Expeditors International of Washington, Inc. provides logistics services in the Americas, North Asia, South Asia, Europe, the Middle East, Africa, and India. The company offers airfreight services, such as air freight consolidation and forwarding; ocean freight and ocean services, including ocean freight consolidation, direct ocean forwarding, and order management; customs brokerage, intra-continental ground transportation and delivery, and warehousing and distribution services; and customs clearance, purchase order management, vendor consolidation, time-definite transportation services, temperature-controlled transit, cargo insurance, specialized cargo monitoring and tracking, and other supply chain solutions. It also provides optimization, trade compliance, consulting, cargo security, and solutions. In addition, it acts as a freight consolidator or as an agent for the airline, which carries the shipment. Further, the company provides ancillary services that include preparation of shipping and customs documentation, packing, crating, insurance services, negotiation of letters of credit, and the preparation of documentation to comply with local export laws. Its customers include retailing and wholesaling, electronics, technology, and industrial and manufacturing companies. Expeditors International of Washington, Inc. was incorporated in 1979 and is headquartered in Seattle, Washington.",
        fullTimeEmployees=19867,
        city="Seattle",
        state="WA",
        trailingPE=14.476177,
        dividendYield=0.012,
        averageVolume=1529146,
        regularMarketOpen=100.47,
        volume=805810,
        fiftyTwoWeekHigh=137.8,
        fiftyTwoWeekLow=93.77,
        recommendationKey="hold",
        industry="Integrated Freight & Logistics"
    )
    db.session.add(EXPD)

    EXR = Stock(
        name="Extra Space Storage Inc.",
        ticker="EXR",
        marketCap=22898210816,
        dayHigh=175.58,
        dayLow=170.5901,
        currentPrice=171.02,
        longBusinessSummary="Extra Space Storage Inc., headquartered in Salt Lake City, Utah, is a self-administered and self-managed REIT and a member of the S&P 500. As of September 30, 2020, the Company owned and/or operated 1,906 self-storage stores in 40 states, Washington, D.C. and Puerto Rico. The Company's stores comprise approximately 1.4 million units and approximately 147.5 million square feet of rentable space. The Company offers customers a wide selection of conveniently located and secure storage units across the country, including boat storage, RV storage and business storage. The Company is the second largest owner and/or operator of self-storage stores in the United States and is the largest self-storage management company in the United States.",
        fullTimeEmployees=4309,
        city="Salt Lake City",
        state="UT",
        trailingPE=31.76449,
        dividendYield=0.0279,
        averageVolume=752845,
        regularMarketOpen=173.11,
        volume=456193,
        fiftyTwoWeekHigh=228.84,
        fiftyTwoWeekLow=156.7,
        recommendationKey="buy",
        industry="REIT—Industrial"
    )
    db.session.add(EXR)

    FFIV = Stock(
        name="F5, Inc.",
        ticker="FFIV",
        marketCap=9379119104,
        dayHigh=158.75,
        dayLow=153.07,
        currentPrice=153.18,
        longBusinessSummary="F5, Inc. provides multi-cloud application security and delivery solutions for the security, performance, and availability of network applications, servers, and storage systems. The company's multi-cloud application security and delivery solutions enable its customers to develop, deploy, operate, secure, and govern applications in any architecture, from on-premises to the public cloud. It offers application security and delivery products, including BIG-IP appliances and VIPRION chassis and related software modules and software-only Virtual Editions; Local Traffic Manager and DNS Services; Advanced Firewall Manager and Policy Enforcement Manager that leverage the unique performance characteristics of its hardware and software architecture; Application Security Manager and Access Policy Manager; NGINX Plus and NGINX Controller; Shape Defense and Enterprise Defense; Secure Web Gateway, and Silverline DDoS and Application security offerings; and online fraud and abuse prevention solutions. The company also provides a range of professional services, including consulting, training, installation, maintenance, and other technical support services. F5, Inc. sells its products to large enterprise businesses, public sector institutions, governments, and service providers through distributors, value-added resellers, managed service providers, and systems integrators in the Americas, Europe, the Middle East, Africa, and the Asia Pacific region. It has partnerships with public cloud providers, such as Amazon Web Services, Microsoft Azure, and Google Cloud Platform. The company was formerly known as F5 Networks, Inc. and changed its name to F5, Inc. in November 2021. F5, Inc. was incorporated in 1996 and is headquartered in Seattle, Washington.",
        fullTimeEmployees=6396,
        city="Seattle",
        state="WA",
        trailingPE=28.68539,
        dividendYield=None,
        averageVolume=536964,
        regularMarketOpen=157.62,
        volume=283770,
        fiftyTwoWeekHigh=249,
        fiftyTwoWeekLow=147.47,
        recommendationKey="buy",
        industry="Software—Infrastructure"
    )
    db.session.add(FFIV)

    FDS = Stock(
        name="FactSet Research Systems Inc.",
        ticker="FDS",
        marketCap=14211746816,
        dayHigh=393.365,
        dayLow=375.23,
        currentPrice=376,
        longBusinessSummary="FactSet Research Systems Inc., a financial data and analytics company, provides integrated financial information and analytical applications to the investment community in the Americas, Europe, the Middle East, Africa, and the Asia Pacific. The company delivers insight and information through the workflow solutions of research, analytics and trading, content and technology solutions, and wealth. It serves portfolio managers, investment banks, asset managers, wealth advisors, corporate clients, and other financial services entities. FactSet Research Systems Inc. was founded in 1978 and is headquartered in Norwalk, Connecticut.",
        fullTimeEmployees=10784,
        city="Norwalk",
        state="CT",
        trailingPE=35.707504,
        dividendYield=0.0095999995,
        averageVolume=290137,
        regularMarketOpen=391.15,
        volume=396392,
        fiftyTwoWeekHigh=495.4,
        fiftyTwoWeekLow=332.67,
        recommendationKey="hold",
        industry="Financial Data & Stock Exchanges"
    )
    db.session.add(FDS)

    FAST = Stock(
        name="Fastenal Company",
        ticker="FAST",
        marketCap=28280764416,
        dayHigh=51.64,
        dayLow=49.06,
        currentPrice=49.17,
        longBusinessSummary="Fastenal Company, together with its subsidiaries, engages in the wholesale distribution of industrial and construction supplies in the United States, Canada, Mexico, North America, and internationally. It offers fasteners, and related industrial and construction supplies under the Fastenal name. The company's fastener products include threaded fasteners, bolts, nuts, screws, studs, and related washers, which are used in manufactured products and construction projects, as well as in the maintenance and repair of machines. It also offers miscellaneous supplies and hardware, including pins, machinery keys, concrete anchors, metal framing systems, wire ropes, strut products, rivets, and related accessories. The company serves the manufacturing market comprising original equipment manufacturers; maintenance, repair, and operations; and non-residential construction market, which includes general, electrical, plumbing, sheet metal, and road contractors. It also serves farmers, truckers, railroads, mining companies, schools, and retail trades; and oil exploration, production, and refinement companies, as well as federal, state, and local governmental entities. The company distributes its products through a network of 3,209 in-market locations and 15 distribution centers. Fastenal Company was founded in 1967 and is headquartered in Winona, Minnesota.",
        fullTimeEmployees=18958,
        city="Winona",
        state="MN",
        trailingPE=31.928572,
        dividendYield=0.0235,
        averageVolume=3428983,
        regularMarketOpen=51.41,
        volume=4099500,
        fiftyTwoWeekHigh=64.75,
        fiftyTwoWeekLow=48.1,
        recommendationKey="hold",
        industry="Industrial Distribution"
    )
    db.session.add(FAST)

    FRT = Stock(
        name="Federal Realty Investment Trust",
        ticker="FRT",
        marketCap=7645152256,
        dayHigh=102.305,
        dayLow=98.17,
        currentPrice=98.28,
        longBusinessSummary="Federal Realty is a recognized leader in the ownership, operation and redevelopment of high-quality retail-based properties located primarily in major coastal markets from Washington, D.C. to Boston as well as San Francisco and Los Angeles. Founded in 1962, Federal Realty's mission is to deliver long-term, sustainable growth through investing in communities where retail demand exceeds supply. Its expertise includes creating urban, mixed-use neighborhoods like Santana Row in San Jose, California, Pike & Rose in North Bethesda, Maryland and Assembly Row in Somerville, Massachusetts. These unique and vibrant environments that combine shopping, dining, living and working provide a destination experience valued by their respective communities. Federal Realty's 106 properties include approximately 3,100 tenants, in 25 million square feet, and approximately 3,200 residential units. Federal Realty has increased its quarterly dividends to its shareholders for 54 consecutive years, the longest record in the REIT industry. Federal Realty is an S&P 500 index member and its shares are traded on the NYSE under the symbol FRT. For additional information about Federal Realty and its properties, visit www.federalrealty.com.",
        fullTimeEmployees=310,
        city="North Bethesda",
        state="MD",
        trailingPE=32.586205,
        dividendYield=0.0369,
        averageVolume=511185,
        regularMarketOpen=100.36,
        volume=515920,
        fiftyTwoWeekHigh=140.51,
        fiftyTwoWeekLow=92.02,
        recommendationKey="buy",
        industry="REIT—Retail"
    )
    db.session.add(FRT)

    FDX = Stock(
        name="FedEx Corporation",
        ticker="FDX",
        marketCap=63616405504,
        dayHigh=248.15,
        dayLow=239.62,
        currentPrice=240.09,
        longBusinessSummary="FedEx Corporation provides transportation, e-commerce, and business services in the United States and internationally. The company's FedEx Express segment offers express transportation, small-package ground delivery, and freight transportation services; time-critical transportation services; and cross-border e-commerce technology and e-commerce transportation solutions. Its FedEx Ground segment provides day-certain delivery services to businesses and residences. The company's FedEx Freight segment offers less-than-truckload freight transportation services. As of May 31, 2021, this segment had approximately 29,000 vehicles and 400 service centers. Its FedEx Services segment provides sales, marketing, information technology, communications, customer service, technical support, billing and collection, and back-office function services. The company's Corporate, Other and Eliminations segment offers integrated supply chain management solutions, specialty transportation, customs brokerage, and global ocean and air freight forwarding services; and an array of document and business services, and retail access to its customers for its package transportation businesses. The company was founded in 1971 and is based in Memphis, Tennessee.",
        fullTimeEmployees=384000,
        city="Memphis",
        state="TN",
        trailingPE=13.205544,
        dividendYield=0.014199999,
        averageVolume=2628708,
        regularMarketOpen=244,
        volume=2588924,
        fiftyTwoWeekHigh=302.65,
        fiftyTwoWeekLow=192.82,
        recommendationKey="buy",
        industry="Integrated Freight & Logistics"
    )
    db.session.add(FDX)

    FITB = Stock(
        name="Fifth Third Bancorp",
        ticker="FITB",
        marketCap=23778508800,
        dayHigh=35.99,
        dayLow=34.81,
        currentPrice=34.84,
        longBusinessSummary="Fifth Third Bancorp operates as a diversified financial services company in the United States. The company's Commercial Banking segment offers credit intermediation, cash management, and financial services; lending and depository products; and cash management, foreign exchange and international trade finance, derivatives and capital markets services, asset-based lending, real estate finance, public finance, commercial leasing, and syndicated finance for business, government, and professional customers. Its Branch Banking segment provides a range of deposit and loan products to individuals and small businesses. This segment offers checking and savings accounts, home equity loans and lines of credit, credit cards, and loans for automobiles and personal financing needs, as well as cash management services for small businesses. The company's Consumer Lending segment engages in direct lending activities that include origination, retention, and servicing of residential mortgage and home equity loans or lines of credit; and indirect lending activities, including loans to consumers through correspondent lenders and automobile dealers. Fifth Third Bancorp's Wealth & Asset Management segment provides various investment alternatives for individuals, companies, and not-for-profit organizations. It offers retail brokerage services to individual clients; and broker dealer services to the institutional marketplace. This segment also provides wealth planning, investment management, banking, insurance, and trust and estate services; and advisory services for institutional clients comprising middle market businesses, non-profits, states, and municipalities. As of December 31, 2021, the company operated 1,117 full-service banking centers and 2,322 ATMs in Ohio, Kentucky, Indiana, Michigan, Illinois, Florida, Tennessee, West Virginia, Georgia, North Carolina, and South Carolina. Fifth Third Bancorp was founded in 1858 and is headquartered in Cincinnati, Ohio.",
        fullTimeEmployees=19247,
        city="Cincinnati",
        state="OH",
        trailingPE=9.629629,
        dividendYield=0.0334,
        averageVolume=5710924,
        regularMarketOpen=35.5,
        volume=3459652,
        fiftyTwoWeekHigh=50.64,
        fiftyTwoWeekLow=33,
        recommendationKey="buy",
        industry="Banks—Regional"
    )
    db.session.add(FITB)

    FRC = Stock(
        name="First Republic Bank",
        ticker="FRC",
        marketCap=26394484736,
        dayHigh=149.9,
        dayLow=146.8975,
        currentPrice=147.22,
        longBusinessSummary="First Republic Bank, together with its subsidiaries, provides private banking, private business banking, and private wealth management services to clients in metropolitan areas in the United States. It operates in two segments, Commercial Banking and Wealth Management. The company accepts deposit products, such as noninterest-bearing checking, interest-bearing checking, money market checking accounts, money market savings accounts, and passbook accounts, as well as certificates of deposit. It also offers a range of lending products that comprise residential mortgage loans, home equity lines of credit, multifamily loans, commercial real estate and construction loans, personal and business loans, single family construction loans, and other loans and lines of credit to businesses and individuals. The company's loans are secured by single family residences, multifamily buildings, and commercial real estate properties. In addition, it provides wealth management services, which include various investment strategies and products, online investment management, trust and custody, full service and online brokerage, financial and estate planning, and access to alternative investments, as well as investing, insurance, and foreign exchange services. Further, the company offers online and mobile banking services; refinancing services; and ATM and debit cards. As of December 31, 2021, it offered its services through 82 licensed deposit taking offices primarily in the San Francisco, Palo Alto, Los Angeles, Santa Barbara, Newport Beach and San Diego, California; Portland, Oregon; Boston, Massachusetts; Palm Beach, Florida; Greenwich, Connecticut; New York, New York; and Jackson, Wyoming. It also has 12 additional offices that offer lending, wealth management, or trust services. First Republic Bank was founded in 1985 and is headquartered in San Francisco, California.",
        fullTimeEmployees=6295,
        city="San Francisco",
        state="CA",
        trailingPE=20.269861,
        dividendYield=0.0076,
        averageVolume=1224751,
        regularMarketOpen=148.26,
        volume=1179351,
        fiftyTwoWeekHigh=222.86,
        fiftyTwoWeekLow=133.37,
        recommendationKey="buy",
        industry="Banks—Regional"
    )
    db.session.add(FRC)

    FE = Stock(
        name="FirstEnergy Corp.",
        ticker="FE",
        marketCap=21575520256,
        dayHigh=38.7,
        dayLow=37.775,
        currentPrice=37.79,
        longBusinessSummary="FirstEnergy Corp., through its subsidiaries, generates, transmits, and distributes electricity in the United States. It operates through Regulated Distribution and Regulated Transmission segments. The company owns and operates coal-fired, nuclear, hydroelectric, natural gas, wind, and solar power generating facilities. It operates 24,074 circuit miles of overhead and underground transmission lines; and electric distribution systems, including 273,295 miles of overhead pole line and underground conduit carrying primary, secondary, and street lighting circuits. The company serves approximately 6 million customers in Ohio, Pennsylvania, West Virginia, Maryland, New Jersey, and New York. FirstEnergy Corp. was incorporated in 1996 and is headquartered in Akron, Ohio.",
        fullTimeEmployees=12395,
        city="Akron",
        state="OH",
        trailingPE=16.961401,
        dividendYield=0.0434,
        averageVolume=3975095,
        regularMarketOpen=38.38,
        volume=2112113,
        fiftyTwoWeekHigh=48.85,
        fiftyTwoWeekLow=35.32,
        recommendationKey="buy",
        industry="Utilities—Regulated Electric"
    )
    db.session.add(FE)

    FIS = Stock(
        name="Fidelity National Information Services, Inc.",
        ticker="FIS",
        marketCap=59085983744,
        dayHigh=99.14,
        dayLow=94,
        currentPrice=94.27,
        longBusinessSummary="Fidelity National Information Services, Inc. provides technology solutions for merchants, banks, and capital markets firms worldwide. It operates through Merchant Solutions, Banking Solutions, and Capital Market Solutions segments. The Merchant Solutions segment offers enterprise acquiring, software-led small- to medium-sized businesses acquiring, and global e-commerce solutions. The Banking Solutions segment provides core processing and ancillary applications; digital solutions, including Internet, mobile, and e-banking; fraud, risk management, and compliance solutions; electronic funds transfer and network services; card and retail payment solutions; wealth and retirement solutions; and item processing and output services. The Capital Market Solutions segment offers securities processing and finance, global trading, asset management and insurance, and corporate liquidity solutions. Fidelity National Information Services, Inc. was founded in 1968 and is headquartered in Jacksonville, Florida.",
        fullTimeEmployees=65000,
        city="Jacksonville",
        state="FL",
        trailingPE=64.12925,
        dividendYield=0.0199,
        averageVolume=3561932,
        regularMarketOpen=97.47,
        volume=2636049,
        fiftyTwoWeekHigh=152.2,
        fiftyTwoWeekLow=85,
        recommendationKey="buy",
        industry="Information Technology Services"
    )
    db.session.add(FIS)

    FISV = Stock(
        name="Fiserv, Inc.",
        ticker="FISV",
        marketCap=59830226944,
        dayHigh=94.99,
        dayLow=90.395,
        currentPrice=90.62,
        longBusinessSummary="Fiserv, Inc., together with its subsidiaries, provides payment and financial services technology worldwide. The company operates through Acceptance, Fintech, and Payments segments. The Acceptance segment provides point-of-sale merchant acquiring and digital commerce services; mobile payment services; security and fraud protection products; Carat, an omnichannel commerce solution; Clover, a cloud-based point-of-sale and business management platform; and Clover Connect, an independent software vendors platform. This segment distributes through various channels, including direct sales teams, strategic partnerships with agent sales forces, independent software vendors, financial institutions, and other strategic partners. The Fintech segment offers customer deposit and loan accounts, as well as manages an institution's general ledger and central information files. This segment also provides digital banking, financial and risk management, professional services and consulting, item processing and source capture, and other products and services. The Payments segment offers card transactions, such as debit, credit, and prepaid card processing and services; security and fraud protection products; card production; print services; and various network services, as well as non-card digital payment software and services, including bill payment, account-to-account transfers, person-to-person payments, electronic billing, and security and fraud protection products. It serves business, banks, credit unions, other financial institutions, merchants, and corporate clients. The company was incorporated in 1984 and is headquartered in Brookfield, Wisconsin.",
        fullTimeEmployees=44000,
        city="Brookfield",
        state="WI",
        trailingPE=46.95337,
        dividendYield=None,
        averageVolume=3110895,
        regularMarketOpen=93.26,
        volume=2606331,
        fiftyTwoWeekHigh=119.86,
        fiftyTwoWeekLow=87.03,
        recommendationKey="buy",
        industry="Information Technology Services"
    )
    db.session.add(FISV)

    FLT = Stock(
        name="FLEETCOR Technologies, Inc.",
        ticker="FLT",
        marketCap=17165383680,
        dayHigh=225.03,
        dayLow=210.85,
        currentPrice=211.4,
        longBusinessSummary="FLEETCOR Technologies, Inc. provides digital payment solutions for businesses to control purchases and make payments. It offers corporate payments solutions, such as accounts payable automation; Virtual Card, which provides a single-use card number for a specific amount usable within a defined timeframe; Cross-Border that is used by its customers to pay international vendors, foreign office and personnel expenses, capital expenditures, and profit repatriation and dividends; and purchasing cards and travel and entertainment cards for its customers to analyze and manage their corporate spending. The company also provides employee expense management solutions, including fuel solutions to businesses and government entities that operate vehicle fleets, as well as to oil and leasing companies, and fuel marketers; lodging solutions to businesses that have employees who travel overnight for work purposes, as well as to airlines and cruise lines to accommodate traveling crews and stranded passengers; and electronic toll payments solutions to businesses and consumers in the form of radio frequency identification tags affixed to vehicles' windshields. In addition, it offers gift card program management and processing services in plastic and digital forms that include card design, production and packaging, delivery and fulfillment, card and account management, transaction processing, promotion development and management, website design and hosting, program analytics, and card distribution channel management. Further, it provides other products consisting of payroll cards, vehicle maintenance service solution, long-haul transportation solution, prepaid food vouchers or cards, and prepaid transportation cards and vouchers. The company serves business, merchant, consumer, and payment network customers in North America, Brazil, and Internationally. The company was founded in 1986 and is headquartered in Atlanta, Georgia.",
        fullTimeEmployees=9700,
        city="Atlanta",
        state="GA",
        trailingPE=21.825315,
        dividendYield=None,
        averageVolume=578825,
        regularMarketOpen=221.37,
        volume=674467,
        fiftyTwoWeekHigh=282.02,
        fiftyTwoWeekLow=200.78,
        recommendationKey="buy",
        industry="Software—Infrastructure"
    )
    db.session.add(FLT)

    FMC = Stock(
        name="FMC Corporation",
        ticker="FMC",
        marketCap=13667560448,
        dayHigh=111.6377,
        dayLow=107.74,
        currentPrice=107.83,
        longBusinessSummary="FMC Corporation, an agricultural sciences company, provides crop protection, plant health, and professional pest and turf management products. It develops, markets, and sells crop protection chemicals that include insecticides, herbicides, and fungicides; and biologicals, crop nutrition, and seed treatment products, which are used in agriculture to enhance crop yield and quality by controlling a range of insects, weeds, and diseases, as well as in non-agricultural markets for pest control. The company markets its products through its own sales organization and through alliance partners, independent distributors, and sales representatives. It operates in North America, Latin America, Europe, the Middle East, Africa, and Asia. FMC Corporation was founded in 1883 and is headquartered in Philadelphia, Pennsylvania.",
        fullTimeEmployees=6400,
        city="Philadelphia",
        state="PA",
        trailingPE=23.600351,
        dividendYield=0.0182,
        averageVolume=1024264,
        regularMarketOpen=109.99,
        volume=728005,
        fiftyTwoWeekHigh=140.99,
        fiftyTwoWeekLow=87.27,
        recommendationKey="buy",
        industry="Agricultural Inputs"
    )
    db.session.add(FMC)

    F = Stock(
        name="Ford Motor Company",
        ticker="F",
        marketCap=47195594752,
        dayHigh=12.435,
        dayLow=11.8,
        currentPrice=11.81,
        longBusinessSummary="Ford Motor Company designs, manufactures, markets, and services a range of Ford trucks, cars, sport utility vehicles, electrified vehicles, and Lincoln luxury vehicles worldwide. It operates through three segments: Automotive, Mobility, and Ford Credit. The Automotive segment sells Ford and Lincoln vehicles, service parts, and accessories through distributors and dealers, as well as through dealerships to commercial fleet customers, daily rental car companies, and governments. The Mobility segment designs and builds mobility services; and provides self-driving systems development services. The Ford Credit segment primarily engages in vehicle-related financing and leasing activities to and through automotive dealers. It provides retail installment sale contracts for new and used vehicles; and direct financing leases for new vehicles to retail and commercial customers, such as leasing companies, government entities, daily rental companies, and fleet customers. This segment also offers wholesale loans to dealers to finance the purchase of vehicle inventory; and loans to dealers to finance working capital and enhance dealership facilities, purchase dealership real estate, and other dealer vehicle programs. The company has a strategic collaboration with ARB Corporation Limited to develop a suite of aftermarket products for the new Ford Bronco. Ford Motor Company was incorporated in 1903 and is based in Dearborn, Michigan.",
        fullTimeEmployees=183000,
        city="Dearborn",
        state="MI",
        trailingPE=16.563816,
        dividendYield=0.0296,
        averageVolume=62205508,
        regularMarketOpen=12.14,
        volume=45318802,
        fiftyTwoWeekHigh=25.87,
        fiftyTwoWeekLow=10.9,
        recommendationKey="hold",
        industry="Auto Manufacturers"
    )
    db.session.add(F)

    FTNT = Stock(
        name="Fortinet, Inc.",
        ticker="FTNT",
        marketCap=9366915072,
        dayHigh=60.59,
        dayLow=57.19,
        currentPrice=57.29,
        longBusinessSummary="Fortinet, Inc. provides broad, integrated, and automated cybersecurity solutions in the Americas, Europe, the Middle East, Africa, and the Asia Pacific. It offers FortiGate hardware and software licenses that provide various security and networking functions, including firewall, intrusion prevention, anti-malware, virtual private network, application control, web filtering, anti-spam, and wide area network acceleration. The company also provides FortiSwitch product family that offers secure switching solutions for connecting customers their end devices; FortiAP product family, which provides secure wireless networking solutions; FortiExtender, a hardware appliance; FortiAnalyzer product family, which offers centralized network logging, analyzing, and reporting solutions; and FortiManager product family that provides central and scalable management solution for its FortiGate products. It offers FortiWeb product family provides web application firewall solutions; FortiMail product family that secure email gateway solutions; FortiSandbox technology that delivers proactive detection and mitigation services; FortiClient that provides endpoint protection with pattern-based anti-malware, behavior-based exploit protection, web-filtering, and an application firewall; FortiToken and FortiAuthenticator product families for multi-factor authentication to safeguard systems, assets, and data; and FortiEDR/XDR, an endpoint protection solution that provides both comprehensive machine-learning anti-malware execution and real-time post-infection protection. It provides security subscription, technical support, professional, and training services. It sells its security solutions to channel partners and directly to various customers in telecommunications, technology, government, financial services, education, retail, manufacturing, and healthcare industries. It has strategic alliance with Linksys. Fortinet, Inc. was incorporated in 2000 and is headquartered in Sunnyvale, California.",
        fullTimeEmployees=10195,
        city="Sunnyvale",
        state="CA",
        trailingPE=17.245636,
        dividendYield=None,
        averageVolume=6511864,
        regularMarketOpen=59.61,
        volume=4749732,
        fiftyTwoWeekHigh=74.354,
        fiftyTwoWeekLow=47.27202,
        recommendationKey="buy",
        industry="Software—Infrastructure"
    )
    db.session.add(FTNT)

    FTV = Stock(
        name="Fortive Corporation",
        ticker="FTV",
        marketCap=19696689152,
        dayHigh=56.47,
        dayLow=54.895,
        currentPrice=54.93,
        longBusinessSummary="Fortive Corporation designs, develops, manufactures, markets, and services professional and engineered products, software, and services worldwide. Its Intelligent Operating Solutions segment offers connected reliability tools; environment, health, safety, and quality enterprise software products; facility and asset lifecycle software; pre-construction planning and construction procurement solutions; ruggedized professional test tools; electric, pressure, and temperature calibration tools; and portable gas detection tools for a range of vertical end markets including manufacturing, process industries, healthcare, utilities and power, communications and electronics, and others. It markets its products and services under the ACCRUENT, FLUKE, GORDIAN, INDUSTRIAL SCIENTIFIC, INTELEX, PRUFTECHNIK, and SERVICECHANNEL brands. The company's Precision Technologies segment provides electrical test and measurement instruments and services; energetic material devices; and sensor and control system solutions for power and energy, medical equipment, food and beverage, aerospace and defense, off-highway vehicles, electronics, semiconductors, and other general industrial markets. This segment markets its products under the ANDERSON-NEGELE, GEMS, SETRA, HENGSTLER-DYNAPAR, QUALITROL, PACIFIC SCIENTIFIC, KEITHLEY, and TEKTRONIX brands. Its Advanced Healthcare Solutions segment offers hardware and software products and services, including instrument and device reprocessing, instrument tracking, biomedical test tools, radiation safety monitoring, and asset management services; subscription-based surgical inventory management systems to facilitate inventory management and regulatory compliance, as well as technical, analytical, and compliance services to determine radiation exposure services under the ASP, CENSIS, CENSITRAC, EVOTECH, FLUKE BIOMEDICAL, INVETECH, LANDAUER, RAYSAFE, and STERRAD brands. Fortive Corporation was incorporated in 2015 and is headquartered in Everett, Washington.",
        fullTimeEmployees=18000,
        city="Everett",
        state="WA",
        trailingPE=11.982985,
        dividendYield=0.0047999998,
        averageVolume=2747156,
        regularMarketOpen=55.93,
        volume=980340,
        fiftyTwoWeekHigh=79.87,
        fiftyTwoWeekLow=53.05,
        recommendationKey="buy",
        industry="Scientific & Technical Instruments"
    )
    db.session.add(FTV)

    FBHS = Stock(
        name="Fortune Brands Home & Security, Inc.",
        ticker="FBHS",
        marketCap=8297419776,
        dayHigh=63.71,
        dayLow=61.081,
        currentPrice=61.13,
        longBusinessSummary="Fortune Brands Home & Security, Inc. provides home and security products for residential home repair, remodeling, new construction, and security applications. It operates in three segments: Plumbing, Outdoors & Security, and Cabinets. The Plumbing segment manufactures, assembles, and sells faucets, accessories, kitchen sinks, and waste disposals under the Moen, ROHL, Riobel, Victoria+Albert, Perrin & Rowe, and Shaws brands in the United States, China, Canada, Mexico, Southeast Asia, Europe, and South America directly through its own sales force, as well as through independent manufacturers' representatives to wholesalers, home centers, mass merchandisers, and industrial distributors. The Outdoors & Security segment offers fiberglass and steel entry door systems under the Therma-Tru brand; storm, screen, and security doors under the Larson brand; composite decking and railing under the Fiberon brand; and urethane millwork under the Fypon brand. This segment also manufactures, sources, and distributes locks, safety and security devices, and electronic security products under the Master Lock and American Lock brands; and fire resistant safes, security containers, and commercial cabinets under the SentrySafe brand. It serves home centers, hardware and other retailers, millwork building products and wholesale distributors, specialty dealers, and remodeling and renovation markets, as well as locksmiths, industrial and institutional users, and original equipment manufacturers in the United States, Canada, Europe, Central America, Japan, and Australia. The Cabinets segment manufactures custom, semi-custom, and custom cabinetry, as well as vanities for the kitchen, bath, and other parts of the home directly to kitchen and bath dealers, home centers, wholesalers, and builders in North America under the AOK, Diamond Brands, Homecrest, Kitchen Craft, Omega, and EVE brands. The company was incorporated in 1988 and is headquartered in Deerfield, Illinois.",
        fullTimeEmployees=28000,
        city="Deerfield",
        state="IL",
        trailingPE=11.282761,
        dividendYield=0.0161,
        averageVolume=1630116,
        regularMarketOpen=62.87,
        volume=681034,
        fiftyTwoWeekHigh=109.23,
        fiftyTwoWeekLow=56.86,
        recommendationKey="buy",
        industry="Furnishings, Fixtures & Appliances"
    )
    db.session.add(FBHS)

    FOXA = Stock(
        name="Fox Corporation",
        ticker="FOXA",
        marketCap=18021378048,
        dayHigh=33.47,
        dayLow=32.625,
        currentPrice=32.71,
        longBusinessSummary="Fox Corporation operates as a news, sports, and entertainment company in the United States. The company operates through three segments: Cable Network Programming; Television; and Other, Corporate and Eliminations. The Cable Network Programming segment produces and licenses news, business news, and sports content for distribution primarily through cable television systems, direct broadcast satellite operators, telecommunications companies, and online multi-channel video programming distributors. It operates FOX News, a national cable news channel; FOX Business, a business news national cable channel; FS1 and FS2 multi-sport national networks; FOX Sports Racing, a video programming service that comprises motor sports programming; and FOX Soccer Plus, a video programming network for live soccer and rugby competitions; FOX Deportes, a Spanish-language sports programming service; and Big Ten Network, a national video programming service. The Television segment acquires, produces, markets, and distributes broadcast network programming. It operates The FOX Network, a national television broadcast network that broadcasts sports programming and entertainment; MyNetworkTV, a programming distribution service; Fox Alternative Entertainment, a full-service production studio that develops and produces unscripted and alternative programming; Bento Box, which develops and produces animated programing; and Tubi, a free advertising-supported video-on-demand service. This segment owns and operates 29 broadcast television stations. The Other, Corporate and Eliminations segment owns the FOX Studios lot that provides production and post-production services, including 15 sound stages, 2 broadcast studios, theaters and screening rooms, editing bays, and television and film production facilities in Los Angeles, California. The company was incorporated in 2018 and is based in New York, New York.",
        fullTimeEmployees=9000,
        city="New York",
        state="NY",
        trailingPE=11.058147,
        dividendYield=0.0143,
        averageVolume=2701979,
        regularMarketOpen=33.16,
        volume=1798986,
        fiftyTwoWeekHigh=44.95,
        fiftyTwoWeekLow=31.325,
        recommendationKey="buy",
        industry="Broadcasting"
    )
    db.session.add(FOXA)

    FOX = Stock(
        name="Fox Corporation",
        ticker="FOX",
        marketCap=17995526144,
        dayHigh=30.94,
        dayLow=30.1915,
        currentPrice=30.22,
        longBusinessSummary="Fox Corporation operates as a news, sports, and entertainment company in the United States. The company operates through three segments: Cable Network Programming; Television; and Other, Corporate and Eliminations. The Cable Network Programming segment produces and licenses news, business news, and sports content for distribution primarily through cable television systems, direct broadcast satellite operators, telecommunications companies, and online multi-channel video programming distributors. It operates FOX News, a national cable news channel; FOX Business, a business news national cable channel; FS1 and FS2 multi-sport national networks; FOX Sports Racing, a video programming service that comprises motor sports programming; and FOX Soccer Plus, a video programming network for live soccer and rugby competitions; FOX Deportes, a Spanish-language sports programming service; and Big Ten Network, a national video programming service. The Television segment acquires, produces, markets, and distributes broadcast network programming. It operates The FOX Network, a national television broadcast network that broadcasts sports programming and entertainment; MyNetworkTV, a programming distribution service; Fox Alternative Entertainment, a full-service production studio that develops and produces unscripted and alternative programming; Bento Box, which develops and produces animated programing; and Tubi, a free advertising-supported video-on-demand service. This segment owns and operates 29 broadcast television stations. The Other, Corporate and Eliminations segment owns the FOX Studios lot that provides production and post-production services, including 15 sound stages, 2 broadcast studios, theaters and screening rooms, editing bays, and television and film production facilities in Los Angeles, California. The company was incorporated in 2018 and is based in New York, New York.",
        fullTimeEmployees=9000,
        city="New York",
        state="NY",
        trailingPE=10.216362,
        dividendYield=0.0156,
        averageVolume=1157427,
        regularMarketOpen=30.59,
        volume=619411,
        fiftyTwoWeekHigh=40.91,
        fiftyTwoWeekLow=28.96,
        recommendationKey="none",
        industry="Broadcasting"
    )
    db.session.add(FOX)

    BEN = Stock(
        name="Franklin Resources, Inc.",
        ticker="BEN",
        marketCap=12384301056,
        dayHigh=25.635,
        dayLow=24.66,
        currentPrice=24.68,
        longBusinessSummary="Franklin Resources, Inc. is a publicly owned asset management holding company. Through its subsidiaries, the firm provides its services to individuals, institutions, pension plans, trusts, and partnerships. It launches equity, fixed income, balanced, and multi-asset mutual funds through its subsidiaries. The firm invests in the public equity, fixed income, and alternative markets. Franklin Resources, Inc. was founded in 1947 and is based in San Mateo, California with an additional office in Hyderabad, India.",
        fullTimeEmployees=10400,
        city="San Mateo",
        state="CA",
        trailingPE=6.9131656,
        dividendYield=0.0462,
        averageVolume=3226470,
        regularMarketOpen=25.33,
        volume=3199246,
        fiftyTwoWeekHigh=38.27,
        fiftyTwoWeekLow=22.76,
        recommendationKey="hold",
        industry="Asset Management"
    )
    db.session.add(BEN)

    FCX = Stock(
        name="Freeport-McMoRan Inc.",
        ticker="FCX",
        marketCap=45199507456,
        dayHigh=32.3,
        dayLow=30.675,
        currentPrice=30.78,
        longBusinessSummary="Freeport-McMoRan Inc. engages in the mining of mineral properties in North America, South America, and Indonesia. The company primarily explores for copper, gold, molybdenum, silver, and other metals, as well as oil and gas. Its assets include the Grasberg minerals district in Indonesia; Morenci, Bagdad, Safford, Sierrita, and Miami in Arizona; Tyrone and Chino in New Mexico; and Henderson and Climax in Colorado, North America, as well as Cerro Verde in Peru and El Abra in Chile. The company also operates a portfolio of oil and gas properties primarily located in offshore California and the Gulf of Mexico. As of December 31, 2021, it operated approximately 135 wells. The company was formerly known as Freeport-McMoRan Copper & Gold Inc. and changed its name to Freeport-McMoRan Inc. in July 2014. Freeport-McMoRan Inc. was incorporated in 1987 and is headquartered in Phoenix, Arizona.",
        fullTimeEmployees=24700,
        city="Phoenix",
        state="AZ",
        trailingPE=11.654676,
        dividendYield=0.0171,
        averageVolume=18740590,
        regularMarketOpen=31.54,
        volume=21909402,
        fiftyTwoWeekHigh=51.99,
        fiftyTwoWeekLow=28.87,
        recommendationKey="buy",
        industry="Copper"
    )
    db.session.add(FCX)

    IT = Stock(
        name="Gartner, Inc.",
        ticker="IT",
        marketCap=19688839168,
        dayHigh=250.36,
        dayLow=239.1,
        currentPrice=239.41,
        longBusinessSummary="Gartner, Inc. operates as a research and advisory company in the United States, Canada, Europe, the Middle East, Africa, and internationally. It operates through three segments: Research, Conferences, and Consulting. The Research segment delivers its research primarily through a subscription service that include on-demand access to published research content, data and benchmarks, and direct access to a network of research experts. The Conferences segment offers business professionals in an organization the opportunity to learn, share, and network. The Consulting segment offers market research, custom analysis, and on-the-ground support services. This segment also offers actionable solutions for IT-related priorities, including IT cost optimization, digital transformation, and IT sourcing optimization. Gartner, Inc. was founded in 1979 and is headquartered in Stamford, Connecticut.",
        fullTimeEmployees=16600,
        city="Stamford",
        state="CT",
        trailingPE=29.833023,
        dividendYield=None,
        averageVolume=553896,
        regularMarketOpen=248.15,
        volume=309835,
        fiftyTwoWeekHigh=369,
        fiftyTwoWeekLow=221.39,
        recommendationKey="buy",
        industry="Information Technology Services"
    )
    db.session.add(IT)

    GNRC = Stock(
        name="Generac Holdings Inc.",
        ticker="GNRC",
        marketCap=13691792384,
        dayHigh=228.9126,
        dayLow=216.46,
        currentPrice=217.02,
        longBusinessSummary="Generac Holdings Inc. designs, manufactures, and sells power generation equipment, energy storage systems, and other power products for the residential, and light commercial and industrial markets worldwide. The company offers engines, alternators, batteries, electronic controls, steel enclosures, and other components. It also provides residential automatic standby generators ranging in output from 7.5kW to 150kW; air-cooled engine residential standby generators ranging from 7.5kW to 26kW; liquid-cooled engine generators with outputs ranging from 22kW to 150kW; and Mobile Link, a remote monitoring system for home standby generators. In addition, the company offers various portable generators ranging in size from 800W to 17.5kW; outdoor power equipment, such as trimmers, field and brush mowers, log splitters, stump grinders, chipper shredders, lawn and leaf vacuums, pressure washers, and water pumps; and clean energy solution under the PWRcell and PWRview brands. Further, it provides light towers, mobile generators, and mobile energy storage systems; commercial mobile pumps and dust-suppression equipment; various gaseous-engine control systems and accessories; light-commercial standby generators ranging from 22kW to 150kW and related transfer switches providing three-phase power for small and mid-sized businesses; and industrial generators ranging in output from 10kW to 3,250kW used as emergency backup for healthcare, telecom, datacom, commercial office, retail, municipal, and manufacturing markets. Additionally, the company sells aftermarket service parts and product accessories to dealers. It distributes its products through independent residential dealers, industrial distributors and dealers, national and regional retailers, e-commerce partners, electrical, HVAC and solar wholesalers, catalogs, equipment rental companies and distributors, and solar installers; and directly to end users. The company was founded in 1959 and is headquartered in Waukesha, Wisconsin.",
        fullTimeEmployees=8955,
        city="Waukesha",
        state="WI",
        trailingPE=26.359774,
        dividendYield=None,
        averageVolume=1121048,
        regularMarketOpen=225.36,
        volume=647929,
        fiftyTwoWeekHigh=524.31,
        fiftyTwoWeekLow=197.94,
        recommendationKey="buy",
        industry="Specialty Industrial Machinery"
    )
    db.session.add(GNRC)

    GD = Stock(
        name="General Dynamics Corporation",
        ticker="GD",
        marketCap=61565882368,
        dayHigh=227.9799,
        dayLow=220.09,
        currentPrice=220.49,
        longBusinessSummary="General Dynamics Corporation operates as an aerospace and defense company worldwide. It operates through four segments: Aerospace, Marine Systems, Combat Systems, and Technologies. The Aerospace segment designs, manufactures, and sells business jets; and offers aircraft maintenance and repair, management, charter, aircraft-on-ground support and completion, staffing, and fixed-base operator services. The Marine Systems segment designs and builds nuclear-powered submarines, surface combatants, and auxiliary ships for the United States Navy and Jones Act ships for commercial customers, as well as builds crude oil and product tankers, and container and cargo ships. This segment also provides navy ships maintenance and modernization services; lifecycle support and repair services for navy surface ships; and program management, planning, engineering, and design support services for submarines and surface ships. The Combat Systems segment manufactures land combat solutions, such as wheeled and tracked combat vehicles, Stryker wheeled combat vehicles, piranha vehicles, weapons systems, munitions, mobile bridge systems with payloads, tactical vehicles, main battle tanks, armored vehicles, and armaments. This segment also offers modernization programs, engineering, support, and sustainment services. The Technologies segment provides information technology solutions and mission support services; mobile communication, computers, and command-and-control mission systems; and intelligence, surveillance, and reconnaissance solutions to military, intelligence, and federal civilian customers. This segment also offers cloud computing, artificial intelligence; machine learning; big data analytics; development, security, and operations; software-defined networks; everything-as-a-service; defense enterprise office system solutions; and unmanned undersea vehicle manufacturing and assembly services. General Dynamics Corporation was founded in 1899 and is headquartered in Reston, Virginia.",
        fullTimeEmployees=103100,
        city="Reston",
        state="VA",
        trailingPE=18.922932,
        dividendYield=0.0223,
        averageVolume=1432179,
        regularMarketOpen=224.78,
        volume=1616946,
        fiftyTwoWeekHigh=254.99,
        fiftyTwoWeekLow=182.66,
        recommendationKey="buy",
        industry="Aerospace & Defense"
    )
    db.session.add(GD)

    GIS = Stock(
        name="General Mills, Inc.",
        ticker="GIS",
        marketCap=42381324288,
        dayHigh=71.69,
        dayLow=70.085,
        currentPrice=70.26,
        longBusinessSummary="General Mills, Inc. manufactures and markets branded consumer foods worldwide. The company operates in five segments: North America Retail; Convenience Stores & Foodservice; Europe & Australia; Asia & Latin America; and Pet. It offers ready-to-eat cereals, refrigerated yogurt, soup, meal kits, refrigerated and frozen dough products, dessert and baking mixes, bakery flour, frozen pizza and pizza snacks, snack bars, fruit and salty snacks, ice cream, nutrition bars, wellness beverages, and savory and grain snacks, as well as various organic products, including frozen and shelf-stable vegetables. It also supplies branded and unbranded food products to the North American foodservice and commercial baking industries; and manufactures and markets pet food products, including dog and cat food. The company markets its products under the Annie's, Betty Crocker, Bisquick, Blue Buffalo, Blue Basics, Blue Freedom, Bugles, Cascadian Farm, Cheerios, Chex, Cinnamon Toast Crunch, Cocoa Puffs, Cookie Crisp, EPIC, Fiber One, Food Should Taste Good, Fruit by the Foot, Fruit Gushers, Fruit Roll-Ups, Gardetto's, Go-Gurt, Gold Medal, Golden Grahams, Häagen-Dazs, Helpers, Jus-Rol, Kitano, Kix, Lärabar, Latina, Liberté, Lucky Charms, Muir Glen, Nature Valley, Oatmeal Crisp, Old El Paso, Oui, Pillsbury, Progresso, Raisin Nut Bran, Total, Totino's, Trix, Wanchai Ferry, Wheaties, Wilderness, Yoki, and Yoplait trademarks. It sells its products directly, as well as through broker and distribution arrangements to grocery stores, mass merchandisers, membership stores, natural food chains, e-commerce retailers, commercial and noncommercial foodservice distributors and operators, restaurants, convenience stores, and pet specialty stores, as well as drug, dollar, and discount chains. The company operates 466 leased and 392 franchise ice cream parlors. General Mills, Inc. was founded in 1866 and is headquartered in Minneapolis, Minnesota.",
        fullTimeEmployees=35000,
        city="Minneapolis",
        state="MN",
        trailingPE=19.366043,
        dividendYield=0.0279,
        averageVolume=3548761,
        regularMarketOpen=71.14,
        volume=3699403,
        fiftyTwoWeekHigh=73.99,
        fiftyTwoWeekLow=56.67,
        recommendationKey="hold",
        industry="Packaged Foods"
    )
    db.session.add(GIS)

    GM = Stock(
        name="General Motors Company",
        ticker="GM",
        marketCap=49348722688,
        dayHigh=36.1277,
        dayLow=33.95,
        currentPrice=33.99,
        longBusinessSummary="General Motors Company designs, builds, and sells trucks, crossovers, cars, and automobile parts and accessories in North America, the Asia Pacific, the Middle East, Africa, South America, the United States, and China. The company operates through GM North America, GM International, Cruise, and GM Financial segments. It markets its vehicles primarily under the Buick, Cadillac, Chevrolet, GMC, Holden, Baojun, and Wuling brand names. The company also sells trucks, crossovers, cars, and purpose-built vehicles to dealers for consumer retail sales, as well as to fleet customers, including daily rental car companies, commercial fleet customers, leasing companies, and governments. In addition, it offers safety and security services for retail and fleet customers, including automatic crash response, emergency services, roadside assistance, crisis assist, stolen vehicle assistance, and turn-by-turn navigation; and connected services comprising mobile applications for owners to remotely control their vehicles and electric vehicle owners to locate charging stations, on-demand vehicle diagnostics, smart driver, marketplace in-vehicle commerce, in-vehicle voice, voice assistant, navigation and app ecosystem, connected navigation, SiriusXM with 360L, and 4G LTE wireless connectivity, as well as develops and commercializes autonomous vehicle technology. Further, the company provides automotive financing and insurance services; and software-enabled services and subscriptions. General Motors Company was founded in 1908 and is headquartered in Detroit, Michigan.",
        fullTimeEmployees=157000,
        city="Detroit",
        state="MI",
        trailingPE=4.548983,
        dividendYield=None,
        averageVolume=17480175,
        regularMarketOpen=35.19,
        volume=15114851,
        fiftyTwoWeekHigh=67.21,
        fiftyTwoWeekLow=30.65,
        recommendationKey="buy",
        industry="Auto Manufacturers"
    )
    db.session.add(GM)

    GPC = Stock(
        name="Genuine Parts Company",
        ticker="GPC",
        marketCap=19291060224,
        dayHigh=138.78,
        dayLow=135.15,
        currentPrice=135.45,
        longBusinessSummary="Genuine Parts Company distributes automotive replacement parts, and industrial parts and materials. It operates through Automotive Parts Group and Industrial Parts Group segments. The company distributes automotive replacement parts for hybrid and electric vehicles, trucks, SUVs, buses, motorcycles, recreational vehicles, farm vehicles, small engines, farm equipment, marine equipment, and heavy duty equipment; and accessory and supply items used by various automotive aftermarket customers, such as repair shops, service stations, fleet operators, automobile and truck dealers, leasing companies, bus and truck lines, mass merchandisers, farms, industrial concerns, and individuals. It also distributes industrial replacement parts and related supplies, such as bearings, mechanical and electrical power transmission products, industrial automation and robotics, hoses, hydraulic and pneumatic components, industrial and safety supplies, and material handling products for original equipment manufacturer, as well as maintenance, repair, and operation customers in equipment and machinery, food and beverage, forest product, primary metal, pulp and paper, mining, automotive, oil and gas, petrochemical, pharmaceutical, power generation, alternative energy, governments, transportation, ports, and other industries. In addition, the company provides various services and repairs comprising gearbox and fluid power and process pump assembly and repair, hydraulic drive shaft repair, electrical panel assembly and repair, hose and gasket manufacture and assembly, and other value-added services. It operates in the United States, Canada, France, the United Kingdom, Ireland, Germany, Poland, the Netherlands, Belgium, Australia, New Zealand, Mexico, Indonesia, and Singapore. The company was incorporated in 1928 and is headquartered in Atlanta, Georgia.",
        fullTimeEmployees=52000,
        city="Atlanta",
        state="GA",
        trailingPE=24.148687,
        dividendYield=0.026600001,
        averageVolume=787696,
        regularMarketOpen=137.47,
        volume=640318,
        fiftyTwoWeekHigh=142.97,
        fiftyTwoWeekLow=115.63,
        recommendationKey="hold",
        industry="Specialty Retail"
    )
    db.session.add(GPC)

    GILD = Stock(
        name="Gilead Sciences, Inc.",
        ticker="GILD",
        marketCap=78034976768,
        dayHigh=63.49,
        dayLow=62.13,
        currentPrice=62.21,
        longBusinessSummary="Gilead Sciences, Inc., a biopharmaceutical company, discovers, develops, and commercializes medicines in the areas of unmet medical need in the United States, Europe, and internationally. The company provides Biktarvy, Genvoya, Descovy, Odefsey, Truvada, Complera/ Eviplera, Stribild, and Atripla products for the treatment of HIV/AIDS; Veklury, an injection for intravenous use, for the treatment of coronavirus disease 2019; and Epclusa, Harvoni, Vosevi, Vemlidy, and Viread for the treatment of liver diseases. It also offers Yescarta, Tecartus, Trodelvy, and Zydelig products for the treatment of hematology, oncology, and cell therapy patients. In addition, the company provides Letairis, an oral formulation for the treatment of pulmonary arterial hypertension; Ranexa, an oral formulation for the treatment of chronic angina; and AmBisome, a liposomal formulation for the treatment of serious invasive fungal infections. Gilead Sciences, Inc. has collaboration agreements with Arcus Biosciences, Inc.; Pionyr Immunotherapeutics Inc.; Tizona Therapeutics, Inc.; Tango Therapeutics, Inc.; Jounce Therapeutics, Inc.; Galapagos NV; Janssen Sciences Ireland Unlimited Company; Japan Tobacco, Inc.; Gadeta B.V.; Bristol-Myers Squibb Company; and Merck & Co, Inc. The company was incorporated in 1987 and is headquartered in Foster City, California.",
        fullTimeEmployees=14400,
        city="Foster City",
        state="CA",
        trailingPE=10.645106,
        dividendYield=0.0468,
        averageVolume=8191243,
        regularMarketOpen=62.83,
        volume=5989598,
        fiftyTwoWeekHigh=74.12,
        fiftyTwoWeekLow=57.17,
        recommendationKey="buy",
        industry="Drug Manufacturers—General"
    )
    db.session.add(GILD)

    GL = Stock(
        name="Globe Life Inc.",
        ticker="GL",
        marketCap=9902000128,
        dayHigh=100.665,
        dayLow=97.905,
        currentPrice=98.06,
        longBusinessSummary="Globe Life Inc., through its subsidiaries, provides various life and supplemental health insurance products, and annuities to lower middle to middle income households in the United States. The company operates through four segments: Life Insurance, Supplemental Health Insurance, Annuities, and Investments. It offers whole life, term life, and other life insurance products; Medicare supplement and supplemental health insurance, such as critical illness and accident plans; and single-premium and flexible-premium deferred annuities. The company was formerly known as Torchmark Corporation and changed its name to Globe Life Inc. in August 2019. Globe Life Inc. was incorporated in 1979 and is headquartered in McKinney, Texas.",
        fullTimeEmployees=3222,
        city="McKinney",
        state="TX",
        trailingPE=13.278266,
        dividendYield=0.0086,
        averageVolume=530687,
        regularMarketOpen=100.04,
        volume=390436,
        fiftyTwoWeekHigh=108.61,
        fiftyTwoWeekLow=85.25,
        recommendationKey="hold",
        industry="Insurance—Life"
    )
    db.session.add(GL)

    GPN = Stock(
        name="Global Payments Inc.",
        ticker="GPN",
        marketCap=32888616960,
        dayHigh=119.8,
        dayLow=113.13,
        currentPrice=113.35,
        longBusinessSummary="Global Payments Inc. provides payment technology and software solutions for card, electronic, check, and digital-based payments in the Americas, Europe, and the Asia-Pacific. It operates through three segments: Merchant Solutions, Issuer Solutions, and Business and Consumer Solutions. The Merchant Solutions segment offers authorization services, settlement and funding services, customer support and help-desk functions, chargeback resolution, terminal rental, sales and deployment, payment security services, consolidated billing and statements, and on-line reporting services. This segment also provides an array of enterprise software solutions that streamline business operations of its customers in various vertical markets; and value-added services, such as point-of-sale solutions, and analytic and engagement tools, as well as payroll and human capital management services. The Issuer Solutions segment offers solutions that enable financial institutions and retailers to manage their card portfolios through a platform; and commercial payments and ePayables solutions for businesses and governments. The Business and Consumer Solutions segment provides general-purpose reloadable prepaid debit and payroll cards, demand deposit accounts, and other financial service solutions to the underbanked and other consumers, and businesses under the Netspend brand. It markets its products and services through direct sales force, trade associations, agent and enterprise software providers, referral arrangements with value-added resellers, and independent sales organizations. The company was founded in 1967 and is headquartered in Atlanta, Georgia.",
        fullTimeEmployees=25000,
        city="Atlanta",
        state="GA",
        trailingPE=35.79097,
        dividendYield=0.0082,
        averageVolume=1808875,
        regularMarketOpen=118.1,
        volume=1296418,
        fiftyTwoWeekHigh=196.88,
        fiftyTwoWeekLow=105.52,
        recommendationKey="buy",
        industry="Specialty Business Services"
    )
    db.session.add(GPN)

    GS = Stock(
        name="The Goldman Sachs Group, Inc.",
        ticker="GS",
        marketCap=99903266816,
        dayHigh=308.97,
        dayLow=299.18,
        currentPrice=299.49,
        longBusinessSummary="The Goldman Sachs Group, Inc., a financial institution, provides a range of financial services for corporations, financial institutions, governments, and individuals worldwide. It operates through four segments: Investment Banking, Global Markets, Asset Management, and Consumer & Wealth Management. The company's Investment Banking segment provides financial advisory services, including strategic advisory assignments related to mergers and acquisitions, divestitures, corporate defense activities, restructurings, and spin-offs; and middle-market lending, relationship lending, and acquisition financing, as well as transaction banking services. This segment also offers underwriting services, such as equity underwriting for common and preferred stock and convertible and exchangeable securities; and debt underwriting for various types of debt instruments, including investment-grade and high-yield debt, bank and bridge loans, and emerging-and growth-market debt, as well as originates structured securities. Its Global Markets segment is involved in client execution activities for cash and derivative instruments; credit and interest rate products; and provision of equity intermediation and equity financing, clearing, settlement, and custody services, as well as mortgages, currencies, commodities, and equities related products. The company's Asset Management segment manages assets across various classes, including equity, fixed income, hedge funds, credit funds, private equity, real estate, currencies, and commodities; and provides customized investment advisory solutions, as well as invests in corporate, real estate, and infrastructure entities. Its Consumer & Wealth Management segment offers wealth advisory and banking services, including financial planning, investment management, deposit taking, and lending; private banking; and unsecured loans, as well as accepts saving and time deposits. The company was founded in 1869 and is headquartered in New York, New York.",
        fullTimeEmployees=45100,
        city="New York",
        state="NY",
        trailingPE=4.9396334,
        dividendYield=0.026099999,
        averageVolume=2698816,
        regularMarketOpen=305.9,
        volume=2261287,
        fiftyTwoWeekHigh=426.16,
        fiftyTwoWeekLow=278.15,
        recommendationKey="buy",
        industry="Capital Markets"
    )
    db.session.add(GS)

    HAL = Stock(
        name="Halliburton Company",
        ticker="HAL",
        marketCap=29708900352,
        dayHigh=33.595,
        dayLow=32.67,
        currentPrice=33.19,
        longBusinessSummary="Halliburton Company provides products and services to the energy industry worldwide. It operates in two segments, Completion and Production, and Drilling and Evaluation. The Completion and Production segment offers production enhancement services that include stimulation and sand control services; cementing services, such as well bonding and casing, and casing equipment; completion tools that offer downhole solutions and services, including well completion products and services, intelligent well completions, and service tools, as well as liner hanger, sand control, and multilateral systems; production solutions comprising coiled tubing, hydraulic workover units, downhole tools, and pumping and nitrogen services; and pipeline and process services, such as pre-commissioning, commissioning, maintenance, and decommissioning. This segment also provides electrical submersible pumps, as well as artificial lift services. The Drilling and Evaluation segment offers drilling fluid systems, performance additives, completion fluids, solids control, specialized testing equipment, and waste management services; oilfield completion, production, and downstream water and process treatment chemicals and services; drilling systems and services; wireline and perforating services consists of open-hole logging, and cased-hole and slickline; and drill bits and services comprising roller cone rock bits, fixed cutter bits, hole enlargement, and related downhole tools and services, as well as coring equipment and services. This segment also provides cloud based digital services and artificial intelligence solutions on an open architecture for subsurface insights, integrated well construction, and reservoir and production management; testing and subsea services, such as acquisition and analysis of reservoir information and optimization solutions; and project management and integrated asset management services. Halliburton Company was founded in 1919 and is based in Houston, Texas.",
        fullTimeEmployees=40000,
        city="Houston",
        state="TX",
        trailingPE=74.25056,
        dividendYield=0.013300001,
        averageVolume=11646254,
        regularMarketOpen=33.06,
        volume=11892069,
        fiftyTwoWeekHigh=43.99,
        fiftyTwoWeekLow=17.82,
        recommendationKey="buy",
        industry="Oil & Gas Equipment & Services"
    )
    db.session.add(HAL)

    HIG = Stock(
        name="The Hartford Financial Services Group, Inc.",
        ticker="HIG",
        marketCap=22279505920,
        dayHigh=67.32,
        dayLow=65.42,
        currentPrice=65.46,
        longBusinessSummary="The Hartford Financial Services Group, Inc. provides insurance and financial services to individual and business customers in the United States, the United Kingdom, and internationally. Its Commercial Lines segment offers workers' compensation, property, automobile, liability, umbrella, bond, marine, livestock, and reinsurance; and customized insurance products and risk management services, including professional liability, bond, surety, and specialty casualty coverages through regional offices, branches, sales and policyholder service centers, independent retail agents and brokers, wholesale agents, and reinsurance brokers. The company's Personal Lines segment provides automobile, homeowners, and personal umbrella coverages through direct-to-consumer channel and independent agents. Its Property & Casualty Other Operations segment offers coverage for asbestos and environmental exposures. The company's Group Benefits segment provides group life, disability, and other group coverages to members of employer groups, associations, and affinity groups through direct insurance policies; reinsurance to other insurance companies; employer paid and voluntary product coverages; disability underwriting, administration, and claims processing to self-funded employer plans; and a single-company leave management solution. This segment distributes its group insurance products and services through brokers, consultants, third-party administrators, trade associations, and private exchanges. Its Hartford Funds segment offers investment products for retail and retirement accounts; exchange-traded products through broker-dealer organizations, independent financial advisers, defined contribution plans, financial consultants, bank trust groups, and registered investment advisers; and investment management and administrative services, such as product design, implementation, and oversight. The company was founded in 1810 and is headquartered in Hartford, Connecticut.",
        fullTimeEmployees=18100,
        city="Hartford",
        state="CT",
        trailingPE=10.89366,
        dividendYield=0.0221,
        averageVolume=1991256,
        regularMarketOpen=66.67,
        volume=1206876,
        fiftyTwoWeekHigh=78.17,
        fiftyTwoWeekLow=59.86,
        recommendationKey="buy",
        industry="Insurance—Diversified"
    )
    db.session.add(HIG)

    HAS = Stock(
        name="Hasbro, Inc.",
        ticker="HAS",
        marketCap=11613758464,
        dayHigh=86.4699,
        dayLow=84.11,
        currentPrice=84.19,
        longBusinessSummary="Hasbro, Inc., together with its subsidiaries, operates as a play and entertainment company. Its Consumer Products segment engages in the sourcing, marketing, and sale of toy and game products. This segment also promotes its brands through the out-licensing of trademarks, characters, and other brand and intellectual property rights to third parties through the sale of branded consumer products, such as toys and apparels. Its toys and games include action figures, arts and crafts and creative play products, fashion and other dolls, play sets, preschool toys, plush products, sports action blasters and accessories, vehicles and toy-related specialty products, games, and other consumer products; and licensed products, such as apparels, publishing products, home goods and electronics, and toy products. The company's Wizards of the Coast and Digital Gaming segment engages in the promotion of its brands through the development of trading card, role-playing, and digital game experiences based on Hasbro and Wizards of the Coast games. Its Entertainment segment engages in the development, acquisition, production, distribution, and sale of world-class entertainment content, including film, scripted and unscripted television, family programming, digital content, and live entertainment. The company sells its products to retailers, distributors, wholesalers, discount stores, drug stores, mail order houses, catalog stores, department stores, and other traditional retailers, as well as ecommerce retailers; and directly to customer through Hasbro PULSE e-commerce website. Hasbro, Inc. was founded in 1923 and is headquartered in Pawtucket, Rhode Island.",
        fullTimeEmployees=6640,
        city="Pawtucket",
        state="RI",
        trailingPE=25.683344,
        dividendYield=0.0304,
        averageVolume=1165516,
        regularMarketOpen=86.05,
        volume=429235,
        fiftyTwoWeekHigh=105.73,
        fiftyTwoWeekLow=78.32,
        recommendationKey="buy",
        industry="Leisure"
    )
    db.session.add(HAS)

    HCA = Stock(
        name="HCA Healthcare, Inc.",
        ticker="HCA",
        marketCap=54684065792,
        dayHigh=181.9699,
        dayLow=174.35,
        currentPrice=175.82,
        longBusinessSummary="HCA Healthcare, Inc., through its subsidiaries, provides health care services company in the United States. The company operates general and acute care hospitals that offers medical and surgical services, including inpatient care, intensive care, cardiac care, diagnostic, and emergency services; and outpatient services, such as outpatient surgery, laboratory, radiology, respiratory therapy, cardiology, and physical therapy. It also operates outpatient health care facilities consisting of freestanding ambulatory surgery centers, freestanding emergency care facilities, urgent care facilities, walk-in clinics, diagnostic and imaging centers, rehabilitation and physical therapy centers, radiation and oncology therapy centers, physician practices, and various other facilities. In addition, the company operates psychiatric hospitals, which provide therapeutic programs comprising child, adolescent and adult psychiatric care, adolescent and adult alcohol, drug abuse treatment, and counseling services. As of December 31, 2021, it operated 182 hospitals, including 175 general and acute care hospitals, five psychiatric hospitals, and two rehabilitation hospitals; 125 freestanding surgery centers; and 21 freestanding endoscopy centers in 20 states and England. The company was formerly known as HCA Holdings, Inc. HCA Healthcare, Inc. was founded in 1968 and is headquartered in Nashville, Tennessee.",
        fullTimeEmployees=204000,
        city="Nashville",
        state="TN",
        trailingPE=9.001178,
        dividendYield=0.0105,
        averageVolume=2166103,
        regularMarketOpen=180.07,
        volume=2543449,
        fiftyTwoWeekHigh=279.02,
        fiftyTwoWeekLow=169.13,
        recommendationKey="buy",
        industry="Medical Care Facilities"
    )
    db.session.add(HCA)

    PEAK = Stock(
        name="Healthpeak Properties, Inc.",
        ticker="PEAK",
        marketCap=13730163712,
        dayHigh=26.44,
        dayLow=25.45,
        currentPrice=25.47,
        longBusinessSummary="Healthpeak Properties, Inc. is a fully integrated real estate investment trust (REIT) and S&P 500 company. Healthpeak owns and develops high-quality real estate in the three private-pay healthcare asset classes of Life Science, Medical Office and Senior Housing, designed to provide stability through the inevitable industry cycles. At Healthpeak, we pair our deep understanding of the healthcare real estate market with a strong vision for long-term growth.",
        fullTimeEmployees=196,
        city="Denver",
        state="CO",
        trailingPE=22.244541,
        dividendYield=0.0399,
        averageVolume=4133233,
        regularMarketOpen=26.19,
        volume=3877970,
        fiftyTwoWeekHigh=37.69,
        fiftyTwoWeekLow=23.23,
        recommendationKey="buy",
        industry="REIT—Healthcare Facilities"
    )
    db.session.add(PEAK)

    HSIC = Stock(
        name="Henry Schein, Inc.",
        ticker="HSIC",
        marketCap=10541997056,
        dayHigh=78.595,
        dayLow=75.92,
        currentPrice=76.02,
        longBusinessSummary="Henry Schein, Inc. provides health care products and services to dental practitioners and laboratories, physician practices, government, institutional health care clinics, and other alternate care clinics worldwide. It operates through two segments, Health Care Distribution, and Technology and Value-Added Services. The Health Care Distribution segment offers dental products, including infection-control products, handpieces, preventatives, impression materials, composites, anesthetics, teeth, dental implants, gypsum, acrylics, articulators, abrasives, dental chairs, delivery units and lights, X-ray supplies and equipment, personal protective equipment, and high-tech and digital restoration equipment, as well as equipment repair services. This segment also provides medical products comprising branded and generic pharmaceuticals, vaccines, surgical products, diagnostic tests, infection-control products, X-ray products, equipment, and vitamins. The Technology and Value-Added Services segment offers software, technology, and other value-added services that include practice management software systems for dental and medical practitioners. This segment also provides value-added practice solutions, which comprise financial services on a non-recourse basis, e-services, practice technology, network, and hardware services, as well as continuing education services for practitioners, and consulting and other services. Henry Schein, Inc. was founded in 1932 and is headquartered in Melville, New York.",
        fullTimeEmployees=21600,
        city="Melville",
        state="NY",
        trailingPE=17.304802,
        dividendYield=None,
        averageVolume=862888,
        regularMarketOpen=78.07,
        volume=1612107,
        fiftyTwoWeekHigh=92.68,
        fiftyTwoWeekLow=70.25,
        recommendationKey="hold",
        industry="Medical Distribution"
    )
    db.session.add(HSIC)

    HSY = Stock(
        name="The Hershey Company",
        ticker="HSY",
        marketCap=44995391488,
        dayHigh=222.49,
        dayLow=217.75,
        currentPrice=218.42,
        longBusinessSummary="The Hershey Company, together with its subsidiaries, engages in the manufacture and sale of confectionery products and pantry items in the United States and internationally. The company operates through three segments: North America Confectionery, North America Salty Snacks, and International. It offers chocolate and non-chocolate confectionery products; gum and mint refreshment products, including mints, chewing gums, and bubble gums; pantry items, such as baking ingredients, toppings, beverages, and sundae syrups; and snack items comprising spreads, meat snacks, bars and snack bites, mixes, popcorn, and protein bars. The company provides its products primarily under the Hershey's, Reese's, Kisses, Jolly Rancher, Almond Joy, Brookside, barkTHINS, Cadbury, Good & Plenty, Heath, Kit Kat, Payday, Rolo, Twizzlers, Whoppers, York, Ice Breakers, Breath Savers, Bubble Yum, Lily's, SkinnyPop, Pirates Booty, Paqui, Dot's Homestyle Pretzels, and ONE Bar brands, as well as under the Pelon Pelo Rico, IO-IO, and Sofit brands. It markets and sells its products to wholesale distributors, chain grocery stores, mass merchandisers, chain drug stores, vending companies, wholesale clubs, convenience stores, dollar stores, concessionaires, and department stores. The company was founded in 1894 and is headquartered in Hershey, Pennsylvania.",
        fullTimeEmployees=16620,
        city="Hershey",
        state="PA",
        trailingPE=31.71022,
        dividendYield=0.016,
        averageVolume=1141762,
        regularMarketOpen=221.17,
        volume=1058931,
        fiftyTwoWeekHigh=231.6,
        fiftyTwoWeekLow=167.8,
        recommendationKey="hold",
        industry="Confectioners"
    )
    db.session.add(HSY)

    HES = Stock(
        name="Hess Corporation",
        ticker="HES",
        marketCap=34974371840,
        dayHigh=113.07,
        dayLow=109.5325,
        currentPrice=112.92,
        longBusinessSummary="Hess Corporation, an exploration and production company, explores, develops, produces, purchases, transports, and sells crude oil, natural gas liquids (NGLs), and natural gas. The company operates in two segments, Exploration and Production, and Midstream. It conducts production operations primarily in the United States, Guyana, the Malaysia/Thailand Joint Development Area, and Malaysia; and exploration activities principally offshore Guyana, the U.S. Gulf of Mexico, and offshore Suriname and Canada. The company is also involved in gathering, compressing, and processing natural gas; fractionating NGLs; gathering, terminaling, loading, and transporting crude oil and NGL through rail car; and storing and terminaling propane, as well as providing water handling services primarily in the Bakken Shale plays in the Williston Basin area of North Dakota. As of December 31, 2021, it had total proved reserves of 1,309 million barrels of oil equivalent. The company was incorporated in 1920 and is headquartered in New York, New York.",
        fullTimeEmployees=1545,
        city="New York",
        state="NY",
        trailingPE=178.38861,
        dividendYield=0.013099999,
        averageVolume=2445901,
        regularMarketOpen=110.25,
        volume=3543091,
        fiftyTwoWeekHigh=131.44,
        fiftyTwoWeekLow=61.93,
        recommendationKey="buy",
        industry="Oil & Gas E&P"
    )
    db.session.add(HES)

    HPE = Stock(
        name="Hewlett Packard Enterprise Company",
        ticker="HPE",
        marketCap=17784799232,
        dayHigh=14.285,
        dayLow=13.739,
        currentPrice=13.75,
        longBusinessSummary="Hewlett Packard Enterprise Company provides solutions that allow customers to capture, analyze, and act upon data seamlessly in the Americas, Europe, the Middle East, Africa, the Asia Pacific, and Japan. The company offers general purpose servers for multi-workload computing and workload-optimized servers; HPE ProLiant rack and tower servers; HPE BladeSystem and HPE Synergy; and solutions for secondary workloads and traditional tape, storage networking, and disk products, such as HPE Modular Storage Arrays and HPE XP. It also offers HPE Apollo and Cray products; and HPE Superdome Flex, HPE Nonstop, HPE Integrity, and HPE Edgeline products. In addition, the company provides HPE Aruba product portfolio that includes wired and wireless local area network hardware products, such as Wi-Fi access points, switches, routers, and sensors; HPE Aruba software and services comprising cloud-based management, network management, network access control, analytics and assurance, and location; and professional and support services, as well as as-a-service and consumption models for the intelligent edge portfolio of products. Further, it offers various leasing, financing, IT consumption, and utility programs and asset management services for customers to facilitate technology deployment models and the acquisition of complete IT solutions, including hardware, software, and services from Hewlett Packard Enterprise and others. Additionally, the company invests in communications and media solutions. It has a partnership with Striim, Inc. to offer high performance and mission-critical solutions with real-time analytics. It serves commercial and large enterprise groups, such as business and public sector enterprises; and through various partners comprising resellers, distribution partners, original equipment manufacturers, independent software vendors, systems integrators, and advisory firms. Hewlett Packard Enterprise Company was founded in 1939 and is headquartered in Houston, Texas.",
        fullTimeEmployees=60400,
        city="Houston",
        state="TX",
        trailingPE=5.3294578,
        dividendYield=0.0301,
        averageVolume=10995146,
        regularMarketOpen=14.2,
        volume=9095742,
        fiftyTwoWeekHigh=17.76,
        fiftyTwoWeekLow=12.99,
        recommendationKey="buy",
        industry="Communication Equipment"
    )
    db.session.add(HPE)

    HLT = Stock(
        name="Hilton Worldwide Holdings Inc.",
        ticker="HLT",
        marketCap=32131069952,
        dayHigh=121.31,
        dayLow=115.2,
        currentPrice=115.28,
        longBusinessSummary="Hilton Worldwide Holdings Inc., a hospitality company, owns, leases, manages, develops, and franchises hotels and resorts. It operates through two segments, Management and Franchise, and Ownership. The company engages in the hotel management and licensing of its brands. It operates hotels under the Waldorf Astoria Hotels & Resorts, LXR Hotels & Resorts, Conrad Hotels & Resorts, Canopy by Hilton, Tempo by Hilton, Motto by Hilton, Signia by Hilton, Hilton Hotels & Resorts, Curio Collection by Hilton, DoubleTree by Hilton, Tapestry Collection by Hilton, Embassy Suites by Hilton, Hilton Garden Inn, Hampton by Hilton, Tru by Hilton, Homewood Suites by Hilton, Home2 Suites by Hilton, and Hilton Grand Vacations. The company operates in North America, South America, and Central America, including various Caribbean nations; Europe, the Middle East, and Africa; and the Asia Pacific. As of February 16, 2022, the company had approximately 6,800 properties with 1 million rooms in 122 countries and territories. Hilton Worldwide Holdings Inc. was founded in 1919 and is headquartered in McLean, Virginia.",
        fullTimeEmployees=142000,
        city="McLean",
        state="VA",
        trailingPE=823.4286,
        dividendYield=0.0044,
        averageVolume=2370335,
        regularMarketOpen=117.87,
        volume=1805781,
        fiftyTwoWeekHigh=167.99,
        fiftyTwoWeekLow=108.71,
        recommendationKey="buy",
        industry="Lodging"
    )
    db.session.add(HLT)

    HOLX = Stock(
        name="Hologic, Inc.",
        ticker="HOLX",
        marketCap=17544157184,
        dayHigh=72.27,
        dayLow=69.705,
        currentPrice=69.78,
        longBusinessSummary="Hologic, Inc. develops, manufactures, and supplies diagnostics products, medical imaging systems, and surgical products for women's health through early detection and treatment in the United States, Europe, the Asia-Pacific, and internationally. It operates through four segments: Diagnostics, Breast Health, GYN Surgical, and Skeletal Health. The company provides Aptima molecular diagnostic assays to detect the infectious microorganisms; Aptima viral load tests for HIV, Hepatitis C, and Hepatitis B; Aptima SARS-CoV-2 and Panther Fusion SARS-CoV-2 assays for the detection of SARS-CoV-2; ThinPrep System for use in cytology applications; Rapid Fetal Fibronectin Test that assists physicians in assessing the risk of pre-term birth; and various diagnostic tests for the detection of Group B Streptococcus. It also offers breast imaging and analytics, such as 2D and 3D digital mammography systems and reading workstations, minimally invasive breast biopsy guidance systems and devices, breast biopsy site markers and localization, specimen radiology, and ultrasound and connectivity solutions; and breast conserving surgery products. In addition, the company provides NovaSure Endometrial Ablation System for the treatment of abnormal uterine bleeding; MyoSure Hysteroscopic Tissue Removal System for the removal of fibroids, polyps, and other pathology within the uterus; and Fluent Fluid Management System that provides liquid distention during diagnostic and operative hysteroscopic procedures. Further, it offers Horizon DXA, a dual energy X-ray system; and the Fluoroscan Insight FD mini C-arm to perform minimally invasive orthopedic surgical procedures. The company sells its products through direct sales and service forces, and independent distributors and sales representatives. Hologic, Inc. was incorporated in 1985 and is headquartered in Marlborough, Massachusetts.",
        fullTimeEmployees=6705,
        city="Marlborough",
        state="MA",
        trailingPE=9.678225,
        dividendYield=None,
        averageVolume=2101817,
        regularMarketOpen=71.99,
        volume=1279777,
        fiftyTwoWeekHigh=81.04,
        fiftyTwoWeekLow=66.26,
        recommendationKey="buy",
        industry="Medical Instruments & Supplies"
    )
    db.session.add(HOLX)

    HD = Stock(
        name="The Home Depot, Inc.",
        ticker="HD",
        marketCap=282101415936,
        dayHigh=285.59,
        dayLow=269.8265,
        currentPrice=270.15,
        longBusinessSummary="The Home Depot, Inc. operates as a home improvement retailer. It operates The Home Depot stores that sell various building materials, home improvement products, lawn and garden products, and décor products, as well as facilities maintenance, repair, and operations products The company also offers installation services for flooring, cabinets and cabinet makeovers, countertops, furnaces and central air systems, and windows. In addition, it provides tool and equipment rental services. The company primarily serves homeowners; and professional renovators/remodelers, general contractors, maintenance professionals, handymen, property managers, building service contractors, and specialty tradesmen, such as electricians, plumbers, and painters. It also sells its products through websites, including homedepot.com; blinds.com, an online site for custom window coverings; and thecompanystore.com, an online site for textiles and décor products. As of December 31, 2021, the company operated 2,317 stores in the United States. The Home Depot, Inc. was incorporated in 1978 and is based in Atlanta, Georgia.",
        fullTimeEmployees=490600,
        city="Atlanta",
        state="GA",
        trailingPE=18.064192,
        dividendYield=0.0257,
        averageVolume=4818759,
        regularMarketOpen=283.78,
        volume=4068691,
        fiftyTwoWeekHigh=420.61,
        fiftyTwoWeekLow=264.51,
        recommendationKey="buy",
        industry="Home Improvement Retail"
    )
    db.session.add(HD)

    HON = Stock(
        name="Honeywell International Inc.",
        ticker="HON",
        marketCap=121128017920,
        dayHigh=181.33,
        dayLow=175.75,
        currentPrice=175.95,
        longBusinessSummary="Honeywell International Inc. operates as a diversified technology and manufacturing company worldwide. Its Aerospace segment offers auxiliary power units, propulsion engines, integrated avionics, environmental control and electric power systems, engine controls, flight safety, communications, navigation hardware, data and software applications, radar and surveillance systems, aircraft lighting, advanced systems and instruments, satellite and space components, and aircraft wheels and brakes; spare parts; repair, overhaul, and maintenance services; thermal systems, as well as wireless connectivity and management services. The company's Honeywell Building Technologies segment offers software applications for building control and optimization; sensors, switches, control systems, and instruments for energy management; access control; video surveillance; fire products; and installation, maintenance, and upgrades of systems. Its Performance Materials and Technologies segment offers automation control, instrumentation, and software and related services; catalysts and adsorbents, equipment, and consulting; and materials to manufacture end products, such as bullet-resistant armor, nylon, computer chips, and pharmaceutical packaging, as well as provides reduced and low global-warming-potential materials based on hydrofluoro-olefin technology. The company's Safety and Productivity Solutions segment provides personal protection equipment, apparel, gear, and footwear; gas detection technology; cloud-based notification and emergency messaging; mobile devices and software; supply chain and warehouse automation equipment, and software solutions; custom-engineered sensors, switches, and controls; and data and asset management productivity software solutions. The company was founded in 1906 and is headquartered in Charlotte, North Carolina.",
        fullTimeEmployees=99000,
        city="Charlotte",
        state="NC",
        trailingPE=22.644787,
        dividendYield=0.020299999,
        averageVolume=3251448,
        regularMarketOpen=179.47,
        volume=3181187,
        fiftyTwoWeekHigh=236.86,
        fiftyTwoWeekLow=172.92,
        recommendationKey="buy",
        industry="Conglomerates"
    )
    db.session.add(HON)

    HRL = Stock(
        name="Hormel Foods Corporation",
        ticker="HRL",
        marketCap=25549621248,
        dayHigh=47.9,
        dayLow=47.03,
        currentPrice=47.09,
        longBusinessSummary="Hormel Foods Corporation develops, processes, and distributes various meat, nuts, and food products to retail, foodservice, deli, and commercial customers in the United States and internationally. The company operates through four segments: Grocery Products, Refrigerated Foods, Jennie-O Turkey Store, and International & Other. It provides various perishable products that include fresh meats, frozen items, refrigerated meal solutions, sausages, hams, guacamoles, and bacons; and shelf-stable products comprising canned luncheon meats, nut butters, snack nuts, chilies, shelf-stable microwaveable meals, hashes, stews, tortillas, salsas, tortilla chips, and others. The company also engages in the processing, marketing, and sale of branded and unbranded pork, beef, poultry, and turkey products, as well as offers nutritional food products and supplements, desserts and drink mixes, and industrial gelatin products. It sells its products primarily under the SKIPPY, SPAM, Hormel, Natural Choice, Applegate, Justin's, Jennie-O, Café H, Herdez, Black Label, Sadler's, Columbus, Gatherings, Herdez, Wholly, Columbus, Planters, NUT-rition, Planters Cheez Balls, Corn Nuts, etc. brand names through sales personnel, independent brokers, and distributors. The company was formerly known as Geo. A. Hormel & Company and changed its name to Hormel Foods Corporation in January 1995. Hormel Foods Corporation was founded in 1891 and is headquartered in Austin, Minnesota.",
        fullTimeEmployees=20000,
        city="Austin",
        state="MN",
        trailingPE=28.36747,
        dividendYield=0.0195,
        averageVolume=1876922,
        regularMarketOpen=47.69,
        volume=1202802,
        fiftyTwoWeekHigh=55.11,
        fiftyTwoWeekLow=40.48,
        recommendationKey="hold",
        industry="Packaged Foods"
    )
    db.session.add(HRL)

    HWM = Stock(
        name="Howmet Aerospace Inc.",
        ticker="HWM",
        marketCap=13619708928,
        dayHigh=32.78,
        dayLow=31.77,
        currentPrice=31.88,
        longBusinessSummary="Howmet Aerospace Inc. provides advanced engineered solutions for the aerospace and transportation industries in the United States, Japan, France, Germany, the United Kingdom, Mexico, Italy, Canada, Poland, China, and internationally. It operates through four segments: Engine Products, Fastening Systems, Engineered Structures, and Forged Wheels. The Engine Products segment offers airfoils and seamless rolled rings primarily for aircraft engines and industrial gas turbines; and rotating parts, as well as structural parts. The Fastening Systems segment produces aerospace fastening systems, as well as commercial transportation, industrial, and other fasteners. The Engineered Structures segment provides titanium ingots and mill products for aerospace and defense applications; and aluminum and nickel forgings, and machined components and assemblies. The Forged Wheels segment offers forged aluminum wheels and related products for heavy-duty trucks and commercial transportation markets. The company was formerly known as Arconic Inc. The company was founded in 1888 and is based in Pittsburgh, Pennsylvania.",
        fullTimeEmployees=19900,
        city="Pittsburgh",
        state="PA",
        trailingPE=48.229954,
        dividendYield=0.0023999999,
        averageVolume=2529320,
        regularMarketOpen=32.1,
        volume=1686696,
        fiftyTwoWeekHigh=37.66,
        fiftyTwoWeekLow=27.41,
        recommendationKey="buy",
        industry="Specialty Industrial Machinery"
    )
    db.session.add(HWM)

    HPQ = Stock(
        name="HP Inc.",
        ticker="HPQ",
        marketCap=37288873984,
        dayHigh=35.7,
        dayLow=34.18,
        currentPrice=34.44,
        longBusinessSummary="HP Inc. provides personal computing and other access devices, imaging and printing products, and related technologies, solutions, and services in the United States and internationally. The company operates through three segments: Personal Systems, Printing, and Corporate Investments. The Personal Systems segment offers commercial and consumer desktop and notebook personal computers, workstations, thin clients, commercial mobility devices, retail point-of-sale systems, displays and peripherals, software, support, and services. The Printing segment provides consumer and commercial printer hardware, supplies, solutions, and services. The Corporate Investments segment is involved in the HP Labs and business incubation, and investment projects. It serves individual consumers, small- and medium-sized businesses, and large enterprises, including customers in the government, health, and education sectors. The company was formerly known as Hewlett-Packard Company and changed its name to HP Inc. in October 2015. HP Inc. was founded in 1939 and is headquartered in Palo Alto, California.",
        fullTimeEmployees=51000,
        city="Palo Alto",
        state="CA",
        trailingPE=6.4615383,
        dividendYield=0.0272,
        averageVolume=13492380,
        regularMarketOpen=35.41,
        volume=7226032,
        fiftyTwoWeekHigh=41.47,
        fiftyTwoWeekLow=26.11,
        recommendationKey="hold",
        industry="Computer Hardware"
    )
    db.session.add(HPQ)

    HUM = Stock(
        name="Humana Inc.",
        ticker="HUM",
        marketCap=59407130624,
        dayHigh=477.44,
        dayLow=461.58,
        currentPrice=462.19,
        longBusinessSummary="Humana Inc., together with its subsidiaries, operates as a health and well-being company in the United States. It operates through three segments: Retail, Group and Specialty, and Healthcare Services. The company offers medical and supplemental benefit plans to individuals. It also has a contract with Centers for Medicare and Medicaid Services to administer the Limited Income Newly Eligible Transition prescription drug plan program; and contracts with various states to provide Medicaid, dual eligible, and long-term support services benefits. In addition, the company provides commercial fully insured medical and specialty health insurance benefits comprising dental, vision, and other supplemental health benefits; and administrative services only products to individuals and employer groups, as well as military services, such as TRICARE T2017 East Region contract. Further, it offers pharmacy solutions, provider services, and home solutions services, such as home health and other services to its health plan members, as well as to third parties. As of December 31, 2021, the company had approximately 17 million members in medical benefit plans, as well as approximately 5 million members in specialty products. Humana Inc. was founded in 1961 and is headquartered in Louisville, Kentucky.",
        fullTimeEmployees=95500,
        city="Louisville",
        state="KY",
        trailingPE=22.53596,
        dividendYield=0.0072000003,
        averageVolume=876833,
        regularMarketOpen=466.93,
        volume=900138,
        fiftyTwoWeekHigh=477.44,
        fiftyTwoWeekLow=351.2,
        recommendationKey="buy",
        industry="Healthcare Plans"
    )
    db.session.add(HUM)

    HBAN = Stock(
        name="Huntington Bancshares Incorporated",
        ticker="HBAN",
        marketCap=18107351040,
        dayHigh=12.645,
        dayLow=12.27,
        currentPrice=12.28,
        longBusinessSummary="Huntington Bancshares Incorporated operates as the bank holding company for The Huntington National Bank that provides commercial, consumer, and mortgage banking services in the United States. The company operates through four segments: Consumer and Business Banking; Commercial Banking; Vehicle Finance; and Regional Banking and The Huntington Private Client Group (RBHPCG). The Consumer and Business Banking segment offers financial products and services, such as checking accounts, savings accounts, money market accounts, certificates of deposit, credit cards, and consumer and small business loans, as well as investment products. This segment also provides mortgages, insurance, interest rate risk protection, foreign exchange, automated teller machine, and treasury management services, as well as online, mobile, and telephone banking services. It serves consumer and small business customers. The Commercial Banking segment offers regional commercial banking solutions for middle market businesses, government and public sector entities, and commercial real estate developers/REITs; and specialty banking solutions for healthcare, technology and telecommunications, franchise finance, sponsor finance, and global services industries. It also provides asset finance services; capital raising solutions, sales and trading, and corporate risk management products; institutional banking services; and treasury management services. The Vehicle Finance segment provides financing to consumers for the purchase of automobiles, light-duty trucks, recreational vehicles, and marine craft at franchised and other select dealerships, as well as to franchised dealerships for the acquisition of new and used inventory. The RBHPCG segment offers private banking, wealth and investment management, and retirement plan services. As of March 18, 2022, the company had approximately 1,000 branches in 11 states. Huntington Bancshares Incorporated was founded in 1866 and is headquartered in Columbus, Ohio.",
        fullTimeEmployees=19722,
        city="Columbus",
        state="OH",
        trailingPE=13.766815,
        dividendYield=0.0475,
        averageVolume=13211198,
        regularMarketOpen=12.56,
        volume=10036550,
        fiftyTwoWeekHigh=17.79,
        fiftyTwoWeekLow=11.73,
        recommendationKey="buy",
        industry="Banks—Regional"
    )
    db.session.add(HBAN)

    HII = Stock(
        name="Huntington Ingalls Industries, Inc.",
        ticker="HII",
        marketCap=8700447744,
        dayHigh=222.475,
        dayLow=215.82,
        currentPrice=217.18,
        longBusinessSummary="Huntington Ingalls Industries, Inc. engages in designing, building, overhauling, and repairing military ships in the United States. It operates through three segments: Ingalls Shipbuilding, Newport News Shipbuilding, and Technical Solutions. The company is involved in the design and construction of non-nuclear ships comprising amphibious assault ships; expeditionary warfare ships; surface combatants; and national security cutters for the U.S. Navy and U.S. Coast Guard. It also provides nuclear-powered ships, such as aircraft carriers and submarines, as well as refueling and overhaul, and inactivation services of ships. In addition, the company offers naval nuclear support services, including fleet services comprising design, construction, maintenance, and disposal activities for in-service the U.S. Navy nuclear ships; and maintenance services on nuclear reactor prototypes. Further, it provides life-cycle sustainment services to the U.S. Navy fleet and other maritime customers; high-end information technology and mission-based solutions for Department of Defense (DoD), intelligence, and federal civilian customers; nuclear management and operations and environmental management services for the Department of Energy, DoD, state and local governments, and private sector companies; defense and federal solutions; and unmanned systems. Huntington Ingalls Industries, Inc. was founded in 1886 and is headquartered in Newport News, Virginia.",
        fullTimeEmployees=44000,
        city="Newport News",
        state="VA",
        trailingPE=13.0297575,
        dividendYield=0.0232,
        averageVolume=384259,
        regularMarketOpen=219.46,
        volume=385978,
        fiftyTwoWeekHigh=228.66,
        fiftyTwoWeekLow=175.5,
        recommendationKey="hold",
        industry="Aerospace & Defense"
    )
    db.session.add(HII)

    IBM = Stock(
        name="International Business Machines Corporation",
        ticker="IBM",
        marketCap=127151955968,
        dayHigh=144.155,
        dayLow=141.35,
        currentPrice=141.86,
        longBusinessSummary="International Business Machines Corporation provides integrated solutions and services worldwide. The company operates through four business segments: Software, Consulting, Infrastructure, and Financing. The Software segment offers hybrid cloud platform and software solutions, such as Red Hat, an enterprise open-source solutions; software for business automation, AIOps and management, integration, and application servers; data and artificial intelligence solutions; and security software and services for threat, data, and identity. This segment also provides transaction processing software that supports clients' mission-critical and on-premise workloads in banking, airlines, and retail industries. The Consulting segment offers business transformation services, including strategy, business process design and operations, data and analytics, and system integration services; technology consulting services; and application and cloud platform services. The Infrastructure segment provides on-premises and cloud-based server and storage solutions for its clients' mission-critical and regulated workloads; and support services and solutions for hybrid cloud infrastructure, as well as remanufacturing and remarketing services for used equipment. The Financing segment offers lease, installment payment, loan financing, and short-term working capital financing services. The company was formerly known as Computing-Tabulating-Recording Co. International Business Machines Corporation was incorporated in 1911 and is headquartered in Armonk, New York.",
        fullTimeEmployees=282100,
        city="Armonk",
        state="NY",
        trailingPE=26.852167,
        dividendYield=0.0494,
        averageVolume=5234998,
        regularMarketOpen=142.92,
        volume=4065202,
        fiftyTwoWeekHigh=144.73,
        fiftyTwoWeekLow=114.56,
        recommendationKey="hold",
        industry="Information Technology Services"
    )
    db.session.add(IBM)

    IEX = Stock(
        name="IDEX Corporation",
        ticker="IEX",
        marketCap=13749536768,
        dayHigh=186.215,
        dayLow=180.72,
        currentPrice=180.84,
        longBusinessSummary="IDEX Corporation, together with its subsidiaries, provides applied solutions worldwide. The company operates through three segments: Fluid & Metering Technologies (FMT), Health & Science Technologies (HST), and Fire & Safety/Diversified Products (FSDP). The FMT segment designs, produces, and distributes positive displacement pumps, small volume provers, flow meters, injectors, and other fluid-handling pump modules and systems, as well as offers flow monitoring and other services for the food, chemical, general industrial, water and wastewater, agricultural, and energy industries. The HST segment designs, produces, and distributes precision fluidics, rotary lobe pumps, centrifugal and positive displacement pumps, roll compaction and drying systems, pneumatic components and sealing solutions, high performance molded and extruded sealing components, custom mechanical and shaft seals, engineered hygienic mixers and valves, biocompatible medical devices and implantables, air compressors and blowers, optical components and coatings, laboratory and commercial equipment, precision photonic solutions, and precision gear and peristaltic pump technologies. This segment serves food and beverage, pharmaceutical and biopharmaceutical, cosmetics, marine, chemical, wastewater and water treatment, life sciences, research, and defense markets. The FSDP segment designs, produces, and distributes firefighting pumps, valves and controls, rescue tools, lifting bags, and other components and systems for the fire and rescue industry; engineered stainless steel banding and clamping devices for various industrial and commercial applications; and precision equipment for dispensing, metering, and mixing colorants and paints used in retail and commercial businesses. IDEX Corporation was incorporated in 1987 and is headquartered in Northbrook, Illinois.",
        fullTimeEmployees=7500,
        city="Northbrook",
        state="IL",
        trailingPE=32.1322,
        dividendYield=0.0128999995,
        averageVolume=435204,
        regularMarketOpen=184.27,
        volume=318908,
        fiftyTwoWeekHigh=240.33,
        fiftyTwoWeekLow=172.19,
        recommendationKey="buy",
        industry="Specialty Industrial Machinery"
    )
    db.session.add(IEX)

    IDXX = Stock(
        name="IDEXX Laboratories, Inc.",
        ticker="IDXX",
        marketCap=29610772480,
        dayHigh=363.85,
        dayLow=347.915,
        currentPrice=349.21,
        longBusinessSummary="IDEXX Laboratories, Inc. develops, manufactures, and distributes products and services primarily for the companion animal veterinary, livestock and poultry, dairy, and water testing markets worldwide. The company operates through CAG; Water Quality Products; LPD; and Other segments. It provides point-of-care veterinary diagnostic products, including instruments, consumables, and rapid assay test kits; veterinary reference laboratory diagnostic and consulting services; practice management and diagnostic imaging systems and services for veterinarians; and health monitoring, biological materials testing, and laboratory animal diagnostic instruments and services for biomedical research community. The company also offers diagnostic and health-monitoring products for livestock, poultry, and dairy; products that test water for various microbiological contaminants; and point-of-care electrolytes and blood gas analyzers and SARS-CoV-2 RT-PCR that are used in the human point-of-care medical diagnostics market; in-clinic chemistry, blood and urine chemistry, hematology, and SediVue Dx analyzers; SNAP rapid assays test kits. In addition, it provides Colilert, Colilert-18, and Colisure tests, which detect the presence of total coliforms and E. coli in water; Enterolert, Pseudalert, Filta-Max and Filta-Max xpress, Legiolert, and Quanti-Tray products; veterinary software and services for independent veterinary clinics and corporate groups. The company markets its products through marketing, customer service, sales, and technical service groups, as well as through independent distributors and other resellers. IDEXX Laboratories, Inc. was incorporated in 1983 and is headquartered in Westbrook, Maine.",
        fullTimeEmployees=10350,
        city="Westbrook",
        state="ME",
        trailingPE=40.056202,
        dividendYield=None,
        averageVolume=698345,
        regularMarketOpen=360.23,
        volume=431049,
        fiftyTwoWeekHigh=706.95,
        fiftyTwoWeekLow=318.5,
        recommendationKey="buy",
        industry="Diagnostics & Research"
    )
    db.session.add(IDXX)

    ITW = Stock(
        name="Illinois Tool Works Inc.",
        ticker="ITW",
        marketCap=57437085696,
        dayHigh=189.505,
        dayLow=182.625,
        currentPrice=182.99,
        longBusinessSummary="Illinois Tool Works Inc. manufactures and sells industrial products and equipment worldwide. It operates through seven segments: Automotive OEM; Food Equipment; Test & Measurement and Electronics; Welding; Polymers & Fluids; Construction Products; and Specialty Products. The Automotive OEM segment offers plastic and metal components, fasteners, and assemblies for automobiles, light trucks, and other industrial uses. The Food Equipment segment provides warewashing, refrigeration, cooking, and food processing equipment; kitchen exhaust, ventilation, and pollution control systems; and food equipment maintenance and repair services. The Test & Measurement and Electronics segment produces and sells equipment, consumables, and related software for testing and measuring of materials and structures, as well as equipment and consumables used in the production of electronic subassemblies and microelectronics. The Welding segment produces arc welding equipment; and metal arc welding consumables and related accessories. The Polymers & Fluids segment produces adhesives, sealants, lubrication and cutting fluids, and fluids and polymers for auto aftermarket maintenance and appearance. The Construction Products segment offers engineered fastening systems and solutions for the residential construction, renovation/remodel, and commercial construction markets. The Specialty Products segment offers beverage packaging equipment and consumables, product coding and marking equipment and consumables, and appliance components and fasteners. It serves the automotive OEM/tiers, commercial food equipment, construction, general industrial, and automotive aftermarket end markets. The company distributes its products directly to industrial manufacturers, as well as through independent distributors. Illinois Tool Works Inc. was founded in 1912 and is based in Glenview, Illinois.",
        fullTimeEmployees=45000,
        city="Glenview",
        state="IL",
        trailingPE=21.280382,
        dividendYield=0.0235,
        averageVolume=1163274,
        regularMarketOpen=188.2,
        volume=979261,
        fiftyTwoWeekHigh=249.81,
        fiftyTwoWeekLow=177.33,
        recommendationKey="hold",
        industry="Specialty Industrial Machinery"
    )
    db.session.add(ITW)

    ILMN = Stock(
        name="Illumina, Inc.",
        ticker="ILMN",
        marketCap=29295308800,
        dayHigh=196.8144,
        dayLow=187.37,
        currentPrice=187.43,
        longBusinessSummary="Illumina, Inc. provides sequencing and array-based solutions for genetic and genomic analysis. Its products and services serve customers in a range of markets enabling the adoption of genomic solutions in research and clinical settings for applications in the life sciences, oncology, reproductive health, agriculture, and other emerging segments. The company provides instruments and consumables used in genetic analysis; and genotyping and sequencing services, instrument service contracts, and development and licensing agreements, as well as cancer detection testing services. Its customers include genomic research centers, academic institutions, government laboratories, and hospitals, as well as pharmaceutical, biotechnology, commercial molecular diagnostic laboratories, and consumer genomics companies. The company markets and distributes its products directly to customers in North America, Europe, Latin America, and the Asia-Pacific region, as well as sells through life-science distributors in various markets within Europe, the Asia-Pacific region, Latin America, the Middle East, and Africa. The company was incorporated in 1998 and is based in San Diego, California.",
        fullTimeEmployees=9800,
        city="San Diego",
        state="CA",
        trailingPE=30.68096,
        dividendYield=None,
        averageVolume=1328350,
        regularMarketOpen=194.66,
        volume=1506569,
        fiftyTwoWeekHigh=526,
        fiftyTwoWeekLow=180,
        recommendationKey="hold",
        industry="Diagnostics & Research"
    )
    db.session.add(ILMN)

    INCY = Stock(
        name="Incyte Corporation",
        ticker="INCY",
        marketCap=16705986560,
        dayHigh=77.63,
        dayLow=75.03,
        currentPrice=75.63,
        longBusinessSummary="Incyte Corporation, a biopharmaceutical company, focuses on the discovery, development, and commercialization of proprietary therapeutics in the United States and internationally. The company offers JAKAFI, a drug for the treatment of myelofibrosis and polycythemia vera; PEMAZYRE, a fibroblast growth factor receptor kinase inhibitor that act as oncogenic drivers in various liquid and solid tumor types; and ICLUSIG, a kinase inhibitor to treat chronic myeloid leukemia and philadelphia-chromosome positive acute lymphoblastic leukemia. Its clinical stage products include ruxolitinib, a steroid-refractory chronic graft-versus-host-diseases (GVHD); itacitinib, which is in Phase II/III clinical trial to treat naïve chronic GVHD; and pemigatinib for treating bladder cancer, cholangiocarcinoma, myeloproliferative syndrome, and tumor agnostic. In addition, the company engages in developing Parsaclisib, which is in Phase II clinical trial for follicular lymphoma, marginal zone lymphoma, and mantel cell lymphoma. Additionally, it develops Retifanlimab that is in Phase II clinical trials for MSI-high endometrial cancer, merkel cell carcinoma, and anal cancer, as well as in Phase II clinical trials for patients with non-small cell lung cancer. It has collaboration agreements with Novartis International Pharmaceutical Ltd.; Eli Lilly and Company; Agenus Inc.; Calithera Biosciences, Inc; MacroGenics, Inc.; Merus N.V.; Syros Pharmaceuticals, Inc.; Innovent Biologics, Inc.; Zai Lab Limited; Cellenkos, Inc.; and Nimble Therapeutics, as well as clinical collaborations with MorphoSys AG and Xencor, Inc. to investigate the combination of tafasitamab, plamotamab, and lenalidomide in patients with relapsed or refractory diffuse large B-cell lymphoma, and relapsed or refractory follicular lymphoma. The company was incorporated in 1991 and is headquartered in Wilmington, Delaware.",
        fullTimeEmployees=2094,
        city="Wilmington",
        state="DE",
        trailingPE=31.35572,
        dividendYield=None,
        averageVolume=1443782,
        regularMarketOpen=77.32,
        volume=952847,
        fiftyTwoWeekHigh=84.99,
        fiftyTwoWeekLow=61.91,
        recommendationKey="buy",
        industry="Biotechnology"
    )
    db.session.add(INCY)

    IR = Stock(
        name="Ingersoll Rand Inc.",
        ticker="IR",
        marketCap=17448714240,
        dayHigh=44.04,
        dayLow=42.76,
        currentPrice=42.81,
        longBusinessSummary="Ingersoll Rand Inc. provides various mission-critical air, fluid, energy, specialty vehicle and medical technologies in the United States, Europe, the Middle East, Africa, and the Asia Pacific. It operates through two segments, Industrial Technologies and Services, and Precision and Science Technologies. The Industrial Technologies and Services segment designs, manufactures, markets, and services various air and gas compression, vacuum, and blower products; fluid transfer equipment and loading systems; and power tools and lifting equipment, including associated aftermarket parts, consumables, air treatment equipment, controls, other accessories, and services. The Precision and Science Technologies segment designs, manufactures, and markets a range of specialized positive displacement pumps, fluid management systems, accessories and aftermarket parts for liquid and gas dosing, transfer, dispensing, compression, sampling, pressure management and flow control in specialized or critical applications. The company's products are used in medical, laboratory, industrial manufacturing, water and wastewater, chemical processing, precision irrigation, energy, food and beverage, agriculture, and vacuum and automated liquid handling end-markets, as well as various manufacturing and industrial facilities applications. It sells through an integrated network of direct sales representatives and independent distributors under the Ingersoll Rand, Gardner Denver, Club Car, CompAir, Nash, Elmo Rietschle, Robuschi, Thomas, Milton Roy, Seepex, ARO, Emco Wheaton, Runtech Systems, Air Dimensions, Albin, Dosatron, Haskel, LMI, Maximus, MP, Oberdorfer, Welch, Williams, Zinnser Analytic, and YZ brands. The company was formerly known as Gardner Denver Holdings, Inc. and changed its name to Ingersoll Rand Inc. in March 2020. Ingersoll Rand Inc. was founded in 1859 and is headquartered in Davidson, North Carolina.",
        fullTimeEmployees=16000,
        city="Davidson",
        state="NC",
        trailingPE=43.373863,
        dividendYield=0.0019,
        averageVolume=2853440,
        regularMarketOpen=43.77,
        volume=1845270,
        fiftyTwoWeekHigh=62.64,
        fiftyTwoWeekLow=40.4,
        recommendationKey="buy",
        industry="Specialty Industrial Machinery"
    )
    db.session.add(IR)

    INTC = Stock(
        name="Intel Corporation",
        ticker="INTC",
        marketCap=153651265536,
        dayHigh=39.02,
        dayLow=37.74,
        currentPrice=37.78,
        longBusinessSummary="Intel Corporation engages in the design, manufacture, and sale of computer products and technologies worldwide. The company operates through CCG, DCG, IOTG, Mobileye, NSG, PSG, and All Other segments. It offers platform products, such as central processing units and chipsets, and system-on-chip and multichip packages; and non-platform or adjacent products, including accelerators, boards and systems, connectivity products, graphics, and memory and storage products. The company also provides high-performance compute solutions for targeted verticals and embedded applications for retail, industrial, and healthcare markets; and solutions for assisted and autonomous driving comprising compute platforms, computer vision and machine learning-based sensing, mapping and localization, driving policy, and active sensors. In addition, it offers workload-optimized platforms and related products for cloud service providers, enterprise and government, and communications service providers. The company serves original equipment manufacturers, original design manufacturers, and cloud service providers. Intel Corporation has a strategic partnership with MILA to develop and apply advances in artificial intelligence methods for enhancing the search in the space of drugs. The company was incorporated in 1968 and is headquartered in Santa Clara, California.",
        fullTimeEmployees=122900,
        city="Santa Clara",
        state="CA",
        trailingPE=7.324544,
        dividendYield=0.0335,
        averageVolume=35542388,
        regularMarketOpen=38.58,
        volume=37842731,
        fiftyTwoWeekHigh=57.46,
        fiftyTwoWeekLow=36.6,
        recommendationKey="hold",
        industry="Semiconductors"
    )
    db.session.add(INTC)

    ICE = Stock(
        name="Intercontinental Exchange, Inc.",
        ticker="ICE",
        marketCap=54509338624,
        dayHigh=99.36,
        dayLow=96.71,
        currentPrice=96.75,
        longBusinessSummary="Intercontinental Exchange, Inc., together with its subsidiaries, operates regulated exchanges, clearing houses, and listings venues for commodity, financial, fixed income, and equity markets in the United States, the United Kingdom, the European Union, Singapore, Israel, and Canada. It operates through three segments: Exchanges, Fixed Income and Data Services, and Mortgage Technology. The company operates marketplaces for listing, trading, and clearing an array of derivatives contracts and financial securities, such as commodities, interest rates, foreign exchange, and equities, as well as corporate and exchange-traded funds; trading venues, including 13 regulated exchanges and 6 clearing houses; and offers futures and options products for energy, agricultural and metals, financial, cash equities and equity, over-the-counter, and other markets, as well as listings and data and connectivity services. It also provides fixed income data and analytic, fixed income execution, CDS clearing, and other multi-asset class data and network services. In addition, the company offers proprietary and comprehensive mortgage origination platform, which serves residential mortgage loans; closing solutions that provides customers connectivity to the mortgage supply chain and facilitates the secure exchange of information; data and analytics services; and Data as a Service for lenders to access data and origination information. Intercontinental Exchange, Inc. was founded in 2000 and is headquartered in Atlanta, Georgia.",
        fullTimeEmployees=8858,
        city="Atlanta",
        state="GA",
        trailingPE=17.847261,
        dividendYield=0.0155,
        averageVolume=3624941,
        regularMarketOpen=98.69,
        volume=2993864,
        fiftyTwoWeekHigh=139.79,
        fiftyTwoWeekLow=90.05,
        recommendationKey="buy",
        industry="Financial Data & Stock Exchanges"
    )
    db.session.add(ICE)

    IP = Stock(
        name="International Paper Company",
        ticker="IP",
        marketCap=16396716032,
        dayHigh=43.4,
        dayLow=42.23,
        currentPrice=42.34,
        longBusinessSummary="International Paper Company operates as a packaging company primarily in United States, the Middle East, Europe, Africa, Pacific Rim, Asia, and rest of the Americas. It operates through two segments: Industrial Packaging and Global Cellulose Fibers. The Industrial Packaging segment manufactures containerboards, including linerboard, medium, whitetop, recycled linerboard, recycled medium, and saturating kraft. The Global Cellulose Fibers segment provides fluff, market, and specialty pulps that are used in absorbent hygiene products, such as baby diapers, feminine care, adult incontinence, and other non-woven products; tissue and paper products; and non-absorbent end applications, including textiles, filtration, construction material, paints and coatings, reinforced plastics, and other applications. It sells its products directly to end users and converters, as well as through agents, resellers, and paper distributors. The company was founded in 1898 and is headquartered in Memphis, Tennessee.",
        fullTimeEmployees=38000,
        city="Memphis",
        state="TN",
        trailingPE=9.323937,
        dividendYield=0.0387,
        averageVolume=3001767,
        regularMarketOpen=42.84,
        volume=2805313,
        fiftyTwoWeekHigh=59.375,
        fiftyTwoWeekLow=40.42,
        recommendationKey="hold",
        industry="Packaging & Containers"
    )
    db.session.add(IP)

    IPG = Stock(
        name="The Interpublic Group of Companies, Inc.",
        ticker="IPG",
        marketCap=10820387840,
        dayHigh=28.42,
        dayLow=27.455,
        currentPrice=27.48,
        longBusinessSummary="The Interpublic Group of Companies, Inc. provides advertising and marketing services worldwide. It operates in two segments, Integrated Agency Networks (IAN) and IPG DXTRA. The company offers consumer advertising, digital marketing, communications planning and media buying, public relations, and specialized communications disciplines, as well as data science services. It also provides various diversified services, including meeting and event production, sports and entertainment marketing, corporate and brand identity, and strategic marketing consulting. The company was formerly known as McCann-Erickson Incorporated and changed its name to The Interpublic Group of Companies, Inc. in January 1961. The Interpublic Group of Companies, Inc. was founded in 1902 and is headquartered in New York, New York.",
        fullTimeEmployees=55600,
        city="New York",
        state="NY",
        trailingPE=15.516657,
        dividendYield=0.0361,
        averageVolume=3455835,
        regularMarketOpen=28.35,
        volume=2716467,
        fiftyTwoWeekHigh=39.98,
        fiftyTwoWeekLow=26.43,
        recommendationKey="buy",
        industry="Advertising Agencies"
    )
    db.session.add(IPG)

    IFF = Stock(
        name="International Flavors & Fragrances Inc.",
        ticker="IFF",
        marketCap=29703090176,
        dayHigh=120.945,
        dayLow=116.64,
        currentPrice=116.69,
        longBusinessSummary="International Flavors & Fragrances Inc., together with its subsidiaries, manufactures and sells cosmetic active and natural health ingredients for use in various consumer products in Europe, Africa, the Middle East, Greater Asia, North America, and Latin America. It operates through Nourish, Scent, Health & Biosciences, and Pharma Solutions segments. The Nourish segment offers natural and plant-based specialty food ingredients, such as flavor compounds, and savory solutions and inclusions. It also provides natural food protection ingredients consist of natural antioxidants and anti-microbials as well as beverages, sweets , and dairy products. The Scent segment provides fragrance compounds, which include fine fragrances comprising perfumes and colognes, as well as consumer fragrances; fragrance ingredients comprising synthetic and natural ingredients that could be combined with other materials to create fragrance and consumer compounds; and cosmetic active ingredients consisting of active and functional ingredients, botanicals, and delivery systems to support its customers' cosmetic and personal care product lines. The Health & Biosciences segment develops and produces enzymes, food cultures, probiotics, and specialty ingredients. The Pharma Solutions segment produces and sells cellulosics and seaweed-based pharma excipients. The company sells its products primarily to manufacturers of perfumes and cosmetics, hair and other personal care products, soaps and detergents, cleaning products, dairy, meat and other processed foods, beverages, snacks and savory foods, sweet and baked goods, dietary supplements, infant and elderly nutrition, functional food, and pharmaceutical excipients and oral care products. International Flavors & Fragrances Inc. was founded in 1833 and is headquartered in New York, New York.",
        fullTimeEmployees=24000,
        city="New York",
        state="NY",
        trailingPE=99.991425,
        dividendYield=0.0239,
        averageVolume=1409001,
        regularMarketOpen=120.31,
        volume=979830,
        fiftyTwoWeekHigh=157.08,
        fiftyTwoWeekLow=105.38,
        recommendationKey="none",
        industry="Specialty Chemicals"
    )
    db.session.add(IFF)

    INTU = Stock(
        name="Intuit Inc.",
        ticker="INTU",
        marketCap=109384589312,
        dayHigh=409.25,
        dayLow=384.5,
        currentPrice=386.29,
        longBusinessSummary="Intuit Inc. provides financial management and compliance products and services for consumers, small businesses, self-employed, and accounting professionals in the United States, Canada, and internationally. The company operates in four segments: Small Business & Self-Employed, Consumer, Credit Karma, and ProConnect. The Small Business & Self-Employed segment provides QuickBooks online services and desktop software solutions comprising QuickBooks Online Advanced, a cloud-based solution; QuickBooks Enterprise, a hosted solution; QuickBooks Self-Employed solution; QuickBooks Commerce, a solution for product-based businesses; QuickBooks Online Accountant and QuickBooks Accountant Desktop Plus solutions; and payroll solutions, such as online payroll processing, direct deposit of employee paychecks, payroll reports, electronic payment of federal and state payroll taxes, and electronic filing of federal and state payroll tax forms. This segment also offers payment-processing solutions, including credit and debit cards, Apple Pay, and ACH payment services; QuickBooks Cash business bank account; and financial supplies and financing for small businesses. The Consumer segment provides TurboTax income tax preparation products and services; and personal finance. The Credit Karma segment offers consumers with a personal finance platform that provides personalized recommendations of home, auto, and personal loans, as well as credit cards and insurance products. The ProConnect segment provides Lacerte, ProSeries, and ProFile desktop tax-preparation software products; and ProConnect Tax Online tax products, electronic tax filing service, and bank products and related services. It sells products and services through various sales and distribution channels, including multi-channel shop-and-buy experiences, websites and call centers, mobile application stores, and retail and other channels. The company was founded in 1983 and is headquartered in Mountain View, California.",
        fullTimeEmployees=13500,
        city="Mountain View",
        state="CA",
        trailingPE=50.95502,
        dividendYield=0.0073,
        averageVolume=1986758,
        regularMarketOpen=405.75,
        volume=1631091,
        fiftyTwoWeekHigh=716.86,
        fiftyTwoWeekLow=339.36,
        recommendationKey="buy",
        industry="Software—Application"
    )
    db.session.add(INTU)

    ISRG = Stock(
        name="Intuitive Surgical, Inc.",
        ticker="ISRG",
        marketCap=72158298112,
        dayHigh=211.28,
        dayLow=201.17,
        currentPrice=201.99,
        longBusinessSummary="Intuitive Surgical, Inc. develops, manufactures, and markets products that enable physicians and healthcare providers to enhance the quality of and access to minimally invasive care in the United States and internationally. The company offers the da Vinci Surgical System to enable complex surgery using a minimally invasive approach; and Ion endoluminal system, which extends its commercial offerings beyond surgery into diagnostic procedures enabling minimally invasive biopsies in the lung. It also provides a suite of stapling, energy, and core instrumentation for its surgical systems; progressive learning pathways to support the use of its technology; a complement of services to its customers, including support, installation, repair, and maintenance; and integrated digital capabilities providing unified and connected offerings, streamlining performance for hospitals with program-enhancing insights. The company was incorporated in 1995 and is headquartered in Sunnyvale, California.",
        fullTimeEmployees=9793,
        city="Sunnyvale",
        state="CA",
        trailingPE=43.5511,
        dividendYield=None,
        averageVolume=2175443,
        regularMarketOpen=209.02,
        volume=1661281,
        fiftyTwoWeekHigh=369.69,
        fiftyTwoWeekLow=186.83,
        recommendationKey="buy",
        industry="Medical Instruments & Supplies"
    )
    db.session.add(ISRG)

    IVZ = Stock(
        name="Invesco Ltd.",
        ticker="IVZ",
        marketCap=7886640128,
        dayHigh=17.73,
        dayLow=17.04,
        currentPrice=17.1,
        longBusinessSummary="Invesco Ltd. is a publicly owned investment manager. The firm provides its services to retail clients, institutional clients, high-net worth clients, public entities, corporations, unions, non-profit organizations, endowments, foundations, pension funds, financial institutions, and sovereign wealth funds. It manages separate client-focused equity and fixed income portfolios. The firm also launches equity, fixed income, commodity, multi-asset, and balanced mutual funds for its clients. It launches equity, fixed income, multi-asset, and balanced exchange-traded funds. The firm also launches and manages private funds. It invests in the public equity and fixed income markets across the globe. The firm also invests in alternative markets, such as commodities and currencies. For the equity portion of its portfolio, it invests in growth and value stocks of large-cap, mid-cap, and small-cap companies. For the fixed income portion of its portfolio, the firm invests in convertibles, government bonds, municipal bonds, treasury securities, and cash. It also invests in short term and intermediate term bonds, investment grade and high yield bonds, taxable and tax-free bonds, senior secured loans, and structured securities such as asset-backed securities, mortgage-backed securities, and commercial mortgage-backed securities. The firm employs absolute return, global macro, and long/short strategies. It employs quantitative analysis to make its investments. The firm was formerly known as Invesco Plc, AMVESCAP plc, Amvesco plc, Invesco PLC, Invesco MIM, and H. Lotery & Co. Ltd. Invesco Ltd. was founded in December 1935 and is based in Atlanta, Georgia with an additional office in Hamilton, Bermuda.",
        fullTimeEmployees=8549,
        city="Atlanta",
        state="GA",
        trailingPE=6.7588935,
        dividendYield=0.042,
        averageVolume=4039659,
        regularMarketOpen=17.54,
        volume=2920808,
        fiftyTwoWeekHigh=27.08,
        fiftyTwoWeekLow=15.68,
        recommendationKey="none",
        industry="Asset Management"
    )
    db.session.add(IVZ)

    IQV = Stock(
        name="IQVIA Holdings Inc.",
        ticker="IQV",
        marketCap=40540598272,
        dayHigh=217.6165,
        dayLow=210.73,
        currentPrice=212.21,
        longBusinessSummary="IQVIA Holdings Inc. provides advanced analytics, technology solutions, and clinical research services to the life sciences industry in the Americas, Europe, Africa, and the Asia-Pacific. It operates through three segments: Technology & Analytics Solutions, Research & Development Solutions, and Contract Sales & Medical Solutions. The Technology & Analytics Solutions segment offers a range of cloud-based applications and related implementation services; real world solutions that enable life sciences and provider customers to generate and disseminate evidence, which informs health care decision making and improves patients' outcomes; and strategic and implementation consulting services, such as advanced analytics and commercial processes outsourcing services. This segment also provides country level performance metrics related to sales of pharmaceutical products, prescribing trends, medical treatment, and promotional activity across various channels, including retail, hospital, and mail order; and measurement of sales or prescribing activity at the regional, zip code, and individual prescriber level. The Research & Development Solutions segment offers project management and clinical monitoring; clinical trial support; virtual trials; and strategic planning and design services, as well as central laboratory, genomic, bioanalytical, ADME, discovery, and vaccine and biomarker laboratory services. The Contract Sales & Medical Solutions segment provides health care provider and patient engagement services, and scientific strategy and medical affairs services. It serves pharmaceutical, biotechnology, device and diagnostic, and consumer health companies. The company has a strategic collaboration with HealthCore, Inc. The company was formerly known as Quintiles IMS Holdings, Inc. and changed its name to IQVIA Holdings Inc. in November 2017. IQVIA Holdings Inc. was founded in 1982 and is headquartered in Durham, North Carolina.",
        fullTimeEmployees=82000,
        city="Durham",
        state="NC",
        trailingPE=54.0112,
        dividendYield=None,
        averageVolume=1174733,
        regularMarketOpen=216.21,
        volume=737629,
        fiftyTwoWeekHigh=285.61,
        fiftyTwoWeekLow=194.67,
        recommendationKey="buy",
        industry="Diagnostics & Research"
    )
    db.session.add(IQV)

    IRM = Stock(
        name="Iron Mountain Incorporated",
        ticker="IRM",
        marketCap=14234278912,
        dayHigh=50.75,
        dayLow=49.09,
        currentPrice=49.16,
        longBusinessSummary="Iron Mountain Incorporated (NYSE: IRM), founded in 1951, is the global leader for storage and information management services. Trusted by more than 225,000 organizations around the world, and with a real estate network of more than 90 million square feet across approximately 1,450 facilities in approximately 50 countries, Iron Mountain stores and protects billions of valued assets, including critical business information, highly sensitive data, and cultural and historical artifacts. Providing solutions that include secure records storage, information management, digital transformation, secure destruction, as well as data centers, cloud services and art storage and logistics, Iron Mountain helps customers lower cost and risk, comply with regulations, recover from disaster, and enable a more digital way of working.",
        fullTimeEmployees=25000,
        city="Boston",
        state="MA",
        trailingPE=22.375967,
        dividendYield=0.0473,
        averageVolume=1629979,
        regularMarketOpen=50.58,
        volume=954692,
        fiftyTwoWeekHigh=58.61,
        fiftyTwoWeekLow=41.67,
        recommendationKey="buy",
        industry="REIT—Specialty"
    )
    db.session.add(IRM)

    JBHT = Stock(
        name="J.B. Hunt Transport Services, Inc.",
        ticker="JBHT",
        marketCap=16555456512,
        dayHigh=164.38,
        dayLow=157.325,
        currentPrice=157.65,
        longBusinessSummary="J.B. Hunt Transport Services, Inc. provides surface transportation, delivery, and logistic services in North America. It operates through five segments: Intermodal (JBI), Dedicated Contract Services (DCS), Integrated Capacity Solutions (ICS), Final Mile Services (FMS), and Truckload (JBT). The JBI segment offers intermodal freight solutions. It operates 104,973 pieces of company-owned trailing equipment; owns and maintains its chassis fleet of 85,649 units; and manages a fleet of 5,612 company-owned tractors, 582 independent contractor trucks, and 6,943 company drivers. The DCS segment designs, develops, and executes supply chain solutions that support various transportation networks. As of December 31, 2021, it operated 11,139 company-owned trucks, 544 customer-owned trucks, and 6 contractor trucks. The company also operates 21,069 owned pieces of trailing equipment and 7,753 customer-owned trailers. The ICS segment provides freight brokerage and transportation logistics solutions; flatbed, refrigerated, expedited, and less-than-truckload, as well as dry-van and intermodal solutions; an online multimodal marketplace; and logistics management for customers to outsource the transportation functions. The FMS segment offers delivery services through 1,272 company-owned trucks, 272 customer-owned trucks, and 19 independent contractor trucks; and 1,036 owned pieces of trailing equipment and 185 customer-owned trailers. The JBT segment provides dry-van freight services by utilizing tractors and trailers operating over roads and highways through 734 company-owned tractors and 11,172 company-owned trailers. It also transports or arranges for the transportation of freight, such as general merchandise, specialty consumer items, appliances, forest and paper products, food and beverages, building materials, soaps and cosmetics, automotive parts, agricultural products, electronics, and chemicals. The company was incorporated in 1961 and is headquartered in Lowell, Arkansas.",
        fullTimeEmployees=33045,
        city="Lowell",
        state="AR",
        trailingPE=25.023808,
        dividendYield=0.0091,
        averageVolume=990075,
        regularMarketOpen=161.72,
        volume=432303,
        fiftyTwoWeekHigh=218.18,
        fiftyTwoWeekLow=153.92,
        recommendationKey="buy",
        industry="Integrated Freight & Logistics"
    )
    db.session.add(JBHT)

    JKHY = Stock(
        name="Jack Henry & Associates, Inc.",
        ticker="JKHY",
        marketCap=13356995584,
        dayHigh=184.895,
        dayLow=179.985,
        currentPrice=180.4,
        longBusinessSummary="Jack Henry & Associates, Inc. provides technology solutions and payment processing services primarily for financial services organizations in the United States. It operates through four segments: Core, Payments, Complementary, and Corporate and Other. The company offers information and transaction processing solutions for banks ranging from community to multi-billion-dollar asset institutions under the Jack Henry Banking brand; core data processing solutions for various credit unions under the Symitar brand; and specialized financial performance, imaging and payments processing, information security and risk management, retail delivery, and online and mobile solutions to financial institutions and corporate entities under the ProfitStars brand. It also provides a suite of integrated applications required to process deposit, loan, and general ledger transactions, as well as to maintain centralized customer/member information; and complementary products and services that enable core bank and credit union clients to respond to evolving customer/member demands. The company's Jack Henry Banking business brand offers SilverLake, a robust primarily designed for commercial-focused banks; CIF 20/20, a parameter-driven, easy-to-use system for banks; and Core Director, a cost-efficient system with point-and-click operation. Its Symitar business brand provides Episys, a robust designed for credit unions. In addition, the company offers digital products and services and electronic payment solutions; purchases and resells hardware systems, including servers, workstations, scanners, and other devices; and provides implementation, training, and support services. Jack Henry & Associates, Inc. was founded in 1976 and is headquartered in Monett, Missouri.",
        fullTimeEmployees=6714,
        city="Monett",
        state="MO",
        trailingPE=41.933983,
        dividendYield=0.0112,
        averageVolume=486545,
        regularMarketOpen=182.56,
        volume=294467,
        fiftyTwoWeekHigh=205.37,
        fiftyTwoWeekLow=147.5,
        recommendationKey="hold",
        industry="Information Technology Services"
    )
    db.session.add(JKHY)

    J = Stock(
        name="Jacobs Engineering Group Inc.",
        ticker="J",
        marketCap=16131138560,
        dayHigh=128.04,
        dayLow=124.38,
        currentPrice=124.61,
        longBusinessSummary="Jacobs Engineering Group Inc. provides consulting, technical, scientific, and project delivery services for the government and private sectors in the United States, Europe, Canada, India, rest of Asia, Australia, New Zealand, South America, Mexico, the Middle East, and Africa. The company operates in two segments, Critical Mission Solutions and People & Places Solutions. The Critical Mission Solutions segment provides cybersecurity, data analytics, systems and software application integration and consulting, enterprise and mission IT, engineering and design, nuclear, enterprise level operations and maintenance, and other technical consulting solutions. The People & Places Solutions segment offers data analytics, artificial intelligence and automation, software development, digitally driven consulting, planning and architecture, program management, and other technical consulting solutions. The company is also involved in the management and execution of wind-tunnel design-build projects; and design-build for water and construction management. Jacobs Engineering Group Inc. was founded in 1947 and is headquartered in Dallas, Texas.",
        fullTimeEmployees=52000,
        city="Dallas",
        state="TX",
        trailingPE=38.98936,
        dividendYield=0.0069,
        averageVolume=671098,
        regularMarketOpen=126.88,
        volume=339676,
        fiftyTwoWeekHigh=150.32,
        fiftyTwoWeekLow=114.11,
        recommendationKey="buy",
        industry="Engineering & Construction"
    )
    db.session.add(J)

    JNJ = Stock(
        name="Johnson & Johnson",
        ticker="JNJ",
        marketCap=465812258816,
        dayHigh=182.97,
        dayLow=176.31,
        currentPrice=176.94,
        longBusinessSummary="Johnson & Johnson researches and develops, manufactures, and sells various products in the healthcare field worldwide. It operates in three segments: Consumer Health, Pharmaceutical, and Medical Devices. The Consumer Health segment offers baby care products under the JOHNSON'S and AVEENO Baby brands; oral care products under the LISTERINE brand; skin health/beauty products under the AVEENO, CLEAN & CLEAR, DR. CI:LABO, NEUTROGENA, and OGX brands; acetaminophen products under the TYLENOL brand; cold, flu, and allergy products under the SUDAFED brand; allergy products under the BENADRYL and ZYRTEC brands; ibuprofen products under the MOTRIN IB brand; smoking cessation products under the NICORETTE brand; and acid reflux products under the PEPCID brand. This segment also provides women's health products, such as sanitary pads and tampons under the STAYFREE, CAREFREE, and o.b. brands; wound care products comprising adhesive bandages under the BAND-AID brand; and first aid products under the NEOSPORIN brand. The Pharmaceutical segment offers products in various therapeutic areas, including immunology, infectious diseases, neuroscience, oncology, pulmonary hypertension, and cardiovascular and metabolic diseases. The Medical Devices segment provides electrophysiology products to treat cardiovascular diseases; neurovascular care products to treat hemorrhagic and ischemic stroke; orthopaedics products in support of hips, knees, trauma, spine, sports, and other; advanced and general surgery solutions that focus on breast aesthetics, ear, nose, and throat procedures; and disposable contact lenses and ophthalmic products related to cataract and laser refractive surgery under the ACUVUE brand. The company markets its products to general public, and retail outlets and distributors, as well as distributes directly to wholesalers, hospitals, and healthcare professionals for prescription use. Johnson & Johnson was founded in 1886 and is based in New Brunswick, New Jersey.",
        fullTimeEmployees=144000,
        city="New Brunswick",
        state="NJ",
        trailingPE=26.444479,
        dividendYield=0.0256,
        averageVolume=7667138,
        regularMarketOpen=182.17,
        volume=9277210,
        fiftyTwoWeekHigh=186.69,
        fiftyTwoWeekLow=155.72,
        recommendationKey="buy",
        industry="Drug Manufacturers—General"
    )
    db.session.add(JNJ)

    JPM = Stock(
        name="JPMorgan Chase & Co.",
        ticker="JPM",
        marketCap=350742347776,
        dayHigh=119.29,
        dayLow=115.6,
        currentPrice=115.82,
        longBusinessSummary="JPMorgan Chase & Co. operates as a financial services company worldwide. It operates through four segments: Consumer & Community Banking (CCB), Corporate & Investment Bank (CIB), Commercial Banking (CB), and Asset & Wealth Management (AWM). The CCB segment offers s deposit, investment and lending products, payments, and services to consumers; lending, deposit, and cash management and payment solutions to small businesses; mortgage origination and servicing activities; residential mortgages and home equity loans; and credit card, auto loan, and leasing services. The CIB segment provides investment banking products and services, including corporate strategy and structure advisory, and equity and debt markets capital-raising services, as well as loan origination and syndication; payments and cross-border financing; and cash and derivative instruments, risk management solutions, prime brokerage, and research. This segment also offers securities services, including custody, fund accounting and administration, and securities lending products for asset managers, insurance companies, and public and private investment funds. The CB segment provides financial solutions, including lending, payments, investment banking, and asset management to small business, large and midsized companies, local governments, and nonprofit clients; and commercial real estate banking services to investors, developers, and owners of multifamily, office, retail, industrial, and affordable housing properties. The AWM segment offers multi-asset investment management solutions in equities, fixed income, alternatives, and money market funds to institutional clients and retail investors; and retirement products and services, brokerage, custody, trusts and estates, loans, mortgages, deposits, and investment management products. The company also provides ATM, online and mobile, and telephone banking services. JPMorgan Chase & Co. was founded in 1799 and is headquartered in New York, New York.",
        fullTimeEmployees=273948,
        city="New York",
        state="NY",
        trailingPE=7.3262067,
        dividendYield=0.0336,
        averageVolume=14305666,
        regularMarketOpen=117.67,
        volume=11547398,
        fiftyTwoWeekHigh=172.96,
        fiftyTwoWeekLow=111.48,
        recommendationKey="buy",
        industry="Banks—Diversified"
    )
    db.session.add(JPM)

    JNPR = Stock(
        name="Juniper Networks, Inc.",
        ticker="JNPR",
        marketCap=9322939392,
        dayHigh=29.53,
        dayLow=28.63,
        currentPrice=28.67,
        longBusinessSummary="Juniper Networks, Inc. designs, develops, and sells network products and services worldwide. The company offers routing products, such as ACX series universal access routers to deploy high-bandwidth services; MX series Ethernet routers that function as a universal edge platform; PTX series packet transport routers; wide-area network SDN controllers; and session smart routers. It also provides switching products, including EX series Ethernet switches to address the access, aggregation, and core layer switching requirements of micro branch, branch office, and campus environments; QFX series of core, spine, and top-of-rack data center switches; and juniper access points, which provide Wi-Fi access and performance. In addition, the company offers security products comprising SRX series services gateways for the data center; Branch SRX family provides an integrated and next-generation firewall; virtual firewall that delivers various features of physical firewalls; and advanced malware protection, a cloud-based service and Juniper ATP. Further, it offers Junos OS, a network operating system; Contrail networking, which provides an open-source and standards-based platform for SDN; Mist AI-driven Wired, Wireless, and WAN assurance solutions to set and measure key metrics; Mist AI-driven Marvis Virtual Network Assistant, which identifies the root cause of issues; Juniper Paragon Automation, a modular portfolio of cloud-native software applications; and Juniper Apstra to automate the network lifecycle in a single system. Additionally, the company provides software-as-a-service, technical support, maintenance, and professional services, as well as education and training programs. It sells its products through direct sales, distributors, value-added resellers, and original equipment manufacturers to end-users in the cloud, service provider, and enterprise markets. The company was incorporated in 1996 and is headquartered in Sunnyvale, California.",
        fullTimeEmployees=10385,
        city="Sunnyvale",
        state="CA",
        trailingPE=63.711113,
        dividendYield=0.0276,
        averageVolume=4118059,
        regularMarketOpen=29.37,
        volume=2467307,
        fiftyTwoWeekHigh=38.14,
        fiftyTwoWeekLow=26.12,
        recommendationKey="hold",
        industry="Communication Equipment"
    )
    db.session.add(JNPR)

    K = Stock(
        name="Kellogg Company",
        ticker="K",
        marketCap=24175388672,
        dayHigh=71.66,
        dayLow=70.5973,
        currentPrice=70.87,
        longBusinessSummary="Kellogg Company, together with its subsidiaries, manufactures and markets snacks and convenience foods. The company operates through four segments: North America, Europe, Latin America, and Asia Middle East Africa. Its principal products include crackers, crisps, savory snacks, toaster pastries, cereal bars, granola bars and bites, ready-to-eat cereals, frozen waffles, veggie foods, and noodles. The company offers its products under the Kellogg's, Cheez-It, Pringles, Austin, Parati, RXBAR, Kashi, Bear Naked, Eggo, Morningstar Farms, Choco Krispies, Crunchy Nut, Nutri-Grain, Special K, Squares, Zucaritas, Sucrilhos, Pop-Tarts, K-Time, Sunibrite, Split Stix, Be Natural, LCMs, Coco Pops, Frosties, Rice Krispies Squares, Kashi Go, Vector, Incogmeato, Veggitizers, and Gardenburger brand names. It sells its products to retailers through direct sales forces, as well as brokers and distributors. The company was founded in 1906 and is headquartered in Battle Creek, Michigan.",
        fullTimeEmployees=31000,
        city="Battle Creek",
        state="MI",
        trailingPE=19.321157,
        dividendYield=0.0318,
        averageVolume=2874911,
        regularMarketOpen=71.13,
        volume=2692456,
        fiftyTwoWeekHigh=75.56,
        fiftyTwoWeekLow=59.54,
        recommendationKey="hold",
        industry="Packaged Foods"
    )
    db.session.add(K)

    KDP = Stock(
        name="Keurig Dr Pepper Inc.",
        ticker="KDP",
        marketCap=50351755264,
        dayHigh=36.32,
        dayLow=35.49,
        currentPrice=35.51,
        longBusinessSummary="Keurig Dr Pepper Inc. operates as a beverage company in the United States and internationally. It operates through Coffee Systems, Packaged Beverages, Beverage Concentrates, and Latin America Beverages segments. The Coffee Systems segment manufactures and distributes various finished goods related to its coffee systems, K-Cup pods, and brewers, as well as specialty coffee. This segment sells its brewers through third-party distributors and retail partners, as well as through its website at keurig.com. The Packaged Beverages segment engages in the manufacture and distribution of packaged beverages of its brands; contract manufacturing of various private label and emerging brand beverages; and distribution of packaged beverages for its partner brands. The Beverage Concentrates segment manufactures and sells beverage concentrates primarily under the Dr Pepper, Canada Dry, A&W, 7UP, Sunkist, Squirt, Big Red, RC Cola, Vernors, Snapple, Mott's, Bai, Hawaiian Punch, Clamato, Yoo-Hoo, Core, ReaLemon, evian, Vita Coco, and Mr and Mrs T mixers brands. This segment also manufactures beverage concentrates into syrup. The Latin America Beverages segment manufactures and distributes carbonated mineral water, flavored carbonated soft drinks, bottled water, and vegetable juice products under the Peñafiel, Clamato, Squirt, Dr Pepper, Crush, and Aguafiel brands. The company serves retailers, bottlers and distributors, restaurants, hotel chains, office coffee distributors, and end-use consumers. Keurig Dr Pepper Inc. was founded in 1981 and is headquartered in Burlington, Massachusetts.",
        fullTimeEmployees=27000,
        city="Burlington",
        state="MA",
        trailingPE=29.347105,
        dividendYield=0.0202,
        averageVolume=11930337,
        regularMarketOpen=35.96,
        volume=7036293,
        fiftyTwoWeekHigh=39.35,
        fiftyTwoWeekLow=32.44,
        recommendationKey="buy",
        industry="Beverages—Non-Alcoholic"
    )
    db.session.add(KDP)

    KEY = Stock(
        name="KeyCorp",
        ticker="KEY",
        marketCap=16395931648,
        dayHigh=18.12,
        dayLow=17.555,
        currentPrice=17.61,
        longBusinessSummary="KeyCorp operates as the holding company for KeyBank National Association that provides various retail and commercial banking products and services in the United States. It operates in two segments, Consumer Bank and Commercial Bank. The company offers various deposits, investment products and services; and personal finance and financial wellness, student loan refinancing, mortgage and home equity, lending, credit card, treasury, business advisory, wealth management, asset management, investment, cash management, portfolio management, and trust and related services to individuals and small and medium-sized businesses. It also provides a suite of banking and capital market products, such as syndicated finance, debt and equity capital market products, commercial payments, equipment finance, commercial mortgage banking, derivatives, foreign exchange, financial advisory, and public finance, as well as commercial mortgage loans comprising consumer, energy, healthcare, industrial, public sector, real estate, and technology loans for middle market clients. In addition, the company offers community development financing, securities underwriting, brokerage, and investment banking services. As of December 31, 2021, it operated through a network of approximately 999 branches and 1,317 ATMs in 15 states, as well as additional offices, online and mobile banking capabilities, and a telephone banking call center. KeyCorp was founded in 1849 and is headquartered in Cleveland, Ohio.",
        fullTimeEmployees=17110,
        city="Cleveland",
        state="OH",
        trailingPE=6.8601484,
        dividendYield=0.0419,
        averageVolume=10664861,
        regularMarketOpen=17.76,
        volume=7895066,
        fiftyTwoWeekHigh=27.17,
        fiftyTwoWeekLow=16.69,
        recommendationKey="hold",
        industry="Banks—Regional"
    )
    db.session.add(KEY)

    KEYS = Stock(
        name="Keysight Technologies, Inc.",
        ticker="KEYS",
        marketCap=25428195328,
        dayHigh=143,
        dayLow=138.71,
        currentPrice=138.92,
        longBusinessSummary="Keysight Technologies, Inc. provides electronic design and test solutions to commercial communications, networking, aerospace, defense and government, automotive, energy, semiconductor, electronic, and education industries in the Americas, Europe, and the Asia Pacific. Its Communications Solutions Group segment provides electronic design automation (EDA) software; radio frequency and microwave test solutions, and related software; hardware and virtual network test platforms and software applications, including data center, routing and switching, software defined networking, security, and encryption; oscilloscopes, logic and serial protocol analyzers, logic-signal sources, arbitrary waveform generators, and bit error rate testers; and optical modulation analyzers, optical component analyzers, optical power meters, and optical laser source solutions, as well as resells refurbished used Keysight equipment. The company's Electronic Industrial Solutions Group segment offers design tools; design verification tools; and digital multimeters, function generators, frequency counters, data acquisition systems, audio analyzers, LCR meters, thermal imagers, source measure units, ultra-high precision device current analyzers, and test executive software platforms, as well as various power supplies comprising AC/DC modular supplies and electronically programmable loads. This segment also provides printed-circuit-board-assembly testers, integrated circuit parametric testers, and sub-nano-meter positioning sub-assemblies; and test and measurement products and software. The company offers product support, technical support, and training and consulting services. It sells its products through direct sales force, distributors, resellers, and manufacturer's representatives. Keysight Technologies, Inc. was founded in 1939 and is headquartered in Santa Rosa, California.",
        fullTimeEmployees=14300,
        city="Santa Rosa",
        state="CA",
        trailingPE=29.06276,
        dividendYield=None,
        averageVolume=1010862,
        regularMarketOpen=142.3,
        volume=614019,
        fiftyTwoWeekHigh=209.08,
        fiftyTwoWeekLow=127.93,
        recommendationKey="buy",
        industry="Scientific & Technical Instruments"
    )
    db.session.add(KEYS)

    KMB = Stock(
        name="Kimberly-Clark Corporation",
        ticker="KMB",
        marketCap=44628467712,
        dayHigh=133.89,
        dayLow=132.27,
        currentPrice=132.54,
        longBusinessSummary="Kimberly-Clark Corporation, together with its subsidiaries, manufactures and markets personal care and consumer tissue products worldwide. It operates through three segments: Personal Care, Consumer Tissue, and K-C Professional. The Personal Care segment offers disposable diapers, swimpants, training and youth pants, baby wipes, feminine and incontinence care products, and other related products under the Huggies, Pull-Ups, Little Swimmers, GoodNites, DryNites, Sweety, Kotex, U by Kotex, Intimus, Depend, Plenitud, Softex, Poise, and other brand names. The Consumer Tissue segment provides facial and bathroom tissues, paper towels, napkins, and related products under the Kleenex, Scott, Cottonelle, Viva, Andrex, Scottex, Neve, and other brand names. The K-C Professional segment offers wipers, tissues, towels, apparel, soaps, and sanitizers under the Kleenex, Scott, WypAll, Kimtech, and KleenGuard brands. The company sells household use products directly to supermarkets, mass merchandisers, drugstores, warehouse clubs, variety and department stores, and other retail outlets, as well as through other distributors and e-commerce; and away-from-home use products directly to manufacturing, lodging, office building, food service, and public facilities, as well as through distributors and e-commerce. Kimberly-Clark Corporation was founded in 1872 and is headquartered in Dallas, Texas.",
        fullTimeEmployees=45000,
        city="Dallas",
        state="TX",
        trailingPE=22.533152,
        dividendYield=0.033299997,
        averageVolume=1944082,
        regularMarketOpen=133.38,
        volume=1136099,
        fiftyTwoWeekHigh=145.79,
        fiftyTwoWeekLow=117.32,
        recommendationKey="hold",
        industry="Household & Personal Products"
    )
    db.session.add(KMB)

    KIM = Stock(
        name="Kimco Realty Corporation",
        ticker="KIM",
        marketCap=12556639232,
        dayHigh=20.935,
        dayLow=20.275,
        currentPrice=20.37,
        longBusinessSummary="Kimco Realty Corp. (NYSE:KIM) is a real estate investment trust (REIT) headquartered in Jericho, N.Y. that is one of North America's largest publicly traded owners and operators of open-air, grocery-anchored shopping centers and mixed-use assets. As of September 30, 2020, the company owned interests in 400 U.S. shopping centers and mixed-use assets comprising 70 million square feet of gross leasable space primarily concentrated in the top major metropolitan markets. Publicly traded on the NYSE since 1991, and included in the S&P 500 Index, the company has specialized in shopping center acquisitions, development and management for more than 60 years.",
        fullTimeEmployees=606,
        city="Jericho",
        state="NY",
        trailingPE=10.089153,
        dividendYield=0.0344,
        averageVolume=4881967,
        regularMarketOpen=20.49,
        volume=5994667,
        fiftyTwoWeekHigh=26.57,
        fiftyTwoWeekLow=18.52,
        recommendationKey="buy",
        industry="REIT—Retail"
    )
    db.session.add(KIM)

    KMI = Stock(
        name="Kinder Morgan, Inc.",
        ticker="KMI",
        marketCap=38999797760,
        dayHigh=17.46,
        dayLow=17.04,
        currentPrice=17.2,
        longBusinessSummary="Kinder Morgan, Inc. operates as an energy infrastructure company in North America. The company operates through four segments: Natural Gas Pipelines, Products Pipelines, Terminals, and CO2. The Natural Gas Pipelines segment owns and operates interstate and intrastate natural gas pipeline, and underground storage systems; natural gas gathering systems and natural gas processing and treating facilities; natural gas liquids fractionation facilities and transportation systems; and liquefied natural gas liquefaction and storage facilities. The Products Pipelines segment owns and operates refined petroleum products, and crude oil and condensate pipelines; and associated product terminals and petroleum pipeline transmix facilities. The Terminals segment owns and/or operates liquids and bulk terminals that stores and handles various commodities, including gasoline, diesel fuel, chemicals, ethanol, metals, and petroleum coke; and owns tankers. The CO2 segment produces, transports, and markets CO2 to recovery and production crude oil from mature oil fields; owns interests in/or operates oil fields and gasoline processing plants; and operates a crude oil pipeline system in West Texas, as well as owns and operates RNG and LNG facilities. It owns and operates approximately 83,000 miles of pipelines and 143 terminals. The company was formerly known as Kinder Morgan Holdco LLC and changed its name to Kinder Morgan, Inc. in February 2011. Kinder Morgan, Inc. was founded in 1936 and is headquartered in Houston, Texas.",
        fullTimeEmployees=10529,
        city="Houston",
        state="TX",
        trailingPE=22.395834,
        dividendYield=0.0592,
        averageVolume=17176167,
        regularMarketOpen=17.19,
        volume=14200915,
        fiftyTwoWeekHigh=20.2,
        fiftyTwoWeekLow=15.01,
        recommendationKey="hold",
        industry="Oil & Gas Midstream"
    )
    db.session.add(KMI)

    KLAC = Stock(
        name="KLA Corporation",
        ticker="KLAC",
        marketCap=50048905216,
        dayHigh=345.1,
        dayLow=329.69,
        currentPrice=330.09,
        longBusinessSummary="KLA Corporation designs, manufactures, and markets process control and yield management solutions for the semiconductor and related nanoelectronics industries worldwide. The company offers chip and wafer manufacturing products, including defect inspection and review systems, metrology solutions, in situ process monitoring products, computational lithography software, and data analytics systems for chip manufacturers to manage yield throughout the semiconductor fabrication process. It also provides reticle manufacturing products, such as reticle inspection, metrology, and data analytics systems for mask shops; and packaging manufacturing products comprising wafer inspection and metrology, die sorting and inspection, IC component inspection and metrology, data analytics, wafer processing systems, and IC substrate production processes. In addition, the company offers compound semiconductor, power device, light emitting diode, and microelectromechanical system manufacturing products; data storage media/head manufacturing products; general purpose/lab applications; and previous-generation KLA systems. Further, it provides wafer processing solutions; printed circuit boards, and display and inspection components; and other services. The company was formerly known as KLA-Tencor Corporation and changed its name to KLA Corporation in July 2019. KLA Corporation was incorporated in 1975 and is headquartered in Milpitas, California.",
        fullTimeEmployees=11300,
        city="Milpitas",
        state="CA",
        trailingPE=18.735952,
        dividendYield=0.0125,
        averageVolume=1397259,
        regularMarketOpen=341.49,
        volume=1283087,
        fiftyTwoWeekHigh=457.12,
        fiftyTwoWeekLow=287.44,
        recommendationKey="buy",
        industry="Semiconductor Equipment & Materials"
    )
    db.session.add(KLAC)

    KHC = Stock(
        name="The Kraft Heinz Company",
        ticker="KHC",
        marketCap=46183026688,
        dayHigh=39.005,
        dayLow=37.56,
        currentPrice=37.73,
        longBusinessSummary="The Kraft Heinz Company, together with its subsidiaries, manufactures and markets food and beverage products in the United States, Canada, the United Kingdom, and internationally. Its products include condiments and sauces, cheese and dairy products, meals, meats, refreshment beverages, coffee, and other grocery products. The company also offers dressings, healthy snacks, and other categories; and spices and other seasonings. It sells its products through its own sales organizations, as well as through independent brokers, agents, and distributors to chain, wholesale, cooperative and independent grocery accounts, convenience stores, drug stores, value stores, bakeries, pharmacies, mass merchants, club stores, and foodservice distributors and institutions, including hotels, restaurants, hospitals, health care facilities, and government agencies; and online through various e-commerce platforms and retailers. The company was formerly known as H.J. Heinz Holding Corporation and changed its name to The Kraft Heinz Company in July 2015. The Kraft Heinz Company was founded in 1869 and is headquartered in Pittsburgh, Pennsylvania.",
        fullTimeEmployees=36000,
        city="Pittsburgh",
        state="PA",
        trailingPE=20.30678,
        dividendYield=0.0361,
        averageVolume=8468170,
        regularMarketOpen=38.66,
        volume=6365730,
        fiftyTwoWeekHigh=44.87,
        fiftyTwoWeekLow=32.785,
        recommendationKey="hold",
        industry="Packaged Foods"
    )
    db.session.add(KHC)

    KR = Stock(
        name="The Kroger Co.",
        ticker="KR",
        marketCap=35608449024,
        dayHigh=49.39,
        dayLow=48.29,
        currentPrice=48.43,
        longBusinessSummary="The Kroger Co. operates as a retailer in the United States. The company operates combination food and drug stores, multi-department stores, marketplace stores, and price impact warehouses. Its combination food and drug stores offer natural food and organic sections, pharmacies, general merchandise, pet centers, fresh seafood, and organic produce; and multi-department stores provide apparel, home fashion and furnishings, outdoor living, electronics, automotive products, and toys. The company's marketplace stores offer full-service grocery, pharmacy, health and beauty care, and perishable goods, as well as general merchandise, including apparel, home goods, and toys; and price impact warehouse stores provide grocery, and health and beauty care items, as well as meat, dairy, baked goods, and fresh produce items. It also manufactures and processes food products for sale in its supermarkets and online; and sells fuel through 1,613 fuel centers. As of January 29, 2022, the company operated 2,726 supermarkets under various banner names in 35 states and the District of Columbia. The Kroger Co. was founded in 1883 and is based in Cincinnati, Ohio.",
        fullTimeEmployees=420000,
        city="Cincinnati",
        state="OH",
        trailingPE=36.55094,
        dividendYield=0.015700001,
        averageVolume=6685151,
        regularMarketOpen=49.04,
        volume=3684966,
        fiftyTwoWeekHigh=62.78,
        fiftyTwoWeekLow=37.26,
        recommendationKey="hold",
        industry="Grocery Stores"
    )
    db.session.add(KR)

    LHX = Stock(
        name="L3Harris Technologies, Inc.",
        ticker="LHX",
        marketCap=46273777664,
        dayHigh=240.68,
        dayLow=235.27,
        currentPrice=235.82,
        longBusinessSummary="L3Harris Technologies, Inc., an aerospace and defense technology company, provides mission-critical solutions for government and commercial customers worldwide. The company's Integrated Mission Systems segment provides multi-mission intelligence, surveillance, and reconnaissance (ISR) systems; and communication systems, as well as fleet management support, sensor development, modification, and periodic depot maintenance services for ISR and airborne missions. It also manufactures and integrates mission systems for maritime platforms, such as signals intelligence and multi-intelligence platforms; unmanned surface and undersea autonomous solutions; and power and ship control systems and other electronic and electrical products and systems. In addition, this segment offers advanced electro-optical and infrared solutions. Its Space and Airborne Systems segment offers space payloads, sensors, and full-mission solutions; classified intelligence and cyber defense solutions; mission avionics; and electronic warfare systems. The company's Communication Systems segment provides tactical communications; broadband secured mobile networked communication equipment, including airborne, space, and surface data link terminals, ground stations, and transportable tactical satellite communication (SATCOM) systems for use in manned aircraft, unmanned aerial vehicles, and naval ships; and helmet and weapon mounted integrated night vision systems. This segment also offers radios, systems applications, and equipment for critical public safety and professional communications; and SATCOM terminals and battlefield management networks. Its Aviation Systems segment offers defense aviation products; commercial pilot training; and mission networks solutions for air traffic management. The company was formerly known as Harris Corporation and changed its name to L3Harris Technologies, Inc. in June 2019. L3Harris Technologies, Inc. was founded in 1895 and is headquartered in Melbourne, Florida.",
        fullTimeEmployees=47000,
        city="Melbourne",
        state="FL",
        trailingPE=31.384085,
        dividendYield=0.019,
        averageVolume=995337,
        regularMarketOpen=237.19,
        volume=761258,
        fiftyTwoWeekHigh=279.71,
        fiftyTwoWeekLow=200.71,
        recommendationKey="none",
        industry="Aerospace & Defense"
    )
    db.session.add(LHX)

    LH = Stock(
        name="Laboratory Corporation of America Holdings",
        ticker="LH",
        marketCap=22581372928,
        dayHigh=243.79,
        dayLow=235.73,
        currentPrice=235.96,
        longBusinessSummary="Laboratory Corporation of America Holdings operates as an independent clinical laboratory company worldwide. It operates in two segments, Labcorp Diagnostics (Dx) and Labcorp Drug Development (DD). It offers various tests, such as blood chemistry analyses, urinalyses, blood cell counts, thyroid tests, Pap tests, hemoglobin A1C and vitamin D products, prostate-specific antigens, tests for sexually transmitted diseases, hepatitis C tests, microbiology cultures and procedures, and alcohol and other substance-abuse tests. The company also provides specialty testing services comprising gene-based and esoteric testing; advanced tests target specific diseases, including anatomic pathology/oncology, cardiovascular disease, coagulation, diagnostic genetics, endocrinology, infectious disease, women's health, pharmacogenetics, and parentage and donor testing; and occupational testing services, medical drug monitoring services, chronic disease programs, and kidney stone prevention tests. It provides online and mobile applications to enable patients to check test results; and online applications for managed care organizations. It offers end-to-end drug development, medical device, and diagnostic development solutions from early-stage research to clinical development and commercial market access. It serves managed care organizations, biopharmaceutical companies, physicians and other healthcare providers, hospitals and health systems, governmental agencies, employers, patients and consumers, contract research organizations, crop protection and chemical companies, academic institutions, and independent clinical laboratories. The company was founded in 1971 and is headquartered in Burlington, North Carolina.",
        fullTimeEmployees=75000,
        city="Burlington",
        state="NC",
        trailingPE=8.371235,
        dividendYield=0.0117999995,
        averageVolume=891804,
        regularMarketOpen=243.64,
        volume=608347,
        fiftyTwoWeekHigh=317.17,
        fiftyTwoWeekLow=212.4,
        recommendationKey="buy",
        industry="Diagnostics & Research"
    )
    db.session.add(LH)

    LRCX = Stock(
        name="Lam Research Corporation",
        ticker="LRCX",
        marketCap=61706575872,
        dayHigh=459.27,
        dayLow=437.94,
        currentPrice=438.26,
        longBusinessSummary="Lam Research Corporation designs, manufactures, markets, refurbishes, and services semiconductor processing equipment used in the fabrication of integrated circuits. The company offers ALTUS systems to deposit conformal films for tungsten metallization applications; SABRE electrochemical deposition products for copper interconnect transition that offers copper damascene manufacturing; SOLA ultraviolet thermal processing products for film treatments; and VECTOR plasma-enhanced CVD ALD products. It also provides SPEED gapfill high-density plasma chemical vapor deposition products; and Striker single-wafer atomic layer deposition products for dielectric film solutions. In addition, the company offers Flex for dielectric etch applications; Kiyo for conductor etch applications; Syndion for through-silicon via etch applications; and Versys metal products for metal etch processes. Further, it provides Coronus bevel clean products to enhance die yield; Da Vinci, DV-Prime, EOS, and SP series products to address various wafer cleaning applications; and Metryx mass metrology systems for high precision in-line mass measurement in semiconductor wafer manufacturing. The company sells its products and services to semiconductors industry in the United States, China, Europe, Japan, Korea, Southeast Asia, Taiwan, and internationally. Lam Research Corporation was incorporated in 1980 and is headquartered in Fremont, California.",
        fullTimeEmployees=16900,
        city="Fremont",
        state="CA",
        trailingPE=14.812087,
        dividendYield=0.012200001,
        averageVolume=1356808,
        regularMarketOpen=451.38,
        volume=937951,
        fiftyTwoWeekHigh=731.85,
        fiftyTwoWeekLow=411.39,
        recommendationKey="buy",
        industry="Semiconductor Equipment & Materials"
    )
    db.session.add(LRCX)

    LW = Stock(
        name="Lamb Weston Holdings, Inc.",
        ticker="LW",
        marketCap=10474535936,
        dayHigh=73.98,
        dayLow=71.54,
        currentPrice=71.71,
        longBusinessSummary="Lamb Weston Holdings, Inc. produces, distributes, and markets value-added frozen potato products worldwide. It operates through four segments: Global, Foodservice, Retail, and Other. The company offers frozen potatoes, commercial ingredients, and appetizers under the Lamb Weston brand, as well as under various customer labels. The company also offers its products under its owned or licensed brands, such as Grown in Idaho and Alexia, and other licensed brands, as well as under retailers' brands. In addition, it engages in the vegetable and dairy businesses. The company serves retail and foodservice customers; and grocery, mass, club, and specialty retailers; and businesses, independent restaurants, regional chain restaurants, and convenience stores, as well as educational institutions. Lamb Weston Holdings, Inc. was founded in 1950 and is headquartered in Eagle, Idaho.",
        fullTimeEmployees=7800,
        city="Eagle",
        state="ID",
        trailingPE=40.977142,
        dividendYield=0.0154,
        averageVolume=1186475,
        regularMarketOpen=73.7,
        volume=909535,
        fiftyTwoWeekHigh=81.42,
        fiftyTwoWeekLow=49.71,
        recommendationKey="buy",
        industry="Packaged Foods"
    )
    db.session.add(LW)

    LDOS = Stock(
        name="Leidos Holdings, Inc.",
        ticker="LDOS",
        marketCap=13930050560,
        dayHigh=102.56,
        dayLow=98.95,
        currentPrice=99.26,
        longBusinessSummary="Leidos Holdings, Inc., together with its subsidiaries, provides services and solutions in the defense, intelligence, civil, and health markets in the United States and internationally. It operates through three segments: Defense Solutions, Civil, and Health. The Defense Solutions segment offers national security solutions and systems for air, land, sea, space, and cyberspace for the U.S. Intelligence Community, the Department of Defense, the National Aeronautics and Space Administration, military services, and government agencies of U.S. allies abroad, as well as other federal and commercial customers in the national security industry. Its solutions include technology, large-scale systems, command and control platforms, data analytics, logistics, and cybersecurity solutions, as well as intelligence analysis and operations support services to critical missions. The Civil segment provides systems integration services to air navigation service providers, including the federal aviation administration, the En route automation modernization, advanced technology oceanic procedure, time based flow management, terminal flight data management, geo-7, and future flight services, as well as enterprise-information display systems; and security detection and automation services. It also offers information technology (IT) solutions in cloud computing, mobility, application modernization, DevOps, data center, network modernization, asset management, help desk operations, and digital workplace enablement; and environment, energy, and infrastructure services. The Health segment offers solutions to federal and commercial customers responsible for health and well-being of people worldwide, including health information management, managed health, digital transformation, and life sciences research and development services. Leidos Holdings, Inc. was founded in 1969 and is headquartered in Reston, Virginia.",
        fullTimeEmployees=43000,
        city="Reston",
        state="VA",
        trailingPE=18.313654,
        dividendYield=0.014199999,
        averageVolume=790550,
        regularMarketOpen=102.1,
        volume=621171,
        fiftyTwoWeekHigh=111.12,
        fiftyTwoWeekLow=81.07,
        recommendationKey="buy",
        industry="Information Technology Services"
    )
    db.session.add(LDOS)

    LEN = Stock(
        name="Lennar Corporation",
        ticker="LEN",
        marketCap=21130870784,
        dayHigh=72.95,
        dayLow=69.65,
        currentPrice=69.74,
        longBusinessSummary="Lennar Corporation, together with its subsidiaries, operates as a homebuilder primarily under the Lennar brand in the United States. It operates through Homebuilding East, Homebuilding Central, Homebuilding Texas, Homebuilding West, Financial Services, Multifamily, and Lennar Other segments. The company's homebuilding operations include the construction and sale of single-family attached and detached homes, as well as the purchase, development, and sale of residential land; and development, construction, and management of multifamily rental properties. It also offers residential mortgage financing, title insurance, and closing services for home buyers and others, as well as originates and sells securitization commercial mortgage loans. In addition, the company is involved in the fund investment activity. It primarily serves first-time, move-up, active adult, and luxury homebuyers. Lennar Corporation was founded in 1954 and is based in Miami, Florida.",
        fullTimeEmployees=10753,
        city="Miami",
        state="FL",
        trailingPE=4.8871756,
        dividendYield=0.0195,
        averageVolume=2842211,
        regularMarketOpen=72.28,
        volume=2126086,
        fiftyTwoWeekHigh=117.54,
        fiftyTwoWeekLow=62.54,
        recommendationKey="buy",
        industry="Residential Construction"
    )
    db.session.add(LEN)

    LNC = Stock(
        name="Lincoln National Corporation",
        ticker="LNC",
        marketCap=8793299968,
        dayHigh=50.43,
        dayLow=48.48,
        currentPrice=48.66,
        longBusinessSummary="Lincoln National Corporation, through its subsidiaries, operates multiple insurance and retirement businesses in the United States. It operates through four segments: Annuities, Retirement Plan Services, Life Insurance, and Group Protection. The Annuities segment offers fixed, variable, and indexed variable annuities. The Retirement Plan Services segment provides employers with retirement plan products and services primarily in the defined contribution retirement plan marketplace. This segment offers individual and group variable annuities, group fixed annuities, and mutual fund-based programs; and a range of plan services, including plan recordkeeping, compliance testing, participant education, and trust and custodial services. The Life Insurance segment provides life insurance products, including term insurance, such as single and survivorship versions of universal life insurance; variable universal life insurance; indexed universal life insurance products; and critical illness and long-term care riders. The Group Protection segment offers group non-medical insurance products comprising short and long-term disability, statutory disability and paid family medical leave administration and absence management services, term life, dental, vision and accident, and critical illness benefits and services to the employer marketplace through various forms of employee-paid and employer-paid plans. The company distributes its products through consultants, brokers, planners, agents, financial advisors, third-party administrators, and other intermediaries. Lincoln National Corporation was founded in 1905 and is based in Radnor, Pennsylvania.",
        fullTimeEmployees=10848,
        city="Radnor",
        state="PA",
        trailingPE=6.979346,
        dividendYield=0.033299997,
        averageVolume=1498833,
        regularMarketOpen=49.65,
        volume=1327296,
        fiftyTwoWeekHigh=77.57,
        fiftyTwoWeekLow=45.25,
        recommendationKey="buy",
        industry="Insurance—Life"
    )
    db.session.add(LNC)

    LKQ = Stock(
        name="LKQ Corporation",
        ticker="LKQ",
        marketCap=14557060096,
        dayHigh=51.51,
        dayLow=49.835,
        currentPrice=49.94,
        longBusinessSummary="LKQ Corporation distributes replacement parts, components, and systems used in the repair and maintenance of vehicles. It operates through three segments: North America, Europe, and Specialty. The company distributes bumper covers, automotive body panels, and lights, as well as automotive glass products, such as windshields; salvage products, including mechanical and collision parts comprising engines; transmissions; door assemblies; sheet metal products, such as trunk lids, fenders, and hoods; lights and bumper assemblies; scrap metal and other materials to metals recyclers; and brake pads, discs and sensors, clutches, steering and suspension products, filters, and oil and automotive fluids, as well as electrical products, including spark plugs and batteries. In addition, the company distributes recreational vehicle appliances and air conditioners, towing hitches, truck bed covers, vehicle protection products, cargo management products, wheels, tires, and suspension products. It serves collision and mechanical repair shops, and new and used car dealerships, as well as retail customers. The company operates in the United States, Canada, the United Kingdom, Germany, Belgium, the Netherlands, Luxembourg, Italy, the Czech Republic, Austria, Poland, Slovakia, Taiwan, and other European countries. LKQ Corporation was incorporated in 1998 and is headquartered in Chicago, Illinois.",
        fullTimeEmployees=46000,
        city="Chicago",
        state="IL",
        trailingPE=14.534342,
        dividendYield=0.02,
        averageVolume=1857858,
        regularMarketOpen=51,
        volume=1590700,
        fiftyTwoWeekHigh=60.43,
        fiftyTwoWeekLow=42.36,
        recommendationKey="strong_buy",
        industry="Auto Parts"
    )
    db.session.add(LKQ)

    LMT = Stock(
        name="Lockheed Martin Corporation",
        ticker="LMT",
        marketCap=116025917440,
        dayHigh=427.56,
        dayLow=419.35,
        currentPrice=420.71,
        longBusinessSummary="Lockheed Martin Corporation, a security and aerospace company, engages in the research, design, development, manufacture, integration, and sustainment of technology systems, products, and services worldwide. It operates through four segments: Aeronautics, Missiles and Fire Control, Rotary and Mission Systems, and Space. The Aeronautics segment offers combat and air mobility aircraft, unmanned air vehicles, and related technologies. The Missiles and Fire Control segment provides air and missile defense systems; tactical missiles and air-to-ground precision strike weapon systems; logistics; fire control systems; mission operations support, readiness, engineering support, and integration services; manned and unmanned ground vehicles; and energy management solutions. The Rotary and Mission Systems segment offers military and commercial helicopters, surface ships, sea and land-based missile defense systems, radar systems, sea and air-based mission and combat systems, command and control mission solutions, cyber solutions, and simulation and training solutions. The Space segment offers satellites; space transportation systems; strategic, advanced strike, and defensive missile systems; and classified systems and services in support of national security systems. This segment also provides network-enabled situational awareness and integrates space and ground-based systems to help its customers gather, analyze, and securely distribute critical intelligence data. It serves primarily serves the U.S. government, as well as foreign military sales contracted through the U.S. government. Lockheed Martin Corporation was founded in 1912 and is headquartered in Bethesda, Maryland.",
        fullTimeEmployees=114000,
        city="Bethesda",
        state="MD",
        trailingPE=19.37952,
        dividendYield=0.0257,
        averageVolume=1405745,
        regularMarketOpen=423,
        volume=937217,
        fiftyTwoWeekHigh=479.99,
        fiftyTwoWeekLow=324.23,
        recommendationKey="buy",
        industry="Aerospace & Defense"
    )
    db.session.add(LMT)

    L = Stock(
        name="Loews Corporation",
        ticker="L",
        marketCap=15101808640,
        dayHigh=60.8,
        dayLow=59.48,
        currentPrice=59.53,
        longBusinessSummary="Loews Corporation provides commercial property and casualty insurance in the United States and internationally. The company offers specialty insurance products, such as management and professional liability, and other coverage products; surety and fidelity bonds; property insurance products that include property, marine and boiler, and machinery coverages; and casualty insurance products, such as workers' compensation, general and product liability, and commercial auto and umbrella coverages. It also provides loss-sensitive insurance programs; and warranty, risk management, information, and claims administration services. The company markets its insurance products and services through independent agents, brokers, and managing general underwriters. In addition, the company is involved in the transportation and storage of natural gas and natural gas liquids(NGLs), and hydrocarbons through natural gas pipelines covering approximately 13,615 miles of interconnected pipelines; 450 miles of NGL pipelines in Louisiana and Texas; 14 underground storage fields with an aggregate gas capacity of approximately 213 billion cubic feet of natural gas; and eleven salt dome caverns and related brine infrastructure for providing brine supply services. Further, the company operates a chain of 26 hotels; and develops, manufactures, and markets a range of extrusion blow-molded and injection molded plastic containers for customers in the pharmaceutical, dairy, household chemicals, food/nutraceuticals, industrial/specialty chemicals, and water and beverage/juice segments, as well as manufactures commodity and differentiated plastic resins from recycled plastic materials. Loews Corporation was incorporated in 1969 and is headquartered in New York, New York.",
        fullTimeEmployees=10340,
        city="New York",
        state="NY",
        trailingPE=9.678101,
        dividendYield=0.004,
        averageVolume=992827,
        regularMarketOpen=60.37,
        volume=609572,
        fiftyTwoWeekHigh=68.2,
        fiftyTwoWeekLow=51.35,
        recommendationKey="hold",
        industry="Insurance—Property & Casualty"
    )
    db.session.add(L)

    LOW = Stock(
        name="Lowe's Companies, Inc.",
        ticker="LOW",
        marketCap=117717082112,
        dayHigh=185.61,
        dayLow=174.57,
        currentPrice=174.72,
        longBusinessSummary="Lowe's Companies, Inc., together with its subsidiaries, operates as a home improvement retailer in the United States and internationally. The company offers a line of products for construction, maintenance, repair, remodeling, and decorating. It provides home improvement products, such as appliances, seasonal and outdoor living, lawn and garden, lumber, kitchens and bath, tools, paint, millwork, hardware, flooring, rough plumbing, building materials, décor, lighting, and electrical. It also offers installation services through independent contractors in various product categories; extended protection plans; and in-warranty and out-of-warranty repair services. The company sells its national brand-name merchandise and private brand products to homeowners, renters, and professional customers. As of January 28, 2022, it operated 1,971 home improvement and hardware stores. The company also sells its products through websites comprising Lowes.com and Lowesforpros.com; and through mobile applications. Lowe's Companies, Inc. was founded in 1921 and is based in Mooresville, North Carolina.",
        fullTimeEmployees=200000,
        city="Mooresville",
        state="NC",
        trailingPE=15.236767,
        dividendYield=0.0165,
        averageVolume=4300701,
        regularMarketOpen=184.48,
        volume=4915824,
        fiftyTwoWeekHigh=263.31,
        fiftyTwoWeekLow=170.12,
        recommendationKey="buy",
        industry="Home Improvement Retail"
    )
    db.session.add(LOW)

    LYB = Stock(
        name="LyondellBasell Industries N.V.",
        ticker="LYB",
        marketCap=29424760832,
        dayHigh=90.51,
        dayLow=87.82,
        currentPrice=88.42,
        longBusinessSummary="LyondellBasell Industries N.V. operates as a chemical company in the United States, Germany, Mexico, Italy, Poland, France, Japan, China, the Netherlands, and internationally. The company operates in six segments: Olefins and PolyolefinsAmericas; Olefins and PolyolefinsEurope, Asia, International; Intermediates and Derivatives; Advanced Polymer Solutions; Refining; and Technology. It produces and markets olefins and co-products; polyolefins; polyethylene products, which consist of high density polyethylene, low density polyethylene, and linear low density polyethylene; and polypropylene (PP) products, such as PP homopolymers and copolymers. The company also produces and sells propylene oxide and its derivatives; oxyfuels and related products; and intermediate chemicals, such as styrene monomers, acetyls, ethylene glycols, and ethylene oxides and derivatives. In addition, it produces and markets compounds and solutions, such as polypropylene compounds, engineered plastics, masterbatches, engineered composites, colors, and powders; and advanced polymers. Further, the company refines crude oil and other crude oils of varied types and sources into gasoline and distillates; develops and licenses chemical and polyolefin process technologies; and manufactures and sells polyolefin catalysts. LyondellBasell Industries N.V. was incorporated in 2009 and is headquartered in Houston, Texas.",
        fullTimeEmployees=19100,
        city="Houston",
        state="TX",
        trailingPE=5.1644177,
        dividendYield=0.0424,
        averageVolume=2353058,
        regularMarketOpen=88.9,
        volume=1928562,
        fiftyTwoWeekHigh=117.22,
        fiftyTwoWeekLow=83.5,
        recommendationKey="buy",
        industry="Specialty Chemicals"
    )
    db.session.add(LYB)

    MTB = Stock(
        name="M&T Bank Corporation",
        ticker="MTB",
        marketCap=20991096832,
        dayHigh=168.13,
        dayLow=162.91,
        currentPrice=163.12,
        longBusinessSummary="M&T Bank Corporation operates as a bank holding company that provides commercial and retail banking services. The company's Business Banking segment offers deposit, lending, cash management, and other financial services to small businesses and professionals. Its Commercial Banking segment provides deposit products, commercial lending and leasing, letters of credit, and cash management services for middle-market and large commercial customers. The company's Commercial Real Estate segment originates, sells, and services commercial real estate loans; and offers deposit services. Its Discretionary Portfolio segment provides deposits; securities, residential real estate loans, and other assets; and short and long term borrowed funds, as well as foreign exchange services. The company's Residential Mortgage Banking segment offers residential real estate loans for consumers and sells those loans in the secondary market; and purchases servicing rights to loans originated by other entities. Its Retail Banking segment offers demand, savings, and time accounts; consumer installment loans, automobile and recreational finance loans, home equity loans and lines of credit, and credit cards; mutual funds and annuities; and other services. The company also provides trust and wealth management; fiduciary and custodial; insurance agency; institutional brokerage and securities; and investment management services. It offers its services through banking offices, business banking centers, telephone and internet banking, and automated teller machines. As of December 31, 2021, the company operates 688 domestic banking offices in New York State, Maryland, New Jersey, Pennsylvania, Delaware, Connecticut, Virginia, West Virginia, and the District of Columbia; and a full-service commercial banking office in Ontario, Canada. M&T Bank Corporation was founded in 1856 and is headquartered in Buffalo, New York.",
        fullTimeEmployees=22000,
        city="Buffalo",
        state="NY",
        trailingPE=11.696544,
        dividendYield=0.028800001,
        averageVolume=1555027,
        regularMarketOpen=166.85,
        volume=742440,
        fiftyTwoWeekHigh=186.95,
        fiftyTwoWeekLow=128.46,
        recommendationKey="buy",
        industry="Banks—Regional"
    )
    db.session.add(MTB)

    MPC = Stock(
        name="Marathon Petroleum Corporation",
        ticker="MPC",
        marketCap=54596497408,
        dayHigh=91.3301,
        dayLow=87.66,
        currentPrice=88.69,
        longBusinessSummary="Marathon Petroleum Corporation, together with its subsidiaries, operates as an integrated downstream energy company primarily in the United States. It operates in two segments, Refining & Marketing, and Midstream. The Refining & Marketing segment refines crude oil and other feedstocks at its refineries in the Gulf Coast, Mid-Continent, and West Coast regions of the United States; and purchases refined products and ethanol for resale. Its refined products include transportation fuels, such as reformulated gasolines and blend-grade gasolines; heavy fuel oil; and asphalt. This segment also manufactures aromatics, propane, propylene, and sulfur. It sells refined products to wholesale marketing customers in the United States and internationally, buyers on the spot market, and independent entrepreneurs who operate primarily Marathon branded outlets, as well as through long-term fuel supply contracts to direct dealer locations primarily under the ARCO brand. The Midstream segment transports, stores, distributes, and markets crude oil and refined products through refining logistics assets, pipelines, terminals, towboats, and barges; gathers, processes, and transports natural gas; and gathers, transports, fractionates, stores, and markets natural gas liquids. As of December 31, 2021, the company operated 7,159 brand jobber outlets in 37 states, the District of Columbia, and Mexico through independent entrepreneurs. Marathon Petroleum Corporation was founded in 1887 and is headquartered in Findlay, Ohio.",
        fullTimeEmployees=17700,
        city="Findlay",
        state="OH",
        trailingPE=6.2256074,
        dividendYield=0.0242,
        averageVolume=6723788,
        regularMarketOpen=89.52,
        volume=5305844,
        fiftyTwoWeekHigh=114.35,
        fiftyTwoWeekLow=50.19,
        recommendationKey="buy",
        industry="Oil & Gas Refining & Marketing"
    )
    db.session.add(MPC)

    MKTX = Stock(
        name="MarketAxess Holdings Inc.",
        ticker="MKTX",
        marketCap=10100979712,
        dayHigh=273.93,
        dayLow=260.64,
        currentPrice=265.63,
        longBusinessSummary="MarketAxess Holdings Inc., together with its subsidiaries, operates an electronic trading platform for institutional investor and broker-dealer companies worldwide. It offers the access to liquidity in the U.S. investment-grade bonds, U.S. high-yield bonds, and U.S. Treasuries, as well as municipal bonds, emerging market debts, Eurobonds, and other fixed income securities. The company, through its Open Trading protocols, executes bond trades between and among institutional investor and broker-dealer clients in an all-to-all anonymous trading environment for corporate bonds. It also offers trading-related products and services, including composite+ pricing and other market data products to assist clients with trading decisions; auto-execution and other execution services for clients requiring specialized workflow solutions; connectivity solutions that facilitate straight-through processing; and technology services to optimize trading environments. In addition, the company provides various pre-and post-trade services, such as trade matching, trade publication, regulatory transaction reporting, and market and reference data across a range of fixed-income and other products. MarketAxess Holdings Inc. was incorporated in 2000 and is headquartered in New York, New York.",
        fullTimeEmployees=689,
        city="New York",
        state="NY",
        trailingPE=36.337894,
        dividendYield=0.0106,
        averageVolume=408935,
        regularMarketOpen=272.53,
        volume=400126,
        fiftyTwoWeekHigh=498.97,
        fiftyTwoWeekLow=249.01,
        recommendationKey="hold",
        industry="Capital Markets"
    )
    db.session.add(MKTX)

    MAR = Stock(
        name="Marriott International, Inc.",
        ticker="MAR",
        marketCap=45168975872,
        dayHigh=146.06,
        dayLow=138.5072,
        currentPrice=138.69,
        longBusinessSummary="Marriott International, Inc. operates, franchises, and licenses hotel, residential, and timeshare properties worldwide. The company operates through U.S. and Canada, and International segments. It operates its properties under the JW Marriott, The Ritz-Carlton, Ritz-Carlton Reserve, W Hotels, The Luxury Collection, St. Regis, EDITION, Bulgari, Marriott Hotels, Sheraton, Delta Hotels, Marriott Executive Apartments, Marriott Vacation Club, Westin, Renaissance, Le Méridien, Autograph Collection, Gaylord Hotels, Tribute Portfolio, Design Hotels, Courtyard, Residence Inn, Fairfield by Marriott, SpringHill Suites, Four Points, TownePlace Suites, Aloft, AC Hotels by Marriott, Protea Hotels, Element, and Moxy brand names. As of February 15, 2022, it operated approximately 7,989 properties under 30 hotel brands in 139 countries and territories. Marriott International, Inc. was founded in 1927 and is headquartered in Bethesda, Maryland.",
        fullTimeEmployees=120000,
        city="Bethesda",
        state="MD",
        trailingPE=97.12185,
        dividendYield=0.0072000003,
        averageVolume=2538995,
        regularMarketOpen=142.73,
        volume=2241569,
        fiftyTwoWeekHigh=195.9,
        fiftyTwoWeekLow=127.23,
        recommendationKey="buy",
        industry="Lodging"
    )
    db.session.add(MAR)

    MMC = Stock(
        name="Marsh & McLennan Companies, Inc.",
        ticker="MMC",
        marketCap=78112309248,
        dayHigh=160.852,
        dayLow=154.66,
        currentPrice=154.71,
        longBusinessSummary="Marsh & McLennan Companies, Inc., a professional services company, provides advice and solutions to clients in the areas of risk, strategy, and people worldwide. It operates in two segments, Risk and Insurance Services, and Consulting. The Risk and Insurance Services segment offers risk management services, such as risk advice, risk transfer, and risk control and mitigation solutions, as well as insurance and reinsurance broking, catastrophe and financial modeling, and related advisory services; and insurance program management services. This segment serves businesses, public entities, insurance companies, associations, professional services organizations, and private clients. The Consulting segment provides health, wealth, and career consulting services and products; and specialized management, as well as economic and brand consulting services. Marsh & McLennan Companies, Inc. was founded in 1871 and is headquartered in New York, New York.",
        fullTimeEmployees=83000,
        city="New York",
        state="NY",
        trailingPE=29.245749,
        dividendYield=0.0134000005,
        averageVolume=2002269,
        regularMarketOpen=159.25,
        volume=1890791,
        fiftyTwoWeekHigh=183.14,
        fiftyTwoWeekLow=137.85,
        recommendationKey="buy",
        industry="Insurance Brokers"
    )
    db.session.add(MMC)

    MLM = Stock(
        name="Martin Marietta Materials, Inc.",
        ticker="MLM",
        marketCap=18889863168,
        dayHigh=312.435,
        dayLow=302.41,
        currentPrice=302.81,
        longBusinessSummary="Martin Marietta Materials, Inc., a natural resource-based building materials company, supplies aggregates and heavy-side building materials to the construction industry in the United States and internationally. It offers crushed stone, sand, and gravel products; ready mixed concrete and asphalt; paving products and services; and Portland and specialty cement for use in the infrastructure projects, and nonresidential and residential construction markets, as well as in the railroad, agricultural, utility, and environmental industries. The company also produces magnesia-based chemicals products that are used in industrial, agricultural, and environmental applications; and dolomitic lime primarily to customers for steel production and soil stabilization. Its chemical products are used in flame retardants, wastewater treatment, pulp and paper production, and other environmental applications. The company was founded in 1939 and is headquartered in Raleigh, North Carolina.",
        fullTimeEmployees=10000,
        city="Raleigh",
        state="NC",
        trailingPE=25.992275,
        dividendYield=0.0073,
        averageVolume=462909,
        regularMarketOpen=310,
        volume=261620,
        fiftyTwoWeekHigh=446.46,
        fiftyTwoWeekLow=295.56,
        recommendationKey="buy",
        industry="Building Materials"
    )
    db.session.add(MLM)

    MAS = Stock(
        name="Masco Corporation",
        ticker="MAS",
        marketCap=12507018240,
        dayHigh=52.3,
        dayLow=51.09,
        currentPrice=51.24,
        longBusinessSummary="Masco Corporation designs, manufactures, and distributes home improvement and building products in North America, Europe, and internationally. The company's Plumbing Products segment offers faucets, showerheads, handheld showers, valves, bath hardware and accessories, bathing units, shower bases and enclosures, sinks, toilets, acrylic tubs, shower trays, spas, exercise pools, and fitness systems; brass, copper, and composite plumbing system components; connected water products; thermoplastic solutions, extruded plastic profiles, specialized fabrications, and PEX tubing products; and other non-decorative plumbing products. This segment provides its products under the DELTA, BRIZO, PEERLESS, HANSGROHE, AXOR, KRAUS, EASY DRAIN, STEAMIST, ELITESTEAM, GINGER, NEWPORT BRASS, BRASSTECH, WALTEC, BRISTAN, HERITAGE, MIROLIN, HOT SPRING, CALDERA, FREEFLOW SPAS, FANTASY SPAS, ENDLESS POOLS, BRASSCRAFT, PLUMB SHOP, COBRA, COBRA PRO, and MASTER PLUMBER brands. Its Decorative Architectural Products segment offers paints, primers, specialty coatings, stains, and waterproofing products, as well as paint applicators and accessories; cabinet and door hardware, functional hardware, wall plates, hook and rail products, closet organization systems, and picture hanging accessories; decorative bath hardware, mirrors, and shower accessories and doors; and decorative indoor and outdoor lighting fixtures, ceiling fans, landscape lighting, and LED lighting systems. This segment provides its products under the BEHR, KILZ, WHIZZ, Elder & Jenks, LIBERTY, BRAINERD, FRANKLIN BRASS, KICHLER, and ÉLAN brands. It sells its products to the plumbing, heating, and hardware wholesalers; home centers and online retailers; hardware stores; electrical and landscape distributors; lighting showrooms; building supply outlets; and other mass merchandisers. Masco Corporation was incorporated in 1929 and is headquartered in Livonia, Michigan.",
        fullTimeEmployees=20000,
        city="Livonia",
        state="MI",
        trailingPE=28.122942,
        dividendYield=0.0202,
        averageVolume=2401675,
        regularMarketOpen=51.84,
        volume=1891130,
        fiftyTwoWeekHigh=71.06,
        fiftyTwoWeekLow=46.27,
        recommendationKey="buy",
        industry="Building Products & Equipment"
    )
    db.session.add(MAS)

    MA = Stock(
        name="Mastercard Incorporated",
        ticker="MA",
        marketCap=312738086912,
        dayHigh=336.99,
        dayLow=318.14,
        currentPrice=318.29,
        longBusinessSummary="Mastercard Incorporated, a technology company, provides transaction processing and other payment-related products and services in the United States and internationally. It facilitates the processing of payment transactions, including authorization, clearing, and settlement, as well as delivers other payment-related products and services. The company offers integrated products and value-added services for account holders, merchants, financial institutions, businesses, governments, and other organizations, such as programs that enable issuers to provide consumers with credits to defer payments; prepaid programs and management services; commercial credit and debit payment products and solutions; and payment products and solutions that allow its customers to access funds in deposit and other accounts. It also provides value-added products and services comprising cyber and intelligence solutions for parties to transact, as well as proprietary insights, drawing on principled use of consumer, and merchant data services. In addition, the company offers analytics, test and learn, consulting, managed services, loyalty, processing, and payment gateway solutions for e-commerce merchants. Further, it provides open banking and digital identity platforms services. The company offers payment solutions and services under the MasterCard, Maestro, and Cirrus. Mastercard Incorporated was founded in 1966 and is headquartered in Purchase, New York.",
        fullTimeEmployees=24000,
        city="Purchase",
        state="NY",
        trailingPE=39.150063,
        dividendYield=0.0058999998,
        averageVolume=3362529,
        regularMarketOpen=332.7,
        volume=3393005,
        fiftyTwoWeekHigh=399.92,
        fiftyTwoWeekLow=303.65,
        recommendationKey="buy",
        industry="Credit Services"
    )
    db.session.add(MA)

    MTCH = Stock(
        name="Match Group, Inc.",
        ticker="MTCH",
        marketCap=20328333312,
        dayHigh=77,
        dayLow=71.64,
        currentPrice=71.81,
        longBusinessSummary="Match Group, Inc. provides dating products worldwide. The company's portfolio of brands includes Tinder, Match, Meetic, OkCupid, Hinge, Pairs, PlentyOfFish, and OurTime, as well as a various other brands. The company was incorporated in 1986 and is based in Dallas, Texas.",
        fullTimeEmployees=2500,
        city="Dallas",
        state="TX",
        trailingPE=38.11571,
        dividendYield=None,
        averageVolume=3390008,
        regularMarketOpen=77,
        volume=2480220,
        fiftyTwoWeekHigh=182,
        fiftyTwoWeekLow=67.25,
        recommendationKey="buy",
        industry="Internet Content & Information"
    )
    db.session.add(MTCH)

    MKC = Stock(
        name="McCormick & Company, Incorporated",
        ticker="MKC",
        marketCap=23216152576,
        dayHigh=88.73,
        dayLow=86.774,
        currentPrice=86.84,
        longBusinessSummary="McCormick & Company, Incorporated manufactures, markets, and distributes spices, seasoning mixes, condiments, and other flavorful products to the food industry. It operates in two segments, Consumer and Flavor Solutions. The Consumer segment offers spices, herbs, and seasonings, as well as condiments and sauces, and desserts. This segment markets its products under the McCormick, French's, Frank's RedHot, Lawry's Cholula Hot Sauce, Gourmet Garden, Club House, and OLD BAY brands in the Americas; Ducros, Schwartz, Kamis, and Drogheria & Alimentari, and Vahiné brands in Europe, the Middle East, and Africa; McCormick and DaQiao brands in China; and McCormick, Aeroplane, and Gourmet Garden brands in Australia, as well as markets regional and ethnic brands, such as Zatarain's, Stubb's, Thai Kitchen, and Simply Asia. It also supplies its products under the private labels. This segment serves retailers comprising grocery, mass merchandise, warehouse clubs, discount and drug stores, and e-commerce retailers directly and indirectly through distributors and wholesale foodservice suppliers. The Flavor Solutions segment offers seasoning blends, spices and herbs, condiments, coating systems, and compound flavors to multinational food manufacturers and foodservice customers. It serves foodservice customers directly and indirectly through distributors. The company was founded in 1889 and is headquartered in Hunt Valley, Maryland.",
        fullTimeEmployees=14000,
        city="Hunt Valley",
        state="MD",
        trailingPE=30.794325,
        dividendYield=0.0148,
        averageVolume=1249038,
        regularMarketOpen=87.91,
        volume=1255008,
        fiftyTwoWeekHigh=107.35,
        fiftyTwoWeekLow=77.85,
        recommendationKey="hold",
        industry="Packaged Foods"
    )
    db.session.add(MKC)

    MCD = Stock(
        name="McDonald's Corporation",
        ticker="MCD",
        marketCap=181453504512,
        dayHigh=249.83,
        dayLow=242.52,
        currentPrice=242.83,
        longBusinessSummary="McDonald's Corporation operates and franchises McDonald's restaurants in the United States and internationally. Its restaurants offer hamburgers and cheeseburgers, chicken sandwiches and nuggets, wraps, fries, salads, oatmeal, shakes, desserts, sundaes, soft serve cones, bakery items, soft drinks, coffee, and beverages and other beverages, as well as breakfast menu, including biscuit and bagel sandwiches, breakfast burritos, hotcakes, and other sandwiches. As of December 31, 2021, the company operated 40,031 restaurants. McDonald's Corporation was founded in 1940 and is headquartered in Chicago, Illinois.",
        fullTimeEmployees=100000,
        city="Chicago",
        state="IL",
        trailingPE=25.034021,
        dividendYield=0.0225,
        averageVolume=2873791,
        regularMarketOpen=247.06,
        volume=2381745,
        fiftyTwoWeekHigh=271.15,
        fiftyTwoWeekLow=217.68,
        recommendationKey="buy",
        industry="Restaurants"
    )
    db.session.add(MCD)

    MRK = Stock(
        name="Merck & Co., Inc.",
        ticker="MRK",
        marketCap=232108621824,
        dayHigh=94.33,
        dayLow=91.47,
        currentPrice=91.89,
        longBusinessSummary="Merck & Co., Inc. operates as a healthcare company worldwide. It operates through two segments, Pharmaceutical and Animal Health. The Pharmaceutical segment offers human health pharmaceutical products in the areas of oncology, hospital acute care, immunology, neuroscience, virology, cardiovascular, and diabetes, as well as vaccine products, such as preventive pediatric, adolescent, and adult vaccines. The Animal Health segment discovers, develops, manufactures, and markets veterinary pharmaceuticals, vaccines, and health management solutions and services, as well as digitally connected identification, traceability, and monitoring products. It serves drug wholesalers and retailers, hospitals, and government agencies; managed health care providers, such as health maintenance organizations, pharmacy benefit managers, and other institutions; and physicians and physician distributors, veterinarians, and animal producers. The company has collaborations with AstraZeneca PLC; Bayer AG; Eisai Co., Ltd.; Ridgeback Biotherapeutics; and Gilead Sciences, Inc. to jointly develop and commercialize long-acting treatments in HIV. Merck & Co., Inc. was founded in 1891 and is headquartered in Kenilworth, New Jersey.",
        fullTimeEmployees=67000,
        city="Kenilworth",
        state="NJ",
        trailingPE=32.424133,
        dividendYield=0.0305,
        averageVolume=12421906,
        regularMarketOpen=94.11,
        volume=12416150,
        fiftyTwoWeekHigh=95.72,
        fiftyTwoWeekLow=70.89,
        recommendationKey="buy",
        industry="Drug Manufacturers—General"
    )
    db.session.add(MRK)

    MTD = Stock(
        name="Mettler-Toledo International Inc.",
        ticker="MTD",
        marketCap=25991540736,
        dayHigh=1152.22,
        dayLow=1130.11,
        currentPrice=1130.77,
        longBusinessSummary="Mettler-Toledo International Inc. engages in the manufacture and supply of precision instruments and services worldwide. It operates in five segments: U.S. Operations, Swiss Operations, Western European Operations, Chinese Operations, and Other. The company's laboratory instruments include laboratory balances, liquid pipetting solutions, automated laboratory reactors, titrators, pH meters, process analytics sensors and analyzer technologies, physical value analyzers, thermal analysis systems, and other analytical instruments; and LabX, a laboratory software platform to manage and analyze data generated from its instruments. Its industrial instruments comprise industrial weighing instruments and related terminals, automatic dimensional measurement and data capture solutions, vehicle scale systems, industrial software, metal detection, x-ray, checkweighing, camera-based imaging equipment, track-and-trace solutions, and product inspection systems. The company's retail weighing solutions consist of networked scales and software, stand-alone scales, and automated packaging and labeling solutions for handling fresh goods. It serves the life science industry, independent research organizations, and testing labs; food and beverage manufacturers; food retailers; chemical, specialty chemical, and cosmetics companies; food retailers; transportation and logistics, metals, and electronics industries; and the academic community through its direct sales force and indirect distribution channels. The company was incorporated in 1991 and is based in Columbus, Ohio.",
        fullTimeEmployees=15600,
        city="Columbus",
        state="OH",
        trailingPE=35.444004,
        dividendYield=None,
        averageVolume=142458,
        regularMarketOpen=1144.27,
        volume=157449,
        fiftyTwoWeekHigh=1714.75,
        fiftyTwoWeekLow=1082.78,
        recommendationKey="hold",
        industry="Diagnostics & Research"
    )
    db.session.add(MTD)

    MGM = Stock(
        name="MGM Resorts International",
        ticker="MGM",
        marketCap=14012524544,
        dayHigh=31.83,
        dayLow=29.815,
        currentPrice=29.88,
        longBusinessSummary="MGM Resorts International, through its subsidiaries, owns and operates casino, hotel, and entertainment resorts in the United States and Macau. The company operates through three segments: Las Vegas Strip Resorts, Regional Operations, and MGM China. Its casino resorts offer gaming, hotel, convention, dining, entertainment, retail, and other resort amenities. The company's casino operations include slots and table games, as well as online sports betting and iGaming through BetMGM. As of February 17, 2021, its portfolio consisted of 29 hotel and destination gaming offerings. The company also owns and operates Las Vegas Strip Resorts and Fallen Oak golf course. Its customers include premium gaming customers; leisure and wholesale travel customers; business travelers; and group customers, including conventions, trade associations, and small meetings. The company was formerly known as MGM MIRAGE and changed its name to MGM Resorts International in June 2010. MGM Resorts International was incorporated in 1986 and is based in Las Vegas, Nevada.",
        fullTimeEmployees=52000,
        city="Las Vegas",
        state="NV",
        trailingPE=23.961508,
        dividendYield=0.00029999999,
        averageVolume=6009861,
        regularMarketOpen=30.96,
        volume=7552683,
        fiftyTwoWeekHigh=51.17,
        fiftyTwoWeekLow=26.41,
        recommendationKey="buy",
        industry="Resorts & Casinos"
    )
    db.session.add(MGM)

    MCHP = Stock(
        name="Microchip Technology Incorporated",
        ticker="MCHP",
        marketCap=32987080704,
        dayHigh=62.92,
        dayLow=59.39,
        currentPrice=59.45,
        longBusinessSummary="Microchip Technology Incorporated develops, manufactures, and sells semiconductor products for various embedded control applications in the Americas, Europe, and Asia. The company offers general purpose 8-bit, 16-bit, and 32-bit microcontrollers; 32-bit embedded microprocessors markets; and specialized microcontrollers for automotive, industrial, computing, communications, lighting, power supplies, motor control, human machine interface, security, wired connectivity, and wireless connectivity applications. It also provides development tools that enable system designers to program microcontroller products for specific applications; field-programmable gate array (FPGA) products; and analog, interface, mixed signal, and timing products comprising power management, linear, mixed-signal, high-voltage, thermal management, discrete diodes and metal oxide semiconductor field effect transistors (MOSFETS), radio frequency (RF), drivers, safety, security, timing, USB, Ethernet, wireless, and other interface products. In addition, the company offers memory products consisting of serial electrically erasable programmable read-only memory, serial flash memories, parallel flash memories, serial static random access memories, and serial electrically erasable random access memories for the production of very small footprint devices; and licenses its SuperFlash embedded flash and Smartbits one time programmable NVM technologies to foundries, integrated device manufacturers, and design partners for use in the manufacture of microcontroller products, gate array, RF, analog, and neuromorphic compute products that require embedded non-volatile memory, as well as provides engineering services. Further, it offers wafer foundry and assembly, and test subcontracting manufacturing services; and timing systems products, application specific integrated circuits, and aerospace products. Microchip Technology Incorporated was incorporated in 1989 and is headquartered in Chandler, Arizona.",
        fullTimeEmployees=19500,
        city="Chandler",
        state="AZ",
        trailingPE=52.01225,
        dividendYield=0.0165,
        averageVolume=5204058,
        regularMarketOpen=62.18,
        volume=9588389,
        fiftyTwoWeekHigh=90,
        fiftyTwoWeekLow=56.24,
        recommendationKey="buy",
        industry="Semiconductors"
    )
    db.session.add(MCHP)

    MU = Stock(
        name="Micron Technology, Inc.",
        ticker="MU",
        marketCap=64610525184,
        dayHigh=60.59,
        dayLow=57.81,
        currentPrice=57.86,
        longBusinessSummary="Micron Technology, Inc. designs, manufactures, and sells memory and storage products worldwide. The company operates through four segments: Compute and Networking Business Unit, Mobile Business Unit, Storage Business Unit, and Embedded Business Unit. It provides memory and storage technologies comprises DRAM products, which are dynamic random access memory semiconductor devices with low latency that provide high-speed data retrieval; NAND products that are non-volatile and re-writeable semiconductor storage devices; and NOR memory products, which are non-volatile re-writable semiconductor memory devices that provide fast read speeds under the Micron and Crucial brands, as well as through private labels. The company offers memory products for the cloud server, enterprise, client, graphics, and networking markets, as well as for smartphone and other mobile-device markets; SSDs and component-level solutions for the enterprise and cloud, client, and consumer storage markets; other discrete storage products in component and wafers; and memory and storage products for the automotive, industrial, and consumer markets. It markets its products through its direct sales force, independent sales representatives, distributors, and retailers; and web-based customer direct sales channel, as well as through channel and distribution partners. Micron Technology, Inc. was founded in 1978 and is headquartered in Boise, Idaho.",
        fullTimeEmployees=44000,
        city="Boise",
        state="ID",
        trailingPE=7.2825675,
        dividendYield=0.0069999998,
        averageVolume=19693766,
        regularMarketOpen=58.98,
        volume=19370226,
        fiftyTwoWeekHigh=98.45,
        fiftyTwoWeekLow=53.6,
        recommendationKey="buy",
        industry="Semiconductors"
    )
    db.session.add(MU)

    MSFT = Stock(
        name="Microsoft Corporation",
        ticker="MSFT",
        marketCap=1925646778368,
        dayHigh=266.91,
        dayLow=256.32,
        currentPrice=256.48,
        longBusinessSummary="Microsoft Corporation develops, licenses, and supports software, services, devices, and solutions worldwide. Its Productivity and Business Processes segment offers Office, Exchange, SharePoint, Microsoft Teams, Office 365 Security and Compliance, and Skype for Business, as well as related Client Access Licenses (CAL); Skype, Outlook.com, OneDrive, and LinkedIn; and Dynamics 365, a set of cloud-based and on-premises business solutions for organizations and enterprise divisions. Its Intelligent Cloud segment licenses SQL, Windows Servers, Visual Studio, System Center, and related CALs; GitHub that provides a collaboration platform and code hosting service for developers; and Azure, a cloud platform. It also offers support services and Microsoft consulting services to assist customers in developing, deploying, and managing Microsoft server and desktop solutions; and training and certification on Microsoft products. Its More Personal Computing segment provides Windows original equipment manufacturer (OEM) licensing and other non-volume licensing of the Windows operating system; Windows Commercial, such as volume licensing of the Windows operating system, Windows cloud services, and other Windows commercial offerings; patent licensing; Windows Internet of Things; and MSN advertising. It also offers Surface, PC accessories, PCs, tablets, gaming and entertainment consoles, and other devices; Gaming, including Xbox hardware, and Xbox content and services; video games and third-party video game royalties; and Search, including Bing and Microsoft advertising. It sells its products through OEMs, distributors, and resellers; and directly through digital marketplaces, online stores, and retail stores. It has collaborations with Dynatrace, Inc., Morgan Stanley, Micro Focus, WPP plc, ACI Worldwide, Inc., and iCIMS, Inc., as well as strategic relationships with Avaya Holdings Corp. and wejo Limited. Microsoft Corporation was founded in 1975 and is based in Redmond, Washington.",
        fullTimeEmployees=181000,
        city="Redmond",
        state="WA",
        trailingPE=28.692247,
        dividendYield=0.0095,
        averageVolume=32275561,
        regularMarketOpen=263.98,
        volume=27380247,
        fiftyTwoWeekHigh=349.67,
        fiftyTwoWeekLow=241.51,
        recommendationKey="buy",
        industry="Software—Infrastructure"
    )
    db.session.add(MSFT)

    MRNA = Stock(
        name="Moderna, Inc.",
        ticker="MRNA",
        marketCap=57650933760,
        dayHigh=149.75,
        dayLow=140.95,
        currentPrice=142.19,
        longBusinessSummary="Moderna, Inc., a biotechnology company, develops therapeutics and vaccines based on messenger RNA for the treatment of infectious diseases, immuno-oncology, rare diseases, cardiovascular diseases, and auto-immune diseases in the United States and internationally. The company has 44 development programs, which includes 26 in clinical trials across seven modalities comprising prophylactic vaccines, systemic secreted and cell surface therapeutics, cancer vaccines, intratumoral immuno-oncology, localized regenerative therapeutics, systemic intracellular therapeutics, and inhaled pulmonary therapeutics. The company has strategic alliances with AstraZeneca PLC; Merck & Co., Inc.; Vertex Pharmaceuticals Incorporated; Vertex Pharmaceuticals (Europe) Limited; Carisma Therapeutics, Inc.; Metagenomi, Inc.; the Defense Advanced Research Projects Agency; Biomedical Advanced Research and Development Authority; Institute for Life Changing Medicines; and The Bill & Melinda Gates Foundation, as well as a collaboration and license agreement with Chiesi Farmaceutici S.P.A. The company was formerly known as Moderna Therapeutics, Inc. and changed its name to Moderna, Inc. in August 2018. Moderna, Inc. was founded in 2010 and is headquartered in Cambridge, Massachusetts.",
        fullTimeEmployees=2700,
        city="Cambridge",
        state="MA",
        trailingPE=8.518453,
        dividendYield=None,
        averageVolume=6016019,
        regularMarketOpen=143.4,
        volume=3988199,
        fiftyTwoWeekHigh=497.49,
        fiftyTwoWeekLow=115.61,
        recommendationKey="buy",
        industry="Biotechnology"
    )
    db.session.add(MRNA)

    MHK = Stock(
        name="Mohawk Industries, Inc.",
        ticker="MHK",
        marketCap=8654845952,
        dayHigh=131.11,
        dayLow=127.635,
        currentPrice=127.78,
        longBusinessSummary="Mohawk Industries, Inc. designs, manufactures, sources, distributes, and markets flooring products for remodeling and new constructions of residential and commercial spaces in the United States, Europe, Russia, and internationally. It operates through three segments: Global Ceramic, Flooring North America (Flooring NA), and Flooring Rest of the World (Flooring ROW). The Global Ceramic segment provides a range of ceramic tile, porcelain tile, and natural stone products; and sources, markets, and distributes other tile related products. This segment markets and distributes its products under the American Olean, Daltile, Eliane, EmilGroup, KAI, Kerama Marazzi, Marazzi, and Ragno brands. The Flooring NA segment offers floor covering product lines in a range of colors, textures, and patterns, including carpets, carpet tiles, rugs and mats, carpet pads, hardwood, laminate, medium-density fiberboards, luxury vinyl tiles (LVT), and sheet vinyl products. This segment markets and distributes its flooring products under the Aladdin Commercial, Durkan, IVC, Karastan, Mohawk, Mohawk Group, Mohawk Home, Pergo, Portico, and Quick-Step brands. The Flooring ROW segment provides wood flooring and vinyl flooring, as well as laminates, roofing elements, sheet vinyl, LVT, insulation boards, medium-density fiberboards, chipboards, and other woods products under the Feltex, Godfrey Hirst, Hycraft, IVC Commercial, IVC Home, Leoline, Moduleo, Pergo, Quick-Step, and Unilin and Xtratherm brands; and licenses its intellectual property to flooring manufacturers. Mohawk Industries, Inc. was incorporated in 1988 and is headquartered in Calhoun, Georgia.",
        fullTimeEmployees=43000,
        city="Calhoun",
        state="GA",
        trailingPE=2.5609605,
        dividendYield=None,
        averageVolume=643435,
        regularMarketOpen=129.72,
        volume=563757,
        fiftyTwoWeekHigh=211.75,
        fiftyTwoWeekLow=114.96,
        recommendationKey="hold",
        industry="Furnishings, Fixtures & Appliances"
    )
    db.session.add(MHK)

    MOH = Stock(
        name="Molina Healthcare, Inc.",
        ticker="MOH",
        marketCap=15898232832,
        dayHigh=279.98,
        dayLow=272,
        currentPrice=272.23,
        longBusinessSummary="Molina Healthcare, Inc. provides managed health care services to low-income families and individuals under the Medicaid and Medicare programs and through the state insurance marketplaces. It operates in four segments, Medicaid, Medicare, Marketplace, and Other. As of December 31, 2021, the company served the company served approximately 5.2 million members eligible for Medicaid, Medicare, and other government-sponsored healthcare programs in 18 states. The company was founded in 1980 and is headquartered in Long Beach, California.",
        fullTimeEmployees=14000,
        city="Long Beach",
        state="CA",
        trailingPE=27.119946,
        dividendYield=None,
        averageVolume=413848,
        regularMarketOpen=275.68,
        volume=235441,
        fiftyTwoWeekHigh=350.19,
        fiftyTwoWeekLow=243.32,
        recommendationKey="buy",
        industry="Healthcare Plans"
    )
    db.session.add(MOH)

    MDLZ = Stock(
        name="Mondelez International, Inc.",
        ticker="MDLZ",
        marketCap=86097551360,
        dayHigh=63.18,
        dayLow=61.555,
        currentPrice=61.72,
        longBusinessSummary="Mondelez International, Inc., through its subsidiaries, manufactures, markets, and sells snack food and beverage products in the Latin America, North America, Asia, the Middle East, Africa, and Europe. It provides biscuits, including cookies, crackers, and salted snacks; chocolates; and gums and candies, as well as various cheese and grocery, and powdered beverage products. The company's snack brand portfolio includes Cadbury, Milka, and Toblerone chocolates; Oreo, belVita, and LU biscuits; Halls candies; Trident gums; and Tang powdered beverages. It serves supermarket chains, wholesalers, supercenters, club stores, mass merchandisers, distributors, convenience stores, gasoline stations, drug stores, value stores, and other retail food outlets through direct store delivery, company-owned and satellite warehouses, third party distributors, and other facilities, as well as through independent sales offices and agents, and e-commerce channels. The company was formerly known as Kraft Foods Inc. and changed its name to Mondelez International, Inc. in October 2012. Mondelez International, Inc. was incorporated in 2000 and is headquartered in Chicago, Illinois.",
        fullTimeEmployees=79000,
        city="Chicago",
        state="IL",
        trailingPE=19.649794,
        dividendYield=0.0211,
        averageVolume=8154954,
        regularMarketOpen=62.87,
        volume=6735151,
        fiftyTwoWeekHigh=69.47,
        fiftyTwoWeekLow=57.63,
        recommendationKey="buy",
        industry="Confectioners"
    )
    db.session.add(MDLZ)

    MPWR = Stock(
        name="Monolithic Power Systems, Inc.",
        ticker="MPWR",
        marketCap=18304913408,
        dayHigh=428.59,
        dayLow=395.84,
        currentPrice=397.13,
        longBusinessSummary="Monolithic Power Systems, Inc. engages in the design, development, marketing, and sale of semiconductor-based power electronics solutions for the computing and storage, automotive, industrial, communications, and consumer markets. The company provides direct current (DC) to DC integrated circuits (ICs) that are used to convert and control voltages of various electronic systems, such as portable electronic devices, wireless LAN access points, computers and notebooks, monitors, infotainment applications, and medical equipment. It also offers lighting control ICs for backlighting that are used in systems, which provide the light source for LCD panels in notebook computers, monitors, car navigation systems, and televisions, as well as for general illumination products. The company sells its products through third-party distributors and value-added resellers, as well as directly to original equipment manufacturers, original design manufacturers, electronic manufacturing service providers, and other end customers in China, Taiwan, Europe, South Korea, Southeast Asia, Japan, the United States, and internationally. Monolithic Power Systems, Inc. was incorporated in 1997 and is headquartered in Kirkland, Washington.",
        fullTimeEmployees=2773,
        city="Kirkland",
        state="WA",
        trailingPE=89.0426,
        dividendYield=0.0069,
        averageVolume=492775,
        regularMarketOpen=418.59,
        volume=435885,
        fiftyTwoWeekHigh=580,
        fiftyTwoWeekLow=351.21,
        recommendationKey="buy",
        industry="Semiconductors"
    )
    db.session.add(MPWR)

    MNST = Stock(
        name="Monster Beverage Corporation",
        ticker="MNST",
        marketCap=48051113984,
        dayHigh=94.715,
        dayLow=90.39,
        currentPrice=90.81,
        longBusinessSummary="Monster Beverage Corporation, through its subsidiaries, engages in development, marketing, sale, and distribution of energy drink beverages and concentrates in the United States and internationally. The company operates through three segments: Monster Energy Drinks, Strategic Brands, and Other. It offers carbonated energy drinks, non-carbonated, ready-to-drink iced teas, lemonades, juice cocktails, single-serve juices and fruit beverages, ready-to-drink dairy and coffee drinks, energy drinks, sports drinks and single-serve still waters, and sodas that are considered natural, sparkling juices, and flavored sparkling beverages. The company sells its products to bottlers, full-service beverage distributors, as well as sells directly to retail grocery and speciality chains, wholesalers, club stores, mass merchandisers, convenience chains, drug stores, foodservice customers, value stores, e-commerce retailers, and the military; and concentrates and/or beverage bases to authorized bottling and canning operations. It provides its products under the Monster Energy, Monster Energy Ultra, Monster Rehab, Monster Energy Nitro, Java Monster, Muscle Monster, Espresso Monster, Punch Monster, Juice Monster, Monster Hydro Energy Water, Monster Hydro Super Sport, Monster HydroSport Super Fuel, Monster Super Fuel, Monster Dragon Tea, Reign Total Body Fuel, and Reign Inferno Thermogenic Fuel, as well as NOS, Full Throttle, Burn, Mother, Nalu, Ultra Energy, Play and Power Play (stylized), Relentless, BPM, BU, Gladiator, Samurai, Live+, Predator, Fury, and True North brands. The company was formerly known as Hansen Natural Corporation and changed its name to Monster Beverage Corporation in January 2012. Monster Beverage Corporation was founded in 1985 and is headquartered in Corona, California.",
        fullTimeEmployees=3458,
        city="Corona",
        state="CA",
        trailingPE=31.751749,
        dividendYield=None,
        averageVolume=3092046,
        regularMarketOpen=94.17,
        volume=3515542,
        fiftyTwoWeekHigh=99.89,
        fiftyTwoWeekLow=71.78,
        recommendationKey="buy",
        industry="Beverages—Non-Alcoholic"
    )
    db.session.add(MNST)

    MCO = Stock(
        name="Moody's Corporation",
        ticker="MCO",
        marketCap=50304540672,
        dayHigh=279.6624,
        dayLow=270.06,
        currentPrice=270.6,
        longBusinessSummary="Moody's Corporation operates as an integrated risk assessment firm worldwide. It operates in two segments, Moody's Investors Service and Moody's Analytics. The Moody's Investors Service segment publishes credit ratings and provides assessment services on various debt obligations, programs and facilities, and entities that issue such obligations, such as various corporate, financial institution, and governmental obligations, as well as and structured finance securities. This segment provides ratings in approximately 140 countries. Its ratings are disseminated through press releases to the public through electronic media, including the internet and real-time information systems used by securities traders and investors. This segment has rated approximately 5,000 non-financial corporates; 3,600 financial institutions; 16,000 public finance issuers; 145 sovereigns; 47 supranational institutions; 459 sub-sovereigns; and 1,000 infrastructure and project finance issuers, as well as 9,100 structured finance deals. The Moody's Analytics segment develops a range of products and services that support the risk management activities of institutional participants in financial markets; and offers subscription based research, data, and analytical products comprising credit ratings, credit research, quantitative credit scores and other analytical tools, economic research and forecasts, business intelligence and company information products, commercial real estate data and analytical tools, and on-line and classroom-based training services, as well as credentialing and certification services. It also offers offshore analytical and research services with learning solutions and certification programs; and software solutions, as well as related risk management services. The company was formerly known as Dun and Bradstreet Company and changed its name to Moody's Corporation in September 2000. Moody's Corporation was founded in 1900 and is headquartered in New York, New York.",
        fullTimeEmployees=13460,
        city="New York",
        state="NY",
        trailingPE=24.242968,
        dividendYield=0.0097,
        averageVolume=1031774,
        regularMarketOpen=276.96,
        volume=739689,
        fiftyTwoWeekHigh=407.94,
        fiftyTwoWeekLow=251.01,
        recommendationKey="buy",
        industry="Financial Data & Stock Exchanges"
    )
    db.session.add(MCO)

    MS = Stock(
        name="Morgan Stanley",
        ticker="MS",
        marketCap=140251086848,
        dayHigh=81.22,
        dayLow=78.05,
        currentPrice=78.16,
        longBusinessSummary="Morgan Stanley, a financial holding company, provides various financial products and services to corporations, governments, financial institutions, and individuals in the Americas, Europe, the Middle East, Africa, and Asia. It operates through Institutional Securities, Wealth Management, and Investment Management segments. The Institutional Securities segment offers capital raising and financial advisory services, including services related to the underwriting of debt, equity, and other securities, as well as advice on mergers and acquisitions, restructurings, real estate, and project finance. This segment also provides sales and trading services, such as sales, financing, prime brokerage, and market-making services in equity and fixed income products consisting of foreign exchange and commodities; corporate and commercial real estate loans, which provides secured lending facilities and financing for sales and trading customers, and asset-backed and mortgage lending; and wealth management services, investment, and research services. The Wealth Management segment offers financial advisor-led brokerage and investment advisory services; self-directed brokerage services; financial and wealth planning services; workplace services, including stock plan administration; annuity and insurance products; securities-based lending, residential real estate loans, and other lending products; banking; and retirement plan services to individual investors and small to medium-sized businesses and institutions. The Investment Management segment provides equity, fixed income, liquidity, and alternative/other products to benefit/defined contribution plans, foundations, endowments, government entities, sovereign wealth funds, insurance companies, and third-party fund sponsors and corporations through institutional and intermediary channels. Morgan Stanley was founded in 1924 and is headquartered in New York, New York.",
        fullTimeEmployees=76541,
        city="New York",
        state="NY",
        trailingPE=9.979571,
        dividendYield=0.0348,
        averageVolume=8749604,
        regularMarketOpen=80.38,
        volume=10004439,
        fiftyTwoWeekHigh=109.73,
        fiftyTwoWeekLow=72.23,
        recommendationKey="none",
        industry="Capital Markets"
    )
    db.session.add(MS)

    MOS = Stock(
        name="The Mosaic Company",
        ticker="MOS",
        marketCap=18253803520,
        dayHigh=51.35,
        dayLow=48.92,
        currentPrice=49.28,
        longBusinessSummary="The Mosaic Company, through its subsidiaries, produces and markets concentrated phosphate and potash crop nutrients in North America and internationally. The company operates through three segments: Phosphates, Potash, and Mosaic Fertilizantes. It owns and operates mines, which produce concentrated phosphate crop nutrients, such as diammonium phosphate, monoammonium phosphate, and ammoniated phosphate products; and phosphate-based animal feed ingredients primarily under the Biofos and Nexfos brand names, as well as produces a double sulfate of potash magnesia product under K-Mag brand name. The company also produces and sells potash for use in the manufacturing of mixed crop nutrients and animal feed ingredients, and for industrial use; and for use in the de-icing and as a water softener regenerant. In addition, it provides nitrogen-based crop nutrients, animal feed ingredients, and other ancillary services; and purchases and sells phosphates, potash, and nitrogen products. The company sells its products to wholesale distributors, retail chains, farmers, cooperatives, independent retailers, and national accounts. The Mosaic Company was incorporated in 2004 and is headquartered in Tampa, Florida.",
        fullTimeEmployees=12525,
        city="Tampa",
        state="FL",
        trailingPE=10.547945,
        dividendYield=0.0072000003,
        averageVolume=8679911,
        regularMarketOpen=49.94,
        volume=7520394,
        fiftyTwoWeekHigh=79.28,
        fiftyTwoWeekLow=28.26,
        recommendationKey="buy",
        industry="Agricultural Inputs"
    )
    db.session.add(MOS)

    MSI = Stock(
        name="Motorola Solutions, Inc.",
        ticker="MSI",
        marketCap=35508903936,
        dayHigh=218.575,
        dayLow=210.19,
        currentPrice=210.24,
        longBusinessSummary="Motorola Solutions, Inc. provides mission critical communications and analytics in the United States, the United Kingdom, Canada, and internationally. The company operates in two segments, Products and Systems Integration, and Software and Services. The Products and Systems Integration segment offers a portfolio of infrastructure, devices, accessories, and video security devices and infrastructure, as well as the implementation, and integration of systems, devices, software, and applications for government, public safety, and commercial customers who operate private communications networks and video security solutions, as well as manage a mobile workforce. Its land mobile radio communications and video security and access control devices include two-way portable and vehicle-mounted radios, fixed and mobile video cameras, and accessories; radio network core and central processing software, base stations, consoles, and repeaters; and video analytics, network video management hardware and software, and access control solutions. The Software and Services segment provides repair, technical support, and hardware maintenance services. This segment also offers monitoring, software updates, and cybersecurity services; and public safety and enterprise command center software, unified communications applications, and video software solutions through on-premise and as a service. It serves government, public safety, and commercial customers. The company was formerly known as Motorola, Inc. and changed its name to Motorola Solutions, Inc. in January 2011. Motorola Solutions, Inc. was founded in 1928 and is headquartered in Chicago, Illinois.",
        fullTimeEmployees=18700,
        city="Chicago",
        state="IL",
        trailingPE=29.018635,
        dividendYield=0.0147,
        averageVolume=879077,
        regularMarketOpen=217.41,
        volume=422408,
        fiftyTwoWeekHigh=273.65,
        fiftyTwoWeekLow=195.18,
        recommendationKey="buy",
        industry="Communication Equipment"
    )
    db.session.add(MSI)

    MSCI = Stock(
        name="MSCI Inc.",
        ticker="MSCI",
        marketCap=34060382208,
        dayHigh=436.81,
        dayLow=412.44,
        currentPrice=413.12,
        longBusinessSummary="MSCI Inc., together with its subsidiaries, provides investment decision support tools for the clients to manage their investment processes worldwide. It operates through four segments: Index, Analytics, ESG and Climate, and All Other  Private Assets. The Index segment provides indexes for use in various areas of the investment process, including indexed product creation, such as ETFs, mutual funds, annuities, futures, options, structured products, over-the-counter derivatives; performance benchmarking; portfolio construction and rebalancing; and asset allocation, as well as licenses GICS and GICS Direct. The Analytics segment offers risk management, performance attribution and portfolio management content, application, and service that provides an integrated view of risk and return, and an analysis of market, credit, liquidity, and counterparty risk across asset classes; managed services, including consolidation of client portfolio data from various sources, review and reconciliation of input data and results, and customized reporting; and HedgePlatform to measure, evaluate, and monitor the risk of hedge fund investments. The ESG and Climate segment provides products and services that help institutional investors understand how ESG factors impact the long-term risk and return of their portfolio and individual security-level investments; and data, ratings, research, and tools to help investors navigate increasing regulation. The All Other  Private Assets segment includes real estate market and transaction data, benchmarks, return-analytics, climate assessments and market insights for funds, investors, and managers; business intelligence to real estate owners, managers, developers, and brokers; and offers investment decision support tools for private capital. It serves asset owners and managers, financial intermediaries, wealth managers, real estate professionals, and corporates. MSCI Inc. was incorporated in 1998 and is headquartered in New York, New York.",
        fullTimeEmployees=4361,
        city="New York",
        state="NY",
        trailingPE=50.13592,
        dividendYield=0.010199999,
        averageVolume=592120,
        regularMarketOpen=429.03,
        volume=316915,
        fiftyTwoWeekHigh=679.85,
        fiftyTwoWeekLow=376.41,
        recommendationKey="buy",
        industry="Financial Data & Stock Exchanges"
    )
    db.session.add(MSCI)

    NDAQ = Stock(
        name="Nasdaq, Inc.",
        ticker="NDAQ",
        marketCap=25862555648,
        dayHigh=159.34,
        dayLow=154.57,
        currentPrice=154.66,
        longBusinessSummary="Nasdaq, Inc. operates as a technology company that serves capital markets and other industries worldwide. The Market Technology segment includes anti financial crime technology business, which offers Nasdaq Trade Surveillance, a SaaS solution for brokers and other market participants to assist them in complying with market rules, regulations, and internal market surveillance policies; Nasdaq Automated Investigator, a cloud-deployed anti-money laundering tool; and Verafin, a SaaS technology provider of anti-financial crime management solutions. This segment also handles assets, such as cash equities, equity derivatives, currencies, interest-bearing securities, commodities, energy products, and digital currencies. The Investment Intelligence segment sells and distributes historical and real-time market data; develops and licenses Nasdaq-branded indexes and financial products; and provides investment insights and workflow solutions. The Corporate Platforms segment operates listing platforms; and offers investor relations intelligence and governance solutions. As of December 31, 2021, it had 4,178 companies listed securities on The Nasdaq Stock Market, including 1,632 listings on The Nasdaq Global Select Market; 1,169 on The Nasdaq Global Market; and 1,377 on The Nasdaq Capital Market. The Market Services segment includes equity derivative trading and clearing, cash equity trading, fixed income and commodities trading and clearing, and trade management service businesses. This segment operates various exchanges and other marketplace facilities across various asset classes, which include derivatives, commodities, cash equity, debt, structured products, and exchange traded products; and provides broker, clearing, settlement, and central depository services. The company was formerly known as The NASDAQ OMX Group, Inc. and changed its name to Nasdaq, Inc. in September 2015. Nasdaq, Inc. was founded in 1971 and is headquartered in New York, New York.",
        fullTimeEmployees=5814,
        city="New York",
        state="NY",
        trailingPE=22.505821,
        dividendYield=0.0163,
        averageVolume=963854,
        regularMarketOpen=157.93,
        volume=644342,
        fiftyTwoWeekHigh=214.96,
        fiftyTwoWeekLow=140.31,
        recommendationKey="buy",
        industry="Financial Data & Stock Exchanges"
    )
    db.session.add(NDAQ)

    NTAP = Stock(
        name="NetApp, Inc.",
        ticker="NTAP",
        marketCap=14590327808,
        dayHigh=68.09,
        dayLow=65.41,
        currentPrice=65.64,
        longBusinessSummary="NetApp, Inc. provides software, systems, and cloud services to manage and share data on-premises, and private and public clouds worldwide. The company offers cloud storage services, including NetApp Cloud Volumes; cloud control solutions, such as NetApp Cloud Manager and NetApp Virtual Desktop Service; cloud services and analytics comprising NetApp Cloud Insights, NetApp Cloud Sync, NetApp Cloud Compliance, NetApp Cloud Tiering, NetApp SaaS Backup, NetApp Cloud Backup, and NetApp Global File Cache; and Cloud Optimization solutions, such as Spot by NetApp, Spot Cloud Analyzer by NetApp, Spot Eco by NetApp, Spot Ocean by NetApp, Spot Wave by NetApp, Spot Elastigroup by NetApp, and NetApp Virtual Desktop Managed Service. It provides data storage solutions comprising NetApp All-Flash FAS series, NetApp Fabric Attached Storage, NetApp FlexPod, NetApp E/EF series, NetApp StorageGRID, NetApp SolidFire, and NetApp HCI; data protection solutions, such as NetApp SnapCenter Backup Management, NetApp SnapMirror Data Replication, NetApp SnapLock Data Compliance, and NetApp Data Availability Services; and data management solutions, including NetApp ONTAP Storage Management System, NetApp ElementOS software, NetApp SANtricity software, NetApp Active IQ Digital Advisor, OnCommand Insight, and OnCommand Workflow Automation. In addition, the company offers application-aware data management service under the NetApp Astra name; and payment solutions and storage-as-a-service under the NetApp Keystone name. Further, it provides assessment, design, consulting, and implementation services. The company serves the energy, financial service, government, technology, internet, life science, healthcare service, manufacturing, media, entertainment, animation, video postproduction, and telecommunication markets through a direct sales force and an ecosystem of partners. NetApp, Inc. was incorporated in 1992 and is headquartered in San Jose, California.",
        fullTimeEmployees=11000,
        city="San Jose",
        state="CA",
        trailingPE=15.959154,
        dividendYield=0.028099999,
        averageVolume=1972143,
        regularMarketOpen=67.47,
        volume=1333295,
        fiftyTwoWeekHigh=96.82,
        fiftyTwoWeekLow=62.78,
        recommendationKey="buy",
        industry="Computer Hardware"
    )
    db.session.add(NTAP)

    NFLX = Stock(
        name="Netflix, Inc.",
        ticker="NFLX",
        marketCap=79554183168,
        dayHigh=192.2,
        dayLow=179.37,
        currentPrice=179.6,
        longBusinessSummary="Netflix, Inc. provides entertainment services. It offers TV series, documentaries, feature films, and mobile games across various genres and languages. The company provides members the ability to receive streaming content through a host of internet-connected devices, including TVs, digital video players, television set-top boxes, and mobile devices. It also provides DVDs-by-mail membership services in the United States. The company has approximately 222 million paid members in 190 countries. Netflix, Inc. was incorporated in 1997 and is headquartered in Los Gatos, California.",
        fullTimeEmployees=11300,
        city="Los Gatos",
        state="CA",
        trailingPE=16.193312,
        dividendYield=None,
        averageVolume=13579724,
        regularMarketOpen=189.2,
        volume=7201897,
        fiftyTwoWeekHigh=700.99,
        fiftyTwoWeekLow=162.71,
        recommendationKey="hold",
        industry="Entertainment"
    )
    db.session.add(NFLX)

    NWL = Stock(
        name="Newell Brands Inc.",
        ticker="NWL",
        marketCap=8261267968,
        dayHigh=20.2,
        dayLow=19.405,
        currentPrice=19.42,
        longBusinessSummary="Newell Brands Inc. designs, manufactures, sources, and distributes consumer and commercial products worldwide. It operates in five segments: Commercial Solutions, Home Appliances, Home Solutions, Learning and Development, and Outdoor and Recreation. The Commercial Solutions segment provides commercial cleaning and maintenance solutions; closet and garage organization products; hygiene systems and material handling solutions; and home and security, and smoke and carbon monoxide alarms products under the BRK, First Alert, Mapa, Quickie, Rubbermaid, Rubbermaid Commercial Products, and Spontex brands. The Home Appliances segment offers kitchen appliances under the Crock-Pot, Mr. Coffee, Oster, and Sunbeam brands. The Home Solutions segment provides food and home storage; fresh preserving; vacuum sealing; and gourmet cookware, bakeware, cutlery, and home fragrance products under the Ball, Calphalon, Chesapeake Bay Candle, FoodSaver, Rubbermaid, Sistema, WoodWick, and Yankee Candle brands. The Learning and Development segment offers writing instruments, including markers and highlighters, pens, and pencils; art products; activity-based adhesive and cutting products; labeling solutions; and baby gear and infant care products under the Aprica, Baby Jogger, Graco, NUK, Tigex, Dymo, Elmer's, EXPO, Graco, Mr. Sketch, NUK, Paper Mate, Parker, Prismacolor, Sharpie, Waterman, and X-Acto brands. The Outdoor and Recreation segment provides outdoor and outdoor-related products under the Campingaz, Coleman, Contigo, ExOfficio, and Marmot brands. It serves warehouse clubs, department and drug/grocery stores, mass merchants, home centers, office superstores and supply stores, contract stationers, and distributors, e-commerce, sporting goods, specialty, and travel retailers. The company was formerly known as Newell Rubbermaid Inc. and changed its name to Newell Brands Inc. in April 2016. Newell Brands Inc. was founded in 1903 and is based in Atlanta, Georgia.",
        fullTimeEmployees=32000,
        city="Atlanta",
        state="GA",
        trailingPE=13.77305,
        dividendYield=0.0405,
        averageVolume=3643243,
        regularMarketOpen=19.82,
        volume=2851770,
        fiftyTwoWeekHigh=27.82,
        fiftyTwoWeekLow=17.4,
        recommendationKey="buy",
        industry="Household & Personal Products"
    )
    db.session.add(NWL)

    NEM = Stock(
        name="Newmont Corporation",
        ticker="NEM",
        marketCap=50206507008,
        dayHigh=64.25,
        dayLow=62.765,
        currentPrice=62.96,
        longBusinessSummary="Newmont Corporation engages in the production and exploration of gold. It also explores for copper, silver, zinc, and lead. The company has operations and/or assets in the United States, Canada, Mexico, Dominican Republic, Peru, Suriname, Argentina, Chile, Australia, and Ghana. As of December 31, 2021, it had proven and probable gold reserves of 92.8 million ounces and land position of 62,800 square kilometers. The company was founded in 1916 and is headquartered in Denver, Colorado.",
        fullTimeEmployees=14400,
        city="Denver",
        state="CO",
        trailingPE=24.816713,
        dividendYield=0.0337,
        averageVolume=6447870,
        regularMarketOpen=64.16,
        volume=5580113,
        fiftyTwoWeekHigh=86.37,
        fiftyTwoWeekLow=52.6,
        recommendationKey="hold",
        industry="Gold"
    )
    db.session.add(NEM)

    NWSA = Stock(
        name="News Corporation",
        ticker="NWSA",
        marketCap=9201447936,
        dayHigh=16.12,
        dayLow=15.48,
        currentPrice=15.49,
        longBusinessSummary="News Corporation, a media and information services company, focuses on creating and distributing content for consumers and businesses worldwide. It operates in six segments: Digital Real Estate Services, Subscription Video Services, Dow Jones, Book Publishing, News Media, and Other. The company distributes content and data products, including The Wall Street Journal, Factiva, Dow Jones Risk & Compliance, Dow Jones Newswires, Barron's, MarketWatch, and Investor's Business Daily through various media channels, such as newspapers, newswires, websites, applications for mobile devices, tablets and e-book readers, newsletters, magazines, proprietary databases, live journalism, videos, and podcasts. It also owns and operates daily, Sunday, weekly, and bi-weekly newspapers comprising The Australian, The Weekend Australian, The Daily Telegraph, The Sunday Telegraph, Herald Sun, Sunday Herald Sun, The Courier Mail, The Sunday Mail, The Advertiser, Sunday Mail, The Sun, The Sun on Sunday, The Times, The Sunday Times, and New York Post, as well as digital mastheads and other websites. In addition, the company publishes general fiction, nonfiction, children's, and religious books; provides video sports, entertainment, and news services to pay-TV subscribers and other commercial licensees primarily through cable, satellite, and internet distribution; and broadcasts rights to live sporting events. Further, it offers property and property-related advertising and services on its websites and mobile applications; online real estate services; and professional software and service products, as well as financial services. The company is headquartered in New York, New York.",
        fullTimeEmployees=24000,
        city="New York",
        state="NY",
        trailingPE=18.662651,
        dividendYield=0.0112,
        averageVolume=3290856,
        regularMarketOpen=15.83,
        volume=3526276,
        fiftyTwoWeekHigh=26.42,
        fiftyTwoWeekLow=14.95,
        recommendationKey="buy",
        industry="Broadcasting"
    )
    db.session.add(NWSA)

    NWS = Stock(
        name="News Corporation",
        ticker="NWS",
        marketCap=9313197056,
        dayHigh=16.43,
        dayLow=15.78,
        currentPrice=15.81,
        longBusinessSummary="News Corporation, a media and information services company, focuses on creating and distributing content for consumers and businesses worldwide. It operates in six segments: Digital Real Estate Services, Subscription Video Services, Dow Jones, Book Publishing, News Media, and Other. The company distributes content and data products, including The Wall Street Journal, Factiva, Dow Jones Risk & Compliance, Dow Jones Newswires, Barron's, MarketWatch, and Investor's Business Daily through various media channels, such as newspapers, newswires, websites, applications for mobile devices, tablets and e-book readers, newsletters, magazines, proprietary databases, live journalism, videos, and podcasts. It also owns and operates daily, Sunday, weekly, and bi-weekly newspapers comprising The Australian, The Weekend Australian, The Daily Telegraph, The Sunday Telegraph, Herald Sun, Sunday Herald Sun, The Courier Mail, The Sunday Mail, The Advertiser, Sunday Mail, The Sun, The Sun on Sunday, The Times, The Sunday Times, and New York Post, as well as digital mastheads and other websites. In addition, the company publishes general fiction, nonfiction, children's, and religious books; provides video sports, entertainment, and news services to pay-TV subscribers and other commercial licensees primarily through cable, satellite, and internet distribution; and broadcasts rights to live sporting events. Further, it offers property and property-related advertising and services on its websites and mobile applications; online real estate services; and professional software and service products, as well as financial services. The company is headquartered in New York, New York.",
        fullTimeEmployees=24000,
        city="New York",
        state="NY",
        trailingPE=19.048193,
        dividendYield=0.0111,
        averageVolume=727927,
        regularMarketOpen=16.11,
        volume=813570,
        fiftyTwoWeekHigh=25.69,
        fiftyTwoWeekLow=15.18,
        recommendationKey="none",
        industry="Broadcasting"
    )
    db.session.add(NWS)

    NEE = Stock(
        name="NextEra Energy, Inc.",
        ticker="NEE",
        marketCap=149985984512,
        dayHigh=78.33,
        dayLow=76.23,
        currentPrice=76.44,
        longBusinessSummary="NextEra Energy, Inc., through its subsidiaries, generates, transmits, distributes, and sells electric power to retail and wholesale customers in North America. The company generates electricity through wind, solar, nuclear, coal, and natural gas facilities. It also develops, constructs, and operates long-term contracted assets that consists of clean energy solutions, such as renewable generation facilities, battery storage projects, and electric transmission facilities; sells energy commodities; and owns, develops, constructs, manages and operates electric generation facilities in wholesale energy markets. As of December 31, 2021, the company had approximately 28,564 megawatts of net generating capacity; approximately 77,000 circuit miles of transmission and distribution lines; and 696 substations. It serves approximately 11 million people through approximately 5.7 million customer accounts in the east and lower west coasts of Florida. The company was formerly known as FPL Group, Inc. and changed its name to NextEra Energy, Inc. in 2010. The company was founded in 1925 and is headquartered in Juno Beach, Florida.",
        fullTimeEmployees=15000,
        city="Juno Beach",
        state="FL",
        trailingPE=124.49512,
        dividendYield=0.0226,
        averageVolume=10312819,
        regularMarketOpen=77.91,
        volume=6001483,
        fiftyTwoWeekHigh=93.73,
        fiftyTwoWeekLow=67.22,
        recommendationKey="buy",
        industry="Utilities—Regulated Electric"
    )
    db.session.add(NEE)

    NLSN = Stock(
        name="Nielsen Holdings plc",
        ticker="NLSN",
        marketCap=8492212736,
        dayHigh=24.27,
        dayLow=23.5,
        currentPrice=23.66,
        longBusinessSummary="Nielsen Holdings plc, together with its subsidiaries, operates as a measurement and data analytics company worldwide. The company provides viewership and listening data, and analytics principally to media publishers and marketers, and advertising agencies for television, computer, mobile, CTV, digital, and listening platforms. It also offers television audience measurement services; digital audience measurement services; video advertising services; and independent measurement and consumer research primarily servicing radio, advertisers, and advertising agencies in the audio industry. In addition, it offers consumer behavioral and transactional data. Nielsen Holdings plc provides marketing solutions. The company was founded in 1923 and is headquartered in New York, New York.",
        fullTimeEmployees=14000,
        city="New York",
        state="NY",
        trailingPE=10.838295,
        dividendYield=0.0095,
        averageVolume=6451093,
        regularMarketOpen=24,
        volume=1313674,
        fiftyTwoWeekHigh=27.79,
        fiftyTwoWeekLow=16.02,
        recommendationKey="hold",
        industry="Consulting Services"
    )
    db.session.add(NLSN)

    NKE = Stock(
        name="NIKE, Inc.",
        ticker="NKE",
        marketCap=162682241024,
        dayHigh=114.05,
        dayLow=102.75,
        currentPrice=102.78,
        longBusinessSummary="NIKE, Inc., together with its subsidiaries, designs, develops, markets, and sells athletic footwear, apparel, equipment, and accessories worldwide. The company offers NIKE brand products in six categories, including running, NIKE basketball, the Jordan brand, football, training, and sportswear. It also markets products designed for kids, as well as for other athletic and recreational uses, such as American football, baseball, cricket, golf, lacrosse, skateboarding, tennis, volleyball, walking, wrestling, and other outdoor activities; and apparel with licensed college and professional team, and league logos, as well as sells sports apparel. In addition, the company sells a line of performance equipment and accessories comprising bags, socks, sport balls, eyewear, timepieces, digital devices, bats, gloves, protective equipment, and other equipment for sports activities; and various plastic products to other manufacturers. Further, it provides athletic and casual footwear, apparel, and accessories under the Jumpman trademark; and casual sneakers, apparel, and accessories under the Converse, Chuck Taylor, All Star, One Star, Star Chevron, and Jack Purcell trademarks. Additionally, the company licenses agreements that permit unaffiliated parties to manufacture and sell apparel, digital devices, and applications and other equipment for sports activities under NIKE-owned trademarks. It sells its products to footwear stores; sporting goods stores; athletic specialty stores; department stores; skate, tennis, and golf shops; and other retail accounts through NIKE-owned retail stores, digital platforms, independent distributors, licensees, and sales representatives. The company was formerly known as Blue Ribbon Sports, Inc. and changed its name to NIKE, Inc. in 1971. NIKE, Inc. was founded in 1964 and is headquartered in Beaverton, Oregon.",
        fullTimeEmployees=73300,
        city="Beaverton",
        state="OR",
        trailingPE=26.976377,
        dividendYield=0.0108,
        averageVolume=7367903,
        regularMarketOpen=108.2,
        volume=31261204,
        fiftyTwoWeekHigh=179.1,
        fiftyTwoWeekLow=102.48,
        recommendationKey="buy",
        industry="Footwear & Accessories"
    )
    db.session.add(NKE)

    NI = Stock(
        name="NiSource Inc.",
        ticker="NI",
        marketCap=11525892096,
        dayHigh=29.77,
        dayLow=29.24,
        currentPrice=29.35,
        longBusinessSummary="NiSource Inc., an energy holding company, operates as a regulated natural gas and electric utility company in the United States. It operates through two segments, Gas Distribution Operations and Electric Operations. The company distributes natural gas to approximately 853,000 customers in northern Indiana, as well as approximately 2.4 million residential, commercial, and industrial customers in Ohio, Pennsylvania, Virginia, Kentucky, and Maryland. It operates approximately 54,600 miles of distribution main pipelines, as well as associated individual customer service lines; and 1,000 miles of transmission main pipelines. The company generates, transmits, and distributes electricity to approximately 483,000 customers in 20 counties in the northern part of Indiana, as well as engages in wholesale electric and transmission transactions. It owns and operates coal-fired electric generating stations with a capacity of 722 megawatts (MW) in Wheatfield and 455 MW in Michigan City; combined cycle gas turbine with a capacity of 563 MW in West Terre Haute; natural gas generating units with a capacity of 155 MW in Wheatfield; hydro generating plants with a capacity of 9 MW in Carroll County and 7 MW in White County; and wind generating units with a capacity of 102 MW and 302 MW in White County, Indiana. The company was formerly known as NIPSCO Industries, Inc. and changed its name to NiSource Inc. in April 1999. NiSource Inc. was founded in 1847 and is headquartered in Merrillville, Indiana.",
        fullTimeEmployees=7272,
        city="Merrillville",
        state="IN",
        trailingPE=26.803652,
        dividendYield=0.031,
        averageVolume=4571646,
        regularMarketOpen=29.35,
        volume=3247823,
        fiftyTwoWeekHigh=32.59,
        fiftyTwoWeekLow=23.65,
        recommendationKey="buy",
        industry="Utilities—Regulated Gas"
    )
    db.session.add(NI)

    NDSN = Stock(
        name="Nordson Corporation",
        ticker="NDSN",
        marketCap=11801123840,
        dayHigh=209.19,
        dayLow=201.995,
        currentPrice=202.85,
        longBusinessSummary="Nordson Corporation engineers, manufactures, and markets products and systems to dispense, apply, and control adhesives, coatings, polymers, sealants, biomaterials, and other fluids worldwide. It operates through two segments, Industrial Precision Solutions (IPS) and Advanced Technology Solutions (ATS). The IPS segment provides dispensing, coating, and laminating systems for adhesives, lotions, liquids, and fibers to disposable products and roll goods; automated adhesive dispensing systems used in packaged goods industries; components and systems used in the thermoplastic melt stream; and product assembly systems for use in paper and paperboard converting applications, and manufacturing roll goods, as well as for the assembly of plastic, metal, and wood products. It also offers automated and manual dispensing products and systems to apply adhesive and sealant materials; dispensing and curing systems to coat and cure containers; systems to apply liquid paints and coatings to consumer and industrial products; and systems to apply powder paints and coatings to metal, plastic, and wood products, as well as ultraviolet equipment for use in curing and drying operations for specialty coatings, semiconductor materials, and paints. The ATS segment provides automated dispensing systems for the attachment, protection, and coating of fluids, as well as related gas plasma treatment systems for cleaning and conditioning surfaces; precision manual and semi-automated dispensers, minimally invasive interventional delivery devices, plastic molded syringes, cartridges, tips, fluid connection components, tubing, balloons, and catheters; and bond testing and automated optical, acoustic microscopy, and x-ray inspection systems for use in semiconductor and printed circuit board industries. The company markets its products through direct sales force, as well as distributors and sales representatives. Nordson Corporation was founded in 1935 and is headquartered in Westlake, Ohio.",
        fullTimeEmployees=7100,
        city="Westlake",
        state="OH",
        trailingPE=26.208012,
        dividendYield=0.0095999995,
        averageVolume=223532,
        regularMarketOpen=205.55,
        volume=258007,
        fiftyTwoWeekHigh=272.28,
        fiftyTwoWeekLow=194.89,
        recommendationKey="buy",
        industry="Specialty Industrial Machinery"
    )
    db.session.add(NDSN)

    NSC = Stock(
        name="Norfolk Southern Corporation",
        ticker="NSC",
        marketCap=55090872320,
        dayHigh=233.88,
        dayLow=226.0001,
        currentPrice=226.39,
        longBusinessSummary="Norfolk Southern Corporation, together with its subsidiaries, engages in the rail transportation of raw materials, intermediate products, and finished goods in the United States. The company transports agriculture, forest, and consumer products comprising soybeans, wheat, corn, fertilizers, livestock and poultry feed, food products, food oils, flour, sweeteners, ethanol, lumber and wood products, pulp board and paper products, wood fibers, wood pulp, scrap paper, beverages, canned goods, and consumer products; chemicals consist of sulfur and related chemicals, petroleum products, chlorine and bleaching compounds, plastics, rubber, industrial chemicals, chemical wastes, and sand; metals and construction materials, such as steel, aluminum products, machinery, scrap metals, cement, aggregates, minerals, clay, transportation equipment, and military-related products; and automotive, including finished motor vehicles and automotive parts, as well as coal. It also transports overseas freight through various Atlantic and Gulf Coast ports; and provides commuter rail passenger transportation services and operates an intermodal network. As of December 31, 2021, the company operated approximately 19,300 route miles in 22 states and the District of Columbia. Norfolk Southern Corporation was incorporated in 1980 and is based in Atlanta, Georgia.",
        fullTimeEmployees=18100,
        city="Atlanta",
        state="GA",
        trailingPE=19.484465,
        dividendYield=0.0199,
        averageVolume=1363882,
        regularMarketOpen=231.15,
        volume=923540,
        fiftyTwoWeekHigh=299.2,
        fiftyTwoWeekLow=219.31,
        recommendationKey="buy",
        industry="Railroads"
    )
    db.session.add(NSC)

    NTRS = Stock(
        name="Northern Trust Corporation",
        ticker="NTRS",
        marketCap=20404768768,
        dayHigh=100.6,
        dayLow=98.02,
        currentPrice=98.26,
        longBusinessSummary="Northern Trust Corporation, a financial holding company, provides wealth management, asset servicing, asset management, and banking solutions for corporations, institutions, families, and individuals worldwide. It operates in two segments, Corporate & Institutional Services (C&IS) and Wealth Management. The C&IS segment offers asset servicing and related services, including custody, fund administration, investment operations outsourcing, investment management, investment risk and analytical services, employee benefit services, securities lending, foreign exchange, treasury management, brokerage services, transition management services, banking, and cash management services. This segment serves corporate and public retirement funds, foundations, endowments, fund managers, insurance companies, sovereign wealth funds, and other institutional investors. The Wealth Management segment offers trust, investment management, custody, and philanthropic; financial consulting; guardianship and estate administration; family business consulting; family financial education; brokerage services; and private and business banking services. This segment serves high-net-worth individuals and families, business owners, executives, professionals, retirees, and established privately held businesses. The company also provides asset management services, such as active and passive equity; active and passive fixed income; cash management; alternative asset classes comprising private equity and hedge funds of funds; and multi-manager advisory services and products through separately managed accounts, bank common and collective funds, registered investment companies, exchange traded funds, non-U.S. collective investment funds, and unregistered private investment funds. In addition, it offers overlay and other risk management services. The company was founded in 1889 and is headquartered in Chicago, Illinois.",
        fullTimeEmployees=21700,
        city="Chicago",
        state="IL",
        trailingPE=15.498423,
        dividendYield=0.0269,
        averageVolume=875158,
        regularMarketOpen=98.72,
        volume=526442,
        fiftyTwoWeekHigh=135.15,
        fiftyTwoWeekLow=89.68,
        recommendationKey="hold",
        industry="Asset Management"
    )
    db.session.add(NTRS)

    NOC = Stock(
        name="Northrop Grumman Corporation",
        ticker="NOC",
        marketCap=73110249472,
        dayHigh=473.82,
        dayLow=464.17,
        currentPrice=464.67,
        longBusinessSummary="Northrop Grumman Corporation operates as an aerospace and defense company worldwide. The company's Aeronautics Systems segment designs, develops, manufactures, integrates, and sustains aircraft systems. This segment also offers unmanned autonomous aircraft systems, including high-altitude long-endurance strategic ISR systems and vertical take-off and landing tactical ISR systems; and strategic long-range strike aircraft, tactical fighter and air dominance aircraft, and airborne battle management and command and control systems. Its Defense Systems segment designs, develops, and produces weapons and mission systems. It offers products and services, such as integrated battle management systems, weapons systems and aircraft, and mission systems. This segment also provides command and control and weapons systems, including munitions and missiles; precision strike weapons; propulsion, such as air-breathing and hypersonic systems; gun systems and precision munitions; life cycle service and support for software, weapons systems, and aircraft; and logistics support, sustainment, operation, and modernization for air, sea, and ground systems. The company's Mission Systems segment offers cyber, command, control, communications and computers, intelligence, surveillance, and reconnaissance systems; radar, electro-optical/infrared and acoustic sensors; electronic warfare systems; advanced communications and network systems; cyber solutions; intelligence processing systems; navigation; and maritime power, propulsion, and payload launch systems. This segment also provides airborne multifunction sensors; maritime/land systems and sensors; navigation, targeting, and survivability solutions; and networked information solutions. Its Space Systems segment offers satellites and payloads; ground systems; missile defense systems and interceptors; launch vehicles and related propulsion systems; and strategic missiles. The company was founded in 1939 and is based in Falls Church, Virginia.",
        fullTimeEmployees=90000,
        city="Falls Church",
        state="VA",
        trailingPE=16.390476,
        dividendYield=0.0139,
        averageVolume=810312,
        regularMarketOpen=468.13,
        volume=564890,
        fiftyTwoWeekHigh=492.3,
        fiftyTwoWeekLow=344.89,
        recommendationKey="buy",
        industry="Aerospace & Defense"
    )
    db.session.add(NOC)

    NLOK = Stock(
        name="NortonLifeLock Inc.",
        ticker="NLOK",
        marketCap=12955683840,
        dayHigh=22.79,
        dayLow=22.1,
        currentPrice=22.27,
        longBusinessSummary="NortonLifeLock Inc. provides cyber safety solutions for consumers worldwide. The company offers Norton 360, an integrated platform provides extensive cyber safety coverage and a subscription service providing protection for PCs, Macs, and mobile devices against malware, viruses, adware, ransomware, and other online threats on various platforms; and LifeLock identity theft protection solution that offers monitoring, alerts, and restoration services to its customers. It also provides Norton Secure VPN solution enhances security and online privacy by providing an encrypted data tunnel; Privacy Monitor Assistant, an on-demand, white glove service where agents help members delete personal information from data brokers online; Home Title Protect product detects fraud and notifies members; and Avira Security, a consumer-focused portfolio of cybersecurity and privacy solutions. The company markets and sells its products and related services through retailers, telecom service providers, hardware original equipment manufacturers, and employee benefit providers, as well as e-commerce platform. It operates in the United States, Canada, Latin America, Europe, the Middle East, Africa, the Asia Pacific, and Japan. The company was formerly known as Symantec Corporation and changed its name to NortonLifeLock Inc. in November 2019. NortonLifeLock Inc. was founded in 1982 and is headquartered in Tempe, Arizona.",
        fullTimeEmployees=2800,
        city="Tempe",
        state="AZ",
        trailingPE=14.886363,
        dividendYield=0.0209,
        averageVolume=5982722,
        regularMarketOpen=22.79,
        volume=3227187,
        fiftyTwoWeekHigh=30.92,
        fiftyTwoWeekLow=21.55,
        recommendationKey="buy",
        industry="Software—Infrastructure"
    )
    db.session.add(NLOK)

    NRG = Stock(
        name="NRG Energy, Inc.",
        ticker="NRG",
        marketCap=9259810816,
        dayHigh=38.91,
        dayLow=37.61,
        currentPrice=37.82,
        longBusinessSummary="NRG Energy, Inc., together with its subsidiaries, operates as an integrated power company in the United States. It operates through Texas, East, and West. The company is involved in the producing, selling, and delivering electricity and related products and services to approximately 6 million residential, commercial, industrial, and wholesale customers. It generates electricity using natural gas, coal, oil, solar, nuclear, and battery storage. The company also provides system power, distributed generation, renewable products, backup generation, storage and distributed solar, demand response, and energy efficiency, and advisory services, as well as carbon management and specialty services; and on-site energy solutions. In addition, it trades in electric power, natural gas, and related commodities; environmental products; weather products; and financial products, including forwards, futures, options, and swaps. Further, the company procures fuels; provides transportation services; and directly sells energy, services, and products and services to retail customers under the NRG, Reliant, Direct Energy, Green Mountain Energy, Stream, and XOOM Energy. As of December 31, 2021, it owns and leases power generation portfolio with approximately 18,000 megawatts of capacity at 25 plants. NRG Energy, Inc. was founded in 1989 and is headquartered in Houston, Texas.",
        fullTimeEmployees=6635,
        city="Houston",
        state="TX",
        trailingPE=3.7910986,
        dividendYield=0.033099998,
        averageVolume=3647075,
        regularMarketOpen=38.69,
        volume=2043078,
        fiftyTwoWeekHigh=47.82,
        fiftyTwoWeekLow=34.7,
        recommendationKey="buy",
        industry="Utilities—Independent Power Producers"
    )
    db.session.add(NRG)

    NUE = Stock(
        name="Nucor Corporation",
        ticker="NUE",
        marketCap=30857719808,
        dayHigh=113.04,
        dayLow=107.56,
        currentPrice=107.97,
        longBusinessSummary="Nucor Corporation manufactures and sells steel and steel products. The company's Steel Mills segment produces hot-rolled, cold-rolled, and galvanized sheet steel products; plate steel products; wide-flange beams, beam blanks, and H-piling and sheet piling products; and bar steel products, such as blooms, billets, concrete reinforcing and merchant bars, and special bar quality products. It also engages in the steel trading and rebar distribution businesses. This segment sells its products to steel service centers, fabricators, and manufacturers in the United States, Canada, and Mexico. Its Steel Products segment offers hollow structural section steel tubing products, electrical conduits, steel racking, steel joists and joist girders, steel decks, fabricated concrete reinforcing steel products, cold finished steel products, steel fasteners, metal building systems, insulated metal panels, steel grating and expanded metal products, and wire and wire mesh products primarily for use in nonresidential construction applications. This segment also engages in the piling distribution business. The company's Raw Materials segment produces direct reduced iron (DRI); brokers ferrous and nonferrous metals, pig iron, hot briquetted iron, and DRI; supplies ferro-alloys; and processes ferrous and nonferrous scrap metal, as well as engages in the natural gas drilling operations. This segment sells its ferrous scrap to electric arc furnace steel mills and foundries for manufacturing process; and nonferrous scrap metal to aluminum can producers, secondary aluminum smelters, steel mills and other processors, and consumers of various nonferrous metals. It serves agriculture, automotive, construction, energy and transmission, oil and gas, heavy equipment, infrastructure, and transportation industries through its in-house sales force; and internal distribution and trading companies. Nucor Corporation was incorporated in 1958 and is based in Charlotte, North Carolina.",
        fullTimeEmployees=28800,
        city="Charlotte",
        state="NC",
        trailingPE=6.5132413,
        dividendYield=0.0162,
        averageVolume=3005133,
        regularMarketOpen=110.74,
        volume=1920514,
        fiftyTwoWeekHigh=187.9,
        fiftyTwoWeekLow=87.71,
        recommendationKey="hold",
        industry="Steel"
    )
    db.session.add(NUE)

    NVDA = Stock(
        name="NVIDIA Corporation",
        ticker="NVDA",
        marketCap=398271447040,
        dayHigh=172.015,
        dayLow=159.4501,
        currentPrice=159.82,
        longBusinessSummary="NVIDIA Corporation provides graphics, and compute and networking solutions in the United States, Taiwan, China, and internationally. The company's Graphics segment offers GeForce GPUs for gaming and PCs, the GeForce NOW game streaming service and related infrastructure, and solutions for gaming platforms; Quadro/NVIDIA RTX GPUs for enterprise workstation graphics; vGPU software for cloud-based visual and virtual computing; automotive platforms for infotainment systems; and Omniverse software for building 3D designs and virtual worlds. Its Compute & Networking segment provides Data Center platforms and systems for AI, HPC, and accelerated computing; Mellanox networking and interconnect solutions; automotive AI Cockpit, autonomous driving development agreements, and autonomous vehicle solutions; cryptocurrency mining processors; Jetson for robotics and other embedded platforms; and NVIDIA AI Enterprise and other software. The company's products are used in gaming, professional visualization, datacenter, and automotive markets. NVIDIA Corporation sells its products to original equipment manufacturers, original device manufacturers, system builders, add-in board manufacturers, retailers/distributors, independent software vendors, Internet and cloud service providers, automotive manufacturers and tier-1 automotive suppliers, mapping companies, start-ups, and other ecosystem participants. It has a strategic collaboration with Kroger Co. NVIDIA Corporation was incorporated in 1993 and is headquartered in Santa Clara, California.",
        fullTimeEmployees=22473,
        city="Santa Clara",
        state="CA",
        trailingPE=49.281532,
        dividendYield=0.00090000004,
        averageVolume=56965550,
        regularMarketOpen=169,
        volume=46185936,
        fiftyTwoWeekHigh=346.47,
        fiftyTwoWeekLow=153.28,
        recommendationKey="buy",
        industry="Semiconductors"
    )
    db.session.add(NVDA)

    NVR = Stock(
        name="NVR, Inc.",
        ticker="NVR",
        marketCap=13761460224,
        dayHigh=4070.455,
        dayLow=3948.8,
        currentPrice=3951.32,
        longBusinessSummary="NVR, Inc. operates as a homebuilder in the United States. The company operates in two segments, Homebuilding and Mortgage Banking. It engages in the construction and sale of single-family detached homes, townhomes, and condominium buildings under the Ryan Homes, NVHomes, and Heartland Homes names. The company markets its Ryan Homes products to first-time and first-time move-up buyers; and NVHomes and Heartland Homes products to move-up and luxury buyers. It also provides various mortgage related services to its homebuilding customers, as well as brokers title insurance; performs title searches in connection with mortgage loan closings; and sells mortgage loans to investors in the secondary markets on a servicing released basis. The company primarily serves in Maryland, Virginia, West Virginia, Delaware, New Jersey, Eastern Pennsylvania, New York, Ohio, Western Pennsylvania, Indiana, Illinois, North Carolina, South Carolina, Florida, Tennessee, and Washington, D.C. NVR, Inc. was founded in 1980 and is headquartered in Reston, Virginia.",
        fullTimeEmployees=6600,
        city="Reston",
        state="VA",
        trailingPE=12.81199,
        dividendYield=None,
        averageVolume=23187,
        regularMarketOpen=4062.5,
        volume=15491,
        fiftyTwoWeekHigh=5982.45,
        fiftyTwoWeekLow=3576.01,
        recommendationKey="hold",
        industry="Residential Construction"
    )
    db.session.add(NVR)

    ORLY = Stock(
        name="O'Reilly Automotive, Inc.",
        ticker="ORLY",
        marketCap=42483429376,
        dayHigh=650.53,
        dayLow=630.05,
        currentPrice=630.52,
        longBusinessSummary="O'Reilly Automotive, Inc., together with its subsidiaries, operates as a retailer and supplier of automotive aftermarket parts, tools, supplies, equipment, and accessories in the United States. The company provides new and remanufactured automotive hard parts and maintenance items, such as alternators, batteries, brake system components, belts, chassis parts, driveline parts, engine parts, fuel pumps, hoses, starters, temperature control, water pumps, antifreeze, appearance products, engine additives, filters, fluids, lighting products, and oil and wiper blades; and accessories, including floor mats, seat covers, and truck accessories. Its stores offer auto body paint and related materials, automotive tools, and professional service provider service equipment. The company's stores also provide enhanced services and programs comprising used oil, oil filter, and battery recycling; battery, wiper, and bulb replacement; battery diagnostic testing; electrical and module testing; check engine light code extraction; loaner tool program; drum and rotor resurfacing; custom hydraulic hoses; and professional paint shop mixing and related materials. Its stores offer do-it-yourself and professional service provider customers a selection of products for domestic and imported automobiles, vans, and trucks. As of December 31, 2021, the company owned and operated 5,759 stores in the United States, and 25 stores in Mexico. O'Reilly Automotive, Inc. was founded in 1957 and is headquartered in Springfield, Missouri.",
        fullTimeEmployees=82516,
        city="Springfield",
        state="MO",
        trailingPE=21.909033,
        dividendYield=None,
        averageVolume=644746,
        regularMarketOpen=642.2,
        volume=457635,
        fiftyTwoWeekHigh=748.68,
        fiftyTwoWeekLow=562.9,
        recommendationKey="buy",
        industry="Specialty Retail"
    )
    db.session.add(ORLY)

    ODFL = Stock(
        name="Old Dominion Freight Line, Inc.",
        ticker="ODFL",
        marketCap=28835557376,
        dayHigh=264.69,
        dayLow=250.02,
        currentPrice=250.72,
        longBusinessSummary="Old Dominion Freight Line, Inc. operates as a less-than-truckload (LTL) motor carrier in the United States and North America. It provides regional, inter-regional, and national LTL services, including expedited transportation. The company also offers various value-added services, such as container drayage, truckload brokerage, and supply chain consulting. As of December 31, 2021, it owned and operated 10,403 tractors, 27,917 linehaul trailers, and 13,303 pickup and delivery trailers; 3 fleet maintenance centers; and 251 service centers. Old Dominion Freight Line, Inc. was founded in 1934 and is headquartered in Thomasville, North Carolina.",
        fullTimeEmployees=24277,
        city="Thomasville",
        state="NC",
        trailingPE=31.002844,
        dividendYield=0.0044,
        averageVolume=1086975,
        regularMarketOpen=259.36,
        volume=695926,
        fiftyTwoWeekHigh=373.58,
        fiftyTwoWeekLow=231.31,
        recommendationKey="hold",
        industry="Trucking"
    )
    db.session.add(ODFL)

    OMC = Stock(
        name="Omnicom Group Inc.",
        ticker="OMC",
        marketCap=13531506688,
        dayHigh=65.82,
        dayLow=63.55,
        currentPrice=63.66,
        longBusinessSummary="Omnicom Group Inc., together with its subsidiaries, provides advertising, marketing, and corporate communications services. It provides a range of services in the areas of advertising, customer relationship management, public relations, and healthcare. The company's services include advertising, branding, content marketing, corporate social responsibility consulting, crisis communications, custom publishing, data analytics, database management, digital/direct marketing, digital transformation, entertainment marketing, experiential marketing, field marketing, financial/corporate business-to-business advertising, graphic arts/digital imaging, healthcare marketing and communications, and in-store design services. Its services also comprise interactive marketing, investor relations, marketing research, media planning and buying, merchandising and point of sale, mobile marketing, multi-cultural marketing, non-profit marketing, organizational communications, package design, product placement, promotional marketing, public affairs, retail marketing, sales support, search engine marketing, shopper marketing, social media marketing, and sports and event marketing services. It operates in the United States, Canada, Puerto Rico, South America, Mexico, Europe, the Middle East, Africa, Australia, Greater China, India, Japan, Korea, New Zealand, Singapore, and other Asian countries. The company was incorporated in 1944 and is based in New York, New York.",
        fullTimeEmployees=71700,
        city="New York",
        state="NY",
        trailingPE=9.915888,
        dividendYield=0.0364,
        averageVolume=1726311,
        regularMarketOpen=65.42,
        volume=1273194,
        fiftyTwoWeekHigh=91.61,
        fiftyTwoWeekLow=61.67,
        recommendationKey="buy",
        industry="Advertising Agencies"
    )
    db.session.add(OMC)

    ON = Stock(
        name="ON Semiconductor Corporation",
        ticker="ON",
        marketCap=22752344064,
        dayHigh=55.58,
        dayLow=52.48,
        currentPrice=52.81,
        longBusinessSummary="ON Semiconductor Corporation provides intelligent sensing and power solutions worldwide. Its intelligent power technologies enable the electrification of the automotive industry that allows for lighter and longer-range electric vehicles, empowers fast-charging systems, and propels sustainable energy for the solar strings, industrial power, and storage systems. The company operates through three segments the Power Solutions Group, the Advanced Solutions Group, and the Intelligent Sensing Group segments. It offers analog, discrete, module, and integrated semiconductor products that perform multiple application functions, including power switching and conversion, signal conditioning, circuit protection, signal amplification, and voltage regulation functions. The company also designs and develops analog, mixed-signal, advanced logic, application specific standard product and ASICs, radio frequency, and integrated power solutions for end-users in end-markets, as well as provides foundry and design services for government customers. In addition, it develops complementary metal oxide semiconductor image sensors, image signal processors, and single photon detectors, including silicon photomultipliers and single photon avalanche diode arrays, as well as actuator drivers for autofocus and image stabilization for a broad base of end-users in various end-markets. ON Semiconductor Corporation was incorporated in 1992 and is headquartered in Phoenix, Arizona.",
        fullTimeEmployees=30000,
        city="Phoenix",
        state="AZ",
        trailingPE=34.471283,
        dividendYield=None,
        averageVolume=8629245,
        regularMarketOpen=54.25,
        volume=6716560,
        fiftyTwoWeekHigh=71.26,
        fiftyTwoWeekLow=34.01,
        recommendationKey="buy",
        industry="Semiconductors"
    )
    db.session.add(ON)

    OKE = Stock(
        name="ONEOK, Inc.",
        ticker="OKE",
        marketCap=25409488896,
        dayHigh=58.87,
        dayLow=56.7,
        currentPrice=56.98,
        longBusinessSummary="ONEOK, Inc., together with its subsidiaries, engages in gathering, processing, storage, and transportation of natural gas in the United States. It operates through Natural Gas Gathering and Processing, Natural Gas Liquids, and Natural Gas Pipelines segments. The company owns natural gas gathering pipelines and processing plants in the Mid-Continent and Rocky Mountain regions. It also gathers, treats, fractionates, and transports natural gas liquids (NGL), as well as stores, markets, and distributes NGL products. The company owns NGL gathering and distribution pipelines in Oklahoma, Kansas, Texas, New Mexico, Montana, North Dakota, Wyoming, and Colorado; terminal and storage facilities in Kansas, Missouri, Nebraska, Iowa, and Illinois; and NGL distribution and refined petroleum products pipelines in Kansas, Missouri, Nebraska, Iowa, Illinois, and Indiana, as well as owns and operates truck- and rail-loading, and -unloading facilities connected to NGL fractionation, storage, and pipeline assets. In addition, it operates regulated interstate and intrastate natural gas transmission pipelines and natural gas storage facilities. Further, the company owns and operates a parking garage in downtown Tulsa, Oklahoma; and leases excess office space. It operates 17,500 miles of natural gas gathering pipelines; 1,500 miles of FERC-regulated interstate natural gas pipelines; 5,100 miles of state-regulated intrastate transmission pipeline; six NGL storage facilities; and eight NGL product terminals. It serves integrated and independent exploration and production companies; NGL and natural gas gathering and processing companies; crude oil and natural gas production companies; propane distributors; municipalities; ethanol producers; and petrochemical, refining, and NGL marketing companies, as well as natural gas distribution and electric generation companies, producers, processors, and marketing companies. The company was founded in 1906 and is headquartered in Tulsa, Oklahoma.",
        fullTimeEmployees=2847,
        city="Tulsa",
        state="OK",
        trailingPE=17.834116,
        dividendYield=0.057800002,
        averageVolume=2798433,
        regularMarketOpen=57.87,
        volume=3288169,
        fiftyTwoWeekHigh=75.07,
        fiftyTwoWeekLow=48.51,
        recommendationKey="hold",
        industry="Oil & Gas Midstream"
    )
    db.session.add(OKE)

    ORCL = Stock(
        name="Oracle Corporation",
        ticker="ORCL",
        marketCap=183139467264,
        dayHigh=71.07,
        dayLow=68.53,
        currentPrice=68.58,
        longBusinessSummary="Oracle Corporation provides products and services that address enterprise information technology environments worldwide. Its Oracle cloud software as a service offering include various cloud software applications, including Oracle Fusion cloud enterprise resource planning (ERP), Oracle Fusion cloud enterprise performance management, Oracle Fusion cloud supply chain and manufacturing management, Oracle Fusion cloud human capital management, Oracle Fusion cloud advertising and customer experience, and NetSuite applications suite. The company also offers cloud-based industry solutions for various industries; Oracle application licenses; and Oracle license support services. In addition, it provides cloud and license business' infrastructure technologies, such as the Oracle Database, an enterprise database; Java, a software development language; and middleware, including development tools and others. The company's cloud and license business' infrastructure technologies also comprise cloud-based compute, storage, and networking capabilities through its Oracle cloud infrastructure as a service offerings. Further, it offers infrastructure offerings comprising Oracle autonomous data warehouse cloud service, Oracle autonomous transaction processing cloud service, Internet-of-Things, digital assistant, and blockchain. Additionally, the company provides hardware products and other hardware-related software offerings, including Oracle engineered systems, enterprise servers, storage solutions, industry-specific hardware, virtualization software, operating systems, management software, and related hardware services; and consulting services. The company markets and sells its cloud, license, hardware, support, and services offerings directly to businesses in various industries, government agencies, and educational institutions, as well as through indirect channels. Oracle Corporation was founded in 1977 and is headquartered in Austin, Texas.",
        fullTimeEmployees=132000,
        city="Austin",
        state="TX",
        trailingPE=19.356478,
        dividendYield=0.018,
        averageVolume=8234012,
        regularMarketOpen=70.57,
        volume=6801343,
        fiftyTwoWeekHigh=106.34,
        fiftyTwoWeekLow=63.76,
        recommendationKey="hold",
        industry="Software—Infrastructure"
    )
    db.session.add(ORCL)

    OGN = Stock(
        name="Organon & Co.",
        ticker="OGN",
        marketCap=8821004288,
        dayHigh=35.595,
        dayLow=34.66,
        currentPrice=34.79,
        longBusinessSummary="Organon & Co., a health care company, develops and delivers health solutions through a portfolio of prescription therapies in the United States and internationally. Its women's health portfolio comprises contraception and fertility brands, such as Nexplanon/Implanon, a long-acting reversible contraceptive. The company's biosimilars portfolio consists of three immunology products, such as Brenzys, Renflexis, and Hadlima, as well as two oncology products, including Ontruzant and Aybintio. It also offers cardiovascular products, consisting of several cholesterol-modifying medicines under the Zetia, Ezetrol, Vytorin, Inegy, Rosuzet, and Zocor brands; Cozaar and Hyzaar for the treatment of hypertension; respiratory products for various treatments to control and prevent symptoms caused by asthma under the Singulair, Dulera, Zenhale, and Asmanex brand names; and Singulair, Nasonex, Clarinex, and Aerius for treating seasonal allergic rhinitis. In addition, the company provides dermatology products under the Diprosone and Elocon brand; bone health portfolio, including Fosamax brand name; non-opioid pain management products under the Arcoxia, Diprospan, and Celestone brand names; Proscar for the treatment of symptomatic benign prostatic hyperplasia; and Propecia for the treatment of male pattern hair loss. The company sells its products primarily to drug wholesalers and retailers, hospitals, and government agencies, as well as managed health care providers, such as health maintenance organizations, pharmacy benefit managers, and other institutions. Organon & Co. was incorporated in 2020 and is based in Jersey City, New Jersey.",
        fullTimeEmployees=9300,
        city="Jersey City",
        state="NJ",
        trailingPE=5.822594,
        dividendYield=0.0323,
        averageVolume=1576474,
        regularMarketOpen=35.48,
        volume=796981,
        fiftyTwoWeekHigh=39.475,
        fiftyTwoWeekLow=28.42,
        recommendationKey="buy",
        industry="Drug Manufacturers—General"
    )
    db.session.add(OGN)

    OTIS = Stock(
        name="Otis Worldwide Corporation",
        ticker="OTIS",
        marketCap=29644627968,
        dayHigh=70.85,
        dayLow=69.49,
        currentPrice=69.79,
        longBusinessSummary="Otis Worldwide Corporation manufactures, installs, and services elevators and escalators in the United States, China, and internationally. The company operates in two segments, New Equipment and Service. The New Equipment segment designs, manufactures, sells, and installs a range of passenger and freight elevators, as well as escalators and moving walkways for residential and commercial buildings, and infrastructure projects. The Service segment performs maintenance and repair services, as well as modernization services to upgrade elevators and escalators. It had a network of approximately 34,000 service mechanics operating approximately 1,400 branches and offices. The company was founded in 1853 and is headquartered in Farmington, Connecticut.",
        fullTimeEmployees=70000,
        city="Farmington",
        state="CT",
        trailingPE=24.933905,
        dividendYield=0.0159,
        averageVolume=2452516,
        regularMarketOpen=70.2,
        volume=1877814,
        fiftyTwoWeekHigh=92.84,
        fiftyTwoWeekLow=66.97,
        recommendationKey="buy",
        industry="Specialty Industrial Machinery"
    )
    db.session.add(OTIS)

    PCAR = Stock(
        name="PACCAR Inc",
        ticker="PCAR",
        marketCap=28888596480,
        dayHigh=85.5,
        dayLow=83.13,
        currentPrice=83.21,
        longBusinessSummary="PACCAR Inc designs, manufactures, and distributes light, medium, and heavy-duty commercial trucks in the United States, Europe, Mexico, South America, Australia, and internationally. It operates through three segments: Truck, Parts, and Financial Services. The Truck segment designs, manufactures, and distributes trucks for the over-the-road and off-highway hauling of commercial and consumer goods. It sells its trucks through a network of independent dealers under the Kenworth, Peterbilt, and DAF nameplates. The Parts segment distributes aftermarket parts for trucks and related commercial vehicles. The Financial Services segment conducts full-service leasing operations under the PacLease trade name, as well as provides finance and leasing products and services to customers and dealers. This segment also offers equipment financing and administrative support services for its franchisees; retail loan and leasing services for small, medium, and large commercial trucking companies, as well as independent owners/operators and other businesses; and truck inventory financing services to independent dealers. In addition, this segment offers loans and leases directly to customers for the acquisition of trucks and related equipment. The company also manufactures and markets industrial winches under the Braden, Carco, and Gearmatic nameplates. PACCAR Inc was founded in 1905 and is headquartered in Bellevue, Washington.",
        fullTimeEmployees=28500,
        city="Bellevue",
        state="WA",
        trailingPE=16.575697,
        dividendYield=0.0162,
        averageVolume=1933011,
        regularMarketOpen=84.05,
        volume=1259295,
        fiftyTwoWeekHigh=97.56,
        fiftyTwoWeekLow=77.96,
        recommendationKey="buy",
        industry="Farm & Heavy Construction Machinery"
    )
    db.session.add(PCAR)

    PKG = Stock(
        name="Packaging Corporation of America",
        ticker="PKG",
        marketCap=13198970880,
        dayHigh=143.06,
        dayLow=138.87,
        currentPrice=138.95,
        longBusinessSummary="Packaging Corporation of America manufactures and sells containerboard and corrugated packaging products in the United States. The company operates through Packaging and Paper segments. The Packaging segment offers various containerboard and corrugated packaging products, such as conventional shipping containers used to protect and transport manufactured goods; multi-color boxes and displays that help to merchandise the packaged product in retail locations; and honeycomb protective packaging products, as well as packaging for meat, fresh fruit and vegetables, processed food, beverages, and other industrial and consumer products. This segment sells its corrugated products through a direct sales and marketing organization, independent brokers, and distribution partners. The Paper segment manufactures and sells commodity and specialty papers, as well as communication papers, including cut-size office papers, and printing and converting papers. This segment sells white papers through its sales and marketing organization. Packaging Corporation of America was founded in 1867 and is headquartered in Lake Forest, Illinois.",
        fullTimeEmployees=15200,
        city="Lake Forest",
        state="IL",
        trailingPE=17.698381,
        dividendYield=0.0257,
        averageVolume=643101,
        regularMarketOpen=141.99,
        volume=511038,
        fiftyTwoWeekHigh=168.5,
        fiftyTwoWeekLow=124.78,
        recommendationKey="buy",
        industry="Packaging & Containers"
    )
    db.session.add(PKG)

    PH = Stock(
        name="Parker-Hannifin Corporation",
        ticker="PH",
        marketCap=32128749568,
        dayHigh=256.915,
        dayLow=249.7,
        currentPrice=250,
        longBusinessSummary="Parker-Hannifin Corporation manufactures and sells motion and control technologies and systems for various mobile, industrial, and aerospace markets worldwide. The company operates through two segments, Diversified Industrial and Aerospace Systems. The Company's Diversified Industrial segment offers sealing, shielding, thermal products and systems, adhesives, coatings, and noise vibration and harshness solutions; filters, systems, and diagnostics solutions to monitor and remove contaminants from fuel, air, oil, water, and other liquids and gases; connectors, which control, transmit, and contain fluid; control solutions for extreme corrosion resistance, temperatures, pressures, and precise flow; and hydraulic, pneumatic, and electromechanical components and systems for builders and users of mobile and industrial machinery and equipment. This segment sells its products to original equipment manufacturers (OEMs) and distributors who serve the replacement markets in manufacturing, packaging, processing, transportation, construction, refrigeration and air conditioning, agricultural, and military machinery and equipment industries. Its Aerospace Systems segment offers products for use in commercial and military airframe and engine programs, such as control actuation systems and components, engine build-up ducting, engine exhaust nozzles and assemblies, engine systems and components, fluid conveyance systems and components, fuel systems and components, fuel tank inerting systems, hydraulic systems and components, lubrication components, pilot controls, pneumatic control components, thermal management products, and wheels and brakes, as well as fluid metering, delivery, and atomization devices. This segment markets its products directly to OEMs and end users. It markets its products through direct-sales employees, independent distributors, and sales representatives. The company was founded in 1917 and is headquartered in Cleveland, Ohio.",
        fullTimeEmployees=54640,
        city="Cleveland",
        state="OH",
        trailingPE=17.427675,
        dividendYield=0.02,
        averageVolume=737538,
        regularMarketOpen=253.45,
        volume=808427,
        fiftyTwoWeekHigh=340,
        fiftyTwoWeekLow=230.44,
        recommendationKey="buy",
        industry="Specialty Industrial Machinery"
    )
    db.session.add(PH)

    PAYX = Stock(
        name="Paychex, Inc.",
        ticker="PAYX",
        marketCap=43247546368,
        dayHigh=123.986,
        dayLow=119.63,
        currentPrice=119.88,
        longBusinessSummary="Paychex, Inc. provides integrated human capital management solutions for human resources (HR), payroll, benefits, and insurance services for small to medium-sized businesses in the United States and Europe. The company offers payroll processing services; payroll tax administration services; employee payment services; and regulatory compliance services, such as new-hire reporting and garnishment processing. It also provides HR solutions, including payroll, employer compliance, HR and employee benefits administration, risk management outsourcing, and the on-site availability of a professionally trained HR representative; and retirement services administration, including plan implementation, ongoing compliance with government regulations, employee and employer reporting, participant and employer online access, electronic funds transfer, and other administrative services. In addition, the company offers cloud-based HR administration software products for employee benefits management and administration, time and attendance, digital communication solutions, recruiting, and onboarding solutions; plan administration outsourcing and state unemployment insurance services; various business services to small to medium-sized businesses comprising payroll funding and outsourcing services, which include payroll processing, invoicing, and tax preparation; and payment processing services, financial fitness programs, and a small-business loan resource center. Further, it provides insurance services for property and casualty coverage, such as workers' compensation, business-owner policies, cyber security protection, and commercial auto, as well as health and benefits coverage, including health, dental, vision, and life. The company markets and sells its services primarily through its direct sales force. Paychex, Inc. was founded in 1971 and is headquartered in Rochester, New York.",
        fullTimeEmployees=15000,
        city="Rochester",
        state="NY",
        trailingPE=34.056816,
        dividendYield=0.026400002,
        averageVolume=1980800,
        regularMarketOpen=122.68,
        volume=2427403,
        fiftyTwoWeekHigh=141.92,
        fiftyTwoWeekLow=106.55,
        recommendationKey="hold",
        industry="Staffing & Employment Services"
    )
    db.session.add(PAYX)

    PAYC = Stock(
        name="Paycom Software, Inc.",
        ticker="PAYC",
        marketCap=17205796864,
        dayHigh=302.78,
        dayLow=286.52,
        currentPrice=286.64,
        longBusinessSummary="Paycom Software, Inc. provides cloud-based human capital management (HCM) solution delivered as software-as-a-service for small to mid-sized companies in the United States. It offers functionality and data analytics that businesses need to manage the employment life cycle from recruitment to retirement. The company's HCM solution provides a suite of applications in the areas of talent acquisition, including applicant tracking, candidate tracker, background checks, on-boarding, e-verify, and tax credit services; and time and labor management, such as time and attendance, scheduling/schedule exchange, time-off requests, labor allocation, labor management reports/push reporting, and geofencing/geotracking, and Microfence, a proprietary Bluetooth. Its HCM solution also offers payroll applications comprising better employee transaction interface, payroll and tax management, Paycom pay, expense management, mileage tracker/fixed and variable rates, garnishment management, and GL concierge applications; and talent management applications that include employee self-service, compensation budgeting, performance management, position management, and Paycom learning and content subscriptions, as well as my analytics, which offer employment predictor reporting. In addition, its HCM solution provides manager on-the-go that gives supervisors and managers the ability to perform a variety of tasks, such as approving time-off requests and expense reimbursements; direct data exchange; ask here, a tool for direct line of communication to ask work-related questions; document and checklist; government and compliance; benefits administration/benefits to carrier; COBRA administration; personnel action and performance discussion forms; surveys; and affordable care act applications, as well as Clue, which securely collect, track, and manage the vaccination and testing data of the workforce. Paycom Software, Inc. was founded in 1998 and is headquartered in Oklahoma City, Oklahoma.",
        fullTimeEmployees=5385,
        city="Oklahoma City",
        state="OK",
        trailingPE=97.16611,
        dividendYield=None,
        averageVolume=457885,
        regularMarketOpen=298.68,
        volume=269010,
        fiftyTwoWeekHigh=558.97,
        fiftyTwoWeekLow=255.82,
        recommendationKey="buy",
        industry="Software—Application"
    )
    db.session.add(PAYC)

    PYPL = Stock(
        name="PayPal Holdings, Inc.",
        ticker="PYPL",
        marketCap=84383473664,
        dayHigh=76.92,
        dayLow=71.6121,
        currentPrice=71.82,
        longBusinessSummary="PayPal Holdings, Inc. operates a technology platform that enables digital payments on behalf of merchants and consumers worldwide. It provides payment solutions under the PayPal, PayPal Credit, Braintree, Venmo, Xoom, Zettle, Hyperwallet, Honey, and Paidy names. The company's payments platform allows consumers to send and receive payments in approximately 200 markets and in approximately 100 currencies, withdraw funds to their bank accounts in 56 currencies, and hold balances in their PayPal accounts in 25 currencies. PayPal Holdings, Inc. was founded in 1998 and is headquartered in San Jose, California.",
        fullTimeEmployees=30900,
        city="San Jose",
        state="CA",
        trailingPE=17.268574,
        dividendYield=None,
        averageVolume=17349353,
        regularMarketOpen=75.68,
        volume=15005631,
        fiftyTwoWeekHigh=310.16,
        fiftyTwoWeekLow=70.47,
        recommendationKey="buy",
        industry="Credit Services"
    )
    db.session.add(PYPL)

    PENN = Stock(
        name="Penn National Gaming, Inc.",
        ticker="PENN",
        marketCap=5388850176,
        dayHigh=33.9,
        dayLow=31.77,
        currentPrice=31.79,
        longBusinessSummary="Penn National Gaming, Inc., together with its subsidiaries, owns and manages gaming and racing properties, and operates video gaming terminals. It operates through five segments: Northeast, South, West, Midwest, Interactive. The company offers casino gaming, online gaming, live racing, sports betting, and digital sports content. As of December 31, 2021, the company owned, managed, or had ownership interests in 44 gaming and racing properties in 20 states. It owns various trademarks and service marks, including, Ameristar, Argosy, Boomtown, Greektown, Hollywood Casino, Hollywood Gaming, Tropicana Las Vegas, L'Auberge, M Resort, and My Choice. The company was formerly known as PNRC Corp. and changed its name to Penn National Gaming, Inc. in 1994. Penn National Gaming, Inc. was founded in 1972 and is based in Wyomissing, Pennsylvania.",
        fullTimeEmployees=21973,
        city="Wyomissing",
        state="PA",
        trailingPE=13.476049,
        dividendYield=None,
        averageVolume=4335782,
        regularMarketOpen=33.09,
        volume=3932767,
        fiftyTwoWeekHigh=86.4,
        fiftyTwoWeekLow=26.46,
        recommendationKey="buy",
        industry="Resorts & Casinos"
    )
    db.session.add(PENN)

    PEP = Stock(
        name="PepsiCo, Inc.",
        ticker="PEP",
        marketCap=226768420864,
        dayHigh=168.45,
        dayLow=163.85,
        currentPrice=164.01,
        longBusinessSummary="PepsiCo, Inc. manufactures, markets, distributes, and sells various beverages and convenient foods worldwide. The company operates through seven segments: Frito-Lay North America; Quaker Foods North America; PepsiCo Beverages North America; Latin America; Europe; Africa, Middle East and South Asia; and Asia Pacific, Australia and New Zealand and China Region. It provides dips, cheese-flavored snacks, and spreads, as well as corn, potato, and tortilla chips; cereals, rice, pasta, mixes and syrups, granola bars, grits, oatmeal, rice cakes, simply granola, and side dishes; beverage concentrates, fountain syrups, and finished goods; ready-to-drink tea, coffee, and juices; dairy products; and sparkling water makers and related products. It serves wholesale and other distributors, foodservice customers, grocery stores, drug stores, convenience stores, discount/dollar stores, mass merchandisers, membership stores, hard discounters, e-commerce retailers and authorized independent bottlers, and others through a network of direct-store-delivery, customer warehouse, and distributor networks, as well as directly to consumers through e-commerce platforms and retailers. The company was founded in 1898 and is headquartered in Purchase, New York.",
        fullTimeEmployees=309000,
        city="Purchase",
        state="NY",
        trailingPE=27.940374,
        dividendYield=0.026500002,
        averageVolume=5450977,
        regularMarketOpen=167.15,
        volume=4391330,
        fiftyTwoWeekHigh=177.62,
        fiftyTwoWeekLow=147.2,
        recommendationKey="buy",
        industry="Beverages—Non-Alcoholic"
    )
    db.session.add(PEP)

    PKI = Stock(
        name="PerkinElmer, Inc.",
        ticker="PKI",
        marketCap=17835845632,
        dayHigh=145.759,
        dayLow=140.86,
        currentPrice=141.33,
        longBusinessSummary="PerkinElmer, Inc. provides products, services, and solutions to the diagnostics, life sciences, and applied services markets worldwide. It operates through two segments, Discovery & Analytical Solutions and Diagnostics. The Discovery & Analytical Solutions segment offers a suite of solutions, including reagents, informatics, and detection and imaging technologies that enable scientists to enhance research breakthroughs in the life sciences research market, as well as contract research and laboratory services. It also provides analytical technologies, solutions, and services for the environmental, food, and industrial markets that enable its customers to understand the characterize the health of various aspects, including air, water, and soil. In addition, this segment offers solutions to farmers and food producers; and analytical instrumentation for the industrial market, which includes the chemical, semiconductor and electronics, energy, lubricant, petrochemical, and polymer industries. The Diagnostics segment provides instruments, reagents, assay platforms, and software products for the early detection of genetic disorders, such as pregnancy and early childhood, as well as infectious disease testing in the diagnostics market. Its products are used for testing and screening genetic abnormalities, disorders, and diseases, including down syndrome, hypothyroidism, muscular dystrophy, infertility, and various metabolic conditions. This segment also develops technologies that enable and support genomic workflows using protein coupled receptor and next-generation DNA sequencing for applications in oncology, immunodiagnostics, and drug discovery. It serves pharmaceutical and biotechnology companies, laboratories, academic and research institutions, public health authorities, private healthcare organizations, doctors, and government agencies. PerkinElmer, Inc. was founded in 1937 and is headquartered in Waltham, Massachusetts.",
        fullTimeEmployees=16700,
        city="Waltham",
        state="MA",
        trailingPE=14.100569,
        dividendYield=0.0019,
        averageVolume=778738,
        regularMarketOpen=144.52,
        volume=377756,
        fiftyTwoWeekHigh=203.16,
        fiftyTwoWeekLow=132.78,
        recommendationKey="buy",
        industry="Diagnostics & Research"
    )
    db.session.add(PKI)

    PFE = Stock(
        name="Pfizer Inc.",
        ticker="PFE",
        marketCap=284347990016,
        dayHigh=51.97,
        dayLow=50.41,
        currentPrice=50.66,
        longBusinessSummary="Pfizer Inc. discovers, develops, manufactures, markets, distributes, and sells biopharmaceutical products worldwide. It offers medicines and vaccines in various therapeutic areas, including cardiovascular metabolic and women's health under the Premarin family and Eliquis brands; biologics, small molecules, immunotherapies, and biosimilars under the Ibrance, Xtandi, Sutent, Inlyta, Retacrit, Lorbrena, and Braftovi brands; and sterile injectable and anti-infective medicines, and oral COVID-19 treatment under the Sulperazon, Medrol, Zavicefta, Zithromax, Vfend, Panzyga, and Paxlovid brands. The company also provides medicines and vaccines in various therapeutic areas, such as pneumococcal disease, meningococcal disease, tick-borne encephalitis, and COVID-19 under the Comirnaty/BNT162b2, Nimenrix, FSME/IMMUN-TicoVac, Trumenba, and the Prevnar family brands; biosimilars for chronic immune and inflammatory diseases under the Xeljanz, Enbrel, Inflectra, Eucrisa/Staquis, and Cibinqo brands; and amyloidosis, hemophilia, and endocrine diseases under the Vyndaqel/Vyndamax, BeneFIX, and Genotropin brands. In addition, the company is involved in the contract manufacturing business. It serves wholesalers, retailers, hospitals, clinics, government agencies, pharmacies, and individual provider offices, as well as disease control and prevention centers. The company has collaboration agreements with Bristol-Myers Squibb Company; Astellas Pharma US, Inc.; Myovant Sciences Ltd.; Akcea Therapeutics, Inc; Merck KGaA; Valneva SE; BioNTech SE; and Arvinas, Inc. Pfizer Inc. was founded in 1849 and is headquartered in New York, New York.",
        fullTimeEmployees=79000,
        city="New York",
        state="NY",
        trailingPE=14.470152,
        dividendYield=0.0321,
        averageVolume=24537416,
        regularMarketOpen=51.83,
        volume=16417766,
        fiftyTwoWeekHigh=61.71,
        fiftyTwoWeekLow=38.82,
        recommendationKey="buy",
        industry="Drug Manufacturers—General"
    )
    db.session.add(PFE)

    PM = Stock(
        name="Philip Morris International Inc.",
        ticker="PM",
        marketCap=159481659392,
        dayHigh=103.875,
        dayLow=101.825,
        currentPrice=102.44,
        longBusinessSummary="Philip Morris International Inc., through its subsidiaries, manufactures and sells cigarettes, other nicotine-containing products, smoke-free products, and related electronic devices and accessories. The company offers IQOS smoke-free products, including heated tobacco and nicotine-containing vapor products under the HEETS, HEETS Creations, HEETS Dimensions, HEETS Marlboro, HEETS FROM MARLBORO, Marlboro Dimensions, Marlboro HeatSticks, and Parliament HeatSticks brands, as well as under the Fiit and Miix licensed brands. It also sells its products under the Marlboro, Parliament, Bond Street, Chesterfield, L&M, Lark, and Philip Morris brands. In addition, the company owns various cigarette brands, such as Dji Sam Soe, Sampoerna A, and Sampoerna U in Indonesia; and Fortune and Jackpot in the Philippines. It markets and sells its products in the European Union, Eastern Europe, the Middle East, Africa, South and Southeast Asia, East Asia, Australia, Latin America, and Canada. Philip Morris International Inc. was incorporated in 1987 and is headquartered in New York, New York.",
        fullTimeEmployees=69600,
        city="New York",
        state="NY",
        trailingPE=17.846691,
        dividendYield=0.0479,
        averageVolume=5745245,
        regularMarketOpen=102.99,
        volume=5036629,
        fiftyTwoWeekHigh=112.48,
        fiftyTwoWeekLow=85.64,
        recommendationKey="buy",
        industry="Tobacco"
    )
    db.session.add(PM)

    PNW = Stock(
        name="Pinnacle West Capital Corporation",
        ticker="PNW",
        marketCap=8253838336,
        dayHigh=73.555,
        dayLow=72.89,
        currentPrice=73.16,
        longBusinessSummary="Pinnacle West Capital Corporation, through its subsidiary, Arizona Public Service Company, provides retail and wholesale electric services primarily in the state of Arizona. The company engages in the generation, transmission, and distribution of electricity using coal, nuclear, gas, oil, and solar generating facilities. Its transmission facilities include approximately 5,814 pole miles of overhead lines and approximately 74 miles of underground lines; and distribution facilities comprise approximately 11,258 miles of overhead lines and approximately 22,821 miles of underground primary cable, as well as owns and maintains 475 transmission and distribution substations. The company also owns or leases approximately 6,323 megawatts of regulated generation capacity. It serves approximately 1.3 million customers. Pinnacle West Capital Corporation was incorporated in 1985 and is headquartered in Phoenix, Arizona.",
        fullTimeEmployees=5872,
        city="Phoenix",
        state="AZ",
        trailingPE=14.507237,
        dividendYield=0.0464,
        averageVolume=739672,
        regularMarketOpen=73.02,
        volume=626159,
        fiftyTwoWeekHigh=86.87,
        fiftyTwoWeekLow=62.78,
        recommendationKey="hold",
        industry="Utilities—Regulated Electric"
    )
    db.session.add(PNW)

    PXD = Stock(
        name="Pioneer Natural Resources Company",
        ticker="PXD",
        marketCap=57452056576,
        dayHigh=238.54,
        dayLow=231.175,
        currentPrice=235.33,
        longBusinessSummary="Pioneer Natural Resources Company operates as an independent oil and gas exploration and production company in the United States. The company explores for, develops, and produces oil, natural gas liquids (NGLs), and gas. It has operations in the Midland Basin in West Texas. As of December 31, 2021, the company had proved undeveloped reserves and proved developed non-producing reserves of 130 million barrels of oil, 92 million barrels of NGLs, and 462 billion cubic feet of gas; and owned interests in 11 gas processing plants. Pioneer Natural Resources Company was founded in 1997 and is headquartered in Irving, Texas.",
        fullTimeEmployees=1932,
        city="Irving",
        state="TX",
        trailingPE=37.472927,
        dividendYield=0.0471,
        averageVolume=2598895,
        regularMarketOpen=236.75,
        volume=2781582,
        fiftyTwoWeekHigh=288.46,
        fiftyTwoWeekLow=133.73,
        recommendationKey="buy",
        industry="Oil & Gas E&P"
    )
    db.session.add(PXD)

    PNC = Stock(
        name="The PNC Financial Services Group, Inc.",
        ticker="PNC",
        marketCap=67516899328,
        dayHigh=164.95,
        dayLow=159.73,
        currentPrice=159.75,
        longBusinessSummary="The PNC Financial Services Group, Inc. operates as a diversified financial services company in the United States. The company's Retail Banking segment offers brokerage, insurance, and investment and cash management services; checking, savings, and money market accounts; certificates of deposits; and lending products, which includes residential mortgages, home equity loans and lines of credit, auto loans, education loans, and personal and small business loans, and credit cards to consumer and small business customers through a network of branches, ATMs, call centers, and online and mobile banking channels. Its Corporate & Institutional Banking segment provides secured and unsecured loans, letters of credit, and equipment leases; cash and investment management services, receivables and disbursement management services, funds transfer services, international payment services, and access to online/mobile information management and reporting services; foreign exchange, derivatives, fixed income, securities underwriting, loan syndications, and mergers and acquisitions and equity capital markets advisory related services; and commercial loan servicing and technology solutions for the commercial real estate finance industry. The company's Asset Management Group segment offers investment and retirement planning, customized investment management, credit and cash management solutions, private banking, and trust management and administration solutions; and multi-generational family planning products, such as estate, financial, tax planning, fiduciary, and customized performance reporting services. This segment also provides outsourced chief investment officer, custody, private real estate, cash and fixed income client solutions, and fiduciary retirement advisory services. As of December 31, 2021, it operated 2,629 branches and 9,523 ATMs. The PNC Financial Services Group, Inc. was founded in 1852 and is headquartered in Pittsburgh, Pennsylvania.",
        fullTimeEmployees=57668,
        city="Pittsburgh",
        state="PA",
        trailingPE=15.703332,
        dividendYield=0.0381,
        averageVolume=2330104,
        regularMarketOpen=162.57,
        volume=1577503,
        fiftyTwoWeekHigh=228.14,
        fiftyTwoWeekLow=149.51,
        recommendationKey="buy",
        industry="Banks—Regional"
    )
    db.session.add(PNC)

    POOL = Stock(
        name="Pool Corporation",
        ticker="POOL",
        marketCap=14154270720,
        dayHigh=359.4,
        dayLow=350.56,
        currentPrice=353.08,
        longBusinessSummary="Pool Corporation distributes swimming pool supplies, equipment, and related leisure products in the United States and internationally. The company offers maintenance products, including chemicals, supplies, and pool accessories; repair and replacement parts for pool equipment, such as cleaners, filters, heaters, pumps, and lights; fiberglass pools, and hot tubs and packaged pool kits comprising walls, liners, braces, and coping for in-ground and above-ground pools; pool equipment and components for new pool construction and the remodeling of existing pools; and irrigation and related products consisting of irrigation system components, and professional lawn care equipment and supplies. It also provides building materials, such as concrete, plumbing and electrical components, functional and decorative pool surfaces, decking materials, tiles, hardscapes, and natural stones for pool installations and remodeling; and commercial products, including heaters, safety equipment, and commercial pumps and filters. In addition, the company offers other pool construction and recreational products comprising discretionary recreational and related outdoor living products, such as grills and components for outdoor kitchens. It serves swimming pool remodelers and builders; specialty retailers that sell swimming pool supplies; swimming pool repair and service businesses; irrigation construction and landscape maintenance contractors; and commercial customers that serve hotels, universities, and community recreational facilities. As of March 03, 2022, the company operated 410 sales centers in North America, Europe, and Australia. Pool Corporation was incorporated in 1993 and is headquartered in Covington, Louisiana.",
        fullTimeEmployees=5500,
        city="Covington",
        state="LA",
        trailingPE=23.932758,
        dividendYield=0.0097,
        averageVolume=453375,
        regularMarketOpen=355.26,
        volume=581248,
        fiftyTwoWeekHigh=582.27,
        fiftyTwoWeekLow=324.14,
        recommendationKey="buy",
        industry="Leisure"
    )
    db.session.add(POOL)

    PPG = Stock(
        name="PPG Industries, Inc.",
        ticker="PPG",
        marketCap=28314816512,
        dayHigh=123.545,
        dayLow=118.86,
        currentPrice=119.27,
        longBusinessSummary="PPG Industries, Inc. manufactures and distributes paints, coatings, and specialty materials worldwide. The company's Performance Coatings segment offers coatings, solvents, adhesives, sealants, sundries, and software for automotive and commercial transport/fleet repair and refurbishing, light industrial coatings, and specialty coatings for signs; and coatings, sealants, transparencies, transparent armor, adhesives, engineered materials, and packaging and chemical management services for commercial, military, regional jet, and general aviation aircraft. It also provides coatings and finishes for the protection of metals and structures, such as metal fabricators, heavy duty maintenance contractors, and manufacturers of ships, bridges, and rail cars; paints, wood stains, adhesives, and purchased sundries for painting and maintenance contractors, and consumers for decoration and maintenance of residential and commercial building structures; and paints, thermoplastics, pavement marking products, and other technologies for pavement marking. The company's Industrial Coatings segment offers coatings, adhesives and sealants, and metal pretreatments, as well as services and coatings applications for appliances, agricultural and construction equipment, consumer electronics, automotive parts and accessories, building products, kitchenware, and transportation vehicles and other finished products; and on-site coatings services. It also provides coatings for metal cans, closures, plastic tubes, and promotional and specialty packaging; amorphous precipitated silica for tire, battery separator, and other end-uses; TESLIN substrates for labels, e-passports, drivers' licenses, breathable membranes, and loyalty and identification cards; and organic light emitting diode materials, displays and lighting lens materials, optical lenses, color-change products, and photochromic dyes. The company was incorporated in 1883 and is headquartered in Pittsburgh, Pennsylvania.",
        fullTimeEmployees=49300,
        city="Pittsburgh",
        state="PA",
        trailingPE=20.04201,
        dividendYield=0.019299999,
        averageVolume=1530135,
        regularMarketOpen=121.77,
        volume=2067199,
        fiftyTwoWeekHigh=177.32,
        fiftyTwoWeekLow=107.06,
        recommendationKey="buy",
        industry="Specialty Chemicals"
    )
    db.session.add(PPG)

    PFG = Stock(
        name="Principal Financial Group, Inc.",
        ticker="PFG",
        marketCap=18053849088,
        dayHigh=69.55,
        dayLow=67.83,
        currentPrice=68.11,
        longBusinessSummary="Principal Financial Group, Inc. provides retirement, asset management, and insurance products and services to businesses, individuals, and institutional clients worldwide. The company operates through Retirement and Income Solutions, Principal Global Investors, Principal International, and U.S. Insurance Solutions segments. The Retirement and Income Solutions segment provides a portfolio of asset accumulation products and services for retirement savings and income. It offers products and services for defined contribution plans, including 401(k) and 403(b) plans, defined benefit pension plans, nonqualified executive benefit plans, employee stock ownership plans, equity compensation, and pension risk transfer services; individual retirement accounts; investment only products; and mutual funds, individual variable annuities, and bank products. The Principal Global Investors segment provides equity, fixed income, real estate, and other alternative investments, as well as asset allocation, stable value management, and other structured investment strategies. The Principal International segment offers pension accumulation products and services, mutual funds, asset management, income annuities, and life insurance accumulation products, as well as voluntary savings plans in Brazil, Chile, Mexico, China, Hong Kong Special Administrative Region, India, and Southeast Asia. The U.S. Insurance Solutions segment provides specialty benefits, such as group dental and vision insurance, group life insurance, and group and individual disability insurance, as well as administers group dental, disability, and vision benefits; and individual life insurance products comprising universal, variable universal, indexed universal, and term life insurance products in the United States. It also offers insurance solutions for small and medium-sized businesses and their owners, as well as executives. Principal Financial Group, Inc. was founded in 1879 and is based in Des Moines, Iowa.",
        fullTimeEmployees=18600,
        city="Des Moines",
        state="IA",
        trailingPE=10.950161,
        dividendYield=0.0366,
        averageVolume=1752996,
        regularMarketOpen=68.34,
        volume=1168522,
        fiftyTwoWeekHigh=80.36,
        fiftyTwoWeekLow=58.66,
        recommendationKey="hold",
        industry="Insurance—Diversified"
    )
    db.session.add(PFG)

    PG = Stock(
        name="The Procter & Gamble Company",
        ticker="PG",
        marketCap=341019361280,
        dayHigh=144.09,
        dayLow=140.58,
        currentPrice=140.92,
        longBusinessSummary="The Procter & Gamble Company provides branded consumer packaged goods to consumers in North and Latin America, Europe, the Asia Pacific, Greater China, India, the Middle East, and Africa. It operates in five segments: Beauty; Grooming; Health Care; Fabric & Home Care; and Baby, Feminine & Family Care. The Beauty segment offers conditioners, shampoos, styling aids, and treatments; and antiperspirants and deodorants, personal cleansing, and skin care products under the Head & Shoulders, Herbal Essences, Pantene, Rejoice, Olay, Old Spice, Safeguard, Secret, and SK-II brands. The Procter & Gamble Company was founded in 1837 and is headquartered in Cincinnati, Ohio.",
        fullTimeEmployees=101000,
        city="Cincinnati",
        state="OH",
        trailingPE=25.752924,
        dividendYield=0.0238,
        averageVolume=7911551,
        regularMarketOpen=143.54,
        volume=5880561,
        fiftyTwoWeekHigh=165.35,
        fiftyTwoWeekLow=129.5,
        recommendationKey="buy",
        industry="Household & Personal Products"
    )
    db.session.add(PG)

    PGR = Stock(
        name="The Progressive Corporation",
        ticker="PGR",
        marketCap=67451445248,
        dayHigh=118.36,
        dayLow=115.27,
        currentPrice=115.42,
        longBusinessSummary="The Progressive Corporation, an insurance holding company, provides personal and commercial auto, personal residential and commercial property, general liability, and other specialty property-casualty insurance products and related services in the United States. It operates in three segments: Personal Lines, Commercial Lines, and Property. The Personal Lines segment writes insurance for personal autos and recreational vehicles (RV). This segment's products include personal auto insurance; and special lines products, including insurance for motorcycles, ATVs, RVs, watercrafts, snowmobiles, and related products. The Commercial Lines segment provides auto-related primary liability and physical damage insurance, and business-related general liability and property insurance for autos, vans, pick-up trucks, and dump trucks used by small businesses; tractors, trailers, and straight trucks primarily used by regional general freight and expeditor-type businesses, and long-haul operators; dump trucks, log trucks, and garbage trucks used by dirt, sand and gravel, logging, and coal-type businesses; and tow trucks and wreckers used in towing services and gas/service station businesses; as well as non-fleet and airport taxis, and black-car services. The Property segment writes residential property insurance for homeowners, other property owners, and renters, as well as offers personal umbrella insurance, and primary and excess flood insurance. The company also offers policy issuance and claims adjusting services; and acts as an agent to homeowner general liability, workers' compensation insurance, and other products. In addition, it provides reinsurance services. The company sells its products through independent insurance agencies, as well as directly on Internet through mobile devices, and over the phone. The Progressive Corporation was founded in 1937 and is headquartered in Mayfield, Ohio.",
        fullTimeEmployees=49077,
        city="Mayfield",
        state="OH",
        trailingPE=16.776163,
        dividendYield=0.0037,
        averageVolume=3048393,
        regularMarketOpen=117.24,
        volume=3272272,
        fiftyTwoWeekHigh=121.36,
        fiftyTwoWeekLow=89.35,
        recommendationKey="hold",
        industry="Insurance—Property & Casualty"
    )
    db.session.add(PGR)

    PLD = Stock(
        name="Prologis, Inc.",
        ticker="PLD",
        marketCap=87950336000,
        dayHigh=123.095,
        dayLow=118.59,
        currentPrice=118.96,
        longBusinessSummary="Prologis, Inc. is the global leader in logistics real estate with a focus on high-barrier, high-growth markets. As of December 31, 2020, the company owned or had investments in, on a wholly owned basis or through co-investment ventures, properties and development projects expected to total approximately 984 million square feet (91 million square meters) in 19 countries. Prologis leases modern logistics facilities to a diverse base of approximately 5,500 customers principally across two major categories: business-to-business and retail/online fulfillment.",
        fullTimeEmployees=2053,
        city="San Francisco",
        state="CA",
        trailingPE=44.992435,
        dividendYield=0.024600001,
        averageVolume=4783100,
        regularMarketOpen=121.67,
        volume=3092522,
        fiftyTwoWeekHigh=174.54,
        fiftyTwoWeekLow=106.46,
        recommendationKey="buy",
        industry="REIT—Industrial"
    )
    db.session.add(PLD)

    PRU = Stock(
        name="Prudential Financial, Inc.",
        ticker="PRU",
        marketCap=36923039744,
        dayHigh=99.745,
        dayLow=97.6,
        currentPrice=97.68,
        longBusinessSummary="Prudential Financial, Inc., together with its subsidiaries, provides insurance, investment management, and other financial products and services in the United States and internationally. It operates through eight segments: PGIM, Retirement, Group Insurance, Individual Annuities, Individual Life, Assurance IQ, International Businesses, and Closed Block. The company offers investment management services and solutions related to public fixed income, public equity, real estate debt and equity, private credit and other alternatives, and multi-asset class strategies to institutional and retail clients, as well as its general account. It also provides a range of retirement investment, and income products and services to retirement plan sponsors in the public, private, and not-for-profit sectors; and group life, long-term and short-term group disability, and group corporate-, bank-, and trust-owned life insurance in the United States, primarily to institutional clients for use in connection with employee and membership benefits plans, as well as sells accidental death and dismemberment, and other supplemental health solutions; and provides plan administration services in connection with its insurance coverages. In addition, the company develops and distributes individual variable and fixed annuity products, principally to the mass affluent and affluent markets; and individual variable, term, and universal life insurance products to the mass middle, mass affluent, and affluent markets in the United States. Further, it provides third-party life, health, Medicare, property and casualty, and term life products to retail shoppers through its digital and independent agent channels. The company offers its products and services to individual and institutional customers through its proprietary and third-party distribution networks. Prudential Financial, Inc. was founded in 1875 and is headquartered in Newark, New Jersey.",
        fullTimeEmployees=40916,
        city="Newark",
        state="NJ",
        trailingPE=5.3205514,
        dividendYield=0.047399998,
        averageVolume=1919082,
        regularMarketOpen=98.7,
        volume=1796492,
        fiftyTwoWeekHigh=124.22,
        fiftyTwoWeekLow=90.25,
        recommendationKey="hold",
        industry="Insurance—Life"
    )
    db.session.add(PRU)

    PTC = Stock(
        name="PTC Inc.",
        ticker="PTC",
        marketCap=12540401664,
        dayHigh=112.98,
        dayLow=106.24,
        currentPrice=106.39,
        longBusinessSummary="PTC Inc. operates as software and services company in the Americas, Europe, and the Asia Pacific. The company operates in two segments, Software Products and Professional Services. It offers ThingWorx platform, which offers a set of capabilities that enable enterprises to digitally transform every aspect of their business with innovative solutions that are simple to create, easy to implement, scalable to meet future needs, and designed to enable customers to accelerate time to value; and Vuforia, which enables the visualization of digital information in a physical context and the creation of AR. The company also provides Onshape, a software-as-a-service product development platform unites computer-aided design with data management, collaboration tools, and real-time analytics; Arena, a PLM solution enables product teams to collaborate virtually anytime and anywhere; Creo, a 3D CAD technology enables the digital design, testing, and modification of product models; and Windchill, a product lifecycle management software. In addition, it offers Integrity, an application lifecycle management solution; Servigistics, service parts management solution; and consulting, implementation, training, cloud, and license and support services. The company was formerly known as Parametric Technology Corporation and changed its name to PTC Inc. in January 2013. PTC Inc. was incorporated in 1985 and is headquartered in Boston, Massachusetts.",
        fullTimeEmployees=6709,
        city="Boston",
        state="MA",
        trailingPE=26.399502,
        dividendYield=None,
        averageVolume=797091,
        regularMarketOpen=112.49,
        volume=956310,
        fiftyTwoWeekHigh=153.73,
        fiftyTwoWeekLow=96.55,
        recommendationKey="buy",
        industry="Software—Application"
    )
    db.session.add(PTC)

    PSA = Stock(
        name="Public Storage",
        ticker="PSA",
        marketCap=54616068096,
        dayHigh=318.185,
        dayLow=311.09,
        currentPrice=311.46,
        longBusinessSummary="Public Storage, a member of the S&P 500 and FT Global 500, is a REIT that primarily acquires, develops, owns and operates self-storage facilities. At September 30, 2020, we had: (i) interests in 2,504 self-storage facilities located in 38 states with approximately 171 million net rentable square feet in the United States, (ii) an approximate 35% common equity interest in Shurgard Self Storage SA (Euronext Brussels:SHUR) which owned 239 self-storage facilities located in seven Western European nations with approximately 13 million net rentable square feet operated under the Shurgard brand and (iii) an approximate 42% common equity interest in PS Business Parks, Inc. (NYSE:PSB) which owned and operated approximately 28 million rentable square feet of commercial space at September 30, 2020. Our headquarters are located in Glendale, California.",
        fullTimeEmployees=5800,
        city="Glendale",
        state="CA",
        trailingPE=37.207024,
        dividendYield=0.0251,
        averageVolume=783927,
        regularMarketOpen=316.46,
        volume=593323,
        fiftyTwoWeekHigh=421.76,
        fiftyTwoWeekLow=292.32,
        recommendationKey="buy",
        industry="REIT—Industrial"
    )
    db.session.add(PSA)

    PHM = Stock(
        name="PulteGroup, Inc.",
        ticker="PHM",
        marketCap=10094525440,
        dayHigh=41.24,
        dayLow=39.84,
        currentPrice=39.87,
        longBusinessSummary="PulteGroup, Inc., through its subsidiaries, primarily engages in the homebuilding business in the United States. It acquires and develops land primarily for residential purposes; and constructs housing on such land. The company also offers various home designs, including single-family detached, townhomes, condominiums, and duplexes under the Centex, Pulte Homes, Del Webb, DiVosta Homes, American West, and John Wieland Homes and Neighborhoods brand names. As of December 31, 2021, it controlled 228,296 lots, of which 109,078 were owned and 119,218 were under land option agreements. In addition, the company arranges financing through the origination of mortgage loans primarily for homebuyers; sells the servicing rights for the originated loans; and provides title insurance policies, and examination and closing services to homebuyers. PulteGroup, Inc. was formerly known as Pulte Homes, Inc. and changed its name to PulteGroup, Inc. in March 2010. The company was founded in 1950 and is headquartered in Atlanta, Georgia.",
        fullTimeEmployees=6182,
        city="Atlanta",
        state="GA",
        trailingPE=6.167053,
        dividendYield=0.014099999,
        averageVolume=3042829,
        regularMarketOpen=40.78,
        volume=1858730,
        fiftyTwoWeekHigh=58.09,
        fiftyTwoWeekLow=35.03,
        recommendationKey="buy",
        industry="Residential Construction"
    )
    db.session.add(PHM)

    PVH = Stock(
        name="PVH Corp.",
        ticker="PVH",
        marketCap=4255337984,
        dayHigh=63.8,
        dayLow=60.665,
        currentPrice=60.81,
        longBusinessSummary="PVH Corp. operates as an apparel company worldwide. The company operates through six segments: Tommy Hilfiger North America, Tommy Hilfiger International, Calvin Klein North America, Calvin Klein International, Heritage Brands Wholesale, and Heritage Brands Retail. It designs, markets, and retails men's, women's, and children's apparel and accessories, including branded dress shirts, neckwear, sportswear, jeans wear, performance apparel, intimate apparel, underwear, swimwear, swim-related products, handbags, accessories, footwear, outerwear, home furnishings, luggage products, sleepwear, loungewear, hats, scarves, gloves, socks, watches and jewelry, eyeglasses and non-ophthalmic sunglasses, fragrance, home bed and bath furnishings, small leather goods, and other products. The company offers its products under its own brands, such as Tommy Hilfiger, Calvin Klein, Van Heusen, IZOD, ARROW, Warner's, Olga, Geoffrey Beene, and True&Co., as well as various other owned, licensed, and private label brands. It also licenses its own brands over various products. The company distributes its products at wholesale in department, chain, and specialty stores, as well as through warehouse clubs, mass market, and off-price and independent retailers; and through company-operated full-price, outlet stores, and concession locations, as well as through digital commerce sites. It markets its products to approximately 40 countries. PVH Corp. was founded in 1881 and is based in New York, New York.",
        fullTimeEmployees=19000,
        city="New York",
        state="NY",
        trailingPE=8.688384,
        dividendYield=0.0022,
        averageVolume=1749738,
        regularMarketOpen=62.93,
        volume=1149327,
        fiftyTwoWeekHigh=125.42,
        fiftyTwoWeekLow=57.82,
        recommendationKey="buy",
        industry="Apparel Manufacturing"
    )
    db.session.add(PVH)

    QRVO = Stock(
        name="Qorvo, Inc.",
        ticker="QRVO",
        marketCap=10862477312,
        dayHigh=101.86,
        dayLow=98.11,
        currentPrice=98.55,
        longBusinessSummary="Qorvo, Inc. develops and commercializes technologies and products for wireless and wired connectivity worldwide. The company operates through two segments, Mobile Products, and Infrastructure and Defense Products. The company offers integrated modules incorporating switches, power amplifiers, filters, multiplexers and other components, radio frequency (RF) power management integrated circuits, antenna tuners, antenna-plexers, discrete filters and duplexers, discrete switches, and ultra-wideband (UWB) system solutions. It also provides integrated solutions that include switch-LNA modules, variable gain amplifiers, discrete power amplifiers (PA), and integrated PA Doherty modules for massive multiple-input/multiple-output systems; RF products and compound semiconductor foundry services to defense primes and other global defense and aerospace customers; Wi-Fi customer premises equipment, including power amplifiers, switches, low noise amplifiers, and bulk acoustic wave filters; system-on-a-chip (SoC) hardware, firmware, and application software for smart home applications; automotive RF connectivity products and UWB SoC solutions; and power application controllers and programmable analog power ICs. The company sells its products directly to original equipment manufacturers and original design manufacturers, as well as through a network of sales representative firms and distributors. Qorvo, Inc. was founded in 1957 and is headquartered in Greensboro, North Carolina.",
        fullTimeEmployees=8400,
        city="Greensboro",
        state="NC",
        trailingPE=10.20609,
        dividendYield=None,
        averageVolume=1419445,
        regularMarketOpen=100.02,
        volume=1109672,
        fiftyTwoWeekHigh=201.46,
        fiftyTwoWeekLow=91.91,
        recommendationKey="buy",
        industry="Semiconductors"
    )
    db.session.add(QRVO)

    PWR = Stock(
        name="Quanta Services, Inc.",
        ticker="PWR",
        marketCap=17684125696,
        dayHigh=129.86,
        dayLow=123.79,
        currentPrice=124.1,
        longBusinessSummary="Quanta Services, Inc. provides specialty contracting services worldwide. The Electric Power Infrastructure Solutions segment engages in the design, procurement, construction, upgrade, repair, and maintenance of electric power transmission and distribution infrastructure and substation facilities; energized installation, maintenance, and upgrade of electric power infrastructure projects; installation of smart grid technologies on electric power networks; and design, installation, maintenance, and repair of commercial and industrial wirings. This segment also offers aviation services; emergency restoration services; and other engineering and technical services; design and construction solutions to wireline and wireless communications, cable multi-system operators, and other customers; and training for electric workers, as well as training for the gas distribution and communications industries. The Renewable Energy Infrastructure Solutions segment is the involved in engineering, procurement, construction, upgrade, repair, and maintenance services to renewable generation facilities, such as wind, solar, and hydropower generation facilities, as well as battery storage facilities; and provision of engineering and construction services for substations and switchyards, transmission, and other electrical infrastructures. The Underground Utility and Infrastructure Solutions segment offers design, engineering, construction, upgrade repair, and maintenance services to customers involved in the transportation, distribution, storage and processing of natural gas, oil, and other products; fabrication of pipeline support systems and related structures and facilities; and engineering and construction of pipeline and storage systems, and compressor and pump stations. The company was formerly known as Fabal Construction, Inc. and changed its name to Quanta Services, Inc. in November 1997. Quanta Services, Inc. was incorporated in 1997 and is headquartered in Houston, Texas.",
        fullTimeEmployees=43700,
        city="Houston",
        state="TX",
        trailingPE=32.58073,
        dividendYield=0.0025,
        averageVolume=1747385,
        regularMarketOpen=128.45,
        volume=888286,
        fiftyTwoWeekHigh=140.04,
        fiftyTwoWeekLow=84.4,
        recommendationKey="buy",
        industry="Engineering & Construction"
    )
    db.session.add(PWR)

    QCOM = Stock(
        name="QUALCOMM Incorporated",
        ticker="QCOM",
        marketCap=147392004096,
        dayHigh=136.45,
        dayLow=126.61,
        currentPrice=131.6,
        longBusinessSummary="QUALCOMM Incorporated engages in the development and commercialization of foundational technologies for the wireless industry worldwide. The company operates through three segments: Qualcomm CDMA Technologies (QCT); Qualcomm Technology Licensing (QTL); and Qualcomm Strategic Initiatives (QSI). The QCT segment develops and supplies integrated circuits and system software based on 3G/4G/5G and other technologies for use in wireless voice and data communications, networking, application processing, multimedia, and global positioning system products. The QTL segment grants licenses or provides rights to use portions of its intellectual property portfolio, which include various patent rights useful in the manufacture and sale of wireless products comprising products implementing CDMA2000, WCDMA,LTE and/or OFDMA-based 5G standards and their derivatives. The QSI segment invests in early-stage companies in various industries, including 5G, artificial intelligence, automotive, consumer, enterprise, cloud, and IoT, and investment for supporting the design and introduction of new products and services for voice and data communications, new industries, and applications. It also provides development, and other services and related products to the United States government agencies and their contractors. QUALCOMM Incorporated was incorpotared in 1985 and is headquartered in San Diego, California.",
        fullTimeEmployees=45000,
        city="San Diego",
        state="CA",
        trailingPE=16.72173,
        dividendYield=0.0222,
        averageVolume=11127756,
        regularMarketOpen=129.78,
        volume=27113344,
        fiftyTwoWeekHigh=193.58,
        fiftyTwoWeekLow=118.23,
        recommendationKey="buy",
        industry="Semiconductors"
    )
    db.session.add(QCOM)

    DGX = Stock(
        name="Quest Diagnostics Incorporated",
        ticker="DGX",
        marketCap=16740231168,
        dayHigh=139.86,
        dayLow=136.28,
        currentPrice=136.46,
        longBusinessSummary="Quest Diagnostics Incorporated provides diagnostic testing, information, and services in the United States and internationally. The company develops and delivers diagnostic information services, such as routine testing, non-routine and advanced clinical testing, anatomic pathology testing, and other diagnostic information services. It offers diagnostic information services primarily under the Quest Diagnostics brand, as well as under the AmeriPath, Dermpath Diagnostics, ExamOne, and Quanum brands to patients, clinicians, hospitals, independent delivery networks, health plans, employers, direct contract entities, and accountable care organizations through a network of laboratories, patient service centers, phlebotomists in physician offices, call centers and mobile paramedics, nurses, and other health and wellness professionals. The company also provides risk assessment services for the life insurance industry; and healthcare organizations and clinicians robust information technology solutions. Quest Diagnostics Incorporated was founded in 1967 and is headquartered in Secaucus, New Jersey.",
        fullTimeEmployees=50000,
        city="Secaucus",
        state="NJ",
        trailingPE=8.204173,
        dividendYield=0.0194,
        averageVolume=1042645,
        regularMarketOpen=139.09,
        volume=500377,
        fiftyTwoWeekHigh=174.16,
        fiftyTwoWeekLow=125.33,
        recommendationKey="buy",
        industry="Diagnostics & Research"
    )
    db.session.add(DGX)

    RL = Stock(
        name="Ralph Lauren Corporation",
        ticker="RL",
        marketCap=6851534336,
        dayHigh=97.39,
        dayLow=92.935,
        currentPrice=93.07,
        longBusinessSummary="Ralph Lauren Corporation designs, markets, and distributes lifestyle products in North America, Europe, Asia, and internationally. The company offers apparel, including a range of men's, women's, and children's clothing and accessories, which comprise casual shoes, dress shoes, boots, sneakers, sandals, eyewear, watches, fashion and fine jewelry, scarves, hats, gloves, umbrellas, and belts, as well as leather goods, such as handbags, luggage, small leather goods, and belts; home products consisting of bed and bath lines, furniture, fabric and wallcoverings, lighting, tabletop, floor coverings, and giftware; and fragrances. It sells apparel and accessories under the Ralph Lauren Collection, Ralph Lauren Purple Label, Polo Ralph Lauren, Double RL, Lauren Ralph Lauren, Polo Golf Ralph Lauren, Ralph Lauren Golf, RLX Ralph Lauren, Polo Ralph Lauren Children, Chaps, and Club Monaco brands; women's fragrances under the Ralph Lauren Collection, Woman by Ralph Lauren, Romance Collection, Ralph Collection, and Big Pony Women's brand names; and men's fragrances under the Polo Blue, Safari, Purple Label, Polo Red, Polo Green, Polo Black, Polo Supreme, Polo Sport, and Big Pony Men's brand names. The company's restaurant concepts include The Polo Bar in New York City; RL Restaurant in Chicago; Ralph's in Paris; and Ralph's Coffee concept. Ralph Lauren Corporation sells its products to department stores, specialty stores, and golf and pro shops, as well as directly to consumers through its retail stores, concession-based shop-within-shops, and its digital commerce sites. The company directly operates 548 retail stores and 650 concession-based shop-within-shops; and operates 139 Ralph Lauren stores, and 143 Club Monaco stores and shops through licensing partners. Ralph Lauren Corporation was founded in 1967 and is headquartered in New York, New York.",
        fullTimeEmployees=12100,
        city="New York",
        state="NY",
        trailingPE=17.212872,
        dividendYield=0.0275,
        averageVolume=1082229,
        regularMarketOpen=95.77,
        volume=668511,
        fiftyTwoWeekHigh=135.99,
        fiftyTwoWeekLow=86.54,
        recommendationKey="buy",
        industry="Apparel Manufacturing"
    )
    db.session.add(RL)

    RJF = Stock(
        name="Raymond James Financial, Inc.",
        ticker="RJF",
        marketCap=18933917696,
        dayHigh=94.7585,
        dayLow=91.57,
        currentPrice=91.84,
        longBusinessSummary="Raymond James Financial, Inc., a diversified financial services company, provides private client group, capital markets, asset management, banking, and other services to individuals, corporations, and municipalities in the United States, Canada, and Europe. The Private Client Group segment offers investment services, portfolio management services, insurance and annuity products, and mutual funds; support to third-party product partners, including sales and marketing support, as well as distribution and accounting, and administrative services; margin loans; and securities borrowing and lending services. The Capital Markets segment provides investment banking services, including equity underwriting, debt underwriting, and merger and acquisition advisory services; and fixed income and equity brokerage services. The Asset Management segment offers asset management, portfolio management, and related administrative services to retail and institutional clients; and administrative support services, such as record-keeping. The Raymond James Bank segment provides insured deposit accounts; commercial and industrial, commercial real estate (CRE) and CRE construction, tax-exempt, residential, securities-based, and other loans; and loan syndication services. The Other segment engages in the private equity investments, including various direct and third-party private equity investments; and legacy private equity funds. The company was founded in 1962 and is headquartered in St. Petersburg, Florida.",
        fullTimeEmployees=15000,
        city="Saint Petersburg",
        state="FL",
        trailingPE=13.852186,
        dividendYield=0.0143,
        averageVolume=1363188,
        regularMarketOpen=93.75,
        volume=613686,
        fiftyTwoWeekHigh=117.37,
        fiftyTwoWeekLow=81.96,
        recommendationKey="buy",
        industry="Capital Markets"
    )
    db.session.add(RJF)

    RTX = Stock(
        name="Raytheon Technologies Corporation",
        ticker="RTX",
        marketCap=140368035840,
        dayHigh=96.79,
        dayLow=93.68,
        currentPrice=93.78,
        longBusinessSummary="Raytheon Technologies Corporation, an aerospace and defense company, provides systems and services for the commercial, military, and government customers worldwide. It operates through four segments: Collins Aerospace Systems, Pratt & Whitney, Raytheon Intelligence & Space, and Raytheon Missiles & Defense. The Collins Aerospace Systems segment offers aerospace and defense products, and aftermarket service solutions for aircraft manufacturers and airlines, as well as regional, business, and general aviation; and for defense and commercial space operations. This segment also designs, produces, and supports cabin interior, communications and aviation systems, oxygen systems, food and beverage preparation, storage and galley systems, and lavatory and wastewater management systems; airborne intelligence, surveillance and reconnaissance systems, test and training range systems, crew escape systems, and simulation and training solutions; information management services; and aftermarket services that include spare parts, overhaul and repair, engineering and technical support, training and fleet management solutions, and information management services. The Pratt & Whitney segment supplies aircraft engines for commercial, military, business jet, and general aviation customers; and produces, sells, and services military and commercial auxiliary power units. The Raytheon Intelligence & Space segment develops and provides integrated space, communication, and sensor systems for missions, training, and cyber and software solutions to intelligence, defense, federal, and commercial customers. The Raytheon Missiles & Defense segment designs, develops, produces, and sustains integrated air and missile defense systems; defensive and combat solutions; land- and sea-based radars; command, control, communications, and intelligence solutions; and naval and undersea sensor solutions for the U.S. and foreign government customers. The company is headquartered in Waltham, Massachusetts.",
        fullTimeEmployees=174000,
        city="Waltham",
        state="MA",
        trailingPE=42.62727,
        dividendYield=0.0239,
        averageVolume=5157388,
        regularMarketOpen=95.43,
        volume=3358893,
        fiftyTwoWeekHigh=106.02,
        fiftyTwoWeekLow=79,
        recommendationKey="buy",
        industry="Aerospace & Defense"
    )
    db.session.add(RTX)

    O = Stock(
        name="Realty Income Corporation",
        ticker="O",
        marketCap=39111331840,
        dayHigh=70.68,
        dayLow=69.03,
        currentPrice=69.13,
        longBusinessSummary="Realty Income, The Monthly Dividend Company, is an S&P 500 company dedicated to providing stockholders with dependable monthly income. The company is structured as a REIT, and its monthly dividends are supported by the cash flow from over 6,500 real estate properties owned under long-term lease agreements with our commercial clients. To date, the company has declared 608 consecutive common stock monthly dividends throughout its 52-year operating history and increased the dividend 109 times since Realty Income's public listing in 1994 (NYSE: O). The company is a member of the S&P 500 Dividend Aristocrats index. Additional information about the company can be obtained from the corporate website at www.realtyincome.com.",
        fullTimeEmployees=367,
        city="San Diego",
        state="CA",
        trailingPE=54.518925,
        dividendYield=0.044,
        averageVolume=4065379,
        regularMarketOpen=69.9,
        volume=2786233,
        fiftyTwoWeekHigh=75.4,
        fiftyTwoWeekLow=62.29,
        recommendationKey="buy",
        industry="REIT—Retail"
    )
    db.session.add(O)

    REG = Stock(
        name="Regency Centers Corporation",
        ticker="REG",
        marketCap=10457690112,
        dayHigh=63.3,
        dayLow=60.965,
        currentPrice=61.08,
        longBusinessSummary="Regency Centers is the preeminent national owner, operator, and developer of shopping centers located in affluent and densely populated trade areas. Our portfolio includes thriving properties merchandised with highly productive grocers, restaurants, service providers, and best-in-class retailers that connect to their neighborhoods, communities, and customers. Operating as a fully integrated real estate company, Regency Centers is a qualified real estate investment trust (REIT) that is self-administered, self-managed, and an S&P 500 Index member.",
        fullTimeEmployees=432,
        city="Jacksonville",
        state="FL",
        trailingPE=31.484535,
        dividendYield=0.0368,
        averageVolume=979200,
        regularMarketOpen=62.68,
        volume=621169,
        fiftyTwoWeekHigh=78.78,
        fiftyTwoWeekLow=55.78,
        recommendationKey="buy",
        industry="REIT—Retail"
    )
    db.session.add(REG)

    REGN = Stock(
        name="Regeneron Pharmaceuticals, Inc.",
        ticker="REGN",
        marketCap=63925706752,
        dayHigh=604.33,
        dayLow=593.63,
        currentPrice=594.42,
        longBusinessSummary="Regeneron Pharmaceuticals, Inc. discovers, invents, develops, manufactures, and commercializes medicines for treating various diseases worldwide. The company's products include EYLEA injection to treat wet age-related macular degeneration and diabetic macular edema; myopic choroidal neovascularization; and diabetic retinopathy, as well as macular edema following retinal vein occlusion, including macular edema following central retinal vein occlusion and macular edema following branch retinal vein occlusion. It also provides Dupixent injection to treat atopic dermatitis and asthma in adults and pediatrics; Libtayo injection to treat metastatic or locally advanced cutaneous squamous cell carcinoma;Praluent injection for heterozygous familial hypercholesterolemia or clinical atherosclerotic cardiovascular disease in adults; REGEN-COV for covid-19; and Kevzara solution for treating rheumatoid arthritis in adults. In addition, the company offers Inmazeb injection for infection caused by Zaire ebolavirus; ARCALYST injection for cryopyrin-associated periodic syndromes, including familial cold auto-inflammatory syndrome and muckle-wells syndrome; and ZALTRAP injection for intravenous infusion to treat metastatic colorectal cancer; and develops product candidates for treating patients with eye, allergic and inflammatory, cardiovascular and metabolic, infectious, and rare diseases; and cancer, pain, and hematologic conditions. It has collaboration and license agreements with Sanofi; Bayer; Teva Pharmaceutical Industries Ltd.; Mitsubishi Tanabe Pharma Corporation; Alnylam Pharmaceuticals, Inc.; Roche Pharmaceuticals; and Kiniksa Pharmaceuticals, Ltd., as well as has an agreement with the U.S. Department of Health and Human Services, as well as with Zai Lab Limited; Intellia Therapeutics, Inc.; Biomedical Advanced Research Development Authority; and AstraZeneca PLC. The company was incorporated in 1988 and is headquartered in Tarrytown, New York.",
        fullTimeEmployees=10368,
        city="Tarrytown",
        state="NY",
        trailingPE=9.506764,
        dividendYield=None,
        averageVolume=709709,
        regularMarketOpen=600.67,
        volume=532418,
        fiftyTwoWeekHigh=747.42,
        fiftyTwoWeekLow=538.01,
        recommendationKey="buy",
        industry="Biotechnology"
    )
    db.session.add(REGN)

    RF = Stock(
        name="Regions Financial Corporation",
        ticker="RF",
        marketCap=18522288128,
        dayHigh=19.905,
        dayLow=19.335,
        currentPrice=19.43,
        longBusinessSummary="Regions Financial Corporation, a financial holding company, provides banking and bank-related services to individual and corporate customers. It operates through three segments: Corporate Bank, Consumer Bank, and Wealth Management. The Corporate Bank segment offers commercial banking services, such as commercial and industrial, commercial real estate, and investor real estate lending; equipment lease financing; deposit products; and securities underwriting and placement, loan syndication and placement, foreign exchange, derivatives, merger and acquisition, and other advisory services. It serves corporate, middle market, and commercial real estate developers and investors. The Consumer Bank segment provides consumer banking products and services related to residential first mortgages, home equity lines and loans, consumer credit cards, and other consumer loans, as well as deposits. The Wealth Management segment offers credit related products, and retirement and savings solutions; and trust and investment management, asset management, and estate planning services to individuals, businesses, governmental institutions, and non-profit entities. The company also provides investment and insurance products; low-income housing tax credit corporate fund syndication services; and other specialty financing services. As of March 01, 2022, it operated through a network of 1,300 banking offices and 2,000 automated teller machines across the South, Midwest, and Texas. Regions Financial Corporation was founded in 1971 and is headquartered in Birmingham, Alabama.",
        fullTimeEmployees=19723,
        city="Birmingham",
        state="AL",
        trailingPE=7.2798805,
        dividendYield=0.0342,
        averageVolume=8508012,
        regularMarketOpen=19.62,
        volume=5259878,
        fiftyTwoWeekHigh=25.57,
        fiftyTwoWeekLow=18.02,
        recommendationKey="buy",
        industry="Banks—Regional"
    )
    db.session.add(RF)

    RSG = Stock(
        name="Republic Services, Inc.",
        ticker="RSG",
        marketCap=40559624192,
        dayHigh=130.84,
        dayLow=127.78,
        currentPrice=127.91,
        longBusinessSummary="Republic Services, Inc., together with its subsidiaries, offers environmental services in the United States. The company offers collection and processing of recyclable materials, collection, transfer and disposal of non-hazardous solid waste, and other environmental solutions. Its collection services include curbside collection of material for transport to transfer stations, landfills, or recycling processing centers; supply of recycling and waste containers; and renting of compactors. In addition, the company engages in the processing and sale of old corrugated containers, old newsprint, aluminum, glass, and other materials; and provision of landfill and transfer services. Further, it offers disposal of non-hazardous solid and liquid material and in-plant services, such as transportation and logistics. It serves small-container, large-container, and residential customers. As of December 31, 2021, the company operated through 356 collection operations, 239 transfer stations, 198 active landfills, 71 recycling processing centers, 6 saltwater disposal wells, and 7 deep injection wells, as well as 3 treatment, recovery, and disposal facilities in 41 states. It also operated 77 landfill gas-to-energy and renewable energy projects and had 124 closed landfills. The company was incorporated in 1996 and is based in Phoenix, Arizona.",
        fullTimeEmployees=35000,
        city="Phoenix",
        state="AZ",
        trailingPE=33.74934,
        dividendYield=0.014099999,
        averageVolume=1301412,
        regularMarketOpen=129.83,
        volume=990739,
        fiftyTwoWeekHigh=145.98,
        fiftyTwoWeekLow=109.06,
        recommendationKey="buy",
        industry="Waste Management"
    )
    db.session.add(RSG)

    RMD = Stock(
        name="ResMed Inc.",
        ticker="RMD",
        marketCap=30786899968,
        dayHigh=215.62,
        dayLow=211.1375,
        currentPrice=211.27,
        longBusinessSummary="ResMed Inc. develops, manufactures, distributes, and markets medical devices and cloud-based software applications for the healthcare markets. The company operates in two segments, Sleep and Respiratory Care, and Software as a Service. It offers various products and solutions for a range of respiratory disorders, including technologies to be applied in medical and consumer products, ventilation devices, diagnostic products, mask systems for use in the hospital and home, headgear and other accessories, dental devices, and cloud-based software informatics solutions to manage patient outcomes, as well as provides customer and business processes. The company also provides AirView, a cloud-based system that enables remote monitoring and changing of patients' device settings; myAir, a personalized therapy management application for patients with sleep apnea that provides support, education, and troubleshooting tools for increased patient engagement and improved compliance; U-Sleep, a compliance monitoring solution that enables home medical equipment (HME)to streamline their sleep programs; and connectivity module and propeller solutions. In addition, it offers out-of-hospital software solution, such as Brightree business management software and service solutions to providers of HME, pharmacy, home infusion, orthotics, and prosthetics services; MatrixCare care management and related ancillary solutions to senior living, skilled nursing, life plan communities, home health, home care, and hospice agencies, as well as related accountable care organizations; and HEALTHCAREfirst that offers electronic health record, software, billing and coding services, and analytics for home health and hospice agencies. The company markets its products primarily to sleep clinics, home healthcare dealers, and hospitals through a network of distributors and direct sales force in approximately 140 countries. ResMed Inc. was founded in 1989 and is headquartered in San Diego, California.",
        fullTimeEmployees=7970,
        city="San Diego",
        state="CA",
        trailingPE=61.919697,
        dividendYield=0.0085,
        averageVolume=590674,
        regularMarketOpen=213.74,
        volume=580130,
        fiftyTwoWeekHigh=301.34,
        fiftyTwoWeekLow=189.4,
        recommendationKey="buy",
        industry="Medical Instruments & Supplies"
    )
    db.session.add(RMD)

    RHI = Stock(
        name="Robert Half International Inc.",
        ticker="RHI",
        marketCap=8435473920,
        dayHigh=79.105,
        dayLow=75.625,
        currentPrice=75.77,
        longBusinessSummary="Robert Half International Inc. provides staffing and risk consulting services in North America, South America, Europe, Asia, and Australia. The company operates through three segments: Temporary and Consultant Staffing, Permanent Placement Staffing, and Risk Consulting and Internal Audit Services. It places temporary services for accounting, finance, and bookkeeping; temporary and full-time office and administrative personnel consisting of executive and administrative assistants, receptionists, and customer service representatives; full-time accounting, financial, tax, and accounting operations personnel; and information technology contract professionals and full-time employees in the areas of platform systems integration to end-user technical and desktop support, including specialists in application development, networking and cloud, systems integration and deployment, database design and administration, and security and business continuity. The company also offers temporary and full-time employees in attorney, paralegal, legal administrative, and legal secretarial positions; and senior-level project professionals in the accounting and finance fields for financial systems conversions, expansion into new markets, business process re-engineering, business systems performance improvement, and post-merger financial consolidation. It is involved in serving professionals in the areas of creative, design, marketing, advertising, and public relations; and placing various positions, such as creative directors, graphics designers, web designers, media buyers, front end developers, copywriters, digital marketing managers, marketing analytics specialists, brand managers, and public relations specialists. The company provides internal audit, technology consulting, risk and compliance consulting, and business performance services. It serves clients and employment candidates. Robert Half International Inc. was founded in 1948 and is headquartered in Menlo Park, California.",
        fullTimeEmployees=14600,
        city="Menlo Park",
        state="CA",
        trailingPE=16.197092,
        dividendYield=0.0184,
        averageVolume=1051646,
        regularMarketOpen=78.13,
        volume=869626,
        fiftyTwoWeekHigh=125.77,
        fiftyTwoWeekLow=73.39,
        recommendationKey="hold",
        industry="Staffing & Employment Services"
    )
    db.session.add(RHI)

    ROK = Stock(
        name="Rockwell Automation, Inc.",
        ticker="ROK",
        marketCap=22928809984,
        dayHigh=202.75,
        dayLow=197.01,
        currentPrice=197.64,
        longBusinessSummary="Rockwell Automation, Inc. provides industrial automation and digital transformation solutions in the United States and internationally. The company operates in three segments, Intelligent Devices, Software & Control, and Lifecycle Services. Its solutions include hardware and software products, and services. The Intelligent Devices segment offers drives, motion, safety, sensing, industrial components, and configured-to-order products. The Software & Control segment provides control and visualization software and hardware, information software, digital twin and simulation software, and network and security infrastructure solutions. The Lifecycle Services segment provides consulting, professional services and solutions, and connected and maintenance services. The company sells its solutions primarily through independent distributors in relation with its direct sales force. It serves discrete end markets, including automotive, semiconductor, warehousing and logistics, and other discrete markets, as well as general industries comprising printing and publishing, marine, glass, fiber and textiles, airports, and aerospace; hybrid end markets, such as food and beverage, life sciences, household and personal care, and tire, as well as eco industrial, including water/wastewater, waste management, mass transit, and renewable energy; and process end markets comprising oil and gas, mining, metals, chemicals, pulp and paper, and others. Rockwell Automation, Inc. was founded in 1903 and is headquartered in Milwaukee, Wisconsin.",
        fullTimeEmployees=24500,
        city="Milwaukee",
        state="WI",
        trailingPE=17.067358,
        dividendYield=0.022,
        averageVolume=1082309,
        regularMarketOpen=201.08,
        volume=878126,
        fiftyTwoWeekHigh=354.99,
        fiftyTwoWeekLow=190.08,
        recommendationKey="hold",
        industry="Specialty Industrial Machinery"
    )
    db.session.add(ROK)

    ROL = Stock(
        name="Rollins, Inc.",
        ticker="ROL",
        marketCap=16980610048,
        dayHigh=35.41,
        dayLow=34.455,
        currentPrice=34.51,
        longBusinessSummary="Rollins, Inc., through its subsidiaries, provides pest and wildlife control services to residential and commercial customers in the United States and internationally. The company offers pest control services to residential properties protecting from common pests, including rodents, insects, and wildlife. It also provides workplace pest control solutions for customers across various end markets, such as healthcare, foodservice, and logistics. In addition, the company offers traditional and baiting termite protection, as well as ancillary services. It serves clients directly, as well as through franchisee operations. Rollins, Inc. was incorporated in 1948 and is headquartered in Atlanta, Georgia.",
        fullTimeEmployees=16482,
        city="Atlanta",
        state="GA",
        trailingPE=48.81188,
        dividendYield=0.0117,
        averageVolume=1507677,
        regularMarketOpen=35.32,
        volume=924364,
        fiftyTwoWeekHigh=40.11,
        fiftyTwoWeekLow=28.51,
        recommendationKey="hold",
        industry="Personal Services"
    )
    db.session.add(ROL)

    ROP = Stock(
        name="Roper Technologies, Inc.",
        ticker="ROP",
        marketCap=41317421056,
        dayHigh=402.4,
        dayLow=391.44,
        currentPrice=391.69,
        longBusinessSummary="Roper Technologies, Inc. designs and develops software, and engineered products and solutions. The company offers management, campus solutions, diagnostic and laboratory information management, enterprise management, information solutions, transportation management, financial and compliance management, and cloud-based financial analytics and performance management software; cloud-based software to the property and casualty insurance industry; and software, services, and technologies for foodservice operations. It also provides cloud-based data, collaboration, and estimating automation software; electronic marketplace; visual effects and 3D content software; wireless sensor network and solutions; cloud-based software for the life insurance and financial services industries; supply chain software; health care service and software; RFID card readers; data analytics and information; and pharmacy software solutions. In addition, the company offers precision rubber and polymer testing instruments, and data analysis software; ultrasound accessories; testing and analyzing plastic solutions; dispensers and metering pumps; control valves; precision weighing equipment; automated surgical scrub and linen dispensing equipment; water meters; optical and electromagnetic measurement systems; automated leak detection equipment; medical devices; products and services for water and gas utilities; and equipment and consumables. It also provides temperature control and emergency shutoff valves; turbomachinery control hardware, software, and services; specialized pumps; flow meter calibrators and controllers; vibration monitoring systems and controls; analytical instrument; drilling power section; and pressure and level sensors. The company was formerly known as Roper Industries, Inc. and changed its name to Roper Technologies, Inc. in April 2015. The company was incorporated in 1981 and is based in Sarasota, Florida.",
        fullTimeEmployees=19300,
        city="Sarasota",
        state="FL",
        trailingPE=37.17282,
        dividendYield=0.0058,
        averageVolume=688817,
        regularMarketOpen=400.01,
        volume=454694,
        fiftyTwoWeekHigh=505,
        fiftyTwoWeekLow=369.51,
        recommendationKey="buy",
        industry="Specialty Industrial Machinery"
    )
    db.session.add(ROP)

    ROST = Stock(
        name="Ross Stores, Inc.",
        ticker="ROST",
        marketCap=25715355648,
        dayHigh=77.3,
        dayLow=72.66,
        currentPrice=72.78,
        longBusinessSummary="Ross Stores, Inc., together with its subsidiaries, operates off-price retail apparel and home fashion stores under the Ross Dress for Less and dd's DISCOUNTS brand names. Its stores primarily offer apparel, accessories, footwear, and home fashions. The company's Ross Dress for Less stores sell its products at department and specialty stores primarily to middle income households; and dd's DISCOUNTS stores sell its products at department and discount stores for households with moderate income. As of March 7, 2022, it operated approximately 1,649 stores under the Ross Dress for Less name' and 303 dd's DISCOUNTS stores in 40 states, the District of Columbia, and Guam. Ross Stores, Inc. was incorporated in 1957 and is headquartered in Dublin, California.",
        fullTimeEmployees=100000,
        city="Dublin",
        state="CA",
        trailingPE=16.300112,
        dividendYield=0.0135,
        averageVolume=4126108,
        regularMarketOpen=76.61,
        volume=3612631,
        fiftyTwoWeekHigh=127.58,
        fiftyTwoWeekLow=69.75,
        recommendationKey="buy",
        industry="Apparel Retail"
    )
    db.session.add(ROST)

    SPGI = Stock(
        name="S&P Global Inc.",
        ticker="SPGI",
        marketCap=80180699136,
        dayHigh=344,
        dayLow=331.52,
        currentPrice=332.7,
        longBusinessSummary="S&P Global Inc., together with its subsidiaries, provides credit ratings, benchmarks, analytics, and workflow solutions in the global capital, commodity, and automotive markets. It operates in six divisions: S&P Global Ratings, S&P Dow Jones Indices, S&P Global Commodity Insights, S&P Global Market Intelligence, S&P Global Mobility, and S&P Global Engineering Solutions. The S&P Global Ratings division operates as an independent provider of credit ratings, research, and analytics, offering investors and other market participants information, ratings, and benchmarks. The S&P Dow Jones Indices division is an index provider that maintains various valuation and index benchmarks for investment advisors, wealth managers, and institutional investors. The S&P Global Commodity Insights division offers data and insights for global energy and commodity markets and enable its customers to make decisions. The S&P Global Market Intelligence division delivers data and technology solutions for customers to provide insights for making decisions. It offers data and services that bring end-to-end workflow solutions, including capital formation, data and distribution, ESG and sustainability, leveraged loans, private markets, sector coverage, supply chain, and issuer solutions, as well as credit, risk, and regulatory solutions. The S&P Global Mobility division provides insights derived from unmatched automotive data, enabling its customers to anticipate change and make decisions. The S&P Global Engineering Solutions division offers engineering expertise and solutions in industries, such as aerospace and defense, energy, architecture, construction, and transportation. Its solutions empower business and technical leaders to transform workflows and make decisions. S&P Global Inc. was founded in 1860 and is headquartered in New York, New York.",
        fullTimeEmployees=22850,
        city="New York",
        state="NY",
        trailingPE=28.683508,
        dividendYield=0.0101,
        averageVolume=2633287,
        regularMarketOpen=340.27,
        volume=1871593,
        fiftyTwoWeekHigh=484.21,
        fiftyTwoWeekLow=311.87,
        recommendationKey="buy",
        industry="Financial Data & Stock Exchanges"
    )
    db.session.add(SPGI)

    CRM = Stock(
        name="Salesforce, Inc.",
        ticker="CRM",
        marketCap=168888107008,
        dayHigh=182.28,
        dayLow=171.4423,
        currentPrice=171.46,
        longBusinessSummary="Salesforce, Inc. provides customer relationship management technology that brings companies and customers together worldwide. Its Customer 360 platform empowers its customers to work together to deliver connected experiences for their customers. The company's service offerings include Sales to store data, monitor leads and progress, forecast opportunities, gain insights through analytics and relationship intelligence, and deliver quotes, contracts, and invoices; and Service that enables companies to deliver trusted and highly personalized customer service and support at scale. Its service offerings also comprise flexible platform that enables companies of various sizes, locations, and industries to build business apps to bring them closer to their customers with drag-and-drop tools; online learning platform that allows anyone to learn in-demand Salesforce skills; and Slack, a system of engagement. In addition, the company's service offerings include Marketing offering that enables companies to plan, personalize, and optimize one-to-one customer marketing journeys; and Commerce offering, which empowers brands to unify the customer experience across mobile, web, social, and store commerce points. Further, its service offerings comprise Tableau, an end-to-end analytics solution serving various enterprise use cases; and MuleSoft, an integration offering that allows its customers to unlock data across their enterprise. The company provides its service offering for customers in financial services, healthcare and life sciences, manufacturing, and other industries. It also offers professional services; and in-person and online courses to certify its customers and partners on architecting, administering, deploying, and developing its service offerings. The company provides its services through direct sales; and consulting firms, systems integrators, and other partners. Salesforce, Inc. was incorporated in 1999 and is headquartered in San Francisco, California.",
        fullTimeEmployees=73541,
        city="San Francisco",
        state="CA",
        trailingPE=94.31244,
        dividendYield=None,
        averageVolume=8266238,
        regularMarketOpen=180.29,
        volume=6682362,
        fiftyTwoWeekHigh=311.75,
        fiftyTwoWeekLow=154.55,
        recommendationKey="buy",
        industry="Software—Application"
    )
    db.session.add(CRM)

    SBAC = Stock(
        name="SBA Communications Corporation",
        ticker="SBAC",
        marketCap=34267103232,
        dayHigh=326.33,
        dayLow=313.902,
        currentPrice=315.01,
        longBusinessSummary="SBA Communications Corporation is a first choice provider and leading owner and operator of wireless communications infrastructure in North, Central, and South America and South Africa. By Building Better Wireless, SBA generates revenue from two primary businesses  site leasing and site development services. The primary focus of the Company is the leasing of antenna space on its multi-tenant communication sites to a variety of wireless service providers under long-term lease contracts. For more information please visit: www.sbasite.com.",
        fullTimeEmployees=1596,
        city="Boca Raton",
        state="FL",
        trailingPE=120.878746,
        dividendYield=0.008,
        averageVolume=713322,
        regularMarketOpen=325.04,
        volume=532291,
        fiftyTwoWeekHigh=391.15,
        fiftyTwoWeekLow=286.41,
        recommendationKey="buy",
        industry="REIT—Specialty"
    )
    db.session.add(SBAC)

    SLB = Stock(
        name="Schlumberger Limited",
        ticker="SLB",
        marketCap=51855233024,
        dayHigh=37.73,
        dayLow=36.47,
        currentPrice=36.97,
        longBusinessSummary="Schlumberger Limited provides technology for the energy industry worldwide. The company operates through four divisions: Digital & Integration, Reservoir Performance, Well Construction, and Production Systems. It offers software, information management, and IT infrastructure services; consulting services for reservoir characterization, field development planning, and production enhancement; petro technical data services and training solutions; reservoir interpretation and data processing services; asset performance solutions; open and cased-hole services; exploration and production pressure and flow-rate measurement services; pressure pumping, well stimulation, and coiled tubing equipment for downhole mechanical well intervention, reservoir monitoring, and downhole data acquisition; and integrated production systems. The company also provides mud logging and engineering support services; drilling equipment and services for shipyards, drilling contractors, energy companies, and rental tool companies; land drilling rigs and related services; drilling tools; well cementing products and services; and well planning and drilling, engineering, supervision, logistics, procurement, contracting, and drilling rig management services, as well as supplies engineered drilling fluid systems; and designs, manufactures, and markets roller cone and fixed cutter drill bits. In addition, it offers well completion services and equipment; artificial lift production equipment and optimization services; valves; process systems; and integrated subsea production systems comprising wellheads, subsea trees, manifolds and flowline connectors, control systems, connectors, and services, as well as designs and manufactures onshore and offshore platform wellhead systems and processing solutions. The company was formerly known as Socie´te´ de Prospection E´lectrique. Schlumberger Limited was founded in 1926 and is based in Houston, Texas.",
        fullTimeEmployees=92000,
        city="Houston",
        state="TX",
        trailingPE=31.76117,
        dividendYield=0.0172,
        averageVolume=13833446,
        regularMarketOpen=36.805,
        volume=13903255,
        fiftyTwoWeekHigh=49.83,
        fiftyTwoWeekLow=25.9,
        recommendationKey="none",
        industry="Oil & Gas Equipment & Services"
    )
    db.session.add(SLB)

    SEE = Stock(
        name="Sealed Air Corporation",
        ticker="SEE",
        marketCap=8639034368,
        dayHigh=60.1,
        dayLow=58.22,
        currentPrice=58.31,
        longBusinessSummary="Sealed Air Corporation provides food safety and security, and product protection solutions and equipment in North America, South America, Europe, the Middle East, Africa, and the Asia Pacific. It operates through two segments, Food and Protective. The Food segment offers integrated packaging materials and automation equipment solutions to provide food safety and shelf life extension, reduce food waste, automate processes, and optimize total cost for food processors in the fresh red meat, smoked and processed meats, poultry, seafood, plant-based, and dairy markets under the CRYOVAC, CRYOVAC Grip & Tear, CRYOVAC Darfresh, Simple Steps, and Optidure brands. This segment sells its solutions directly to customers through its sales, marketing, and customer service personnel. The Protective segment provides foam, inflatable, suspension and retention, temperature assurance packaging solutions to protect goods to e-commerce, consumer goods, pharmaceutical and medical devices, and industrial manufacturing markets under the SEALED AIR, BUBBLE WRAP, AUTOBAG, SEALED AIR, AUTOBAG, Instapak, Korrvu, Kevothermal, and TempGuard brands. This segment sells its solutions through supply distributors, as well as directly to fabricators, original equipment manufacturers, contract manufacturers, logistics partners, and e-commerce/fulfillment operations. Sealed Air Corporation was incorporated in 1960 and is headquartered in Charlotte, North Carolina.",
        fullTimeEmployees=16500,
        city="Charlotte",
        state="NC",
        trailingPE=19.19987,
        dividendYield=0.0128,
        averageVolume=846151,
        regularMarketOpen=59.69,
        volume=744512,
        fiftyTwoWeekHigh=70.72,
        fiftyTwoWeekLow=53.87,
        recommendationKey="buy",
        industry="Packaging & Containers"
    )
    db.session.add(SEE)

    SRE = Stock(
        name="Sempra",
        ticker="SRE",
        marketCap=48286949376,
        dayHigh=153.72,
        dayLow=150.95,
        currentPrice=151.21,
        longBusinessSummary="Sempra operates as an energy-services holding company in the United States and internationally. The company's San Diego Gas & Electric Company segment provides electric services; and supplies natural gas. It offers electric services to approximately 3.6 million population and natural gas services to approximately 3.3 million population that covers 4,100 square miles. Its Southern California Gas Company segment owns and operates a natural gas distribution, transmission, and storage system that supplies natural gas to a population of approximately 22 million covering an area of 24,000 square miles. The company's Sempra Texas Utilities segment engages in the regulated transmission and distribution of electricity serving 3.8 million homes and businesses, and operation of 140,000 miles of transmission and distribution lines. Its transmission system includes 18,249 circuit miles of transmission lines, a total of 1,174 transmission and distribution substations, and interconnection to 130 third-party generation facilities totaling 45,403 megawatts. The company was formerly known as Sempra Energy and changed its name to Sempra in July 2021. Sempra was founded in 1998 and is headquartered in San Diego, California.",
        fullTimeEmployees=15390,
        city="San Diego",
        state="CA",
        trailingPE=43.376366,
        dividendYield=0.028399998,
        averageVolume=1603279,
        regularMarketOpen=151.76,
        volume=1282023,
        fiftyTwoWeekHigh=173.28,
        fiftyTwoWeekLow=119.56,
        recommendationKey="buy",
        industry="Utilities—Diversified"
    )
    db.session.add(SRE)

    NOW = Stock(
        name="ServiceNow, Inc.",
        ticker="NOW",
        marketCap=94214561792,
        dayHigh=500.26,
        dayLow=471.03,
        currentPrice=473.44,
        longBusinessSummary="ServiceNow, Inc. provides enterprise cloud computing solutions that defines, structures, consolidates, manages, and automates services for enterprises worldwide. It operates the Now platform for workflow automation, artificial intelligence, machine learning, robotic process automation, performance analytics, electronic service catalogs and portals, configuration management systems, data benchmarking, encryption, and collaboration and development tools. The company also provides information technology (IT) service management applications; IT service management product suite for enterprise's employees, customers, and partners; IT business management product suite; IT operations management product that connects a customer's physical and cloud-based IT infrastructure; IT Asset Management to automate IT asset lifecycles; and security operations that connects with internal and third party. In addition, it offers governance, risk, and compliance product to manage risk and resilience; human resources, legal, and workplace service delivery products; safe workplace applications; customer service management product; and field service management applications. Further, it provides App Engine product; IntegrationHub enables application to extend workflows; and professional, industry solutions, and customer support services. It serves government, financial services, healthcare, telecommunications, manufacturing, IT services, technology, oil and gas, education, and consumer products through direct sales team and resale partners. It has a strategic partnership with Celonis to help customers identify and prioritize processes that are suitable for automation. The company was formerly known as Service-now.com and changed its name to ServiceNow, Inc. in May 2012. The company was founded in 2004 and is headquartered in Santa Clara, California.",
        fullTimeEmployees=16881,
        city="Santa Clara",
        state="CA",
        trailingPE=433.95053,
        dividendYield=None,
        averageVolume=1725385,
        regularMarketOpen=496.7,
        volume=1254946,
        fiftyTwoWeekHigh=707.6,
        fiftyTwoWeekLow=406.47,
        recommendationKey="buy",
        industry="Software—Application"
    )
    db.session.add(NOW)

    SHW = Stock(
        name="The Sherwin-Williams Company",
        ticker="SHW",
        marketCap=58550988800,
        dayHigh=231.37,
        dayLow=222.84,
        currentPrice=223.31,
        longBusinessSummary="The Sherwin-Williams Company develops, manufactures, distributes, and sells paints, coatings, and related products to professional, industrial, commercial, and retail customers. It operates through three segments: The Americas Group, Consumer Brands Group, and Performance Coatings Group. The Americas Group segment offers architectural paints and coatings, and protective and marine products, as well as OEM product finishes and related products for architectural and industrial paint contractors, and do-it-yourself homeowners. The Consumer Brands Group segment supplies a portfolio of branded and private-label architectural paints, stains, varnishes, industrial products, wood finishes products, wood preservatives, applicators, corrosion inhibitors, aerosols, caulks, and adhesives to retailers and distributors. The Performance Coatings Group segment develops and sells industrial coatings for wood finishing and general industrial applications, automotive refinish products, protective and marine coatings, coil coatings, packaging coatings, and performance-based resins and colorants. It serves retailers, dealers, jobbers, licensees, and other third-party distributors through its branches and direct sales staff, as well as through outside sales representatives. The company has operations primarily in the North and South America, the Caribbean, Europe, Asia, and Australia. As of February 17, 2022, it operated approximately 5,000 company-operated stores and facilities. The Sherwin-Williams Company was founded in 1866 and is headquartered in Cleveland, Ohio.",
        fullTimeEmployees=61000,
        city="Cleveland",
        state="OH",
        trailingPE=30.594603,
        dividendYield=0.0088,
        averageVolume=1829885,
        regularMarketOpen=229.09,
        volume=1143280,
        fiftyTwoWeekHigh=354.15,
        fiftyTwoWeekLow=214.22,
        recommendationKey="buy",
        industry="Specialty Chemicals"
    )
    db.session.add(SHW)

    SBNY = Stock(
        name="Signature Bank",
        ticker="SBNY",
        marketCap=11371607040,
        dayHigh=195.46,
        dayLow=187.34,
        currentPrice=187.55,
        longBusinessSummary="Signature Bank provides commercial banking products and services. It accepts various deposit products, including checking accounts, money market accounts, escrow deposit accounts, cash concentration accounts, certificates of deposit, and other cash management products. The company provides various lending products comprising commercial and industrial loans, real estate loans, and letters of credit. In addition, it offers asset management and investment products; and retirement products, such as individual retirement accounts and administrative services for retirement vehicles. Further, the company provides wealth management services to its high net worth personal clients; and purchases, sells, and assembles small business administration loans and pools. Additionally, it offers individual and group insurance products, including health, life, disability, and long-term care insurance products for business and private clients. As of December 31, 2021, the company operated 37 private client offices located in the metropolitan New York area, Connecticut, California, and North Carolina. Signature Bank was incorporated in 2000 and is headquartered in New York, New York.",
        fullTimeEmployees=1854,
        city="New York",
        state="NY",
        trailingPE=13.44059,
        dividendYield=0.0117999995,
        averageVolume=1078050,
        regularMarketOpen=191.31,
        volume=680597,
        fiftyTwoWeekHigh=374.76,
        fiftyTwoWeekLow=165.36,
        recommendationKey="buy",
        industry="Banks—Regional"
    )
    db.session.add(SBNY)

    SPG = Stock(
        name="Simon Property Group, Inc.",
        ticker="SPG",
        marketCap=32615436288,
        dayHigh=102.48,
        dayLow=99.14,
        currentPrice=99.25,
        longBusinessSummary="Simon is a real estate investment trust engaged in the ownership of premier shopping, dining, entertainment and mixed-use destinations and an S&P 100 company (Simon Property Group, NYSE: SPG). Our properties across North America, Europe and Asia provide community gathering places for millions of people every day and generate billions in annual sales.",
        fullTimeEmployees=2400,
        city="Indianapolis",
        state="IN",
        trailingPE=16.06767,
        dividendYield=0.0582,
        averageVolume=2231296,
        regularMarketOpen=101.43,
        volume=1498200,
        fiftyTwoWeekHigh=171.12,
        fiftyTwoWeekLow=93.5,
        recommendationKey="buy",
        industry="REIT—Retail"
    )
    db.session.add(SPG)

    SWKS = Stock(
        name="Skyworks Solutions, Inc.",
        ticker="SWKS",
        marketCap=15913538560,
        dayHigh=100.545,
        dayLow=96.05,
        currentPrice=96.22,
        longBusinessSummary="Skyworks Solutions, Inc., together with its subsidiaries, designs, develops, manufactures, and markets proprietary semiconductor products, including intellectual property in the United States, China, South Korea, Taiwan, Europe, the Middle East, Africa, and rest of Asia-Pacific. Its product portfolio includes amplifiers, antenna tuners, attenuators, automotive tuners and digital radios, circulators/isolators, DC/DC converters, demodulators, detectors, diodes, wireless analog system on chip products, directional couplers, diversity receive modules, filters, front-end modules, hybrids, light emitting diode drivers, low noise amplifiers, mixers, modulators, optocouplers/optoisolators, phase locked loops, phase shifters, power dividers/combiners, receivers, switches, synthesizers, timing devices, technical ceramics, voltage controlled oscillators/synthesizers, and voltage regulators. The company provides its products for use in the aerospace, automotive, broadband, cellular infrastructure, connected home, entertainment and gaming, industrial, medical, military, smartphone, tablet, and wearable markets. It sells its products through direct sales force, electronic component distributors, and independent sales representatives. The company was incorporated in 1962 and is headquartered in Irvine, California.",
        fullTimeEmployees=11000,
        city="Irvine",
        state="CA",
        trailingPE=10.726867,
        dividendYield=0.0216,
        averageVolume=2240698,
        regularMarketOpen=98.68,
        volume=2135023,
        fiftyTwoWeekHigh=197.62,
        fiftyTwoWeekLow=88.76,
        recommendationKey="buy",
        industry="Semiconductors"
    )
    db.session.add(SWKS)

    SJM = Stock(
        name="The J. M. Smucker Company",
        ticker="SJM",
        marketCap=13784857600,
        dayHigh=129.64,
        dayLow=126.995,
        currentPrice=127.21,
        longBusinessSummary="The J. M. Smucker Company manufactures and markets branded food and beverage products worldwide. It operates in four segments: U.S. Retail Coffee, U.S. Retail Consumer Foods, U.S. Retail Pet Foods, and International and Away From Home. The company offers mainstream roast, ground, single serve, and premium coffee; peanut butter and specialty spreads; fruit spreads, shortening and oils, and frozen sandwiches; pet food and pet snacks; and foodservice hot beverage, foodservice portion control, and flour products, as well as dog and cat food, frozen handheld products, juices and beverages, and baking ingredient. It provides its products under the Folgers, Café Bustelo, Dunkin' Donuts, 1850, Jif, Smucker's, Crisco, Smucker's Uncrustables, Meow Mix, Kibbles n Bits, 9Lives, Nature's Recipe, Milk-Bone, Pup-Peroni, Rachael Ray Nutrish, Natural Balance, Robin Hood, and Five Roses brands. The company sells its products through direct sales and brokers to food retailers and wholesalers, club stores, pet specialty stores, discount and dollar stores, drug stores, military commissaries, mass merchandisers, natural foods stores and distributors, and online retailers; and through retail channels, and foodservice distributors and operators. The J. M. Smucker Company was founded in 1897 and is headquartered in Orrville, Ohio.",
        fullTimeEmployees=7100,
        city="Orrville",
        state="OH",
        trailingPE=18.152113,
        dividendYield=0.0275,
        averageVolume=946624,
        regularMarketOpen=129.01,
        volume=771882,
        fiftyTwoWeekHigh=146.74,
        fiftyTwoWeekLow=118.55,
        recommendationKey="hold",
        industry="Packaged Foods"
    )
    db.session.add(SJM)

    SNA = Stock(
        name="Snap-on Incorporated",
        ticker="SNA",
        marketCap=10766424064,
        dayHigh=206.58,
        dayLow=201,
        currentPrice=201.11,
        longBusinessSummary="Snap-on Incorporated manufactures and markets tools, equipment, diagnostics, and repair information and systems solutions for professional users worldwide. It operates through Commercial & Industrial Group, Snap-on Tools Group, Repair Systems & Information Group, and Financial Services segments. The company offers hand tools, including wrenches, sockets, ratchet wrenches, pliers, screwdrivers, punches and chisels, saws and cutting tools, pruning tools, torque measuring instruments, and other products; power tools, such as cordless, pneumatic, hydraulic, and corded tools; and tool storage products comprising tool chests, roll cabinets, and other products. It also provides handheld and computer-based diagnostic products, service and repair information products, diagnostic software solutions, electronic parts catalogs, business management systems and services, point-of-sale systems, integrated systems for vehicle service shops, original equipment manufacturer purchasing facilitation services, and warranty management systems and analytics. In addition, the company offers solutions for the service of vehicles and industrial equipment that include wheel alignment equipment, wheel balancers, tire changers, vehicle lifts, test lane equipment, collision repair equipment, vehicle air conditioning service equipment, brake service equipment, fluid exchange equipment, transmission troubleshooting equipment, safety testing equipment, battery chargers, and hoists, as well as after-sales support services and training programs. Further, it provides financing programs to facilitate the sales of its products and support its franchise business. The company serves the aviation and aerospace, agriculture, construction, government and military, mining, natural resources, power generation, and technical education industries, as well as vehicle dealerships and repair centers. Snap-on Incorporated was founded in 1920 and is based in Kenosha, Wisconsin.",
        fullTimeEmployees=12800,
        city="Kenosha",
        state="WI",
        trailingPE=13.724834,
        dividendYield=0.026199998,
        averageVolume=372335,
        regularMarketOpen=205.96,
        volume=291145,
        fiftyTwoWeekHigh=235.36,
        fiftyTwoWeekLow=190.08,
        recommendationKey="hold",
        industry="Tools & Accessories"
    )
    db.session.add(SNA)

    SO = Stock(
        name="The Southern Company",
        ticker="SO",
        marketCap=74843078656,
        dayHigh=71.43,
        dayLow=70.5562,
        currentPrice=70.62,
        longBusinessSummary="The Southern Company, through its subsidiaries, engages in the generation, transmission, and distribution of electricity. It operates through Gas Distribution Operations, Gas Pipeline Investments, Wholesale Gas Services, and Gas Marketing Services segments. The company also develops, constructs, acquires, owns, and manages power generation assets, including renewable energy projects and sells electricity in the wholesale market; and distributes natural gas in Illinois, Georgia, Virginia, and Tennessee, as well as provides gas marketing services, wholesale gas services, and gas pipeline investments operations. In addition, it owns and/or operates 30 hydroelectric generating stations, 24 fossil fuel generating stations, three nuclear generating stations, 13 combined cycle/cogeneration stations, 45 solar facilities, 15 wind facilities, one fuel cell facility, and four battery storage facility; and constructs, operates, and maintains 76,289 miles of natural gas pipelines and 14 storage facilities with total capacity of 157 Bcf to provide natural gas to residential, commercial, and industrial customers. The company serves approximately 8.7 million electric and gas utility customers. Further, the company offers digital wireless communications and fiber optics services. The Southern Company was incorporated in 1945 and is headquartered in Atlanta, Georgia.",
        fullTimeEmployees=27027,
        city="Atlanta",
        state="GA",
        trailingPE=25.212423,
        dividendYield=0.0369,
        averageVolume=5412285,
        regularMarketOpen=70.71,
        volume=3728458,
        fiftyTwoWeekHigh=77.24,
        fiftyTwoWeekLow=60.12,
        recommendationKey="hold",
        industry="Utilities—Regulated Electric"
    )
    db.session.add(SO)

    SWK = Stock(
        name="Stanley Black & Decker, Inc.",
        ticker="SWK",
        marketCap=17521156096,
        dayHigh=111.6,
        dayLow=107.38,
        currentPrice=107.47,
        longBusinessSummary="Stanley Black & Decker, Inc. engages in the tools and storage and industrial businesses in the United States, Canada, rest of Americas, France, rest of Europe, and Asia. Its Tools & Storage segment offers professional products, including professional grade corded and cordless electric power tools and equipment, and pneumatic tools and fasteners; and consumer products, such as corded and cordless electric power tools primarily under the BLACK+DECKER brand, as well as corded and cordless lawn and garden products and related accessories; home products; and hand tools, power tool accessories, and storage products. This segment sells its products through retailers, distributors, dealers, and a direct sales force to professional end users, distributors, dealers, retail consumers, and industrial customers in various industries. The company's Industrial segment provides engineered fastening systems and products to customers in the automotive, manufacturing, electronics, construction, aerospace, and other industries; sells and rents custom pipe handling, joint welding, and coating equipment for use in the construction of large and small diameter pipelines, as well as provides pipeline inspection services; and sells hydraulic tools and performance-driven heavy equipment attachment tools. This segment serves oil and natural gas pipeline industry and other industrial customers. It also sells automatic doors to commercial customers. The company was formerly known as The Stanley Works and changed its name to Stanley Black & Decker, Inc. in March 2010. Stanley Black & Decker, Inc. was founded in 1843 and is headquartered in New Britain, Connecticut.",
        fullTimeEmployees=71300,
        city="New Britain",
        state="CT",
        trailingPE=9.726672,
        dividendYield=0.025999999,
        averageVolume=2095375,
        regularMarketOpen=109.79,
        volume=1186267,
        fiftyTwoWeekHigh=210.92,
        fiftyTwoWeekLow=99.43,
        recommendationKey="buy",
        industry="Tools & Accessories"
    )
    db.session.add(SWK)

    STT = Stock(
        name="State Street Corporation",
        ticker="STT",
        marketCap=23579412480,
        dayHigh=66.49,
        dayLow=64.384,
        currentPrice=64.49,
        longBusinessSummary="State Street Corporation, through its subsidiaries, provides a range of financial products and services to institutional investors worldwide. The company offers investment servicing products and services, including custody; product accounting; daily pricing and administration; master trust and master custody; depotbank services; record-keeping; cash management; foreign exchange, brokerage and other trading services; securities finance and enhanced custody products; deposit and short-term investment facilities; loans and lease financing; investment manager and alternative investment manager operations outsourcing; performance, risk, and compliance analytics; and financial data management to support institutional investors. It also engages in the provision of portfolio management and risk analytics, as well as trading and post-trade settlement services with integrated compliance and managed data. In addition, the company offers investment management strategies and products, such as core and enhanced indexing, multi-asset strategies, active quantitative and fundamental active capabilities, and alternative investment strategies. Further, it provides services and solutions, including environmental, social, and governance investing; defined benefit and defined contribution; and global fiduciary solutions, as well as exchange-traded fund under the SPDR ETF brand. The company provides its products and services to mutual funds, collective investment funds and other investment pools, corporate and public retirement plans, insurance companies, foundations, endowments, and investment managers. State Street Corporation was founded in 1792 and is headquartered in Boston, Massachusetts.",
        fullTimeEmployees=39335,
        city="Boston",
        state="MA",
        trailingPE=9.501988,
        dividendYield=0.032899998,
        averageVolume=2930375,
        regularMarketOpen=65.09,
        volume=1891400,
        fiftyTwoWeekHigh=104.87,
        fiftyTwoWeekLow=61.29,
        recommendationKey="buy",
        industry="Asset Management"
    )
    db.session.add(STT)

    SYK = Stock(
        name="Stryker Corporation",
        ticker="SYK",
        marketCap=74618077184,
        dayHigh=205.34,
        dayLow=197.65,
        currentPrice=197.8,
        longBusinessSummary="Stryker Corporation operates as a medical technology company. The company operates through two segments, MedSurg and Neurotechnology, and Orthopaedics and Spine. The Orthopaedics and Spine segment provides implants for use in hip and knee joint replacements, and trauma and extremities surgeries. This segment also offers spinal implant products comprising cervical, thoracolumbar, and interbody systems that are used in spinal injury, deformity, and degenerative therapies. The MedSurg and Neurotechnology segment offers surgical equipment and surgical navigation systems, endoscopic and communications systems, patient handling, emergency medical equipment and intensive care disposable products, reprocessed and remanufactured medical devices, and other medical device products that are used in various medical specialties. This segment also provides neurotechnology products, which include products used for minimally invasive endovascular techniques; products for brain and open skull based surgical procedures; orthobiologic and biosurgery products, such as synthetic bone grafts and vertebral augmentation products; minimally invasive products for the treatment of acute ischemic and hemorrhagic stroke; and craniomaxillofacial implant products, including cranial, maxillofacial, and chest wall devices, as well as dural substitutes and sealants. The company sells its products to doctors, hospitals, and other healthcare facilities through company-owned subsidiaries and branches, as well as third-party dealers and distributors in approximately 75 countries. Stryker Corporation was founded in 1941 and is headquartered in Kalamazoo, Michigan.",
        fullTimeEmployees=46000,
        city="Kalamazoo",
        state="MI",
        trailingPE=39.814816,
        dividendYield=0.0119,
        averageVolume=1438324,
        regularMarketOpen=204.32,
        volume=1284163,
        fiftyTwoWeekHigh=281.16,
        fiftyTwoWeekLow=193.34,
        recommendationKey="buy",
        industry="Medical Devices"
    )
    db.session.add(SYK)

    SIVB = Stock(
        name="SVB Financial Group",
        ticker="SIVB",
        marketCap=23747856384,
        dayHigh=425,
        dayLow=404.41,
        currentPrice=404.65,
        longBusinessSummary="SVB Financial Group, a diversified financial services company, offers various banking and financial products and services. It operates through four segments: Global Commercial Bank, SVB Private Bank, SVB Capital, and SVB Securities. The Global Commercial Bank segment provides commercial banking products and services, including credit, treasury management, foreign exchange, trade finance, and other financial products and services. This segment also offers traditional term and equipment loans, asset-based loans, revolving lines of credit, warehouse facilities, recurring revenue and acquisition finance facilities, mezzanine lending, corporate working capital facilities, and credit card programs; treasury management products and services; business and analysis checking, money market, multi-currency, in-country bank, and sweep accounts; receivables services, which include merchant services, remote capture, lockbox, and fraud control services; wire transfer and automated clearing house payment services; business bill pay, credit and debit cards, account analysis, and disbursement services. In addition, it offers foreign exchange and trade finance products and services; letters of credit; and investment services and solutions. The SVB Private Bank segment offers mortgages, home equity lines of credit, restricted and private stock loans, capital call lines of credit, and other secured and unsecured lending products; planning-based financial strategies, wealth management, family office, financial planning, tax planning, and trust services; and real estate secured loans. The SVB Capital segment provides venture capital investment services. The SVB Securities segment provides investment banking services; products and services, including capital raising, merger and acquisition advisory, equity research, and sales and trading. It operates through 56 offices in the United States and internationally. The company was founded in 1983 and is headquartered in Santa Clara, California.",
        fullTimeEmployees=7149,
        city="Santa Clara",
        state="CA",
        trailingPE=12.41448,
        dividendYield=None,
        averageVolume=616470,
        regularMarketOpen=416.16,
        volume=314547,
        fiftyTwoWeekHigh=763.22,
        fiftyTwoWeekLow=384.83,
        recommendationKey="buy",
        industry="Banks—Regional"
    )
    db.session.add(SIVB)

    SYF = Stock(
        name="Synchrony Financial",
        ticker="SYF",
        marketCap=15848620032,
        dayHigh=30.4925,
        dayLow=28.835,
        currentPrice=28.96,
        longBusinessSummary="Synchrony Financial, together with its subsidiaries, operates as a consumer financial services company in the United States. It provides credit products, such as credit cards, commercial credit products, and consumer installment loans. The company also offers private label credit cards, dual cards, co-brand and general purpose credit cards, short- and long-term installment loans, and consumer banking products; and deposit products, including certificates of deposit, individual retirement accounts, money market accounts, and savings accounts to retail and commercial customers, as well as accepts deposits through third-party securities brokerage firms. In addition, it provides debt cancellation products to its credit card customers through online, mobile, and direct mail; healthcare payments and financing solutions under the CareCredit, Pets Best, and Walgreens brands; payments and financing solutions in the apparel, specialty retail, outdoor, music, and luxury industries; and point-of-sale consumer financing for audiology products and dental services. The company offers its credit products through programs established with a group of national and regional retailers, local merchants, manufacturers, buying groups, industry associations, and healthcare service providers; and deposit products through various channels, such as digital and print. It serves digital, health and wellness, retail, home, auto, powersports, jewelry, pets, and other industries. Synchrony Financial was founded in 1932 and is headquartered in Stamford, Connecticut.",
        fullTimeEmployees=18000,
        city="Stamford",
        state="CT",
        trailingPE=4.0967603,
        dividendYield=0.026199998,
        averageVolume=6869422,
        regularMarketOpen=29.69,
        volume=4415813,
        fiftyTwoWeekHigh=52.49,
        fiftyTwoWeekLow=27.4,
        recommendationKey="buy",
        industry="Credit Services"
    )
    db.session.add(SYF)

    SNPS = Stock(
        name="Synopsys, Inc.",
        ticker="SNPS",
        marketCap=46594519040,
        dayHigh=314.13,
        dayLow=302.24,
        currentPrice=303.67,
        longBusinessSummary="Synopsys, Inc. provides electronic design automation software products used to design and test integrated circuits. The company offers Fusion Design Platform that provides digital design implementation solutions; Verification Continuum Platform that provides virtual prototyping, static and formal verification, simulation, emulation, field programmable gate array (FPGA)-based prototyping, and debug solutions; and FPGA design products that are programmed to perform specific functions. It also provides intellectual property (IP) solutions for USB, PCI Express, DDR, Ethernet, SATA, MIPI, HDMI, and Bluetooth low energy applications; analog IP, including data converters and audio codecs; and system-on-chip (SoC) infrastructure IP, datapath and building block IP, and verification IP products, as well as mathematical and floating-point components, and Arm AMBA interconnect fabric and peripherals. In addition, the company offers logic libraries and embedded memories; configurable processor cores and application-specific instruction-set processor tools for embedded applications; IP subsystems for audio, sensor, and data fusion functionality; and security IP solutions. Further, it provides Platform Architect solutions for SoC architecture analysis and optimization; virtual prototyping solutions; and HAPS FPGA-based prototyping systems, as well as a series of tools used in the design of optical systems and photonic devices. Additionally, the company offers security testing, managed services, programs and professional services, and training that enable its customers to detect and remediate security vulnerabilities, and defects in the software development lifecycle, as well as manufacturing solutions. It serves electronics, financial services, automotive, medicine, energy, and industrial areas. The company was incorporated in 1986 and is headquartered in Mountain View, California.",
        fullTimeEmployees=16361,
        city="Mountain View",
        state="CA",
        trailingPE=63.13306,
        dividendYield=None,
        averageVolume=999109,
        regularMarketOpen=312.02,
        volume=726257,
        fiftyTwoWeekHigh=377.6,
        fiftyTwoWeekLow=255.02,
        recommendationKey="buy",
        industry="Software—Infrastructure"
    )
    db.session.add(SNPS)

    SYY = Stock(
        name="Sysco Corporation",
        ticker="SYY",
        marketCap=43601395712,
        dayHigh=87.32,
        dayLow=84.79,
        currentPrice=85.05,
        longBusinessSummary="Sysco Corporation, through its subsidiaries, engages in the marketing and distribution of various food and related products primarily to the foodservice or food-away-from-home industry in the United States, Canada, the United Kingdom, France, and internationally. It operates through U.S. Foodservice Operations, International Foodservice Operations, SYGMA, and Other segments. The company distributes frozen foods, such as meats, seafood, fully prepared entrées, fruits, vegetables, and desserts; canned and dry foods; fresh meats and seafood; dairy products; beverage products; imported specialties; and fresh produce. It also supplies various non-food items, including paper products comprising disposable napkins, plates, and cups; tableware consisting of China and silverware; cookware, which include pots, pans, and utensils; restaurant and kitchen equipment and supplies; and cleaning supplies. The company serves restaurants, hospitals and nursing homes, schools and colleges, hotels and motels, industrial caterers, and other foodservice venues. As of August 27, 2021, it operated 343 distribution facilities. Sysco Corporation was incorporated in 1969 and is headquartered in Houston, Texas.",
        fullTimeEmployees=58000,
        city="Houston",
        state="TX",
        trailingPE=63.851353,
        dividendYield=0.0231,
        averageVolume=2382769,
        regularMarketOpen=86.47,
        volume=1906158,
        fiftyTwoWeekHigh=91.53,
        fiftyTwoWeekLow=68.05,
        recommendationKey="buy",
        industry="Food Distribution"
    )
    db.session.add(SYY)

    TMUS = Stock(
        name="T-Mobile US, Inc.",
        ticker="TMUS",
        marketCap=166161121280,
        dayHigh=138.44,
        dayLow=132.79,
        currentPrice=133.03,
        longBusinessSummary="T-Mobile US, Inc., together with its subsidiaries, provides mobile communications services in the United States, Puerto Rico, and the United States Virgin Islands. The company offers voice, messaging, and data services to 108.7 million customers in the postpaid, prepaid, and wholesale markets. It also provides wireless devices, including smartphones, wearables, and tablets and other mobile communication devices, as well as wireless devices and accessories. In addition, the company offers services, devices, and accessories under the T-Mobile and Metro by T-Mobile brands through its owned and operated retail stores, T-Mobile app and customer care channels, and its websites. It also sells its devices to dealers and other third-party distributors for resale through independent third-party retail outlets and various third-party websites. As of December 31, 2021, it operated approximately 102,000 macro cell and 41,000 small cell/distributed antenna system sites. The company was founded in 1994 and is headquartered in Bellevue, Washington.",
        fullTimeEmployees=75000,
        city="Bellevue",
        state="WA",
        trailingPE=50.011276,
        dividendYield=None,
        averageVolume=4813903,
        regularMarketOpen=137.09,
        volume=4261082,
        fiftyTwoWeekHigh=150.2,
        fiftyTwoWeekLow=101.51,
        recommendationKey="buy",
        industry="Telecom Services"
    )
    db.session.add(TMUS)

    TROW = Stock(
        name="T. Rowe Price Group, Inc.",
        ticker="TROW",
        marketCap=27015569408,
        dayHigh=122.6975,
        dayLow=117.29,
        currentPrice=117.87,
        longBusinessSummary="T. Rowe Price Group, Inc. is a publicly owned investment manager. The firm provides its services to individuals, institutional investors, retirement plans, financial intermediaries, and institutions. It launches and manages equity and fixed income mutual funds. The firm invests in the public equity and fixed income markets across the globe. It employs fundamental and quantitative analysis with a bottom-up approach. The firm utilizes in-house and external research to make its investments. It employs socially responsible investing with a focus on environmental, social, and governance issues. It makes investment in late-stage venture capital transactions and usually invests between $3 million and $5 million. The firm was previously known as T. Rowe Group, Inc. and T. Rowe Price Associates, Inc. T. Rowe Price Group, Inc. was founded in 1937 and is based in Baltimore, Maryland, with additional offices in Colorado Springs, Colorado; Owings Mills, Maryland; San Francisco, California; New York, New York; Philadelphia, Pennsylvania; Tampa, Florida; Toronto, Ontario; Hellerup, Denmark; Amsterdam, The Netherlands; Luxembourg, Grand Duchy of Luxembourg; Zurich, Switzerland; Dubai, United Arab Emirates; London, United Kingdom; Sydney, New South Wales; Hong Kong; Tokyo, Japan; Singapore; Frankfurt, Germany, Madrid, Spain, Milan, Italy, Stockholm, Sweden, Melbourne, Australia, and Amsterdam, Netherlands.",
        fullTimeEmployees=7529,
        city="Baltimore",
        state="MD",
        trailingPE=8.8824415,
        dividendYield=0.0394,
        averageVolume=1756546,
        regularMarketOpen=121.29,
        volume=1774782,
        fiftyTwoWeekHigh=224.56,
        fiftyTwoWeekLow=104.72,
        recommendationKey="hold",
        industry="Asset Management"
    )
    db.session.add(TROW)

    TTWO = Stock(
        name="Take-Two Interactive Software, Inc.",
        ticker="TTWO",
        marketCap=14548553728,
        dayHigh=131.375,
        dayLow=126.05,
        currentPrice=126.18,
        longBusinessSummary="Take-Two Interactive Software, Inc. develops, publishes, and markets interactive entertainment solutions for consumers worldwide. The company offers its products under the Rockstar Games, 2K, Private Division, Social Point, and Playdots labels. It develops and publishes action/adventure products under the Grand Theft Auto, Max Payne, Midnight Club, and Red Dead Redemption names; and offers episodes and content. The company also develops brands in other genres, including the LA Noire, Bully, and Manhunt franchises. In addition, the company publishes various entertainment properties across various platforms and a range of genres, such as shooter, action, role-playing, strategy, sports, and family/casual entertainment under the BioShock, Mafia, Sid Meier's Civilization, XCOM series, and Borderlands. Further, it publishes sports simulation titles comprising NBA 2K series, a basketball video game; the WWE 2K professional wrestling series; and PGA TOUR 2K. It also offers Kerbal Space Program, and The Outer Worlds and Ancestors: the Humankind Odyssey under Private Division. Additionally, the company offers free-to-play mobile games, such as Dragon City and Monster Legends, as well as Two Dots mobile game. Its products are designed for console gaming systems, including PlayStation 4; Xbox One; the Nintendo Switch; and personal computers comprising smartphones and tablets. The company provides its products through physical retail, digital download, online platforms, and cloud streaming services. Take-Two Interactive Software, Inc. was incorporated in 1993 and is based in New York, New York.",
        fullTimeEmployees=6495,
        city="New York",
        state="NY",
        trailingPE=26.091812,
        dividendYield=None,
        averageVolume=2955354,
        regularMarketOpen=129.99,
        volume=1705723,
        fiftyTwoWeekHigh=195.83,
        fiftyTwoWeekLow=101.85,
        recommendationKey="buy",
        industry="Electronic Gaming & Multimedia"
    )
    db.session.add(TTWO)

    TPR = Stock(
        name="Tapestry, Inc.",
        ticker="TPR",
        marketCap=8865107968,
        dayHigh=33.72,
        dayLow=32.155,
        currentPrice=32.22,
        longBusinessSummary="Tapestry, Inc. provides luxury accessories and branded lifestyle products in the United States, Japan, Greater China, and internationally. The company operates through three segments: Coach, Kate Spade, and Stuart Weitzman. The company offers women's accessories, including handbags, such as wallets, money pieces, wristlets, and cosmetic cases; novelty accessories comprising address books, time management and travel accessories, sketchbooks, and portfolios; and key rings and charms. It also provides bag collections, including business cases, computer bags, messenger-style bags, backpacks, and totes; small leather goods, such as wallets, card cases, travel organizers, and belts; and footwear, watches, sunglasses, novelty accessories, and ready-to-wear for men. In addition, the company offers women's footwear; sunglasses; bracelets, necklaces, rings, and earrings; fragrances and watches; women's seasonal lifestyle apparel collections that include outerwear and ready-to-wear, and cold weather accessories, which comprise gloves, scarves, and hats. Further, it provides footwear items; and housewares and home accessories for kids, such as fashion bedding and tableware; and stationery and gifts. Additionally, the company licenses rights to market and distribute its jewelry, eyewear, watches, fragrances, and tech accessories under the Coach brand; and fashion beddings, tableware and housewares, eyewear, watches, stationery and gifts, and tech accessories under the Kate Spade brand. As of July 3, 2021, it operated through a network of 939 Coach stores, 407 Kate Spade stores, and 104 Stuart Weitzman stores. The company sells its products through e-commerce sites and concession shop-in-shops, and wholesale customers, as well as through independent third-party distributors. The company was formerly known as Coach, Inc. and changed its name to Tapestry, Inc. in October 2017. Tapestry, Inc. was founded in 1941 and is based in New York, New York.",
        fullTimeEmployees=12100,
        city="New York",
        state="NY",
        trailingPE=11.026694,
        dividendYield=0.024500001,
        averageVolume=4298970,
        regularMarketOpen=33.21,
        volume=2985738,
        fiftyTwoWeekHigh=47.05,
        fiftyTwoWeekLow=26.39,
        recommendationKey="buy",
        industry="Luxury Goods"
    )
    db.session.add(TPR)

    TGT = Stock(
        name="Target Corporation",
        ticker="TGT",
        marketCap=69243002880,
        dayHigh=151.305,
        dayLow=144.33,
        currentPrice=144.52,
        longBusinessSummary="Target Corporation operates as a general merchandise retailer in the United States. The company offers food assortments, including perishables, dry grocery, dairy, and frozen items; apparel, accessories, home décor products, electronics, toys, seasonal offerings, food, and other merchandise; and beauty and household essentials. It also provides in-store amenities, such as Target Café, Target Optical, Starbucks, and other food service offerings. The company sells its products through its stores; and digital channels, including Target.com. As of March 09, 2022, the company operated approximately 2,000 stores. Target Corporation was incorporated in 1902 and is headquartered in Minneapolis, Minnesota.",
        fullTimeEmployees=450000,
        city="Minneapolis",
        state="MN",
        trailingPE=10.636639,
        dividendYield=0.0164,
        averageVolume=6361551,
        regularMarketOpen=150.44,
        volume=4122595,
        fiftyTwoWeekHigh=268.98,
        fiftyTwoWeekLow=138.58,
        recommendationKey="buy",
        industry="Discount Stores"
    )
    db.session.add(TGT)

    TDY = Stock(
        name="Teledyne Technologies Incorporated",
        ticker="TDY",
        marketCap=17356201984,
        dayHigh=385.54,
        dayLow=371.481,
        currentPrice=372.01,
        longBusinessSummary="Teledyne Technologies Incorporated provides enabling technologies for industrial growth markets in the United States, Canada, the United Kingdom, Belgium, the Netherlands, and internationally. The company's Instrumentation segment offers monitoring and control instruments for marine, environmental, industrial, and other applications, as well as electronic test and measurement equipment; and power and communications connectivity devices for distributed instrumentation systems and sensor networks. Its Digital Imaging segment provides visible spectrum sensors and digital cameras for industrial machine vision and automated quality control, as well as for medical, research, and scientific applications; and infrared and X-ray spectra for use in industrial, government, and medical applications, as well as micro electromechanical systems and semiconductors, including analog-to-digital and digital-to-analog converters. This segment also offers thermal imaging systems, visible-light imaging systems, locater systems, measurement and diagnostic systems, and threat-detection solutions. The company's Aerospace and Defense Electronics segment provides electronic components and subsystems, as well as communications products, such as defense electronics, environment interconnects, data acquisition and communications equipment for aircraft, components and subsystems for wireless and satellite communications, and general aviation batteries. Its Engineered Systems segment offers systems engineering and integration, technology development, and manufacturing solutions for defense, space, environmental, and energy applications; and designs and manufactures electrochemical energy systems and electronics for military applications. The company markets and sells its products and services through a direct internal sales force, as well as third-party sales representatives and distributors. Teledyne Technologies Incorporated was founded in 1960 and is headquartered in Thousand Oaks, California.",
        fullTimeEmployees=14500,
        city="Thousand Oaks",
        state="CA",
        trailingPE=37.429317,
        dividendYield=None,
        averageVolume=324159,
        regularMarketOpen=379.64,
        volume=156918,
        fiftyTwoWeekHigh=493.97,
        fiftyTwoWeekLow=344.66,
        recommendationKey="buy",
        industry="Scientific & Technical Instruments"
    )
    db.session.add(TDY)

    TFX = Stock(
        name="Teleflex Incorporated",
        ticker="TFX",
        marketCap=11863964672,
        dayHigh=261.93,
        dayLow=252.98,
        currentPrice=253.26,
        longBusinessSummary="Teleflex Incorporated designs, develops, manufactures, and supplies single-use medical devices for common diagnostic and therapeutic procedures in critical care and surgical applications worldwide. It provides vascular access products that comprise Arrow branded catheters, catheter navigation and tip positioning systems, and intraosseous access systems for the administration of intravenous therapies, the measurement of blood pressure, and the withdrawal of blood samples through a single puncture site. The company also offers interventional products, which consists of various coronary catheters, structural heart therapies, and peripheral intervention and cardiac assist products that are used by interventional cardiologists and radiologists, and vascular surgeons; and Arrow branded catheters, Guideline and Trapliner catheters, the Manta Vascular Closure, and Arrow Oncontrol devices. It provides anesthesia products, such as airway and pain management products to support hospital, emergency medicine, and military channels; and surgical products, including metal and polymer ligation clips, and fascial closure surgical systems that are used in laparoscopic surgical procedures, percutaneous surgical systems, and other surgical instruments. The company also offers interventional urology products comprising the UroLift System, an invasive technology for treating lower urinary tract symptoms due to benign prostatic hyperplasia; and respiratory products, including oxygen and aerosol therapies, spirometry, and ventilation management products for use in various care settings. It provides urology products, such as catheters, urine collectors, and catheterization accessories and products for operative endourology; and bladder management services. The company serves hospitals and healthcare providers, medical device manufacturers, and home care markets. The company was incorporated in 1943 and is headquartered in Wayne, Pennsylvania.",
        fullTimeEmployees=14000,
        city="Wayne",
        state="PA",
        trailingPE=27.69685,
        dividendYield=0.0049,
        averageVolume=363898,
        regularMarketOpen=260.58,
        volume=335738,
        fiftyTwoWeekHigh=428.36,
        fiftyTwoWeekLow=244.81,
        recommendationKey="buy",
        industry="Medical Instruments & Supplies"
    )
    db.session.add(TFX)

    TER = Stock(
        name="Teradyne, Inc.",
        ticker="TER",
        marketCap=15522871296,
        dayHigh=99.25,
        dayLow=94.9,
        currentPrice=95.23,
        longBusinessSummary="Teradyne, Inc. designs, develops, manufactures, sells, and supports automatic test equipment worldwide. The company operates through Semiconductor Test, System Test, Industrial Automation, and Wireless Test segments. The Semiconductor Test segment offers products and services for wafer level and device package testing in automotive, industrial, communications, consumer, smartphones, cloud computer and electronic game, and other applications. This segment also provides FLEX test platform systems; J750 test system to address the volume semiconductor devices; Magnum platform that tests memory devices, such as flash memory and DRAM; and ETS platform for semiconductor manufacturers, and assembly and test subcontractors in the analog/mixed signal markets. It serves integrated device manufacturers that integrate the fabrication of silicon wafers into their business; fabless companies that outsource the manufacturing of silicon wafers; foundries; and semiconductor assembly and test providers. The System Test segment offers defense/aerospace test instrumentation and systems; storage test systems; and circuit-board test and inspection systems. The Industrial Automation segment provides collaborative robotic arms, autonomous mobile robots, and advanced robotic control software for manufacturing, logistics, and light industrial customers. The Wireless Test segment provides test solutions for use in the development and manufacture of wireless devices and modules, smartphones, tablets, notebooks, laptops, peripherals, and Internet-of-Things devices under the LitePoint brand name. This segment also offers IQxel products for Wi-Fi and other standards; IQxstream solution for testing GSM, EDGE, CDMA2000, TD-SCDMA, WCDMA, HSPA+, LTE, and 5G technologies; IQcell, a multi-device cellular signaling test solution; IQgig test solution; and turnkey test software for wireless chipsets. Teradyne, Inc. was incorporated in 1960 and is headquartered in North Reading, Massachusetts.",
        fullTimeEmployees=6000,
        city="North Reading",
        state="MA",
        trailingPE=17.937466,
        dividendYield=0.0041,
        averageVolume=1761725,
        regularMarketOpen=98.01,
        volume=2352418,
        fiftyTwoWeekHigh=168.91,
        fiftyTwoWeekLow=85.66,
        recommendationKey="buy",
        industry="Semiconductor Equipment & Materials"
    )
    db.session.add(TER)

    TSLA = Stock(
        name="Tesla, Inc.",
        ticker="TSLA",
        marketCap=700963422208,
        dayHigh=749.91,
        dayLow=697.03,
        currentPrice=697.99,
        longBusinessSummary="Tesla, Inc. designs, develops, manufactures, leases, and sells electric vehicles, and energy generation and storage systems in the United States, China, and internationally. The company operates in two segments, Automotive, and Energy Generation and Storage. The Automotive segment offers electric vehicles, as well as sells automotive regulatory credits. It provides sedans and sport utility vehicles through direct and used vehicle sales, a network of Tesla Superchargers, and in-app upgrades; and purchase financing and leasing services. This segment is also involved in the provision of non-warranty after-sales vehicle services, sale of used vehicles, retail merchandise, and vehicle insurance, as well as sale of products to third party customers; services for electric vehicles through its company-owned service locations, and Tesla mobile service technicians; and vehicle limited warranties and extended service plans. The Energy Generation and Storage segment engages in the design, manufacture, installation, sale, and leasing of solar energy generation and energy storage products, and related services to residential, commercial, and industrial customers and utilities through its website, stores, and galleries, as well as through a network of channel partners. This segment also offers service and repairs to its energy product customers, including under warranty; and various financing options to its solar customers. The company was formerly known as Tesla Motors, Inc. and changed its name to Tesla, Inc. in February 2017. Tesla, Inc. was incorporated in 2003 and is headquartered in Austin, Texas.",
        fullTimeEmployees=99290,
        city="Austin",
        state="TX",
        trailingPE=227.95232,
        dividendYield=None,
        averageVolume=29091609,
        regularMarketOpen=733.45,
        volume=30062991,
        fiftyTwoWeekHigh=1243.49,
        fiftyTwoWeekLow=620.46,
        recommendationKey="buy",
        industry="Auto Manufacturers"
    )
    db.session.add(TSLA)

    TXN = Stock(
        name="Texas Instruments Incorporated",
        ticker="TXN",
        marketCap=142370766848,
        dayHigh=158.99,
        dayLow=154.08,
        currentPrice=154.16,
        longBusinessSummary="Texas Instruments Incorporated designs, manufactures, and sells semiconductors to electronics designers and manufacturers worldwide. It operates in two segments, Analog and Embedded Processing. The Analog segment offers power products to manage power requirements in various levels using battery-management solutions, DC/DC switching regulators, AC/DC and isolated controllers and converters, power switches, linear regulators, voltage supervisors, voltage references, and lighting products. This segment also provides signal chain products that sense, condition, and measure signals to allow information to be transferred or converted for further processing and control for use in end markets, including amplifiers, data converters, interface products, motor drives, clocks, and sensing products. The Embedded Processing segment offers microcontrollers that are used in electronic equipment; digital signal processors for mathematical computations; and applications processors for specific computing activity. This segment offers products for use in various markets, such as industrial, automotive, personal electronics, communications equipment, enterprise systems, and calculators and other. The company also provides DLP products primarily for use in projectors to create high-definition images; calculators; and application-specific integrated circuits. It markets and sells its semiconductor products through direct sales and distributors, as well as through its website. Texas Instruments Incorporated was founded in 1930 and is headquartered in Dallas, Texas.",
        fullTimeEmployees=31000,
        city="Dallas",
        state="TX",
        trailingPE=19.794556,
        dividendYield=0.0271,
        averageVolume=5982217,
        regularMarketOpen=156.74,
        volume=4687615,
        fiftyTwoWeekHigh=202.26,
        fiftyTwoWeekLow=149.1,
        recommendationKey="hold",
        industry="Semiconductors"
    )
    db.session.add(TXN)

    TXT = Stock(
        name="Textron Inc.",
        ticker="TXT",
        marketCap=13236520960,
        dayHigh=62.26,
        dayLow=59.98,
        currentPrice=60.05,
        longBusinessSummary="Textron Inc. operates in the aircraft, defense, industrial, and finance businesses. The company's Textron Aviation segment manufactures, sells, and services business jets, turboprop and piston engine aircraft, and military trainer and defense aircraft; and offers maintenance, inspection, and repair services, as well as sells commercial parts. Its Bell segment supplies military and commercial helicopters, tiltrotor aircrafts, and related spare parts and services. The company's Textron Systems segment offers unmanned aircraft systems, electronic systems and solutions, advanced marine crafts, piston aircraft engines, live military air-to-air and air-to-ship training, weapons and related components, and armored and specialty vehicles. Its Industrial segment offers blow-molded plastic fuel systems, including conventional plastic fuel tanks and pressurized fuel tanks for hybrid vehicle applications, clear-vision systems, and plastic tanks for catalytic reduction systems primarily to automobile original equipment manufacturers; and golf cars, off-road utility vehicles, recreational side-by-side and all-terrain vehicles, snowmobiles, light transportation vehicles, aviation ground support equipment, professional turf-maintenance equipment, and turf-care vehicles to golf courses and resorts, government agencies and municipalities, consumers, outdoor enthusiasts, and commercial and industrial users. The company's Finance segment provides financing services to purchase new and pre-owned aircraft and bell helicopters. It serves in the United States, Europe, Asia, Australia, and internationally. Textron Inc. was founded in 1923 and is headquartered in Providence, Rhode Island.",
        fullTimeEmployees=33000,
        city="Providence",
        state="RI",
        trailingPE=17.661764,
        dividendYield=0.0013,
        averageVolume=1298959,
        regularMarketOpen=61.3,
        volume=1197342,
        fiftyTwoWeekHigh=79.45,
        fiftyTwoWeekLow=57.11,
        recommendationKey="none",
        industry="Aerospace & Defense"
    )
    db.session.add(TXT)

    TMO = Stock(
        name="Thermo Fisher Scientific Inc.",
        ticker="TMO",
        marketCap=211119112192,
        dayHigh=545.1228,
        dayLow=534.3,
        currentPrice=535.77,
        longBusinessSummary="Thermo Fisher Scientific Inc. offers life sciences solutions, analytical instruments, specialty diagnostics, and laboratory products and service worldwide. The company's Life Sciences Solutions segment offers reagents, instruments, and consumables for biological and medical research, discovery, and production of drugs and vaccines, as well as diagnosis of infections and diseases to pharmaceutical, biotechnology, agricultural, clinical, healthcare, academic, and government markets. Its Analytical Instruments segment provides instruments, consumables, software, and services for use in laboratory, on production line, and in field for pharmaceutical, biotechnology, academic, government, environmental, and other research and industrial markets, as well as clinical laboratories. The company's Specialty Diagnostics segment offers liquid, ready-to-use, and lyophilized immunodiagnostic reagent kits, as well as calibrators, controls, and calibration verification fluids; ImmunoCAP for allergy and asthma tests, and EliA for autoimmunity tests; dehydrated and prepared culture media, collection and transport systems, instrumentation, and consumables; human leukocyte antigen typing and testing for organ transplant market; and healthcare products. Its Laboratory Products and Services segment provides laboratory refrigerators and freezers, ultralow-temperature freezers, and cryopreservation storage tanks; temperature control, sample preparation and preservation, centrifugation, and biological safety cabinet products; water analysis instruments; laboratory plastics products; laboratory chemicals; and pharma services. The company offers products and services through a direct sales force, customer-service professionals, electronic commerce, third-party distributors, and catalogs. It has a strategic alliance with the University of California, San Francisco. The company was incorporated in 1956 and is based in Waltham, Massachusetts.",
        fullTimeEmployees=130000,
        city="Waltham",
        state="MA",
        trailingPE=24.86864,
        dividendYield=0.0022,
        averageVolume=1439629,
        regularMarketOpen=542.6,
        volume=704431,
        fiftyTwoWeekHigh=672.34,
        fiftyTwoWeekLow=497.83,
        recommendationKey="buy",
        industry="Diagnostics & Research"
    )
    db.session.add(TMO)

    TJX = Stock(
        name="The TJX Companies, Inc.",
        ticker="TJX",
        marketCap=68566740992,
        dayHigh=60.59,
        dayLow=57.44,
        currentPrice=57.48,
        longBusinessSummary="The TJX Companies, Inc., together with its subsidiaries, operates as an off-price apparel and home fashions retailer. It operates through four segments: Marmaxx, HomeGoods, TJX Canada, and TJX International. The company sells family apparel, including footwear and accessories; home fashions, such as home basics, furniture, rugs, lighting products, giftware, soft home products, decorative accessories, tabletop, and cookware, as well as expanded pet, kids, and gourmet food departments; jewelry and accessories; and other merchandise. As of February 23, 2022, it operated 1,284 T.J. Maxx, 1,148 Marshalls, 850 HomeGoods, 59 Sierra, and 39 Homesense stores, as well as tjmaxx.com, marshalls.com, and sierra.com in the United States; 293 Winners, 147 HomeSense, and 106 Marshalls stores in Canada; 618 T.K. Maxx and 77 Homesense stores, as well as tkmaxx.com in Europe; and 68 T.K. Maxx stores in Australia. The company was incorporated in 1962 and is headquartered in Framingham, Massachusetts.",
        fullTimeEmployees=340000,
        city="Framingham",
        state="MA",
        trailingPE=26.525148,
        dividendYield=0.020599999,
        averageVolume=7437900,
        regularMarketOpen=60.13,
        volume=5504268,
        fiftyTwoWeekHigh=77.35,
        fiftyTwoWeekLow=53.69,
        recommendationKey="buy",
        industry="Apparel Retail"
    )
    db.session.add(TJX)

    TSCO = Stock(
        name="Tractor Supply Company",
        ticker="TSCO",
        marketCap=22222379008,
        dayHigh=205.37,
        dayLow=194.92,
        currentPrice=195.25,
        longBusinessSummary="Tractor Supply Company operates as a rural lifestyle retailer in the United States. The company offers a selection of merchandise, including equine, livestock, pet, and small animal products necessary for their health, care, growth, and containment; hardware, truck, towing, and tool products; seasonal products, such as heating products, lawn and garden items, power equipment, gifts, and toys; work/recreational clothing and footwear; and maintenance products for agricultural and rural use. It provides its products under the 4health, Producer's Pride, American Farmworks, Red Shed, Bit & Bridle, Redstone, Blue Mountain, Retriever, C.E. Schmidt, Ridgecut, Countyline, Royal Wing, Dumor, Strive, Groundwork, Traveller, Huskee, Treeline, JobSmart, TSC Tractor Supply Co, Paws & Claws, and Untamed brands. As of December 25, 2021, it operated 2,003 Tractor Supply stores in 49 states, as well as 177 Petsense stores in 23 states. The company operates its retail stores under the Tractor Supply Company, Del's Feed & Farm Supply, and Petsense names. It also operates websites under the TractorSupply.com and Petsense.com names. The company sells its products to recreational farmers, ranchers, and others. The company was founded in 1938 and is based in Brentwood, Tennessee.",
        fullTimeEmployees=46000,
        city="Brentwood",
        state="TN",
        trailingPE=24.964838,
        dividendYield=0.0182,
        averageVolume=1264506,
        regularMarketOpen=202.84,
        volume=820260,
        fiftyTwoWeekHigh=241.54,
        fiftyTwoWeekLow=166.49,
        recommendationKey="buy",
        industry="Specialty Retail"
    )
    db.session.add(TSCO)

    TDG = Stock(
        name="TransDigm Group Incorporated",
        ticker="TDG",
        marketCap=29425563648,
        dayHigh=551.675,
        dayLow=532.06,
        currentPrice=532.6,
        longBusinessSummary="TransDigm Group Incorporated designs, produces, and supplies aircraft components in the United States and internationally. Its Power & Control segment offers mechanical/electro-mechanical actuators and controls, ignition systems and engine technology, specialized pumps and valves, power conditioning devices, specialized AC/DC electric motors and generators, batteries and chargers, databus and power controls, sensor products, switches and relay panels, hoists, winches and lifting devices, and cargo loading and handling systems. This segment serves engine and power system and subsystem suppliers, airlines, third party maintenance suppliers, military buying agencies, and repair depots. The company's Airframe segment provides engineered latching and locking devices, engineered rods, engineered connectors and elastomer sealing solutions, cockpit security components and systems, cockpit displays, engineered audio, radio and antenna systems, lavatory components, seat belts and safety restraints, engineered and customized interior surfaces and related components, thermal protection and insulation products, lighting and control technology, and parachutes. This segment serves airframe manufacturers, cabin system and subsystem suppliers, airlines, third party maintenance suppliers, military buying agencies, and repair depots. Its Non-aviation segment offers seat belts and safety restraints for ground transportation applications; electro-mechanical actuators for space applications; hydraulic/electromechanical actuators and fuel valves for land-based gas turbines; refueling systems for heavy equipment used in mining, construction, and other industries; and turbine controls for the energy and oil and gas markets. This segment serves off-road vehicle and subsystem suppliers, child restraint system suppliers, and satellite and space system suppliers; and manufacturers of heavy equipment. TransDigm Group Incorporated was founded in 1993 and is based in Cleveland, Ohio.",
        fullTimeEmployees=13300,
        city="Cleveland",
        state="OH",
        trailingPE=51.241096,
        dividendYield=None,
        averageVolume=354869,
        regularMarketOpen=538.65,
        volume=301277,
        fiftyTwoWeekHigh=686.06,
        fiftyTwoWeekLow=500.08,
        recommendationKey="buy",
        industry="Aerospace & Defense"
    )
    db.session.add(TDG)

    TRV = Stock(
        name="The Travelers Companies, Inc.",
        ticker="TRV",
        marketCap=41199124480,
        dayHigh=170.645,
        dayLow=167.42,
        currentPrice=167.47,
        longBusinessSummary="The Travelers Companies, Inc., through its subsidiaries, provides a range of commercial and personal property, and casualty insurance products and services to businesses, government units, associations, and individuals in the United states and internationally. The company operates through three segments: Business Insurance, Bond & Specialty Insurance, and Personal Insurance. The Business Insurance segment offers workers' compensation, commercial automobile and property, general liability, commercial multi-peril, employers' liability, public and product liability, professional indemnity, marine, aviation, onshore and offshore energy, construction, terrorism, personal accident, and kidnap and ransom insurance products. This segment operates through select accounts, which serve small businesses; commercial accounts that serve mid-sized businesses; national accounts, which serve large companies; and national property and other that serve large and mid-sized customers, commercial trucking industry, and agricultural businesses, as well as markets and distributes its products through brokers, wholesale agents, and program managers. The Bond & Specialty Insurance segment provides surety, fidelity, management and professional liability, and other property and casualty coverages and related risk management services through independent agencies and brokers. The Personal Insurance segment offers property and casualty insurance covering personal risks, primarily automobile and homeowners insurance to individuals through independent agencies and brokers. The Travelers Companies, Inc. was founded in 1853 and is based in New York, New York.",
        fullTimeEmployees=30184,
        city="New York",
        state="NY",
        trailingPE=11.726769,
        dividendYield=0.0215,
        averageVolume=1290706,
        regularMarketOpen=168.43,
        volume=1061739,
        fiftyTwoWeekHigh=187.98,
        fiftyTwoWeekLow=145.4,
        recommendationKey="hold",
        industry="Insurance—Property & Casualty"
    )
    db.session.add(TRV)

    TRMB = Stock(
        name="Trimble Inc.",
        ticker="TRMB",
        marketCap=14824532992,
        dayHigh=60.92,
        dayLow=58.81,
        currentPrice=59.06,
        longBusinessSummary="Trimble Inc. provides technology solutions that enable professionals and field mobile workers to enhance or transform their work processes worldwide. The company's Buildings and Infrastructure segment offers field and office software for route selection and design; systems to guide and control construction equipment; software for 3D design and data sharing; systems to monitor, track, and manage assets, equipment, and workers; software to share and communicate data; program management solutions for construction owners; 3D conceptual design and modeling software; building information modeling software; enterprise resource planning, project management, and project collaboration solutions; integrated site layout and measurement systems; cost estimating, scheduling, and project controls solutions; and applications for sub-contractors and trades. Its Geospatial segment provides surveying and geospatial products, and geographic information systems. The company's Resources and Utilities segment offers precision agriculture products and services, such as guidance and positioning systems, including autonomous steering systems, automated and variable-rate application and technology systems, and information management solutions; manual and automated navigation guidance for tractors and other farm equipment; solutions to automate application of pesticide and seeding; water solutions; and agricultural software. Its Transportation segment offers solutions for long haul trucking and freight shipper markets; mobility solutions comprising route management, safety and compliance, end-to-end vehicle management, video intelligence, and supply chain communications; and fleet and transportation management systems, analytics, routing, mapping, reporting, and predictive modeling solutions. The company was formerly known as Trimble Navigation Limited and changed its name to Trimble Inc. in October 2016. Trimble Inc. was founded in 1978 and is headquartered in Sunnyvale, California.",
        fullTimeEmployees=11931,
        city="Sunnyvale",
        state="CA",
        trailingPE=26.882113,
        dividendYield=None,
        averageVolume=1147430,
        regularMarketOpen=60.36,
        volume=1110246,
        fiftyTwoWeekHigh=96.49,
        fiftyTwoWeekLow=55.65,
        recommendationKey="buy",
        industry="Scientific & Technical Instruments"
    )
    db.session.add(TRMB)

    TFC = Stock(
        name="Truist Financial Corporation",
        ticker="TFC",
        marketCap=64568627200,
        dayHigh=49.68,
        dayLow=48.18,
        currentPrice=48.37,
        longBusinessSummary="Truist Financial Corporation, a holding company, provides banking and trust services in the Southeastern and Mid-Atlantic United States. The company operates through three segments: Consumer Banking and Wealth, Corporate and Commercial Banking, and Insurance Holdings. Its deposit products include noninterest-bearing checking, interest-bearing checking, savings, and money market deposit accounts, as well as certificates of deposit and individual retirement accounts. The company also provides funding; asset management; automobile lending; bankcard lending; consumer finance; home equity and mortgage lending; insurance, such as property and casualty, life, health, employee benefits, workers compensation and professional liability, surety coverage, title, and other insurance products; investment brokerage; mobile/online banking; and payment, lease financing, small business lending, and wealth management/private banking services. In addition, it offers association, capital market, institutional trust, insurance premium and commercial finance, international banking, leasing, merchant, commercial deposit and treasury, government finance, commercial middle market lending, small business and student lending, floor plan and commercial mortgage lending, mortgage warehouse lending, private equity investment, real estate lending, and supply chain financing services. Further, the company provides corporate and investment banking, retail and wholesale brokerage, securities underwriting, and investment advisory services. As of December 31, 2021, the company operated through 2,517 banking offices. The company was formerly known as BB&T Corporation and changed its name to Truist Financial Corporation in December 2019. Truist Financial Corporation was founded in 1872 and is headquartered in Charlotte, North Carolina.",
        fullTimeEmployees=51169,
        city="Charlotte",
        state="NC",
        trailingPE=11.413403,
        dividendYield=0.041500002,
        averageVolume=7860685,
        regularMarketOpen=48.9,
        volume=4886931,
        fiftyTwoWeekHigh=68.95,
        fiftyTwoWeekLow=44.75,
        recommendationKey="hold",
        industry="Banks—Regional"
    )
    db.session.add(TFC)

    TYL = Stock(
        name="Tyler Technologies, Inc.",
        ticker="TYL",
        marketCap=13694279680,
        dayHigh=344.6,
        dayLow=332.03,
        currentPrice=334.2,
        longBusinessSummary="Tyler Technologies, Inc. provides integrated information management solutions and services for the public sector. The company operates in three segments: Enterprise Software; Appraisal and Tax; and NIC. It offers financial management solutions, including modular fund accounting systems for government agencies or not-for-profit entities; utility billing systems for the billing and collection of metered and non-metered services; products to automate city and county functions, such as municipal courts, parking tickets, equipment and project costing, animal and business licenses, permits and inspections, code enforcement, citizen complaint tracking, ambulance billing, fleet maintenance, and cemetery records management; and student information and transportation solutions for K-12 schools. The company also provides a suite of judicial solutions comprising court case management, court and law enforcement, prosecutor, and supervision systems to handle multi-jurisdictional county or statewide implementations, and single county systems; public safety software solutions; systems and software to automate the appraisal and assessment of real and personal property, as well as tax applications for agencies that bill and collect taxes; planning, regulatory, and maintenance software solutions for public sector agencies; software applications to enhance and automate operations involving records and document management; and data and insights solutions. In addition, it offers software as a service arrangements and electronic document filing solutions for courts and law offices; software and hardware installation, data conversion, training, product modification, and maintenance and support services; and property appraisal outsourcing services for taxing jurisdictions. The company has a strategic collaboration agreement with Amazon Web Services for cloud hosting services. Tyler Technologies, Inc. was founded in 1966 and is headquartered in Plano, Texas.",
        fullTimeEmployees=6959,
        city="Plano",
        state="TX",
        trailingPE=87.37255,
        dividendYield=None,
        averageVolume=286320,
        regularMarketOpen=341.6,
        volume=203839,
        fiftyTwoWeekHigh=557.55,
        fiftyTwoWeekLow=300.85,
        recommendationKey="buy",
        industry="Software—Application"
    )
    db.session.add(TYL)

    TSN = Stock(
        name="Tyson Foods, Inc.",
        ticker="TSN",
        marketCap=31086995456,
        dayHigh=86.95,
        dayLow=85.39,
        currentPrice=85.62,
        longBusinessSummary="Tyson Foods, Inc., together with its subsidiaries, operates as a food company worldwide. It operates through four segments: Beef, Pork, Chicken, and Prepared Foods. The company processes live fed cattle and live market hogs; fabricates dressed beef and pork carcasses into primal and sub-primal meat cuts, as well as case ready beef and pork, and fully cooked meats; raises and processes chickens into fresh, frozen, and value-added chicken products; and supplies poultry breeding stock; sells specialty products, such as hides and meats. It also manufactures and markets frozen and refrigerated food products, including ready-to-eat sandwiches, flame-grilled hamburgers, Philly steaks, pepperoni, bacon, breakfast sausage, turkey, lunchmeat, hot dogs, flour and corn tortilla products, appetizers, snacks, prepared meals, ethnic foods, side dishes, meat dishes, breadsticks, and processed meats under the Jimmy Dean, Hillshire Farm, Ball Park, Wright, State Fair, Aidells, and Gallo Salame brands. The company also offers its products under Tyson and ibp brands. It sells its products through its sales staff to grocery retailers, grocery wholesalers, meat distributors, warehouse club stores, military commissaries, industrial food processing companies, chain restaurants or their distributors, live markets, international export companies, and domestic distributors who serve restaurants and food service operations, such as plant and school cafeterias, convenience stores, hospitals, and other vendors, as well as through independent brokers and trading companies. The company was founded in 1935 and is headquartered in Springdale, Arkansas.",
        fullTimeEmployees=137000,
        city="Springdale",
        state="AR",
        trailingPE=10.266188,
        dividendYield=0.020399999,
        averageVolume=2028798,
        regularMarketOpen=86.25,
        volume=1207430,
        fiftyTwoWeekHigh=100.72,
        fiftyTwoWeekLow=69.88,
        recommendationKey="buy",
        industry="Farm Products"
    )
    db.session.add(TSN)

    USB = Stock(
        name="U.S. Bancorp",
        ticker="USB",
        marketCap=69528494080,
        dayHigh=48.2,
        dayLow=46.695,
        currentPrice=46.89,
        longBusinessSummary="U.S. Bancorp, a financial services holding company, provides various financial services to individuals, businesses, institutional organizations, governmental entities and other financial institutions in the United States. It operates in Corporate and Commercial Banking, Consumer and Business Banking, Wealth Management and Investment Services, Payment Services, and Treasury and Corporate Support segments. The company offers depository services, including checking accounts, savings accounts, and time certificate contracts; lending services, such as traditional credit products; and credit card services, lease financing and import/export trade, asset-backed lending, agricultural finance, and other products. It also provides ancillary services comprising capital markets, treasury management, and receivable lock-box collection services to corporate and governmental entity customers; and a range of asset management and fiduciary services for individuals, estates, foundations, business corporations, and charitable organizations. In addition, the company offers investment and insurance products to its customers principally within its markets, as well as fund administration services to a range of mutual and other funds. Further, it provides corporate and purchasing card, and corporate trust services; and merchant processing services, as well as investment management, ATM processing, mortgage banking, insurance, and brokerage and leasing services. As of December 31, 2021, the company provided its products and services through a network of 2,230 banking offices principally operating in the Midwest and West regions of the United States, as well as through on-line services, over mobile devices, and other distribution channels; and operated a network of 4,059 ATMs. The company was founded in 1863 and is headquartered in Minneapolis, Minnesota.",
        fullTimeEmployees=70000,
        city="Minneapolis",
        state="MN",
        trailingPE=9.409994,
        dividendYield=0.0379,
        averageVolume=7896104,
        regularMarketOpen=47.72,
        volume=6401582,
        fiftyTwoWeekHigh=63.57,
        fiftyTwoWeekLow=44.79,
        recommendationKey="hold",
        industry="Banks—Regional"
    )
    db.session.add(USB)

    UDR = Stock(
        name="UDR, Inc.",
        ticker="UDR",
        marketCap=14299851776,
        dayHigh=47.345,
        dayLow=46.135,
        currentPrice=46.25,
        longBusinessSummary="UDR, Inc. (NYSE: UDR), an S&P 500 company, is a leading multifamily real estate investment trust with a demonstrated performance history of delivering superior and dependable returns by successfully managing, buying, selling, developing and redeveloping attractive real estate communities in targeted U.S. markets. As of September 30, 2020, UDR owned or had an ownership position in 51,649 apartment homes including 1,031 homes under development. For over 48 years, UDR has delivered long-term value to shareholders, the best standard of service to Residents and the highest quality experience for Associates.",
        fullTimeEmployees=1219,
        city="Highlands Ranch",
        state="CO",
        trailingPE=256.94443,
        dividendYield=0.0312,
        averageVolume=2045741,
        regularMarketOpen=46.93,
        volume=2127228,
        fiftyTwoWeekHigh=61.06,
        fiftyTwoWeekLow=42,
        recommendationKey="buy",
        industry="REIT—Residential"
    )
    db.session.add(UDR)

    ULTA = Stock(
        name="Ulta Beauty, Inc.",
        ticker="ULTA",
        marketCap=20884985856,
        dayHigh=405,
        dayLow=385.8,
        currentPrice=385.9,
        longBusinessSummary="Ulta Beauty, Inc. operates as a retailer of beauty products in the United States. The company's stores offer cosmetics, fragrances, skincare and haircare products, bath and body products, and salon styling tools; professional hair products; salon services, including hair, skin, makeup, and brow services; and nail services. It also provides its private label products, such as the Ulta Beauty Collection branded cosmetics, skincare, and bath products, as well as Ulta Beauty branded products; and the Ulta Beauty branded gifts. As of March 10, 2022, the company operated 1,308 retail stores across 50 states. It also distributes its products through its website ulta.com; and mobile applications. The company was formerly known as Ulta Salon, Cosmetics & Fragrance, Inc. and changed its name to Ulta Beauty, Inc. in January 2017. Ulta Beauty, Inc. was incorporated in 1990 and is based in Bolingbrook, Illinois.",
        fullTimeEmployees=16500,
        city="Bolingbrook",
        state="IL",
        trailingPE=24.732424,
        dividendYield=None,
        averageVolume=831283,
        regularMarketOpen=400.74,
        volume=705544,
        fiftyTwoWeekHigh=438.63,
        fiftyTwoWeekLow=319.05,
        recommendationKey="buy",
        industry="Specialty Retail"
    )
    db.session.add(ULTA)

    UNP = Stock(
        name="Union Pacific Corporation",
        ticker="UNP",
        marketCap=137164029952,
        dayHigh=218.85,
        dayLow=213.15,
        currentPrice=213.36,
        longBusinessSummary="Union Pacific Corporation, through its subsidiary, Union Pacific Railroad Company, operates in the railroad business in the United States. The company offers transportation services for grain and grain products, fertilizers, food and refrigerated products, and coal and renewables to grain processors, animal feeders, ethanol producers, and other agricultural users; petroleum, and liquid petroleum gases; and construction products, industrial chemicals, plastics, forest products, specialized products, metals and ores, soda ash, and sand, as well as finished automobiles, automotive parts, and merchandise in intermodal containers. As of December 31, 2021, its rail network included 32,452 route miles connecting Pacific Coast and Gulf Coast ports with the Midwest and Eastern United States gateways. The company was founded in 1862 and is headquartered in Omaha, Nebraska.",
        fullTimeEmployees=30189,
        city="Omaha",
        state="NE",
        trailingPE=22.855919,
        dividendYield=0.0225,
        averageVolume=3300777,
        regularMarketOpen=216.13,
        volume=2156387,
        fiftyTwoWeekHigh=278.94,
        fiftyTwoWeekLow=195.68,
        recommendationKey="buy",
        industry="Railroads"
    )
    db.session.add(UNP)

    UPS = Stock(
        name="United Parcel Service, Inc.",
        ticker="UPS",
        marketCap=156376023040,
        dayHigh=185.28,
        dayLow=179.51,
        currentPrice=179.92,
        longBusinessSummary="United Parcel Service, Inc. provides letter and package delivery, transportation, logistics, and related services. It operates through two segments, U.S. Domestic Package and International Package. The U.S. Domestic Package segment offers time-definite delivery of letters, documents, small packages, and palletized freight through air and ground services in the United States. The International Package segment provides guaranteed day and time-definite international shipping services in Europe, the Asia Pacific, Canada and Latin America, the Indian sub-continent, the Middle East, and Africa. This segment offers guaranteed time-definite express options. The company also provides international air and ocean freight forwarding, customs brokerage, distribution and post-sales, and mail and consulting services in approximately 200 countries and territories. In addition, it offers truckload brokerage services; supply chain solutions to the healthcare and life sciences industry; shipping, visibility, and billing technologies; and financial and insurance services. The company operates a fleet of approximately 121,000 package cars, vans, tractors, and motorcycles; and owns 59,000 containers that are used to transport cargo in its aircraft. United Parcel Service, Inc. was founded in 1907 and is headquartered in Atlanta, Georgia.",
        fullTimeEmployees=534000,
        city="Atlanta",
        state="GA",
        trailingPE=24.46227,
        dividendYield=0.0341,
        averageVolume=3671153,
        regularMarketOpen=182.76,
        volume=2020813,
        fiftyTwoWeekHigh=233.72,
        fiftyTwoWeekLow=165.34,
        recommendationKey="buy",
        industry="Integrated Freight & Logistics"
    )
    db.session.add(UPS)

    UNH = Stock(
        name="UnitedHealth Group Incorporated",
        ticker="UNH",
        marketCap=478874730496,
        dayHigh=518.61,
        dayLow=505.08,
        currentPrice=508.44,
        longBusinessSummary="UnitedHealth Group Incorporated operates as a diversified health care company in the United States. It operates through four segments: UnitedHealthcare, Optum Health, Optum Insight, and Optum Rx. The UnitedHealthcare segment offers consumer-oriented health benefit plans and services for national employers, public sector employers, mid-sized employers, small businesses, and individuals; health care coverage and well-being services to individuals age 50 and older addressing their needs for preventive and acute health care services, as well as services dealing with chronic disease and other specialized issues for older individuals; Medicaid plans, children's health insurance and health care programs; health and dental benefits; and hospital and clinical services. The OptumHealth segment provides access to networks of care provider specialists, health management services, care delivery, consumer engagement, and financial services. This segment serves individuals directly through care delivery systems, employers, payers, and government entities. The OptumInsight segment offers software and information products, advisory consulting arrangements, and managed services outsourcing contracts to hospital systems, physicians, health plans, governments, life sciences companies, and other organizations. The OptumRx segment provides pharmacy care services and programs, including retail network contracting, home delivery, specialty and compounding pharmacy, and purchasing and clinical capabilities, as well as develops programs in the areas of step therapy, formulary management, drug adherence, and disease/drug therapy management. UnitedHealth Group Incorporated was incorporated in 1977 and is based in Minnetonka, Minnesota.",
        fullTimeEmployees=350000,
        city="Minnetonka",
        state="MN",
        trailingPE=31.558563,
        dividendYield=0.0119,
        averageVolume=3405824,
        regularMarketOpen=512.08,
        volume=4978896,
        fiftyTwoWeekHigh=553.29,
        fiftyTwoWeekLow=383.12,
        recommendationKey="buy",
        industry="Healthcare Plans"
    )
    db.session.add(UNH)

    UHS = Stock(
        name="Universal Health Services, Inc.",
        ticker="UHS",
        marketCap=8527184384,
        dayHigh=110,
        dayLow=105.92,
        currentPrice=106.09,
        longBusinessSummary="Universal Health Services, Inc., through its subsidiaries, owns and operates acute care hospitals, and outpatient and behavioral health care facilities. The company operates through Acute Care Hospital Services and Behavioral Health Care Services segments. Its hospitals offer general and specialty surgery, internal medicine, obstetrics, emergency room care, radiology, oncology, diagnostic and coronary care, pediatric services, pharmacy services, and/or behavioral health services. As of February 24, 2022, it owned and/or operated 363 inpatient facilities, and 40 outpatient and other facilities located in 39 states; Washington, D.C.; the United Kingdom; and Puerto Rico. The company also provides commercial health insurance services; and various management services, which include central purchasing, information, finance and control systems, facilities planning, physician recruitment, administrative personnel management, marketing, and public relations services. Universal Health Services, Inc. founded in 1978 and is headquartered in King of Prussia, Pennsylvania.",
        fullTimeEmployees=89000,
        city="King of Prussia",
        state="PA",
        trailingPE=8.539804,
        dividendYield=0.0064,
        averageVolume=830914,
        regularMarketOpen=108.6,
        volume=540795,
        fiftyTwoWeekHigh=165,
        fiftyTwoWeekLow=99.54,
        recommendationKey="hold",
        industry="Medical Care Facilities"
    )
    db.session.add(UHS)

    VTR = Stock(
        name="Ventas, Inc.",
        ticker="VTR",
        marketCap=20401885184,
        dayHigh=52.61,
        dayLow=50.99,
        currentPrice=51.11,
        longBusinessSummary="Ventas, an S&P 500 company, operates at the intersection of two powerful and dynamic industries  healthcare and real estate. As one of the world's foremost Real Estate Investment Trusts (REIT), we use the power of capital to unlock the value of real estate, partnering with leading care providers, developers, research and medical institutions, innovators and healthcare organizations whose success is buoyed by the demographic tailwind of an aging population. For more than twenty years, Ventas has followed a successful strategy that endures: combining a high-quality diversified portfolio of properties and capital sources to manage through cycles, working with industry leading partners, and a collaborative and experienced team focused on producing consistent growing cash flows and superior returns on a strong balance sheet, ultimately rewarding Ventas shareholders. As of September 30, 2020, Ventas owned or managed through unconsolidated joint ventures approximately 1,200 properties.",
        fullTimeEmployees=434,
        city="Chicago",
        state="IL",
        trailingPE=96.616264,
        dividendYield=0.0327,
        averageVolume=2102683,
        regularMarketOpen=52.1,
        volume=1363985,
        fiftyTwoWeekHigh=64.02,
        fiftyTwoWeekLow=45.44,
        recommendationKey="buy",
        industry="REIT—Healthcare Facilities"
    )
    db.session.add(VTR)

    VRSN = Stock(
        name="VeriSign, Inc.",
        ticker="VRSN",
        marketCap=18245670912,
        dayHigh=170.62,
        dayLow=163.67,
        currentPrice=164.26,
        longBusinessSummary="VeriSign, Inc., together with its subsidiaries, provides domain name registry services and internet infrastructure that enables internet navigation for various recognized domain names worldwide. It enables the security, stability, and resiliency of internet infrastructure and services, including providing root zone maintainer services, operating two of the 13 internet root servers; and offering registration services and authoritative resolution for the .com and .net domains, which support global e-commerce. The company also back-end systems for .cc, .gov, .edu, and .name domain names, as well as operates distributed servers, networking, security, and data integrity services. VeriSign, Inc. was incorporated in 1995 and is headquartered in Reston, Virginia.",
        fullTimeEmployees=902,
        city="Reston",
        state="VA",
        trailingPE=30.27834,
        dividendYield=None,
        averageVolume=796990,
        regularMarketOpen=168.97,
        volume=529811,
        fiftyTwoWeekHigh=257.03,
        fiftyTwoWeekLow=155.25,
        recommendationKey="buy",
        industry="Software—Infrastructure"
    )
    db.session.add(VRSN)

    VRSK = Stock(
        name="Verisk Analytics, Inc.",
        ticker="VRSK",
        marketCap=27226537984,
        dayHigh=175.45,
        dayLow=168.81,
        currentPrice=168.94,
        longBusinessSummary="Verisk Analytics, Inc. provides data analytics solutions in the United States and internationally. The company provides predictive analytics and decision support solutions to customers in rating, underwriting, claims, catastrophe and weather risk, global risk analytics, natural resources intelligence, economic forecasting, commercial banking and finance, and various other fields. It operates in three segments: Insurance, Energy and Specialized Markets, and Financial Services. The Insurance segment focuses on the prediction of loss, selection and pricing of risk, and compliance with their reporting requirements for property and casualty customers, as well as develops machine learned and artificially intelligent models to forecast scenarios and produce standard and customized analytics that help its customers to manage their businesses, including detecting fraud before and after a loss event, and quantifying losses. The Energy and Specialized Markets segment provides data analytics for the natural resources value chain, including energy, chemicals, metals, mining, power, and renewables sectors; research and consulting services focusing on supporting customer capital allocation decisions, asset valuation and benchmarking, commodity markets, and corporate analysis; and consultancy services in the areas of business environment, business improvement, business strategies, commercial advisory, and transaction support, as well as analysis and advice on assets, companies, governments, and markets. The Financial Services segment offers benchmarking, decisioning algorithms, business intelligence, and customized analytic services to financial institutions, payment networks and processors, alternative lenders, regulators, and merchants. The company was founded in 1971 and is headquartered in Jersey City, New Jersey.",
        fullTimeEmployees=9367,
        city="Jersey City",
        state="NJ",
        trailingPE=39.471962,
        dividendYield=0.0069999998,
        averageVolume=1052119,
        regularMarketOpen=174.08,
        volume=667414,
        fiftyTwoWeekHigh=231.57,
        fiftyTwoWeekLow=156.05,
        recommendationKey="buy",
        industry="Consulting Services"
    )
    db.session.add(VRSK)

    VZ = Stock(
        name="Verizon Communications Inc.",
        ticker="VZ",
        marketCap=211818971136,
        dayHigh=51.3,
        dayLow=50.43,
        currentPrice=50.46,
        longBusinessSummary="Verizon Communications Inc., through its subsidiaries, offers communications, technology, information, and entertainment products and services to consumers, businesses, and governmental entities worldwide. Its Consumer segment provides postpaid and prepaid service plans; internet access on notebook computers and tablets; wireless equipment, including smartphones and other handsets; and wireless-enabled internet devices, such as tablets, and other wireless-enabled connected devices comprising smart watches. It also provides residential fixed connectivity solutions, such as internet, video, and voice services; and sells network access to mobile virtual network operators. As of December 31, 2021, it had approximately 115 million wireless retail connections, 7 million wireline broadband connections, and 4 million Fios video connections. The company's Business segment provides network connectivity products, including private networking, private cloud connectivity, virtual and software defined networking, and internet access services; and internet protocol-based voice and video services, unified communications and collaboration tools, and customer contact center solutions. This segment also offers a suite of management and data security services; domestic and global voice and data solutions, such as voice calling, messaging services, conferencing, contact center solutions, and private line and data access networks; customer premises equipment; installation, maintenance, and site services; and Internet of Things products and services. As of December 31, 2021, it had approximately 27 million wireless retail postpaid connections and 477 thousand wireline broadband connections. The company was formerly known as Bell Atlantic Corporation and changed its name to Verizon Communications Inc. in June 2000. Verizon Communications Inc. was incorporated in 1983 and is headquartered in New York, New York.",
        fullTimeEmployees=118500,
        city="New York",
        state="NY",
        trailingPE=9.4849615,
        dividendYield=0.0531,
        averageVolume=23597859,
        regularMarketOpen=51.07,
        volume=16616610,
        fiftyTwoWeekHigh=56.85,
        fiftyTwoWeekLow=45.55,
        recommendationKey="hold",
        industry="Telecom Services"
    )
    db.session.add(VZ)

    VRTX = Stock(
        name="Vertex Pharmaceuticals Incorporated",
        ticker="VRTX",
        marketCap=70216777728,
        dayHigh=289.41,
        dayLow=275.97,
        currentPrice=276.17,
        longBusinessSummary="Vertex Pharmaceuticals Incorporated, a biotechnology company, engages in developing and commercializing therapies for treating cystic fibrosis. The company markets SYMDEKO/SYMKEVI, ORKAMBI, and KALYDECO to treat patients with cystic fibrosis who have specific mutations in their cystic fibrosis transmembrane conductance regulator gene; and TRIKAFTA for the treatment of patients with CF 6 years of age or older who have at least one F508del mutation. Its pipeline includes VX-864 for the treatment of AAT deficiency, which is in Phase 2 clinical trial; VX-147 for the treatment of APOL1-mediated focal segmental glomerulosclerosis, or FSGS, and other serious kidney diseases which is in Phase 2 clinical trial; VX- 880, treatment for Type 1 Diabetes which is in Phase 1/2 clinical trial; VX-548, a NaV1.8 inhibitor for treatments of acute, neuropathic, musculoskeletal pain which is in Phase 2 clinical trial; and CTX001 for the treatment severe SCD and TDT which is in Phase 3 clinical trial. The company sells its products primarily to specialty pharmacy and specialty distributors in the United States, as well as specialty distributors and retail chains, and hospitals and clinics internationally. It has collaborations with Affinia Therapeutics, Inc.; Arbor Biotechnologies, Inc.; CRISPR Therapeutics AG.; Kymera Therapeutics, Inc.; Mammoth Biosciences, Inc.; Moderna, Inc.; Obsidian Therapeutics, Inc.; and Skyhawk Therapeutics, Inc.; as well as Ribometrix, Inc.; Genomics plc; Merck KGaA; Darmstadt, Germany, and X-Chem, Inc. Vertex Pharmaceuticals Incorporated was founded in 1989 and is headquartered in Boston, Massachusetts.",
        fullTimeEmployees=3900,
        city="Boston",
        state="MA",
        trailingPE=33.121853,
        dividendYield=None,
        averageVolume=1781803,
        regularMarketOpen=288.45,
        volume=1777912,
        fiftyTwoWeekHigh=293.17,
        fiftyTwoWeekLow=176.36,
        recommendationKey="buy",
        industry="Biotechnology"
    )
    db.session.add(VRTX)

    VFC = Stock(
        name="V.F. Corporation",
        ticker="VFC",
        marketCap=18091540480,
        dayHigh=48.14,
        dayLow=46.02,
        currentPrice=46.06,
        longBusinessSummary="V.F. Corporation, together with its subsidiaries, engages in the design, production, procurement, marketing, and distribution of branded lifestyle apparel, footwear, and related products for men, women, and children in the Americas, Europe, and the Asia-Pacific. It operates through three segments: Outdoor, Active, and Work. The company offers outdoor, merino wool and other natural fibers-based, lifestyle, and casual apparel; equipment; accessories; outdoor lifestyle, performance-based, youth culture/action sports-inspired, streetwear, and protective work footwear; handbags, luggage, backpacks, totes, and travel accessories; and work and work-inspired lifestyle apparel and footwear. It provides its products under the North Face, Timberland, Smartwool, Icebreaker, Altra, Vans, Supreme, Kipling, Napapijri, Eastpak, JanSport, Eagle Creek, Dickies, and Timberland PRO brand names. The company sells its products primarily to specialty stores, department stores, national chains, and mass merchants, as well as sells through direct-to-consumer operations, including retail stores, concession retail stores, and e-commerce sites, and other digital platforms. V.F. Corporation was founded in 1899 and is headquartered in Denver, Colorado.",
        fullTimeEmployees=27200,
        city="Denver",
        state="CO",
        trailingPE=14.762821,
        dividendYield=0.042,
        averageVolume=3333137,
        regularMarketOpen=47.81,
        volume=2620481,
        fiftyTwoWeekHigh=84.96,
        fiftyTwoWeekLow=44.17,
        recommendationKey="buy",
        industry="Apparel Manufacturing"
    )
    db.session.add(VFC)

    VICI = Stock(
        name="VICI Properties Inc.",
        ticker="VICI",
        marketCap=19182852096,
        dayHigh=31.39,
        dayLow=30.445,
        currentPrice=30.5,
        longBusinessSummary="VICI Properties is an experiential real estate investment trust that owns one of the largest portfolios of market-leading gaming, hospitality and entertainment destinations, including the world-renowned Caesars Palace. VICI Properties' national, geographically diverse portfolio consists of 29 gaming facilities comprising over 48 million square feet and features approximately 19,200 hotel rooms and more than 200 restaurants, bars and nightclubs. Its properties are leased to industry leading gaming and hospitality operators, including Caesars Entertainment, Inc., Century Casinos Inc., Hard Rock International, JACK Entertainment and Penn National Gaming, Inc. VICI Properties also owns four championship golf courses and 34 acres of undeveloped land adjacent to the Las Vegas Strip. VICI Properties' strategy is to create the nation's highest quality and most productive experiential real estate portfolio.",
        fullTimeEmployees=105,
        city="New York",
        state="NY",
        trailingPE=16.576086,
        dividendYield=0.0525,
        averageVolume=17015669,
        regularMarketOpen=30.97,
        volume=7607884,
        fiftyTwoWeekHigh=33.95,
        fiftyTwoWeekLow=26.23,
        recommendationKey="buy",
        industry="REIT—Diversified"
    )
    db.session.add(VICI)

    VMC = Stock(
        name="Vulcan Materials Company",
        ticker="VMC",
        marketCap=19025915904,
        dayHigh=147.85,
        dayLow=143.225,
        currentPrice=143.37,
        longBusinessSummary="Vulcan Materials Company, together with its subsidiaries, produces and supplies construction aggregates primarily in the United States. It operates through four segments: Aggregates, Asphalt, Concrete, and Calcium. The Aggregates segment provides crushed stones, sand and gravel, sand, and other aggregates; and related products and services that are applied in construction and maintenance of highways, streets, and other public works, as well as in the construction of housing and commercial, industrial, and other nonresidential facilities. The Asphalt Mix segment offers asphalt mix in Alabama, Arizona, California, New Mexico, Tennessee, and Texas, as well as engages in the asphalt construction paving activity in Alabama, Tennessee, and Texas. The Concrete segment provides ready-mixed concrete in California, Maryland, New Jersey, New York, Oklahoma, Pennsylvania, Texas and Virginia, and Washington D.C. The Calcium segment mines, produces, and sells calcium products for the animal feed, plastics, and water treatment industries. The company was formerly known as Virginia Holdco, Inc. and changed its name to Vulcan Materials Company. Vulcan Materials Company was founded in 1909 and is headquartered in Birmingham, Alabama.",
        fullTimeEmployees=11912,
        city="Birmingham",
        state="AL",
        trailingPE=29.560823,
        dividendYield=0.0095,
        averageVolume=793658,
        regularMarketOpen=146.56,
        volume=502078,
        fiftyTwoWeekHigh=213.65,
        fiftyTwoWeekLow=141.18,
        recommendationKey="buy",
        industry="Building Materials"
    )
    db.session.add(VMC)

    WAB = Stock(
        name="Westinghouse Air Brake Technologies Corporation",
        ticker="WAB",
        marketCap=15631311872,
        dayHigh=86.63,
        dayLow=83.51,
        currentPrice=83.67,
        longBusinessSummary="Westinghouse Air Brake Technologies Corporation provides technology-based equipment, systems, and services for the freight rail and passenger transit industries worldwide. It operates through two segments, Freight and Transit. The Freight segment manufactures and services components for new and existing freight cars and locomotives; builds new commuter locomotives; rebuilds freight locomotives; supplies railway electronics, positive train control equipment, signal design, and engineering services; and provides related heat exchange and cooling systems. It serves publicly traded railroads; leasing companies; manufacturers of original equipment, including locomotives and freight cars; and utilities. The Transit segment manufactures and services components for new and existing passenger transit vehicles, such as regional trains, high speed trains, subway cars, light-rail vehicles, and buses; refurbishes subway cars; and provides heating, ventilation, and air conditioning equipment, as well as doors for buses and subways. This segment serves public transit authorities and municipalities, leasing companies, and manufacturers of subway cars and buses. It also provides electronically controlled pneumatic braking products; railway electronics; freight car trucks; draft gears, couplers, and slack adjusters; air compressors and dryers; heat exchangers and cooling products; and track and switch products. In addition, the company offers railway braking equipment and related components; friction products; new switcher locomotives; transit locomotive and car overhaul services; and freight locomotive overhaul, modernizations, and refurbishment services. Further, it provides platform screen doors; pantographs; window assemblies; couplers; accessibility lifts and ramps for buses and subway cars; and traction motors. The company was founded in 1869 and is headquartered in Pittsburgh, Pennsylvania.",
        fullTimeEmployees=25000,
        city="Pittsburgh",
        state="PA",
        trailingPE=34.732254,
        dividendYield=0.0069,
        averageVolume=952479,
        regularMarketOpen=86.09,
        volume=856803,
        fiftyTwoWeekHigh=100.05,
        fiftyTwoWeekLow=77.61,
        recommendationKey="buy",
        industry="Railroads"
    )
    db.session.add(WAB)

    WBA = Stock(
        name="Walgreens Boots Alliance, Inc.",
        ticker="WBA",
        marketCap=35387187200,
        dayHigh=42.73,
        dayLow=40.9,
        currentPrice=40.96,
        longBusinessSummary="Walgreens Boots Alliance, Inc. operates as a pharmacy-led health and beauty retail company. It operates through two segments, the United States and International. The United States segment sells prescription drugs and an assortment of retail products, including health, wellness, beauty, personal care, consumable, and general merchandise products through its retail drugstores. It also provides central specialty pharmacy services and mail services. As of August 31, 2021, this segment operated 8,965 retail stores under the Walgreens and Duane Reade brands in the United States; and five specialty pharmacies. The International segment sells prescription drugs; and health and wellness, beauty, personal care, and other consumer products through its pharmacy-led health and beauty retail stores and optical practices, as well as through boots.com and an integrated mobile application. It also engages in pharmaceutical wholesaling and distribution business in Germany. As of August 31, 2021, this segment operated 4,031 retail stores under the Boots, Benavides, and Ahumada in the United Kingdom, Thailand, Norway, the Republic of Ireland, the Netherlands, Mexico, and Chile; and 548 optical practices, including 160 on a franchise basis. Walgreens Boots Alliance, Inc. was founded in 1901 and is based in Deerfield, Illinois.",
        fullTimeEmployees=315000,
        city="Deerfield",
        state="IL",
        trailingPE=13.965222,
        dividendYield=0.043899998,
        averageVolume=7432111,
        regularMarketOpen=41.03,
        volume=7825456,
        fiftyTwoWeekHigh=55,
        fiftyTwoWeekLow=39.14,
        recommendationKey="hold",
        industry="Pharmaceutical Retailers"
    )
    db.session.add(WBA)

    WMT = Stock(
        name="Walmart Inc.",
        ticker="WMT",
        marketCap=339439714304,
        dayHigh=125.57,
        dayLow=122.3,
        currentPrice=122.37,
        longBusinessSummary="Walmart Inc. engages in the operation of retail, wholesale, and other units worldwide. The company operates through three segments: Walmart U.S., Walmart International, and Sam's Club. It operates supercenters, supermarkets, hypermarkets, warehouse clubs, cash and carry stores, and discount stores; membership-only warehouse clubs; ecommerce websites, such as walmart.com, walmart.com.mx, walmart.ca, flipkart.com, and samsclub.com; and mobile commerce applications. The company offers grocery and consumables, which includes dairy, meat, bakery, deli, produce, dry, chilled or frozen packaged foods, alcoholic and nonalcoholic beverages, floral, snack foods, candy, other grocery items, health and beauty aids, paper goods, laundry and home care, baby care, pet supplies, and other consumable items; and health and wellness products covering pharmacy, over-the-counter drugs and other medical products, and optical and hearing services. It also provides gasoline stations and tobacco; home improvement, outdoor living, gardening, furniture, apparel, jewelry, tools and power equipment, housewares, toys, seasonal items, mattresses, and tire and battery centers; and consumer electronics and accessories, software, video games, office supplies, appliances, and third-party gift cards. In addition, the company offers fuel and financial services and related products, including money orders, prepaid cards, money transfers, and check cashing and bill payment, as well as various types of installment lending. It operates approximately 10,500 stores and various e-commerce websites under 46 banners in 24 countries. The company was formerly known as Wal-Mart Stores, Inc. and changed its name to Walmart Inc. in February 2018. The company was founded in 1945 and is based in Bentonville, Arkansas.",
        fullTimeEmployees=2300000,
        city="Bentonville",
        state="AR",
        trailingPE=43.08803,
        dividendYield=0.0150999995,
        averageVolume=9515750,
        regularMarketOpen=124.66,
        volume=4974429,
        fiftyTwoWeekHigh=160.77,
        fiftyTwoWeekLow=117.27,
        recommendationKey="buy",
        industry="Discount Stores"
    )
    db.session.add(WMT)

    WM = Stock(
        name="Waste Management, Inc.",
        ticker="WM",
        marketCap=62278889472,
        dayHigh=150.855,
        dayLow=148.56,
        currentPrice=148.88,
        longBusinessSummary="Waste Management, Inc., through its subsidiaries, provides waste management environmental services to residential, commercial, industrial, and municipal customers in North America. It offers collection services, including picking up and transporting waste and recyclable materials from where it was generated to a transfer station, material recovery facility (MRF), or disposal site; and owns, develops, and operates landfill gas-to-energy facilities in the United States, as well as owns and operates transfer stations. As of December 31, 2021, the company owned or operated 255 solid waste landfills; 5 secure hazardous waste landfills; 96 MRFs; and 340 transfer stations. It also provides materials processing and commodities recycling services; recycling brokerage services, such as managing the marketing of recyclable materials for third parties; and other strategic business solutions. In addition, the company offers construction and remediation services; services related with the disposal of fly ash, and residue generated from the combustion of coal and other fuel stocks; in-plant services comprising full-service waste management solutions and consulting services; and specialized disposal services for oil and gas exploration and production operations. The company was formerly known as USA Waste Services, Inc. and changed its name to Waste Management, Inc. in 1998. Waste Management, Inc. was incorporated in 1987 and is headquartered in Houston, Texas.",
        fullTimeEmployees=48500,
        city="Houston",
        state="TX",
        trailingPE=36.135925,
        dividendYield=0.0165,
        averageVolume=1794745,
        regularMarketOpen=150.09,
        volume=1153789,
        fiftyTwoWeekHigh=170.18,
        fiftyTwoWeekLow=138.58,
        recommendationKey="buy",
        industry="Waste Management"
    )
    db.session.add(WM)

    WAT = Stock(
        name="Waters Corporation",
        ticker="WAT",
        marketCap=20107798528,
        dayHigh=335.08,
        dayLow=327.18,
        currentPrice=329.44,
        longBusinessSummary="Waters Corporation, a specialty measurement company, provides analytical workflow solutions in Asia, the Americas, and Europe. It operates through two segments, Waters and TA. The company designs, manufactures, sells, and services high and ultra-performance liquid chromatography, as well as mass spectrometry (MS) technology systems and support products, including chromatography columns, other consumable products, and post-warranty service plans. It also designs, manufactures, sells, and services thermal analysis, rheometry, and calorimetry instruments; and develops and supplies software-based products that interface with its instruments, as well as other manufacturers' instruments. Its MS technology instruments are used in drug discovery and development comprising clinical trial testing, the analysis of proteins in disease processes, nutritional safety analysis, and environmental testing. The company offers thermal analysis, rheometry, and calorimetry instruments for use in predicting the suitability and stability of fine chemicals, pharmaceuticals, water, polymers, metals, and viscous liquids for various industrial, consumer good, and healthcare products, as well as for life science research. Its products are used by life science, pharmaceutical, biochemical, industrial, nutritional safety, environmental, academic, and governmental customers working in research and development, quality assurance, and other laboratory applications. Waters Corporation was founded in 1958 and is headquartered in Milford, Massachusetts.",
        fullTimeEmployees=7800,
        city="Milford",
        state="MA",
        trailingPE=29.519714,
        dividendYield=None,
        averageVolume=432512,
        regularMarketOpen=330.24,
        volume=371473,
        fiftyTwoWeekHigh=428.22,
        fiftyTwoWeekLow=288.32,
        recommendationKey="hold",
        industry="Diagnostics & Research"
    )
    db.session.add(WAT)

    WEC = Stock(
        name="WEC Energy Group, Inc.",
        ticker="WEC",
        marketCap=31265918976,
        dayHigh=100.15,
        dayLow=99.06,
        currentPrice=99.12,
        longBusinessSummary="WEC Energy Group, Inc., through its subsidiaries, provides regulated natural gas and electricity, and renewable and nonregulated renewable energy services in the United States. The company operates through six segments: Wisconsin, Illinois, Other States, Electric Transmission, Non-Utility Energy Infrastructure, and Corporate and Other. It generates and distributes electricity from coal, natural gas, oil, hydroelectric, wind, solar, and biomass sources; provides electric transmission services; offers retail natural gas distribution services; transports natural gas; and generates, distributes, and sells steam. As of December 31, 2021, it operated approximately 35,800 miles of overhead distribution lines and 35,600 miles of underground distribution cables, as well as 440 electric distribution substations and 510,500 line transformers; 50,900 miles of natural gas distribution mains; 1,200 miles of natural gas transmission mains; 2.3 million natural gas lateral services; 500 natural gas distribution and transmission gate stations; and 68.2 billion cubic feet of working gas capacities in underground natural gas storage fields. The company was formerly known as Wisconsin Energy Corporation and changed its name to WEC Energy Group, Inc. in June 2015. WEC Energy Group, Inc. was incorporated in 1981 and is headquartered in Milwaukee, Wisconsin.",
        fullTimeEmployees=6938,
        city="Milwaukee",
        state="WI",
        trailingPE=23.884338,
        dividendYield=0.028499998,
        averageVolume=1505208,
        regularMarketOpen=99.34,
        volume=1441765,
        fiftyTwoWeekHigh=108.39,
        fiftyTwoWeekLow=86.84,
        recommendationKey="hold",
        industry="Utilities—Regulated Electric"
    )
    db.session.add(WEC)

    WFC = Stock(
        name="Wells Fargo & Company",
        ticker="WFC",
        marketCap=160206897152,
        dayHigh=41.56,
        dayLow=40.08,
        currentPrice=40.18,
        longBusinessSummary="Wells Fargo & Company, a diversified financial services company, provides banking, investment, mortgage, and consumer and commercial finance products and services in the United States and internationally. It operates through four segments: Consumer Banking and Lending; Commercial Banking; Corporate and Investment Banking; and Wealth and Investment Management. The Consumer Banking and Lending segment offers diversified financial products and services for consumers and small businesses. Its financial products and services include checking and savings accounts, and credit and debit cards, as well as home, auto, personal, and small business lending services. The Commercial Banking segment provides financial solutions to private, family owned, and certain public companies. Its products and services include banking and credit products across various industry sectors and municipalities, secured lending and lease products, and treasury management services. The Corporate and Investment Banking segment offers a suite of capital markets, banking, and financial products and services to corporate, commercial real estate, government, and institutional clients. Its products and services comprise corporate banking, investment banking, treasury management, commercial real estate lending and servicing, equity, and fixed income solutions, as well as sales, trading, and research capabilities services. The Wealth and Investment Management segment provides personalized wealth management, brokerage, financial planning, lending, private banking, and trust and fiduciary products and services to affluent, high-net worth, and ultra-high-net worth clients. It also operates through financial advisors. Wells Fargo & Company was founded in 1852 and is headquartered in San Francisco, California.",
        fullTimeEmployees=246577,
        city="San Francisco",
        state="CA",
        trailingPE=9.584924,
        dividendYield=0.0235,
        averageVolume=25793504,
        regularMarketOpen=40.97,
        volume=17976607,
        fiftyTwoWeekHigh=60.3,
        fiftyTwoWeekLow=36.54,
        recommendationKey="buy",
        industry="Banks—Diversified"
    )
    db.session.add(WFC)

    WELL = Stock(
        name="Welltower Inc.",
        ticker="WELL",
        marketCap=36075589632,
        dayHigh=84.76,
        dayLow=82.74,
        currentPrice=82.88,
        longBusinessSummary="""Welltower Inc. (NYSE:WELL), an S&P 500 company headquartered in Toledo, Ohio, is driving the transformation of health care infrastructure. The Company invests with leading seniors housing operators, post-acute providers and health systems to fund the real estate infrastructure needed to scale innovative care delivery models and improve people's wellness and overall health care experience. Welltower, a real estate investment trust ("REIT"), owns interests in properties concentrated in major, high-growth markets in the United States, Canada and the United Kingdom, consisting of seniors housing and post-acute communities and outpatient medical properties.""",
        fullTimeEmployees=464,
        city="Toledo",
        state="OH",
        trailingPE=80.07729,
        dividendYield=0.0276,
        averageVolume=2433908,
        regularMarketOpen=83.78,
        volume=1388268,
        fiftyTwoWeekHigh=99.43,
        fiftyTwoWeekLow=76.56,
        recommendationKey="buy",
        industry="REIT—Healthcare Facilities"
    )
    db.session.add(WELL)

    WST = Stock(
        name="West Pharmaceutical Services, Inc.",
        ticker="WST",
        marketCap=21961666560,
        dayHigh=304.86,
        dayLow=296.31,
        currentPrice=296.46,
        longBusinessSummary="West Pharmaceutical Services, Inc. designs, manufactures, and sells containment and delivery systems for injectable drugs and healthcare products in the Americas, Europe, the Middle East, Africa, and the Asia Pacific. It operates in two segments, Proprietary Products and Contract-Manufactured Products. The Proprietary Products segment offers stoppers and seals for injectable packaging systems; syringe and cartridge components, including custom solutions for the needs of injectable drug applications, as well as administration systems that enhance the safe delivery of drugs through advanced reconstitution, mixing, and transfer technologies; and films, coatings, washing, and vision inspection and sterilization processes and services to enhance the quality of packaging components. It also provides drug containment solutions, including Crystal Zenith, a cyclic olefin polymer in the form of vials, syringes, and cartridges; and self-injection devices, as well as a range of integrated solutions, including analytical lab services, pre-approval primary packaging support and engineering development, regulatory expertise, and after-sales technical support. This segment serves biologic, generic, and pharmaceutical drug companies. The Contract-Manufactured Products segment is involved in the design, manufacture, and automated assembly of devices used in surgical, diagnostic, ophthalmic, injectable, and other drug delivery systems, as well as consumer products. It serves pharmaceutical, diagnostic, and medical device companies. The company distributes its products through its sales force and distribution network, as well as contract sales agents and regional distributors. West Pharmaceutical Services, Inc. was incorporated in 1923 and is headquartered in Exton, Pennsylvania.",
        fullTimeEmployees=10065,
        city="Exton",
        state="PA",
        trailingPE=36.767952,
        dividendYield=0.0023999999,
        averageVolume=453008,
        regularMarketOpen=303.51,
        volume=362267,
        fiftyTwoWeekHigh=475.35,
        fiftyTwoWeekLow=275.89,
        recommendationKey="buy",
        industry="Medical Instruments & Supplies"
    )
    db.session.add(WST)

    WDC = Stock(
        name="Western Digital Corporation",
        ticker="WDC",
        marketCap=14565260288,
        dayHigh=48.44,
        dayLow=46.64,
        currentPrice=46.74,
        longBusinessSummary="Western Digital Corporation develops, manufactures, and sells data storage devices and solutions in the United States, China, Hong Kong, Europe, the Middle East, Africa, rest of Asia, and internationally. It offers client devices, including hard disk drives (HDDs) and solid state drives (SSDs) for computing devices, such as desktop and notebook personal computers (PCs), smart video systems, gaming consoles, and set top boxes; flash-based embedded storage products for mobile phones, tablets, notebook PCs, and other portable and wearable devices, as well as automotive, Internet of Things, industrial, and connected home applications; and flash-based memory wafers. The company also provides data center devices and solutions comprising enterprise helium hard drives; enterprise SSDs consisting of flash-based SSDs and software solutions for use in enterprise servers, online transactions, data analysis, and other enterprise applications; data center solutions for data storage systems and tiered storage models; and data storage platforms. In addition, it offers client solutions, such as external HDD storage products in mobile and desktop form; client portable SSDs; removable cards that are used in consumer devices comprising mobile phones, tablets, imaging systems, and cameras and smart video systems; universal serial bus flash drives for use in the computing and consumer markets; and wireless drive products used in-field back up of created content, as well as wireless streaming of high-definition movies, photos, music, and documents to tablets, smartphones, and PCs. The company sells its products under the G-Technology, SanDisk, and WD brands to original equipment manufacturers, distributors, dealers, resellers, and retailers. Western Digital Corporation was founded in 1970 and is headquartered in San Jose, California.",
        fullTimeEmployees=65600,
        city="San Jose",
        state="CA",
        trailingPE=9.778243,
        dividendYield=None,
        averageVolume=4277250,
        regularMarketOpen=47.82,
        volume=2055888,
        fiftyTwoWeekHigh=72.15,
        fiftyTwoWeekLow=43.85,
        recommendationKey="buy",
        industry="Computer Hardware"
    )
    db.session.add(WDC)

    WRK = Stock(
        name="WestRock Company",
        ticker="WRK",
        marketCap=10607708160,
        dayHigh=41.8,
        dayLow=40.28,
        currentPrice=40.32,
        longBusinessSummary="WestRock Company, together with its subsidiaries, provides fiber-based paper and packaging solutions in North America, South America, Europe, Asia, and Australia. It operates through two segments, Corrugated Packaging and Consumer Packaging. The Corrugated Packaging segment produces containerboards, corrugated sheets, corrugated packaging, and preprinted linerboards to consumer and industrial products manufacturers, and corrugated box manufacturers. It also provides structural and graphic design, engineering services and custom, and proprietary and standard automated packaging machines, as well as turn-key installation, automation, line integration, and packaging solutions; distributes corrugated packaging materials and other specialty packaging products, including stretch films, void fills, carton sealing tapes, and other specialty tapes; operates recycling facilities that collect, sort, grade, and bale recovered paper; and provides lithographic laminated packaging products, as well as contract packing services. The Consumer Packaging segment manufactures and sells folding cartons that are used to package food, paper, beverages, dairy products, tobacco, confectionery, health and beauty, other household consumer, and commercial and industrial products; and express mail packages for the overnight courier industry. It also offers inserts and labels, as well as rigid packaging and other printed packaging products, such as transaction cards, brochures, product literature, marketing materials, and grower tags and plant stakes for the horticultural market; and secondary packages and paperboard packaging for over-the-counter and prescription drugs. In addition, this segment manufactures and sells solid fiber and corrugated partitions, and die-cut paperboard components principally to glass container manufacturers and the automotive industry, as well as producers of beer, food, wine, spirits, cosmetics, and pharmaceuticals. WestRock Company is based in Atlanta, Georgia.",
        fullTimeEmployees=50000,
        city="Atlanta",
        state="GA",
        trailingPE=12.881788,
        dividendYield=0.0216,
        averageVolume=2379890,
        regularMarketOpen=41.38,
        volume=1848536,
        fiftyTwoWeekHigh=54.78,
        fiftyTwoWeekLow=38.4,
        recommendationKey="buy",
        industry="Packaging & Containers"
    )
    db.session.add(WRK)

    WY = Stock(
        name="Weyerhaeuser Company",
        ticker="WY",
        marketCap=25010612224,
        dayHigh=34.26,
        dayLow=33.3,
        currentPrice=33.39,
        longBusinessSummary="Weyerhaeuser Company, one of the world's largest private owners of timberlands, began operations in 1900. We own or control approximately 11 million acres of timberlands in the U.S. and manage additional timberlands under long-term licenses in Canada. We manage these timberlands on a sustainable basis in compliance with internationally recognized forestry standards. We are also one of the largest manufacturers of wood products in North America. Our company is a real estate investment trust. In 2020, we generated $7.5 billion in net sales and employed approximately 9,400 people who serve customers worldwide. We are listed on the Dow Jones Sustainability North America Index. Our common stock trades on the New York Stock Exchange under the symbol WY.",
        fullTimeEmployees=9200,
        city="Seattle",
        state="WA",
        trailingPE=10.084566,
        dividendYield=0.0186,
        averageVolume=4558435,
        regularMarketOpen=34.17,
        volume=3552699,
        fiftyTwoWeekHigh=43.04,
        fiftyTwoWeekLow=32.58,
        recommendationKey="buy",
        industry="REIT—Specialty"
    )
    db.session.add(WY)

    WHR = Stock(
        name="Whirlpool Corporation",
        ticker="WHR",
        marketCap=9781460992,
        dayHigh=165.99,
        dayLow=160.8,
        currentPrice=161.03,
        longBusinessSummary="Whirlpool Corporation manufactures and markets home appliances and related products. It operates through four segments: North America; Europe, Middle East and Africa; Latin America; and Asia. The company's principal products include refrigerators, freezers, ice makers, and refrigerator water filters; laundry appliances and related laundry accessories; cooking and other small domestic appliances; and dishwasher appliances and related accessories, as well as mixers. It markets and distributes its products primarily under the Whirlpool, Maytag, KitchenAid, JennAir, Amana, Roper, Affresh, Gladiator, Swash, everydrop, Speed Queen, Hotpoint, Bauknecht, Indesit, Ignis, Privileg, Consul, Eslabon de Lujo, Brastemp, Acros, Ariston, Diqua, and Royalstar brands. The company sells its products to retailers, distributors, dealers, builders, and other manufacturers, as well as directly to consumers. Whirlpool Corporation was founded in 1911 and is headquartered in Benton Harbor, Michigan.",
        fullTimeEmployees=69000,
        city="Benton Harbor",
        state="MI",
        trailingPE=5.136359,
        dividendYield=0.0383,
        averageVolume=1171664,
        regularMarketOpen=164.63,
        volume=745664,
        fiftyTwoWeekHigh=245.44,
        fiftyTwoWeekLow=145.93,
        recommendationKey="hold",
        industry="Furnishings, Fixtures & Appliances"
    )
    db.session.add(WHR)

    WMB = Stock(
        name="The Williams Companies, Inc.",
        ticker="WMB",
        marketCap=38565052416,
        dayHigh=31.945,
        dayLow=31.2,
        currentPrice=31.74,
        longBusinessSummary="The Williams Companies, Inc., together with its subsidiaries, operates as an energy infrastructure company primarily in the United States. It operates through Transmission & Gulf of Mexico, Northeast G&P, West, and Gas & NGL Marketing Services segments. The Transmission & Gulf of Mexico segment comprises Transco and Northwest natural gas pipelines; and natural gas gathering and processing, and crude oil production handling and transportation assets in the Gulf Coast region, as well as various petrochemical and feedstock pipelines. The Northeast G&P segment engages in the midstream gathering, processing, and fractionation activities in the Marcellus Shale region primarily in Pennsylvania and New York, and the Utica Shale region of eastern Ohio. The West segment comprises gas gathering, processing, and treating operations in the Rocky Mountain region of Colorado and Wyoming, the Barnett Shale region of north-central Texas, the Eagle Ford Shale region of South Texas, the Haynesville Shale region of northwest Louisiana, and the Mid-Continent region, which includes the Anadarko, Arkoma, and Permian basins; and operates natural gas liquid (NGL) fractionation and storage facilities in central Kansas near Conway. The Gas & NGL Marketing Services segment provides wholesale marketing, trading, storage, and transportation of natural gas for natural gas utilities, municipalities, power generators, and producers; risk and asset management; and NGL marketing services. The company owns and operates 30,000 miles of pipelines, 29 processing facilities, 7 fractionation facilities, and approximately 23 million barrels of NGL storage capacity. The Williams Companies, Inc. was founded in 1908 and is headquartered in Tulsa, Oklahoma.",
        fullTimeEmployees=4783,
        city="Tulsa",
        state="OK",
        trailingPE=38.707317,
        dividendYield=0.048899997,
        averageVolume=8881904,
        regularMarketOpen=31.24,
        volume=9849761,
        fiftyTwoWeekHigh=37.97,
        fiftyTwoWeekLow=23.53,
        recommendationKey="buy",
        industry="Oil & Gas Midstream"
    )
    db.session.add(WMB)

    GWW = Stock(
        name="W.W. Grainger, Inc.",
        ticker="GWW",
        marketCap=23217487872,
        dayHigh=468.19,
        dayLow=449.77,
        currentPrice=450.65,
        longBusinessSummary="W.W. Grainger, Inc. distributes maintenance, repair, and operating (MRO) products and services in the United States, Japan, Canada, the United Kingdom, and internationally. The company operates through two segments, High-Touch Solutions N.A. and Endless Assortment. It offers safety and security supplies, material handling and storage equipment, pumps and plumbing equipment, cleaning and maintenance supplies, and metalworking and hand tools. It also offers inventory management and technical support services. The company serves businesses, corporations, government entities, and other institutions through sales and service representatives, and electronic and ecommerce channels. W.W. Grainger, Inc. was founded in 1927 and is headquartered in Lake Forest, Illinois.",
        fullTimeEmployees=22700,
        city="Lake Forest",
        state="IL",
        trailingPE=25.758787,
        dividendYield=0.014400001,
        averageVolume=305156,
        regularMarketOpen=464.89,
        volume=311469,
        fiftyTwoWeekHigh=529.91,
        fiftyTwoWeekLow=391.16,
        recommendationKey="hold",
        industry="Industrial Distribution"
    )
    db.session.add(GWW)

    XEL = Stock(
        name="Xcel Energy Inc.",
        ticker="XEL",
        marketCap=37701931008,
        dayHigh=70.41,
        dayLow=69.27,
        currentPrice=69.99,
        longBusinessSummary="Xcel Energy Inc., through its subsidiaries, generates, purchases, transmits, distributes, and sells electricity. It operates through Regulated Electric Utility, Regulated Natural Gas Utility, and All Other segments. The company generates electricity through coal, nuclear, natural gas, hydroelectric, solar, biomass, oil, wood/refuse, and wind energy sources. It also purchases, transports, distributes, and sells natural gas to retail customers, as well as transports customer-owned natural gas. In addition, the company develops and leases natural gas pipelines, and storage and compression facilities; and invests in rental housing projects, as well as procures equipment for the construction of renewable generation facilities. It serves residential, commercial, and industrial customers in the portions of Colorado, Michigan, Minnesota, New Mexico, North Dakota, South Dakota, Texas, and Wisconsin. The company sells electricity to approximately 3.7 million customers; and natural gas to approximately 2.1 million customers. Xcel Energy Inc. was incorporated in 1909 and is headquartered in Minneapolis, Minnesota.",
        fullTimeEmployees=11321,
        city="Minneapolis",
        state="MN",
        trailingPE=23.936388,
        dividendYield=0.026199998,
        averageVolume=3330216,
        regularMarketOpen=69.47,
        volume=4182088,
        fiftyTwoWeekHigh=76.63,
        fiftyTwoWeekLow=61.16,
        recommendationKey="buy",
        industry="Utilities—Regulated Electric"
    )
    db.session.add(XEL)

    XYL = Stock(
        name="Xylem Inc.",
        ticker="XYL",
        marketCap=14047316992,
        dayHigh=80.47,
        dayLow=77.77,
        currentPrice=77.9,
        longBusinessSummary="Xylem Inc., together with its subsidiaries, engages in the design, manufacture, and servicing of engineered products and solutions for the water and wastewater applications in the United States, Europe, the Asia Pacific, and internationally. It operates through three segments: Water Infrastructure, Applied Water, and Measurement & Control Solutions. The Water Infrastructure segment offers various products, including water, storm water, and wastewater pumps; controls and systems; filtration, disinfection, and biological treatment equipment; and mobile dewatering equipment under the Flygt, Godwin, Wedeco, Sanitaire, Leopold, Wedeco, and Xylem Vue brand names for the transportation and treatment of water. The Applied Water segment provides pumps, valves, heat exchangers, controls, and dispensing equipment systems under the Goulds Water Technology, Bell & Gossett, A-C Fire Pump, Standard Xchange, Lowara, Jabsco, Xylem Vue and Flojet brand names for residential and commercial building services, and industrial water applications. The Measurement & Control Solutions segment provides smart meters, networked communication devices, and measurement and control technologies, as well as critical infrastructure technologies. It also offers software and services, including cloud-based analytics, remote monitoring and data management, leak detection, condition assessment, asset management, and pressure monitoring solutions, as well as testing equipment and managed services. This segment sells its products under the Pure, Sensus, Smith Blair, WTW, Xylem Vue, and YSI brand names. The company markets and sells its products through a network of direct sales force, resellers, distributors, and value-added solution providers. Xylem Inc. was formerly known as ITT WCO, Inc. and changed its name to Xylem Inc. in May 2011. The company. was incorporated in 2011 and is headquartered in Rye Brook, New York.",
        fullTimeEmployees=16100,
        city="Rye Brook",
        state="NY",
        trailingPE=30.561005,
        dividendYield=0.0143,
        averageVolume=1190219,
        regularMarketOpen=79.53,
        volume=768441,
        fiftyTwoWeekHigh=138.78,
        fiftyTwoWeekLow=72.08,
        recommendationKey="hold",
        industry="Specialty Industrial Machinery"
    )
    db.session.add(XYL)

    YUM = Stock(
        name="Yum! Brands, Inc.",
        ticker="YUM",
        marketCap=33264732160,
        dayHigh=118.03,
        dayLow=113.13,
        currentPrice=113.48,
        longBusinessSummary="YUM! Brands, Inc., together with its subsidiaries, develops, operates, and franchises quick service restaurants worldwide. It operates through four segments: the KFC Division, the Taco Bell Division, the Pizza Hut Division, and the Habit Burger Grill Division. The company operates restaurants under the KFC, Pizza Hut, Taco Bell, and The Habit Burger Grill brands, which specialize in chicken, pizza, made-to-order chargrilled burgers, sandwiches, Mexican-style food categories, and other food products. As of December 31, 2021, it had 26,934 KFC units; 18,381 Pizza Hut units; 7,791 Taco Bell units; and 318 The Habit Burger Grill units in approximately 157 countries and territories. The company was formerly known as TRICON Global Restaurants, Inc. and changed its name to YUM! Brands, Inc. in May 2002. YUM! Brands, Inc. was incorporated in 1997 and is headquartered in Louisville, Kentucky.",
        fullTimeEmployees=36000,
        city="Louisville",
        state="KY",
        trailingPE=21.915798,
        dividendYield=0.0202,
        averageVolume=1776848,
        regularMarketOpen=117.28,
        volume=983021,
        fiftyTwoWeekHigh=139.85,
        fiftyTwoWeekLow=108.37,
        recommendationKey="buy",
        industry="Restaurants"
    )
    db.session.add(YUM)

    ZBRA = Stock(
        name="Zebra Technologies Corporation",
        ticker="ZBRA",
        marketCap=16150555648,
        dayHigh=312.99,
        dayLow=301.42,
        currentPrice=302.21,
        longBusinessSummary="Zebra Technologies Corporation, together with its subsidiaries, provides enterprise asset intelligence solutions in the automatic identification and data capture solutions industry worldwide. It operates in two segments, Asset Intelligence & Tracking and Enterprise Visibility & Mobility. The company designs, manufactures, and sells printers, which produce labels, wristbands, tickets, receipts, and plastic cards; dye-sublimination thermal card printers, which produce images which are used for personal identification, access control, and financial transactions; RFID printers that encode data into passive RFID transponders; accessories and options for our printers, including vehicle mounts and battery chargers; stock and customized thermal labels, receipts, ribbons, plastic cards, and RFID tags for printers; and temperature-monitoring labels primarily used in vaccine distribution. It also provides various maintenance, technical support, repair, and managed and professional services; real-time location systems and services; and tags, sensors, exciters, middleware software, and application software; as well as physical inventory management solutions, and rugged tablets and enterprise-grade mobile computing products and accessories. In addition, the company offers barcode scanners, image capture devices, and RFID readers; and workforce management solutions, workflow execution and task management solutions, and prescriptive analytics solutions, as well as communications and collaboration solutions. It also provides services, including maintenance, technical support, repair, managed and professional services; as well as cloud-based software subscriptions and robotics automation solutions. The company serves retail and e-commerce, manufacturing, transportation and logistics, healthcare, public sector, and other industries through direct sales force, and network of channel partners. The company was founded in 1969 and is headquartered in Lincolnshire, Illinois.",
        fullTimeEmployees=9800,
        city="Lincolnshire",
        state="IL",
        trailingPE=19.26868,
        dividendYield=None,
        averageVolume=489027,
        regularMarketOpen=309.87,
        volume=264425,
        fiftyTwoWeekHigh=615,
        fiftyTwoWeekLow=287.93,
        recommendationKey="buy",
        industry="Communication Equipment"
    )
    db.session.add(ZBRA)

    ZBH = Stock(
        name="Zimmer Biomet Holdings, Inc.",
        ticker="ZBH",
        marketCap=22244524032,
        dayHigh=110.31,
        dayLow=106.38,
        currentPrice=106.48,
        longBusinessSummary="Zimmer Biomet Holdings, Inc., together with its subsidiaries, operates in the musculoskeletal healthcare business in the Americas, Europe, the Middle East, Africa, and the Asia Pacific. The company designs, manufactures, and markets orthopaedic reconstructive products, such as knee and hip products; S.E.T. products, including sports medicine, biologics, foot and ankle, extremities, and trauma products; spine products comprising medical devices and surgical instruments; and face and skull reconstruction products, as well as products that fixate and stabilize the bones of the chest toss facilitate healing or reconstruction after open heart surgery, trauma, or for deformities of the chest. It also offers dental products that include dental reconstructive implants, and dental prosthetic and regenerative products, as well as robotic, surgical and bone cement products. The company's products and solutions are used to treat patients suffering from disorders of, or injuries to, bones, joints, or supporting soft tissues. It serves orthopedic surgeons, neurosurgeons, oral surgeons, dentists, hospitals, stocking distributors, healthcare dealers, and other specialists, as well as agents, healthcare purchasing organizations, or buying groups. The company was formerly known as Zimmer Holdings, Inc. and changed its name to Zimmer Biomet Holdings, Inc. in June 2015. Zimmer Biomet Holdings, Inc. was founded in 1927 and is headquartered in Warsaw, Indiana.",
        fullTimeEmployees=19500,
        city="Warsaw",
        state="IN",
        trailingPE=27.204906,
        dividendYield=0.0083,
        averageVolume=1356658,
        regularMarketOpen=109,
        volume=787944,
        fiftyTwoWeekHigh=160.58252,
        fiftyTwoWeekLow=101.22,
        recommendationKey="hold",
        industry="Medical Devices"
    )
    db.session.add(ZBH)

    ZION = Stock(
        name="Zions Bancorporation, National Association",
        ticker="ZION",
        marketCap=8244035584,
        dayHigh=53.91,
        dayLow=52.61,
        currentPrice=52.69,
        longBusinessSummary="Zions Bancorporation, National Association provides various banking and related services primarily in the states of Arizona, California, Colorado, Idaho, Nevada, New Mexico, Oregon, Texas, Utah, Washington, and Wyoming. The company offers corporate banking services; commercial banking, including a focus on small- and medium-sized businesses; commercial real estate banking services; municipal and public finance services; retail banking, including residential mortgages; trust services; wealth management and private client banking services; and capital markets products and services. As of December 31, 2020, it operated 422 branches, which included 273 owned and 149 leased. The company was formerly known as ZB, National Association and changed its name to Zions Bancorporation, National Association in September 2018. Zions Bancorporation, National Association was founded in 1873 and is headquartered in Salt Lake City, Utah.",
        fullTimeEmployees=9724,
        city="Salt Lake City",
        state="UT",
        trailingPE=7.444193,
        dividendYield=0.028399998,
        averageVolume=1542945,
        regularMarketOpen=53.32,
        volume=631969,
        fiftyTwoWeekHigh=75.44,
        fiftyTwoWeekLow=47.06,
        recommendationKey="buy",
        industry="Banks—Regional"
    )
    db.session.add(ZION)

    ZTS = Stock(
        name="Zoetis Inc.",
        ticker="ZTS",
        marketCap=80488194048,
        dayHigh=174.67,
        dayLow=170.01,
        currentPrice=170.12,
        longBusinessSummary="Zoetis Inc. discovers, develops, manufactures, and commercializes animal health medicines, vaccines, and diagnostic products in the United States and internationally. It commercializes products primarily across species, including livestock, such as cattle, swine, poultry, fish, and sheep; and companion animals comprising dogs, cats, and horses. The company also offers vaccines, which are biological preparations to prevent diseases of the respiratory, gastrointestinal, and reproductive tracts or induce a specific immune response; anti-infectives that prevent, kill, or slow the growth of bacteria, fungi, or protozoa; and parasiticides that prevent or eliminate external and internal parasites, which include fleas, ticks, and worms. It also provides other pharmaceutical products that comprise pain and sedation, antiemetic, reproductive, and oncology products; dermatology products for itch associated with allergic conditions and atopic dermatitis; and medicated feed additives, which offer medicines to livestock. In addition, the company provides portable blood and urine analysis testing, including point-of-care diagnostic products, instruments and reagents, rapid immunoassay tests, reference laboratory kits and services, and blood glucose monitors; and other non-pharmaceutical products, including nutritionals and agribusiness services, as well as products and services in areas, such as biodevices, genetics tests, and precision animal health. It markets its products to veterinarians, livestock producers, and retail outlets, as well as third-party veterinary distributors through its sales representatives, and technical and veterinary operations specialists. The company was founded in 1952 and is headquartered in Parsippany, New Jersey.",
        fullTimeEmployees=12100,
        city="Parsippany",
        state="NJ",
        trailingPE=41.002647,
        dividendYield=0.007900001,
        averageVolume=2229877,
        regularMarketOpen=172.96,
        volume=1605779,
        fiftyTwoWeekHigh=249.27,
        fiftyTwoWeekLow=154.18,
        recommendationKey="buy",
        industry="Drug Manufacturers—Specialty & Generic"
    )
    db.session.add(ZTS)




    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_stocks():
    db.session.execute('TRUNCATE stocks RESTART IDENTITY CASCADE;')
    db.session.commit()
