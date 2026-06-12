import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Configurare pagină
st.set_page_config(
    page_title="ONU: 80 de Ani de Istorie și Geopolitică",
    page_icon="🌍",
    layout="wide"
)

# CSS custom
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1e3a8a;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #64748b;
        text-align: center;
        margin-bottom: 2rem;
    }
    .timeline-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 1rem;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .timeline-year {
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .timeline-event {
        font-size: 1.1rem;
    }
    .timeline-category {
        font-size: 0.9rem;
        opacity: 0.9;
        margin-top: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================
# DATE - ȚĂRI MEMBRE ONU
# ============================================
tari_lista = [
    ('China', 'Beijing', 'Asia', 1945, 1412, 35.86, 104.20),
    ('Franța', 'Paris', 'Europa', 1945, 68, 46.23, 2.21),
    ('Rusia', 'Moscova', 'Europa', 1945, 144, 61.52, 105.32),
    ('Regatul Unit', 'Londra', 'Europa', 1945, 67, 55.38, -3.44),
    ('SUA', 'Washington', 'N.America', 1945, 331, 37.09, -95.71),
    ('Argentina', 'Buenos Aires', 'S.America', 1945, 45, -38.42, -63.62),
    ('Brazilia', 'Brasilia', 'S.America', 1945, 213, -14.24, -51.93),
    ('Chile', 'Santiago', 'S.America', 1945, 19, -35.68, -71.54),
    ('Cuba', 'Havana', 'N.America', 1945, 11, 21.52, -77.78),
    ('Egipt', 'Cairo', 'Africa', 1945, 104, 26.10, 30.04),
    ('Iran', 'Tehran', 'Asia', 1945, 84, 32.43, 53.69),
    ('India', 'New Delhi', 'Asia', 1945, 1380, 20.59, 78.96),
    ('Australia', 'Canberra', 'Oceania', 1945, 26, -25.27, 133.78),
    ('Grecia', 'Atena', 'Europa', 1945, 10, 39.07, 21.82),
    ('Afganistan', 'Kabul', 'Asia', 1946, 40, 33.94, 67.71),
    ('Suedia', 'Stockholm', 'Europa', 1946, 10, 60.13, 18.64),
    ('Pakistan', 'Islamabad', 'Asia', 1947, 225, 30.38, 69.35),
    ('Albania', 'Tirana', 'Europa', 1955, 2.8, 41.15, 20.17),
    ('Austria', 'Viena', 'Europa', 1955, 9, 47.52, 14.55),
    ('Bulgaria', 'Sofia', 'Europa', 1955, 6.8, 42.73, 25.49),
    ('Finlanda', 'Helsinki', 'Europa', 1955, 5.5, 61.92, 25.75),
    ('Irlanda', 'Dublin', 'Europa', 1955, 5, 53.14, -7.69),
    ('Italia', 'Roma', 'Europa', 1955, 59, 41.87, 12.57),
    ('Japonia', 'Tokyo', 'Asia', 1956, 125, 36.20, 138.25),
    ('Maroc', 'Rabat', 'Africa', 1956, 37, 31.79, -7.09),
    ('Nigeria', 'Abuja', 'Africa', 1960, 211, 9.08, 8.68),
    ('Ghana', 'Accra', 'Africa', 1957, 31, 7.95, -1.02),
    ('Algeria', 'Algiers', 'Africa', 1962, 44, 28.03, 1.66),
    ('Kenya', 'Nairobi', 'Africa', 1963, 54, -0.02, 37.91),
    ('Indonezia', 'Jakarta', 'Asia', 1950, 274, -0.79, 113.92),
    ('Turcia', 'Ankara', 'Asia', 1945, 84, 38.96, 35.24),
    ('Germania', 'Berlin', 'Europa', 1973, 83, 51.17, 10.45),
    ('Spania', 'Madrid', 'Europa', 1955, 47, 40.46, -3.75),
    ('Canada', 'Ottawa', 'N.America', 1945, 38, 56.13, -106.35),
    ('Mexic', 'Mexico City', 'N.America', 1945, 126, 23.63, -102.55),
    ('Etiopia', 'Addis Ababa', 'Africa', 1945, 115, 9.15, 40.49),
    ('Africa de Sud', 'Pretoria', 'Africa', 1945, 60, -30.56, 22.94),
    ('Ecuador', 'Quito', 'S.America', 1945, 17.6, -1.83, -78.18),
    ('Peru', 'Lima', 'S.America', 1945, 33, -9.19, -75.02),
    ('Venezuela', 'Caracas', 'S.America', 1945, 28, 6.42, -66.59),
    ('Columbia', 'Bogota', 'S.America', 1945, 51, 4.57, -74.30),
    ('Ucraina', 'Kiev', 'Europa', 1945, 44, 48.38, 31.17),
    ('Polonia', 'Varșovia', 'Europa', 1945, 38, 51.92, 19.15),
    ('România', 'București', 'Europa', 1955, 19, 45.94, 24.97),
    ('Ungaria', 'Budapesta', 'Europa', 1955, 9.6, 47.16, 19.41),
    ('Cehia', 'Praga', 'Europa', 1993, 10.7, 49.82, 15.47),
    ('Serbia', 'Belgrad', 'Europa', 2000, 6.9, 44.02, 20.91),
    ('Croația', 'Zagreb', 'Europa', 1992, 4, 45.10, 15.20),
    ('Bosnia', 'Sarajevo', 'Europa', 1992, 3.3, 43.92, 18.34),
    ('Slovenia', 'Ljubljana', 'Europa', 1992, 2.1, 46.15, 14.99),
    ('Elveția', 'Berna', 'Europa', 2002, 8.6, 46.82, 8.23),
    ('Norvegia', 'Oslo', 'Europa', 1945, 5.4, 60.47, 8.47),
    ('Danemarca', 'Copenhaga', 'Europa', 1945, 5.8, 56.26, 9.50),
    ('Islanda', 'Reykjavik', 'Europa', 1946, 0.37, 64.96, -19.02),
    ('Portugalia', 'Lisabona', 'Europa', 1955, 10, 39.40, -8.22),
    ('Belgia', 'Bruxelles', 'Europa', 1945, 11.5, 50.50, 4.47),
    ('Olanda', 'Amsterdam', 'Europa', 1945, 17.4, 52.13, 5.29),
    ('Luxemburg', 'Luxembourg', 'Europa', 1945, 0.6, 49.82, 6.13),
    ('Malta', 'Valletta', 'Europa', 1964, 0.5, 35.94, 14.38),
    ('Cipru', 'Nicosia', 'Europa', 1960, 1.2, 35.13, 33.43),
    ('Estonia', 'Tallinn', 'Europa', 1991, 1.3, 58.60, 25.01),
    ('Letonia', 'Riga', 'Europa', 1991, 1.9, 56.88, 24.60),
    ('Lituania', 'Vilnius', 'Europa', 1991, 2.8, 55.17, 23.88),
    ('Moldova', 'Chisinau', 'Europa', 1992, 2.6, 47.41, 28.37),
    ('Georgia', 'Tbilisi', 'Asia', 1992, 3.7, 42.32, 43.36),
    ('Armenia', 'Erevan', 'Asia', 1992, 3, 40.07, 45.04),
    ('Azerbaidjan', 'Baku', 'Asia', 1992, 10, 40.14, 47.58),
    ('Kazahstan', 'Astana', 'Asia', 1992, 19, 48.02, 66.92),
    ('Uzbekistan', 'Tashkent', 'Asia', 1992, 34, 41.38, 64.59),
    ('Vietnam', 'Hanoi', 'Asia', 1977, 97, 14.06, 108.28),
    ('Thailanda', 'Bangkok', 'Asia', 1946, 70, 15.87, 100.99),
    ('Coreea de Sud', 'Seoul', 'Asia', 1991, 52, 35.91, 127.77),
    ('Coreea de Nord', 'Phenian', 'Asia', 1991, 26, 40.34, 127.51),
    ('Filipine', 'Manila', 'Asia', 1945, 110, 12.88, 121.77),
    ('Malaezia', 'Kuala Lumpur', 'Asia', 1957, 32, 4.21, 101.98),
    ('Singapore', 'Singapore', 'Asia', 1965, 5.7, 1.35, 103.82),
    ('Bangladesh', 'Dhaka', 'Asia', 1974, 166, 23.68, 90.36),
    ('Sri Lanka', 'Colombo', 'Asia', 1955, 22, 7.87, 80.77),
    ('Nepal', 'Kathmandu', 'Asia', 1955, 30, 28.39, 84.12),
    ('Myanmar', 'Naypyidaw', 'Asia', 1948, 54, 21.91, 96.07),
    ('Cambodgia', 'Phnom Penh', 'Asia', 1955, 17, 12.57, 104.99),
    ('Laos', 'Vientiane', 'Asia', 1955, 7.3, 19.86, 102.50),
    ('Mongolia', 'Ulaanbaatar', 'Asia', 1961, 3.3, 46.86, 103.85),
    ('Tadjikistan', 'Dushanbe', 'Asia', 1992, 9.5, 38.86, 71.28),
    ('Kârgâzstan', 'Bishkek', 'Asia', 1992, 6.5, 41.20, 74.77),
    ('Turkmenistan', 'Ashgabat', 'Asia', 1992, 6, 38.97, 59.56),
    ('Arabia Saudită', 'Riyadh', 'Asia', 1945, 35, 23.89, 45.08),
    ('Emiratele Arabe Unite', 'Abu Dhabi', 'Asia', 1971, 9.9, 23.42, 53.85),
    ('Qatar', 'Doha', 'Asia', 1971, 2.9, 25.35, 51.18),
    ('Kuwait', 'Kuwait City', 'Asia', 1963, 4.3, 29.31, 47.48),
    ('Oman', 'Muscat', 'Asia', 1971, 5.1, 21.47, 55.98),
    ('Bahrain', 'Manama', 'Asia', 1971, 1.7, 25.93, 50.64),
    ('Iordania', 'Amman', 'Asia', 1945, 10, 30.59, 35.93),
    ('Israel', 'Ierusalim', 'Asia', 1949, 9, 31.05, 34.85),
    ('Liban', 'Beirut', 'Asia', 1945, 6, 33.85, 35.86),
    ('Siria', 'Damascus', 'Asia', 1945, 18, 33.51, 36.28),
    ('Irak', 'Baghdad', 'Asia', 1945, 40, 33.22, 43.68),
    ('Yemen', 'Sanaa', 'Asia', 1947, 30, 15.55, 48.52),
    ('Libia', 'Tripoli', 'Africa', 1955, 7, 26.34, 17.23),
    ('Tunisia', 'Tunis', 'Africa', 1956, 12, 33.89, 10.18),
    ('Sudan', 'Khartoum', 'Africa', 1956, 45, 15.18, 30.22),
    ('Somalia', 'Mogadishu', 'Africa', 1960, 16, 5.15, 46.20),
    ('Djibouti', 'Djibouti', 'Africa', 1977, 1, 11.83, 42.59),
    ('Eritreea', 'Asmara', 'Africa', 1993, 3.6, 15.18, 37.45),
    ('Uganda', 'Kampala', 'Africa', 1962, 47, 1.37, 32.58),
    ('Tanzania', 'Dodoma', 'Africa', 1961, 61, -6.37, 34.89),
    ('Rwanda', 'Kigali', 'Africa', 1962, 13, -1.94, 30.06),
    ('Burundi', 'Gitega', 'Africa', 1962, 12, -3.37, 29.87),
    ('Republica Centrafricană', 'Bangui', 'Africa', 1960, 5, 6.61, 20.94),
    ("Ciad", "N\'Djamena", 'Africa', 1960, 17, 15.45, 18.73),
    ('Niger', 'Niamey', 'Africa', 1960, 24, 17.61, 8.08),
    ('Mali', 'Bamako', 'Africa', 1960, 20, 17.57, -4.00),
    ('Burkina Faso', 'Ouagadougou', 'Africa', 1960, 21, 12.24, -1.56),
    ('Guineea', 'Conakry', 'Africa', 1958, 13, 9.95, -13.68),
    ('Sierra Leone', 'Freetown', 'Africa', 1961, 8, 8.46, -12.30),
    ('Liberia', 'Monrovia', 'Africa', 1945, 5, 6.43, -10.80),
    ('Togo', 'Lome', 'Africa', 1960, 8, 8.62, 1.23),
    ('Benin', 'Porto-Novo', 'Africa', 1960, 12, 9.31, 2.32),
    ('Coasta de Fildeș', 'Yamoussoukro', 'Africa', 1960, 27, 7.54, -5.55),
    ('Senegal', 'Dakar', 'Africa', 1960, 17, 14.50, -17.37),
    ('Gambia', 'Banjul', 'Africa', 1965, 2.4, 13.44, -16.58),
    ('Guineea-Bissau', 'Bissau', 'Africa', 1974, 2, 11.80, -15.60),
    ('Capul Verde', 'Praia', 'Africa', 1975, 0.55, 14.92, -23.04),
    ('Sao Tome', 'Sao Tome', 'Africa', 1975, 0.22, 0.19, 6.61),
    ('Gabon', 'Libreville', 'Africa', 1960, 2, 0.80, 11.61),
    ('Congo', 'Brazzaville', 'Africa', 1960, 6, -4.04, 15.83),
    ('Congo (RDC)', 'Kinshasa', 'Africa', 1960, 90, -0.23, 21.76),
    ('Angola', 'Luanda', 'Africa', 1976, 33, -11.20, 13.25),
    ('Mozambic', 'Maputo', 'Africa', 1975, 32, -18.67, 35.53),
    ('Zambia', 'Lusaka', 'Africa', 1964, 18, -13.13, 27.85),
    ('Zimbabwe', 'Harare', 'Africa', 1980, 15, -19.02, 23.43),
    ('Botswana', 'Gaborone', 'Africa', 1966, 2.4, -22.33, 30.80),
    ('Namibia', 'Windhoek', 'Africa', 1990, 2.5, -22.96, 17.19),
    ('Eswatini', 'Mbabane', 'Africa', 2018, 1.16, -26.52, 31.53),
    ('Lesotho', 'Maseru', 'Africa', 1966, 2.1, -29.61, 27.72),
    ('Madagascar', 'Antananarivo', 'Africa', 1960, 28, -18.77, 46.87),
    ('Mauritius', 'Port Louis', 'Africa', 1968, 1.26, -20.35, 57.55),
    ('Seychelles', 'Victoria', 'Africa', 1976, 0.1, -4.68, 55.49),
    ('Comore', 'Moroni', 'Africa', 1975, 0.87, -11.65, 43.33),
    ('Maldives', 'Male', 'Asia', 1965, 0.54, 3.20, 73.22),
    ('Fiji', 'Suva', 'Oceania', 1970, 0.9, -16.58, 179.41),
    ('Papua Noua Guinee', 'Port Moresby', 'Oceania', 1975, 9, -6.31, 143.96),
    ('Samoa', 'Apia', 'Oceania', 1976, 0.2, -13.76, -171.76),
    ("Tonga", "Nuku\'alofa", 'Oceania', 1999, 0.1, -21.18, -175.20),
    ('Vanuatu', 'Port Vila', 'Oceania', 1981, 0.31, -15.38, 166.96),
    ('Solomon Islands', 'Honiara', 'Oceania', 1978, 0.7, -9.65, 159.16),
    ('Kiribati', 'Tarawa', 'Oceania', 1999, 0.12, 1.87, 173.00),
    ('Nauru', 'Yaren', 'Oceania', 1999, 0.01, -0.52, 166.93),
    ('Tuvalu', 'Funafuti', 'Oceania', 2000, 0.012, -7.11, 177.65),
    ('Palau', 'Ngerulmud', 'Oceania', 1994, 0.018, 7.51, 134.58),
    ('Marshall Islands', 'Majuro', 'Oceania', 1991, 0.06, 7.13, 171.18),
    ('Micronezia', 'Palikir', 'Oceania', 1991, 0.115, 6.89, 158.22),
    ('Noua Zeelandă', 'Wellington', 'Oceania', 1945, 5, -40.90, 174.89),
    ('Guatemala', 'Guatemala City', 'N.America', 1945, 17, 15.78, -90.23),
    ('Honduras', 'Tegucigalpa', 'N.America', 1945, 10, 15.20, -86.24),
    ('El Salvador', 'San Salvador', 'N.America', 1945, 6.7, 13.79, -88.90),
    ('Nicaragua', 'Managua', 'N.America', 1945, 6.5, 12.87, -85.21),
    ('Costa Rica', 'San Jose', 'N.America', 1945, 5.1, 9.75, -83.75),
    ('Panama', 'Panama City', 'N.America', 1945, 4.3, 8.54, -80.78),
    ('Jamaica', 'Kingston', 'N.America', 1962, 2.9, 18.11, -77.30),
    ('Haiti', 'Port-au-Prince', 'N.America', 1945, 11, 18.97, -72.29),
    ('Republica Dominicană', 'Santo Domingo', 'N.America', 1945, 11, 18.74, -69.99),
    ('Trinidad și Tobago', 'Port of Spain', 'N.America', 1962, 1.4, 10.69, -61.22),
    ('Barbados', 'Bridgetown', 'N.America', 1966, 0.28, 13.19, -59.54),
    ('Saint Lucia', 'Castries', 'N.America', 1979, 0.18, 13.91, -60.98),
    ("Grenada", "St. George\'s", 'N.America', 1974, 0.11, 12.12, -61.68),
    ('Saint Vincent', 'Kingstown', 'N.America', 1980, 0.11, 13.25, -61.20),
    ('Antigua', 'St. John\'s', 'N.America', 1981, 0.1, 17.06, -61.80),
    ('Saint Kitts', 'Basseterre', 'N.America', 1983, 0.05, 17.36, -62.78),
    ('Dominica', 'Roseau', 'N.America', 1978, 0.07, 15.42, -61.37),
    ('Belize', 'Belmopan', 'N.America', 1981, 0.4, 17.19, -88.50),
    ('Guyana', 'Georgetown', 'S.America', 1966, 0.79, 4.86, -58.93),
    ('Surinam', 'Paramaribo', 'S.America', 1975, 0.59, 3.92, -56.03),
    ('Bolivia', 'Sucre', 'S.America', 1945, 11.7, -16.29, -65.12),
    ('Paraguay', 'Asuncion', 'S.America', 1945, 7, -23.44, -58.44),
    ('Uruguay', 'Montevideo', 'S.America', 1945, 3.5, -32.52, -55.77),
    ('Bahamas', 'Nassau', 'N.America', 1973, 0.39, 25.03, -77.40),
]

coloane = ['tara', 'capitala', 'continent', 'an_aderare', 'populatie_mil', 'lat', 'lon']
df_tari = pd.DataFrame(tari_lista, columns=coloane)

# Evenimente istorice ONU
evenimente_data = {
    'an': [1945, 1945, 1946, 1948, 1950, 1956, 1960, 1961, 1962, 1963,
           1965, 1968, 1971, 1972, 1975, 1979, 1982, 1991, 1992, 2000,
           2002, 2005, 2011, 2015, 2020, 2024, 2025],
    'eveniment': [
        'Conferința de la San Francisco - Fondarea ONU',
        'Intrarea în vigoare a Cartei ONU (24 octombrie)',
        'Prima Adunare Generală la Londra',
        'Declarația Universală a Drepturilor Omului',
        'Războiul din Coreea - Rezoluție de intervenție',
        'Criza Suezului - Prima misiune de menținere a păcii (UNEF)',
        'Anul Africii - 17 noi state membre',
        'Secretarul General Dag Hammarskjöld moare în accident',
        'Criza rachetelor din Cuba',
        'Tratatul de Neproliferare Nucleară (NPT)',
        'Crearea programului UN Development Programme (UNDP)',
        'Tratatul de Neproliferare Nucleară intră în vigoare',
        'Admiterea Chinei (Republica Populară) și expulzarea Taiwanului',
        'Conferința de la Stockholm despre Mediu',
        'Conferința de la Helsinki pentru Securitate',
        'Convenția CEDAW - Eliminarea discriminării femeilor',
        'Conferința de la Viena pentru Drepturile Omului',
        'Sfârșitul Războiului Rece - ONU supervizează tranziții',
        'Operațiunea de relief în Somalia (UNOSOM)',
        'Adoptarea Millennium Development Goals',
        'Intrarea Elveției în ONU (referendum)',
        'Reforma ONU propusă de Kofi Annan',
        'Criza din Libia - Rezoluție 1973',
        'Adoptarea Obiectivelor de Dezvoltare Durabilă (SDG)',
        'Răspunsul ONU la pandemia COVID-19',
        'Conflictul din Gaza - Rezoluții pentru încetarea focului',
        '80 de ani de la fondarea ONU'
    ],
    'categorie': ['Fondare', 'Fondare', 'Instituțional', 'Drepturi', 'Securitate',
                  'Pace', 'Extindere', 'Instituțional', 'Securitate', 'Dezarmare',
                  'Dezvoltare', 'Dezarmare', 'Extindere', 'Mediu', 'Securitate',
                  'Drepturi', 'Drepturi', 'Tranziție', 'Umanitar', 'Dezvoltare',
                  'Extindere', 'Reformă', 'Securitate', 'Dezvoltare', 'Sănătate',
                  'Securitate', 'Aniversare'],
    'importanta': [10, 10, 7, 9, 8, 9, 10, 8, 9, 10,
                   8, 9, 9, 7, 7, 8, 8, 10, 8, 9,
                   7, 8, 9, 10, 9, 9, 10]
}

df_evenimente = pd.DataFrame(evenimente_data)

# Secretari Generali
secretari_data = {
    'nume': ['Trygve Lie', 'Dag Hammarskjöld', 'U Thant', 'Kurt Waldheim', 
             'Javier Pérez de Cuéllar', 'Boutros Boutros-Ghali', 'Kofi Annan', 
             'Ban Ki-moon', 'António Guterres'],
    'tara': ['Norvegia', 'Suedia', 'Myanmar', 'Austria', 'Peru', 'Egipt', 'Ghana', 'Coreea de Sud', 'Portugalia'],
    'continent': ['Europa', 'Europa', 'Asia', 'Europa', 'S.America', 'Africa', 'Africa', 'Asia', 'Europa'],
    'mandat_start': [1946, 1953, 1961, 1972, 1982, 1992, 1997, 2007, 2017],
    'mandat_end': [1952, 1961, 1971, 1981, 1991, 1996, 2006, 2016, 2026]
}

df_secretari = pd.DataFrame(secretari_data)
df_secretari['durata'] = df_secretari['mandat_end'] - df_secretari['mandat_start']

# ============================================
# HEADER
# ============================================
st.markdown('<div class="main-header">🌍 Organizația Națiunilor Unite</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">80 de Ani de Istorie, Diplomație și Cooperare Internațională (1945–2025)</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("🌐 Țări Membre", "193")
with col2:
    st.metric("📅 Ani de Activitate", "80")
with col3:
    st.metric("🗣️ Limbi Oficiale", "6")
with col4:
    st.metric("🏢 Sediul Principal", "New York")

st.markdown("---")

# ============================================
# TABS
# ============================================

tab1, tab2, tab3, tab4 = st.tabs(["🗺️ Hartă Interactivă", "📊 Statistici & Grafice", "📜 Cronologie Istorică", "🏛️ Secretari Generali"])

# ============================================
# TAB 1: HARTĂ INTERACTIVĂ
# ============================================

with tab1:
    st.header("🗺️ Hartă Interactivă a Țărilor Membre")

    continente = ['Toate'] + sorted(df_tari['continent'].unique().tolist())
    continent_selectat = st.selectbox("Filtrează după continent:", continente)

    if continent_selectat != 'Toate':
        df_filtrat = df_tari[df_tari['continent'] == continent_selectat]
    else:
        df_filtrat = df_tari

    culori_continente = {
        'Europa': '#3b82f6', 'Asia': '#ef4444', 'Africa': '#10b981',
        'N.America': '#f59e0b', 'S.America': '#8b5cf6', 'Oceania': '#ec4899'
    }

    fig_harta = px.scatter_geo(
        df_filtrat,
        lat='lat',
        lon='lon',
        hover_name='tara',
        hover_data={
            'capitala': True,
            'continent': True,
            'an_aderare': True,
            'populatie_mil': ':.1f',
            'lat': False,
            'lon': False
        },
        color='continent',
        color_discrete_map=culori_continente,
        size='populatie_mil',
        size_max=30,
        projection='natural earth',
        title=f'Distribuția Geografică a Țărilor Membre ONU ({len(df_filtrat)} țări)'
    )

    fig_harta.update_layout(height=600, geo=dict(showframe=False, showcoastlines=True, projection_type='natural earth'))
    st.plotly_chart(fig_harta, use_container_width=True)

    st.subheader("📋 Lista Țărilor")
    col_a, col_b = st.columns(2)
    with col_a:
        st.dataframe(
            df_filtrat[['tara', 'capitala', 'continent', 'an_aderare', 'populatie_mil']]
            .sort_values('an_aderare')
            .rename(columns={
                'tara': 'Țara', 'capitala': 'Capitala', 'continent': 'Continent',
                'an_aderare': 'An Aderare', 'populatie_mil': 'Populație (mil)'
            }),
            use_container_width=True, height=400
        )
    with col_b:
        fig_pie = px.pie(
            df_tari.groupby('continent').size().reset_index(name='count'),
            values='count', names='continent', title='Distribuția Țărilor pe Continente',
            color='continent', color_discrete_map=culori_continente
        )
        st.plotly_chart(fig_pie, use_container_width=True)

# ============================================
# TAB 2: STATISTICI & GRAFICE - CORECTAT
# ============================================

with tab2:
    st.header("📊 Statistici și Analize")

    col1, col2 = st.columns(2)

    with col1:
        # Grafic curat de evoluție - FĂRĂ linii verticale suprapuse
        ani_aderare = df_tari['an_aderare'].value_counts().sort_index().cumsum()

        fig_evol = go.Figure()
        fig_evol.add_trace(go.Scatter(
            x=ani_aderare.index, y=ani_aderare.values, mode='lines+markers',
            name='Total Membri', line=dict(color='#3b82f6', width=3),
            fill='tozeroy', fillcolor='rgba(59, 130, 246, 0.2)'
        ))

        # Adăugăm DOAR puncte pentru evenimentele majore, nu linii verticale cu text
        evenimente_majore = df_evenimente[df_evenimente['importanta'] >= 9]
        fig_evol.add_trace(go.Scatter(
            x=evenimente_majore['an'],
            y=[ani_aderare.get(an, 0) for an in evenimente_majore['an']],
            mode='markers',
            marker=dict(size=12, color='red', symbol='star'),
            name='Evenimente Majore',
            hovertemplate='<b>%{text}</b><br>An: %{x}<br>Membri: %{y}<extra></extra>',
            text=evenimente_majore['eveniment']
        ))

        fig_evol.update_layout(
            title='Evoluția Numărului de Țări Membre (1945-2025)',
            xaxis_title='An',
            yaxis_title='Număr de Țări Membre',
            height=450,
            hovermode='x unified'
        )
        st.plotly_chart(fig_evol, use_container_width=True)

    with col2:
        df_tari['deceniu'] = (df_tari['an_aderare'] // 10) * 10
        decenii = df_tari['deceniu'].value_counts().sort_index()

        fig_bar = px.bar(x=decenii.index, y=decenii.values,
            labels={'x': 'Deceniu', 'y': 'Număr de Țări'},
            title='Valuri de Aderare pe Decenii',
            color=decenii.values, color_continuous_scale='Viridis')
        fig_bar.update_layout(height=450)
        st.plotly_chart(fig_bar, use_container_width=True)

    # Tabel cu evenimentele majore sub grafic
    st.subheader("⭐ Evenimente Majore Marcate pe Grafic")
    evenimente_majore_display = df_evenimente[df_evenimente['importanta'] >= 9][['an', 'eveniment', 'categorie']].sort_values('an')
    st.dataframe(evenimente_majore_display.rename(columns={
        'an': 'An', 'eveniment': 'Eveniment', 'categorie': 'Categorie'
    }), use_container_width=True, height=250)

    col3, col4, col5 = st.columns(3)

    with col3:
        st.subheader("🌍 Top 5 Continente")
        top_continente = df_tari['continent'].value_counts().head()
        fig_top = px.bar(x=top_continente.values, y=top_continente.index, orientation='h',
            color=top_continente.values, color_continuous_scale='Blues',
            labels={'x': 'Număr Țări', 'y': 'Continent'})
        st.plotly_chart(fig_top, use_container_width=True)

    with col4:
        st.subheader("📈 Top 10 Țări după Populație")
        top_pop = df_tari.nlargest(10, 'populatie_mil')[['tara', 'populatie_mil']]
        fig_pop = px.bar(top_pop, x='populatie_mil', y='tara', orientation='h',
            color='populatie_mil', color_continuous_scale='Reds',
            labels={'populatie_mil': 'Populație (milioane)', 'tara': 'Țara'})
        st.plotly_chart(fig_pop, use_container_width=True)

    with col5:
        st.subheader("🏛️ Analiză Temporală")
        inainte_1990 = len(df_tari[df_tari['an_aderare'] < 1990])
        dupa_1990 = len(df_tari[df_tari['an_aderare'] >= 1990])

        fig_timeline = px.pie(names=['Înainte de 1990', 'După 1990'],
            values=[inainte_1990, dupa_1990],
            title='Aderări: Războiul Rece vs. Post-Război Rece', hole=0.4)
        st.plotly_chart(fig_timeline, use_container_width=True)

# ============================================
# TAB 3: CRONOLOGIE ISTORICĂ
# ============================================

with tab3:
    st.header("📜 Cronologia Evenimentelor ONU")

    an_selectat = st.slider("Selectează anul pentru a vedea evenimentele:",
        min_value=1945, max_value=2025, value=1945, step=1)

    evenimente_an = df_evenimente[df_evenimente['an'] == an_selectat]

    if not evenimente_an.empty:
        for _, ev in evenimente_an.iterrows():
            st.markdown(f"""
                <div class="timeline-card">
                    <div class="timeline-year">📅 {ev['an']}</div>
                    <div class="timeline-event">{ev['eveniment']}</div>
                    <div class="timeline-category">🏷️ {ev['categorie']} | {'⭐' * ev['importanta']}</div>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Nu există evenimente majore documentate pentru acest an.")

    st.subheader("📊 Timeline Vizual Complet")

    fig_timeline = px.bar(
        df_evenimente.sort_values('an'),
        x='an',
        y='importanta',
        color='categorie',
        hover_data=['eveniment'],
        title='Evenimente ONU pe Ani și Importanță',
        labels={'an': 'An', 'importanta': 'Importanță (1-10)', 'categorie': 'Categorie'},
        height=500
    )
    fig_timeline.update_layout(xaxis_tickangle=-45, showlegend=True)
    st.plotly_chart(fig_timeline, use_container_width=True)

    st.subheader("📊 Distribuția Evenimentelor pe Categorii")

    cat_counts = df_evenimente['categorie'].value_counts().reset_index()
    cat_counts.columns = ['Categorie', 'Număr Evenimente']

    fig_cat = px.bar(
        cat_counts,
        x='Categorie',
        y='Număr Evenimente',
        color='Categorie',
        title='Numărul de Evenimente pe Categorii',
        height=400
    )
    st.plotly_chart(fig_cat, use_container_width=True)

    st.subheader("📋 Toate Evenimentele")
    st.dataframe(
        df_evenimente.sort_values('an')[['an', 'eveniment', 'categorie', 'importanta']]
        .rename(columns={'an': 'An', 'eveniment': 'Eveniment', 'categorie': 'Categorie', 'importanta': 'Importanță (1-10)'}),
        use_container_width=True, height=400
    )

# ============================================
# TAB 4: SECRETARI GENERALI
# ============================================

with tab4:
    st.header("🏛️ Secretarii Generali ai ONU")

    st.subheader("📅 Mandatele Secretarilor Generali (1946-2026)")

    fig_secretari = px.bar(
        df_secretari,
        x='durata',
        y='nume',
        color='continent',
        orientation='h',
        hover_data=['tara', 'mandat_start', 'mandat_end'],
        title='Durata Mandatelor Secretarilor Generali',
        labels={'durata': 'Durată (ani)', 'nume': 'Secretar General', 'continent': 'Continent'},
        height=500
    )
    fig_secretari.update_layout(yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig_secretari, use_container_width=True)

    st.subheader("📊 Timeline Visual al Mandatelor")

    fig_timeline_sg = go.Figure()

    culori_sg = {'Europa': '#3b82f6', 'Asia': '#ef4444', 'Africa': '#10b981', 'S.America': '#8b5cf6'}

    for idx, row in df_secretari.iterrows():
        fig_timeline_sg.add_trace(go.Bar(
            name=row['nume'],
            y=[row['nume']],
            x=[row['durata']],
            orientation='h',
            marker_color=culori_sg.get(row['continent'], '#gray'),
            hovertemplate=f"<b>{row['nume']}</b><br>Țară: {row['tara']}<br>Perioada: {row['mandat_start']}-{row['mandat_end']}<br>Durată: {row['durata']} ani<extra></extra>",
            showlegend=False
        ))

    fig_timeline_sg.update_layout(
        title='Timeline al Mandatelor Secretarilor Generali',
        xaxis_title='Ani în funcție',
        yaxis_title='',
        height=500,
        yaxis=dict(autorange="reversed")
    )
    st.plotly_chart(fig_timeline_sg, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🌍 Distribuția pe Continente")
        fig_sec_cont = px.pie(df_secretari, names='continent',
            title='Continentul de Origine al Secretarilor Generali',
            color='continent',
            color_discrete_map=culori_sg)
        st.plotly_chart(fig_sec_cont, use_container_width=True)

    with col2:
        st.subheader("⏱️ Durata Mandatelor")
        fig_durata = px.bar(df_secretari.sort_values('durata', ascending=False), 
            x='nume', y='durata', color='durata',
            color_continuous_scale='Teal',
            labels={'nume': 'Secretar General', 'durata': 'Ani în funcție'},
            height=400)
        fig_durata.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_durata, use_container_width=True)

    st.subheader("📋 Informații Complete")
    st.dataframe(
        df_secretari[['nume', 'tara', 'continent', 'mandat_start', 'mandat_end', 'durata']]
        .rename(columns={'nume': 'Nume', 'tara': 'Țară', 'continent': 'Continent',
            'mandat_start': 'Început Mandat', 'mandat_end': 'Sfârșit Mandat', 'durata': 'Durată (ani)'}),
        use_container_width=True
    )

# ============================================
# FOOTER
# ============================================

st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #64748b; padding: 1rem;">
        <p>🎓 Proiect realizat de elevele clasei a XI-a A: Gologan Iustina, Munteanu Mihaela și Mirică Cristina</p>
        <p>📊 Date actualizate până în 2025 | Sursa: Națiunile Unite</p>
        <p><em>"Pacea nu este doar absența războiului, ci prezența dreptății, a egalității și a armoniei."</em></p>
    </div>
""", unsafe_allow_html=True)