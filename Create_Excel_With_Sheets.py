def saving_reports(tbl_id_cross,tbl_id_combs,df_matches_idcross_idcombs,df_unmatch_idcrosses,df_unmatch_idccombs):
    # Crie um objeto ExcelWriter
    with pd.ExcelWriter('results.xlsx') as writer:
        df_matches_idcross_idcombs.to_excel(writer, sheet_name='Matches',index=False)
        tbl_id_cross.to_excel(writer, sheet_name='ID_CROSS',index=False)
        tbl_id_combs.to_excel(writer, sheet_name='ID_COMBS',index=False)
        df_unmatch_idcrosses.to_excel(writer, sheet_name='Unmatches ID_CROSS',index=False)
        df_unmatch_idccombs.to_excel(writer, sheet_name='Unmatches ID_COMBS',index=False)


# WRITER == EXCEL 
