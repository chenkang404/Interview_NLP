Thyroid_Ultrasound = {
    "report_information": {
        "report_id": "123456",  # 报告唯一标识
        "patient_id": "987654",  # 患者唯一标识
        "exam_date": "2024-12-25",  # 检查日期
        "exam_location": "甲状腺",  # 检查部位，如“甲状腺”
        "conclusion": "甲状腺双侧叶实性结节，TI-RADS-3级，左侧叶囊肿，TI-RADS-2级，建议随访复查",  # 结论
        "ultrasound_mode": "彩色多普勒"  # 超声模式相关信息
    },
    "organ_extraction": {
        "Organ_thyroid": {
            "description": "甲状腺形态大小正常，左侧叶探及低回声结节，右侧叶探及多个低回声结节",  # 甲状腺整体描述
            "is_normal": False,  # 甲状腺形态是否正常（根据结节描述）
            "size_cm": 5.0,  # 甲状腺大小，单位：厘米（假设值）
            "echotexture": "均匀",  # 回声特征，如“均匀”
            "echogenicity": "等回声",  # 回声强度，如“等回声”
            "margins": "清晰",  # 结节边界描述，如“清晰”
            "echogenic_foci": "无",  # 回声灶，如“无”
            "calcifications": "未见明显强回声",  # 钙化情况，如“未见明显强回声”
            "echo_condition": "未见异常",  # 回声情况，如“未见异常”
            "shape": "规则",  # 结节形状，如“规则”
            "morphology": "形态正常",  # 甲状腺形态描述，如“形态正常”
            "size_status": "正常",  # 大小状态，如“大小正常”
            "blood_flow": "部分血流信号",  # 血流情况，如“部分血流信号”
            "enhancement": "无",  # 强化情况，如“无”
            "posterior_echo": "无异常",  # 后方回声，如“无异常”
            "elasticity": "未描述",  # 质地弹性，如“未描述”
            "capsule": "未描述",  # 包膜情况，如“未描述”
            "surgical_history": "未描述"  # 手术情况，如“未描述”
        },
        "Organ_larynx": "未描述",  # 喉部描述
        "Organ_trachea": "未描述",  # 气管描述
        "Organ_cervical_lymph_nodes": "未探及异常增大淋巴结"  # 颈部淋巴结描述
    },
    "space_occupying_lesions": [
        {
            "lesion_id": "1",  # 占位病变唯一标识
            "lesion_type": "结节",  # 占位病变类型，如“结节”
            "lesion_subtype": "实性",  # 占位病变子类型，如“实性”
            "location": "左叶",  # 占位病变位置，如“左叶”
            "size_long_axis_cm": 2.5,  # 长轴尺寸，单位：厘米
            "size_short_axis_cm": 2.5,  # 短轴尺寸，单位：厘米
            "composition": "实性",  # 结节组成，如“实性”
            "echogenicity": "低回声",  # 回声特性，如“低回声”
            "margins": "清晰",  # 边缘描述，如“清晰”
            "calcifications": "无钙化",  # 钙化情况，如“无钙化”
            "vascularity": "无",  # 血流情况，如“无”
            "shape": "椭圆形",  # 形状，如“椭圆形”
            "morphology": "形态规则",  # 形态，如“形态规则”
            "aspect_ratio": "≤",  # 纵横比，如“≤”
            "number": 1,  # 数目，如“1”
            "suspected_diagnosis": "良性结节",  # 疑似诊断，如“良性结节”
            "surrounding_tissue": "周围无异常",  # 周围组织描述，如“周围无异常”
            "additional_features": "无囊性变"  # 其他特征描述，如“无囊性变”
        },
        {
            "lesion_id": "2",  # 占位病变唯一标识
            "lesion_type": "结节",  # 占位病变类型
            "lesion_subtype": "低回声",  # 占位病变子类型
            "location": "右叶",  # 结节位置
            "size_long_axis_cm": 7.0,  # 长轴尺寸
            "size_short_axis_cm": 4.0,  # 短轴尺寸
            "composition": "实性",  # 结节组成
            "echogenicity": "低回声",  # 低回声
            "margins": "清晰",  # 边界清晰
            "calcifications": "无钙化",  # 无钙化
            "vascularity": "丰富",  # 血流丰富
            "shape": "规则",  # 形状规则
            "morphology": "形态规则",  # 形态规则
            "aspect_ratio": "≤",  # 纵横比
            "number": 1,  # 数目
            "suspected_diagnosis": "良性结节",  # 疑似诊断
            "surrounding_tissue": "周围无异常",  # 周围组织描述
            "additional_features": "无囊性变"  # 无囊性变
        }
    ],
    "quantitative_metrics": {
        "thyroid_volume_ml": 15.0,  # 甲状腺体积，单位：毫升
        "nodule_count": 3,  # 结节数量
        "largest_nodule_size_cm": 7.0,  # 最大结节尺寸，单位：厘米
        "vascular_index": 0.5  # 血管指数
    },
    "lymph_nodes": {
        "lymph_node_condition": "未见异常增大淋巴结",  # 淋巴结情况，如“未见异常增大淋巴结”
        "activity": "未描述",  # 活动度，如“未描述”
        "cortex_medulla": "未描述",  # 皮髓质，如“未描述”
        "gate": "未描述"  # 淋巴门，如“未描述”
    },
    "diagnostic_opinion": {
        "accurate_diagnosis": "甲状腺双侧叶实性结节，TI-RADS-3级，左侧叶囊肿，TI-RADS-2级"  # 准确的诊断名称
    }
}

