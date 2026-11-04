# 06 来源索引：Wave4 当前身份/区间复核 + 原历史文献证据

**R04（round-p4-final-2026-10-30）覆盖口径，取代 Wave4 的“66/103 + 37 NOT_PROVEN”。**
截至 2026-10-30，103 本来源逐书原版与阅读版 SHA 匹配，并二次核对工作区材料 manifest.yaml 103/103（P1）。
**P2：103/103 均有连续区间级阅读证据**，分三档：① 87 份由历史 `## L起-止` / `- 块N L起-止` 分块台账连续覆盖；② 6 份由本轮 Read 实读补齐并通过 `kd32_ledger_gate.py` 核验（PG39576 / PG5978 / PG63483 / PG1142 / PG33148 / PG50975，共 9,636 行）；③ 10 份以 Markdown 表格、共享台账分片或自报分片形式存在（PG1752 / PG47901 / PG51127 / PG525 / PG1918 / PG91 / PG32328 / PG35443 / PG53607 / PG62010），本轮已逐本打开核对格式与自述状态，可信但门禁不能解析，不计入门禁通过数。
下表第四列是 **Wave4 当时的机器识别结果**，保留作历史追溯；**当前结论以本文件 R04 表的“R04 状态”列为准**。历史旧表中的 FULL/PARTIAL/SCAN 是 R01/R02 当时的文献使用程度，不能充当当前 P2 结论。

