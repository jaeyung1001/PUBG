def check_ammo(gun_name):
    diction = {
        # 7탄
        "Item_Weapon_AK47_C": "Item_Ammo_762mm_C",
        "Item_Weapon_BerylM762_C": "Item_Ammo_762mm_C",
        "Item_Weapon_FNFal_C": "Item_Ammo_762mm_C",
        "Item_Weapon_Groza_C": "Item_Ammo_762mm_C",
        "Item_Weapon_Kar98k_C": "Item_Ammo_762mm_C",
        "Item_Weapon_SKS_C": "Item_Ammo_762mm_C",
        "Item_Weapon_DP28_C": "Item_Ammo_762mm_C",
        "Item_Weapon_M24_C": "Item_Ammo_762mm_C",
        "Item_Weapon_Mk14_C": "Item_Ammo_762mm_C",
        "Item_Weapon_Mk47Mutant_C": "Item_Ammo_762mm_C",
        "Item_Weapon_NagantM1895_C": "Item_Ammo_762mm_C",
          
        # 5탄
        "Item_Weapon_AUG_C": "Item_Ammo_556mm_C",
        "Item_Weapon_QBU88_C": "Item_Ammo_556mm_C",
        "Item_Weapon_QBZ95_C": "Item_Ammo_556mm_C",
        "Item_Weapon_G36C_C": "Item_Ammo_556mm_C",
        "Item_Weapon_HK416_C": "Item_Ammo_556mm_C",
        "Item_Weapon_M16A4_C": "Item_Ammo_556mm_C",
        "Item_Weapon_M249_C": "Item_Ammo_556mm_C",
        "Item_Weapon_Mini14_C": "Item_Ammo_556mm_C",
        "Item_Weapon_SCAR-L_C": "Item_Ammo_556mm_C",
          
        #샷건
        "Item_Weapon_Berreta686_C": "Item_Ammo_12Guage_C",
        "Item_Weapon_Saiga12_C": "Item_Ammo_12Guage_C",
        "Item_Weapon_Sawnoff_C": "Item_Ammo_12Guage_C",
        "Item_Weapon_Winchester_C": "Item_Ammo_12Guage_C",
        "Item_Weapon_DP12_C": "Item_Ammo_12Guage_C",
          
        # 플레어건
        "Item_Weapon_FlareGun_C": "Item_Ammo_Flare_C",
          
        # 45탄
        "Item_Weapon_Thompson_C": "Item_Ammo_45ACP_C",
        "Item_Weapon_UMP_C": "Item_Ammo_45ACP_C",
        "Item_Weapon_M1911_C": "Item_Ammo_45ACP_C",
        "Item_Weapon_Rhino_C": "Item_Ammo_45ACP_C",
        "Item_Weapon_Win1894_C": "Item_Ammo_45ACP_C",
        "Item_Weapon_DesertEagle_C": "Item_Ammo_45ACP_C",
          
        # 화살
        "Item_Weapon_Crossbow_C": "Item_Ammo_Bolt_C",
          
        # AWM 탄
        "Item_Weapon_AWM_C": "Item_Ammo_300Magnum_C",
          
        # 9탄
        "Item_Weapon_BizonPP19_C": "Item_Ammo_9mm_C",
        "Item_Weapon_G18_C": "Item_Ammo_9mm_C",
        "Item_Weapon_M9_C": "Item_Ammo_9mm_C",
        "Item_Weapon_MP5K_C": "Item_Ammo_9mm_C",
        "Item_Weapon_UZI_C": "Item_Ammo_9mm_C",
        "Item_Weapon_Vector_C": "Item_Ammo_9mm_C",
        "Item_Weapon_VSS_C": "Item_Ammo_9mm_C",
        "Item_Weapon_vz61Skorpion_C": "Item_Ammo_9mm_C",
          
          
        "Item_Weapon_Grenade_C": "Throwable",
        "Item_Weapon_FlashBang_C": "Throwable",
        "Item_Weapon_Machete_C": "Throwable",
        "Item_Weapon_Cowbar_C": "Throwable",
        "Item_Weapon_Molotov_C": "Throwable",
        "Item_Weapon_Pan_C": "Throwable",
        "Item_Weapon_Sickle_C": "Throwable",
        "Item_Weapon_Apple_C": "Throwable",
        "Item_Weapon_SmokeBomb_C": "Throwable",
        "Item_Weapon_Snowball_C": "Throwable"
    }
    return diction[gun_name]