Pulmonary_CT = {
    "report_information": {
        "report_id": "NULL",
        "patient_id": "NULL",
        "exam_date": "NULL",
        "exam_location": "肺部",
        "conclusion": "双肺内少许微小斑点结节影，右肺中叶外侧小于0.2cm结节，肺门结构紊乱，纵隔内结构显示清晰，胸膜无增厚，建议定期复查、必要时进一步检查",
        "CDFI": "NULL"
    },
    "organ_extraction": {
        "Organ_aorta": "NULL",
        "Organ_aortic_arch": "NULL",
        "Organ_cardiac_shadow": "NULL",
        "Organ_trachea": "气管纵隔居中",
        "Organ_mediastinum": "纵隔内结构显示清晰",
        "Organ_costophrenic_angle": "NULL",
        "Organ_pulmonary_texture": "两肺纹理增强",
        "Organ_pulmonary_field": "透光度增强",
        "Organ_hilar_region": "肺门结构紊乱",
        "Organ_thoracic_cage": "胸廓对称",
        "Organ_pleura": "胸膜无增厚",
        "Organ_diaphragm_surface": "NULL",
        "Organ_skeleton": "NULL"
    },
    "space_occupying_lesions": [
        {
            "lesion_id": "ima19层右肺中叶外侧",
            "lesion_type": "结节",
            "lesion_subtype": "NULL",
            "location": "右肺中叶外侧",
            "size_long_axis_cm": 0.2,
            "size_short_axis_cm": "NULL",
            "density": "NULL",
            "shape": "NULL",
            "edge": "NULL",
            "number": "单发",
            "suspected_diagnosis": "NULL",
            "surrounding_tissue": "NULL",
            "contrast_enhancement": "NULL",
            "additional_features": "NULL"
        }
    ],
    "quantitative_metrics": {
        "lung_volume_L": "NULL",
        "lung_density_distribution": "NULL",
        "nodules_statistics": "结节：右肺中叶外侧小于0.2cm，双肺少许微小斑点结节影",
        "blood_vessels_distribution": "NULL"
    },
    "diagnostic_opinion": {
        "accurate_diagnosis": "NULL"
    }
}