| Source ID | 固定作者 / 作品 | 阅读版 SHA-256 | 本轮连续台账核验 |
|---|---|---|---|
| PG1083 | Conrad, Joseph, 1857-1924 / The Arrow of Gold: A Story Between Two Notes | 26e586b00ec73c36a0c86a6f69807b2cc6030ea7679b4847c8492ca3eefc7d03 | FULL_COVERAGE_LEDGER |
| PG1142 | Conrad, Joseph, 1857-1924 / Typhoon | 9cb80a12212978cc04ecca481eaa4b5991629a0de8a9d5b8706b1a7684d82f6a | PARTIAL_OR_MISSING_LEDGER |
| PG13740 | Libbey, Laura Jean, 1862-1924 / Mischievous Maid Faynie | e152c926d94324acf4c1a0fd1fcd51b8f7aa8ee4466432bbc816d4dd56611cad | FULL_COVERAGE_LEDGER |
| PG1401 | Burroughs, Edgar Rice, 1875-1950 / Tarzan the Untamed | 3a205447e0160f3a672720629b06f54af977cc792073c5f5eedfa5cda1cdc5ca | FULL_COVERAGE_LEDGER |
| PG14096 | Carter, Nicholas (House name) / With Links of Steel; Or, The Peril of the Unknown | 7f0d0f5ad64d290a47eae147afb68a07ac71bc22dca73f75bf59d5901175f252 | FULL_COVERAGE_LEDGER |
| PG15979 | Rathborne, St. George, 1854-1938 / Miss Caprice | 93794dbbd6a33ce5a2ad1122aef463362179282938a6f757b33b09881e9f600e | FULL_COVERAGE_LEDGER |
| PG1730 | London, Jack, 1876-1916 / Michael, Brother of Jerry | 723fb6011e51359611d60f8eba29a59719f4e41005b4190ea8ae1886d75a9261 | FULL_COVERAGE_LEDGER |
| PG1752 | Orczy, Emmuska Orczy, Baroness, 1865-1947 / El Dorado: An Adventure of the Scarlet Pimpernel | 6ce801d89566424c1136bea11da9b3d4d48d0d7493c4e4baa38c1a9adcf43353 | PARTIAL_OR_MISSING_LEDGER (覆盖 43.93%) |
| PG1918 | Haggard, H. Rider (Henry Rider), 1856-1925 / Long Odds | 3a63f62b54e6d64511bdc519df941dcf9bb8b583c6c985ef78d25b3fba523bbf | PARTIAL_OR_MISSING_LEDGER |
| PG19901 | Williamson, A. M. (Alice Muriel), 1869-1933 / The Castle Of The Shadows | a3dcb624abd55f2b400b572e5647e1ee1750f22b02df7ff8cdc6e8349a692d86 | FULL_COVERAGE_LEDGER |
| PG2020 | Burroughs, Edgar Rice, 1875-1950 / Tarzan the Terrible | 4a9ba7721ee2a782ded18109fcec5e874c8fcbfd3359e508d4b3aeceae5b59c5 | FULL_COVERAGE_LEDGER |
| PG2377 | London, Jack, 1876-1916 / The Son of the Wolf | df3e6651b829a21a8528dccd47c699aa1c8dc849efe12f4c5becfae1ceac12f0 | FULL_COVERAGE_LEDGER |
| PG26925 | Doughty, Francis Worcester, 1850-1917 / The Bradys Beyond Their Depth; Or, The Great Swamp Mystery | e6351e9e7fbd2430c1405a97d3a8f30fceb66ffbc458630e384856b203e14e8a | FULL_COVERAGE_LEDGER |
| PG27621 | Duchess, 1855?-1897 / How I write my novels | ce5fc4a10ca29fa80b3b0a59b9430bde550a8cfff34d99d743c26686e1eefd55 | PARTIAL_OR_MISSING_LEDGER |
| PG27622 | Duchess, 1855?-1897 / The story of my first novel; How a novel is written | d9040e5538bfa201484a4b55d6212756c8afd3d3877530e874aef4c51cc6a830 | PARTIAL_OR_MISSING_LEDGER |
| PG29544 | Libbey, Laura Jean, 1862-1924 / Jolly Sally Pendleton; Or, the Wife Who Was Not a Wife | 28fdf4fff1282ac073601ffb0af01ce1d01224270ad0653462b6a2d33eaa4b53 | FULL_COVERAGE_LEDGER |
| PG30137 | Libbey, Laura Jean, 1862-1924 / Daisy Brooks; Or, A Perilous Love | 3e6e2eaf6c24987eb12029697ba0668d59f18f1ad34e72b457b166c66cf9af0a | FULL_COVERAGE_LEDGER |
| PG32328 | Erichsen, Hugo, 1860-1944 / Methods of Authors | 9d7fb50877fc5637118c9603d88203f23993d6db198d8ab22a2934a8a05b5137 | PARTIAL_OR_MISSING_LEDGER |
| PG331 | Burroughs, Edgar Rice, 1875-1950 / The Mucker | f2a11f5fc4c91932d01c9c433df892841865b69d13c13ac079fb12261cbc2434 | FULL_COVERAGE_LEDGER |
| PG33148 | Various / My First Book: the experiences of Walter Besant, James Payn, W. Clark Russell, Grant Allen, Hall Caine, George R. Sims, Rudyard Kipling, A. Conan Doyle, M.E. Braddon, F.W. Robinson, H. Rider Haggard, R.M. Ballantyne, I. Zangwill, Morley Roberts, David Christie Murray, Marie Corelli, Jerome K. Jerome, John Strange Winter, Bret Harte, "Q.", Robert Buchanan, Robert Louis Stevenson, with an introduction by Jerome K. Jerome. | d5affc090169493661b58e460610ea8c0325678b5b64ee3e9ebee4fe585cd973 | PARTIAL_OR_MISSING_LEDGER (覆盖 97.63%) |
| PG35443 | Reid, Mayne, 1818-1883 / Lost Lenore: The Adventures of a Rolling Stone | 32f61852ed166ae2260e82ca6e934ed9b94e51200d6233487a365051c3078fbb | PARTIAL_OR_MISSING_LEDGER |
| PG37092 | Doughty, Francis Worcester, 1850-1917 / The Bradys' Chinese Clew; Or, The Secret Dens of Pell Street | 9470c9994ab06133104fb236bfc4ff5e4576117daa0002bfae4ea989dda838e7 | PARTIAL_OR_MISSING_LEDGER |
| PG39576 | Verrill, A. Hyatt (Alpheus Hyatt), 1871-1954 / The Radio Detectives | 00ba6e8f0fa35d4233e10f77302f0e8f1a7be5ba8d247e1aa701e655690f4300 | PARTIAL_OR_MISSING_LEDGER |
| PG41078 | Le Queux, William, 1864-1927 / The Hunchback of Westminster | c1e2f25ec204837fd8f5d48d3a689855e1c7382a4958861343836d0f8d84064d | FULL_COVERAGE_LEDGER |
| PG42545 | Verrill, A. Hyatt (Alpheus Hyatt), 1871-1954 / The Radio Detectives in the Jungle | cb8138c4d3c71e433ff336a1bb885702e31549ef5d4fda6a920c28c17b10dc6b | FULL_COVERAGE_LEDGER |
| PG42569 | Verrill, A. Hyatt (Alpheus Hyatt), 1871-1954 / The Radio Detectives Under the Sea | 95bd44f5ce1a373e428106380db14effc703d90c92a440f2730b346fd936aecc | PARTIAL_OR_MISSING_LEDGER (覆盖 99.69%) |
| PG43298 | MacLaren, Gordon / The Riddle and the Ring; or, Won by Nerve | e7b216e13aa3b8b5db458c02afdc0b1e19eb23b2ca42f47ba9afc7f61163ccdf | FULL_COVERAGE_LEDGER |
| PG43301 | Ingraham, Prentiss, 1843-1904 / Wizard Will, the wonder worker | ffbbb38978fb31ac8b2267d92614cd2311b902acc7f2422a0e98be2b6eaea61c | FULL_COVERAGE_LEDGER |
| PG43765 | Old Sleuth, 1839?-1898 / The Twin Ventriloquists; or, Nimble Ike and Jack the Juggler A Tale of Strategy and Jugglery | 7fae944b827ecf9b4bfcd277021e3279891aae6f29e6db228b6a6b45499bf2de | PARTIAL_OR_MISSING_LEDGER |
| PG45455 | Howard, Police Captain / Shadow, the Mysterious Detective | 6a2ff45f65fed0bc9112e8e4b353babcb375e263fd11da5aeec9d958a4137356 | FULL_COVERAGE_LEDGER |
| PG45492 | Raymond, P. T. / Bats in the Wall; or, The Mystery of Trinity Church-yard | 5bbc289c9af2e4d3d557e43fc17c30077dc42d999316ac577e3f48f142819e18 | FULL_COVERAGE_LEDGER |
| PG45636 | Oppenheim, E. Phillips (Edward Phillips), 1866-1946 / Stolen Idols | 1850b96f32e017404a883ffe879fb7a594b8d64dee4a7e505e5d8f6d6ec81fdc | FULL_COVERAGE_LEDGER |
| PG47071 | Matthews, Stanley R. / Motor Matt's "Century" Run; or, The Governor's Courier | df11ef11d1ebb662d3106e6ef39fb48760dcfcfdfb03dae21adfa1a3e7fab591 | FULL_COVERAGE_LEDGER |
| PG47087 | Matthews, Stanley R. / Motor Matt's Race; or, The Last Flight of the Comet | 8ebf7a759cb1edbabeef4de8155c623f014ca9fda9d6bca3da5c22bfce71046b | FULL_COVERAGE_LEDGER |
| PG47179 | Matthews, Stanley R. / Motor Matt's Mystery; or, Foiling a Secret Plot | 9fd27cc0abf3997f46b35e1d85f8abd35db9d94a21c8ae6a36551cc720968dd5 | PARTIAL_OR_MISSING_LEDGER |
| PG47455 | William Wallace Cook / The Fiction Factory | 1d8383eb0ce921eaaec811486415dc3462c6e0c190ae02df820fe01529f5a007 | FULL_COVERAGE_LEDGER |
| PG47625 | Matthews, Stanley R. / Motor Matt's Clue; or, The Phantom Auto | bf5bef75f4cabf247baf2f961ac97efdc464f980f17f06f1df0ec9fd6840e2a1 | FULL_COVERAGE_LEDGER |
| PG47788 | Matthews, Stanley R. / Motor Matt's Triumph; or, Three Speeds Forward | 2e46bd71c83a76dbb7e4f2c48427760b3871d019306020fe53888d8f2fe5863c | FULL_COVERAGE_LEDGER |
| PG47901 | Matthews, Stanley R. / Motor Matt's Air Ship; or, The Rival Inventors | 70fc540988df9fca87e19c002520bea81cdf9ef2bb6488429800a56fc0991d65 | PARTIAL_OR_MISSING_LEDGER |
| PG47975 | Matthews, Stanley R. / Motor Matt's Hard Luck; or, The Balloon-House Plot | 84513b45026a49c0298883d0d2a52be6da7bb7097764c27472ff8f7147885b00 | PARTIAL_OR_MISSING_LEDGER |
| PG481 | Michelson, Miriam, 1870-1942 / In the Bishop's Carriage | 460c5ccf9b0dc56c5070c9fabfbb5523d2456466c8591dac8f967c26f24290bb | FULL_COVERAGE_LEDGER |
| PG48252 | Matthews, Stanley R. / Motor Matt's Daring Rescue; or, The Strange Case of Helen Brady | 615e38cc9f3d38443400fed12756b500593402d5fd8d8de1b6fd070693548104 | PARTIAL_OR_MISSING_LEDGER |
| PG48524 | Matthews, Stanley R. / Motor Matt's Queer Find; or, The Secret of the Iron Chest | ee63c42f2c8bc5fae16783633060eb091c77e6a48eb4d4df58a2af6073f93294 | FULL_COVERAGE_LEDGER |
| PG48591 | Matthews, Stanley R. / Motor Matt's Promise; or, The Wreck of the Hawk | 09cab4037b67662dddfe6c150da42aa7db7b77d16e7516b3de250b100e5d631d | FULL_COVERAGE_LEDGER |
| PG49197 | Matthews, Stanley R. / Motor Matt's Submarine; or, The Strange Cruise of the Grampus | d41bd1dbe876fe55038fc5a93d9e2b00c4f2b26a450798956329dbee99dbaacd | FULL_COVERAGE_LEDGER |
| PG49638 | Senarens, Luis, 1863-1939 / Frank Reade and His Steam Horse | ff468a7ff060578b66b5bc6efa54fa8e8c104c65b5a3e3f26d18faa3a00107f6 | PARTIAL_OR_MISSING_LEDGER (覆盖 99.79%) |
| PG49644 | Matthews, Stanley R. / Motor Matt's Quest; or Three Chums in Strange Waters | f7576a8b42cdab87d3cc58901bf54d340a027f8d549a951b3a16e8619deee3c3 | FULL_COVERAGE_LEDGER |
| PG49695 | Matthews, Stanley R. / Motor Matt's Close Call; or, The Snare of Don Carlos | 12d749d387028c1834182dbfb4521f71c56455deefbbc1d75b0d96b54e1faff9 | FULL_COVERAGE_LEDGER |
| PG49746 | Matthews, Stanley R. / Motor Matt in Brazil; or, Under The Amazon | 504d246865282504b545a61e91284f81875f1145fb454248457edf288176c588 | PARTIAL_OR_MISSING_LEDGER |
| PG49937 | Matthews, Stanley R. / Motor Matt's Defiance; or, Around the Horn | 92e4680fd46ff8a0cb423081f5dad57e66f379ea1cdb937532cc53c4d1c29076 | PARTIAL_OR_MISSING_LEDGER |
| PG50080 | Matthews, Stanley R. / Motor Matt Makes Good; or, Another Victory For the Motor Boys | e3d4c3119b3afc518e89c54ab0f6eb0a0d3d5aba31b5372202361f9c4b5bb681 | PARTIAL_OR_MISSING_LEDGER |
| PG50533 | Matthews, Stanley R. / Motor Matt's Launch; or, A Friend in Need | ac169d4dd3123e87d2777b477eb000853ab251963558e17693d8b56e89c53a25 | PARTIAL_OR_MISSING_LEDGER |
| PG50975 | Matthews, Stanley R. / Motor Matt's Prize; or, The Pluck That Wins | 2d11cb6bb532a985f97a3b640cf9eafb1a3d97e05cc7397a641d5b95322a268f | PARTIAL_OR_MISSING_LEDGER |
| PG51127 | Matthews, Stanley R. / Motor Matt on the Wing; or, Flying for Fame and Fortune | 1e125165c247b6a682cbd5cc79a911f5cb533e206d90544ea9c5589f446c16da | PARTIAL_OR_MISSING_LEDGER |
| PG51343 | Matthews, Stanley R. / Motor Matt's Reverse; or, Caught in a Losing Cause | b26c80b09e55d144b9d6038adb0e5ad6630986b3a923f44d19eb53a8fa4db0bd | PARTIAL_OR_MISSING_LEDGER |
| PG52138 | Matthews, Stanley R. / Motor Matt's Engagement; or, On the Road with a Show | 5b7fb4c134a941a754c7885b13492128b5a59a3da40b30eba59609eaa69488ca | PARTIAL_OR_MISSING_LEDGER |
| PG52397 | Matthews, Stanley R. / Motor Matt's Short Circuit; or, The Mahout's Vow | cf92ba7b8470ecbef92a6ff76a125abb9def54a25a043b69a9b1efb131738e16 | FULL_COVERAGE_LEDGER |
| PG525 | Conrad, Joseph, 1857-1924 / Youth, a Narrative | ec4e16d041110f1275ff38c6ef69994dfe0af2cfbc6b9d6e6ef0b8015c6a3674 | PARTIAL_OR_MISSING_LEDGER |
| PG52891 | Matthews, Stanley R. / Motor Matt's Make Up; or, Playing a New Rôle | dd4d7516a1aee42a197e8b774135760e042a51dcee86d7def018ce0cc1b7d1e2 | FULL_COVERAGE_LEDGER |
| PG53390 | Matthews, Stanley R. / Motor Matt's Mandarin; or, Turning a Trick for Tsan Ti | 26b3ea29f167b3ef7cc2c940afba74030f68776a21edec89f4bca7a702441ba5 | PARTIAL_OR_MISSING_LEDGER |
| PG53466 | Matthews, Stanley R. / Motor Matt's Mariner; or, Filling the Bill for Bunce | be8765b58252ed0f8f9c4c19a1635e6ca672959097c12be74010dccc16d14c77 | PARTIAL_OR_MISSING_LEDGER (覆盖 89.85%) |
| PG53533 | Matthews, Stanley R. / Motor Matt's Double Trouble; or, The Last of the Hoodoo | 57e1a62549b91e0544da111ceb9799e536fdbd392e80b3ee124ff005c1f5a251 | FULL_COVERAGE_LEDGER |
| PG53602 | Matthews, Stanley R. [Adapter] / A Taxicab Tangle; or, The Mission of the Motor Boys | 2dbc378a9517d05744a6cea58600f04b76d99b7e92c2678a0e2876d8a4dbd390 | FULL_COVERAGE_LEDGER |
| PG53607 | Matthews, Stanley R. [Adapter] / A Hoodoo Machine; or, The Motor Boys' Runabout No. 1313. | a5a4087ce618a14d7c6875b8e501397348bfe1516d719ef13b9272b2db2ee826 | PARTIAL_OR_MISSING_LEDGER |
| PG54709 | Senarens, Luis, 1863-1939 / The Galleon's Gold; or, Frank Reade, Jr.'s Deep Sea Search. | 75ac90354b0a90e50846246575eb0c0fbdd0b74d78f2391a0e35251ad844cdfc | PARTIAL_OR_MISSING_LEDGER |
| PG55374 | Senarens, Luis, 1863-1939 / Frank Reade, Jr., Fighting the Terror of the Coast | 44ca60f451b8d8705c114dac94822e679b672cfef6f7acd906041280a77128d3 | PARTIAL_OR_MISSING_LEDGER |
| PG55463 | Standish, Burt L., 1866-1945 / Owen Clancy's Run of Luck; or, The Motor Wizard in the Garage | 927df36c33a6139f4a674c80474706e4be2284fb8208bbebc6d417af1cc7c0e5 | FULL_COVERAGE_LEDGER |
| PG56007 | Smith, Elizabeth Oakes Prince, 1806-1893 / The Sagamore of Saco | d697c2d0cacbb700265b123ad9dd1ce932188794e4ea9e41b0941965d436b8de | FULL_COVERAGE_LEDGER |
| PG58420 | Powell, Van / The Mystery Boys and the Secret of the Golden Sun | 0c9b7798421a51699a7d1f8772c7893fa1bf3015f4112c0451901810fae58492 | FULL_COVERAGE_LEDGER |
| PG5978 | Trollope, Anthony, 1815-1882 / An Autobiography of Anthony Trollope | f6f42435e53c95fcb3973efc4837e117bfb2f7094d72b2bc7ce9eeb8ccd36b54 | PARTIAL_OR_MISSING_LEDGER (覆盖 84.26%) |
| PG60978 | Morris, Charles, 1833-1922 / Will Somers, the Boy Detective | 75bc8a6aaedb3ef593f040ab0fb7c6940d52ef142ea15c2f9ada311712702aa6 | FULL_COVERAGE_LEDGER |
| PG611 | Buchan, John, 1875-1940 / Prester John | cc0cb9317b36bf04fe8438d619160348f22fa983b9aae156148a0d2001791d95 | FULL_COVERAGE_LEDGER |
| PG61135 | Carter, Nicholas (House name) / Out of Death's Shadow; Or, A Case Without a Precedent | 8a060f3820500327c91e731c83b40b16763be05fcfd076dc2773b87b309784c5 | FULL_COVERAGE_LEDGER |
| PG61174 | Standish, Burt L., 1866-1945 / Dick Merriwell's Day; Or, Iron Nerve | 554ff7462864bacb6957c0b1a1a225d19a646c24e84bcf9ad3dcb310c5b0094a | PARTIAL_OR_MISSING_LEDGER (覆盖 99.89%) |
| PG61514 | Carter, Nicholas (House name) / Captain Sparkle, Pirate; Or, A Hard Man to Catch | cb4917cc5ccda6d289ea11b2a21b35f359f438ccd0aab41222322c552cadb657 | FULL_COVERAGE_LEDGER |
| PG61830 | Standish, Burt L., 1866-1945 / Dick Merriwell's Assurance; Or, In His Brother's Footsteps | 13974f5de882f8c1f70eb9f80d717eea0f64cbed437ae718556fd8250117e1d9 | FULL_COVERAGE_LEDGER |
| PG62010 | Carter, Nicholas (House name) / The Photographer's Evidence; Or, Clever but Crooked | eeeec4bf6e68a9af7e8daecd09d78417bb6df8d08df2b59e8f58a5244c23bdb5 | FULL_COVERAGE_LEDGER |
| PG62072 | Standish, Burt L., 1866-1945 / Frank Merriwell's Marriage; Or, Inza's Happiest Day | 87d5dda55b51da3c1a6651711c1ac1ddcba1fee4a959bc8ca0a6f70141184ba9 | FULL_COVERAGE_LEDGER |
| PG62411 | Standish, Burt L., 1866-1945 / Dick Merriwell's Glory; Or, Friends and Foes | 2ff8d4bea060bfe0742c02df92d59df2c95e20c275fadff9eef7985f79dc94f0 | FULL_COVERAGE_LEDGER |
| PG62428 | Carter, Nicholas (House name) / A Battle for Right; Or, A Clash of Wits | 9a79ab81029775c8f46dcd6d16f5da7d60e45b137321a6a5c713e14bd5f7d303 | FULL_COVERAGE_LEDGER |
| PG62639 | Standish, Burt L., 1866-1945 / Frank Merriwell's Trust; Or, Never Say Die | ad48d96f86dc9d37d160d1d4139fb608caec07d38ed564e35fab783c5d9c6576 | FULL_COVERAGE_LEDGER |
| PG62860 | Carter, Nicholas (House name) / Hidden Foes; Or, A Fatal Miscalculation | 86b4b026065f37c10dc64e590d08f3466eade0992f4c91fbf9cdbd0348bc4c15 | FULL_COVERAGE_LEDGER |
| PG62963 | Wentworth, Patricia, 1878-1961 / The Astonishing Adventure of Jane Smith | 1561311fd5fef2d6338a241761d7a1cfccef3d9aab75f2c37d25f335b99026e3 | FULL_COVERAGE_LEDGER |
| PG63024 | Standish, Burt L., 1866-1945 / Dick Merriwell's Fighting Chance; Or, The Split in the Varsity | a25f1a7bf079c4c6dbd4acd56300716659a884c6f5b86bcbb056e0b2be53c410 | FULL_COVERAGE_LEDGER |
| PG63143 | Carter, Nicholas (House name) / A Broken Bond; Or, The Man Without Morals | a9601c07a2fc640151700d47580a7809186e7ef937507676492cb471d247473d | FULL_COVERAGE_LEDGER |
| PG63483 | Standish, Burt L., 1866-1945 / Frank Merriwell's Chase; Or, Exciting Times Afloat | b3b9d59e10de34a1a17f5edf48816b10527737c6c28127e7948a5ea7f5410296 | PARTIAL_OR_MISSING_LEDGER (覆盖 50.85%) |
| PG63815 | Standish, Burt L., 1866-1945 / Frank Merriwell on the Road; Or, The All-Star Combination | 25403be63179cddf31c204d2e23406218f5a0a53150b4786641bb8514b7a7129 | FULL_COVERAGE_LEDGER |
| PG63864 | Carter, Nicholas (House name) / The Man Without a Conscience; Or, From Rogue to Convict | 1283d86a140bb1a2b80a3e286f24f0ce2ee6b2a8b72cce2cce6d060c8515e482 | FULL_COVERAGE_LEDGER |
| PG63977 | Carter, Nicholas (House name) / Snarled Identities; Or, A Desperate Tangle | 85cd45d77ba828a9f234a906d0eef00dcdc6d5fc62ac3629437bc7a7ecd8f1dd | FULL_COVERAGE_LEDGER |
| PG64147 | Carter, Nicholas (House name) / A Stolen Name; Or, The Man Who Defied Nick Carter | 63e7c5e4ce2a6a2ff562c209d2458c0363ffbfeaf17af1386ec2d8ef6f88b012 | FULL_COVERAGE_LEDGER |
| PG64347 | Standish, Burt L., 1866-1945 / Frank Merriwell's Prosperity; or, Toil Has Its Reward | f565158721c227cdf392ad04813e4086e1497db36297e81cc8a4cf777680c0e7 | FULL_COVERAGE_LEDGER |
| PG65608 | Stark, Inspector / The Great Green Diamond; Or, Thief Against Thief | c6673063eb2c10631846d6d58464976902ef99146231761f68a6ad35079bf601 | FULL_COVERAGE_LEDGER |
| PG65783 | Carter, Nicholas (House name) / The Twin Mystery; Or, A Dashing Rescue | d0fcd26f57f1a9bea078b715466a8846e56bc5bcbb91b7ff19246b10b221e9c6 | FULL_COVERAGE_LEDGER |
| PG66700 | Carter, Nicholas (House name) / A Cigarette Clew; Or, "Salted" For a Million | dff3154dda580bde77f6f57159b2439427026dec4e0a68142142bae6c2a58f92 | FULL_COVERAGE_LEDGER |
| PG66718 | Carter, Nicholas (House name) / A Sharper's Downfall; Or, Into the Net | a6fd704a770fc0eec005a52b29227da9cc2a01b2fb68e8d137b9e101093fa106 | FULL_COVERAGE_LEDGER |
| PG66724 | Carter, Nicholas (House name) / The Four-Fingered Glove; Or, The Cost of a Lie | 9eda8b359e3a6a895937d32be3457eb0c065360ee60c516522266a76ee482e4c | FULL_COVERAGE_LEDGER |
| PG66740 | Carter, Nicholas (House name) / The Stolen Brain; Or, A Wonderful Crime | e9063c87973b4c92f11441860d5f13f6fda4bf4245ed61395d27703ffc1309ae | FULL_COVERAGE_LEDGER |
| PG66863 | Carter, Nicholas (House name) / The Plot That Failed; or, When Men Conspire | 33fb274fa07ba2948bac139c75a4771ee0f6f69df74258ebb8ca2f6cc5a9c80f | FULL_COVERAGE_LEDGER |
| PG69168 | Ellis, Edward Sylvester, 1840-1916 / The phantom hunter; or, love after death | 4ffbdfc3d24198f5435aec59818fc523c321631791442b1f7c9361c14b73a9d6 | PARTIAL_OR_MISSING_LEDGER |
| PG711 | Haggard, H. Rider (Henry Rider), 1856-1925 / Allan Quatermain | dcfae94e91685410dfd7814f7131adc327c003d7969a822af2d6c9dd0e0cd007 | FULL_COVERAGE_LEDGER |
| PG71337 | Scott, Leroy, 1875-1929 / Mary Regan | 45f8a6a2de55ee98cf43a96870596e8b409d1a016439163c03d7b7b034c5f6f9 | FULL_COVERAGE_LEDGER |
| PG74755 | Anderson, Sherwood, 1876-1941 / A story teller's story :  The tale of an American writer's journey through his own imaginative world and through the world of facts, with many of his experiences and impressions among other writers | fa9b309dd77e9c4e322b58ed3d5f33a683ec434de3fe90418cec8dc599eca4ef | PARTIAL_OR_MISSING_LEDGER (覆盖 98.96%) |
| PG91 | Twain, Mark, 1835-1910 / Tom Sawyer Abroad | 5a39e3eebf693fbee937b499da7f761e271966d4b3f55f2ea58d61f02b4cfd39 | PARTIAL_OR_MISSING_LEDGER |

