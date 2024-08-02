import visualization 
import dashboard 
import filehandling 
import exceptions 
import data_cleaning

def main():
    df = filehandling.read_csv('country_wise_latest.csv')
    try:
        df = data_cleaning.clean_data(df)
        filehandling.write_csv('clean_covid_data.csv', df)
    except exceptions.DataCleaningError as e:
        print(f"Data cleaning error: {e.message}")
        return

    visualization.plot_total_cases(df)
    visualization.plot_top_countries(df)
    visualization.plot_daily_cases(df)

    dashboard.create_dashboard(df)  

main()