Kidney_Abdominal_BUS = {
    "report_information": {
        "report_id": "NULL",
        "patient_id": "NULL",
        "exam_date": "NULL",
        "exam_location": "腹部B超",
        "conclusion": "双肾结石，双肾囊肿。",
        "CDFI": "肝牌双肾血流木见异常"
    },
    "organ_extraction": {
        "kidney_left": {
            "size_length_cm": 0.8,
            "size_width_cm": 0.8,
            "size_thickness_cm": "NULL",
            "echotexture": "囊性回声",
            "borders": "清晰",
            "renal_pelvis_size_cm": "NULL",
            "hydronephrosis_degree": "NULL",
            "perirenal_fat": "NULL",
            "cortical_thickness_cm": "NULL",
            "medullary_echo": "NULL",
            "adjacent_organs": "NULL"
        },
        "kidney_right": {
            "size_length_cm": 0.7,
            "size_width_cm": 0.6,
            "size_thickness_cm": "NULL",
            "echotexture": "囊性回声",
            "borders": "清晰",
            "renal_pelvis_size_cm": "NULL",
            "hydronephrosis_degree": "NULL",
            "perirenal_fat": "NULL",
            "cortical_thickness_cm": "NULL",
            "medullary_echo": "NULL",
            "adjacent_organs": "NULL"
        }
    },
    "kidney_lesions": {
        "masses": [
            {
                "lesion_id": "NULL",
                "side": "左",
                "location": "NULL",
                "size_cm": 0.5,
                "shape": "不规则形",
                "margins": "不规则",
                "echogenicity": "强回声",
                "posterior_features": "声影",
                "vascularity": "NULL",
                "suspected_diagnosis": "NULL",
                "additional_features": "NULL"
            },
            {
                "lesion_id": "NULL",
                "side": "右",
                "location": "NULL",
                "size_cm": 0.5,
                "shape": "不规则形",
                "margins": "不规则",
                "echogenicity": "强回声",
                "posterior_features": "声影",
                "vascularity": "NULL",
                "suspected_diagnosis": "NULL",
                "additional_features": "NULL"
            }
        ],
        "cysts": [
            {
                "cyst_id": "NULL",
                "side": "左",
                "location": "NULL",
                "size_cm": 0.8,
                "shape": "圆形",
                "margins": "清晰",
                "echogenicity": "强回声",
                "posterior_features": "透声",
                "vascularity": "NULL",
                "suspected_diagnosis": "单纯性囊肿",
                "additional_features": "光斑"
            },
            {
                "cyst_id": "NULL",
                "side": "右",
                "location": "NULL",
                "size_cm": 0.7,
                "shape": "圆形",
                "margins": "清晰",
                "echogenicity": "强回声",
                "posterior_features": "透声",
                "vascularity": "NULL",
                "suspected_diagnosis": "单纯性囊肿",
                "additional_features": "光斑"
            }
        ],
        "other_lesions": []
    },
    "lymph_nodes": [],
    "quantitative_metrics": {
        "kidney_left_volume_ml": "NULL",
        "kidney_right_volume_ml": "NULL",
        "lesions_volume_statistics": "NULL",
        "blood_vessels_distribution": "NULL"
    },
    "diagnostic_opinion": {
        "accurate_diagnosis": "双肾结石，双肾囊肿"
    }
}
 
Liver_Abdominal_BUS = {
    "report_information": {
        "report_id": "NULL",
        "patient_id": "NULL",
        "exam_date": "NULL",
        "exam_location": "腹部B超",
        "conclusion": "脂肪肝，肝囊肿。",
        "CDFI": "NULL"
    },
    "organ_extraction": {
        "liver": {
            "size_length_cm": "NULL",
            "size_width_cm": "NULL",
            "size_thickness_cm": "NULL",
            "echotexture": "前场细密，后场衰减",
            "surface": "NULL",
            "vascular_structures": "肝内血管尚清，走行尚清",
            "biliary_ducts": "NULL",
            "adjacent_organs": "NULL",
            "surrounding_tissues": "NULL"
        }
    },
    "liver_lesions": {
        "masses": [],
        "cysts": [
            {
                "cyst_id": "NULL",
                "side": "左",
                "location": "肝左叶",
                "size_cm": 0.7,
                "shape": "圆形",
                "margins": "清晰",
                "echogenicity": "无回声",
                "posterior_features": "后伴增强效应",
                "vascularity": "NULL",
                "suspected_diagnosis": "单纯性囊肿",
                "additional_features": "有包膜"
            }
        ],
        "other_lesions": []
    },
    "lymph_nodes": [],
    "quantitative_metrics": {
        "liver_volume_ml": "NULL",
        "nodules_volume_statistics": "NULL",
        "blood_vessels_distribution": "NULL"
    },
    "diagnostic_opinion": {
        "accurate_diagnosis": "脂肪肝，肝囊肿"
    }
}