## 当前 Rule/家族证据与分层标记
正式 11 条规则以 SKILL.md 所列的 M01/M02/M03/M04/M05/M07/M11/M12/M13/M14/M15 为入口；带 source ID 的旧段落仅是历史文学观察 F、个人写作证词 F-AUTHOR 或格式扫描 F-STRUCTURAL，而非无条件执行依据。

- 卷级 M01/M02/M14：用 PG61174、PG42545、PG42569、PG64347 等卷末互异样本互相限制，不强制每卷结案或留钩。
- 章级 M03/M11：章末期刊钩与回顾长短按载体和读者记忆负担条件化，历史三种钩只是可观察类别。
- 连续性 M04/M13：跨卷状态与开放线以人物和世界实事为约束，不机械计两条或必须复位。
- 变奏 M05 与排产 M07/M12/M15：编号系列公式与 Trollope 个人存稿证词仅是不同生产案例；不用于推断所有平台、作者或市场的最优值。
- 正式来源元数据只证明固定文本身份；区间审计只证明存在连续记录；角色行为、作者自述和跨书 H/P 的可信度仍需另行审查。

## 历史旧索引和原有来源片段（仅供回查，保留原始元数据）

下列为上一版本当时的覆盖级别与规则锚点，现可能过期。引用时以本页前段当前 SHA/P2 表及实际所见片段为准，不能把旧 FULL 标识误当最终审计。

