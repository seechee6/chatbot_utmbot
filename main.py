from flask import Flask, request
import re
import random

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def return_response():
    query = request.args.get('query', '')  # Get the 'query' parameter from the request

    # Check various conditions based on the query
    intents_and_patterns = {
        'ask_about_query': r'.*\s*query.*',
        'ask_about_question': r'.*\s*question.*',
        'hi': r'.*\s*hi.*',
        'hello': r'.*\s*hello.*',
        'ask_about_course': r'.*\s*course.*',
        'ask_about_faculty': r'.*\s*faculty.*',
        'ask_about_arked': r'.*\s*arked.*',
        'ask_about_fees': r'.*\s*fees.*',
        'ask_about_public_holidaysjb': r'.*\s*holidaysjb.*',
        'ask_about_public_holidayskl': r'.*\s*holidayskl.*',
        'ask_about_sembreakjb': r'.*\s*sembreakjb.*',
        'ask_about_sembreakkl': r'.*\s*sembreakkl.*',
        'ask_about_utm': r'.*\s*about utm.*',
        'ask_about_club': r'.*\s*club.*',
        'ask_about_library': r'.*\s*library.*',
        'ask_about_transportation': r'.*\s*transportation.*',
        'ask_about_kolej': r'.*\s*kolej.*',
        'ask_about_facilities': r'.*\s*facilities.*',
        'bye': r'.*\s*bye.*',
        'goodbye': r'.*\s*goodbye.*',
        'thank you': r'.*\s*thank you.*',
        'thanks': r'.*\s*thanks.*',
        # Add more intents and corresponding regex patterns as needed
    }

    answer = None

    for intent, regex_pattern in intents_and_patterns.items():
        found_match = re.search(regex_pattern, query, re.IGNORECASE)
        if found_match:
            if intent == 'ask_about_course':
                answer = [
                    "Faculty of Computing:\n1.Bachelor of Computer Science (Software Engineering)\n2.Bachelor of Computer Science (Data Engineering)\n3.Bachelor of Computer Science (Computer Networks and Security)\n4.Bachelor of Computer Science (Graphics and Multimedia Software)\n",
                    "Faculty of Electrical Engineering:\n1.Bachelor of Electrical Engineering\n2.Bachelor of Electronic Engineering\n3.Bachelor of Engineering (Electrical - Mechatronic)\n4.Bachelor of Biomedical Engineering\n",
                    "Faculty of Civil Engineering:\n1.Bachelor of Civil Engineering\n",
                    "Faculty of Mechanical Engineering:\n1.Bahelor of Mechanical Engineering\n2.Bachelor of Mechanical Engineering (Materials)\n3.Bachelor of Mechanical Engineering (Industrial)\n4.Bachelor of Mechanical Engineering (Manufacturing)\n5.Bachelor of Mechanical Engineering (Aeronautics)\n6.Bachelor of Mechanical Engineering (Automative)\n7.Bachelor of Engineering (Naval Architecture and Offshore Engineering)\n",
                    "Faculty of Chemical and Energy Engineering:\n1.Bachelor of Engineering (Chemical)\n2.Bachelor of Engineering (Chemical-Bioprocess)\n3.Bachelor of Engineering (Chemical-Gas)\n4.Bachelor of Engineering (Petroleum)\n5.Bachelor of Engineering (Nuclear)\n",
                    "Faculty of Build Environment and Surveying:\n1.Bachelor of Science in Architecture\n2.Bachelor of Quantity Surveying\n3.Bachelor of Urban and Regional Planning\n4.Bachelor of Landscape Architecture\n5.Bachelor of Geomatics Engineering\n6.Bachelor of Science Geoinformatics\n7.Bachelor of Science Land Administration and Development\n8.Bachelor of Real Estate\n9.Bachelor of Science in Construction\n",
                    "Faculty of Social Sciences and Humanities:\n1.Bachelor of Technology with Education (Building Construction)\n2.Bachelor of Technology with Education (Electric and Electronic)\n3.Bachelor of Technology with Education (Mechanical Engineering)\n4.Bachelor of Technology with Education (Design and Technology)\n5.Bachelor of Education (Teaching English as a Second Language)\n6.Bahcelor of Education (Islamic Studies)\n7.Bachelor of Science (Sports Science)\n8.Bachelor of Science (Mathematics)\n9.Bachelor of Science with Education (Physics)\n10.Bachelor of Science with Education (Chemistry)\n11.Bachelor of Science (Human Resource Development)\n12.Bachelor of Psychology with Human Resource Development\n",
                    "Faculty of Management:\n1.Bachelor of Accounting\n2.Bachelor of Management (Marketing)\n3.Bachelor of Management (Techonology)\n",
                    "Razak Faculty of Technology and Informatics:\n1.Bachelor of Science (Industrial Design)\n",
                    "Malaysia-Japan International Institute of Technology:\n1.Bachelor of Electronic System Engineering\n2.Bachelor of Chemical Process Engineering\n3.Bachelor of Mechanical Precision Engineering\n4.Bachelor of Software Engineering\n5.Bachelor of Science (Industrial Mathematics)\n"]
                return random.choice(answer)
            elif intent == 'ask_about_faculty':
                answer = [
                    "Faculty of Civil Engineering\nFaculty of Mechanical Engineering\nFaculty of Chemical and Energy Engineering\nFaculty of Electrical Engineering\nFaculty of Build Environment and Surveying\nFaculty of Computing\nFaculty of Science\nFaculty of Social Sciences and Humanities\nFaculty of Management\nRazak Faculty of Technology and Informatics\nAzman Hashim International Business School\nMalaysia-Japan International Institute of Technology\n"]
                return random.choice(answer)
            elif intent == 'ask_about_arked':
                answer = ["Arked Meranti\nArked Angkasa\nArked Cengal\nArked Lestari\nArked N24\nArked Perdana\n"]
                return random.choice(answer)
            elif intent == 'ask_about_fees':
                answer = ["Bachelor of Computer Science: RM10760.00\n",
                          "Bachelor of Engineering: RM11200.00\n",
                          "Bachelor of Architecture: RM8610.00\n",
                          "Bachelor of Education: RM10760.\n",
                          "Bachelor of Sciences: RM10760.00\n",
                          "Bachelor of HRD, Business and Management: RM9880.00\n",
                          "Bachelor of Humanities and Social Sciences: RM9880.00\n",
                          "Bachelor of Quantity Surveying: RM11080.00\n",
                          "Bachelor of Data Engineering (2u2i): RM13120.00\n",
                          "Bachelor of Equine Management: RM18936.00\n",
                          "Bachelor of Electronic System Engineering (Japan International Institute of Technology): RM40000.00\n",
                          "Bachelor of Mechanical Precision Engineering (Japan International Institute of Technology): RM40000.00\n",
                          "Bachelor of Chemical Process Engineering (Japan International Institute of Technology): RM40000.00\n"]
                return random.choice(answer)
            elif intent == 'ask_about_public_holidaysjb':
                answer = [
                    "1.Deepavali (12 Nov 2023 - Sunday)\n2.Christmas Day (25 Dec 2023 - Monday)\n3.Thaipusam (25 Jan 2024 - Thursday)\n4.Chinese New Year (10, 11 Feb 2024 - Saturday & Sunday)\n5.Awal Ramadhan (11 Mar 2024 - Monday)\n6.Sultan Johor’s Birthday (23 Mar 2024 - Saturday)\n7.Aidilfitri Eid (10, 11 Apr 2024 - Wednesday & Thursday)\n8.Labour Day (1 May 2024 - Wednesday)\n9.Wesak Day (22 May 2024 - Wednesday)\n10.Hari Keputeraan YDP Agong (3 Jun 2024 - Monday)\n11.Aidiladha Eid (17 Jun 2024 - Monday)\n12.Awal Muharram (8 Jul 2024 - Monday)\n"]
                return random.choice(answer)
            elif intent == 'ask_about_public_holidayskl':
                answe = [
                    "1.Deepavali (13 Nov 2023 - Monday)\n2.Christmas Day (25 Dec 2023 - Monday)\n3.New Year’s Day (1 Jan 2024 - Monday)\n4.Thaipusam (25 Jan 2024 - Thursday)\n5.Federal Territory Day (1 Feb 2024 - Thursday)\n6.Chinese New Year (10, 11, 12 Feb 2024 - Saturday, Sunday & Monday)\n7.Awal Ramadhan (11 Mar 2024 - Monday)\n8.Nurul Al-Quran  (28 Mar 2024 -Thursday)\n9.Aidilfitri Eid (10, 11 Apr 2024 - Wednesday & Thursday)\n10.Labour Day (1 May 2024 - Wednesday)\n11.Wesak Day (22 May 2024 - Wednesday)\n12.Hari Keputeraan YDP Agong (3 Jun 2024 - Monday)\n13.Aidiladha Eid (17 Jun 2024 - Monday)\n"]
                return random.choice(answer)
            elif intent == 'ask_about_sembreakjb':
                answer = [
                    "Semester I: \nMid-Semester Break (26 Nov until 2 Dec 2024 - 1 week)\nFinal Break (21 Feb until 16 Mar 2024 - 4 weeks)\n\nSemester II: \nMid-Semester Break (5 May until 11 May 2024 - 1 week)\nFinal Break (28 Jul until 3 Oct 2024 - 10 weeks)\n"]
                return random.choice(answer)
            elif intent == 'ask_about_sembreakkl':
                answer = [
                    "Semester I: \nMid-Semester Break (27 Nov until 3 Dec 2024 - 1 week)\nFinal Break (21 Feb until 17 Mar 2024 - 4 weeks)\n\nSemester II: \nMid-Semester Break (6 May until 12 May 2024 - 1 week)\nFinal Break (29 Jul until 4 Oct 2024 - 10 weeks)\n"]
                return random.choice(answer)
            elif intent == 'ask_about_utm':
                answer = [
                    "University Teknologi Malaysia is Malaysia’s Premier University in Engineering and technology. According to QS University Rankings, UTM is a highly regarded public research-intensive university in Malaysia, ranked 188th in the world. UTM has three campuses which are Skudai, Kuala Lumpur and Pagoh. The Skudai campus is the largest public university in Malaysia and is the main campus of UTM. It is the first university in the state of Johor.\n",
                    "The top engineering and technology university in Malaysia is called University Teknologi Malaysia. It is ranked 188th in the world by QS University Rankings. UTM is a well-known public research-intensive university in Malaysia. There are three campuses of UTM: Pagoh, Skudai, and Kuala Lumpur. The main campus of UTM is located in Skudai, which is the largest public university in Malaysia. It is the state of Johor's first university.\n"]
                return random.choice(answer)
            elif intent == 'ask_about_club':
                answer = [
                    "Cluster Academic Business, Social Science And Humanities:\n1.Persatuan Pengurusan Teknologi\n2.Accounting Club\n3.Student of Human Resource Developmentn\n4.Kelab Psycology Interactive\n5.Per. Mahasiswa Pendidikan\n",
                    "Cluster Supreme:\n1.Class A - 5 Execellence Track Programme (5 ETP)\n2.Class B - Kelab Fotokreatif\n3.Class C - Student Union Task Force\n4.Class D - Alumni Utm\n5.Class E - Campus Election Committee",
                    "Cluster Academic Engineering:\n1.Class A\n- Persatuan Mahasiswa Kejuruteraan Gas (GESS)\n- Persatuan Mahasiswa Kejuruteraan Kimia (AICHE)\n- SC Petroleum Engineering Student Society (NESS)\n- Bioprocess Engineering Student Society (BIOSS)\n\n2.Class B\n- Persatuan Pelajar Kejiuruteraan Elektrik (JURUTEK)\n- Institute of Electrical and Electronics Engineers (IEEE)\n- Robocon UTM\n- Jazari Innovation Club\n- Kelab Kenderaan Elektrik (EVOLT)\n- Institute of Engineering and Technology (IET)\n\nClass C\n- Persatuan Kejuruteraan Awan (PEKA)\n\nClass D\n- SC manufacturing Engineering (SME)\n- Persatuan Pelajar Kejiriteraan Mekanikal (PETERA)\n- Persatuan Teknologi Marin (TEKNOMARIN)\n- Student Chapter Automative Engineering (SAE)\n- Kelab Automative Technology (AUTECH)\n- Kelab Kaji Terbang (AERO)\n -Kelab Kejuruteraan Industri (IEC)\n\nClass E\n- Persatuan Pelajar Kejuruteraan Bioperubatan & Sains Kesihatan (BIOMEHS)\n- Equine Scholar Society (ESS)\n\nClass F\n- Persatuan Sains Komputer (PERSAKA)\n- Persatuan Grafik Komputer & Multimedia (CGMA)\n",
                    "Cluster Science, Built Environment and Surveying:\n1.Persatuan Sains dan Teknologi\n2.Kelab  Geoinformatik (GEOINFO)\n3.Persatuan Ukur Bahan & Pembinaan (QS-BINA)\n4.Kelab Pentadbiran & Pembangunan Tanah (LADS)\n5.Persatuan Seni Bina\n",
                    "Cluster Sports:\n1.E-Sports Club (ESC)\n2.Per. Seni Silat Cekak UTM (PSSC UTM)\n3.Per. Silat Gayung UTM (PSSG UTM)\n4.Student Recreation Club (SRC)\n5.UTM Football Club\n6.Kelab Ekuin\n",
                    "Cluster Culture and Arts:\n1.Askara Resak (KTDI)\n2.Cansellor Star (KTC)\n3.Kelab SEMASEH (K9)\n4.Purnama Nilam (KTHO)\n",
                    "Cluster Religion:\n1.Persatuan Mahasiswa Islam PMI\n2.Persatuan Mahasiswa Hindu PMH\n3.Persatuan Mahasiswa Sikh PMS\n4.Persatuan Mahasiswa Buddha PMB\n5.Ikatan Kristian IK\n6.Sahabat YADIM\n7.Kelab Iqra’\n8.Biro Kerohanian 11 Kolej Kediaman Pelajar\n9.Rakan Pusat Islam\n",
                    "Cluster Entrepreneurship:\n1.Kelab Usahawan UTM\n2.Entrepreneurial Action Us (ENACTUS)\n3.Sekretariat Rakan Muda (SRM)\n",
                    "Cluster International:\n1.ISS Central\n2.ISS China\n3.ISS Bangladesh\n4.ISS Bangladesh\n5.ISS Indonesia\n6.ISS India\n7.ISS Iran\n8.ISS Iraq\n9.ISS Jordan\n10.ISS Libya\n11.ISS Nigeria\n12.ISS Palestine\n13.ISS Pakistan\n14.ISS Sudan\n15.ISS Yemen\n16.ISS Saudi Arabia\n17.ISS Afghanistan\n18.Global Buddies\n",
                    "Cluster Postgraduates:\n1.PGSS UTM\n2.PGSS SC\n3.PGSS FS\n4.PGSS FE\n5.PGSS SKA\n6.PGSS SKE\n7.PGSS FABU\n8.PGSS SKM SKBSK\n9.PGSS AHIBS JB\n",
                    "Cluster Uniform:\n1.Kumpulan Latihan Kelanasiswa (KLKM)\n2.Siswa Siswi Pertahanan Awam (SISPA)\n3.PALAPES\n4.SUKSIS\n5.Pandu Puteri\n",
                    "Cluster Residential Colleges:\n1.JKM Kolej Tunku Razak\n2.JKM Kolej Tun Hussein Onn\n3.JKM Koej Tun Dr Ismail\n4.JKM Kolej Datin Seri Endon\n5.JKM Kolej Dato’ Onn Jaafar\n6.JKM Kolej Perdana\n7.JKM Kolej Tuanku Canselor\n8.JKM Kolej 9 & 10\n9.JKM Kolej Rahman Putra\n10.JKM Kolej Tun Fatimah\n11.JKM Kolej Siswa Jaya UTMKL\n",
                    "Cluster Non-Academic:\n1.Kelab PEMADAM\n2.Kelab Debat & Pidato (DE’PIKIR)\n3.Gerakan Pengguna Siswa (GPS)\n4.Sekretariat Rakan Badan Pencegah\n5.Rasuah (SPRa UTM)\n6.Kelab Kaunseling dan Kerjaya (KKDK)\n7.Persatuan Pembimbing Rakan Sebaya (PERSIS)\n8.Kelab Volunteer@UTM\n",
                    "Clustr General:\n1.The Institution of Engineers, Malaysia UTM Student Section (IEM-UTM SS)\n2.Tuanku Chancellor English Language Club (TCELC UTM)\n3.Bursa Young Investor Club\n4.Kelab UNESCO\n5.Kelab Bahasa Mandarin UTM\n6.SC Goldenkey Honour Society Club (TOASTMAKER)\n7.Student Chapter AIESEC (AIESEC)\n8.TED X UTM\n",
                    "Cluster State:\n1.Perwakilan Anak Sarawak (MASSA)\n2.Perwaklan Mahasiswa Sabah (PERMAS)\n3.Sekretariat Anak Perak\n4.Himpunan Siswazah Kelantan\n5.Semua perwakilan Anak Negeri Semenanjung\n6.Persatuan Mahasiswa Anak Terengganu\n7.Sekretariat Mahasiswa Anak Negeri Sembilan\n8.Persatuan Anak Felda (PERSADA)\n9.Sekretariat Anak Johor\n"]
                return random.choice(answer)
            elif intent == 'ask_about_library':
                answer = [
                    "1.Perpustakaan Raja Zarith Sofiah (PRZS), UTM Johor Bahru\n2.Perpustakaan Sultanah Zanariah, UTM Johor Bahru\n3.Menara Razak Library, UTM Kuala Lumpur\n4.MJIIT Library, UTM Kuala Lumpur\n5.UTM Pagoh Library\n6.The Institute of Bioproduct (IBD) Library, UTM Johor Bahru\n"]
                return random.choice(answer)
            elif intent == 'ask_about_transportation':
                answer = ["Bus A to H\n"]
                return random.choice(answer)
            elif intent == 'ask_about_kolej':
                answer = [
                    "There are 10 kolej provided.\n1.Kolej Rahman Putra\n2.Kolej Tun Fatimah\n3.Kolej Tun Razak\n4.Kolej Tun Hussein Onn\n5.Kolej Tun Dr. Ismail\n6.Kolej Tuanku Canselor\n7.Kolej Perdana\n8.Kolej 9 Dan 10\n9.Kolej Datin Seri Endon\n10.Koleh Dato'Onn Jaafar\n"]
                return random.choice(answer)
            elif intent == 'ask_about_facilities':
                answer = [
                    "1.Computer Lab\n2.Seminar Hall\n3.Lectures Room\n4.Meeting Room\n5.Kejora Hall\n6.CCNP Network Lab\n7.Tutorial Room\n8.Discussion Room\n9.Activity Learning Lab\n10.Sports Hall\n11.Padang\n"]
                return random.choice(answer)
            elif intent == 'ask_about_query':
                answer = ["Hi, I am glad that you are reaching me.Feel free to ask me your questions.",
                          "Hello, please tell me your queries."]
                return random.choice(answer)
            elif intent == 'ask_about_question':
                answer = ["Hi, I am glad that you are reaching me.Feel free to ask me your questions.",
                          "Hello, please tell me your queries."]
                return random.choice(answer)
            elif intent == 'hi':
                answer = ["Hi, I am glad that you are reaching me.Feel free to ask me your questions.",
                          "Hello, please tell me your queries."]
                return random.choice(answer)
            elif intent == 'hello':
                answer = ["Hi, I am glad that you are reaching me.Feel free to ask me your questions.",
                          "Hello, please tell me your queries."]
                return random.choice(answer)
            elif intent == 'bye':
                answer = ["Thank you for chatting with me!It was a pleasure,see you again",
                          "Thanks for visiting me, and have a nice day!",
                          "Thank you for your time!Goodbye"]
                return random.choice(answer)
            elif intent == 'goodbye':
                answer = ["Thank you for chatting with me!It was a pleasure,see you again",
                          "Thanks for visiting me, and have a nice day!",
                          "Thank you for your time!Goodbye"]
                return random.choice(answer)
            elif intent == 'thank you':
                answer = ["Thank you for chatting with me!It was a pleasure,see you again",
                          "Thanks for visiting me, and have a nice day!",
                          "Thank you for your time!Goodbye"]
                return random.choice(answer)
            elif intent == 'thanks':
                answer = ["Thank you for chatting with me! It was a pleasure, see you again",
                          "Thanks for visiting me, and have a nice day!",
                          "Thank you for your time! Goodbye"]
                return random.choice(answer)
    if answer is not None:
        print("Answer:", answer)
    else:
        print("Sorry,I have no idea")

    return answer


if __name__ == "__main__":
    app.run()