Gallbladder_Abdominal_BUS = {
    "report_information": {
        "report_id": "NULL",
        "patient_id": "NULL",
        "exam_date": "NULL",
        "exam_location": "腹部B超",
        "conclusion": "胆囊强回声光团，考虑结石，胆囊等回声光团，考虑息肉。",
        "CDFI": "NULL"
    },
    "organ_extraction": {
        "gallbladder": {
            "size_length_cm": "NULL",
            "size_width_cm": "NULL",
            "wall_thickness_cm": "NULL",
            "wall_echogenicity": "粗糙",
            "wall_surface": "NULL",
            "pericholecystic_fluid": "NULL",
            "gallstones_present": True,
            "gallstones_count": 1,
            "gallstones_size_cm": 0.55,
            "polyps_present": True,
            "polyps_count": 1,
            "polyps_size_cm": 0.62,
            "sludge_present": "NULL",
            "sludge_description": "NULL",
            "sonographic_murphy_sign": "NULL",
            "adjacent_organs": "NULL"
        }
    },
    "gallbladder_lesions": {
        "masses": [],
        "polyps": [
            {
                "polyp_id": "NULL",
                "location": "胆囊",
                "size_cm": 0.62,
                "echogenicity": "等回声",
                "margins": "附着",
                "suspected_diagnosis": "良性",
                "additional_features": "NULL"
            }
        ],
        "other_lesions": [
            {
                "lesion_id": "NULL",
                "type": "胆结石",
                "location": "胆囊",
                "size_cm": 0.55,
                "shape": "光团",
                "margins": "强回声",
                "echogenicity": "强回声",
                "posterior_features": "NULL",
                "vascularity": "NULL",
                "suspected_diagnosis": "结石",
                "additional_features": "NULL"
            }
        ]
    },
    "lymph_nodes": [],
    "quantitative_metrics": {
        "gallbladder_volume_ml": "NULL",
        "lesions_volume_statistics": "NULL",
        "blood_vessels_distribution": "NULL"
    },
    "diagnostic_opinion": {
        "accurate_diagnosis": "胆囊结石，胆囊息肉"
    }
}

Pancreas_Abdominal_BUS = {
    "report_information": {
        "report_id": "NULL",
        "patient_id": "NULL",
        "exam_date": "NULL",
        "exam_location": "腹部B超",
        "conclusion": "胰腺大小形态正常，边缘规整，实质回声均匀，主胰管无扩张，未见明显异常。",
        "CDFI": "NULL"
    },
    "organ_extraction": {
        "pancreas": {
            "size_length_cm": "NULL",
            "size_width_cm": "NULL",
            "size_thickness_cm": "NULL",
            "echotexture": "均匀回声",
            "borders": "规整",
            "duct_visibility": "可见",
            "main_pancreatic_duct": "无扩张",
            "surrounding_tissues": "未见肿块",
            "adjacent_organs": "NULL"
        }
    },
    "pancreas_lesions": {
        "masses": [],
        "cysts": [],
        "other_lesions": []
    },
    "lymph_nodes": [],
    "quantitative_metrics": {
        "pancreas_volume_ml": "NULL",
        "nodules_volume_statistics": "NULL",
        "blood_vessels_distribution": "NULL"
    },
    "diagnostic_opinion": {
        "accurate_diagnosis": "胰腺正常"
    }
}

Spleen_Abdominal_BUS = {
    "report_information": {
        "report_id": "NULL",
        "patient_id": "NULL",
        "exam_date": "NULL",
        "exam_location": "腹部B超",
        "conclusion": "脾大小10.9×4.05cm回声均匀，脾门静脉无扩张，脾面积略大。",
        "CDFI": "NULL"
    },
    "organ_extraction": {
        "spleen": {
            "size_length_cm": 10.9,
            "size_width_cm": 4.05,
            "size_thickness_cm": "NULL",
            "echotexture": "均匀回声",
            "borders": "NULL",
            "hilum_visibility": "可见",
            "vascular_structures": "脾门静脉无扩张",
            "surrounding_tissues": "未见肿块",
            "adjacent_organs": "NULL"
        }
    },
    "spleen_lesions": {
        "masses": [],
        "cysts": [],
        "other_lesions": []
    },
    "lymph_nodes": [],
    "quantitative_metrics": {
        "spleen_volume_ml": "NULL",
        "nodules_volume_statistics": "NULL",
        "blood_vessels_distribution": "NULL"
    },
    "diagnostic_opinion": {
        "accurate_diagnosis": "脾脏略大"
    }
}