# 06 来源索引：book_id、定位、覆盖等级、族去重

本索引随 Skill 包独立可读：只列 book_id（Project Gutenberg 编号）、作品、作者/族、定位、覆盖等级、被哪条规则使用、能与不能证明什么。**不依赖任何轮次笔记或本机路径。**

## 1. 定位读法

- **L** = 纯文本阅读版的行号（从文件开头计）；**C≈** = 字符偏移（从文件开头计，约 ±300 字符）。
- 行号以本轮使用的纯文本阅读版为准；换版本可能漂移。重找方法：用 book_id + 本节引文片段检索。
- 引文做了弯引号/破折号/斜体归一化；引文 ≤30 words，只用于定位，不代替原文。
- 覆盖等级：**FULL** = 叙事正文读完（末页广告/书目除外）；**PARTIAL** = 读了开头/结尾/若干窗口；**STRUCTURAL** = 只做结构扫描（刊头/章目/卷末），单本 0.5–4.5%。
- “族” = 同系列多卷/同一作者多本/house name 各计 1 族；**同族多本不增加独立证据**。

## 2. 语料总览（只用于说明边界）

- 103 份文本：61 份编号系列、29 份单本长篇、7 份作者自述、6 份形式/元数据不符。
- 全类约 38 个独立来源族；本索引实际引用 **17 族**（R02 新增 Anderson 族；Trollope/Erichsen/My First Book 三族在 R01 已列，本次为深读覆盖升级；dime 刊物装置观察并入原有 Standish/Matthews/Senarens/Bradys 族）。其余族未被本轮规则采用，不列入。
- 覆盖（R01+R02 累计，R02 按 R01 同口径估算）：约 1.04M token / 7,426,717 ≈ **14%**；全文逐字 13 本、定向深读 8 本（单本 2–17%）、STRUCTURAL 81 本（每本 <2%）、UNREAD 0 本。深读/扫描的行号区间在各来源行与轮次证据卡（工作区内部记录，本包不依赖）；STRUCTURAL 只证明体例与出版装置，不证明章内技巧。
- 语料以 1900–1925 年英美通俗连载为主，含少量 1880s–1890s 的作者自述/汇编；不是现代网文样本。

