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





    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_stocks():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