Uterus_Abdominal_BUS = {
    "report_information": {
        "report_id": "NULL",
        "patient_id": "NULL",
        "exam_date": "NULL",
        "exam_location": "腹部B超",
        "conclusion": "子宫体积缩小，轮廓光整，实质回声均匀，内膜不厚，子查壁面里多个解回声区，较大约35mm×34mm，宫颈见多个类医形无回声区，较大约为4mm×4mm，左附件显示不清，右附件显示不清。绝经后子宫，子宫肌瘤(多发)，宫颈囊肿(多发)。",
        "CDFI": "NULL"
    },
    "organ_extraction": {
        "uterus": {
            "position": "NULL",
            "anteversion_angle_deg": "NULL",
            "anteflexion_angle_deg": "NULL",
            "size_length_cm": "NULL",
            "size_width_cm": "NULL",
            "size_thickness_cm": "NULL",
            "echotexture": "均匀回声",
            "myometrium_echogenicity": "正常",
            "endometrium_thickness_cm": "NULL",
            "endometrium_echogenicity": "NULL",
            "myometrial_hyperplasia": "NULL",
            "fibroids_present": True,
            "fibroids_count": "多发",
            "fibroids_size_cm": "NULL",
            "polyps_present": "NULL",
            "polyps_count": "NULL",
            "polyps_size_cm": "NULL",
            "adenomyosis_present": "NULL",
            "adjacent_organs": "左附件显示不清，右附件显示不清"
        }
    },
    "uterus_lesions": {
        "fibroids": [],
        "polyps": [],
        "other_lesions": [
            {
                "lesion_id": "NULL",
                "type": "宫颈囊肿",
                "location": "宫颈",
                "size_cm": 0.4,
                "shape": "类医形",
                "margins": "光滑",
                "echogenicity": "无回声",
                "posterior_features": "NULL",
                "vascularity": "NULL",
                "suspected_diagnosis": "良性",
                "additional_features": "NULL"
            }
        ]
    },
    "quantitative_metrics": {
        "uterus_volume_ml": "NULL",
        "fibroids_volume_statistics": "子宫肌瘤(多发)",
        "polyps_volume_statistics": "NULL",
        "blood_vessels_distribution": "NULL"
    },
    "diagnostic_opinion": {
        "accurate_diagnosis": "子宫肌瘤(多发)，宫颈囊肿(多发)"
    }
}

Breast_Ultrasound = {
    "report_information": {
        "report_id": "NULL",
        "patient_id": "NULL",
        "exam_date": "NULL",
        "exam_location": "乳腺",
        "conclusion": "双侧乳房切面形态轮廓正常，腺体层回声增强增粗，结构稍紊乱，双侧乳腺导管未见扩张。左侧乳腺腺体内探及一低回声结节，大小约5.8mmx2.7mm，边界尚清，尚规则，内回声欠均匀。CDFI低回声结节周边及内部未见明显异常血流信号，乳腺腺体内未见明显异常彩色血流。双侧乳腺小叶增生，左侧乳腺低回声结节（增生结节），BI-RADS3级，BI-RADS0级影像学评估不完全，建议进一步评估。",
        "CDFI": "低回声结节周边及内部未见明显异常血流信号，乳腺腺体内未见明显异常彩色血流"
    },
    "organ_extraction": {
        "breast_left": {
            "size_cm": "NULL",
            "echotexture": "回声增强增粗，结构稍紊乱",
            "ducts": "未见扩张",
            "surrounding_tissues": "NULL"
        },
        "breast_right": {
            "size_cm": "NULL",
            "echotexture": "回声增强增粗，结构稍紊乱",
            "ducts": "未见扩张",
            "surrounding_tissues": "NULL"
        },
        "skin": "NULL",
        "nipple": "NULL",
        "axillary_region": "NULL"
    },
    "breast_lesions": {
        "masses": [
            {
                "lesion_id": "NULL",
                "side": "左",
                "location": "乳腺",
                "size_cm": 0.58,
                "shape": "不规则",
                "margins": "尚清",
                "echogenicity": "低回声",
                "posterior_features": "NULL",
                "vascularity": "未见明显异常血流",
                "suspected_diagnosis": "增生结节",
                "additional_features": "内回声欠均匀"
            }
        ],
        "cysts": [],
        "other_lesions": []
    },
    "lymph_nodes": [],
    "quantitative_metrics": {
        "breast_volume_left_ml": "NULL",
        "breast_volume_right_ml": "NULL",
        "masses_volume_statistics": "左乳腺低回声结节（5.8mmx2.7mm）",
        "cysts_volume_statistics": "NULL",
        "blood_vessels_distribution": "NULL"
    },
    "diagnostic_opinion": {
        "accurate_diagnosis": "左侧乳腺低回声结节（增生结节），BI-RADS3级，双侧乳腺小叶增生"
    }
}