## 3. 族谱与去重（先看这张表）

| 族 | 本索引中的 book_id（覆盖） | 规则 | 去重说明 |
|---|---|---|---|
| **Standish**（Merriwell 等） | PG61174（FULL）、PG61830（PARTIAL）、PG62072（PARTIAL）、PG64347（STRUCTURAL） | M01/M02/M03/M05/M13 | 4 本只计 1 族；PG64347 仅结构扫描，不能支撑章内技巧；PG61174 L2989 是伪装身份，不作 M11 证据 |
| **Matthews**（Motor Matt 等） | PG49197（FULL）、PG47071（FULL）、PG47901（PARTIAL）、PG49644（PARTIAL）、PG51127（PARTIAL）、PG48252（STRUCTURAL） | M01/M03/M04/M05/M06/M09/M11/M13 | 6 本只计 1 族；26 本 Motor Matt 不等于 26 份证据 |
| **Nick Carter**（house name） | PG62428（STRUCTURAL）、PG66724（PARTIAL） | M01/M04 | house name 只计 1 族；PG62428 仅结构扫描 |
| **Verrill**（Radio Detectives） | PG42545（FULL）、PG39576（PARTIAL）、PG42569（PARTIAL） | M02/M03/M04/M11/M13/M09 | 3 本只计 1 族；同系列跨卷断言需逐卷核 |
| **Burroughs** | PG2020（PARTIAL）、PG1401（PARTIAL） | M02/M04/M06/M09/M14 | 2 本 1 族；同作者一闭一开 |
| **Orczy** | PG1752（PARTIAL） | M03/M06/M09/M14 | 1 族 |
| **Conrad** | PG1083（PARTIAL 14.2%）、PG525（R02 FULL，暂无规则引用，仅覆盖改善） | M14 | 1 族；PG525 全文卡存于轮次工作区（本包不依赖外部路径），规则未引用 |
| **Anderson**（R02） | PG74755（浅抽样 3%：Definition 节） | CTX-ECON 背景 | 1 族；意识流回忆录，仅市场压力观察 |
| **Buchan** | PG611（PARTIAL） | M14 | 1 族 |
| **Haggard** | PG711（PARTIAL） | M14 | 1 族；末章装置不可泛化 |
| **Cook** | PG47455（PARTIAL 95%） | M05/M07/M08/M12 | 1 族；作者自述，不是行业统计 |
| **Trollope** | PG5978（R01 PARTIAL 9.9% + R02 定向深读至 17%：L2985–3311/L3311–3710/L5760–5940/L6560–6900） | M07/M08/M12/M15、CTX-RISK | 1 族；R02 升级：完稿原则已是作者原话（L3485–3522），不再是“其子 Preface”口径；配额证词与 Hills 转录互证 |
| **Duchess** | PG27621（FULL）、PG27622（FULL，未引用） | M05/M07/M10 | 2 本 1 族；PG27622 不增加证据 |
| **Anderson** | PG74755（PARTIAL 4.5%） | M05/M12 | 1 族 |
| **Erichsen（汇编/二手）** | PG32328（R01 PARTIAL 17.7% + R02 深读第 XI 章 L3015–3305） | M08/M12、M03 补强 | 1894 年二手汇编；转引 Trollope 不增加族；Daudet 路线证词为本族独有 |
| **Howard** | PG45455（PARTIAL 3.4%） | M02/M09 | 1 族；覆盖低，只作反例 |
| **My First Book（编辑卷）** | PG33148（R01 PARTIAL 12.2% + R02 深读 Besant L811–1074/Kipling L2712–2858/Doyle L2868–3090 三节） | M07/M08、CTX-RISK | 22 位作者合辑，按 1 个编辑卷计；Stevenson 证词只算 1 条；R02 三节未新增族 |

> 规则表里的“族数”按这张表计，不按 book_id 数计。同一本书在多条规则里出现，也不增加族数。

## 4. 规则 → 来源对照（每条 ≥2 个 book_id + 定位）

