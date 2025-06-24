{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "40e71059-daf7-458b-8977-8ba138753431",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "45c19674-d776-49ec-8cba-a89e661203e2",
   "metadata": {},
   "outputs": [],
   "source": [
    "df= pd.read_csv(\"New_More_Halls_Data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2680ffa0-7ab7-435a-83d4-c2212f0a79d4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Type</th>\n",
       "      <th>Location</th>\n",
       "      <th>Ratings</th>\n",
       "      <th>Reviews</th>\n",
       "      <th>Menu_Price</th>\n",
       "      <th>Pax</th>\n",
       "      <th>Rooms</th>\n",
       "      <th>Amenities</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>AMBAR PALMS ARAVALI</td>\n",
       "      <td>Banquet Halls, Marriage Garden / Lawns</td>\n",
       "      <td>Sohna Road, Delhi NCR</td>\n",
       "      <td>5.0</td>\n",
       "      <td>15 reviews</td>\n",
       "      <td>₹1,800per plate</td>\n",
       "      <td>100-600</td>\n",
       "      <td>33.0</td>\n",
       "      <td>+5 more</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Cherish Ballrooms at Imperial Club of India</td>\n",
       "      <td>Banquet Halls, Marriage Garden / Lawns</td>\n",
       "      <td>Vasant Kunj, Delhi NCR</td>\n",
       "      <td>5.0</td>\n",
       "      <td>4 reviews</td>\n",
       "      <td>₹3,000per plate</td>\n",
       "      <td>80-650</td>\n",
       "      <td>20.0</td>\n",
       "      <td>+4 more</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Moksha Himalaya Spa Resort Himachal Pradesh</td>\n",
       "      <td>4 Star &amp; Above Wedding Hotels, Banquet Halls</td>\n",
       "      <td>Delhi NCR</td>\n",
       "      <td>4.9</td>\n",
       "      <td>6 reviews</td>\n",
       "      <td>₹4,500per plate</td>\n",
       "      <td>70-700</td>\n",
       "      <td>110.0</td>\n",
       "      <td>+5 more</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Crowne Plaza New Delhi Okhla, an IHG Hotel</td>\n",
       "      <td>4 Star &amp; Above Wedding Hotels, Banquet Halls</td>\n",
       "      <td>Okhla, Delhi NCR</td>\n",
       "      <td>5.0</td>\n",
       "      <td>10 reviews</td>\n",
       "      <td>₹3,199per plate</td>\n",
       "      <td>40-600</td>\n",
       "      <td>208.0</td>\n",
       "      <td>+5 more</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Radiance Tania Farms</td>\n",
       "      <td>Banquet Halls, Marriage Garden / Lawns</td>\n",
       "      <td>Chattarpur, Delhi NCR</td>\n",
       "      <td>4.8</td>\n",
       "      <td>19 reviews</td>\n",
       "      <td>₹2,300per plate</td>\n",
       "      <td>200-1500</td>\n",
       "      <td>7.0</td>\n",
       "      <td>+6 more</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Hotel Surya Grand</td>\n",
       "      <td>Banquet Halls, 3 Star Hotels with Banquets</td>\n",
       "      <td>Rajouri Garden, Delhi NCR</td>\n",
       "      <td>4.9</td>\n",
       "      <td>191 reviews</td>\n",
       "      <td>₹1,800per plate</td>\n",
       "      <td>50-600</td>\n",
       "      <td>22.0</td>\n",
       "      <td>+6 more</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>The Leela Palace New Delhi</td>\n",
       "      <td>4 Star &amp; Above Wedding Hotels, Banquet Halls</td>\n",
       "      <td>New Delhi, Delhi NCR</td>\n",
       "      <td>4.7</td>\n",
       "      <td>14 reviews</td>\n",
       "      <td>₹6,000per plate</td>\n",
       "      <td>25-300</td>\n",
       "      <td>254.0</td>\n",
       "      <td>+4 more</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Park Boulevard Hotel, New Delhi</td>\n",
       "      <td>4 Star &amp; Above Wedding Hotels, Banquet Halls</td>\n",
       "      <td>Chattarpur, Delhi NCR</td>\n",
       "      <td>5.0</td>\n",
       "      <td>52 reviews</td>\n",
       "      <td>₹4,200per plate</td>\n",
       "      <td>300-1000</td>\n",
       "      <td>45.0</td>\n",
       "      <td>+7 more</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Crowne Plaza New Delhi Mayur Vihar Noida, an I...</td>\n",
       "      <td>4 Star &amp; Above Wedding Hotels, Banquet Halls</td>\n",
       "      <td>Mayur Vihar, Delhi NCR</td>\n",
       "      <td>4.6</td>\n",
       "      <td>19 reviews</td>\n",
       "      <td>₹2,500per plate</td>\n",
       "      <td>30-700</td>\n",
       "      <td>160.0</td>\n",
       "      <td>+4 more</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Tivoli Bijwasan</td>\n",
       "      <td>Banquet Halls, Marriage Garden / Lawns</td>\n",
       "      <td>Delhi NCR</td>\n",
       "      <td>NaN</td>\n",
       "      <td>25 reviews</td>\n",
       "      <td>₹3,000per plate</td>\n",
       "      <td>150-1400</td>\n",
       "      <td>16.0</td>\n",
       "      <td>+4 more</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                Name  \\\n",
       "0                                AMBAR PALMS ARAVALI   \n",
       "1        Cherish Ballrooms at Imperial Club of India   \n",
       "2        Moksha Himalaya Spa Resort Himachal Pradesh   \n",
       "3         Crowne Plaza New Delhi Okhla, an IHG Hotel   \n",
       "4                               Radiance Tania Farms   \n",
       "5                                  Hotel Surya Grand   \n",
       "6                         The Leela Palace New Delhi   \n",
       "7                    Park Boulevard Hotel, New Delhi   \n",
       "8  Crowne Plaza New Delhi Mayur Vihar Noida, an I...   \n",
       "9                                    Tivoli Bijwasan   \n",
       "\n",
       "                                           Type                    Location  \\\n",
       "0        Banquet Halls, Marriage Garden / Lawns      Sohna Road, Delhi NCR    \n",
       "1        Banquet Halls, Marriage Garden / Lawns     Vasant Kunj, Delhi NCR    \n",
       "2  4 Star & Above Wedding Hotels, Banquet Halls                  Delhi NCR    \n",
       "3  4 Star & Above Wedding Hotels, Banquet Halls           Okhla, Delhi NCR    \n",
       "4        Banquet Halls, Marriage Garden / Lawns      Chattarpur, Delhi NCR    \n",
       "5    Banquet Halls, 3 Star Hotels with Banquets  Rajouri Garden, Delhi NCR    \n",
       "6  4 Star & Above Wedding Hotels, Banquet Halls       New Delhi, Delhi NCR    \n",
       "7  4 Star & Above Wedding Hotels, Banquet Halls      Chattarpur, Delhi NCR    \n",
       "8  4 Star & Above Wedding Hotels, Banquet Halls     Mayur Vihar, Delhi NCR    \n",
       "9        Banquet Halls, Marriage Garden / Lawns                  Delhi NCR    \n",
       "\n",
       "   Ratings      Reviews       Menu_Price       Pax  Rooms Amenities  \n",
       "0      5.0   15 reviews  ₹1,800per plate   100-600   33.0   +5 more  \n",
       "1      5.0    4 reviews  ₹3,000per plate    80-650   20.0   +4 more  \n",
       "2      4.9    6 reviews  ₹4,500per plate    70-700  110.0   +5 more  \n",
       "3      5.0   10 reviews  ₹3,199per plate    40-600  208.0   +5 more  \n",
       "4      4.8   19 reviews  ₹2,300per plate  200-1500    7.0   +6 more  \n",
       "5      4.9  191 reviews  ₹1,800per plate    50-600   22.0   +6 more  \n",
       "6      4.7   14 reviews  ₹6,000per plate    25-300  254.0   +4 more  \n",
       "7      5.0   52 reviews  ₹4,200per plate  300-1000   45.0   +7 more  \n",
       "8      4.6   19 reviews  ₹2,500per plate    30-700  160.0   +4 more  \n",
       "9      NaN   25 reviews  ₹3,000per plate  150-1400   16.0   +4 more  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "47d488f5-9042-4e9a-99fe-be4ed8cd9054",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 3000 entries, 0 to 2999\n",
      "Data columns (total 9 columns):\n",
      " #   Column      Non-Null Count  Dtype  \n",
      "---  ------      --------------  -----  \n",
      " 0   Name        3000 non-null   object \n",
      " 1   Type        3000 non-null   object \n",
      " 2   Location    3000 non-null   object \n",
      " 3   Ratings     1176 non-null   float64\n",
      " 4   Reviews     1516 non-null   object \n",
      " 5   Menu_Price  3000 non-null   object \n",
      " 6   Pax         2864 non-null   object \n",
      " 7   Rooms       1445 non-null   float64\n",
      " 8   Amenities   2999 non-null   object \n",
      "dtypes: float64(2), object(7)\n",
      "memory usage: 211.1+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ab471685-04e3-4e36-9eec-ab46fcedff77",
   "metadata": {},
   "outputs": [],
   "source": [
    "# extracting only review count from the review column\n",
    "\n",
    "df[\"Reviews\"]= df[\"Reviews\"].replace(\"[\\D]\",\"\",regex=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a5cbc92a-a581-4797-bf55-83d16ddd95c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# extracting only price from menu price column\n",
    "\n",
    "df[\"Menu_Price\"]= df[\"Menu_Price\"].replace(\"[\\D]\",\"\",regex=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "3b309946-8ecd-4e50-8200-4034a6524a7b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Extracting min and max guest capacities from pax column\n",
    "\n",
    "df[[\"Pax_Min\", \"Pax_Max\"]]= df[\"Pax\"].str.extract(r\"(\\d+)-(\\d+)\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "429098b9-0d94-47d3-8c53-b66c152cbf8c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# converting name, type, and location column to lower case\n",
    "\n",
    "df[\"Name\"]= df[\"Name\"].str.lower()\n",
    "df[\"Type\"]= df[\"Type\"].str.lower()\n",
    "df[\"Location\"]= df[\"Location\"].str.lower()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "3b9cbc00-071d-4b94-b963-76cf22c4f101",
   "metadata": {},
   "outputs": [],
   "source": [
    "# extracting destination/ city name from the location column \n",
    "\n",
    "df[\"Destination\"]= df[\"Location\"].str.strip().str.split().str[-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a2d0d58a-8b05-4fc4-ba94-7ad252754db3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# extracting only digits from amenities column\n",
    "df[\"Amenities_+more\"]= df[\"Amenities\"].replace(\"[\\D]\",\"\",regex=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "daa2f442-b788-4c68-9289-657cf5fe78c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dropping Pax column because its not more needed \n",
    "\n",
    "df.drop(df[[\"Pax\"]], axis=1, inplace=True)\n",
    "\n",
    "# # droppping location cause we extract city names from the location in destination column\n",
    "\n",
    "df.drop(df[[\"Location\"]], axis=1, inplace=True)\n",
    "\n",
    "# # dropping amenities column because we extracted number of amenities from it\n",
    "\n",
    "df.drop(df[[\"Amenities\"]], axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "3b1105bd-89f9-4443-95f3-04c0aa5ae83c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Name                  0\n",
       "Type                  0\n",
       "Ratings            1824\n",
       "Reviews            1484\n",
       "Menu_Price            0\n",
       "Rooms              1555\n",
       "Pax_Min             136\n",
       "Pax_Max             136\n",
       "Destination           0\n",
       "Amenities_+more       1\n",
       "dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# checking for missing values\n",
    "df.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "c60e112f-68e2-4294-822d-98a364852ccb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# step 1: calculating missing  value percentage\n",
    "\n",
    "missing_per= df.isna().mean()*100\n",
    "\n",
    "# step 2: converting to a dataframe \n",
    "\n",
    "missing_df= missing_per.reset_index()\n",
    "\n",
    "missing_df.columns= [\"Column\", \"Missing_Per\"]\n",
    "\n",
    "\n",
    "# step 3: this step is optional but if you want to sort values by highest you can\n",
    "\n",
    "missing_df= missing_df.sort_values(by=\"Missing_Per\", ascending= False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "968e768f-e645-476e-8870-0173cf84867d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Column</th>\n",
       "      <th>Missing_Per</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Ratings</td>\n",
       "      <td>60.800000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Rooms</td>\n",
       "      <td>51.833333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Reviews</td>\n",
       "      <td>49.466667</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Pax_Min</td>\n",
       "      <td>4.533333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Pax_Max</td>\n",
       "      <td>4.533333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Amenities_+more</td>\n",
       "      <td>0.033333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Name</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Type</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Menu_Price</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Destination</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Column  Missing_Per\n",
       "2          Ratings    60.800000\n",
       "5            Rooms    51.833333\n",
       "3          Reviews    49.466667\n",
       "6          Pax_Min     4.533333\n",
       "7          Pax_Max     4.533333\n",
       "9  Amenities_+more     0.033333\n",
       "0             Name     0.000000\n",
       "1             Type     0.000000\n",
       "4       Menu_Price     0.000000\n",
       "8      Destination     0.000000"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "missing_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "71b978be-61a7-44d5-867d-3d3a3e530cfa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 3000 entries, 0 to 2999\n",
      "Data columns (total 10 columns):\n",
      " #   Column           Non-Null Count  Dtype  \n",
      "---  ------           --------------  -----  \n",
      " 0   Name             3000 non-null   object \n",
      " 1   Type             3000 non-null   object \n",
      " 2   Ratings          1176 non-null   float64\n",
      " 3   Reviews          1516 non-null   object \n",
      " 4   Menu_Price       3000 non-null   object \n",
      " 5   Rooms            1445 non-null   float64\n",
      " 6   Pax_Min          2864 non-null   object \n",
      " 7   Pax_Max          2864 non-null   object \n",
      " 8   Destination      3000 non-null   object \n",
      " 9   Amenities_+more  2999 non-null   object \n",
      "dtypes: float64(2), object(8)\n",
      "memory usage: 234.5+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "8dc58298-68bc-4a26-808a-584ad72d9919",
   "metadata": {},
   "outputs": [],
   "source": [
    "# converting pax min, pax maqx column to numeric \n",
    "df[\"Pax_Max\"]= pd.to_numeric(df[\"Pax_Max\"])\n",
    "df[\"Pax_Min\"]= pd.to_numeric(df[\"Pax_Min\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "16ba8386-f60f-4cb8-9800-b2573ecc29f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# filling out missing valuees for each column \n",
    "\n",
    "df[\"Ratings\"].fillna(df[\"Ratings\"].median(), inplace=True)\n",
    "\n",
    "df[\"Rooms\"].fillna(df[\"Rooms\"].median(), inplace=True)\n",
    "\n",
    "df[\"Reviews\"].fillna(0, inplace=True)\n",
    "\n",
    "df[\"Pax_Min\"].fillna(df[\"Pax_Min\"].median(), inplace=True)\n",
    "\n",
    "df[\"Pax_Max\"].fillna(df[\"Pax_Max\"].median(), inplace=True)\n",
    "\n",
    "df.dropna(subset=[\"Amenities_+more\"], inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "892ed902-ba71-4a62-a00b-83f57a5cce44",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Name               0\n",
       "Type               0\n",
       "Ratings            0\n",
       "Reviews            0\n",
       "Menu_Price         0\n",
       "Rooms              0\n",
       "Pax_Min            0\n",
       "Pax_Max            0\n",
       "Destination        0\n",
       "Amenities_+more    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "1901c780-6c2f-4b46-9bf7-6d877bbbaf85",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['1800', '3000', '4500', '3199', '2300', '6000', '4200', '2500',\n",
       "       '1200', '1850', '1000', '4000', '5500', '3299', '2800', '1000000',\n",
       "       '', '850', '415', '200000', '750', '80000', '250000', '650',\n",
       "       '42000', '50000', '777', '800', '699', '550', '400', '600',\n",
       "       '500000', '1300', '1500', '150000', '1650', '999', '899', '499',\n",
       "       '2899', '700', '799', '900', '2375', '1399', '3400', '1600',\n",
       "       '1100', '1400', '3000000', '1700', '3500', '1900', '5000', '2400',\n",
       "       '7000', '3800', '2100', '1250', '2000', '1199', '1550', '2200',\n",
       "       '2999', '350', '560', '300', '40000', '500', '275', '100000',\n",
       "       '1450', '800000', '2950', '2700', '1350', '2449', '200', '250',\n",
       "       '450', '125000', '1050', '525', '120000', '680', '110000',\n",
       "       '600000', '4300', '1699', '950', '175', '420', '90000', '60000',\n",
       "       '150', '1150', '460', '1750', '1099', '425', '1375', '25000',\n",
       "       '130000', '1299', '70000', '2650', '3700', '1210', '575', '2450',\n",
       "       '951', '2699', '69502', '28000', '690', '30000', '1599', '1801',\n",
       "       '3100', '180000', '55000', '700000', '80', '1444', '280000', '529',\n",
       "       '65000', '900000', '3200', '459', '849', '92000', '90', '140000',\n",
       "       '220', '890', '45000', '35000', '369000', '175000', '375', '435',\n",
       "       '290', '240000', '11000', '95000', '675', '104000', '3450',\n",
       "       '165000', '230000', '51000', '475', '240', '145000', '349',\n",
       "       '20000', '180', '270', '649', '170000', '695', '395', '549',\n",
       "       '2900', '3300', '27000', '6500', '599', '300000', '2600', '225',\n",
       "       '325', '85000', '15000', '350000', '75000', '446', '315', '650000',\n",
       "       '595', '2000000', '2250', '2750', '5999', '280', '590', '815',\n",
       "       '2050', '48000', '550000', '990', '225000', '1950', '430',\n",
       "       '101000', '330000', '261000', '100', '210000'], dtype=object)"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"Menu_Price\"].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "8c488db0-7f18-4bef-8eb7-ca1fa8eb3f21",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Menu price is cotaining \"\" this value which is not appropriate while changing the data type of price column, so replacing it by nan value\n",
    "\n",
    "df[\"Menu_Price\"]= df[\"Menu_Price\"].replace(\"\", np.nan)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "e8254197-2d40-4067-ab89-4883eff07de2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "459"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"Menu_Price\"].isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "7134d97d-b3c0-47c5-8f11-3d10dc11e256",
   "metadata": {},
   "outputs": [],
   "source": [
    "# dropping missing values for menu price cause we cannot manually add them\n",
    "\n",
    "df.dropna(subset=\"Menu_Price\", inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "b6f1fcbf-0e02-416c-aab4-e8589360b2d6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Index: 2540 entries, 0 to 2999\n",
      "Data columns (total 10 columns):\n",
      " #   Column           Non-Null Count  Dtype  \n",
      "---  ------           --------------  -----  \n",
      " 0   Name             2540 non-null   object \n",
      " 1   Type             2540 non-null   object \n",
      " 2   Ratings          2540 non-null   float64\n",
      " 3   Reviews          2540 non-null   object \n",
      " 4   Menu_Price       2540 non-null   object \n",
      " 5   Rooms            2540 non-null   float64\n",
      " 6   Pax_Min          2540 non-null   float64\n",
      " 7   Pax_Max          2540 non-null   float64\n",
      " 8   Destination      2540 non-null   object \n",
      " 9   Amenities_+more  2540 non-null   object \n",
      "dtypes: float64(4), object(6)\n",
      "memory usage: 218.3+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "b0285c0a-0ddc-47d2-8a50-0beea9eefe58",
   "metadata": {},
   "outputs": [],
   "source": [
    "# now chaging data type for each feature according to its need\n",
    "\n",
    "df[\"Reviews\"]=df[\"Reviews\"].astype(int)\n",
    "\n",
    "df[\"Menu_Price\"]= df[\"Menu_Price\"].astype(float)\n",
    "\n",
    "df[\"Rooms\"]= df[\"Rooms\"].astype(int)\n",
    "\n",
    "df[\"Pax_Min\"]= df[\"Pax_Min\"].astype(int)\n",
    "\n",
    "df[\"Pax_Max\"]= df[\"Pax_Max\"].astype(int)\n",
    "\n",
    "df[\"Amenities_+more\"]= df[\"Amenities_+more\"].astype(int)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "d13b8b4f-db77-4bd8-ac13-398ebc99789d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Index: 2540 entries, 0 to 2999\n",
      "Data columns (total 10 columns):\n",
      " #   Column           Non-Null Count  Dtype  \n",
      "---  ------           --------------  -----  \n",
      " 0   Name             2540 non-null   object \n",
      " 1   Type             2540 non-null   object \n",
      " 2   Ratings          2540 non-null   float64\n",
      " 3   Reviews          2540 non-null   int32  \n",
      " 4   Menu_Price       2540 non-null   float64\n",
      " 5   Rooms            2540 non-null   int32  \n",
      " 6   Pax_Min          2540 non-null   int32  \n",
      " 7   Pax_Max          2540 non-null   int32  \n",
      " 8   Destination      2540 non-null   object \n",
      " 9   Amenities_+more  2540 non-null   int32  \n",
      "dtypes: float64(2), int32(5), object(3)\n",
      "memory usage: 168.7+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "743eaf79-1961-4568-873b-9ec681a8a361",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "57"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# checking for duplicates\n",
    "\n",
    "df.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "66b7bc51-5bc6-4f29-80a2-efc203f9c30e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# droppping duplicates \n",
    "\n",
    "df.drop_duplicates(inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "50a02e5d-edc3-4839-88a6-8c3aaa7db9fc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# again checking for duplicates\n",
    "\n",
    "df.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "c6075fd7-348a-41af-a77a-583b057f11b0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2483, 10)"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "b7212c09-3b46-4a75-8dbb-ce5e60f05940",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Ratings</th>\n",
       "      <th>Reviews</th>\n",
       "      <th>Menu_Price</th>\n",
       "      <th>Rooms</th>\n",
       "      <th>Pax_Min</th>\n",
       "      <th>Pax_Max</th>\n",
       "      <th>Amenities_+more</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>2483.000000</td>\n",
       "      <td>2483.000000</td>\n",
       "      <td>2.483000e+03</td>\n",
       "      <td>2483.000000</td>\n",
       "      <td>2483.000000</td>\n",
       "      <td>2483.000000</td>\n",
       "      <td>2483.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>4.964035</td>\n",
       "      <td>2.658880</td>\n",
       "      <td>1.348506e+04</td>\n",
       "      <td>31.621023</td>\n",
       "      <td>328.772050</td>\n",
       "      <td>767.468385</td>\n",
       "      <td>2.715667</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.112295</td>\n",
       "      <td>7.615934</td>\n",
       "      <td>9.317938e+04</td>\n",
       "      <td>44.163486</td>\n",
       "      <td>361.074579</td>\n",
       "      <td>851.346483</td>\n",
       "      <td>0.871073</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>4.500000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>8.000000e+01</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>5.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>4.500000e+02</td>\n",
       "      <td>21.000000</td>\n",
       "      <td>100.000000</td>\n",
       "      <td>300.000000</td>\n",
       "      <td>2.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>5.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>7.000000e+02</td>\n",
       "      <td>21.000000</td>\n",
       "      <td>200.000000</td>\n",
       "      <td>500.000000</td>\n",
       "      <td>3.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>5.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.274500e+03</td>\n",
       "      <td>22.500000</td>\n",
       "      <td>400.000000</td>\n",
       "      <td>1000.000000</td>\n",
       "      <td>3.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>5.000000</td>\n",
       "      <td>191.000000</td>\n",
       "      <td>3.000000e+06</td>\n",
       "      <td>670.000000</td>\n",
       "      <td>2500.000000</td>\n",
       "      <td>20000.000000</td>\n",
       "      <td>8.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Ratings      Reviews    Menu_Price        Rooms      Pax_Min  \\\n",
       "count  2483.000000  2483.000000  2.483000e+03  2483.000000  2483.000000   \n",
       "mean      4.964035     2.658880  1.348506e+04    31.621023   328.772050   \n",
       "std       0.112295     7.615934  9.317938e+04    44.163486   361.074579   \n",
       "min       4.500000     0.000000  8.000000e+01     0.000000     0.000000   \n",
       "25%       5.000000     0.000000  4.500000e+02    21.000000   100.000000   \n",
       "50%       5.000000     1.000000  7.000000e+02    21.000000   200.000000   \n",
       "75%       5.000000     2.000000  1.274500e+03    22.500000   400.000000   \n",
       "max       5.000000   191.000000  3.000000e+06   670.000000  2500.000000   \n",
       "\n",
       "            Pax_Max  Amenities_+more  \n",
       "count   2483.000000      2483.000000  \n",
       "mean     767.468385         2.715667  \n",
       "std      851.346483         0.871073  \n",
       "min        0.000000         1.000000  \n",
       "25%      300.000000         2.000000  \n",
       "50%      500.000000         3.000000  \n",
       "75%     1000.000000         3.000000  \n",
       "max    20000.000000         8.000000  "
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "31ca7ed5-f20b-4d21-bfb8-aad63da9c27c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# created finalized dataset for visualization\n",
    "# df.to_csv(\"Fully_Cleaned_Halls_Data.csv\", index= False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "93bbeddf-9b16-4db1-83f8-983b798206ba",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Type</th>\n",
       "      <th>Ratings</th>\n",
       "      <th>Reviews</th>\n",
       "      <th>Menu_Price</th>\n",
       "      <th>Rooms</th>\n",
       "      <th>Pax_Min</th>\n",
       "      <th>Pax_Max</th>\n",
       "      <th>Destination</th>\n",
       "      <th>Amenities_+more</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ambar palms aravali</td>\n",
       "      <td>banquet halls, marriage garden / lawns</td>\n",
       "      <td>5.0</td>\n",
       "      <td>15</td>\n",
       "      <td>1800.0</td>\n",
       "      <td>33</td>\n",
       "      <td>100</td>\n",
       "      <td>600</td>\n",
       "      <td>ncr</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>cherish ballrooms at imperial club of india</td>\n",
       "      <td>banquet halls, marriage garden / lawns</td>\n",
       "      <td>5.0</td>\n",
       "      <td>4</td>\n",
       "      <td>3000.0</td>\n",
       "      <td>20</td>\n",
       "      <td>80</td>\n",
       "      <td>650</td>\n",
       "      <td>ncr</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>moksha himalaya spa resort himachal pradesh</td>\n",
       "      <td>4 star &amp; above wedding hotels, banquet halls</td>\n",
       "      <td>4.9</td>\n",
       "      <td>6</td>\n",
       "      <td>4500.0</td>\n",
       "      <td>110</td>\n",
       "      <td>70</td>\n",
       "      <td>700</td>\n",
       "      <td>ncr</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>crowne plaza new delhi okhla, an ihg hotel</td>\n",
       "      <td>4 star &amp; above wedding hotels, banquet halls</td>\n",
       "      <td>5.0</td>\n",
       "      <td>10</td>\n",
       "      <td>3199.0</td>\n",
       "      <td>208</td>\n",
       "      <td>40</td>\n",
       "      <td>600</td>\n",
       "      <td>ncr</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>radiance tania farms</td>\n",
       "      <td>banquet halls, marriage garden / lawns</td>\n",
       "      <td>4.8</td>\n",
       "      <td>19</td>\n",
       "      <td>2300.0</td>\n",
       "      <td>7</td>\n",
       "      <td>200</td>\n",
       "      <td>1500</td>\n",
       "      <td>ncr</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2995</th>\n",
       "      <td>hotel grand capitol</td>\n",
       "      <td>banquet halls, destination wedding venues</td>\n",
       "      <td>5.0</td>\n",
       "      <td>0</td>\n",
       "      <td>800.0</td>\n",
       "      <td>47</td>\n",
       "      <td>30</td>\n",
       "      <td>50</td>\n",
       "      <td>jaipur</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2996</th>\n",
       "      <td>hotel regal by rhytham</td>\n",
       "      <td>banquet halls, marriage garden / lawns</td>\n",
       "      <td>4.8</td>\n",
       "      <td>2</td>\n",
       "      <td>700.0</td>\n",
       "      <td>28</td>\n",
       "      <td>150</td>\n",
       "      <td>300</td>\n",
       "      <td>jaipur</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2997</th>\n",
       "      <td>skylit</td>\n",
       "      <td>banquet halls</td>\n",
       "      <td>5.0</td>\n",
       "      <td>0</td>\n",
       "      <td>500.0</td>\n",
       "      <td>21</td>\n",
       "      <td>105</td>\n",
       "      <td>150</td>\n",
       "      <td>jaipur</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2998</th>\n",
       "      <td>shahpura house</td>\n",
       "      <td>3 star hotels with banquets, small function / ...</td>\n",
       "      <td>5.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1500.0</td>\n",
       "      <td>62</td>\n",
       "      <td>80</td>\n",
       "      <td>120</td>\n",
       "      <td>jaipur</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2999</th>\n",
       "      <td>gokul vatika</td>\n",
       "      <td>marriage garden / lawns</td>\n",
       "      <td>5.0</td>\n",
       "      <td>0</td>\n",
       "      <td>550.0</td>\n",
       "      <td>21</td>\n",
       "      <td>250</td>\n",
       "      <td>400</td>\n",
       "      <td>jaipur</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2483 rows × 10 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                             Name  \\\n",
       "0                             ambar palms aravali   \n",
       "1     cherish ballrooms at imperial club of india   \n",
       "2     moksha himalaya spa resort himachal pradesh   \n",
       "3      crowne plaza new delhi okhla, an ihg hotel   \n",
       "4                            radiance tania farms   \n",
       "...                                           ...   \n",
       "2995                          hotel grand capitol   \n",
       "2996                       hotel regal by rhytham   \n",
       "2997                                       skylit   \n",
       "2998                               shahpura house   \n",
       "2999                                 gokul vatika   \n",
       "\n",
       "                                                   Type  Ratings  Reviews  \\\n",
       "0                banquet halls, marriage garden / lawns      5.0       15   \n",
       "1                banquet halls, marriage garden / lawns      5.0        4   \n",
       "2          4 star & above wedding hotels, banquet halls      4.9        6   \n",
       "3          4 star & above wedding hotels, banquet halls      5.0       10   \n",
       "4                banquet halls, marriage garden / lawns      4.8       19   \n",
       "...                                                 ...      ...      ...   \n",
       "2995          banquet halls, destination wedding venues      5.0        0   \n",
       "2996             banquet halls, marriage garden / lawns      4.8        2   \n",
       "2997                                      banquet halls      5.0        0   \n",
       "2998  3 star hotels with banquets, small function / ...      5.0        1   \n",
       "2999                            marriage garden / lawns      5.0        0   \n",
       "\n",
       "      Menu_Price  Rooms  Pax_Min  Pax_Max Destination  Amenities_+more  \n",
       "0         1800.0     33      100      600         ncr                5  \n",
       "1         3000.0     20       80      650         ncr                4  \n",
       "2         4500.0    110       70      700         ncr                5  \n",
       "3         3199.0    208       40      600         ncr                5  \n",
       "4         2300.0      7      200     1500         ncr                6  \n",
       "...          ...    ...      ...      ...         ...              ...  \n",
       "2995       800.0     47       30       50      jaipur                3  \n",
       "2996       700.0     28      150      300      jaipur                4  \n",
       "2997       500.0     21      105      150      jaipur                2  \n",
       "2998      1500.0     62       80      120      jaipur                3  \n",
       "2999       550.0     21      250      400      jaipur                2  \n",
       "\n",
       "[2483 rows x 10 columns]"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "b52f7a22-cc22-4121-b1d2-50eac8c977c7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['banquet halls, marriage garden / lawns',\n",
       "       '4 star & above wedding hotels, banquet halls',\n",
       "       'banquet halls, 3 star hotels with banquets',\n",
       "       '4 star & above wedding hotels, marriage garden / lawns',\n",
       "       'marriage garden / lawns, 3 star hotels with banquets',\n",
       "       'marriage garden / lawns', 'banquet halls',\n",
       "       'banquet halls, kalyana mandapams',\n",
       "       'banquet halls, convention / function halls',\n",
       "       'marriage garden / lawns, venues with rooms',\n",
       "       'banquet halls, party restaurants / lounge bars',\n",
       "       'venues with rooms, wedding farmhouses',\n",
       "       'banquet halls, small function / party halls',\n",
       "       'marriage garden / lawns, party restaurants / lounge bars',\n",
       "       'marriage garden / lawns, wedding farmhouses',\n",
       "       'banquet halls, venues with rooms',\n",
       "       '3 star hotels with banquets, destination wedding venues',\n",
       "       'marriage garden / lawns, convention / function halls',\n",
       "       '4 star & above wedding hotels, 3 star hotels with banquets',\n",
       "       'marriage garden / lawns, wedding resorts',\n",
       "       'marriage garden / lawns, destination wedding venues',\n",
       "       'banquet halls, wedding resorts', 'wedding resorts',\n",
       "       'small function / party halls', '3 star hotels with banquets',\n",
       "       'wedding resorts, venues with rooms',\n",
       "       'banquet halls, destination wedding venues',\n",
       "       'party restaurants / lounge bars, small function / party halls',\n",
       "       'wedding farmhouses',\n",
       "       '4 star & above wedding hotels, destination wedding venues',\n",
       "       '4 star & above wedding hotels, 5 star luxury wedding hotels',\n",
       "       'marriage garden / lawns, small function / party halls',\n",
       "       '3 star hotels with banquets, venues with rooms',\n",
       "       'banquet halls, forts / palaces for wedding',\n",
       "       'small function / party halls, small function / party halls',\n",
       "       '3 star hotels with banquets, small function / party halls',\n",
       "       'marriage garden / lawns, kalyana mandapams',\n",
       "       'party restaurants / lounge bars',\n",
       "       'small function / party halls, convention / function halls',\n",
       "       '3 star hotels with banquets, wedding resorts',\n",
       "       'wedding resorts, destination wedding venues',\n",
       "       '4 star & above wedding hotels, venues with rooms',\n",
       "       'party restaurants / lounge bars, banquet halls',\n",
       "       '4 star & above wedding hotels, wedding resorts',\n",
       "       'small function / party halls, venues with rooms',\n",
       "       '4 star & above wedding hotels, small function / party halls',\n",
       "       'small function / party halls, 3 star hotels with banquets',\n",
       "       '3 star hotels with banquets, party restaurants / lounge bars',\n",
       "       'banquet halls, 4 star & above wedding hotels',\n",
       "       'party restaurants / lounge bars, marriage garden / lawns',\n",
       "       'marriage garden / lawns, banquet halls',\n",
       "       '3 star hotels with banquets, convention / function halls'],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Type.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "a1623dc0-48ce-47b3-ba16-f9fc5c9b63ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Index: 2483 entries, 0 to 2999\n",
      "Data columns (total 10 columns):\n",
      " #   Column           Non-Null Count  Dtype  \n",
      "---  ------           --------------  -----  \n",
      " 0   Name             2483 non-null   object \n",
      " 1   Type             2483 non-null   object \n",
      " 2   Ratings          2483 non-null   float64\n",
      " 3   Reviews          2483 non-null   int32  \n",
      " 4   Menu_Price       2483 non-null   float64\n",
      " 5   Rooms            2483 non-null   int32  \n",
      " 6   Pax_Min          2483 non-null   int32  \n",
      " 7   Pax_Max          2483 non-null   int32  \n",
      " 8   Destination      2483 non-null   object \n",
      " 9   Amenities_+more  2483 non-null   int32  \n",
      "dtypes: float64(2), int32(5), object(3)\n",
      "memory usage: 164.9+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f7e5965-c84f-4f2a-935c-44ce41ed4327",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