Bladder_Urinary_Sys_ULTRASOUND = {
    "report_information": {
        "report_id": "NULL",
        "patient_id": "NULL",
        "exam_date": "NULL",
        "exam_location": "泌尿系统超声",
        "conclusion": "膀胱充盈良好，右侧输尿管下段、膀胱出口处探及等回声光团，向膀胱腔内突起，大小约7mm×5mm，边界清，内部回声欠均匀。CDFI示膀胱等回声团块周边及内部未见明显血流信号，其他各脏器未见异常血流信号。膀胱等回声区，性质待定，建议进一步检查。",
        "CDFI": "膀胱等回声团块周边及内部未见明显血流信号，其他各脏器未见异常血流信号"
    },
    "organ_extraction": {
        "bladder": {
            "volume_ml": "NULL",
            "wall_thickness_mm": "NULL",
            "echotexture": "均匀回声",
            "presence_of_diverticula": "NULL",
            "diverticula_count": "NULL",
            "diverticula_size_cm": "NULL",
            "presence_of_calculus": "NULL",
            "calculus_count": "NULL",
            "calculus_size_cm": "NULL",
            "presence_of_mass": "TRUE",
            "mass_size_cm": 0.7,
            "mass_characteristics": "边界清，内部回声欠均匀",
            "post_void_residual_volume_ml": "NULL",
            "bladder_shape": "NULL",
            "bladder_position": "NULL"
        }
    },
    "bladder_lesions": {
        "masses": [
            {
                "lesion_id": "NULL",
                "location": "右侧输尿管下段、膀胱出口处",
                "size_cm": 0.7,
                "shape": "光团",
                "boundary": "清晰",
                "echogenicity": "等回声",
                "posterior_features": "NULL",
                "vascularity": "无血流",
                "suspected_diagnosis": "待定",
                "additional_features": "内部回声欠均匀"
            }
        ]
    },
    "quantitative_metrics": {
        "bladder_volume_ml": "NULL",
        "post_void_residual_volume_ml": "NULL",
        "bladder_wall_thickness_statistics_mm": "NULL"
    },
    "diagnostic_opinion": {
        "accurate_diagnosis": "膀胱等回声团块，性质待定"
    }
}

Echocardiogram = {
    "report_information": {
        "report_id": "NULL",
        "patient_id": "NULL",
        "exam_date": "NULL",
        "exam_location": "超声心动图",
        "conclusion": "心脏各房室腔内径正常。房室间隔连续完整。各组瓣膜形态、回声未见异常。左室各段心肌厚度、动度及回声未见异常。左室收缩功能：LVEF:63%。",
        "recommendations": "NULL"
    },
    "echocardiogram_findings": {
        "chambers": {
            "left_atrium": {
                "size_cm": "NULL",
                "size_unit": "cm",
                "volume_ml": "NULL",
                "volume_unit": "ml",
                "wall_thickness_mm": "NULL",
                "wall_thickness_unit": "mm",
                "function": "正常"
            },
            "left_ventricle": {
                "size_cm": "NULL",
                "size_unit": "cm",
                "volume_ml": "NULL",
                "volume_unit": "ml",
                "wall_thickness_mm": "NULL",
                "wall_thickness_unit": "mm",
                "ejection_fraction_percent": 63.0,
                "fractional_shortening_percent": "NULL",
                "function": "正常"
            },
            "right_atrium": {
                "size_cm": "NULL",
                "size_unit": "cm",
                "volume_ml": "NULL",
                "volume_unit": "ml",
                "wall_thickness_mm": "NULL",
                "wall_thickness_unit": "mm",
                "function": "正常"
            },
            "right_ventricle": {
                "size_cm": "NULL",
                "size_unit": "cm",
                "volume_ml": "NULL",
                "volume_unit": "ml",
                "wall_thickness_mm": "NULL",
                "wall_thickness_unit": "mm",
                "function": "正常"
            }
        },
        "valves": {
            "mitral_valve": {
                "morphology": "正常",
                "regurgitation_grade": "NULL",
                "stenosis_grade": "NULL",
                "associated_features": "NULL"
            },
            "aortic_valve": {
                "morphology": "正常",
                "regurgitation_grade": "NULL",
                "stenosis_grade": "NULL",
                "associated_features": "NULL"
            },
            "tricuspid_valve": {
                "morphology": "正常",
                "regurgitation_grade": "NULL",
                "stenosis_grade": "NULL",
                "associated_features": "NULL"
            },
            "pulmonary_valve": {
                "morphology": "正常",
                "regurgitation_grade": "NULL",
                "stenosis_grade": "NULL",
                "associated_features": "NULL"
            }
        },
        "pericardium": {
            "effusion_present": "NULL",
            "effusion_volume_ml": "NULL",
            "effusion_characteristics": "NULL",
            "constrictive_pericarditis": "NULL"
        },
        "wall_motion": {
            "abnormalities_present": "NULL",
            "regions_with_abnormal_motion": "NULL",
            "description": "NULL"
        },
        "doppler_findings": {
            "mitral_inflow": {
                "e_velocity_cm_s": "NULL",
                "a_velocity_cm_s": "NULL",
                "e_a_ratio": "NULL",
                "deceleration_time_ms": "NULL"
            },
            "tricuspid_inflow": {
                "e_velocity_cm_s": "NULL",
                "a_velocity_cm_s": "NULL",
                "e_a_ratio": "NULL",
                "deceleration_time_ms": "NULL"
            },
            "aortic_outflow": {
                "velocity_cm_s": "NULL",
                "pressure_gradient_mmHg": "NULL"
            },
            "pulmonic_outflow": {
                "velocity_cm_s": "NULL",
                "pressure_gradient_mmHg": "NULL"
            }
        }
    },
    "quantitative_metrics": {
        "ejection_fraction_percent": 63.0,
        "fractional_shortening_percent": "NULL",
        "left_atrium_volume_ml": "NULL",
        "left_ventricle_volume_ml": "NULL",
        "right_atrium_volume_ml": "NULL",
        "right_ventricle_volume_ml": "NULL",
        "mitral_valve_area_cm2": "NULL",
        "aortic_valve_area_cm2": "NULL",
        "tricuspid_valve_area_cm2": "NULL",
        "pulmonary_valve_area_cm2": "NULL"
    },
    "diagnostic_opinion": {
        "accurate_diagnosis": "正常心脏结构与功能"
    }
}