| 规则 | 主来源（book_id + 定位） | 反例/边界来源 | 族数 | 置信 |
|---|---|---|---|---|
| **M01** 槽位表 | PG61174 L165–168（卷首 114/115 号+排期）；PG49197 L3884–3890（卷末下号+章题）；PG62428 L8894（书末广告：同图书馆 No.1002）；PG47901 184180（书末 No.11 广告）；同书 157540（No.10 预告） | PG64347 卷末无下号（STRUCTURAL）；PG45455 全闭合无预告（PARTIAL） | 3 | 中 |
| **M02** 双线结尾 | PG61174 L7366–7383（积分表闭合）/ L9216–9217（宿敌开口）；PG42545 L5633–5647（海图）；PG2020 513008–520600（政治层闭合） | PG64347/PG45455 全闭合；PG42569 C≈300600 全开；PG2020/PG1401 一闭一开 | 3 | 中 |
| **M03** 三类章末钩 | PG42545 L370/L822/L1278/L1812（多章钩）；PG1752 349,979（下章绝对时间）；PG61174 L945（证人现身）；PG49197 L1276（抛海+救援） | PG42545 末章用卷末实物钩；PG1083 章末场景收束；PG47455 leave-off 过强 | 4 | 高（3 章阈值为 H/P） |
| **M04** 复位四问 | PG49197 L3816–3878（sealed orders+同船同班底）；PG42545 L5633–5647（实物入口）；PG66724 L8025（余敌未除）；PG47071 L3776–3799（Pima Pete 纸条）；PG49644 ~156900 / L3777（机构决定挂起） | PG2020 513008–520600 制度改变；PG51127 152438 预计遗孀可得十万美元（预测，非已获得）；PG49197 同救援用两次 | 3 | 中（后半句 H） |
| **M05** 公式与变奏 | PG47455 L1117–1121（same hero/same class）；PG47455 L3888–3898（三篇一组）；PG27621 L89–95（固定场景+年轻男女）；PG61174 L4024–4291（竞赛插入）；PG47901 89720–97720（敌方女儿功能位） | PG62072 207500–215500 vs 273333–281333（两章同构）；PG74755 352194（sawdust）；PG47455 编辑抱怨“action was rarely varied” | 4 | 中 |
| **M07** 容量表 | PG47455 L3867–3871（5 页/章→16 章）；PG47455 L1356–1364（两周 40,000 词）；PG5978 182,402（250 词/页+周配额）；PG5978 404,700（3h/日+250 词/刻钟）；PG33148 425,361（15 天 15 章）；PG27621 L129–130（一夜 3–4 章） | PG33148 419,954/425,361 Stevenson 第 16 章崩盘；PG5978 3h/日非通用；PG47455 5 页是印刷规格 | 4 | 中 |
| **M11** 回顾分档 | PG42545 L80–164（1–2 页人物+前案+位置，约 4,900 字符）；PG51127 ~5600（一句能力句） | PG42569 C≈4200（约 8,000 字符长回顾，重复上一卷末；反例，不是上限） | 2 | 中（长度上限 H） |
| **M12** 反馈日志 | PG5978 L6755（俱乐部抱怨→杀角色→后悔）；PG47455 1890–1891（编辑要婚礼）/ 3190–3191（电报收尾）；PG74755 652288（编辑不许转型） | PG32328 3048–3050（二手版本，矛盾）；编辑配方被称“little plot” | 3 | 低 |
| **M13** 开放线台账 | PG42569 C≈300600（主犯逃走+跟踪货轮）；PG39576 L4543–4585（经纬度+三个数字+姓名未说）；PG61830 L10833（财产承诺留后）；PG49644 2405（卷首人物表：绑领事换被捕者）；PG48252 卷首人物表（Brady 转变客户，STRUCTURAL） | PG39576 同时扣主谋/坐标/数字；PG61830 财产拖卷；PG42569 未回收旧线 | 3 | 中 |
| **M14** 部界类型 | PG1083 L1840–1846（同夜续写+回指）/ L7154–7161（出海转场）；PG1752 353783/501194（三部约 51/21/27，Part III 首章）；PG2020 513008–520600（闭合卷末）；PG611 352788（第 21 章在 89%）；PG711 558732/562445（末章“BY ANOTHER HAND”） | PG1083 末部 30% 是单本测量；PG1752 不等长是失败结构；PG2020/PG1401 一闭一开 | 5 | 中 |

## 5. 逐书条目（只列本索引引用的书）

