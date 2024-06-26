## FINAL PROJECT 
1. Buat file *docker-compose.yaml* untuk membentuk image airflow init, airflow webserver, airflow scheduler, dan postgresql
2. Buat file *mongodb_loader.py* untuk mengelola koneksi ke database mongodb dengan tujuan untuk dapat mengakses database di dalamnya
3. Buat file *finnhub_loader.py* untuk menghubungkan ke finnhub dengan tujuan untuk mengakses news dari finnhub
4. Buat file *postgres_loader.py* untuk menghubungkan ke postgres
5. Buat file *finnhub_mongodb_loader.py* untuk membuat koneksi antara finnhub ke mongodb untuk load news dari finnhub ke mongodb
6. Buat file *sentiment_analysis.py* untuk melakukan analisis sentimen terhadap news
7. Buat file *sentiment_analysis_loader.py* untuk menerapkan analisis sentimen terhadap setiap dokumen berita di finnhub, kemudian menyimpan hasilnya dalam bentuk dataframe dengan `sentiment_output = pd.DataFrame(output)`, kemudian load hasilnya ke postgres