organ_zh_2_ouput = {
    "肾脏腹部超声": Kidney_Abdominal_BUS,
    # "附件腹部超声": Attachments_Abdominal_BUS,
    # "霍尔特动态心电图": Holter_ECG,
    # "前列腺超声": Prostate_ULTRASOUND,
    "甲状腺超声": Thyroid_Ultrasound,
    # "静息心电图": Resting_ECG,
    "胰腺腹部超声": Pancreas_Abdominal_BUS,
    "肝脏腹部超声": Liver_Abdominal_BUS,
    "子宫腹部超声": Uterus_Abdominal_BUS,
    # "胸部X光": Chest_Xray,
    "超声心动图": Echocardiogram,
    # "肺功能测试": Pulmonary_Function_Test,
    "胆囊腹部超声": Gallbladder_Abdominal_BUS,
    "膀胱泌尿系统超声": Bladder_Urinary_Sys_ULTRASOUND,
    # "输尿管泌尿系统超声": Ureter_Urinary_Sys_ULTRASOUND,
    "乳腺超声": Breast_Ultrasound,
    "脾脏腹部超声": Spleen_Abdominal_BUS,
    "肺部CT": Pulmonary_CT
}

# organ_zh_2_ouput = {
#     "肾脏腹部超声": Kidney_Abdominal_BUS,
#     "附件腹部超声": Attachments_Abdominal_BUS,
#     "霍尔特动态心电图": Holter_ECG,
#     "前列腺超声": Prostate_ULTRASOUND,
#     "甲状腺超声": Thyroid_Ultrasound,
#     "静息心电图": Resting_ECG,
#     "胰腺腹部超声": Pancreas_Abdominal_BUS,
#     "肝脏腹部超声": Liver_Abdominal_BUS,
#     "子宫腹部超声": Uterus_Abdominal_BUS,
#     "胸部X光": Chest_Xray,
#     "超声心动图": Echocardiogram,
#     "肺功能测试": Pulmonary_Function_Test,
#     "胆囊腹部超声": Gallbladder_Abdominal_BUS,
#     "膀胱泌尿系统超声": Bladder_Urinary_Sys_ULTRASOUND,
#     "输尿管泌尿系统超声": Ureter_Urinary_Sys_ULTRASOUND,
#     "乳腺超声": Breast_Ultrasound,
#     "脾脏腹部超声": Spleen_Abdominal_BUS,
#     "肺部CT": Pulmonary_CT
# }