| book_id | 作品 | 作者/族 | 覆盖 | 本索引用到的定位 | 能证明 | 不能证明 |
|---|---|---|---|---|---|---|
| PG61174 | Dick Merriwell's Day; Or, Iron Nerve | Standish | FULL（98%） | L165–168；L945；L4024–4291；L7366–7383；L9216–9217 | 卷首排期/下号；证人到场钩；竞赛插入；积分表闭合；宿敌开口 | L2989 是伪装身份进入本卷（章末揭面），不构成回顾；不能证明作者按号写作；不能证明整个 Merriwell 系列都这样 |
| PG49197 | Motor Matt's Submarine; Or, The Strange Cruise of the Grampus | Matthews | FULL（98%） | L1276；L3816–3878；L3884–3890 | 章末抛海钩；卷末 sealed orders+同船同班底；下号+章题 | 不能证明“每卷都同船同班底” |
| PG62428 | A Battle for Right; Or, A Clash of Wits | Nick Carter | STRUCTURAL（1.5%） | L8894（书末广告 No.1002） | 书末广告是发行装置/版式 | 不能提炼章内技巧；不能证明写作顺序 |
| PG47901 | Motor Matt's Air Ship; Or, The Rival Inventors | Matthews | FULL（R02 补读完成） | 184180（书末 No.11 广告）；157540（THE NEXT NUMBER (10) 预告）；89720–97720（敌方女儿功能位）；154800–157700（Brady 逃走） | 广告提前公布下号；主案未结卷末仍有 No.10 预告；功能位变奏；主犯可跨卷逃走 | 广告不是创作顺序；不能用它证明全书结构 |
| PG42545 | The Radio Detectives in the Jungle | Verrill | FULL（100%） | L80–164；L370/L822/L1278/L1812；L5633–5647 | 续卷三段式回顾（约 4,900 字符）；多章三类钩；海图实物入口；末章不用章末钩 | 不能证明“回顾只用一次”是系列通则 |
| PG42569 | The Radio Detectives Under the Sea | Verrill | R01 21% + R02 补读 4%（书名页/第1→2章/结尾） | C≈4200；C≈300600；第1→2章平收过渡；结尾 hunch 决策+软钩 | 约 8,000 字符回顾的反例；全开卷存在；书装平收章末样本 | 不能证明全开卷的留存效果 |
| PG2020 | Tarzan the Terrible | Burroughs | PARTIAL（8.6%） | 186248 / 432802 / 513235（被当作神/囚/新王登基）；513008–520600（闭合） | 政治层闭合（登基/离场）；统治者更替 | 社会/私人层未逐段核；不能证明“每卷都闭合”；同作者 PG1401 相反 |
| PG1401 | Tarzan the Untamed | Burroughs | PARTIAL（6.0%） | 405687 / 428249（新地图）；584997–604656（开口） | 换地图不必然提高赌注；开口卷存在 | 不能证明“换地图”是升级路径 |
| PG64347 | Frank Merriwell's Prosperity; or, Toil Has Its Reward | Standish | STRUCTURAL（2.4%） | 卷末（THE END+广告，无下号） | 全闭合、无下一号的卷存在 | 不能提炼章内技巧；不能证明全书质量 |
| PG45455 | Shadow, the Mysterious Detective | Howard | PARTIAL（3.4%） | 目录/末尾（“THE MYSTERY EXPLAINED”+逐人判决） | 全闭合、无续作钩的卷存在 | 覆盖低；不能当结构模板 |
| PG1752 | El Dorado: An Adventure of the Scarlet Pimpernel | Orczy | PARTIAL（9.3%） | 349,979；353783 / 501194；453952–461952；683928–689928 | 下章绝对时间落地；三部不等长；施救者→人质；全开结尾无预告 | 约 51/21/27 是单本失败结构，不是篇幅公式 |
| PG49644 | Motor Matt's Quest; or Three Chums in Strange Waters | Matthews | PARTIAL（20.5%） | ~156900 / L3777（机构决定挂起）；2405（人物表：绑领事换 Sixty）；~93700（亲属关系） | 世界状态可挂起；旧反派可变交易筹码（人物表） | 不能证明所有旧线都能转性；~93700 只证明亲属关系，不证明“筹码” |
| PG47071 | Motor Matt's "Century" Run; or, The Governor's Courier | Matthews | FULL（97%） | L3776–3799 | 败反派留纸条，预告手下 Pima Pete 求助 | 不能证明“每卷都留纸条” |
| PG66724 | The Four-Fingered Glove; Or, The Cost of a Lie | Nick Carter | PARTIAL（4.1%） | L8025 | 卷末“还有余敌”的开口 | 覆盖低；不能当完整结构证据 |
| PG47455 | The Fiction Factory | Cook, William Wallace | PARTIAL（95%） | L1117–1121；L1356–1364；L3867–3871；L3888–3898；1890–1891；3190–3191 | 出版社以“same hero/same class”续订；每章 5 页→16 章；两周 40,000 词；三篇一组；编辑要婚礼；电报收尾 | 作者自述，不是行业统计；5 页是印刷规格，不是叙事规律；不能外推现代合同 |
| PG62072 | Frank Merriwell's Marriage; Or, Inza's Happiest Day | Standish | PARTIAL（15.3%） | 207500–215500 / 273333–281333 | 两章几乎同构，只换项目→公式疲劳 | 不能量化“读者何时疲劳” |
| PG74755 | A Story Teller's Story | Anderson | R01 4.5% + R02 定义节 2.6%（L5040–5239） | 352194；652288；L5144–5150（杂志市场压力） | 类型作者被配方锁定；锯末批评；1920s 美国杂志市场画像 | 意识流回忆录半虚构；个人审美批评，不是市场统计 |
| PG27621 | How I write my novels | Duchess | FULL（100%） | L30–32；L89–95；L129–130；L132–134；L145 | 固定场景/年轻男女；一夜 3–4 章；整块降临/先写末章/不逼稿（个人主张） | 单作者、单卷言情；不能当连载流程 |
| PG5978 | An Autobiography of Anthony Trollope | Trollope | R01 9.9% + R02 深读至 17%（方法章 L2985–3311/L3311–3710/L5760–5940/L6560–6900） | 182,402；404,700；L6755；L3007–3031；L3485–3522；L6647–6699 | 页数日记/周配额；3h/日；俱乐部抱怨→杀角色→后悔；完稿原则作者原话（R02 更正 R01 其子 Preface 口径）；存稿缓冲 1–3 部 | 不是行业统计；深读 17%，其余未读；配额数值不可移植 |
| PG33148 | My First Book（22 位作者合辑） | Various / 编辑卷 | R01 12.2% + R02 三节 8%（Besant L811–1074/Kipling L2712–2858/Doyle L2868–3090） | 419,954 / 425,361；L855–861；L972–996；L998–1015；L3032–3062；L3066–3089 | 有地图+章表仍第 16 章崩盘；Besant 连载救刊/委托出版；Kipling 报纸填栏；Doyle 悬念中断/碎片接缝失效/品类先验可错 | 22 人回忆不是统计；成功者偏差 |
| PG61830 | Dick Merriwell's Assurance; Or, In His Brother's Footsteps | Standish | PARTIAL（3.1%） | L10833 | 财产/身世承诺留到以后（开放线） | 覆盖低；不能证明下一卷一定兑现 |
| PG39576 | The Radio Detectives | Verrill | FULL（R02 补读完成） | L4543–4585 | 垂死者给经纬度+三个数字、姓名未说→多线堆积 | 不能证明下一卷回收质量 |
| PG48252 | Motor Matt's Daring Rescue; or, The Strange Case of Helen Brady | Matthews | STRUCTURAL（3.3%） | 卷首人物表 | 上卷反派 Brady 变成求助客户（旧线转性） | 结构扫描；不能支撑章内技巧 |
| PG51127 | Motor Matt on the Wing; or, Flying for Fame and Fortune | Matthews | FULL（R02 补读完成） | ~5600（一句能力句）；152438（Matt 预计遗孀可得十万美元）；31878 / 56347（half interest / $500） | 短回顾足够；财产安排可作卷末变化（预测，非既成）；赌注换成产权 | 不能证明“产权线”普遍有效；不能把预测写成“遗孀已致富” |
| PG1083 | The Arrow of Gold: A Story Between Two Notes | Conrad | PARTIAL（14.2%） | L1840–1846；L7154–7161 | 连续型部界：同夜续写+回指；末部以出海转场 | 未读满；末部 30% 是单本测量，不是公式 |
| PG611 | Prester John | Buchan | PARTIAL（5.8%） | 352788 | 第 21 章在全书 89% 处，之后是返回/结算 | 单一部界位置，不能当比例 |
| PG525 | Youth, a Narrative | Conrad | FULL（R02） | 全文卡（轮次工作区证据卡，本包不依赖） | 单篇完整叙事弧对照样本 | 规则暂未引用，仅覆盖改善；不可当连载证据 |
| PG1918 | Long Odds | 短篇（单本） | FULL（R02） | 全文卡 | 短篇完整样本 | 规则暂未引用 |
| PG43765 | The Twin Ventriloquists | Old Sleuth 系 | FULL（R02） | 全文卡 | 双主角身份错位结构 | 规则暂未引用；族归属见 §3 |
| PG55374 | Frank Reade, Jr., Fighting the Terror of the Coast | Senarens | FULL（R02） | 全文卡 | Frank Reade 电气时代代表 | 规则暂未引用 |
| PG63483 | Frank Merriwell's Chase; or, Exciting Times Afloat | Standish | R02 定向深读 4.5%（SAMPLED） | L238–242；L908–911；L7460–7472；L7480–7530 | 动作/密谈双钩型；宽恕式闭环；Magnet Library 周刊装置 | 族内其余 7 册仅扫描；中段未读 |
| PG37092 | The Bradys' Chinese Clew | house pen（Bradys 族） | R02 定向深读 3.4%（SAMPLED） | L4883–4884；L4886–5004；L1086 | 5¢/32 页/周更规格公示；29 期双题公式；代际主角对 | 种族刻板为时代产物；单期完结制证据 |
| PG49638 | Frank Reade and His Steam Horse | Noname（Senarens 族） | R02 定向深读 2%（SAMPLED） | L13–14；L11；尾部书目；第2→3章钩 | 第二类邮件登记；Noname 品牌；载具换型书目；预言告别钩 | 深读 2%；载具公式重复风险已记 |
| PG711 | Allan Quatermain | Haggard | PARTIAL（6.3%） | 558732 / 562445 | 末章“BY ANOTHER HAND”，叙述者死后交接 | 终卷专用装置；连载中卷不能照搬 |
| PG32328 | Methods of Authors | Erichsen（编） | R01 17.7% + R02 第 XI 章全章 13%（L3015–3305） | 3048–3050；3289–3301；L3023–3037；L3041–3048；L3240–3261 | 1894 年二手转引：Trollope 配额/杀角色异文（与 PG5978 互证）；发现式情节；Daudet 截稿路线；方法披露反噬 | 二手汇编，转引不增族；不能当一手证词 |
| PG27622 | The story of my first novel | Duchess | FULL（100%） | 未使用 | 与 PG27621 同作者重复，不增加证据 | 不作为规则来源 |

## 6. 覆盖等级与“能/不能”

| 等级 | 本索引中的书 | 能支持 | 不能支持 |
|---|---|---|---|
| **FULL** | PG61174、PG49197、PG42545、PG47071、PG27621、PG27622 | 章内钩、卷末结构、人物/班底复位、作者主张 | 不能支持“全类通则”；单本 FULL 仍只是 1 族 |
| **PARTIAL** | PG61830、PG62072、PG47901、PG49644、PG51127、PG39576、PG42569、PG66724、PG2020、PG1401、PG1752、PG5978、PG33148、PG47455、PG74755、PG1083、PG611、PG711、PG32328、PG45455（共 20 本） | 已读窗口内的结构/语句 | 未读部分不能补；不能评价全书；不能把窗口当全文 |
| **STRUCTURAL** | PG62428、PG64347、PG48252 | 刊头、章目、卷末下号/广告、人物表等体例 | 章内技巧、全书质量、写作顺序 |
| **UNREAD（未引用）** | 17 本 | 无 | 无 |

> 本表 29 条（含 PG27622 重复说明）是**本索引实际列出的书**，不是全类 103 本的分布；全类分布见 [SKILL §1](../SKILL.md)：6 FULL / 26 PARTIAL / 54 STRUCTURAL / 17 UNREAD。

## 7. UNVERIFIED（单列，引用时必须降级）

1. **EV-S3-024（PG47901 定位错误）**：卡头写“Ch I，约 2,600 字符”，引文实际在 **Ch II，约 12,330 字符**；事实是“Ch I 发生载具失控，Ch II 由驾驶员承认”。本索引不使用该卡作为 M01/M05 的证据；若引用，写“Ch I–II”。
2. **EV-S4-005（PG42545 跨卷断言）**：L1592–1594 的引文可核，但“本系列上一卷已有同型桥段”是跨卷断言，本轮未读上一卷，**不能核验**。只能引用“本卷的假遇难者是内应”，不能写“上一卷也有”。
3. **抽查面**：本轮只对 282 张证据卡抽查 21 张（7.4%）；未抽查卡的定位不能声称已逐字核。本索引只把已核/已用于融合的定位列为规则来源。未抽查的 261 张不当作已逐字核。
4. **同族跨卷**：PG61174 的“下号”是事实，但不能推出“Merriwell 每卷都有下号”（PG64347 反例）；PG61830 的财产承诺是事实，但不能推出“下一卷一定兑现”。
5. **窗口阅读**：PG1083 14.2%、PG32328 17.7%、PG39576 43%、PG42569 21%、PG1752 9.3% 等均为窗口；不能当全文。
6. **C 档结构扫描**：PG62428、PG64347、PG48252 只能证明体例；不能提炼章内技巧。
7. **二手/转述**：PG5978 的“先完稿再载”来自其子 Preface；PG32328 是 1894 年二手汇编；PG33148 是 22 人合辑；PG27621/PG27622 同作者。都不能当“行业统计”。
8. **发行装置**：卷首书目、卷末“下一号”、订阅印花、书末广告只能证明“卷是可编号的商品槽位”，不能证明作者写作顺序。
9. **现代数据**：没有现代网文样本、读者留存、销量、完读率；所有现代迁移均为 H / `NOT_PROVEN`。

## 8. 不可引用项（硬禁止）

- **同族当独立证据**：26 本 Motor Matt、9 本 Merriwell、16 本 Nick Carter 只能各计 1 族；不得写成 26/9/16 份证据。
- **本分类以外的资料**：不引用其他分类、外部摘要或未校验文本；本索引只列本分类 manifest 中的 PG 文本。
- **本机绝对路径**：本索引不写任何绝对路径；只用 book_id + 行号/偏移。
- **单本装置当通则**：
  - PG1083 的编者注框架/删节许可/尾声摘要（Conrad 单本手法，且是叙述者的话，不是合同）。
  - PG711 的“叙述者死后由第二人交接”（终卷专用）。
  - PG1730 的卷首政论序、PG2020 的词汇表、PG525 的不分章中篇。
  - PG331 的“切到配角烤肉念诗”软钩（作者自己也没复用）。
  - PG27621 的“整块降临/先写末章/不逼稿”（单作者、单卷言情，不进主规则）。
  - PG47455 的“每章 5 页→16 章”（印刷规格，不是叙事规律）。
  - PG1752 的“三部约 51/21/27 配比”（单本失败结构，不是篇幅公式）。
- **时代局限当角色模板**：Motor Matt 的华人仆从 Ping（洋泾浜英语）、Bradys/Nick Carter 的华人帮会刻板形象，只能作“1900 年代种族偏见”的注记，不能当人物/情节模板。
- **广告/预告当创作顺序**：出版社书目、卷末预告、订阅印花、书末广告是发行装置，不是作者意图或写作顺序。

## 9. 本索引的自检

- 10 条规则每条至少 2 个 book_id + 定位；族数按 §3 计，不按 book_id 计。
- 每条规则都有反例/边界来源（§4 第 3 列）；没有反例的规则不成立。
- FULL/PARTIAL/STRUCTURAL 已标；UNREAD 不引用。
- UNVERIFIED 与不可引用项单列；现代迁移不在本索引冒充 F。
- 本索引不依赖轮次笔记、卡片文件或本机路径；换版本时按 book_id + 引文片段重找。

返回 [SKILL](../SKILL.md)｜上一篇：[05 生产约束](05-production-constraints.md)


## 10. R02 新增规则-来源映射（供复审回读）

| 规则 | 新来源与定位 | R02 变化 |
|---|---|---|
| M07 | PG5978 L3007–3031（周配额簿/250 词页/逐词清点）、L6647–6685（3 小时+秒表+昨日稿重读） | 置信 中→高；参数不可移植，四件套结构标 H |
| M08 | PG5978 L3485–3522（完稿原则原话+唯一破例）、L3490–3492（三死于连载）、L6687–6699（缓冲）；PG32328 L3289–3301（Daudet 截稿路线） | UNRESOLVED→结构化判据（07 §3）；仍禁单一通则 |
| M15（新） | PG5978 L6687–6699（1–3 部完成稿库存） | 新增低置信可选规则（1 族自证） |
| M03/M12 补强 | PG5978 L3609–3620（分期反沉闷）、L5924–5935（冗长自检）、L6739–6757（杀 Mrs. Proudie 全语境）；PG63483 L238–242/L908–911（动作/密谈钩型） | 证词补全，不改断言 |
| CTX-ECON/CTX-RISK | PG37092 L4883–5004（5¢/32 页/周更+29 期双题公式）、PG49638 L13–14（第二类邮件）+书目（载具换型）、PG42569（真名精装对照+平收章末）、PG33148 L855–861/L972–996/L3032–3062/L3066–3089、PG5978 L6787–6798（版权碎片）、L6701–6713（分册市场）、PG74755 L5144–5150 | 背景判据两条，不入正式规则 |


## R04 增补证据（本轮实读补齐，全部通过 `kd32_ledger_gate.py`）

| PG | 本轮补齐区间 | 行数 | 台账文件 | 门禁 | 为新规则/裁决提供 |
|---|---|---:|---|---|---|
| PG39576 | L1301–5141 | 3841 | `notes/reading/ledger-PG39576-L1301-5141.md` | PASS | M02（物证收束 / 主谋未收束 / 财宝降级）、M06 反例（误认→技术性纠正）、M12（元叙事坦白） |
| PG5978 | L1–3 / L20–112 / L1815–1882 / L2985–3710 / L5760–5940 / L6560–6900 | 1412 | `ledger-PG5978-L1-130-L1800-1894.md` + `ledger-PG5978-L2985-3710-L5760-5940-L6560-6900.md` | PASS | M08（原则的技术理由 + 一次记账的破例）、M12 边界（杀角后后悔）、M17（长度 vs 密度冲突）、M07（比例法） |
| PG63483 | L58–3610 | 3553 | `ledger-PG63483-L58-3610.md` | PASS | M04（跨册因果靠对白回放）、M13（未确认死亡作为跨册悬置项）、M06 反例（用排除法推进） |
| PG1142 | L3001–3320 | 320 | `ledger-PG1142-L3001-3320.md` | PASS | M02（结局可由信息的分发方式构成） |
| PG33148 | L985–1026 | 42 | `ledger-PG33148-L985-1026.md` | PASS | **M08 路线 C**（匿名新作→自费印制+委托发行+付款时点后移；并自陈破例与区分条件） |
| PG50975 | L4001–4468 | 468 | `ledger-PG50975-L4001-4468.md` | PASS | **M16**（载体构成六层）、M01（编号 + 带日期的下期预告）、M14（边界由载体决定） |

**逐来源角色核账与规则裁决**见本轮 `notes/source-synthesis.md`；**逐来源覆盖状态**见 `notes/source-coverage.md`。
